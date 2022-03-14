# PartDesign SubtractiveTorus/de
---
- GuiCommand:/de
   Name:PartDesign SubtractiveTorus
   Name/de:PartDesign Abzuziehender Torus
   Workbenches:[PartDesign](PartDesign_Workbench/de.md)
   MenuLocation:Part Design → Erzeuge einen abzuziehenden Grundkörper → Abzuziehender Torus
   Shortcut:None
   SeeAlso:[Erzeuge einen abzuziehenden Grundkörper](PartDesign_CompPrimitiveSubtractive/de.md)---

## Beschreibung

Fügt einen abzuziehenden Torus in den aktiven Körper (Body) ein. Die Form wird von dem existierenden Volumenkörper abgezogen.

![](images/PartDesign_SubtractiveTorus_example.svg ) *Auf der linken Seite ist der aktive Körper (A) in Grau und der abzuziehende Torus (B) in durchscheinenden Rot gezeigt. Auf der rechten Seite ist das Resultat zu sehen.*

## Anwendung


<div class="mw-translate-fuzzy">

1.  Auf die Schaltfläche **<img src="images/PartDesign_SubtractiveTorus.svg" width=24px> '''Abzuziehender Torus'''** klicken. **Anmerkung**: Abzuziehender Torus ist Teil des benannten Symbols *Erzeugen eines zusätzlichen geometrischen Körpers*. Direkt nach dem Start von FreeCAD wird das Symbol von „Abzuziehender Quader" in der Werkzeugleiste angezeigt. Wenn ein anderer Grundkörper zu sehen ist, kann durch Klicken auf den Pfeil neben dem Symbol der zu abzuziehende Torus in dem aufklappenden Menü ausgewählt werden.
2.  Die Parameter des Grundkörpers und über [Attachment](Part_EditAttachment/de.md) den räumlichen Bezug einstellen.
3.  Mit Klick auf **OK** bestätigen.
4.  Ein Torus erscheint unterhalb des aktiven Körpers (Body).


</div>

## Optionen

Der Torus kann auf zwei verschieden Wege bearbeitet werden:

-   Durch Doppelklick in der Baumstruktur oder durch Rechtsklick und Auswahl von **Grundkörper bearbeiten** in dem Kontextmenü. Dies öffnet den Dialog „Parameter des Grundkörpers" in dem Aufgabenpaneel.
-   Mittels des [Eigenschafteneditors](Property_editor/de.md) im Reiter Daten.

## Eigenschaften


<div class="mw-translate-fuzzy">

-    {{PropertyData/de|Attachment}}: Bestimmt den Befestigungsmodus und den Befestigungsversatz. Siehe [Befestigung](Part_EditAttachment/de.md).

-    {{PropertyData/de|Label}}: Die vom Benutzer vergebene Bezeichung für das Torus-Objekt. Dies kann nach Bedarf geändert werden.

-    {{PropertyData/de|Radius1}}: Der Radius des imaginären Orbits, auf den das Querschnittsprofil den Mittelpunkt umrundet. (Der Abstand von dem Mittelpunkt des Torus zu dem Mittelpunkt des umlaufenden Profils)

-    {{PropertyData/de|Radius2}}: Der Radius von dem kreisförmigen Profil, welches die Torusform bestimmt.

-    {{PropertyData/de|Angle1}}: (mit *V-Parameter:* in dem Dialog Parameter des Grundkörpers bezeichnet) Der Winkel des unteren Halbbogens des kreisförmigen Profils (-180° in einem vollen Torus). Ein Fehler in der Programmierung verusacht unerwartete Ergebenisse bei Änderung von Angle1.

-    {{PropertyData/de|Angle2}}: (ohne Beschriftung in dem Dialog Parameter des Grundkörpers) Der Winkel des oberen Halbbogens des kreisförmigen Querschnittsprofils (180° in einem vollen Torus). Ein Fehler in der Programmierung verusacht unerwartete Ergebenisse bei Änderung von Angle2.

-    {{PropertyData/de|Angle3}}: (mit *U-Parameter:* in dem Dialog Parameter des Grundkörpers bezeichnet) Rotationswinkel des kreisförmigen Profilquerschnitts (360° in einem vollen Torus).


</div>


<div class="mw-translate-fuzzy">





</div>


{{PartDesign_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign SubtractiveTorus/de
