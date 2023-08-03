---
 GuiCommand:
   Name: TechDraw RichTextAnnotation
   Name/de: TechDraw FormatierteTextAnmerkung
   MenuLocation: TechDraw , Anmerkungen , Rich-Text-Anmerkungen einfügen
   Workbenches: TechDraw_Workbench/de
   Version: 0.19
   SeeAlso: TechDraw_Templates/de
---

# TechDraw RichTextAnnotation/de



## Beschreibung

Das Werkzeug **TechDraw FormatierteTextAnmerkung** fügt einer [Hinweislinie](TechDraw_LeaderLine/de.md) oder einer Ansicht einen formatierten Beschriftungsblock hinzu .

<img alt="" src=images/TechDraw_RichTextBlock_sample.png  style="width:220px;"> 
*Eigenständige FormatierteTextAnmerkung*



## Anwendung

1.  Wenn mehrere Zeichnungsblätter im Dokument vorhanden sind: Wahlweise das gewünschte Zeichnungsblatt durch Auswahl in der [Baumansicht](Tree_view/de.md) aktivieren.
2.  Um eine Rich-Text-Beschriftung an eine [Hinweislinie](TechDraw_LeaderLine/de.md) anzuhängen, wird die Linie in der [Baumansicht](Tree_view/de.md) oder auf dem Zeichnungsblatt ausgewählt.
3.  Es gibt mehrere Möglichkeiten, das Werkzeug aufzurufen:
    -   Die Schaltfläche **<img src="images/TechDraw_RichTextAnnotation.svg" width=16px> [Rich-Text-Anmerkung einfügen](TechDraw_RichTextAnnotation/de.md)** drücken.
    -   Den Menüeintrag **TechDraw → Anmerkungen → <img src="images/TechDraw_RichTextAnnotation.svg" width=16px> Rich-Text-Anmerkung einfügen** auswählen.
4.  Wenn mehrere Zeichnungsblätter im Dokument vorhanden sind und noch kein Blatt aktiviert wurde, wird das Dialogfeld **Blattauswahl** geöffnet: {{Version/de|0.20}}
    1.  Das gewünschte Blatt auswählen.
    2.  Die Schaltfläche **OK** drücken.
5.  Der Aufgaben-Bereich wird geöffnet und ermöglicht eine schnelle Eingabe von Text.
6.  Die Schaltfläche **Rich-Text-Editor starten** öffnet einen voll ausgestatteten Editor:
    1.  Ist die Texteingabe abgaschlossen, wird die Schaltfläche **<img src="images/Document-save.svg" width=16px>** gedrückt, um die Änderungen zu speichern und den Editor zu schließen.
7.  Die Schaltfläche **OK** drücken, um den Aufgaben-Bereich zu schließen.



## Hinweise

-   Nach der Erstellung kann ein RichTextAnnotation-Objekt mit einem Doppelklick auf dem Zeichnungsblatt zum Bearbeiten ausgewählt werden.



## Eigenschaften

-    {{PropertyData/de|X,Y}}: Die Position des Blocks; relativ zum Ende der Linie, wenn er an eine [Hinweisline](TechDraw_LeaderLine/de.md) angehängt ist, ansonsten ist dies die Position auf dem Zeichnungsblatt.

-    {{PropertyData/de|Show Frame}}: Zeichnet einen Rahmen um den Block herum.

-    {{PropertyData/de|Max Width}}: Begrenzt die (horizontale) Breite des Blocks. Ein Wert von -1 steht für eine unbegrenzte Breite.

-    {{PropertyData/de|Anno Text}}: Der HTML-Text des Blocks.



## Skripten

Siehe auch: [Autogenerierte API Dokumentation](https://freecad.github.io/SourceDoc/) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Das Werkzeug **FormatierteTextAnmerkung** kann in [Makros](Macros/de.md) und von der [Python](Python/de.md)-Konsole aus verwendet werden.


```python
myPage = FreeCAD.ActiveDocument().Page
myBase = FreeCAD.ActiveDocument().View
blockObj = FreeCAD.ActiveDocument.addObject('TechDraw::DrawRichAnno','DrawRichAnno')
FreeCAD.activeDocument().myPage.addView(blockObj)
blockObj.X = 5
blockObj.Y = 5
blockObj.AnnoText = myHTMLText
```





{{TechDraw Tools navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw RichTextAnnotation/de
