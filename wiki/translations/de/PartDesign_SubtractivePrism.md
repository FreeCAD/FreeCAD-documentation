---
- GuiCommand:/de
   Name:PartDesign SubtractivePrism
   Name/de:PartDesign PrismaAbziehen
   MenuLocation:Part Design → Grundkörper abziehen → Prisma
   Workbenches:[PartDesign](PartDesign_Workbench/de.md)
   Version:0.17
   SeeAlso:[PartDesign AuswahlGrundkörperAbziehen](PartDesign_CompPrimitiveSubtractive/de.md), [PartDesign PrismaHinzufügen](PartDesign_AdditivePrism/de.md)
---

# PartDesign SubtractivePrism/de



## Beschreibung

Fügt einen Prisma-Grundkörper in den aktiven Körper (Body-Objekt) ein. Seine Form wird von dem vorhandenen Volumenkörper abgezogen.

![](images/PartDesign_SubtractivePrism_example.svg )

*Auf der linken Seite ist der aktive Körper (A) in Grau und das abzuziehende Prisma (B) in durchscheinendem Rot gezeigt. Auf der rechten Seite ist das Resultat zu sehen.*



## Anwendung

1.  Die Schaltfläche **<img src="images/PartDesign_SubtractivePrism.svg" width=24px> '''Prisma'''** drücken. **Hinweis**: Das Prisma ist Teil eines Symbolmenüs mit der Bezeichnung *Grundkörper abziehen*. Nach dem Start von FreeCAD wird der Quader in der Werkzeugleiste angezeigt. Um zur Schaltfläche Prisma zu gelangen, den Abwärtspfeil neben dem sichtbaren Symbol anklicken und Prisma im Menü auswählen.

2.  Parameter des Grundkörpers und [Befestigung](Part_EditAttachment/de.md) festlegen.

3.  
    **OK**klicken.

4.  Ein Prism-Objekt (Formelement) erscheint unter dem aktiven Körper (in der Baumansicht).



## Optionen

Es ist möglich, schräge Prismen durch Angabe von Winkeln mit Bezug auf den Normalenvektor der gewählten Befestigung zu erzeugen.

Das Prisma kann nach seiner Erstellung auf zwei Arten bearbeitet werden:

-   Durch Doppelklick in der Baumstruktur oder durch Rechtsklick und Auswahl von Grundkörper bearbeiten im Kontextmenü. Dies öffnet den Dialog „Parameter des Grundkörpers" im Aufgabenbereich.
-   Mit Hilfe des [Eigenschafteneditors](Property_editor/de.md).



## Eigenschaften

-    {{PropertyData/de|Attachment}}: Bestimmt den Befestigungsmodus und den Befestigungsversatz. Siehe [Part Befestigung](Part_EditAttachment/de.md).

-    {{PropertyData/de|Label}}: Die vom Benutzer vergebene Bezeichnung für das Prisma (Prism-Objekt). Dies kann nach Bedarf geändert werden.

-    {{PropertyData/de|Polygon}}: Anzahl der Seiten im Polygonquerschnitt des Prismas.

-    {{PropertyData/de|Circumradius}}: [Umkreisradius](https://de.wikipedia.org/wiki/Umkreis) des Polygonquerschnitts des Prismas.

-    {{PropertyData/de|Height}}: Höhe des Prismas.

-    {{PropertyData/de|First Angle}}: Winkel in der ersten Richtung.

-    {{PropertyData/de|Second Angle}}: Winkel in der zweiten Richtung.





{{PartDesign_Tools_navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign SubtractivePrism/de
