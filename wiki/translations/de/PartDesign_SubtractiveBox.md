---
- GuiCommand:/de
   Name:PartDesign SubtractiveBox
   Name/de:PartDesign QuaderAbziehen
   MenuLocation:Part Design → Grundkörper abziehen → Quader
   Workbenches:[PartDesign](PartDesign_Workbench/de.md)
   Version:0.17
   SeeAlso:[PartDesign AuswahlGrundkörperAbziehen](PartDesign_CompPrimitiveSubtractive/de.md), [PartDesign QuaderHinzufügen](PartDesign_AdditiveBox/de.md)
---

# PartDesign SubtractiveBox/de

## Beschreibung

Fügt einen Quader-Grundkörper in den aktiven Körper (Body-Objekt) ein. Seine Form wird von dem vorhandenen Volumenkörper abgezogen.

![](images/PartDesign_SubtractiveBox_example.png ) *Auf der linken Seite ist der aktive Körper (A) in grau und der abzuziehender Quader (B) in durchscheinenden rot gezeigt. Auf der rechten Seite ist das Resultat zu sehen.*

## Anwendung

1.  Die Schaltfläche **<img src="images/PartDesign_SubtractiveBox.svg" width=24px> '''Quader'''** drücken **Hinweis**: Der Quader ist Teil eines Symbolmenüs mit der Bezeichnung Grundkörper abziehen. Nach dem Start von FreeCAD wird der Quader in der Werkzeugleiste angezeigt. Wenn ein anderer Grundkörper angezeigt wird, den Abwärtspfeil neben dem Symbol anklicken und Quader im Menü auswählen.

2.  Parameter des Grundkörpers und [Befestigung](Part_EditAttachment/de.md) festlegen.

3.  
    **OK**klicken.

4.  Ein Box-Objekt (Formelement) erscheint unter dem aktiven Körper (in der Baumansicht).

## Optionen

Der Quader kann nach der Erstellung auf zwei Arten bearbeitet werden:

-   Durch Doppelklick in der Baumstruktur oder durch Rechtsklick und Auswahl von **Grundkörper bearbeiten** im Kontextmenü. Dies öffnet den Dialog „Parameter des Grundkörpers" im Aufgabenbereich.
-   Mit Hilfe des [Eigenschafteneditors](Property_editor/de.md).

## Eigenschaften

-    {{PropertyData/de|Attachment}}: Bestimmt den Befestigungsmodus und den Befestigungsversatz. Siehe [Part Befestigung](Part_EditAttachment/de.md).

-    {{PropertyData/de|Label}}: Die vom Benutzer vergebene Bezeichung für den Quader (Box-Objekt). Dies kann nach Bedarf geändert werden.

-    {{PropertyData/de|Length}}: Die Länge des Quaders in der X-Richtung.

-    {{PropertyData/de|Width}}: Die Länge des Quaders in der Y-Richtung.

-    {{PropertyData/de|Height}}: Die Länge des Quaders in der Z-Richtung.





{{PartDesign_Tools_navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign SubtractiveBox/de
