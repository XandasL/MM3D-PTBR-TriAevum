#!/usr/bin/env python3
"""Gera as especificações de mensagens do Forge sem arquivos da ROM."""
import argparse
import json
import pathlib
import re
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parents[1]
UPSTREAM = "https://raw.githubusercontent.com/coccofresco/TriAevum/672d13f15cb336bc7651c861d23cf45924a9f936/titles/mm3d/dekui/setup/reviewed-dialogue.json"

def load_json(source):
    if source.startswith(("https://", "http://")):
        with urllib.request.urlopen(source, timeout=25) as response:
            return json.load(response)
    with open(source, encoding="utf-8") as handle:
        return json.load(handle)

def build(spec, catalog, plan):
    languages = {"en", "de", "fr", "es", "it"}
    if set(spec) != languages:
        raise ValueError("O JSON base precisa conter os cinco idiomas europeus.")
    if catalog.get("format") != "mm3d_ptbr_catalog_v1":
        raise ValueError("Formato de catálogo desconhecido.")
    reserved = set(plan["metadata_ids"]) | set(plan["literal_ids"]) | set(plan["special_literals"])
    edits = spec["en"]["edits"]
    by_slot = {(e["id"].lower(), e.get("segment"), e.get("section")): e for e in edits}
    slots = set()
    for e in catalog["edits"]:
        id_ = e["id"].lower()
        if not re.fullmatch(r"[0-9a-f]{4}", id_):
            raise ValueError("ID inválido: " + repr(id_))
        if id_ in reserved:
            raise ValueError("Mensagem reservada pelo sistema de preços: " + id_)
        if not isinstance(e.get("text"), str) or not e["text"] or "\\x00" in e["text"] or "\\x7f" in e["text"]:
            raise ValueError("Texto inválido: " + id_)
        slot = (id_, e.get("segment"), e.get("section"))
        if slot in slots:
            raise ValueError("Entrada PT-BR repetida: " + id_)
        slots.add(slot)
        old = by_slot.get(slot)
        if old is not None:
            if old != e:
                raise ValueError("Regra existente diferente: " + id_)
        else:
            # Outras regras no mesmo ID exigem revisão manual de sobreposição.
            if any(r["id"].lower() == id_ for r in edits):
                raise ValueError("Regra existente no mesmo ID: " + id_)
            edits.append(dict(e))
            by_slot[slot] = e
    return spec

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base", default=UPSTREAM, help="Especificação oficial JSON ou caminho local (não modificado)")
    parser.add_argument("--catalogo", default=str(ROOT / "catalogo" / "ptbr.json"))
    parser.add_argument("--precos", default=str(ROOT / "referencias" / "price-plan.json"))
    parser.add_argument("--saida", default=str(ROOT / "distribuicao" / "mm3d-message-specs.json"))
    args = parser.parse_args()
    result = build(load_json(args.base), load_json(args.catalogo), load_json(args.precos))
    path = pathlib.Path(args.saida)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Gerado: {path} ({len(load_json(args.catalogo)['edits'])} entradas PT-BR)")

if __name__ == "__main__":
    main()
