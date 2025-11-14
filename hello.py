from rdkit import Chem
from rdkit.Chem import AllChem, Draw
from rdkit.Chem.Draw import rdMolDraw2D

# SMILES
smiles_list = {
    'Hydrolyzed A-187': 'O[Si](O)(O)CCCOCC1CO1',
    'Diol form': 'OCC(O)COCCC[Si](O)(O)O',
    'Hybrid': 'CC1(C)CC(N=C=O)CC(C)(CNC(=O)OCC(O)COCCCO[Si](O)(O)O)C1'
}

mols = {}
for name, smi in smiles_list.items():
    mol = Chem.MolFromSmiles(smi)
    mol = Chem.AddHs(mol)  # Добавляем H для реализма
    AllChem.EmbedMolecule(mol, randomSeed=42)
    AllChem.MMFFOptimizeMolecule(mol)
    mols[name] = mol
    canon_smi = Chem.MolToSmiles(mol, canonical=True)
    print(f"{name}: {canon_smi}")
    # Сохраните PDB
    with open(f"{name.replace(' ', '_')}.pdb", 'w') as f:
        f.write(Chem.MolToPDBBlock(mol))

# 2D-изображения
img = Draw.MolsToGridImage(list(mols.values()), legends=list(mols.keys()), molsPerRow=3)
img.save('models_2D.jpg')

# 3D в Jupyter (nglview)
# import nglview as nv
# for name, mol in mols.items():
#     view = nv.show_rdkit(mol)
#     view.add_representation('ball+stick')
#     view