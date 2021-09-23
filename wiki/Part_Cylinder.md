---
- GuiCommand:
   Name:Part Cylinder
   MenuLocation:Part → Primitives → Cylinder
   Workbenches:[Part](Part_Workbench.md)
   SeeAlso:[Part Primitives](Part_Primitives.md)
---

# Part Cylinder

## Description

Creates a simple parametric cylinder, with position, angle, radius and height parameters.

## Usage

1.  Switch to the <img alt="" src=images/Workbench_Part.svg  style="width:16px;"> [Part Workbench](Part_Workbench.md)
2.  There are several ways to invoke the command:
    -   Press the **<img src="images/Part_Cylinder.svg" width=16px> Cylinder** button in the toolbar.
    -   Select **Part → Primitives → <img src="images/Part_Cylinder.svg" width=16px> Cylinder** entry from the top menu

**Result:** The default result is a full cylinder with a radius of 2 mm and height of 10 mm, centered along the global z-axis and attached to the global xy-plane.

The cylinder properties can later be edited, either in the [Property editor](Property_editor.md) or by double-clicking the cylinder in the [Tree view](Tree_view.md).

<img alt="a cylinder created with the Cylinder tool" src=images/cylinder.png  style="width:650px;">

## Properties

-    **Angle**: This is the rotation angle that permits the creation of a portion of cylinder (it is set to 360° by default)

-    **Height**: The height is the distance in the z-axis

-    **Radius**: The radius defines a plane in x-y.

-    **First Angle**: Angle in first direction. <small>(v0.20)</small> 

-    **Second Angle**: Angle in second direction. <small>(v0.20)</small>

---
[documentation index](../README.md) > [Part](Part_Workbench.md) > Part Cylinder
