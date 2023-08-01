---
- GuiCommand:
   Name:PartDesign SubtractiveEllipsoid
   Name/de:PartDesign EllipsoidAbziehen
   MenuLocation:Part Design → Grundkörper abziehen → Ellipsoid
   Workbenches:[PartDesign](PartDesign_Workbench/de.md)
   Version:0.17
   SeeAlso:[PartDesign AuswahlGrundkörperAbziehen](PartDesign_CompPrimitiveSubtractive/de.md), [PartDesign EllipsoidHinzufügen](PartDesign_AdditiveEllipsoid/de.md)
---

# PartDesign SubtractiveEllipsoid/de



## Beschreibung

Fügt einen Ellipsoid-Grundkörper in den aktiven Körper (Body-Objekt) ein. Seine Form wird von dem vorhandenen Volumenkörper abgezogen.

![](images/PartDesign_SubtractiveEllipsoid_example.svg )

*Auf der linken Seite ist der aktive Körper (A) in Grau und das abzuziehende Ellipsoid (B) in durchscheinendem Rot gezeigt. Auf der rechten Seite ist das Resultat zu sehen.*



## Anwendung

1.  Die Schaltfläche **<img src="images/PartDesign_SubtractiveEllipsoid.svg" width=24px> '''Ellipsoid'''** drücken. **Hinweis**: Das Ellipsoid ist Teil eines Symbolmenüs mit der Bezeichnung *Grundkörper abziehen*. Nach dem Start von FreeCAD wird der Quader in der Werkzeugleiste angezeigt. Um zur Schaltfläche Ellipsoid zu gelangen, den Abwärtspfeil neben dem sichtbaren Symbol anklicken und Ellipsoid im Menü auswählen.

2.  Parameter des Grundkörpers und [Befestigung](Part_EditAttachment/de.md) festlegen.

3.  
    **OK**klicken.

4.  Ein Ellipsoid-Objekt (Formelement) erscheint unter dem aktiven Körper (in der Baumansicht).



## Optionen

Das Ellipsoid kann nach der Erstellung auf zwei Arten bearbeitet werden:

-   Durch Doppelklick in der Baumstruktur oder durch Rechtsklick und Auswahl von **Grundkörper bearbeiten** im Kontextmenü. Dies öffnet den Dialog „Parameter des Grundkörpers" im Aufgabenbereich.
-   Mit Hilfe des [Eigenschafteneditors](Property_editor/de.md).



## Eigenschaften

-    {{PropertyData/de|Attachment}}: Bestimmt den Befestigungsmodus und den Befestigungsversatz. Siehe [Part Befestigung](Part_EditAttachment/de.md).

-    {{PropertyData/de|Label}}: Die vom Benutzer vergebene Bezeichung für das Ellipsoid (Ellipsoid-Objekt). Dies kann nach Bedarf geändert werden.

-    {{PropertyData/de|Radius1}}: Der Wert des Radius entlang der vertikalen Achse des Ellipsoids, in der Voreinstellung parallel zur Z-Achse.

-    {{PropertyData/de|Radius2}}: Der Wert des Radius der Längsachse, in der Voreinstellung parallel zur X-Achse.

-    {{PropertyData/de|Radius3}}: Der Wert des Radius entlang der Breite, in der Voreinstellung parallel zu der Y-Achse. In der Voreinstellung mit einen Wert von Null ist das Ellipsoid ein [abgeplattetes Rotationsellipsoid](https://de.wikipedia.org/wiki/Rotationsellipsoid). Dies hat die gleiche Form, als wäre Radius 3 identisch mit Radius2.

-    {{PropertyData/de|Angle1}}: (mit *V-Parameter* im Dialog Parameter des Grundkörpers bezeichnet) Die untere Verkürzung des Ellipsoids, normal zur Z-Achse (-90° für ein ganzes Rotationsellipsoid)

-    {{PropertyData/de|Angle2}}: (ohne Beschriftung im Dialog Parameter des Grundkörpers) Die obere Verkürzung des Ellipsoids, normal zur Z-Achse (90° für ein ganzes Rotationsellipsoid).

-    {{PropertyData/de|Angle3}}: (mit *U-Parameter* im Dialog Parameter des Grundkörpers bezeichnet) Rotationswinkel des (halben) elliptischen Querschnitts (360° für ein ganzes Rotationsellipsoid).





{{PartDesign_Tools_navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign SubtractiveEllipsoid/de
