---
 GuiCommand:
   Name: TechDraw 2PointCosmeticLine
   Name/de: TechDraw 2PunkteHilfslinie
   MenuLocation: TechDraw , Linien hinzufügen ,Hilfslinie durch 2 Punkte hinzufügen
   Workbenches: TechDraw_Workbench/de
   Version: 0.19
   SeeAlso: TechDraw_FaceCenterLine/de, TechDraw_2LineCenterLine/de
---

# TechDraw 2PointCosmeticLine/de



## Beschreibung

Das Werkzeug **TechDraw 2PunkteHilfslinie** fügt eine Hilfslinie zwischen zwei Punkten hinzu. Die Punkte können 2D oder 3D sein. Die resultierende Linie kann zum Bemaßen verwendet werden.

<img alt="" src=images/CosLine2PointsSample.png  style="width:200px;">



*Hilfslinie zwischen zwei Punkten*



## Anwendung, Erstellen 

1.  Zwei Punkte in einer TechDraw-Ansicht oder zweiPunkte in der [3D-Ansicht](3D_view/de.md) auswählen.
2.  Wenn die Punkte in der 3D-Ansicht ausgewählt wurden: Die korrekte TechDraw-Ansicht zur Auswahl hinzufügen, indem sie in der [Baumansicht](Tree_view/de.md) ausgewählt wird.
3.  Es gibt mehrere Möglichkeiten, das Werkzeug aufzurufen:
    -   Die Schaltfläche **<img src="images/TechDraw_2PointCosmeticLine.svg" width=16px> [Hilfslinie durch 2 Punkte hinzufügen](TechDraw_2PointCosmeticLine/de.md)** drücken.
    -   Den Menüeintrag **TechDraw → Linien hinzufügen → <img src="images/TechDraw_2PointCosmeticLine.svg" width=16px> Hilfslinie durch 2 Punkte hinzufügen** auswählen.
4.  Ein Aufgaben-Bereich wird geöffnet.
5.  Wahlweise die Koordinaten der Punkte anpassen.
6.  Die Schaltfläche **OK** drücken.
7.  Eine Hilfslinie, die die beiden Punkte verbindet, wird hinzugefügt. Im Falle von 3D-Punkten verbindet die Linie die Projektionen der Punkte.



## Anwendung, Bearbeiten 

Zum Ändern der Endpunkte einer Hilfslinie:

1.  Die Hilfslinie auswählen.
2.  Es gibt mehrere Möglichkeiten, das Werkzeug aufzurufen:
    -   Die Schaltfläche **<img src="images/TechDraw_2PointCosmeticLine.svg" width=16px> [Hilfslinie durch 2 Punkte hinzufügen](TechDraw_2PointCosmeticLine/de.md)** drücken.
    -   Den Menüeintrag **TechDraw → Linien hinzufügen → <img src="images/TechDraw_2PointCosmeticLine.svg" width=16px> Hilfslinie durch 2 Punkte hinzufügen** auswählen.
3.  Ein Aufgaben-Bereich wird geöffnet.
4.  Die Koordinaten der Punkte anpassen.
5.  Die Schaltfläche **OK** drücken.



## Hinweise

-   Zum Löschen einer Hilfslinie wird <img alt="" src=images/TechDraw_CosmeticEraser.svg  style="width:16px;"> [TechDraw HilfsobjektEntfernen](TechDraw_CosmeticEraser/de.md) verwendet.
-   Um die Darstellung einer Hilfslinie anzupassen, wird <img alt="" src=images/TechDraw_DecorateLine.svg  style="width:16px;"> [TechDraw LiniendarstellungÄndern](TechDraw_DecorateLine/de.md) verwendet.



## Eigenschaften

Hilfslinien haben keine eigenen Eigenschaften, da sie keine Dokumentobjekte sind.



## Skripten

Siehe auch: [Autogenerierte API Dokumentation](https://freecad.github.io/SourceDoc/) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Hilfslinien können mit den Methoden {{Incode|makeCosmeticLine(v1, v2)}} oder {{Incode|makeCosmeticLine3d(v1, v2)}} von DrawViewPart erstellt werden.





{{TechDraw Tools navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw 2PointCosmeticLine/de
