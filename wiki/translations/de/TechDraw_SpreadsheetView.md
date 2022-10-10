---
- GuiCommand   */de
   Name   *TechDraw SpreadsheetView
   Name/de   *TechDraw KalkulationstabelleAnsicht
   MenuLocation   *TechDraw → Einfügen Kalkulationstabelle Ansicht
   Workbenches   *[TechDraw](TechDraw_Workbench/de.md), [Kalkulationstabelle Arbeitsbereich](Spreadsheet_Workbench/de.md)
---

# TechDraw SpreadsheetView/de

## Beschreibung

Dieses Werkzeug ermöglicht dir eine [Kalkulationstabellen](Spreadsheet_Workbench/de.md) Ansicht auf einer gewählten [Seite](TechDraw_Workbench/de.md) zu platzieren.

![](images/TechDraw_Spreadsheetview.png ) 
*In das TechDraw Zeichnungsblatt eingefügtes Rechenblattelement*

## Anwendung

1.  Wähle ein Tabellenblatt in der [Bauamsicht](Tree_view/de.md) aus.
2.  Drücke die **<img src="images/TechDraw_SpreadsheetView.svg" width=16px> [Einfügen Kalkulationstabelle Ansicht](TechDraw_SpreadsheetView/de.md)**-Schaltfläche

## Eigenschaften

Siehe auch [TechDraw Ansicht](TechDraw_View/de#Eigenschaften.md)

### Daten


{{TitleProperty|Spreadsheet}}


<div class="mw-translate-fuzzy">

-    **Quelle**   * Das der Seite hinzuzufügende Arbeitsblatt

-    **Zellanfang**   * Die linke obere Zelle des Zellbereichs, der in diese Ansicht aufgenommen werden soll

-    **Zellenende**   * Die Zelle unten rechts des Zellbereichs, der in diese Ansicht aufgenommen werden soll

-    **Schriftart**   * Der Name der für Texte verwendeten Schriftart

-    **Farbe**   * Die Farbe von Linien und Texten, die keine in der Kalkulationstabelle angegebene Farbe haben

-    **Schriftgröße**   * Die Schriftgröße von Texten

-    **Linienbreite**   * Die Breite der Zellränder


</div>

## Hinweise

-   In {{VersionMinus|0.19}} some characters in spreadsheet cells will cause errors when displayed in a Spreadsheet View. These characters have to be XML encoded. Currently known characters are   * {{Incode|&}} (replace with {{Incode|&amp;amp;}}) and {{Incode|&lt;}} (replace with {{Incode|&amp;lt;}}). See also this [discussion](https   *//forum.freecadweb.org/viewtopic.php?p=629853#p629885) in the forum.





{{TechDraw Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw SpreadsheetView/de
