---
- GuiCommand:
   Name:PartDesign AdditiveCone
   Name/de:PartDesign KegelHinzufügen
   MenuLocation:Part Design - Grundkörper hinzufügen - Kegel
   Workbenches:[PartDesign](PartDesign_Workbench/de.md)
   Version:0.17
   SeeAlso:[PartDesign AuswahlGründkörperHinzufügen](PartDesign_CompPrimitiveAdditive/de.md), [PartDesign KegelAbziehen](PartDesign_SubtractiveCone/de.md)
---

# PartDesign AdditiveCone/de

## Beschreibung

Fügt einen Kegel-Grundkörper in den aktiven Körper (Body-Objekt) als Basisformelement ein oder vereinigt ihn mit den bereits vorhandenen Formelementen.

<img alt="" src=images/PartDesign_AdditiveCone_example.png  style="width:200px;">

## Anwendung

1.  Die Schaltfläche **<img src="images/PartDesign_AdditiveCone.svg" width=24px> '''Kegel'''** drücken. **Hinweis**: Der Kegel ist Teil eines Symbolmenüs mit der Bezeichnung *Grundkörper hinzufügen*. Nach dem Start von FreeCAD wird der Quader in der Werkzeugleiste angezeigt. Um zur Schaltfläche Kegel zu gelangen, den Abwärtspfeil neben dem sichtbaren Symbol anklicken und Kegel im Menü auswählen.

2.  Parameter des Grundkörpers (für einen spitzen Kegel wird einer der Radien auf Null gesetzt) und [Befestigung](Part_EditAttachment/de.md) festlegen.

3.  
    **OK**klicken.

4.  Ein Cone-Objekt (Formelement) erscheint unter dem aktiven Körper (in der Baumansicht).

## Optionen

Der Kegel kann nach der Erstellung auf zwei Arten bearbeitet werden:

-   Durch Doppelklick in der Baumstruktur oder durch Rechtsklick und Auswahl von **Grundkörper bearbeiten** im Kontextmenü. Dies öffnet den Dialog „Parameter des Grundkörpers" im Aufgabenbereich.
-   Mit Hilfe des [Eigenschafteneditors](Property_editor/de.md).

## Eigenschaften

-    **Attachment**: Bestimmt den Befestigungsmodus und den Befestigungsversatz. Siehe [Part Befestigung](Part_EditAttachment/de.md).

-    **Label**: Die vom Benutzer vergebene Bezeichung für den Kegel (Cone-Objekt). Dies kann nach Bedarf geändert werden.

-    **Radius1**: Der Wert des Radius an der Kegelbasis.

-    **Radius2**: Der Wert des Radius an der Kegeloberseite. Ein anderer Wert als Null erzeugt einen Kegelstumpf.

-    **Height**: Die Höhe des Kegels entlang seiner Achse.

-    **Angle**: Der Rotationswinkel des (halben) Querschnitts (360° ergeben einen ganzen Kegel).





{{PartDesign_Tools_navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign AdditiveCone/de
