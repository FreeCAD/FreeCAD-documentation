---
- GuiCommand:/ro
   Name:Arch Remove
   Name/ro:Arch Remove
   MenuLocation:Arch → Remove
   Workbenches:[Arch](Arch_Workbench/fr.md)
   SeeAlso:[[Arch Add]]
---

# Arch Remove/ro


</div>

## Descriere


<div class="mw-translate-fuzzy">

Instrumentele de eliminare vă permit să efectuați două tipuri de operații:

-   Eliminați o subcomponentă dintr-un obiect Arch, de exemplu, scoateți o cutie adăugată pe un perete, ca în exemplul [Arch Add](Arch_Add.md)
-   Scoateți un obiect bazat pe [shape](Part_Workbench.md) dintr-o componentă Arch, cum ar fi [wall](Arch_Wall.md) sau [structure](Arch_Structure.md)


</div>

The counterpart of this tool is the **<img src="images/Arch_Add.svg" width=16px> [Arch Add](Arch_Add.md)** tool.

<img alt="" src=images/Arch_Remove_example.jpg  style="width:600px;">


<div class="mw-translate-fuzzy">

*In imaginea de mai sus, o casetă este extrasă dintr-un perete.*


</div>


<div class="mw-translate-fuzzy">

## Cum se folosește 


</div>


<div class="mw-translate-fuzzy">

1.  Selectați o subcomponentă în interiorul unui obiect Arch, **sau**:
2.  Selectați obiectul (obiectele) care trebuie scos, apoi componenta Arch din care trebuie să fie scăzută (componenta Arch trebuie să fie ultimul lucru pe care l-ați selectat)
3.  Apăsați butonul **<img src="images/Arch_Remove.png" width=16px> '''Remove'''
**


</div>

Or

1.  Select objects to be subtracted, the last object selected must the Arch object from which the other objects will be subtracted.
2.  Press the **<img src="images/Arch_Remove.svg" width=16px>** button, or **Arch** → **<img src="images/Arch_Remove.svg" width=16px> [Remove](Arch_Remove.md)** from the top menu.


<div class="mw-translate-fuzzy">

## Scrip-Programare 


</div>


<div class="mw-translate-fuzzy">

Instrumentul Remove poate fi folosit în [macros](macros.md) și din consola python utilizând următoarea funcție:


</div>


```python
removeComponents(objectsList, host=None)
```


<div class="mw-translate-fuzzy">

-   elimină componenta dată sau componentele din lista dată de la părinți ei. Dacă este specificat un obiect gazdă, această funcție va încerca să adauge componentele ca găuri la obiectul gazdă.

Exemplu:


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
```


<div class="mw-translate-fuzzy">


{{docnav/ro|[Add component](Arch_Add.md)|[Survey](Arch_Survey.md)|[Arch](Arch_Workbench.md)|IconL=Arch_Add.svg |IconC=Workbench_Arch.svg |IconR=Arch_Survey.svg}}


</div>

---
[documentation index](../README.md) > [Arch](Category_Arch.md) > [Arch](Arch_Workbench.md) > Arch Remove/ro
