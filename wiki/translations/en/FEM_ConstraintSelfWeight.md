---
 GuiCommand:
   Name: FEM ConstraintSelfWeight
   MenuLocation: Model , Mechanical boundary conditions and loads , Gravity load
   Workbenches: FEM_Workbench
   SeeAlso: FEM_tutorial
---

# FEM ConstraintSelfWeight/en

## Description

Defines a gravity acceleration of 9,81 m/s\^2 acting on the whole model in the prescribed direction.

## Usage

1.  There are several ways to invoke the command:
    -   Press the **<img src="images/FEM_ConstraintSelfWeight.svg" width=16px> [Gravity load](FEM_ConstraintSelfWeight.md)** button.
    -   Select the **Model → Mechanical boundary conditions and loads → <img src="images/FEM_ConstraintSelfWeight.svg" width=16px> Gravity load** option from the menu.
2.  You can modify the direction of gravity load by changing its vector coordinates in the property bar of the newly created ConstraintSelfWeight object.

## Scripting

New object:


```python
import ObjectsFem
ObjectsFem.makeConstraintSelfWeight(name)
```

Add object to the analysis named Analysis:


```python
App.ActiveDocument.Analysis.Member = App.ActiveDocument.Analysis.Member + [(object)]
```

Example:


```python
import ObjectsFem
selfweight_obj = ObjectsFem.makeConstraintSelfWeight("MySelfWeightObject")
App.ActiveDocument.Analysis.Member = App.ActiveDocument.Analysis.Member + [selfweight_obj]
```

## Solver CalculiX 

### Limitations

-   You need to modify the .inp file to edit gravity acceleration.
-   Self-weight is applied to the element set Eall which includes the whole model.

### Editing CalculiX input file 

The acceleration constant can be manually edited after generating the CalculiX input file.

Example of lines in the .inp file:


```python
*DLOAD
Eall,GRAV,9810,0.0,0.0,-1.0
```

where 9810 is a gravity acceleration magnitude in \[mm/s\^2\], and 0,0,-1 is the direction vector. The value can be set as a multiple of standard gravity acceleration to simulate loading of e.g. 4g.

## Solver Z88 

-   Currently, not implemented in the Z88 solver.





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintSelfWeight/en
