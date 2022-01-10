# Part Cylinder/cs
---
- GuiCommand:/cs   Name:Part Cylinder   Name/cs:Díl Válec   MenuLocation:Díl -> Válec   |Workbenches:[SeeAlso:[[Part_CreatePrimitives/cs|Díl Vytváření zakl.geom.tvarů](Part_Workbench/cs___Modul_Díl]],_Kompletace.md)---


</div>

## Description

Creates a simple parametric cylinder, with position, angle, radius and height parameters.

## Usage

1.  Switch to the <img alt="" src=images/Workbench_Part.svg  style="width:16px;"> [Part Workbench](Part_Workbench.md)
2.  There are several ways to invoke the command:
    -   Press the **<img src="images/Part_Cylinder.svg" width=16px> Cylinder** button in the toolbar.
    -   Select **Part → Primitives → <img src="images/Part_Cylinder.svg" width=16px> Cylinder** entry from the top menu

**Result:** The default result is a full cylinder with a radius of 2 mm and height of 10 mm, centered along the global z-axis and attached to the global xy-plane.

The cylinder properties can later be edited, either in the [Property editor](Property_editor.md) or by double-clicking the cylinder in the [Tree view](Tree_view.md).

<img alt="válec vytvořený nástrojem Válec" src=images/cylinder.png  style="width:650px;">

## Properties

-    **Angle**: This is the rotation angle that permits the creation of a portion of cylinder (it is set to 360° by default)

-    **Height**: The height is the distance in the z-axis

-    **Radius**: The radius defines a plane in x-y.

-    **First Angle**: Angle in first direction. <small>(v0.20)</small> 

-    **Second Angle**: Angle in second direction. <small>(v0.20)</small> 

## Scripting

A Part Cylinder can be created using the following function:


```python
cylinder = FreeCAD.ActiveDocument.addObject("Part::Cylinder", "myCylinder")
```

-   Where {{Incode|"myCylinder"}} is the name for the object.
-   The function returns the newly created object.

---
[documentation index](../README.md) > [Part](Part_Workbench.md) > Part Cylinder/cs
