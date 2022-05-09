---
- GuiCommand   */cs
   Name   *Arch Remove
   Name/cs   *Architektura Odebrat
   MenuLocation   *Arch → Remove
   Workbenches   *[Arch](Arch_Workbench/cs.md)
   SeeAlso   *[[Arch Add]]
---

# Arch Remove/cs


</div>

## Popis


<div class="mw-translate-fuzzy">

Nástroj Odebrat Vám umožňuje 2 druhy činnosti   *

-   Odebrat komponentu ze stavebního objektu, například odebrat kvádr, který byl přidán do zdi, jako je v příkladu [Přidat](Arch_Add/cs.md)
-   Odebrat objekt založený na objektu [tvar](Part_Workbench/cs.md) ze stavební komponenty jako je třeba [zeď](Arch_Wall/cs.md) nebo [struktura](Arch_Structure/cs.md)


</div>

The counterpart of this tool is the **<img src="images/Arch_Add.svg" width=16px> [Arch Add](Arch_Add.md)** tool.

<img alt="" src=images/Arch_Remove_example.jpg  style="width   *600px;">


<div class="mw-translate-fuzzy">

*Na obrázku výše je ze zdi odebrán kvádr*


</div>


<div class="mw-translate-fuzzy">

## Použití


</div>


<div class="mw-translate-fuzzy">

1.  Vyberte součást uvnitř stavebního objektu **nebo**   *
2.  Vyberte objekt(y), který má být odebrán, potom stavební komponentu, ze které se bude odebírat (tato stavební komponenta musí být vybrána jako poslední)
3.  Stiskněte tlačítko **<img src="images/Arch_Remove.png" width=16px> '''Odebrat'''
**


</div>

Or

1.  Select objects to be subtracted, the last object selected must the Arch object from which the other objects will be subtracted.
2.  Press the **<img src="images/Arch_Remove.svg" width=16px>** button, or **Arch** → **<img src="images/Arch_Remove.svg" width=16px> [Remove](Arch_Remove.md)** from the top menu.


<div class="mw-translate-fuzzy">

## Skriptování


</div>


<div class="mw-translate-fuzzy">

Nástroj Odebrat může být využit v [makrech](macros.md) a z konzoly Pythonu použitím následující funkce   *


</div>


```python
removeComponents(objectsList, host=None)
```


<div class="mw-translate-fuzzy">

-   odebere zadanou komponentu nebo komponenty podle zadaného seznamu objectsList z jejich rodičů. Je-li specifikován hlavní objekt hostObject, tato funkce se pokusí místo nich přidat komponenty jako jsou mezery.

Příklad   *


</div>

Example   * 
```python
import FreeCAD, Draft, Arch

Line = Draft.makeWire([FreeCAD.Vector(0, 0, 0),FreeCAD.Vector(2000, 2000, 0)])
Wall = Arch.makeWall(Line, width=150, height=3000)

Box = FreeCAD.ActiveDocument.addObject("Part   *   *Box", "Box")
Box.Length = 900
Box.Width = 450
Box.Height = 2000
FreeCAD.ActiveDocument.recompute()

Draft.rotate(Box, 45)
Draft.move(Box, FreeCAD.Vector(1000, 700, 0))

Arch.removeComponents(Box, Wall)
FreeCAD.ActiveDocument.recompute()
```


<div class="mw-translate-fuzzy">


{{docnav/cs|[Add component](Arch_Add.md)|[Survey](Arch_Survey.md)|[Arch](Arch_Workbench.md)|IconL=Arch_Add.svg |IconC=Workbench_Arch.svg |IconR=Arch_Survey.svg}}


</div>



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch Remove/cs
