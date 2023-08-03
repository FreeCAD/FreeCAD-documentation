---
 GuiCommand:
   Name: Arch Check
   Workbenches: Arch_Workbench/ro
   MenuLocation: Arch , Utilities , Check
   SeeAlso: Arch CloseHoles
---

# Arch Check/ro


</div>



## Descriere


<div class="mw-translate-fuzzy">

Acest instrument verifică documentul curent sau obiectele selectate pentru obiecte non-solide [Part](Part_Workbench.md) sau [Arch](Arch_Workbench.md) care ar putea crea probleme, deoarece cele mai multe operații ale modulului Arch necesită obiecte solide.


</div>




<div class="mw-translate-fuzzy">

## Cum se folosește 


</div>


<div class="mw-translate-fuzzy">

1.  Apăsați **<img src="images/Arch_Check.png" width=16px> '''Check'''** entry in Arch → Utilities menu


</div>




<div class="mw-translate-fuzzy">

## Scrip-Programare 


</div>


**See also:**

[Arch API](Arch_API.md) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).


<div class="mw-translate-fuzzy">

Acest instrument poate fi utilizat în [macros](macros.md) și din consola Python utilizând următoarea funcție:


</div>


```python
list_bad = check(objectslist, includehidden=False)
```


<div class="mw-translate-fuzzy">

verifică dacă obiectele date conțin numai solide


</div>

Example:


```python
import FreeCAD, Draft, Arch

p1 = FreeCAD.Vector(0, 0, 0)
p2 = FreeCAD.Vector(2000, 0, 0)
baseline = Draft.makeLine(p1, p2)
Wall1 = Arch.makeWall(baseline, length=None, width=150, height=2000)
FreeCAD.ActiveDocument.recompute()

Wall2 = Arch.makeWall(None, length=2000, width=200, height=1000)
FreeCAD.ActiveDocument.recompute()

Circle = Draft.makeCircle(450)
Wire = Draft.makeWire([FreeCAD.Vector(1000, 0, 0), FreeCAD.Vector(1500, 1000, 0), FreeCAD.Vector(2500, -1000, 0)])

list_bad = Arch.check([Wall1, Wall2, Circle, Wire], includehidden=True)
print(list_bad)
```


<div class="mw-translate-fuzzy">


{{docnav/ro|[Merge Walls](Arch_MergeWalls.md)|[Ifc Explorer](Arch_IfcExplorer.md)|[Arch](Arch_Workbench.md)|IconL=Arch_MergeWalls.svg |IconC=Workbench_Arch.svg |IconR=Arch_IfcExplorer.png}}


</div>



---
⏵ [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch Check/ro
