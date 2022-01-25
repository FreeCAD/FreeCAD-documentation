---
- GuiCommand:/de
   Name:PartDesign SubtractiveBox
   Name/de:PartDesign Abzuziehender Quader
   Workbenches:[[PartDesign_Workbench/de   PartDesign]]|MenuLocation:Part Design → Erzeuge einen abzuziehenden Grundkörper → Abzuziehender Quader
   Version:0.17
   SeeAlso:[PartDesign Erzeuge einen abzuziehenden Grundkörper](PartDesign_CompPrimitiveSubtractive/de.md)
---

# PartDesign SubtractiveBox/de

## Beschreibung

Fügt einen abzuziehenden Quader in den aktiven Körper (Body) ein. Die Form wird von dem existierenden Volumenkörper abgezogen.

![](images/PartDesign_SubtractiveBox_example.png ) *Auf der linken Seite ist der aktive Körper (A) in grau und der abzuziehender Quader (B) in durchscheinenden rot gezeigt. Auf der rechten Seite ist das Resultat zu sehen.*

## Anwendung


<div class="mw-translate-fuzzy">

1.  Drücke die **<img src="images/PartDesign_SubtractiveBox.svg" width=24px> '''Abzuziehender Quader''** Schaltfläche . **Anmerkung**: Abzuziehender Quader ist Teil des benannten Symbols *Erzeuge einen abzuziehenden Grundkörper*. Direkt nach dem Start von FreeCAD wird das Symbol von „Abzuziehender Quader" in der Werkzeugleiste angezeigt. Wenn ein anderer Grundkörper zu sehen ist, kann durch Klicken auf den Pfeil neben dem Symbol der abzuziehende Quader in dem aufklappenden Menü ausgewählt werden.
2.  Lege die Grundkörperparameter und [Anhang](Part_EditAttachment/de.md) fest.
3.  Klicke **OK**.
4.  Ein Quader erscheint unterhalb des aktiven Körpers.


</div>

## Optionen

Der Quader kann auf zwei verschieden Wege bearbeitet werden:

-   Doppelklicke in den Modellbaum oder durch Rechtsklick und Auswahl von **Grundkörper bearbeiten** im Kontextmenü; dadurch werden die Grundkörperparameter angezeigt.
-   Mittels des [Eigenschafteneditors](Property_editor/de.md).

## Eigenschaften


<div class="mw-translate-fuzzy">

-    **Attachment**: Bestimmt den Befestigungsmodus und den Befestigungsversatz. Siehe [Befestigung](Part_EditAttachment/de.md).

-    **Label**: Die vom Benutzer vergebene Bezeichung für das Quader-Objekt. Dies kann nach Bedarf geändert werden.

-    **Length**: Die Länge des Quaders in der X-Richtung.

-    **Width**: Die Länge des Quaders in der Y-Richtung.

-    **Height**: Die Länge des Quaders in der Z-Richtung.


</div>





{{PartDesign Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign SubtractiveBox/de
