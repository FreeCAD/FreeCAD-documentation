---
- GuiCommand:/de
   Name:TechDraw RichTextAnnotation
   Name/de:TechDraw FormatierteTextAnmerkung
   MenuLocation:TechDraw → Anmerkungen → Einfügen Formatierte Text Anmerkungen
   Workbenches:[TechDraw](TechDraw_Workbench/de.md)
   Version:0.19
   SeeAlso:[TechDraw Vorlagen](TechDraw_Templates/de.md), [Entwurf SVG](Draft_SVG/de.md), [TechDraw Führungslinie](TechDraw_LeaderLine/de.md)
---

## Beschreibung

Das FormatierterTextBlock Werkzeug fügt einen formatierten Anmerkungsblock zu einer [Führunglinie](TechDraw_LeaderLine/de.md) oder einer Ansicht hinzu.

<img alt="" src=images/TechDraw_RichTextBlock_sample.png  style="width:220px;"> 
*Eigenständiger FormatierterTextBlock*

## Anwendung

1.  Drücke die **<img src="images/TechDraw_RichTextAnnotation.svg" width=16px> [Formatierte Text Anmerkung](TechDraw_RichTextAnnotation/de.md)** Schaltfläche
2.  Ein Aufgabendialog wird geöffnet. Der Dialog ermöglicht eine schnelle Eingabe von Text.
3.  Die **Formatierter Text Editor starten** Schaltfläche öffnet einen voll ausgestatteten Editor. Drücke auf das Symbol Speichern, um deine Änderungen aufzuzeichnen.
4.  Nachdem der Block erstellt wurde, kann er durch Doppelklicken auf den FormatierterTextBlock im Baum bearbeitet werden.
5.  Um den Block an eine [Führungslinie](TechDraw_LeaderLine/de.md) anzuhängen, wähle die Linie aus, bevor du das FormatierterTextBlock Werkzeug startest.

## Eigenschaften

-    {{PropertyData/de|X,Y}}: Die Position des Blocks. Relativ zum Ende der Zeile, wenn sie an eine [LeaderLine](TechDraw_LeaderLine/de.md) angehängt ist, ansonsten ist dies die Position auf der Seite.

-    {{PropertyData/de|AnzeigeRahmen}}: Zeichnet einen Umriss um den Block herum.

-    {{PropertyData/de|MaxBreite}}: Begrenzt die horizontale Größe des Blocks. Ein Wert von -1 ist für unbegrenzte Breite.

-    {{PropertyData/de|AnmerkungsText}}: Der HTML-Text des Blocks.

## Skripten


**Siehe auch:**

[TechDraw API](TechDraw_API/de.md) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Das FormatierterTextBlock Werkzeug kann in [Makros](Macros/de.md) und aus der [Python](Python/de.md) Konsole verwendet werden. 
```python
myPage = FreeCAD.ActiveDocument().Page
myBase = FreeCAD.ActiveDocument().View
blockObj = FreeCAD.ActiveDocument.addObject('TechDraw::DrawRichAnno','DrawRichAnno')
FreeCAD.activeDocument().myPage.addView(blockObj)
blockObj.X = 5
blockObj.Y = 5
blockObj.AnnoText = myHTMLText
```

## Hinweise

-   Du kannst deinen FormatierterTextBlock bearbeiten, indem du in der Baumansicht darauf doppelklickst. Ein Doppelklick in den Grafikbereich wird noch nicht unterstützt.





{{TechDraw Tools navi

}}  
