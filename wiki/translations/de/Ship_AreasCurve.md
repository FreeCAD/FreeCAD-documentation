---
- GuiCommand:/de
   Name:Ship Area
   Name/de:Schiffsbereich
   Icon:Ship_AreaCurve.svg
   MenuLocation:Schiffskonstruktion → Bereichskurve
   |Workbenches:[Schiff](Ship_Workbench/de.md)
   Shortcut:
   SeeAlso:
---

# Ship AreasCurve/de


</div>

## Beschreibung

Plotten der transversalen Bereichskurve

<img alt="" src=images/FreeCAD-Ship-s60Areas.png  style="width:800px;"> 
*Design draft transversal areas curve*

The transversal areas curve offers really valuable information in the first stages of a ship\'s design, as it gives an idea of the shape and volume distribution of the ship.

Special attention should be paid to the eventual shoulders of the curve, which would indicate a large ship resistance (less efficiency in other words).

## Anwendung

In order to compute the transversal areas curve, select a **Ship instance** (see [Ship CreateShip](Ship_CreateShip.md)), and invoke **Ship design → <img src="images/Ship_AreasCurve.svg" width=16px> Areas curve**.

The task panel and a free-surface annotation in the [3D view](3D_view.md) are shown. The annotation is temporary and will be removed when you close the tool, so don\'t worry about that.

By default the design ship draft is selected, as well as a null trim angle. You are free to edit both fields. Each time the draft and trim data is edited some basic information regarding the submerged part of the ship is updated in the text box.

You can also select the number of transversal sections to be considered. The larger the number of sections the better resolution will be obtained, at a cost of longer computation time.

When you press the **Accept** button, the computation starts. It may hang FreeCAD for a while, be patient. When the computation finishes a plot of the transversal areas curve is created, as well as a spreadsheet with that information.

## Tutorien

-   [FreeCAD Schiffs s60 Tutorium](FreeCAD-Ship_s60_tutorial/de.md)
-   [FreeCAD Schiffs s60 Tutorium (II)](FreeCAD-Ship_s60_tutorial_(II)/de.md)


<div class="mw-translate-fuzzy">





</div>



---
![](images/Button_right.svg) [documentation index](../README.md) > [Ship](Category_Ship.md) > Ship AreasCurve/de
