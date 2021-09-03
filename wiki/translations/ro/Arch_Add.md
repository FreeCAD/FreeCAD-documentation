---
- GuiCommand:/ro   Name:Arch Add   Name/ro:Arch Add   Workbenches:[MenuLocation:Arch → Add   SeeAlso:[[Arch Remove|Arch Remove](Arch_Workbench/ro___Arch]].md)---


</div>

## Descriere


<div class="mw-translate-fuzzy">

Instrumentul Add vă permite 4 feluri de operații:

-   Add [shape](Part_Workbench.md)-based objects to an Arch component, such as a [wall](Arch_Wall.md) or [structure](Arch_Structure.md). Aceste obiecte fac parte din componenta Arch și vă permit să modificați forma sa, dar păstrând proprietățile sale de bază ca lățimea și înalțimea
-   Adaugă componente Arch, ca de exemplu [walls](Arch_Wall.md) sau [structures](Arch_Structure.md), la un grup de obiecte de bază Arch ca de exempluh o [floors](Arch_Floor.md).
-   Adaugă [axis systems](Arch_Axis.md) la [structural objects](Arch_Structure.md)
-   Adaugă obiecte la [section planes](Arch_SectionPlane.md)


</div>

The counterpart of this tool is the **<img src="images/Arch_Remove.svg" width=16px> [Arch Remove](Arch_Remove.md)** tool.

<img alt="" src=images/Arch_Add_example.jpg  style="width:640px;">


<div class="mw-translate-fuzzy">

*In imaginea de mai sus, o casetă este adăugată la un perete.*


</div>


<div class="mw-translate-fuzzy">

## Cum se folosește {#cum_se_folosește}


</div>


<div class="mw-translate-fuzzy">

1.  Selectați obiectul (obiectele) care urmează să fie adăugat e, apoi obiectul \"gazdă\" (obiectul gazdă trebuie să fie ultimul selectat)
2.  Apăsați tasta **<img src="images/Arch_Add.png" width=16px> '''Add'''
**


</div>


<div class="mw-translate-fuzzy">

## Script


</div>


<div class="mw-translate-fuzzy">

Instrumentul Add poate fi folosit în [macros](macros.md) și de la consola Python utilizând următoarea funcție:


</div>


:   
    
```python
    addComponents(objectsList, host)
    
```
    


<div class="mw-translate-fuzzy">

-   Adaugați obiectul dat sau obiectele din lista dată ca componente la obiectul gazdă. Îl utilizați pentru a adauga o ferestră la un perete , sau a adăga un peret la o pardoseală.
-   Nu Returnează nimic.


</div>

Exempluː


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









