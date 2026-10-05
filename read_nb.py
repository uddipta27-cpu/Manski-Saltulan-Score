import json

with open(r'e:\mental helath project\Untitled5.ipynb', encoding='utf-8') as f:
    nb = json.load(f)

for i, c in enumerate(nb['cells']):
    print(f"--- Cell {i} ({c['cell_type']}) ---")
    print(''.join(c['source']))
    print()
