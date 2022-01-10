---
- GuiCommand:
   Name:Part Box
   MenuLocation:Part → Primitives → Cube
   Workbenches:[Part](Part_Workbench.md)
   SeeAlso:[Part Primitives](Part_Primitives.md)
---

# Part Box

## Description

The Box command from the [Part Workbench](Part_Workbench.md) inserts a parametric, [rectangular cuboid](http://en.wikipedia.org/wiki/Cuboid#Rectangular_cuboid), geometric primitive into the active document. By default, the Box command will insert a 10x10x10 mm cube, positioned at the origin, with the label \"cube\". These parameters may be modified after the object has been added.

 <img alt="Part\_Box" src=images/Part_Box.jpg  style="width:400px;"> 

## Usage

1.  Switch to the <img alt="" src=images/Workbench_Part.svg  style="width:16px;"> [Part Workbench](Part_Workbench.md)
2.  There are several ways to invoke the command:
    -   Press the **<img src="images/Part_Box.svg" width=16px> Cube** button in the toolbar.
    -   Select the **Part → Primitives → <img src="images/Part_Box.svg" width=16px> Cube** from the menu bar.

**Result:** The default result is a box with an equal length, width and height of 10 mm. It is attached to the global xy-plane and one edge is coincident with the global z-axis.

The box properties can later be edited, either in the property editor or by double-clicking on the box in the model tree.

## Properties


{{Properties_Title|Box}}

-    **Length**: The length parameter is the Box\'s dimension in the x-direction.

-    **Width**: The width parameter is the Box\'s dimension in the y-direction.

-    **Height**: The height parameter is the Box\'s dimension in the z-direction.

## Scripting

A Part Box can be created using the following function:

 
```python
box = FreeCAD.ActiveDocument.addObject("Part::Box", "myBox")
```

-   Where {{Incode|"myBox"}} is the name for the object.
-   The function returns the newly created object.

You can access and modify attributes of the {{Incode|box}} object. For example, you may wish to modify the length, width and height parameters.

 
```python
box.Length = 25
box.Width = 15
box.Height = 30
```

You can change its placement with:

 
```python
box.Placement = FreeCAD.Placement(FreeCAD.Vector(4, 6, 3), FreeCAD.Rotation(30, 45, 10))
```

---
[documentation index](../README.md) > [Part](Part_Workbench.md) > Part Box
