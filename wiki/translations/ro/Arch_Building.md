---
- GuiCommand:/ro   Name:Arch Building   Name/ro:Arch Building   Workbenches:[MenuLocation:Arch → Building   Shortcut:B U   SeeAlso:[[Arch Floor](Arch_Workbench/ro___Arch]].md), [[Arch Site]]---


</div>

## Descriere

Clădirea Arch este un tip special de obiect al grupului FreeCAD, care este special conceput pentru a reprezenta o întreagă unitate de construcție. Ele sunt cele mai utilizate pentru a vă organiza modelul, conținând obiecte [floor](Arch_Floor.md).


<div class="mw-translate-fuzzy">

## Cum se folosește 


</div>


<div class="mw-translate-fuzzy">

1.  Optionally, select one or more objects to be included in your new building
2.  Apăsați butonul **<img src="images/Arch_Building.png" width=16px> '''Arch Building'''
** , sau apăsați tastele **B** apoi **U**


</div>

## Opţiuni


<div class="mw-translate-fuzzy">

-   După crearea unei clădiri, puteți să adăugați mai multe obiecte prin glisarea și plasarea acestora în Vizualizarea Arborescentă sau utilizând instrumentul <img alt="" src=images/Arch_Add.png  style="width:16px;"> [Arch Add](Arch_Add.md)
-   Puteți să eliminați obiecte dintr-o clădire prin tragerea/glisarea și scoaterea lor din Vizualizarea arborescentă sau folosind instrumentul <img alt="" src=images/Arch_Remove.png  style="width:16px;"> [Arch Remove](Arch_Remove.md)


</div>

## Properties

-    **Building Type**: The type of this building, to choose from a list


<div class="mw-translate-fuzzy">

## Scrip-Programare 


</div>


<div class="mw-translate-fuzzy">

Instrumentul pentru Construcție poate fi utilizat în [macro-uri](macro-uri.md) și din consola Python utilizând următoarea funcție:


</div>


```python
Building = makeBuilding(objectslist=None, baseobj=None, name="Building")
```


<div class="mw-translate-fuzzy">

creează o consrucție incluzând obiectele din lista dată.


</div>

Exempluː


```python
import FreeCAD, Draft, Arch

p1 = FreeCAD.Vector(0, 0, 0)
p2 = FreeCAD.Vector(2000, 0, 0)
baseline = Draft.makeLine(p1, p2)
baseline2 = Draft.makeLine(p1, -1*p2)

Wall1 = Arch.makeWall(baseline, length=None, width=150, height=2000)
Wall2 = Arch.makeWall(baseline2, length=None, width=150, height=1800)
FreeCAD.ActiveDocument.recompute()

Building = Arch.makeBuilding([Wall1, Wall2])

Site = Arch.makeSite(Building)
FreeCAD.ActiveDocument.recompute()
```


<div class="mw-translate-fuzzy">


{{docnav|[Building Part](Arch_BuildingPart.md)|[Site](Arch_Site.md)|[Arch](Arch_Workbench/ro.md)|IconL=Arch_BuildingPart.svg |IconC=Workbench_Arch.svg |IconR=Arch_Site.svg}}


</div>


 
