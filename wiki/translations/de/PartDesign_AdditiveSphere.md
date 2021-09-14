---
- GuiCommand:/de
   Name:PartDesign AdditiveSphere
   Name/de:PartDesign Zu addierende Kugel
   Workbenches:[PartDesign](PartDesign_Workbench/de.md)
   MenuLocation:Part Design → Erzeugen eines zusätzlichen Grundkörpers → Zu addierende Kugel
   Shortcut:None
   Version:0.17
   Siehe auch:[Erzeugen eines zusätzlichen geometrischen Körpers](PartDesign_CompPrimitiveAdditive/de.md)---

## Beschreibung

Fügt den Grundkörper Kugel in den aktiven Körper (Body) als Basisformelement ein oder vereinigt ihn mit den bereits bestehenden Formelementen.

<img alt="" src=images/PartDesign_AdditiveSphere_example.png  style="width:200px;">

## Anwendung


<div class="mw-translate-fuzzy">

1.  Auf die Schaltfläche **<img src="images/PartDesign_AdditiveSphere.svg" width=24px> '''Zu addierende Kugel'''** klicken. **Anmerkung**: Zu addierende Kugel ist Teil des benannten Symbols *Erzeugen eines zusätzlichen geometrischen Körpers*. Direkt nach dem Start von FreeCAD wird das Symbol von „zu addierender Quader" in der Werkzeugleiste angezeigt. Wenn ein anderer Grundkörper zu sehen ist, kann durch Klicken auf den Pfeil neben dem Symbol der zu addierenden Kugel in dem aufklappenden Menü ausgewählt werden.
2.  Die Parameter des Grundkörpers und über [Attachment](Part_Attachment/de.md) den räumlichen Bezug einstellen.
3.  Mit Klick auf **OK** bestätigen.
4.  Das Feature (Formelement) Kugel (Sphere) erscheint unterhalb des aktiven Körpers (Body).


</div>

## Optionen

Die Kugel kann auf zwei verschieden Wege bearbeitet werden:

-   Durch Doppelklick in der Baumstruktur oder durch Rechtsklick und Auswahl von **Grundkörper bearbeiten** in dem Kontextmenü. Dies öffnet den Dialog „Parameter des Grundkörpers" in dem Aufgabenpaneel.
-   Mittels des [Eigenschafteneditors](Property_editor/de.md) im Reiter Daten.

## Eigenschaften


<div class="mw-translate-fuzzy">

-    {{PropertyData/de|Attachment}}: Bestimmt den Befestigungsmodus und den Befestigungsversatz. Siehe [Befestigung](Part_Attachment/de.md).

-    **Label**: Die vom Benutzer vergebene Bezeichung für das Kugel-Objekt. Dies kann nach Bedarf geändert werden.

-    {{PropertyData/de|Radius}}: Radius Kugel.

-    {{PropertyData/de|Angle1}}: (mit *V-Parameter:* in dem Dialog Parameter des Grundkörpers bezeichnet) Die untere Verkürzung der Kugel, normal zur Z-Achse (-90° in einer vollen Kugel)

-    {{PropertyData/de|Angle2}}: (ohne Beschriftung in dem Dialog Parameter des Grundkörpers) Die obere Verkürzung der Kugel, normal zur Z-Achse (90° in einer vollen Kugel).

-    {{PropertyData/de|Angle3}}: (mit *U-Parameter:* in dem Dialog Parameter des Grundkörpers bezeichnet) Rotationswinkel des halben Kugelquerschnitts (360° in einer vollen Kugel).


</div>





{{PartDesign Tools navi

}}  
