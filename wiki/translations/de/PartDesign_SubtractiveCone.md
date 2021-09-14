---
- GuiCommand:/de
   Name:PartDesign SubtractiveCone
   Name/de:PartDesign Abzuziehender Kegel
   Workbenches:[PartDesign](PartDesign_Workbench/de.md)
   MenuLocation:Part Design → Erzeuge einen abzuziehenden Grundkörper → Abzuziehender Kegel
   Shortcut:None
   SeeAlso:[Erzeuge einen abzuziehenden Grundkörper](PartDesign_CompPrimitiveSubtractive/de.md)
---


</div>

## Beschreibung

Fügt einen abzuziehenden Kegel in den aktiven Körper (Body) ein. Die Form wird von dem existierenden Volumenkörper abgezogen.

![](images/PartDesign_SubtractiveCone_example.png )

*Auf der linken Seite ist der aktive Körper (A) in grau und der abzuziehender Kegel (B) in durchscheinenden rot gezeigt. Auf der rechten Seite ist das Resultat zu sehen.*

## Anwendung


<div class="mw-translate-fuzzy">

1.  Auf die Schaltfläche **<img src="images/PartDesign_SubtractiveCone.svg" width=24px> '''Abzuziehender Kegel'''** klicken. **Anmerkung**: Abzuziehender Kegel ist Teil des benannten Symbols *Erzeuge einen abzuziehenden Grundkörper*. Direkt nach dem Start von FreeCAD wird das Symbol von „Abzuziehender Quader" in der Werkzeugleiste angezeigt. Wenn ein anderer Grundkörper zu sehen ist, kann durch Klicken auf den Pfeil neben dem Symbol der abzuziehende Kegel in dem aufklappenden Menü ausgewählt werden.
2.  Die Parameter des Grundkörpers und über [Attachment](Part_Attachment/de.md) den räumlichen Bezug einstellen.
3.  Mit Klick auf **OK** bestätigen.
4.  Das Feature (Formelement) Kegel (Cone) erscheint unterhalb des aktiven Körpers (Body).


</div>

## Optionen

Der Kegel kann auf zwei verschiedene Wege bearbeitet werden:

-   Durch Doppelklick in der Baumstruktur oder durch Rechtsklick und Auswahl von **Grundkörper bearbeiten** in dem Kontextmenü. Dies öffnet den Dialog „Parameter des Grundkörpers" in dem Aufgabenpaneel.
-   Mittels der [Eigenschaften-Palette](Property_editor/de.md) im Reiter Daten.

## Eigenschaften


<div class="mw-translate-fuzzy">

-    {{PropertyData/de|Attachment}}: Bestimmt den Befestigungsmodus und den Befestigungsversatz. Siehe [Befestigung](Part_Attachment/de.md).

-    {{PropertyData/de|Label}}: Die vom Benutzer vergebene Bezeichung für das Kegel-Objekt. Dies kann nach Bedarf geändert werden.

-    {{PropertyData/de|Radius1}}: Der Wert des Radius an der Kegelbasis.

-    {{PropertyData/de|Radius2}}: Der Wert des Radius an der Kegeloberspitze. Ein von Null verschiedener Wert erzeugt einen Kegelstumpf.

-    {{PropertyData/de|Height}}: Die Höhe des Kegels entlang seiner Achse.

-    {{PropertyData/de|Angle}}: Der Rotationswinkel des halben Querschnitts (360° ergeben einen vollen Kegel).


</div>





{{PartDesign Tools navi

}}  
