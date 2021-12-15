# PartDesign AdditiveWedge/de
---
- GuiCommand:/de
   Name:PartDesign AdditiveWedge
   Name/de:PartDesign Zu addierender Keil
   Workbenches:[PartDesign](PartDesign_Workbench/de.md)
   MenuLocation:Part Design → Erzeugen eines zusätzlichen geometrischen Körpers → Zu addierender Keil
   Shortcut:None
   SeeAlso:[Erzeugen eines zusätzlichen geometrischen Körpers](PartDesign_CompPrimitiveAdditive/de.md)---


</div>

## Beschreibung

Fügt den Grundkörper Keil in den aktiven Körper (Body) als Basisformelement ein oder vereinigt ihn mit den bereits bestehenden Formelementen.

<img alt="" src=images/PartDesign_AdditiveWedge_example.png  style="width:200px;">

## Anwendung


<div class="mw-translate-fuzzy">

1.  Auf die Schaltfläche **<img src="images/PartDesign_AdditiveWedge.svg" width=24px> '''Zu addierender Keil'''** klicken. **Anmerkung**: zu addierender Keil ist Teil des benannten Symbols *Erzeugen eines zusätzlichen geometrischen Körpers*. Direkt nach dem Start von FreeCAD wird das Symbol von „zu addierender Quader" in der Werkzeugleiste angezeigt. Durch Klicken auf den Pfeil neben dem Symbol kann der zu addierenden Keil in dem aufklappenden Menü ausgewählt werden.
2.  Die Parameter des Grundkörpers und über [Attachment](Part_EditAttachment/de.md) den räumlichen Bezug einstellen.
3.  Mit Klick auf **OK** bestätigen.
4.  Das Element Keil erscheint unterhalb des aktiven Körpers (Body).


</div>

## Optionen

Der Torus kann auf zwei verschiedene Weisen bearbeitet werden:

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





{{PartDesign Tools navi

}}

---
[documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign AdditiveWedge/de
