# Arch Add/cs
---
- GuiCommand:   Name: Arch Add   Name/cs: Arch Přidat   Workbenches: Arch_Workbench/cs   Arch---


</div>

## Popis


<div class="mw-translate-fuzzy">

Nástroj Přidat Vám umožní 4 druhy operací:

-   Přidání na [tvaru](Part_Workbench/cs.md) založených objektů na stavební prvek jako například [zeď](Arch_Wall/cs.md) nebo [struktura](Arch_Structure/cs.md). Tyto objekty pak tvoří součást stavebního prvku a umožňují vám modifikovat jeho tvar, ale dál si udržují základní vlastnosti jako je šířka a výška
-   Přidávání stavebních prvků jako jsou [zdi](Arch_Wall/cs.md) nebo [struktury](Arch_Structure/cs.md) ke skupinám založeným na stavebních objektech jako jsou [podlaží](Arch_Floor/cs.md).
-   Přidávání [osových systémů](Arch_Axis/cs.md) ke [strukturovaným objektům](Arch_Structure/cs.md)
-   Přidávání stavebních objektů do [dílčích plánů](Arch_SectionPlane/cs.md)


</div>

The counterpart of this tool is the **<img src="images/Arch_Remove.svg" width=16px> [Arch Remove](Arch_Remove.md)** tool.

<img alt="" src=images/Arch_Add_example.jpg  style="width:640px;">


<div class="mw-translate-fuzzy">

*Na předchozím obrázku je kvádr přidaný do zdi.*


</div>


<div class="mw-translate-fuzzy">

## Použití


</div>


<div class="mw-translate-fuzzy">

1.  Vyberte objekt(y), který má být přidán a potom \"hlavní\" objekt (hlavní objekt posledním, který vyberete)
2.  Stiskněte tlačítko **<img src="images/Arch_Add.png" width=16px> '''Přidat'''
**


</div>


<div class="mw-translate-fuzzy">

## Skriptování


</div>


<div class="mw-translate-fuzzy">

Nástroj Add (Přidat) může být využit v [makrech](macros/cs.md) a z konzole Pythonu použitím následující funkce:


</div>


:   
    
```python
    addComponents(objectsList, host)
    
```
    


<div class="mw-translate-fuzzy">

-   Přidává vybraný objekt nebo objekty z daného seznamu (objectList) jako prvky k vybranému hlavnímu objektu (hostObject). Využijete to například pro přidávání oken do zdi nebo přidávání zdí na podlaží.
-   Nevrací nic.


</div>

Příklad:


```python
import FreeCAD, Arch, Draft, Part

p1 = FreeCAD.Vector(0, 0, 0)
p2 = FreeCAD.Vector(2000, 2000, 0)

Line = Draft.makeWire([p1, p2])
Wall = Arch.makeWall(Line, width=150, height=2000)

p3 = FreeCAD.Vector(0, 2000, 0)
p4 = FreeCAD.Vector(3000, 0, 0)

Line2 = Draft.makeWire([p3, p4])
Wall2 = Arch.makeWall(Line2, width=150, height=2000)
FreeCAD.ActiveDocument.recompute()

Arch.addComponents(Wall2, Wall)
FreeCAD.ActiveDocument.recompute()
```



---
⏵ [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch Add/cs
