---
- TutorialInfo   *   Topic   *Modeling
   Level   *Experienced User
   Author   *domad
   FCVersion   *0.19.23300 or higher
---

# Advanced TechDraw Tutorial




 



## Purpose in Brief 

Create points, lines, circles, arcs, etc. in TechDraw views and/ or entire \"cosmetic\" drawings with absolute precision, suitable for the dimensioning tools that the workbench is equipped with, to generate compliant and detailed technical drawings.

## Introduction

This tutorial introduces the experienced user to some advanced use of existing tools and techniques from other workbenches to extend actually missing functionality in <img alt="" src=images/Workbench_TechDraw.svg  style="width   *24px;"> [TechDraw Workbench](TechDraw_Workbench.md). This tutorial is not a complete and comprehensive guide to the TechDraw Workbench and many of the tools and capabilities are not covered. It should contribute to overcome the difficulties that are encountered in quoting and enriching the technical drawing using TechDraw. This tutorial will take advanced users through the steps needed to produce challenging technical drawings of the part from the [Basic Part Design Tutorial](Basic_Part_Design_Tutorial.md) using drawing tools of the

1.  <img alt="" src=images/Workbench_Draft.svg  style="width   *24px;"> [Draft Workbench](Draft_Workbench.md) (lines, polylines, circumferences, arcs, splines, beziers, etc.), in particular the snaps, to create on the object effectively precise \"cosmetic points\" that could then be used for dimensioning in TechDraw.
2.  It is also possible to use the <img alt="" src=images/Workbench_Sketcher.svg  style="width   *24px;"> [Sketcher Workbench](Sketcher_Workbench.md) as
    -   generator of \"base-sketchTD\" (sketch bases for TechDraw) in 2D (e.g. such as system diagram, floor plans, elevations, views of mechanical or overall parts, etc.) or by
    -   using directly the sketches that generated the 3D models, or by
    -   converting to sketch the "facebinder" generated with Draft obtained from faces and/ or sections of the 3D models.
3.  To obtain particular sections (cuts on different planes or axes) to be presented on the page in TechDraw (it is advised to use a copy of the original 3D object), then through the creation of planes (even on different axes) using the <img alt="" src=images/Workfeature_workbench_icon.svg  style="width   *24px;"> [Workfeature Workbench](Workfeature_Workbench.md), it is possible to section the copy of the 3D object <img alt="" src=images/Part_SliceApart.svg  style="width   *24px;"> [Part SliceApart](Part_SliceApart.md) to obtain the faces to be converted into sketch <img alt="" src=images/Draft_Draft2Sketch.svg  style="width   *24px;"> [Draft Draft2Sketch](Draft_Draft2Sketch.md) and then through the Sketcher Workbench edit them to make them suitable to the technical drawing that we are interested in generating in TechDraw. The [Workfeature Workbench](Workfeature_Workbench.md) (and [Macro WorkFeatures](Macro_WorkFeatures.md)) are full of convenient additional functions, that allow us to easily create planes (theoretically infinite in extension and quantity) by selecting three points (vertices) *(remember that for three points passing, one and only one plane passes through three non-aligned points one and only one plane passes through three non-aligned points*) is a geometric axiom, which confirms without any ambiguity (!) the validity and importance of the WorkFeatureDev tool to create precise plans very easily.

(\**This is quite comparable to AutoCAD Slice command [1](https   *//knowledge.autodesk.com/support/autocad/learn-explore/caas/CloudHelp/cloudhelp/2019/ENU/AutoCAD-Core/files/GUID-27593C5E-4B89-41F2-872B-927D69517CBF-htm.html) which is based on that axiom. Without pre-building any new plane, a cutting plane using three points is defined.*)

*Note   * These planes can be joined together by overlapping/ coinciding of two edges using the Boolean feature of <img alt="" src=images/Part_Fuse.svg  style="width   *24px;"> [Part Union](Part_Fuse.md).* The planes thus formed and suitably positioned (according to our provisions) will be used as **cutting blades** <img alt="" src=images/Part_SliceApart.svg  style="width   *24px;"> [Part SliceApart](Part_SliceApart.md), cutting our 3D object into several parts according to the chosen planar confirmation.\'\'

## Before You Begin 

The Workbenches that are used to produce the drawings of the attached examples are   *
\* <img alt="" src=images/Workbench_Part.svg  style="width   *24px;"> [Part Workbench](Part_Workbench.md)

-   <img alt="" src=images/Workbench_Draft.svg  style="width   *24px;"> [Draft Workbench](Draft_Workbench.md)
-   <img alt="" src=images/Workbench_Sketcher.svg  style="width   *24px;"> [Sketcher Workbench](Sketcher_Workbench.md)
-   <img alt="" src=images/Workfeature_workbench_icon.svg  style="width   *24px;"> [Workfeature Workbench](Workfeature_Workbench.md)
-   <img alt="" src=images/Workbench_TechDraw.svg  style="width   *24px;"> [TechDraw Workbench](TechDraw_Workbench.md)

## The Task 

Stages of the procedure   *

1.  Creation of the 3D object(s) according to the canons of traditional modeling;
2.  Possible creation of independent or simple copies, eg. to be used for the creation of specific continuous sections positioned on multiple planes or axes, and which then through the use of the \"facebinder\", \"Draft to Sketch\", Shape 2D View, etc. functions. it will allow us to produce perfect "Sketches", then edit them to make them (by creating ad hoc "cosmetic points or lines") usable in TechDraw; to these sketches I gave the name of \"base-sketchTD\";
3.  insertion / creation of \"base-sketchTD\" in the layers of belonging (also with \"drag and drop\");
4.  creation of the drawing page with its template;
5.  creation of the view with TechDraw   * select the layer or the grouping folder (which contains the "base-sketchTD") from the structure, then click on the "insert view" button; TechDraw will insert the contents of the layer or grouping folder into the view. For a correct creation \"base-sketchTD\" must be perpendicular to the monitor / display view; I point out that whatever we add later in the layer or in the grouping-folder, or modifications of the "base-sketchTD", will be updated in realtime in the TechDraw view. Keep in mind that updates and / or modifications may affect the dimensions already introduced or cosmetic lines created with the specific tool of TechDraw in the view.
6.  once the "base-sketchTD" has been defined in the view, we can move on to dimensioning with the appropriate TechDraw tools;

It is possible to insert the \"base-sketchTD\" also in the projection group views   *

-   select the projection view -\> properties tab -\> Data -\> "Projection" record section -\> Source click on the button with the three dots and directly add the "base-sketchTD" or the layer that contains it.

   *   It should be noted that the \"base-sketchTD\" must be positioned on the highest face of the model / object, otherwise it will be hidden and will be invisible in TechDraw.

The sections obtained from the views do not seem to have this possibility. Whenever it is necessary to create precise cosmetic points suitable for dimensioning (e.g. tangency points), they can be generated   *

-   in \"Sketcher\" through construction lines and inserting circles with infinitesimal diameter / radius (0.00001) in the ends, these will be seen by TechDraw as points / vertices suitable for dimensioning;
-   in Draft with the same method to be inserted in the relevant layer or folder-grouping;

   *   once the \"base-sketchTD\" has been modified or the Draft object added in the layer or grouping folder, TechDraw will automatically update the view, if this does not happen, update manually with the appropriate command.

To insert section fills or patterns   *
pay attention to the lines created on the faces that intersect two or more edges, they are seen by TechDraw as separating elements of the face that affect the creation of the fills or patterns. This occurs e.g. when creating the outer lines that define the thread of a hole, this line will prevent the fill or pattern from extending further preventing it from arriving on the one that defines the pre-drill hole. In this case it is better to create cosmetic points through construction lines by inserting circles of infinitesimal radius in the vertices that will be seen by TechDraw as cosmetic points and then join them in TechDraw with create cosmetic line by two points.
All lines and / or paths (including cosmetic ones) that are displayed in the views can be edited in the formatting through TechDraw\'s "Change Apparence of selected Lines" command.
To create specific continuous sections on different axes or planes, I used the "WorkFeatureDev" workbench which allows you to create "solid" planes, with a thickness of "0", by selecting three vertices. These planes can be joined through a common or overlapping edge using the Boolean functions of the "Part" workbench and subsequently used for slicing / sectioning the solid model through the "Slice apart" command of the same workbench. The faces of the cut objects can be suitably exploited for the creation, with the "Facebinder" function, the "base-sketchTD"s to produce specific section views in TechDraw and therefore to be able to dimension and detail them.
I believe I have made public every \"trick\" (or rather system) experimented to be able to use more specific tools (not provided for TechDraw) and create high quality professional technical drawings without any limits, making the TechDraw workbench more efficient and adaptable to any need , in all likelihood on par (if not more flexible and powerful) than commercial peers.
It should be said, which is not negligible, that with this system it is possible to create entire 2D files and quote them with TechDraw in the same way as \"LibreCad\" or \"Autocad LT\" or other two-dimensional cads.
I hope I was clear enough (translation permitting) in explaining the procedure (\"trick / system\") that I believe to be \"easier to do than to say\", as it is all about being able to enter 2D drawings into the views of TDs created with \"Draft\" and / or with \"Sketcher\" simply by selecting them from the structure and creating a view in TD with the appropriate command \"create a view\"; but I thought of doing something pleasant and more technical by describing the procedure, certainly, in a \"simplified\" way to create a minimum of organized workflow.
It is up to each of us, with imagination and inventiveness, to optimize it to the maximum to obtain the best result.
I am attaching the files of some workflow examples of technical drawings (not feasible with TechDraw only) from which the images shown below were taken.
In the hope of having been useful, good work and good experimentation!

## Notes

## Future Outlook 

However, the described path could represent the starting point (or the idea) to write additional code to automate the system and integrate it directly into TechDraw with appropriate button / command functions.

## Links

-   [Macro WorkFeatures](https   *//wiki.freecadweb.org/Macro_WorkFeatures) Wiki page to macro
-   [FreeCAD WorkFeature Workbench](https   *//github.com/Rentlau/WorkFeature-WB) Repository to source code
-   [TechDraw without limits = Layout autocad](https   *//forum.freecadweb.org/viewtopic.php?t=54499) Forum Thread
-   [TechDraw   * -- come utilizzare gli strumenti Draft/Snaps per creare " vertici/punti cosmetici"](https   *//forum.freecadweb.org/viewtopic.php?f=28&t=53329) Forum Thread in Italian language

  {{TechDraw Tools navi}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Tutorials](Category_Tutorials.md) > [TechDraw](Category_TechDraw.md) > Advanced TechDraw Tutorial
