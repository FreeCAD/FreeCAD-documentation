---
 GuiCommand:
   Name: TechDraw CosmeticCircle
   Name/de: TechDraw Hilfskreis
   MenuLocation: TechDraw , Linien hinzufügen , Hilfskreis hinzufügen
   Workbenches: TechDraw_Workbench/de
   Version: 0.22
   SeeAlso: TechDraw_2PointCosmeticLine/de
---

# TechDraw CosmeticCircle/de



## Beschreibung

Das Werkzeug **TechDraw Hilfskreis** fügt an einem ausgewählten Mittelpunkt einen Hilfskreis hinzu. Es kann ein 2D- oder 3D-Punkt sein.

<img alt="" src=images/CosmeticCircleSample.png  style="width:200px;">



*Hilfskreis*



## Anwendung, Erstellen 


<div lang="en" dir="ltr" class="mw-content-ltr">

1.  Select a center point in a TechDraw View or in the [3D view](3D_view.md).
2.  If you have selected a point in the 3D view: add the correct TechDraw View to the selection by selecting it in the [Tree view](Tree_view.md).
3.  There are several ways to invoke the tool:
    -   Press the **<img src="images/TechDraw_CosmeticCircle.svg" width=16px> [Add Cosmetic Circle](TechDraw_CosmeticCircle.md)** button.
    -   Select the **TechDraw → Add Lines → <img src="images/TechDraw_CosmeticCircle.svg" width=16px> Add Cosmetic Circle** option from the menu.
4.  A task panel opens.
5.  Optionally adjust the coordinates of the center point, the radius, and the start and end angles of the circle.
6.  Press the **OK** button.
7.  A cosmetic circle is added. In the case of a 3D center point, the circle is located at the projection of the point.


</div>



## Anwendung, Bearbeiten 

Zum Ändern der Attribute eines Hilfskreises:


<div lang="en" dir="ltr" class="mw-content-ltr">

1.  Select the cosmetic circle.
2.  There are several ways to invoke the tool:
    -   Press the **<img src="images/TechDraw_CosmeticCircle.svg" width=16px> [Add Cosmetic Circle](TechDraw_CosmeticCircle.md)** button.
    -   Select the **TechDraw → Add Lines → <img src="images/TechDraw_CosmeticCircle.svg" width=16px> Add Cosmetic Circle** option from the menu.
3.  A task panel opens.
4.  Adjust the coordinates of the center point, the radius, or the start and end angles of the circle.
5.  Press the **OK** button.


</div>



## Hinweise

-   Zum Löschen eines Hilfskreises wird <img alt="" src=images/TechDraw_CosmeticEraser.svg  style="width:16px;"> [TechDraw HilfsobjektEntfernen](TechDraw_CosmeticEraser/de.md) verwendet; alternativ wird das Objekt ausgewählt und die Löschtaste gedrückt.
-   Um die Darstellung eines Hilfskreises anzupassen, wird <img alt="" src=images/TechDraw_DecorateLine.svg  style="width:16px;"> [TechDraw LiniendarstellungÄndern](TechDraw_DecorateLine/de.md) verwendet.



## Eigenschaften

Hilfskreise haben keine eigenen Eigenschaften, da sie keine Dokumentobjekte sind.



## Skripten

Siehe auch: [Autogenerierte API-Dokumentation](https://freecad.github.io/SourceDoc/) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Hilfskreise können mit der Methode {{Incode|makeCosmeticCircle(center, radius, start angle, end angle)}} von DrawViewPart erstellt werden.





{{TechDraw Tools navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw CosmeticCircle/de
