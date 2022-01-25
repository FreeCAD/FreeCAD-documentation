# PartDesign SubtractivePrism/de
---
- GuiCommand:/de|
Name=PartDesign SubtractivePrism|
Name/de=PartDesign Abzuziehendes Prisma
   Workbenches:[PartDesign](PartDesign_Workbench/de.md)
   MenuLocation:Part Design → Erzeuge einen abzuziehenden Grundkörper → Abzuziehendes Prisma
   Shortcut:Keiner
   SeeAlso:[Erzeuge einen abzuziehenden Grundkörper](PartDesign_CompPrimitiveSubtractive/de.md)---


</div>

## Beschreibung

Fügt ein abzuziehendes Prisma in den aktiven Körper (Body) ein. Die Form wird von dem existierenden Volumenkörper abgezogen.

![](images/PartDesign_SubtractivePrism_example.svg )

*Auf der linken Seite ist der aktive Körper (A) in Grau und das abzuziehende Prisma (B) in durchscheinenden Rot gezeigt. Auf der rechten Seite ist das Resultat zu sehen.*

## Anwendung


<div class="mw-translate-fuzzy">

1.  Auf die Schaltfläche **<img src="images/PartDesign_SubtractivePrism.svg" width=24px> '''Abzuziehendes Prisma'''** klicken. **Anmerkung**: Abzuziehendes Prisma ist Teil des benannten Symbols *Erzeuge einen abzuziehenden Grundkörper*. Direkt nach dem Start von FreeCAD wird das Symbol von „Abzuziehender Quader" in der Werkzeugleiste angezeigt. Wenn ein anderer Grundkörper zu sehen ist, kann durch Klicken auf den Pfeil neben dem Symbol das abzuziehende Prisma in dem aufklappenden Menü ausgewählt werden.
2.  Die Parameter des Grundkörpers und über [Attachment](Part_EditAttachment/de.md) den räumlichen Bezug einstellen.
3.  Mit Klick auf **OK** bestätigen.
4.  Das Feature (Formelement) Prisma (Prism) erscheint unterhalb des aktiven Körpers (Body).


</div>

## Optionen

Es ist möglich, schräge Prismen durch Angabe von Winkeln in Bezug auf den Normalenvektor des gewählten Anhangs zu erzeugen. <small>(v0.19)</small> 

Das Prisma kann auf zwei verschieden Wege bearbeitet werden:

-   Durch Doppelklick in der Baumstruktur oder durch Rechtsklick und Auswahl von **Grundkörper bearbeiten** in dem Kontextmenü. Dies öffnet den Dialog „Parameter des Grundkörpers" in dem Aufgabenpaneel.
-   Mittels des [Eigenschafteneditors](Property_editor/de.md) im Reiter Daten.

## Eigenschaften


<div class="mw-translate-fuzzy">

-    {{PropertyData/de|Attachment}}: Bestimmt den Befestigungsmodus und den Befestigungsversatz. Siehe [Befestigung](Part_EditAttachment/de.md).

-    {{PropertyData/de|Label}}: lDie vom Benutzer vergebene Bezeichung für das Prisma-Objekt. Dies kann nach Bedarf geändert werden.

-    {{PropertyData/de|Polygon}}: Die Anzahl der Seiten des Polygons in der Kontur des Prismas.

-    {{PropertyData/de|Circumradius}}: [Umkreisradius](https://de.wikipedia.org/wiki/Umkreis) der Kontur des Prismas.

-    {{PropertyData/de|Height}}: Höhe des Prismas.


</div>





{{PartDesign Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign SubtractivePrism/de
