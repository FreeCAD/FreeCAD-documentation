---
 GuiCommand:
   Name: Arch CloseHoles
   Name/ro: Arch CloseHoles
   MenuLocation: Arch , Utilities , Close Holes
   Workbenches: Arch_Workbench/ro
   SeeAlso: Arch Check/ro
---

# Arch CloseHoles/ro


</div>



## Descriere


<div class="mw-translate-fuzzy">

Acest instrument identifică găuri/orificii (secvența circulară a marginilor deschise) într-un obiect [ Shape](Part_Workbench.md) și încearcă să le închidă prin adăugarea unei fațete noi constrută pe acea secvență de margini. Totuși, trebuie să vă asigurați că rezultatul este un obiect solid.


</div>




<div class="mw-translate-fuzzy">

## Cum se folosește 


</div>


<div class="mw-translate-fuzzy">

1.  Selectați un obiect [Shape](Part_Workbench.md)
2.  Apăsați **<img src="images/Arch_CloseHoles.svg" width=16px> [Close Holes](Arch_CloseHoles.md)
** entry in **Arch → Utilities → Close Holes**


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
solid = closeHole(shape)
```


<div class="mw-translate-fuzzy">

închide o gaură într-o formă deschisă


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
⏵ [documentation index](../README.md) > [BIM](Category_BIM.md) > Arch CloseHoles/ro
