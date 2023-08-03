# Arch Floor/cs
---
 GuiCommand:   Name: Arch Floor   Name/cs: Arch Floor   Workbenches: Arch_Workbench/cs   Arch, Arch Site/cs---


</div>

## Popis


<div class="mw-translate-fuzzy">

Podlaží je speciální typ skupinového objektu FreeCADu, který má pár doplňkových vlastností zvláště vhodných pro výstavbu podlaží. Speciálně mají vlastnost výška, kterou mohou potomci objektu ([zdi](Arch_Wall/cs.md) a [struktury](Arch_Structure/cs.md)) automaticky použít pro nastavení jejich vlastní výšky.


</div>

As of <small>(v0.18)</small>  the Arch Floor is derived entirely from the [Arch BuildingPart](Arch_BuildingPart.md) object, which is a general container to organize a building model not limited to floors or storeys. Older Floor objects can be converted to the new type by right clicking on them and choosing `Convert to BuildingPart`.

## Použití


<div class="mw-translate-fuzzy">

1.  Volitelně lze vybrat jeden nebo více objektů, které lze vložit do Vašeho nového podlaží
2.  Stiskněte tlačítko **<img src="images/Arch_Floor.png" width=16px> '''Podlaží'''
** nebo klávesy **F** a **L**


</div>

## Volby


<div class="mw-translate-fuzzy">

-   Po vytvoření podlaží můžete přidávat další objekty pomocí myši přetáhnutím a upuštěním (drag and drop) na požadované místo v panelu stromu nebo použitím nástroje <img alt="" src=images/Arch_Add.png  style="width:16px;"> [Přidat](Arch_Add/cs.md)
-   Odstranit objekty z podlaží můžete podobně myší přetáhnutím a upuštěním objektu mimo panelu stromu nebo použitím nástroje <img alt="" src=images/Arch_Remove.png  style="width:16px;"> [Odebrat](Arch_Remove/cs.md).


</div>

## Vlastnosti

An Arch Floor object shares all properties from an [Arch BuildingPart](Arch_BuildingPart.md), with the **Ifc Type** set to `"Building Storey"`.


<div class="mw-translate-fuzzy">

## Skriptování


</div>


<div class="mw-translate-fuzzy">

Nástroj Podlaží může být využit v [makrech](macros/cs.md) a z konzoly Pythonu použitím následující funkce:


</div>


```python
Floor = makeFloor(objectslist=None, baseobj=None, name="Floor")
```


<div class="mw-translate-fuzzy">

vytvoří podlaží včetně objektů ze seznamu objectslist


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

Floor = Arch.makeFloor([Wall1, Wall2])

Building = Arch.makeBuilding([Floor])
Site = Arch.makeSite(Building)
FreeCAD.ActiveDocument.recompute() 
```


<div class="mw-translate-fuzzy">


{{docnav/cs|[Rebar](Arch_Rebar.md)|[Building Part](Arch_BuildingPart.md)|[Arch](Arch_Workbench/cs.md)|IconL=Arch_Rebar.svg |IconC=Workbench_Arch.svg |IconR=Arch_BuildingPart.svg}}


</div>



---
⏵ [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch Floor/cs
