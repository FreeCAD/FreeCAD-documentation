---
 TutorialInfo:
   Topic: TechDraw
   Level: Beginner
   Time: 10 minutes
   Author: Andergrin
   FCVersion: 0.19
---

# TechDraw Pitch Circle Tutorial/ru





## Введение

This tutorial explains how to add a pitch circle to a <img alt="" src=images/Workbench_TechDraw.svg  style="width:24px;"> [TechDraw](TechDraw_Workbench.md) view. It assumes that the model is a <img alt="" src=images/PartDesign_Body.svg  style="width:24px;"> [PartDesign Body](PartDesign_Body.md) with at least three holes in a circular pattern. For the circle a separate sketch will be created. A similar procedure can be used in other situations and to add other annotation-like elements to [TechDraw](TechDraw_Workbench.md) views.

In FreeCAD version 0.20 and above a pitch circle can be created with the [TechDraw ExtensionHoleCircle](TechDraw_ExtensionHoleCircle.md) tool.

<img alt="" src=images/Circle.png  style="width:250px;"> <img alt="" src=images/Pitch_Circle.png  style="width:300px;">

## Create the sketch for the circle 

1.  Activate the <img alt="" src=images/PartDesign_Body.svg  style="width:24px;"> [PartDesign Body](PartDesign_Body.md). This will also activate the <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [PartDesign Workbench](PartDesign_Workbench.md), if required.
2.  In the [3D view](3D_view.md) select the correct face belonging to the body.
3.  Create a new sketch with the <img alt="" src=images/PartDesign_NewSketch.svg  style="width:24px;"> [PartDesign NewSketch](PartDesign_NewSketch.md) command.
4.  The sketch will be attached to the selected face.
5.  Call the <img alt="" src=images/Sketcher_External.svg  style="width:24px;"> [Sketcher External](Sketcher_External.md) command.
6.  Select three circular edges (holes) from the body.
7.  Use the <img alt="" src=images/Sketcher_Create3PointCircle.svg  style="width:24px;"> [Sketcher Create3PointCircle](Sketcher_Create3PointCircle.md) command to create a circle constrained to the center points of the external geometry.
8.  The sketch should now be fully constrained.
9.  Close the sketch.

## Create the TechDraw view 

1.  Switch to the <img alt="" src=images/Workbench_TechDraw.svg  style="width:24px;"> [TechDraw Workbench](TechDraw_Workbench.md).
2.  If you don\'t have one already: create a <img alt="" src=images/TechDraw_PageDefault.svg  style="width:24px;"> [TechDraw page](TechDraw_PageDefault.md).
3.  Make sure the [3D view](3D_view.md) is properly aligned.
4.  Hold down the **Ctrl** key and in the [Tree view](Tree_view.md) select the body and the sketch that was just just created.
5.  Insert a new view by calling the <img alt="" src=images/TechDraw_View.svg  style="width:24px;"> [TechDraw View](TechDraw_View.md) command.
6.  Switch to the [TechDraw](TechDraw_Workbench.md) page.
7.  Select the circle.
8.  Call the <img alt="" src=images/TechDraw_DecorateLine.svg  style="width:24px;"> [TechDraw DecorateLine](TechDraw_DecorateLine.md) command.
9.  Change the **Style** and **Weight** of the circle.


{{TechDraw Tools navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw Pitch Circle Tutorial/ru
