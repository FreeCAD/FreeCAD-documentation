# Arch CloseHoles/cs
---
- GuiCommand:   Name:Arch CloseHoles   Name/cs:Arch CloseHoles   Workbenches:[MenuLocation:Arch - Utilities - Close Holes   SeeAlso:[[Arch Check](Arch_Workbench/cs___Arch]].md)---


</div>



## Popis


<div class="mw-translate-fuzzy">

Tento nástroj identifikuje mezery (kruhovité sekvence s otevřenými okraji) v objektu [Tvary](Part_Workbench.md) a pokouší se je uzavřít přidáním nové části vytvořené z okrajové sekvence. Nicméně, musíte přitom stále kontrolovat zda je výsledek těleso.


</div>




<div class="mw-translate-fuzzy">

## Použití


</div>


<div class="mw-translate-fuzzy">

1.  Vyberte objekt [Tvar](Part_Workbench.md)
2.  Stiskněte tlačítko **<img src="images/Arch_CloseHoles.png" width=16px> '''Uzavřít mezery'''** a dostanete se do nástrojového menu Architektura -\> Menu Utility


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
solid = closeHole(shape)
```


<div class="mw-translate-fuzzy">

uzavře mezery v otevřeném tvaru


</div>

Example: 
```python
import FreeCAD, Draft, Arch

Line = Draft.makeWire([FreeCAD.Vector(0, 0, 0),FreeCAD.Vector(2000, 2000, 0)])
Wall = Arch.makeWall(Line, width=150, height=3000)

Box = FreeCAD.ActiveDocument.addObject("Part::Box", "Box")
Box.Length = 900
Box.Width = 450
Box.Height = 2000
FreeCAD.ActiveDocument.recompute()

Draft.rotate(Box, 45)
Draft.move(Box, FreeCAD.Vector(1000, 700, 0))

Arch.removeComponents(Box, Wall)
FreeCAD.ActiveDocument.recompute() 

solid = Arch.closeHole(Wall.Shape)
```



---
![](images/Button_right.svg) [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch CloseHoles/cs
