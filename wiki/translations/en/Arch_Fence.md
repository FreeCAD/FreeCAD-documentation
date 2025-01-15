---
 GuiCommand:
   Name: Arch Fence
   MenuLocation: 3D/BIM , Fence
   Workbenches: BIM_Workbench
   Version: 0.19
---

# Arch Fence/en

## Description

The **Arch Fence** is an object that builds a fence by repeating a single fence post and section along a given path.

<img alt="" src=images/Arch_Fence_description_example.png  style="width:600px;">

## Usage

### Creating from scratch 

1.  Use a workbench of your choice to create a single fence post and a single section.
2.  Create the path the fence should follow using the [Sketcher Workbench](Sketcher_Workbench.md) or [Draft Workbench](Draft_Workbench.md).
3.  Switch back to the [BIM Workbench](BIM_Workbench.md).
4.  Select the section, post and path in exactly that order.
5.  Press the **<img src="images/Arch_Fence.svg" width=16px> [Fence](Arch_Fence.md)** button

## Options

For now the tool assumes the following

1.  The Path is drawn on the XY-Plane
2.  Section and Post are drawn at the origin so that they stand upright in front view

## Properties

### Data

-    **Path**: The path the fence should follow

-    **Post**: A single fence post to repeat

-    **Section**: A single section to repeat

-    **Number Of Posts**: The total number of posts used to build the fence. This is calculated automatically.

-    **Number Of Sections**: The total number of sections used to build the fence. This is calculated automatically.

### View

-    **Use Original Colors**: When set to `True` the fence will use the colors from the original section and post. Otherwise the ShapeColor of the fence will be used to colorize the fence.

## Notes

-   Arch Fence was introduced in FC v0.19 by user furti.
-   [Forum thread](https://forum.freecadweb.org/viewtopic.php?t=36149) discussing Arch Fence functionality

## Scripting

The Fence tool can be used in [macros](Macros.md) and from the [Python](Python.md) console by using the following function:


```python
Fence = buildFence(section, post, path)
```

Example:


```python
import FreeCAD
import Part
import Arch

parts = []

parts.append(Part.makeBox(2000, 50, 30, FreeCAD.Vector(0, 0, 1000 - 30)))
parts.append(Part.makeBox(2000, 50, 30))
parts.append(Part.makeBox(20, 20, 1000 - 60, FreeCAD.Vector(0, 15, 30)))
parts.append(Part.makeBox(20, 20, 1000 - 60, FreeCAD.Vector(1980, 15, 30)))

for i in range(8):
    parts.append(Part.makeBox(20, 20, 1000 - 60, FreeCAD.Vector((2000 / 9 * (i + 1)) - 10, 15, 30)))

Part.show(Part.makeCompound(parts), "Fence_section")
fence_section = FreeCAD.ActiveDocument.Fence_section

sketch = FreeCAD.ActiveDocument.addObject("Sketcher::SketchObject", "Path")
sketch.Placement = FreeCAD.Placement(FreeCAD.Vector(0, 0, 0), FreeCAD.Rotation(0, 0, 0, 1))
sketch.addGeometry(Part.LineSegment(FreeCAD.Vector(0, 0, 0), FreeCAD.Vector(20000, 0, 0)), False)
sketch.addGeometry(Part.LineSegment(FreeCAD.Vector(20000, 0, 0), FreeCAD.Vector(20000, 20000, 0)), False)

post = Part.makeBox(100, 100, 1000, FreeCAD.Vector(0, 0, 0))
Part.show(post, "Post")
post = FreeCAD.ActiveDocument.Post

Fence = Arch.buildFence(fence_section, post, sketch)
```



---
⏵ [documentation index](../README.md) > [BIM](Category_BIM.md) > Arch Fence/en
