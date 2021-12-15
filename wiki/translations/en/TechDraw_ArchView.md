---
- GuiCommand:
   Name:TechDraw ArchView
   MenuLocation:TechDraw → Insert Arch Workbench Object
   Workbenches:[TechDraw](TechDraw_Workbench.md), [Arch](Arch_Workbench.md)
   SeeAlso:[Arch Section Plane](Arch_SectionPlane.md)
---

# TechDraw ArchView/en

## Description

The ArchView tool inserts a view of an **<img src="images/Arch_SectionPlane.svg" width=16px> [Arch SectionPlane](Arch_SectionPlane.md)** on a [TechDraw page](TechDraw_PageDefault.md).

![](images/TechDraw_Arch_example.jpg )

## Usage

1.  Select an Arch section plane in the 3D view or in the tree
2.  If you have multiple drawing pages in your document, you will need to select the desired page in the tree.
3.  Press the **<img src="images/TechDraw_ArchView.svg" width=24px> [Insert Arch Workbench Object](TechDraw_ArchView.md)** button
4.  A view of the objects seen by the section plane will appear on the page.

### Limitations

The ArchView is rendered within the [Arch Workbench](Arch_Workbench.md), therefore TechDraw has limited control over its appearance. You may need to make changes within Arch to get the representation you want.

## Options

-   The Arch View is rendered by the [Arch Workbench](Arch_Workbench.md), the same way as in the [Drawing Workbench](Drawing_Workbench.md). See Notes.
-   [Draft Dimensions](Draft_Snap_Dimensions.md), [Draft Texts](Draft_Text.md) and any other 2D (Sketch or Draft) object considered by the section plane is rendered \"as is\" (no intersection or hidden lines) on top of the solid geometry
-   The volume of [Arch Spaces](Arch_Space.md) is not rendered, only the label will be rendered
-   Cut lines, projected lines (if Show Hidden property is set to True) and 2D lines above can be rendered with different line widths. This can be configured in the Arch preferences.
-   The ArchView has two rendering modes: Wireframe, which uses the OpenCasCade algorithms of the [Drawing Workbench](Drawing_Workbench.md), is fast and produces only lines (no face fill possible), and Solid, which is based on the [Painter\'s algorithm](https://en.wikipedia.org/wiki/Painter%27s_algorithm), and is capable of rendering faces filled with their shape color. However, it is much slower and can fail in many situations. The image below illustrates the difference between the two rendering modes:

![](images/TechDraw_Arch_rendering.jpg )

-   Only the base line of [Arch Pipes](Arch_Pipe.md) is rendered, not the full volume of the tube:

![](images/TechDraw_Arch_piping.jpg )

## Properties

-    **Source**: The section plane object to be displayed

-    **All On**: If hidden objects must be shown or not. If False, only objects that are visible in the 3D view are rendered

-    **Render Mode**: The render mode to use, Solid or Wireframe

-    **Show Hidden**: If the hidden geometry (the part of the geometry that lies behind the section plane) is shown or not. It will be rendered in dashed line, which can be configured in the Arch preferences.

-    **Show Fill**: If cut areas must be filled with a grey color or not

-    **Line Width**: The width of the main lines. Cut lines and projected/2D line widths ratios can be configured in the Arch preferences

-    **Font Size**: The size of all texts that appear in this view

## Scripting


**See also:**

[TechDraw API](TechDraw_API.md) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

The ArchView tool can be used in [macros](Macros.md) and from the [Python](Python.md) console by using the following functions:


```python
dv = FreeCAD.ActiveDocument.addObject('TechDraw::DrawViewArch','TestArch')
dv.Source = mySectionPlane
rc = page.addView(dv)
```





{{TechDraw Tools navi

}}

---
[documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw ArchView/en
