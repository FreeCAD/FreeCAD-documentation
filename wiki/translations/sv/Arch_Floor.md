---
 GuiCommand:
   Name: Arch Floor
   Name/sv: Arch Floor
   Workbenches: Arch_Workbench/sv
   MenuLocation: Arch , Floor
   Shortcut: **F** **L**
   SeeAlso: Arch Building, Arch BuildingPart, Arch Site
---

# Arch Floor/sv


</div>

#### Beskrivning


<div class="mw-translate-fuzzy">

Arch Floor är en speciell typ av FreeCAD group objekt som har några extra egenskaper speciellt anpassade för att bygga golv. De har bland annat en höjdegenskap, som dess barnobjekt ([väggar](Arch_Wall.md) och [strukturer](Arch_Structure.md)) kan använda för att ställa in sin egen höjd automatiskt.


</div>

As of <small>(v0.18)</small>  the Arch Floor is derived entirely from the [Arch BuildingPart](Arch_BuildingPart.md) object, which is a general container to organize a building model not limited to floors or storeys. Older Floor objects can be converted to the new type by right clicking on them and choosing `Convert to BuildingPart`.

## Usage

1.  Optionally, select one or more objects to be included in your new floor.
2.  Invoke the Arch Floor command several ways:
    -   Pressing the **<img src="images/Arch_Floor.svg" width=16px> [Arch Floor](Arch_Floor.md)** button on the toolbar.
    -   Using the **L** then **V** keyboard keys.
    -   Using the **Arch → Floor** entry from the top menu.

## Options

-   After creating a floor, you can add more objects to it by drag and dropping them in the Tree View or by using the **<img src="images/Arch_Add.svg" width=16px> [Arch Add](Arch_Add.md)** tool.
-   You can remove objects from a floor by drag and dropping them out of it the Tree View or by using the **<img src="images/Arch_Remove.svg" width=16px> [Arch Remove](Arch_Remove.md)** tool.

## Properties

An Arch Floor object shares all properties from an [Arch BuildingPart](Arch_BuildingPart.md), with the **Ifc Type** set to `"Building Storey"`.

## Scripting


**See also:**

[Arch API](Arch_API.md) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

The Floor tool can be used in [macros](macros.md) and from the [Python](Python.md) console by using the following function: 
```python
Floor = makeFloor(objectslist=None, baseobj=None, name="Floor")
```

-   Creates a `Floor` object from `objectslist`, which is a list of objects.

Example:


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


{{docnav/sv|[Rebar](Arch_Rebar.md)|[Building Part](Arch_BuildingPart.md)|[Arch](Arch_Workbench/sv.md)|IconL=Arch_Rebar.svg |IconC=Workbench_Arch.svg |IconR=Arch_BuildingPart.svg}}


</div>



---
⏵ [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch Floor/sv
