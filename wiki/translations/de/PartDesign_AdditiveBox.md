---
- GuiCommand:
   Name: PartDesign AdditiveBox
   Name/de: PartDesign QuaderHinzufügen
   MenuLocation: Part Design -> Grundkörper hinzufügen -> Quader
   Workbenches: PartDesign_Workbench/de
   Version: 0.17
   SeeAlso: PartDesign_CompPrimitiveAdditive/de, PartDesign_SubtractiveBox/de
---

# PartDesign AdditiveBox/de

## Beschreibung

Fügt einen Quader-Grundkörper in den aktiven Körper (Body-Objekt) als Basisformelement ein oder vereinigt ihn mit den bereits vorhandenen Formelementen.

<img alt="" src=images/PartDesign_AdditiveBox_example.png  style="width:200px;">

## Anwendung

1.  Die Schaltfläche **<img src="images/PartDesign_AdditiveBox.svg" width=24px> '''Quader'''** drücken. **Hinweis**: Der Quader ist Teil eines Symbolmenüs mit der Bezeichnung *Grundkörper hinzufügen*. Nach dem Start von FreeCAD wird der Quader in der Werkzeugleiste angezeigt. Wenn ein anderer Grundkörper angezeigt wird, den Abwärtspfeil neben dem Symbol anklicken und Quader im Menü auswählen.

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
⏵ [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign AdditiveBox/de
