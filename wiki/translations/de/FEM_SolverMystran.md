---
 GuiCommand:
   Name: FEM SolverMystran
   MenuLocation: Solve , Solver Mystran
   Workbenches: FEM_Workbench
   Shortcut: **S** **M**
   Version: 0.20
   SeeAlso: FEM_tutorial
---

# FEM SolverMystran/de



## Beschreibung

The [SolverMystran](FEM_SolverMystran.md) command enables usage of the [MYSTRAN](https://www.mystran.com) solver. It may be used for:

1.  Setting analysis parameters.
2.  Selecting working directory.
3.  Running the MYSTRAN solver.

## Installation

You can get the Mystran Windows executable [here](https://github.com/MYSTRANsolver/MYSTRAN%20Releases). Put the folder where you place **Mystran.exe** in the Windows\'s PATH variable.

The [SolverMystran](FEM_SolverMystran.md) also needs two other packages:

-   [pyNastran](https://github.com/SteveDoyle2/pyNastran) - to write out case file.
-   [hfcMystran](https://github.com/ceanwang/hfcMystran) - to read in Mystran\'s NEU result file.

pyNastran can be installed through pip:

1.  Open a Command terminal in your **FreeCAD\bin** folder.
2.  Enter: {{Incode|python -m pip install pyNastran}}
3.  It will be installed in the **FreeCAD\bin\lib\site-packages** folder.

hfcMystran can be downloaded from its github site as a zip file. Unzip it and place it in the **FreeCAD\Mod** folder.

## Quick test 

After installation you can select **Utilities → Open FEM examples** in the FEM Workbench. Under **Solver → Mystran** you can find some working Mystran examples.



## Anwendung

ToDo

## File function 

Under Mod\\Fem\\femsolver\\mystran, there are these files:


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

The function of each file are:

writer.py - main control file


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

BDF() - Create empty case file.


```python
$pyNastran: version=msc
$pyNastran: punch=False
$pyNastran: encoding=utf-8
$pyNastran: nnodes=0
$pyNastran: nelements=0
ENDDATA
```

add_solver_control.py - Adding EXECUTIVE CONTROL DECK and CASE CONTROL DECK.


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

add_femelement_geometry.py - Adding GRID cards

add_mesh.py - Adding element cards

add_femelement_material.py - Adding MAT1 card

add_con_fixed.py - Adding SPCADD and SPC1 cards

add_con_displacement.py - Adding SPCADD and SPC1 cards

add_con_force.py - Adding FORCE cards





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM SolverMystran/de
