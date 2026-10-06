import json
import os
from typing import Optional
from difflib import SequenceMatcher

_DATA_PATH = os.path.join(os.path.dirname(__file__), "ligand_list.json")

def _load():
    with open(_DATA_PATH) as f:
        data = json.load(f)
    if isinstance(data, dict):
        return {k.lower(): v for k, v in data.items()}
    return {entry["name"].lower(): entry["smiles"] for entry in data if entry.get("name") and entry.get("smiles")}

_LOOKUP = _load()

def name_to_smiles(name: str) -> Optional[str]:
  
    return _LOOKUP.get(name.strip().lower())


def search(query: str) -> list:
 
    query = query.strip().lower()
    with open(_DATA_PATH) as f:
        data = json.load(f)
    if isinstance(data, dict):
        return [{"name": k, "smiles": v} for k, v in data.items() if query in k.lower()]
    return [
        {"name": e["name"], "smiles": e["smiles"]}
        for e in data
        if e.get("name") and e.get("smiles") and query in e["name"].lower()
    ]


def fuzzy_search(name: str, threshold: float = 0.6, top_n: int = 5) -> list:
  
    query = name.strip().lower()
    results = []

    for key, smiles in _LOOKUP.items():
        score = SequenceMatcher(None, query, key).ratio()
        if score >= threshold:
            results.append({"name": key, "smiles": smiles, "score": round(score, 3)})

    results.sort(key=lambda x: x["score"], reverse=True)
    return results[:top_n]


def available_names() -> list:
  
    with open(_DATA_PATH) as f:
        data = json.load(f)
    if isinstance(data, dict):
        return sorted(data.keys())
    return sorted(e["name"] for e in data if e.get("name"))
