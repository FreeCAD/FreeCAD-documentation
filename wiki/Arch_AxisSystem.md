---
- GuiCommand:
   Name: Arch AxisSystem
   MenuLocation: Arch -> Axis tools -> Axis System
   Workbenches: Arch_Workbench
   SeeAlso: Arch_Axis, Arch_Grid
---

# Arch AxisSystem

## Description

The [AxisSystem](Arch_AxisSystem.md) tool allows you to combine two or three [Arch Axis](Arch_Axis.md) objects.

This is useful to define the intersection points between the different axes. Arch objects can then use this system to duplicate their shape on the different intersection points.

 <img alt="" src=images/Arch_AxisSystem_example.jpg  style="width:600px;">  
*Three [Arch Axis](Arch_Axis.md) objects combined into one [Arch AxisSystem](Arch_AxisSystem.md). An [Arch Structure](Arch_Structure.md) object uses this system as its **Axis* property, to have its shape duplicated at each intersection point.**

## Usage

1.  Optionally, select the [Arch Axis](Arch_Axis.md) objects you wish to include in this system.
2.  Press the **<img src="images/Arch_AxisSystem.svg" width=16px> [[Arch AxisSystem]]** button.
3.  Right-click the newly created axes system object in the tree view to add/edit the [Arch Axis](Arch_Axis.md) objects included in this system.
4.  Select any existing [Arch Axis](Arch_Axis.md) and press **<img src="images/Arch_Add.svg" width=16px> [Arch Add](Arch_Add.md)** or **<img src="images/Arch_Remove.svg" width=16px> [Arch Remove](Arch_Remove.md)** buttons to add or remove it to/from this system.
5.  Set the **Axis** property of any Arch object to point to this system, to have its shape duplicated to the intersection points of this system.

## Options

-   A same [Arch Axis](Arch_Axis.md) object can be part of more than one system
-   Any shape-based object can also be used as the **Axis** property of Arch objects. In this case, the object shape will be duplicated along the vertices of the Axis object

## Scripting


**See also:**

[Arch API](Arch_API.md) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

The AxisSystem tool can be used in [macros](Macros.md) and from the [Python](Python.md) console by using the following function:  
```python
AxisSystem = makeAxisSystem(axes, name="Axis System")
```

-   Creates an `AxisSystem` object from the given `axes`, which is a single [Arch Axis](Arch_Axis.md), or a list of them.

Example:  
```python
import Draft, Arch

Axes = Arch.makeAxis(5, 1000)

Axes.ViewObject.LineWidth = 3
Axes.ViewObject.BubbleSize = 200
Axes.ViewObject.FontSize = 150

Axes2 = Arch.makeAxis(6, 500)

Axes2.ViewObject.LineWidth = 2
Axes2.ViewObject.BubbleSize = 200
Axes2.ViewObject.FontSize = 150
Axes2.ViewObject.NumberingStyle = "A,B,C"
FreeCAD.ActiveDocument.recompute()

Axes2.Length = 6000
Draft.rotate(Axes2, -90)
Draft.move(Axes2, FreeCAD.Vector(-1000, 2500, 0))
FreeCAD.ActiveDocument.recompute()

AxisSystem = Arch.makeAxisSystem([Axes, Axes2])

Structure = Arch.makeStructure(length=200, width=200, height=100)
Draft.move(Structure, FreeCAD.Vector(-100, 0, 0))
Structure.Axis = AxisSystem
FreeCAD.ActiveDocument.recompute()
```



---
⏵ [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch AxisSystem
