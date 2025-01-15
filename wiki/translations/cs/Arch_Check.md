# Arch Check/cs
---
 GuiCommand:   Name: Arch Check   Name/cs: Arch Check   Workbenches: Arch_Workbench/cs   Arch---


</div>



## Popis


<div class="mw-translate-fuzzy">

Tento nástroj kontroluje daný dokument nebo jen vybrané objekty na objekty které nejsou tělesy v [Modulu Díl](Part_Workbench.md) nebo [Architektura](Arch_Workbench.md), tj. takové které mohou dělat problémy, protože většina činností v modulu Stavitelství vyžaduje tělesa.


</div>




<div class="mw-translate-fuzzy">

## Použití


</div>


<div class="mw-translate-fuzzy">

1.  Stiskněte tlačítko **<img src="images/Arch_Check.png" width=16px> '''Kontrola'''** a vstoupíte do Architektura → Menu Utility


</div>




<div class="mw-translate-fuzzy">

## Skriptování


</div>


**See also:**

[Arch API](Arch_API.md) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).


<div class="mw-translate-fuzzy">

Tento nástroj může být použit v [makrech](macros.md) a z konzoly Pythonu použitím následující funkce:


</div>


```python
list_bad = check(objectslist, includehidden=False)
```


<div class="mw-translate-fuzzy">

kontroluje zda daný objekt obsahuje pouze statické objekty


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



---
⏵ [documentation index](../README.md) > [BIM](Category_BIM.md) > Arch Check/cs
