---
- GuiCommand:/de
   Name:PartDesign AdditiveBox
   Name/de:PartDesign AdditiverQuader
   MenuLocation:Part Design → Erstellen eines additiven Grundelements → Additiver Quader
   Workbenches:[PartDesign](PartDesign_Workbench/de.md)
   Version:0.17
   SeeAlso:[PartDesign Additives Grundelement](PartDesign_CompPrimitiveAdditive/de.md)
---

# PartDesign AdditiveBox/de

## Beschreibung

Fügt einen einfachen Quader in den aktiven Körper (body) als Basisformelement ein oder vereinigt ihn mit den bereits bestehenden Formelementen.

<img alt="" src=images/PartDesign_AdditiveBox_example.png  style="width:200px;">

## Anwendung

1.  Drücke die **<img src="images/PartDesign_AdditiveBox.svg" width=24px> '''Additiver Quader'''** Schaltfläche. **Hinweis**: Der Additive Quader ist Teil eines Symbolmenüs mit der Bezeichnung *Erstellen eines additiven Grundelements*. Nach dem Start von FreeCAD wird der Additive Quader in der Werkzeugleiste angezeigt. Wenn ein anderes Grundelement angezeigt wird, klicke auf den Abwärtspfeil neben dem Symbol und wähle Additiver Quader im Menü.
2.  Lege die Parameter für Grundelemente und [Anhang](Part_EditAttachment/de.md).
3.  Klicke **OK**.
4.  Unter dem aktiven Körper erscheint eine Quaderfunktion.

## Optionen

Der Quader kann auf zwei verschiedene Weisen bearbeitet werden:

-   Durch Doppelklick in der Baumstruktur oder durch Rechtsklick und Auswahl von **Grundkörper bearbeiten** in dem Kontextmenü. Dies öffnet den Dialog „Parameter des Grundkörpers" in dem Aufgabenpaneel.
-   Mittels der [Eigenschaften-Palette](Property_editor/de.md) im Reiter Daten.

## Eigenschaften

-    {{PropertyData/de|Attachment}}: Bestimmt den Befestigungsmodus und den Befestigungsversatz. Siehe [Anhang](Part_EditAttachment/de.md).

-    {{PropertyData/de|Label}}: Die vom Benutzer vergebene Bezeichung für das Quader-Objekt. Dies kann nach Bedarf geändert werden.

-    {{PropertyData/de|Length}}: Die Länge des Quaders in der X-Richtung.

-    {{PropertyData/de|Width}}: Die Länge des Quaders in der Y-Richtung.

-    {{PropertyData/de|Height}}: Die Länge des Quaders in der Z-Richtung.





{{PartDesign Tools navi

}}

---
[documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign AdditiveBox/de
