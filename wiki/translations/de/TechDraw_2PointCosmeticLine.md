---
- GuiCommand:/de
   Name:TechDraw 2PointCosmeticLine
   Name/de:TechDraw 2PunkteHilfslinie
   MenuLocation:TechDraw → Linien hinzufügen →Hilfslinie durch 2 Punkte hinzufügen
   Workbenches:[TechDraw](TechDraw_Workbench/de.md)
   Version:0.19
   SeeAlso:[TechDraw FlächenMittellinie](TechDraw_FaceCenterLine/de.md), [TechDraw 2LinienMittellinie](TechDraw_2LineCenterLine/de.md)
---

# TechDraw 2PointCosmeticLine/de


</div>



## Beschreibung


<div class="mw-translate-fuzzy">

Das Werkzeug **TechDraw 2PunkteHilfslinie** fügt eine Hilfslinie zwischen zwei Knoten (Punkten) hinzu. Die Knoten können 2D oder 3D sein. Die resultierende Linie kann zur Bemaßung verwendet werden. Das Aussehen der Linie kann mit dem Werkzeug [Liniendarstellung ändern](TechDraw_DecorateLine/de.md) geändert werden.


</div>

<img alt="" src=images/CosLine2PointsSample.png  style="width:200px;">


<div class="mw-translate-fuzzy">



*Hilfslinie durch zwei Punkte*


</div>




<div class="mw-translate-fuzzy">

## Anwendung


</div>


<div class="mw-translate-fuzzy">

1.  2 Knoten in einer Ansicht auswählen oder 2 Knoten in der 3D-Ansicht.
2.  Die Schaltfläche **<img src="images/TechDraw-line2points.svg" width=16px> Hilfslinie durch 2 Punkte hinzufügen** drücken.
3.  Ein Dialog wird geöffnet, in dem die Koordinaten der 2 Punkte angepasst werden können.
4.  Eine Linie wird hinzugefügt, die die 2 ausgewählten Knoten verbindet. Im Fall von 3D-Punkten verbindet die Linie die Projektion der ausgewählten Punkte.


</div>




<div class="mw-translate-fuzzy">

## Hilfslinien bearbeiten 


</div>

Zum Ändern der Endpunkte einer Hilfslinie:


<div class="mw-translate-fuzzy">

1.  Eine Hilfslinie auswählen.

2.  Die Schaltfläche **<img src="images/TechDraw-line2points.svg" width=16px> Hilfslinie durch 2 Punkte hinzufügen** drücken.

3.  Ein Dialogfeld wird geöffnet, in dem die Koordinaten der Endpunkte geändert werden können.

4.  
    **OK**drücken, um die Änderungen zu sehen.


</div>

## Notes

-   To delete a cosmetic line use <img alt="" src=images/TechDraw_CosmeticEraser.svg  style="width:16px;"> [TechDraw CosmeticEraser](TechDraw_CosmeticEraser.md).
-   To change the appearance of a cosmetic line use <img alt="" src=images/TechDraw_DecorateLine.svg  style="width:16px;"> [TechDraw DecorateLine](TechDraw_DecorateLine.md).



## Eigenschaften

Hilfslinien haben keine eigenen Eigenschaften, da sie keine Dokumentobjekte sind.



## Skripten

Siehe auch: [Autogenerierte API Dokumentation](https://freecad.github.io/SourceDoc/) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).


<div class="mw-translate-fuzzy">

Hilfslinien können mit den Methoden makeCosmeticLine(v1, v2) oder makeCosmeticLine3d(v1, v2) von DrawViewPart erzeugt werden.


</div>





{{TechDraw Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw 2PointCosmeticLine/de
