---
 GuiCommand:
   Name: TechDraw CosmeticCircle
   Name/de: TechDraw Hilfskreis
   MenuLocation: TechDraw , Linien hinzufügen , Hilfskreis hinzufügen
   Workbenches: TechDraw_Workbench/de
   Version: 1.0
   SeeAlso: TechDraw_2PointCosmeticLine/de
---

# TechDraw CosmeticCircle/de



## Beschreibung

Das Werkzeug **TechDraw Hilfskreis** fügt an einem ausgewählten Mittelpunkt einen Hilfskreis hinzu. Es kann ein 2D- oder 3D-Punkt sein.

<img alt="" src=images/CosmeticCircleSample.png  style="width:200px;">



*Hilfskreis*



## Anwendung, Erstellen 

1.  Einen Punkt in einer TechDraw-Ansicht oder in der [3D-Ansicht](3D_view/de.md) auswählen.
2.  Wurde ein Punkt in der 3D-Ansicht ausgewählt: Die korrekte TechDraw-Ansicht zur Auswahl hinzufügen, indem sie in der [Baumansicht](Tree_view/de.md) ausgewählt wird.
3.  Es gibt mehrere Möglichkeiten, den Befehl aufzurufen:
    -   Die Schaltfläche **<img src="images/TechDraw_CosmeticCircle.svg" width=16px> [Hilfkreis hinzufügen](TechDraw_CosmeticCircle.md)** drücken.
    -   Den Menüeintrag **TechDraw → Linien hinzufügen → <img src="images/TechDraw_CosmeticCircle.svg" width=16px> Hilfskreis hinzufügen** auswählen.
4.  Der Aufgaben-Bereich wird geöffnet.
5.  Wahlweise die Koordinaten des Mittelpunktes, den Radius sowie Start- und Endwinkel des Kreises anpassen.
6.  Die Schaltfläche **OK** drücken.
7.  Ein Hilfskreis wird hinzugefügt. Im Falle eines 3D-Mittelpunktes wird der Kreis auf der Projektion des Punktes plaziert.



## Anwendung, Bearbeiten 

Zum Ändern der Attribute eines Hilfskreises:

1.  Den Hilfskreis auswählen..
2.  Es gibt mehrere Möglichkeiten, den Befehl aufzurufen:
    -   Die Schaltfläche **<img src="images/TechDraw_CosmeticCircle.svg" width=16px> [Hilfkreis hinzufügen](TechDraw_CosmeticCircle.md)** drücken.
    -   Den Menüeintrag **TechDraw → Linien hinzufügen → <img src="images/TechDraw_CosmeticCircle.svg" width=16px> Hilfskreis hinzufügen** auswählen.
3.  Der Aufgaben-Bereich wird geöffnet.
4.  Die Koordinaten des Mittelpunktes, den Radius sowie Start- und Endwinkel des Kreises anpassen.
5.  Die Schaltfläche **OK** drücken.



## Hinweise

-   Um einen Hilfskreis zu löschen, wird er ausgewählt und die **Entf**-Taste gedrückt. {{Version/de|0.22}}
-   Um die Darstellung eines Hilfskreises anzupassen, wird <img alt="" src=images/TechDraw_DecorateLine.svg  style="width:16px;"> [TechDraw LiniendarstellungÄndern](TechDraw_DecorateLine/de.md) verwendet.



## Eigenschaften

Hilfskreise haben keine eigenen Eigenschaften, da sie keine Dokumentobjekte sind.



## Skripten

Siehe auch: [Autogenerierte API-Dokumentation](https://freecad.github.io/SourceDoc/) und [Grundlagen der Skripterstellung in FreeCAD](FreeCAD_Scripting_Basics/de.md).

Hilfskreise können mit der Methode {{Incode|makeCosmeticCircle(center, radius, start angle, end angle)}} von DrawViewPart erstellt werden.





{{TechDraw_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw CosmeticCircle/de
