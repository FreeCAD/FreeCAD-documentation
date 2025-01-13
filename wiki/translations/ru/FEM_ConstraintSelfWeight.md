---
 GuiCommand:
   Name: FEM ConstraintSelfWeight
   Name/ru: FEM ConstraintSelfWeight
   MenuLocation: FEM , Constraint self weight
   Workbenches: FEM_Workbench/ru
   Shortcut: C,W
   SeeAlso: FEM_tutorial/ru
---

# FEM ConstraintSelfWeight/ru


</div>



## Описание

Defines a gravity acceleration acting on the whole model in the prescribed direction.


{{VersionMinus|0.21}}

: The acceleration has a fixed value of 9.81 m/s\^2.



## Применение

1.  There are several ways to invoke the command:
    -   Press the **<img src="images/FEM_ConstraintSelfWeight.svg" width=16px> [Gravity load](FEM_ConstraintSelfWeight.md)** button.
    -   Select the **Model → Mechanical boundary conditions and loads → <img src="images/FEM_ConstraintSelfWeight.svg" width=16px> Gravity load** option from the menu.

2.  A ConstraintSelfWeight object is created.

3.  
    <small>(v1.0)</small> : Optionally change its **Gravity Acceleration** property.

4.  Optionally change its **Gravity Direction** property.



## Программирование

New object:


```python
import ObjectsFem
ObjectsFem.makeConstraintSelfWeight(name)
```

Add object to the analysis named Analysis:


```python
App.ActiveDocument.Analysis.Member = App.ActiveDocument.Analysis.Member + [(object)]
```

Пример:


```python
import ObjectsFem
selfweight_obj = ObjectsFem.makeConstraintSelfWeight("MySelfWeightObject")
App.ActiveDocument.Analysis.Member = App.ActiveDocument.Analysis.Member + [selfweight_obj]
```



## Решатель CalculiX 

### Limitations

-    {{VersionMinus|0.21}}: You need to modify the .inp file to edit gravity acceleration.

-   Self-weight is applied to the element set Eall which includes the whole model.

### Editing CalculiX input file 

The acceleration constant can be manually edited after generating the CalculiX input file.

Example of lines in the .inp file:


```python
*DLOAD
Eall,GRAV,9810,0.0,0.0,-1.0
```

where 9810 is a gravity acceleration magnitude in \[mm/s\^2\], and 0,0,-1 is the direction vector. The value can be set as a multiple of standard gravity acceleration to simulate loading of e.g. 4g.



## Решатель Z88 

-   Currently, not implemented in the Z88 solver.





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintSelfWeight/ru
