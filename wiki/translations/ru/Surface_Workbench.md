# Surface Workbench/ru
<div class="mw-translate-fuzzy">





</div>

<img alt="Логотип верстака Surface" src=images/Workbench_Surface.svg  style="width:128px;">






## Введение

<img alt="" src=images/Workbench_Surface.svg  style="width:24px;"> [Верстак Surface](Surface_Workbench/ru.md) предоставляет инструменты для создания и изменения простых [поверхностей NURBS](https://ru.wikipedia.org/wiki/NURBS). Эти инструменты имеют функциональность, похожую на инструменты **[<img src=images/Part_Builder.svg style="width:16px"> [Part Builder](Part_Builder/ru.md)** при использовании опции **Face from edges**. Однако, в отличие от этих инструментов, Верстак Surface параметрический и даёт дополнительные опции. В этом отношении, инструменты этого верстака похожи на **[<img src=images/PartDesign_AdditiveLoft.svg style="width:16px"> [PartDesign AdditiveLoft](PartDesign_AdditiveLoft/ru.md)** и **[<img src=images/PartDesign_AdditivePipe.svg style="width:16px"> [PartDesign AdditivePipe](PartDesign_AdditivePipe/ru.md)**.

Некоторые из предоставляемых функций:

-   Создание поверхностей из граничных ребер.
-   Выравнивание кривизны от соседних граней.
-   Ограничение поверхностей дополнительными кривыми и вершинами.
-   Расширение лица.
-   Можно использовать сетку в качестве шаблона для создания сплайновых кривых на ее поверхности.

<img alt="" src=images/Surface_example.png  style="width:350px;">



## Применение

Верстак Surface предназначен для создания граней с формами, что невозможно сделать стандартными инструментами в других верстаках.

<img alt="" src=images/Toy_Duck.png  style="width:350px;">



*Surface created with sketches placed in datum planes with the tools of the [PartDesign Workbench](PartDesign_Workbench.md)*

The Surface Workbench integrates with other workbenches of FreeCAD. The above example was created from **[<img src=images/Sketcher_NewSketch.svg style="width:16px"> [Sketches](Sketch.md)** placed on **[<img src=images/PartDesign_Plane.svg style="width:16px"> [PartDesign Datum planes](PartDesign_Plane.md)** in the <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [PartDesign Workbench](PartDesign_Workbench.md). The design can be fully parametric if all datum planes and sketches are defined accordingly. In most cases it is sufficient to draw a closed sketch to define the boundary of a face, and then use different options to further modify its shape.

The generated surface cannot be placed inside a **[<img src=images/PartDesign_Body.svg style="width:16px"> [PartDesign Body](PartDesign_Body.md)**. However, the generated surface can be contained inside a **[<img src=images/Std_Part.svg style="width:16px"> [Std Part](Std_Part.md)** together with the associated **[<img src=images/PartDesign_Body.svg style="width:16px"> [PartDesign Body](PartDesign_Body.md)** that holds the datum planes and sketches. The non-parametric **[<img src=images/Part_Builder.svg style="width:16px"> [Part Builder](Part_Builder.md)** tool can then be used in order to create a [shell](Glossary#Shell.md) and finally a [solid](Glossary#Solid.md).



## Инструменты

-   <img alt="" src=images/Surface_Filling.svg  style="width:32px;"> [Filling](Surface_Filling.md): fills a series of boundary curves with a surface.

-   <img alt="" src=images/Surface_GeomFillSurface.svg  style="width:32px;"> [Fill boundary curves](Surface_GeomFillSurface.md): creates a surface from two, three or four boundary edges.

-   <img alt="" src=images/Surface_Sections.svg  style="width:32px;"> [Sections](Surface_Sections.md): creates a surface from edges that represent transversal sections of surface.

-   <img alt="" src=images/Surface_ExtendFace.svg  style="width:32px;"> [Extend face](Surface_ExtendFace.md): extrapolates the surface at the boundaries with its local U parameter and V parameter.

-   <img alt="" src=images/Surface_CurveOnMesh.svg  style="width:32px;"> [Curve on mesh](Surface_CurveOnMesh.md): creates approximated spline segments on top of a selected [mesh](Mesh_Workbench.md).

-   <img alt="" src=images/Surface_BlendCurve.svg  style="width:32px;"> [Blend Curve](Surface_BlendCurve.md): creates a Bezier curve between two edges, with desired continuity.


<div class="mw-translate-fuzzy">





</div>


{{Surface Tools navi

}}



---
⏵ [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > [Surface](Category_Surface.md) > Surface Workbench/ru
