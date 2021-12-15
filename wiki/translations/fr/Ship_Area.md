---
- GuiCommand:/fr
   Name:Ship Area
   Name/fr:Ship Area
   Icon:Ship_AreaCurve.svg
   MenuLocation:Ship design → Areas curve
   Workbenches:[Ship](Ship_Workbench/fr.md)
   Shortcut:
   SeeAlso:
---

# Ship Area/fr


</div>

## Description

Plot the transversal areas curve

<img alt="" src=images/FreeCAD-Ship-s60Areas.png  style="width:800px;"> 
*Design draft transversal areas curve*

The transversal areas curve offers really valuable information in the first stages of a ship\'s design, as it gives an idea of the shape and volume distribution of the ship.

Special attention should be paid to the eventual shoulders of the curve, which would indicate a large ship resistance (less efficiency in other words).

## Usage

In order to compute the transversal areas curve, select a **Ship instance** (see [Ships creation](Ship_New.md)), and invoke **Ship design → Areas curve**.

The task panel and a free-surface annotation in the [3D view](3D_view.md) are shown. The annotation is temporary and will be removed when you close the tool, so don\'t worry about that.

By default the design ship draft is selected, as well as a null trim angle. You are free to edit both fields. Each time the draft and trim data is edited some basic information regarding the submerged part of the ship is updated in the text box.

You can also select the number of transversal sections to be considered. The larger the number of sections the better resolution will be obtained, at a cost of longer computation time.

When you press the **Accept** button, the computation starts. It may hang FreeCAD for a while, be patient. When the computation finishes a plot of the transversal areas curve is created, as well as a spreadsheet with that information.

## Tutorials

-   [FreeCAD-Ship s60 tutorial](FreeCAD-Ship_s60_tutorial.md)
-   [FreeCAD-Ship s60 tutorial (II)](FreeCAD-Ship_s60_tutorial_(II).md)





{{Ship_Tools_navi

}}

---
[documentation index](../README.md) > Ship Area/fr
