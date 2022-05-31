# Drawing/zh-cn
## 简介

在FreeCAD中，\"[图样](Drawing.md)\"通常指一个[3D 模型的二维投影](model.md)。这个3D模型通常是用[TechDraw 工作台创建的](TechDraw_Workbench.md)

## 用法

1.  从一个已经构建的[3D模型开始](model.md)，例如，使用[PartDesign Workbench创建的模型](PartDesign_Workbench.md)。 事实上，模型可以是任何具有[Shape的对象](Shape.md)(包括2D对象)。
2.  切换到 [TechDraw Workbench](TechDraw_Workbench.md).
3.  点击 **[<img src=images/TechDraw_PageDefault.svg style="width   *16px"> [TechDraw PageDefault](TechDraw_PageDefault.md)** 或**[<img src=images/TechDraw_PageTemplate.svg style="width   *16px"> [TechDraw PageTemplate](TechDraw_PageTemplate.md)** 创建一个页面.
4.  选择已有的模型,然后点击 **[<img src=images/TechDraw_View.svg style="width   *16px"> [TechDraw View](TechDraw_View.md)** 或**[<img src=images/TechDraw_ProjectionGroup.svg style="width   *16px"> [TechDraw ProjectionGroup](TechDraw_ProjectionGroup.md)**.
5.  在新创建的页面上会有一个2D投影被创建. 现在你可以调整他的属性, 比如**Scale**, **Rotation**, 还有**Direction**.
6.  图样准备好之后, 你可以点按 **[<img src=images/TechDraw_ExportPageSVG.svg style="width   *16px"> [TechDraw ExportPageSVG](TechDraw_ExportPageSVG.md)**, **[<img src=images/TechDraw_ExportPageDXF.svg style="width   *16px"> [TechDraw ExportPageDXF](TechDraw_ExportPageDXF.md)**, 或使用 [Std Export](Std_Export.md), 将页面导出到 SVG, DXF, or PDF 格式以备将来用在其他软件中, 或用于打印.

## 说明

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
![](images/Right_arrow.png) [documentation index](../README.md) > [Glossary](Category_Glossary.md) > [TechDraw](Category_TechDraw.md) > Drawing/zh-cn
