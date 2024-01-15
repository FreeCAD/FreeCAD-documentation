---
 GuiCommand:
   Name: FEM SolverMystran
   Name/fr: FEM Solveur Mystran
   MenuLocation: Résolution , Solveur Mystran
   Workbenches: FEM_Workbench/fr
   Shortcut: **S** **M**
   Version: 0.20
   SeeAlso: FEM_tutorial/fr
---

# FEM SolverMystran/fr

## Description

La commande [Solveur Mystran](FEM_SolverMystran/fr.md) permet d\'utiliser le solveur [MYSTRAN](https://www.mystran.com). Il peut être utilisé pour :

1.  Définir les paramètres d\'analyse.
2.  Sélectionner le répertoire de travail.
3.  Exécuter le solveur MYSTRAN.

## Installation

Vous pouvez obtenir l\'exécutable Windows Mystran [ici](https://github.com/MYSTRANsolver/MYSTRAN%20Releases). Placez le dossier où vous avez placé **Mystran.exe** dans la variable PATH de Windows.

Le [Solveur Mystran](FEM_SolverMystran/fr.md) a également besoin de deux autres paquets :

-   [pyNastran](https://github.com/SteveDoyle2/pyNastran) - pour écrire le fichier de cas.
-   [hfcMystran](https://github.com/ceanwang/hfcMystran) - pour lire le fichier de résultats NEU de Mystran.

pyNastran peut être installé via pip :

1.  Ouvrez un terminal de commande dans votre dossier **FreeCAD\bin**.
2.  Entrez : {{Incode|python -m pip install pyNastran}}
3.  Il sera installé dans le dossier **FreeCAD\bin\lib\site-packages**.

hfcMystran peut être téléchargé depuis son site github sous forme de fichier zip. Décompressez-le et placez-le dans le dossier **FreeCAD\Mod**.



## Test rapide 

Après l\'installation, vous pouvez sélectionner **Utilitaires → Ouvrir des exemples de l'atelier FEM** dans l\'atelier FEM. Sous **Solveur → Mystran**, vous pouvez trouver des exemples Mystran fonctionnels.



## Utilisation

À faire



## Fonction du fichier 

Sous Mod\\Fem\\femsolver\\mystran, il y a ces fichiers :


```python
add_con_displacement.py
add_con_fixed.py
add_con_force.py
add_femelement_geometry.py
add_femelement_material.py
add_mesh.py
add_solver_control.py
writer.py
solver.py
tasks.py
```

Les fonctions de chaque fichier sont les suivantes :

writer.py - Fichier de contrôle principal


```python
model = BDF()
model = add_solver_control.add_solver_control(pynasf, model, self)
model = add_femelement_geometry.add_femelement_geometry(pynasf, model, self)
model = add_mesh.add_mesh(pynasf, model, self)
model = add_femelement_material.add_femelement_material(pynasf, model, self)
model = add_con_fixed.add_con_fixed(pynasf, model, self)
model = add_con_displacement.add_con_displacement(pynasf, model, self)
model = add_con_force.add_con_force(pynasf, model, self)
```

BDF() - Crée un fichier de cas vide.


```python
$pyNastran: version=msc
$pyNastran: punch=False
$pyNastran: encoding=utf-8
$pyNastran: nnodes=0
$pyNastran: nelements=0
ENDDATA
```

add_solver_control.py - Ajout du DECK DE CONTRÔLE EXÉCUTIF et du DECK DE CONTRÔLE DE CASE.


```python
$EXECUTIVE CONTROL DECK
SOL 101
CEND
$CASE CONTROL DECK
ECHO = NONE
TITLE = pyNastran for generating solverinput for for Mystran
SUBCASE 1
    DISPLACEMENT(SORT1,REAL) = ALL
    LOAD = 1
    SPC = 1
    SPCFORCES(SORT1,REAL) = ALL
    STRESS(SORT1,REAL,VONMISES,BILIN) = ALL
    SUBTITLE = Default
BEGIN BULK
$PARAMS
PARAM       POST      -1
```

add_femelement_geometry.py - Ajout de jeux de paramètres GRID

add_mesh.py - Ajout de jeux de paramètres d\'éléments

add_femelement_material.py - Ajout du jeu de paramètres MAT1

add_con_fixed.py - Ajout des jeux de paramètres SPCADD et SPC1

add_con_displacement.py - Ajout des jeux de paramètres SPCADD et SPC1

add_con_force.py - Ajout de jeux de paramètres FORCE





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM SolverMystran/fr
