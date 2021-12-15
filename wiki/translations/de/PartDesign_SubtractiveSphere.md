---
- GuiCommand:
   Name:PartDesign SubtractiveSphere
   Name/de:PartDesign Abzuziehende Kugel
   Workbenches:[PartDesign](PartDesign_Workbench/de.md)
   MenuLocation:Part Design → Erzeuge einen abzuziehenden Grundkörper → Abzuziehende Kugel
   Shortcut:None
   SeeAlso:[Erzeuge einen abzuziehenden Grundkörper](PartDesign_CompPrimitiveSubtractive/de.md)
---

# PartDesign SubtractiveSphere/de

## Beschreibung

Fügt eine abzuziehende Kugel in den aktiven Körper (Body) ein. Die Form wird von dem existierenden Volumenkörper abgezogen.

![](images/PartDesign_SubtractiveSphere_example.svg ) *Auf der linken Seite ist der aktive Körper (A) in Grau und die abzuziehende Kugel (B) in durchscheinenden Rot gezeigt. Auf der rechten Seite ist das Resultat zu sehen.*

## Anwendung


<div class="mw-translate-fuzzy">

1.  Auf die Schaltfläche **<img src="images/PartDesign_SubtractiveSphere.svg" width=24px> '''Abzuziehende Kugel'''** klicken. **Anmerkung**: Abzuziehende Kugel ist Teil des benannten Symbols *Erzeugen eines zusätzlichen geometrischen Körpers*. Direkt nach dem Start von FreeCAD wird das Symbol von „Abzuziehender Quader" in der Werkzeugleiste angezeigt. Wenn ein anderer Grundkörper zu sehen ist, kann durch Klicken auf den Pfeil neben dem Symbol der abzuziehenden Kugel in dem aufklappenden Menü ausgewählt werden.
2.  Die Parameter des Grundkörpers und über [Attachment](Part_EditAttachment/de.md) den räumlichen Bezug einstellen.
3.  Mit Klick auf **OK** bestätigen.
4.  Das Feature (Formelement) Kugel (Sphere) erscheint unterhalb des aktiven Körpers (Body).


</div>

## Optionen

Die Kugel kann auf zwei verschieden Wege bearbeitet werden:

-   Durch Doppelklick in der Baumstruktur oder durch Rechtsklick und Auswahl von **Grundkörper bearbeiten** in dem Kontextmenü. Dies öffnet den Dialog „Parameter des Grundkörpers" in dem Aufgabenpaneel.
-   Mittels des [Eigenschafteneditors](Property_editor/de.md) im Reiter Daten.

## Eigenschaften


<div class="mw-translate-fuzzy">

-    {{PropertyData/de|Attachment}}: Bestimmt den Befestigungsmodus und den Befestigungsversatz. Siehe [Befestigung](Part_EditAttachment/de.md).

-    **Label**: Die vom Benutzer vergebene Bezeichung für das Kugel-Objekt. Dies kann nach Bedarf geändert werden.

-    {{PropertyData/de|Radius}}: Radius Kugel.

-    {{PropertyData/de|Angle1}}: (mit *V-Parameter:* in dem Dialog Parameter des Grundkörpers bezeichnet) Die untere Verkürzung der Kugel, normal zur Z-Achse (-90° für eine volle Kugel)

-    {{PropertyData/de|Angle2}}: (ohne Beschriftung in dem Dialog Parameter des Grundkörpers) Die obere Verkürzung der Kugel, normal zur Z-Achse (90° für eine volle Kugel).

-    {{PropertyData/de|Angle3}}: (mit *U-Parameter:* in dem Dialog Parameter des Grundkörpers bezeichnet) Rotationswinkel des halben Kugelquerschnitts (360° für eine volle Kugel).


</div>





{{PartDesign Tools navi

}}

---
[documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign SubtractiveSphere/de
