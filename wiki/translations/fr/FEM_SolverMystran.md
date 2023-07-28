---
- GuiCommand:/fr
   Name:FEM SolverMystran
   Name/fr:FEM Solveur Mystran
   MenuLocation:Résolution → Solveur Mystran
   Workbenches:[FEM](FEM_Workbench/fr.md)
   Shortcut:**S** **M**
   Version:0.20
   SeeAlso:[FEM Tutoriel](FEM_tutorial/fr.md)
---

# FEM SolverMystran/fr

## Description

La commande [Solveur Mystran](FEM_SolverMystran/fr.md) permet d\'utiliser le solveur [MYSTRAN](https://www.mystran.com). Il peut être utilisé pour :

1.  Définir les paramètres d\'analyse
2.  Sélectionner le répertoire de travail
3.  Exécuter le solveur MYSTRAN



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

add_femelement_geometry.py - Ajout de cartes GRID

add_mesh.py - Ajout de cartes d\'éléments

add_femelement_material.py - Ajout de la carte MAT1

add_con_fixed.py - Ajout des cartes SPCADD et SPC1

add_con_displacement.py - Ajout des cartes SPCADD et SPC1

add_con_force.py - Ajout de cartes FORCE





{{FEM Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM SolverMystran/fr
