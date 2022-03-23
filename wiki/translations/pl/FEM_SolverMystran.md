---
- GuiCommand:
   Name:FEM SolverMystran
   MenuLocation:Solve → Solver Mystran
   Workbenches:[FEM](FEM_Workbench.md)
   Shortcut:**S** **M**
   Version:0.20
   SeeAlso:[FEM tutorial](FEM_tutorial.md)
---

# FEM SolverMystran/pl

## Description

[SolverMystran](FEM_SolverMystran.md) enables usage of the [MYSTRAN](https://www.mystran.com) solver. It may be used for:

1.  Setting analysis parameters
2.  Selecting working directory
3.  Running the MYSTRAN solver

## Usage

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

add\_solver\_control.py - Adding EXECUTIVE CONTROL DECK and CASE CONTROL DECK.


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

add\_femelement\_geometry.py - Adding GRID cards

add\_mesh.py - Adding element cards

add\_femelement\_material.py - Adding MAT1 card

add\_con\_fixed.py - Adding SPCADD and SPC1 cards

add\_con\_displacement.py - Adding SPCADD and SPC1 cards

add\_con\_force.py - Adding FORCE cards





{{FEM Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM SolverMystran/pl
