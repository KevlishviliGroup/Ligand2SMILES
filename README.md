
<img width="6912" height="3456" alt="from Ligand2SMILES" src="https://github.com/user-attachments/assets/524d343c-77c6-4622-9899-81cc33d9b27e" />

# Ligand2SMILES

A lightweight Python module for looking up SMILES strings from compound and ligand names.
Built from Wikidata (P2017/P233) and PubChem, with a curated list of phosphine ligands
including the full Buchwald monophosphine family, bisphosphines, NHC ligands, and more.

## Installation

```
pip install ligand2smiles
```

Or install the latest version straight from GitHub:

```
pip install git+https://github.com/KevlishviliGroup/Ligand2SMILES.git
```

Or from a local clone:

```
git clone https://github.com/KevlishviliGroup/Ligand2SMILES
cd Ligand2SMILES
pip install .
```

Requires Python 3.9+. No dependencies beyond the Python standard library. The lookup database is included, so no setup or scraping is required.

All entries are validated through RDKit and cross-checked against source molecular weights (entries with a discrepancy of ≥1 Da were removed) before inclusion in the database.


## Usage

### Exact name lookup

```python
from Ligand2SMILES import name_to_smiles

smiles = name_to_smiles("XPhos")
# 'CC(C)C1=CC(=C(C(=C1)C(C)C)...'

smiles = name_to_smiles("triphenylphosphine")
# 'C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3'

smiles = name_to_smiles("unknown")
# None
```

### Partial name search

```python
from Ligand2SMILES import search

results = search("phos")
# [{'name': 'XPhos', 'smiles': '...'}, {'name': 'SPhos', 'smiles': '...'}, ...]
```

### List all available names

```python
from Ligand2SMILES import available_names

names = available_names()
# ['1,10-phenanthroline', 'BINAP', 'BrettPhos', 'XPhos', ...]
```
### Fuzzy search 

```python 
from Ligand2SMILES import fuzzy_search

fuzzy_search("xphos")
# [{'name': 'XPhos', 'smiles': '...', 'score': 1.0}]

fuzzy_search("triphenylphospine")  # typo
# [{'name': 'triphenylphosphine', 'smiles': '...', 'score': 0.97}]

fuzzy_search("j-Pr")  # OCR error for i-Pr
# returns closest phosphine matches
```

## Coverage

~12000+ compounds including:
- Buchwald monophosphines (XPhos, SPhos, RuPhos, BrettPhos, DavePhos, JohnPhos, ...)
- Bisphosphines (BINAP, DPPF, dppe, Xantphos, SEGPHOS, ...)
- NHC ligands (IMes, IPr, SIMes, SIPr, ...)
- SelectPhos family (SelectPhos, CySelectPhos, PhSelectPhos)
- Nitrogen donors (1,10-phenanthroline, 2,2-bipyridine, ...)
- General compounds from Wikidata

## Data sources

- **Wikidata**: SPARQL queries for P2017 (isomeric SMILES) and P233 (canonical SMILES)
- **PubChem**: CAS number and systematic name lookups for specialty phosphine ligands not in Wikidata

Found something wrong?
Let me know here: https://forms.gle/jbzANwcuArx13yis5

Thank you!
