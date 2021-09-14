---
- GuiCommand:/ru
   Name:FEM ConstraintSelfWeight
   Name/ru:FEM ConstraintSelfWeight
   MenuLocation:FEM → Constraint self weight
   Workbenches:[FEM](FEM_Workbench/ru.md)
   Shortcut:C,W
   SeeAlso:[FEM tutorial](FEM_tutorial/ru.md)
---


</div>

## Description

Constraint self weight defines gravity acceleration 9,81 m/s\^2 acting on the whole model in the prescribed direction.

## Usage

1.  There are several ways to invoke the command:
    -   Press the **<img src="images/FEM_ConstraintSelfWeight.svg" width=16px> [FEM ConstraintSelfWeight](FEM_ConstraintSelfWeight.md)** button.
    -   Select the **Model → Mechanical Constraints → <img src="images/FEM_ConstraintSelfWeight.svg" width=16px> Constraint self weight** option from the menu.
2.  You can modify the direction of gravitation by changing its vector coordinates in the property bar of newly created ConstraintSelfWeight object.

## Scripting

**New object** 
```python
import ObjectsFem
ObjectsFem.makeConstraintSelfWeight( name )
```

**Add object to the analysis named Analysis** 
```python
App.ActiveDocument.Analysis.Member = App.ActiveDocument.Analysis.Member + [ (object) ]
```

**Example:** 
```python
import ObjectsFem
selfweight_obj = ObjectsFem.makeConstraintSelfWeight( 'MySelfWeightObject' )
App.ActiveDocument.Analysis.Member = App.ActiveDocument.Analysis.Member + [selfweight_obj]

```

## Solver CalculiX 

### Limitations

-   You need to modify .inp file to edit gravity acceleration.
-   Self weight is applied to the element set Eall means to the whole model.

### Editing CalculiX input file 

Acceleration constant can be edited by hand modification after generating CalculiX input file.

Example of lines in .inp file: 
```python
*DLOAD
Eall,GRAV,9810,0.0,0.0,-1.0
``` where 9810 is gravity acceleration magnitude in \[mm/s\^2\], and 0,0,-1 is direction vector.

## Solver Z88 

-   not implemented in Z88 solver (March 2017)





{{FEM Tools navi

}}  
