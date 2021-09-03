---
- GuiCommand:/de
   Name:PartDesign SubtractiveEllipsoid
   Name/de:PartDesign Abzuziehendes Ellipsoid
   Workbenches:[PartDesign](PartDesign_Workbench/de.md)
   MenuLocation:Part Design → Erzeuge einen abzuziehenden Grundkörper → Abzuziehendes Ellipsoid
   SeeAlso:[[PartDesign_CompPrimitiveSubtractive/de]]---


</div>

## Beschreibung

Fügt ein abzuziehendes Ellipsoid in den aktiven Körper (Body) ein. Die Form wird von dem existierenden Volumenkörper abgezogen.

![](images/PartDesign_SubtractiveEllipsoid_example.svg )

*Auf der linken Seite ist der aktive Körper (A) in grau und der abzuziehendes Ellipsoid (B) in durchscheinenden rot gezeigt. Auf der rechten Seite ist das Resultat zu sehen.*

## Anwendung

1.  Auf die Schaltfläche **<img src="images/PartDesign_SubtractiveEllipsoid.svg" width=24px> '''Abzuziehendes Ellipsoid'''** klicken. **Anmerkung**: Abzuziehendes Ellipsoid ist Teil des benannten Symbols *Erzeuge einen abzuziehenden Grundkörper*. Direkt nach dem Start von FreeCAD wird das Symbol von „Abzuziehender Quader" in der Werkzeugleiste angezeigt. Wenn ein anderer Grundkörper zu sehen ist, kann durch Klicken auf den Pfeil neben dem Symbol das abzuziehende Ellipsoid in dem aufklappenden Menü ausgewählt werden.
2.  Die Parameter des Grundkörpers und über [Attachment](Part_Attachment/de.md) den räumlichen Bezug einstellen.
3.  Mit Klick auf **OK** bestätigen.
4.  Das Feature (Formelement) Ellipsoid erscheint unterhalb des aktiven Körpers (Body).

## Optionen

Das Ellipsoid kann auf zwei verschieden Wege bearbeitet werden:

-   Durch Doppelklick in der Baumstruktur oder durch Rechtsklick und Auswahl von **Grundkörper bearbeiten** in dem Kontextmenü. Dies öffnet den Dialog „Parameter des Grundkörpers" in dem Aufgabenpaneel.
-   Mittels des [Eigenschafteneditors](Property_editor/de.md) im Reiter Daten.

## Eigenschaften

-    {{PropertyData/de|Attachment}}: Bestimmt den Befestigungsmodus und den Befestigungsversatz. Siehe [Befestigung](Part_Attachment/de.md).

-    {{PropertyData/de|Label}}: Die vom Benutzer vergebene Bezeichung für das Ellipsoid-Objekt. Dies kann nach Bedarf geändert werden.

-    {{PropertyData/de|Radius1}}: Der Wert des Radius entlang der vertikalen Achse des Ellipsoids, in der Voreinstellung parallel zur Z-Achse.

-    {{PropertyData/de|Radius2}}: Der Wert des Radius der Längsachse, in der Voreinstellung parallel zur X-Achse.

-    {{PropertyData/de|Radius3}}: Der Wert des Radius entlang der Breite, in der Voreinstellung parallel zu der Y-Achse. In der Voreinstellung mit einen Wert von Null ist das Ellipsoid ein [abgeplattetes Rotationsellipsoid](https://de.wikipedia.org/wiki/Rotationsellipsoid). Dies hat die gleiche Form, als wäre Radius 3 identisch mit Radius2.

-    {{PropertyData/de|Angle1}}: (mit *V-Parameter:* in dem Dialog Parameter des Grundkörpers bezeichnet) Die untere Verkürzung des Ellipsoids, normal zur Z-Achse (-90° in einem vollen Rotationsellipsoid)

-    {{PropertyData/de|Angle2}}: (ohne Beschriftung in dem Dialog Parameter des Grundkörpers) Die obere Verkürzung des Ellipsoids, normal zur Z-Achse (90° in einem vollen Rotationsellipsoid).

-    {{PropertyData/de|Angle3}}: (mit *U-Parameter:* in dem Dialog Parameter des Grundkörpers bezeichnet) Rotationswinkel des halben elliptischen Querschnitts (360° in einem vollen Rotationsellipsoid).





{{PartDesign Tools navi

}}  
