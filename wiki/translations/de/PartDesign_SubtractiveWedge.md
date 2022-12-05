# PartDesign SubtractiveWedge/de
---
- GuiCommand:/de
   Name:PartDesign SubtractiveWedge
   Name/de:PartDesign Abzuziehender Keil
   Workbenches:[PartDesign](PartDesign_Workbench/de.md)
   MenuLocation:Part Design → Erzeuge einen abzuziehenden Grundkörper → Abzuziehender Keil
   Shortcut:None
   SeeAlso:[Erzeuge einen abzuziehenden Grundkörper](PartDesign_CompPrimitiveSubtractive/de.md)---


</div>

## Beschreibung

Fügt einen abzuziehenden Keil in den aktiven Körper (Body) ein. Die Form wird von dem existierenden Volumenkörper abgezogen.

![](images/PartDesign_SubtractiveWedge_example.svg ) *Auf der linken Seite ist der aktive Körper (A) in Grau und der abzuziehender Keil (B) in durchscheinenden Rot gezeigt. Auf der rechten Seite ist das Resultat zu sehen.*

## Anwendung


<div class="mw-translate-fuzzy">

1.  Auf die Schaltfläche **<img src="images/PartDesign_SubtractiveWedge.svg" width=24px> '''Abzuziehender Keil'''** klicken. **Anmerkung**: Abzuziehender Keil ist Teil des benannten Symbols *Erzeugen eines zusätzlichen geometrischen Körpers*. Direkt nach dem Start von FreeCAD wird das Symbol von „Abzuziehender Quader" in der Werkzeugleiste angezeigt. Wenn ein anderer Grundkörper zu sehen ist, kann durch Klicken auf den Pfeil neben dem Symbol der abzuziehende Keil in dem aufklappenden Menü ausgewählt werden.
2.  Die Parameter des Grundkörpers und über [Attachment](Part_EditAttachment/de.md) den räumlichen Bezug einstellen.
3.  Mit Klick auf **OK** bestätigen.
4.  Das Feature (Formelement) Torus erscheint unterhalb des aktiven Körpers (Body).


</div>

## Optionen

Der Torus kann auf zwei verschiedene Wege bearbeitet werden:

-   Durch Doppelklick in der Baumstruktur oder durch Rechtsklick und Auswahl von **Grundkörper bearbeiten** in dem Kontextmenü. Dies öffnet den Dialog „Parameter des Grundkörpers" in dem Aufgabenpaneel.
-   Mittels des [Eigenschafteneditors](Property_editor/de.md) im Reiter Daten.

## Eigenschaften

Wenn die voreingestellte Platzierung verwendet wird, verhalten sich die aufgeführten Eigenschaften wie folgt:

-    {{PropertyData/de|X min/max}}: Koordinatenwerte der unteren Fläche in X-Richtung

-    {{PropertyData/de|Y min/max}}: Lage der oberen und unteren Fläche in Y-Richtung

-    {{PropertyData/de|Z min/max}}: Koordinatenwerte der unteren Fläche in Z-Richtung

-    {{PropertyData/de|X2 min/max}}: Koordinatenwerte der oberen Fläche in X-Richtung

-    {{PropertyData/de|Z2 min/max}}: Koordinatenwerte der oberen Fläche in Z-Richtung

## Pyramids

Wedges can be used to create pyramids by setting **X2 min/max** and **Z2 min/max** each so that min = max.


<div class="mw-translate-fuzzy">





</div>


{{PartDesign_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign SubtractiveWedge/de
