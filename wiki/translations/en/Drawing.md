# Drawing/en
## Introduction

In FreeCAD the word \"[Drawing](Drawing.md)\" is normally used to refer to a 2D projection of a [3D model](model.md). This is usually created with the [TechDraw Workbench](TechDraw_Workbench.md).

## Usage

1.  Start with an already built [3D model](model.md), created with, for example, the [PartDesign Workbench](PartDesign_Workbench.md). In fact, any object that has a [Shape](Shape.md), including 2D objects, will work.
2.  Switch to the [TechDraw Workbench](TechDraw_Workbench.md).
3.  Press **[<img src=images/TechDraw_PageDefault.svg style="width   *16px"> [TechDraw PageDefault](TechDraw_PageDefault.md)** or **[<img src=images/TechDraw_PageTemplate.svg style="width   *16px"> [TechDraw PageTemplate](TechDraw_PageTemplate.md)** to create a Page.
4.  Select the existing model, and then press **[<img src=images/TechDraw_View.svg style="width   *16px"> [TechDraw View](TechDraw_View.md)** or **[<img src=images/TechDraw_ProjectionGroup.svg style="width   *16px"> [TechDraw ProjectionGroup](TechDraw_ProjectionGroup.md)**.
5.  A 2D projection on the page will be created. You may now adjust its properties, like **Scale**, **Rotation**, and **Direction**.
6.  When the drawing is ready, you can press **[<img src=images/TechDraw_ExportPageSVG.svg style="width   *16px"> [TechDraw ExportPageSVG](TechDraw_ExportPageSVG.md)**, **[<img src=images/TechDraw_ExportPageDXF.svg style="width   *16px"> [TechDraw ExportPageDXF](TechDraw_ExportPageDXF.md)**, or use [Std Export](Std_Export.md), to export the page to SVG, DXF, or PDF formats for further use in another software, or for printing.

## Notes

In informal usage, a \"Drawing\" may be any geometrical figure that is visible in the [3D view](3D_view.md), and thus its concept may be confused with that of \"[Body](Body.md)\", \"[Part](Part.md)\", or \"[model](Model.md)\".

However, when more precision is required, the distinction must be made.

-   A \"[Body](Body.md)\" ([PartDesign Body](PartDesign_Body.md)) is an object derived from a [Part Feature](Part_Feature.md) (`Part   *   *Feature` class), created with the [PartDesign Workbench](PartDesign_Workbench.md).
-   A \"[Part](Part.md)\" ([App Part](App_Part.md)) is used to group several \"[Bodies](Body.md)\" to form an assembly.
-   A \"Drawing\" is a 2D projection of a \"Body\" or a \"Part\".
-   A \"Drawing\" may also be created with the [Drawing Workbench](Drawing_Workbench.md). However, since this workbench became obsolete in 0.17, you should prefer [TechDraw Workbench](TechDraw_Workbench.md) instead.


{{TechDraw Tools navi

}} {{Document objects navi}} 

[Category   *Glossary](Category_Glossary.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Glossary](Category_Glossary.md) > [TechDraw](Category_TechDraw.md) > Drawing/en
