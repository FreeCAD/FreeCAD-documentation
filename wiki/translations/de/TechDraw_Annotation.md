---
 GuiCommand:
   Name: TechDraw Annotation
   Name/de: TechDraw Beschriftung
   MenuLocation: TechDraw , Anmerkungen , Anmerkung einfügen
   Workbenches: TechDraw_Workbench/de
   SeeAlso: TechDraw_RichTextAnnotation/de
---

# TechDraw Annotation/de



## Beschreibung

Das Werkzeug **TechDraw Beschriftung** fügt einem Zeichnungsblatt einen Textblock hinzu.

<img alt="" src=images/AnnotationSample.png  style="width:250px;"> 
*Beschriftung auf einem Zeichnungsblatt*



## Anwendung

1.  Wenn mehrere Zeichnungsblätter im Dokument vorhanden sind: Wahlweise das gewünschte Zeichnungsblatt durch Auswahl in der [Baumansicht](Tree_view/de.md) aktivieren.
2.  Es gibt mehrere Möglichkeiten, das Werkzeug aufzurufen:
    -   Die Schaltfläche **<img src="images/TechDraw_Annotation.svg" width=16px> [Anmerkung einfügen](TechDraw_Annotation.md)** drücken.
    -   Den Menüeintrag **TechDraw → Anmerkungen → <img src="images/TechDraw_Annotation.svg" width=16px> Anmerkung einfügen** auswählen.
3.  Wenn mehrere Zeichnungsblätter im Dokument vorhanden sind und noch kein Blatt aktiviert wurde, wird das Dialogfeld **Blattauswahl** geöffnet: {{Version/de|0.20}}
    1.  Das gewünschte Blatt auswählen.
    2.  Die Schaltfläche **OK** drücken.
4.  Ein Textblock mit *Default Text* erscheint auf der Zeichnung.
5.  Zum Bearbeiten des Textes wird der [ Eigenschafteneditor](Property_editor/de.md) verwendet.
6.  Wahlweise den Textblock auf die gewünschte Position ziehen.

![](images/UpdateAnnotation.png ) 
*Ändern der Beschriftung im Eigenschafteneditor*



## Hinweise

-   Einige Zeichen stören die interne Darstellung des Beschriftungstextes. Im Einzelnen sind dies die doppelten Anführungszeichen `"` sowie die Symbole kleiner als `<` und größer als `>`; diese müssen durch die HTML-Escape-Zeichen `&amp;quot;`, `&amp;lt;` und `&amp;gt;` entsprechend ersetzt werden. Siehe [Zeichenkodierungen in HTML](https://en.wikipedia.org/wiki/Character_encodings_in_HTML#HTML_character_references) für Einzelheiten.



## Eigenschaften

Die Beschriftung übernimmt alle anwendbaren grundlegenden Eigenschaften der Ansicht außer {{PropertyData/de|Scale}} (Maßstab). Stattdessen wird die {{PropertyData/de|Text Size}} (Schrifthöhe) verwendet.

-    {{PropertyData/de|Text}}: Der anzuzeigende Text.

-    {{PropertyData/de|Font}}: Der Name der zu verwendenden Schriftart. Für Beschriftungen wird die beste Übereinstimmung der installierten Schriftarten verwenden.

-    {{PropertyData/de|Text Color}}: Die Farbe des Textes.

-    {{PropertyData/de|Text Size}}: Die Schrifthöhe.

-    {{PropertyData/de|Max Width}}: Die maximale Breite des Beschriftungsblocks. -1 gibt keine maximale Breite an.

-    {{PropertyData/de|LineSpace}}: Einstellung des Zeilenabstands (%).

-    {{PropertyData/de|Text Style}}: \"Normal\", \"Bold\", \"Italic\", \"Bold-Italic\" (normal, fett, kursiv, fett-kursiv)



## Skripten

Siehe auch: [Autogenerierte API Dokumentation](https://freecad.github.io/SourceDoc/) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Das neue Werkzeug Beschriftung kann in [Makros](Macros/de.md) und von der [Python](Python/de.md)-Konsole aus mit den folgenden Funktionen verwendet werden:


```python
anno = FreeCAD.ActiveDocument.addObject('TechDraw::DrawViewAnnotation','TestAnno')
anno.Text = ['Different Text']
anno.TextStyle = 'Bold'
rc = page.addView(anno)
```





{{TechDraw Tools navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw Annotation/de
