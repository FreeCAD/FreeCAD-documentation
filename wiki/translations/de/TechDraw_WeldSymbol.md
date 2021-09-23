---
- GuiCommand:/de
   Name:TechDraw WeldingSymbol
   Name/de:TechDraw SchweißSymbol
   Icon:techdraw-weldsymbol.svg
   MenuLocation:TechDraw → Schweißinformation zur Führungslinie hinzufügen
   Workbenches:[TechDraw](TechDraw_Workbench/de.md)
   Version:0.19
   SeeAlso:[TechDraw Führungslinie](TechDraw_LeaderLine/de.md)
---

## Beschreibung

Das SchweißSymbol Werkzeug fügt Schweißspezifikationen einer bestehenden Führungslinie hinzu.

<img alt="" src=images/TechDraw_WeldingSymbol_example.png  style="width:330px;"> 
*Schweißspezifikation zu einer Führungslinie hinzugefügt*

## Anwendung

1.  Wähle eine vorhandene [Führungslinie](TechDraw_LeaderLine/de.md).
2.  Drücke die **<img src="images/techdraw-weldsymbol.svg" width=16px> Schweißinformationen zur Führungslinie hinzufügen** Schaltfläche.
3.  Ein Aufgabendialog wird geöffnet. Er ermöglicht es, individuelle Schweißsymbole und begleitenden Text festzulegen, die der Führungslinie hinzugefügt werden sollen.
4.  Um den Dialog zu verlassen und die Änderungen zu speichern, drücke die OK Taste. Um das Dialogfeld zu verlassen, ohne zu speichern, drücke die Schaltfläche Abbrechen.
5.  Nachdem das Schweisssymbol erstellt wurde, kann es durch Doppelklicken auf das Schweisssymbol im Baum bearbeitet werden.

## Eigenschaften

### Schweißsymbol

-    {{PropertyData/de|Rundum}}: Zeigt das Kreis-Symbol am Knick in der Führungslinie.

-    {{PropertyData/de|FeldSchweißung}}: Zeigt das *FeldSchweißsymbol* (Flagge) an der Knickstelle der Führungslinie.

-    {{PropertyData/de|ErsatzSchweißung}}: Versetzt das untere Symbol, um wechselseitig Schweißungen anzuzeigen.

-    {{PropertyData/de|SchwanzText}}: Text, der am Ende der Führungslinie angezeigt werden soll

### Kacheln

Jedes einzelne Symbol (\"Pfeilseite\" und \"andere Seite\") wird durch ein \"Kachel\" Objekt dargestellt. Einem Schweißsymbol sind 1 oder 2 Kacheln zugeordnet. Die Eigenschaften können geändert werden. Dazu muß in der Baumansicht auf die jeweilige Schweißkachel geklickt werden. Unten im Eigenschaftsfeld können dann Änderungen vorgenommen werden:

-    {{PropertyData/de|Kachel Eltern}}: das ursprüngliche Schweißsymbol

-    {{PropertyData/de|Kachelreihe}}: Reihe der Kachel. 0 bedeutet oberhalb der Linie, -1 unterhalb der Linie. **Hinweis:** Wenn du die Reihe einer Kachel änderst, musst du auch die Kachel für die zweite Seite ändern! Auf diesem Weg kannst du die Seiten tauschen.

-    {{PropertyData/de|Kachel Säule}}: Im Moment = 0, zur Zeit noch nicht änderbar.

-    {{PropertyData/de|Symboldatei}}: Verzeichnis und Dateiname der svg Datei für das Symbol.

-    {{PropertyData/de|LinkerText}}: Text, der links neben dem svg Symbol angezeigt werden soll.

-    {{PropertyData/de|MittenText}}: Text, der oberhalb/unterhalb des svg Symbols angezeigt werden soll.

-    {{PropertyData/de|RechterText}}: Text, der rechts neben dem svg Symbol angezeigt werden soll.

## Skripten


**Siehe auch:**

[TechDraw API](TechDraw_API/de.md) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Das SchweißSymbol Werkzeug kann in [Makros](Macros/de.md) und von der [Python](Python/de.md) Konsole aus mit den folgenden Funktionen verwendet werden:


```python
symbolName = "DrawWeldSymbol001")
symbolType = "TechDraw::DrawWeldSymbol"
App.activeDocument().addObject(symbolType, symbolName)
App.activeDocument().Page.addView(App.activeDocument().DrawWeldSymbol001)
App.activeDocument().DrawWeldSymbol001.Leader = myLeader
App.activeDocument().DrawWeldSymbol001.AllAround = True
App.activeDocument().DrawWeldSymbol001.FieldWeld = True
App.activeDocument().DrawWeldSymbol001.AlternatingWeld = True
App.activeDocument().DrawWeldSymbol001.TailText = "process text"

tileName = "DrawTileWeld001"
tileType = "TechDraw::DrawTileWeld"
App.activeDocument().addObject(tileType, tileName)
App.activeDocument().DrawTileWeld001.TileParent = App.activeDocument().DrawWeldSymbol001
App.activeDocument().DrawTileWeld001.TileRow = 0
App.activeDocument().DrawTileWeld001.TileColumn = 0
App.activeDocument().DrawTileWeld001.SymbolFile = fullPathToMySvgFile
App.activeDocument().DrawTileWeld001.LeftText = "left text"
App.activeDocument().DrawTileWeld001.RightText = "right text"
App.activeDocument().DrawTileWeld001.CenterText = "center text"
```

## Svg Symbol Tiles 


<div class="mw-translate-fuzzy">

## Svg Symbol Kacheln 

-   Einzelne Symbole werden durch 64x64 Pixel Svg Dateien gebildet. Zusätzliche Symbole können in einem SVG Programm wie z.B. Inkscape [Inkscape](https://en.wikipedia.org/wiki/Inkscape) aus einem der mitgelieferten Symbole als Vorlage erstellt werden.

<img alt="" src=images/Techdraw-WeldingSymbolLayoutArrow.svg  style="width:128px;"> <img alt="" src=images/Techdraw-WeldingSymbolLayoutOther.svg  style="width:128px;">


</div>

<img alt="" src=images/Techdraw-WeldingSymbolLayoutArrow.svg  style="width:128px;"> <img alt="" src=images/Techdraw-WeldingSymbolLayoutOther.svg  style="width:128px;">


<div class="mw-translate-fuzzy">

\* Einzelne Symbole werden durch SVG Dateien mit 64x64 (nominal) Pixeln gebildet. Die Kacheln haben einen \"Rand\" von 4px. Der Rand sorgt dafür, dass sich Führungslinie und Symbol gut treffen.

-   Das Symbol wird in Schwarz auf einem transparenten Hintergrund gezeichnet. Die Strichstärke beträgt 0,5 mm.
-   Die Führungslinie verläuft unterhalb der Symbole für die Pfeilseite und oberhalb der Symbole für die \"andere\" Seite.
-   Es gibt keinen besonderen Namensstandard, außer dass bei Bedarf \"Auf/Ab\" an die Symbole der Pfeil- und der anderen Seite angehängt wird.


</div>

## Hinweise

-   Du kannst dein Schweißsymbol bearbeiten, indem du in der Baumansicht darauf doppelklickst. Ein Doppelklick in den Grafikbereich wird noch nicht unterstützt.
-   Es gibt einen [Einstellungsparameter](TechDraw_Preferences/de.md) für das Standard Schweißsymbolverzeichnis. Du kannst deine eigenen Symbole in einem persönlichen Verzeichnis hinzufügen.





{{TechDraw Tools navi

}} 
