---
- GuiCommand:
   Name:PartDesign SubtractiveCylinder
   Name/de:PartDesign ZylinderAbziehen
   MenuLocation:Part Design - Grundkörper abziehen - Zylinder
   Workbenches:[PartDesign](PartDesign_Workbench/de.md)
   Version:0.17
   SeeAlso:[PartDesign AuswahlGrundkörperAbziehen](PartDesign_CompPrimitiveSubtractive/de.md), [PartDesign ZylinderHinzufügen](PartDesign_AdditiveCylinder/de.md)
---

# PartDesign SubtractiveCylinder/de



## Beschreibung

Fügt einen Zylinder-Grundkörper in den aktiven Körper (Body-Objekt) ein. Seine Form wird von dem vorhandenen Volumenkörper abgezogen.

![](images/PartDesign_SubtractiveCylinder_example.svg )

*Auf der linken Seite ist der aktive Körper (A) in Grau und der abzuziehende Zylinder (B) in durchscheinendem Rot gezeigt. Auf der rechten Seite ist das Resultat zu sehen.*



## Anwendung

1.  Die Schaltfläche **<img src="images/PartDesign_SubtractiveCylinder.svg" width=24px> '''Zylinder'''** drücken. Hinweis: Der Zylinder ist Teil eines Symbolmenüs mit der Bezeichnung Grundkörper abziehen. Nach dem Start von FreeCAD wird der Quader in der Werkzeugleiste angezeigt. Um zur Schaltfläche Zylinder zu gelangen, den Abwärtspfeil neben dem sichtbaren Symbol anklicken und Zylinder im Menü auswählen.

2.  Parameter des Grundkörpers und [Befestigung](Part_EditAttachment/de.md) festlegen.

3.  
    **OK**klicken.

4.  Ein Cylinder-Objekt (Formelement) erscheint unter dem aktiven Körper (in der Baumansicht).



## Optionen

Es ist möglich, schräge Zylinder durch Angabe von Winkeln mit Bezug auf den Normalenvektor der gewählten Befestigung zu erzeugen. {{Version/de|0.20}}

Der Zylinder kann nach der Erstellung auf zwei Arten bearbeitet werden:

-   Durch Doppelklick in der Baumstruktur oder durch Rechtsklick und Auswahl von **Grundkörper bearbeiten** im Kontextmenü. Dies öffnet den Dialog „Parameter des Grundkörpers" im Aufgabenbereich.
-   Mit Hilfe des [Eigenschafteneditors](Property_editor/de.md).



## Eigenschaften

-    {{PropertyData/de|Attachment}}: Bestimmt den Befestigungsmodus und den Befestigungsversatz. Siehe [Part Befestigung](Part_EditAttachment/de.md).

-    {{PropertyData/de|Label}}: Die vom Benutzer vergebene Bezeichung für das Zylinder-Objekt. Dies kann nach Bedarf geändert werden.

-    {{PropertyData/de|Radius}}: Der Wert des Radius des Zylinders.

-    {{PropertyData/de|Angle}}: Der Rotationswinkel des (halben) Querschnitts (360° ergeben einen ganzen Zylinder).

-    {{PropertyData/de|Height}}: Die Höhe des Zylinders entlang seiner Achse.

-    {{PropertyData/de|First Angle}}: Winkel in der ersten Richtung. {{Version/de|0.20}}

-    {{PropertyData/de|Second Angle}}: Winkel in der zweiten Richtung. {{Version/de|0.20}}





{{PartDesign_Tools_navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign SubtractiveCylinder/de
