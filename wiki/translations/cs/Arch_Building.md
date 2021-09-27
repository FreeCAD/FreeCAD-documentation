# Arch Building/cs
---
- GuiCommand:/cs   Name:Arch Building   Name/cs:Arch Budova   Workbenches:[MenuLocation:Arch → Building   Shortcut:B U   SeeAlso:[[Arch Floor/cs|Arch Podlaží](Arch_Workbench/cs___Architektura]].md), [Arch Staveniště](Arch_Site/cs.md)---


</div>

## Popis

Stavba je speciální typ skupiny objektů FreeCADu, zvlášť přizpůsobené k prezentaci celých stavebních jednotek. Většinou jsou využívány pro uspořádání Vašeho modelu obsahujícího objekty [podlaží](Arch_Floor/cs.md)


<div class="mw-translate-fuzzy">

## Použití


</div>


<div class="mw-translate-fuzzy">

1.  Volitelně lze vybrat jeden nebo více objektů, které lze vložit do Vaší nové stavby
2.  Stiskněte tlačítko **<img src="images/Arch_Building.png" width=16px> '''Stavba'''
** nebo klávesy **B** a **U**


</div>

## Volby


<div class="mw-translate-fuzzy">

-   Po vytvoření stavby můžete přidávat další objekty pomocí myši přetáhnutím a upuštěním (drag and drop) na požadované místo v panelu stromu nebo použitím nástroje <img alt="" src=images/Arch_Add.png  style="width:16px;"> [Přidat](Arch_Add/cs.md)
-   Odstranit objekty ze stavby můžete podobně myší přetáhnutím a upuštěním objektu mimo panelu stromu nebo použitím nástroje <img alt="" src=images/Arch_Remove.png  style="width:16px;"> [Odebrat](Arch_Remove/cs.md).


</div>

## Properties

-    **Building Type**: The type of this building, to choose from a list


<div class="mw-translate-fuzzy">

## Skriptování


</div>


<div class="mw-translate-fuzzy">

Nástroj Stavba může být použit v [makrech](macros/cs.md) a z konzoly Pythonu použitím následující funkce:


</div>


```python
Building = makeBuilding(objectslist=None, baseobj=None, name="Building")
```


<div class="mw-translate-fuzzy">

vytvoří stavbu včetně objektů ze seznamu objectslist


</div>

Příklad:


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


{{docnav|[Building Part](Arch_BuildingPart.md)|[Site](Arch_Site.md)|[Arch](Arch_Workbench/cs.md)|IconL=Arch_BuildingPart.svg |IconC=Workbench_Arch.svg |IconR=Arch_Site.svg}}


</div>

---
[documentation index](../README.md) > [Arch](Category_Arch.md) > [Arch](Arch_Workbench.md) > Arch Building/cs
