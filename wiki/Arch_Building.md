---
 GuiCommand:
   Name: Arch Building
   MenuLocation: 3D/BIM , Building
   Workbenches: BIM_Workbench
   Shortcut: **B** **U**
   SeeAlso: 
---

# Arch Building

## Description

The Arch Building is a special type of FreeCAD group object particularly suited for representing a whole building unit. They are mostly used to organize your model, by containing [floor](Arch_Floor.md) objects.

## Usage

1.  Optionally, select one or more objects to be included in your new building.
2.  Press the **<img src="images/Arch_Building.svg" width=16px> [Building](Arch_Building.md)** button, or press the **B** then **U** keys.

## Options

-   Starting from FreeCAD version 0.18, the Building object is actually a [BuildingPart](Arch_BuildingPart.md) with its **IFC Type** property set to \"Building\". You can convert any BuildingPart to a Building simply by changing its IFC Type.
-   After creating a building, you can add more objects to it by drag and dropping them in the Tree View or by using the **<img src="images/Arch_Add.svg" width=16px> [Arch Add](Arch_Add.md)** tool.
-   You can remove objects from a building by drag and dropping them out of it the Tree View or by using the **<img src="images/Arch_Remove.svg" width=16px> [Arch Remove](Arch_Remove.md)** tool.

## Properties

-    **Building Type**: The type of this building, to choose from a list

## Scripting


**See also:**

[Arch API](Arch_API.md) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

The Building tool can be used in [macros](macros.md) and from the [Python](Python.md) console by using the following function:  
```python
Building = makeBuilding(objectslist=None, baseobj=None, name="Building")
```

-   Creates a `Building` object from `objectslist`, which is a list of objects, or `baseobj`, which is a `Shape`.

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

Building = Arch.makeBuilding([Wall1, Wall2])

Site = Arch.makeSite(Building)
FreeCAD.ActiveDocument.recompute()
```




 {{BIM_Tools_navi}}



---
⏵ [documentation index](../README.md) > Arch Building
