# Surface Workbench/uk





<img alt="Surface workbench icon" src=images/Workbench_Surface.svg  style="width:128px;">


{{TOCright}}

## Introduction

The <img alt="" src=images/Workbench_Surface.svg  style="width:24px;"> <img src=images/Part_Builder.svg style="width:Surface Workbench](Surface_Workbench.md) provides tools to create and modify simple [NURBS surfaces](https://en.wikipedia.org/wiki/Non-uniform_rational_B-spline). These tools have a similar functionality to the **[16px"> <img src=images/PartDesign_AdditiveLoft.svg style="width:Part Builder](Part_Builder.md)** tool when the **Face from edges** option is used. However, unlike that tool, the tools of the Surface Workbench are parametric and provide additional options. In this respect, the tools in this workbench are similar to **[16px"> <img src=images/PartDesign_AdditivePipe.svg style="width:PartDesign AdditiveLoft](PartDesign_AdditiveLoft.md)** and **[16px"> [PartDesign AdditivePipe](PartDesign_AdditivePipe.md)**.

Some of the features provided are:

-   Creation of surfaces from boundary edges.
-   Alignment of the curvature from neighboring faces.
-   Constraining of surfaces to additional curves and vertices.
-   Extension of faces.
-   A mesh can be used as a template to create spline curves on its surface.

<img alt="" src=images/Surface_example.png  style="width:350px;">

## Usage

The Surface Workbench intends to create faces with shapes, which is not possible to do with the standard tools in other workbenches.

<img alt="" src=images/Toy_Duck.png  style="width:350px;">


*Surface created with sketches placed in datum planes with the tools of the [PartDesign Workbench](PartDesign_Workbench.md)*

The Surface Workbench integrates with other workbenches of FreeCAD. The above example was created from **<img src=images/Sketcher_NewSketch.svg style="width:16px"> <img src=images/PartDesign_Plane.svg style="width:Sketches](Sketch.md)** placed on **[16px"> [PartDesign Datum planes](PartDesign_Plane.md)** in the <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [PartDesign Workbench](PartDesign_Workbench.md). The design can be fully parametric if all datum planes and sketches are defined accordingly. In most cases it is sufficient to draw a closed sketch to define the boundary of a face, and then use different options to further modify its shape.

The generated surface cannot be placed inside a **<img src=images/PartDesign_Body.svg style="width:16px"> <img src=images/Std_Part.svg style="width:PartDesign Body](PartDesign_Body.md)**. However, the generated surface can be contained inside a **[16px"> <img src=images/PartDesign_Body.svg style="width:Std Part](Std_Part.md)** together with the associated **[16px"> <img src=images/Part_Builder.svg style="width:PartDesign Body](PartDesign_Body.md)** that holds the datum planes and sketches. The non-parametric **[16px"> [Part Builder](Part_Builder.md)** tool can then be used in order to create a [shell](Glossary#Shell.md) and finally a [solid](Glossary#Solid.md).

## Tools

-   <img alt="" src=images/Surface_Filling.svg  style="width:32px;"> [Filling](Surface_Filling.md): fills a series of boundary curves with a surface.

-   <img alt="" src=images/Surface_GeomFillSurface.svg  style="width:32px;"> [Fill boundary curves](Surface_GeomFillSurface.md): creates a surface from two, three or four boundary edges.

-   <img alt="" src=images/Surface_Sections.svg  style="width:32px;"> [Sections](Surface_Sections.md): creates a surface from edges that represent transversal sections of surface. <small>(v0.19)</small> 

-   <img alt="" src=images/Surface_ExtendFace.svg  style="width:32px;"> [Extend face](Surface_ExtendFace.md): extrapolates the surface at the boundaries with its local U parameter and V parameter.

-   <img alt="" src=images/Surface_CurveOnMesh.svg  style="width:32px;"> [Curve on mesh](Surface_CurveOnMesh.md): create approximated spline segments on top of a selected [mesh](Mesh_Workbench.md).





{{Surface Tools navi

}} 

[Category:Workbenches](Category:Workbenches.md)
