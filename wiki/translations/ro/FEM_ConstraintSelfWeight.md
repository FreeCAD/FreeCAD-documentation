# FEM ConstraintSelfWeight/ro
---
- GuiCommand:/ro   Name:FEM ConstraintSelfWeight   Name/ro:FEM ConstraintSelfWeight   MenuLocation:Model → Mechanical Constraints → Constraint self weight   |Workbenches:[Shortcut:C,W   SeeAlso:[[FEM_tutorial/ro|FEM tutorial](FEM_Workbench/ro___FEM]].md)---


</div>

## Descriere

Constrângerea greutății proprii este definită de către accelerația gravitațională de 9,81 m / s \^ 2 care acționează asupra întregului model în direcția prescrisă.


<div class="mw-translate-fuzzy">

## Cum se folosește 


</div>


<div class="mw-translate-fuzzy">

1.  Click pe <img alt="" src=images/FEM_ConstraintSelfWeight.png  style="width:32px;"> sau alegeți **Model** → **Mechanical Constraints** → **<img src="images/FEM_ConstraintSelfWeight.png" width=32px> Constraint self weight** din meniul de sus sau apăsați tastele **C** apoi **W**.
2.  Puteți modifica direcția gravitației schimbând coordonatele sale vectoriale în bara de proprietăți a obiectului nou creat ConstraintSelfWeight.


</div>

## Script


<div class="mw-translate-fuzzy">

-   obiect nou


</div>


```python
import ObjectsFem
ObjectsFem.makeConstraintSelfWeight(name)
```


<div class="mw-translate-fuzzy">

-   adăugați obiectul la analiza numită Analysis


</div>


```python
App.ActiveDocument.Analysis.Member = App.ActiveDocument.Analysis.Member + [(object)]
```


<div class="mw-translate-fuzzy">

-   examplu:


</div>


```python
import ObjectsFem
selfweight_obj = ObjectsFem.makeConstraintSelfWeight("MySelfWeightObject")
App.ActiveDocument.Analysis.Member = App.ActiveDocument.Analysis.Member + [selfweight_obj]
```

## Solver CalculiX 

### Limitations


<div class="mw-translate-fuzzy">

## Solver CalculiX 

### Limite

-   Trebuie să modificați fișierul .inp pentru a edita accelerația gravitațională.
-   Gerutatea proprie este aplicată elemetului set Eall înseamnă întreg modelul .


</div>

### Editing CalculiX input file 


<div class="mw-translate-fuzzy">

### Editing CalculiX input file 

Accelerarea constantă poate fi modificată prin modificarea manuală după generarea fișierului de intrare CalculiX.


</div>


<div class="mw-translate-fuzzy">

Example of lines in .inp file: 
```python
*DLOAD
Eall,GRAV,9810,0.0,0.0,-1.0
``` where 9810 is gravity acceleration in \[mm/s\^2\]


</div>


```python
*DLOAD
Eall,GRAV,9810,0.0,0.0,-1.0
```

where 9810 is gravity acceleration magnitude in \[mm/s\^2\], and 0,0,-1 is direction vector.

## Solver Z88 


<div class="mw-translate-fuzzy">

## Rezolvitorul Z88 

-   nu este implementat în rezolvitorul Z88 (March 2017)


</div>





{{FEM Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintSelfWeight/ro
