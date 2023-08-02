---
- GuiCommand:
   Name: TechDraw Annotation
   Name/de: TechDraw Beschriftung
   MenuLocation: TechDraw -> Anmerkungen -> Anmerkung einfügen
   Workbenches: TechDraw_Workbench/de
   SeeAlso: Draft_Text/de, Draft_ShapeString/de
---

# TechDraw Annotation/de


</div>



## Beschreibung

Das Werkzeug **TechDraw Beschriftung** fügt einem Zeichnungsblatt einen Textblock hinzu.

<img alt="" src=images/AnnotationSample.png  style="width:250px;"> 
*Beschriftung auf einem Zeichnungsblatt*



## Anwendung


<div class="mw-translate-fuzzy">

1.  Sind mehrere Zeichnungsblätter in einem Dokument vorhanden, muss die gewünschte Seite im Baum ausgewählt werden.
2.  Die Schaltfläche **<img src="images/TechDraw_Annotation.svg" width=24px> [Anmerkung einfügen](TechDraw_Annotation/de.md)** drücken.
3.  Ein Textblock mit *Default Text* erscheint auf der Seite. Zum Ändern des Textes, wird der Eigenschafteneditor verwendet. Die Anmerkung an die gewünschte Position ziehen.
4.  Möglicherweise musst **<img src="images/Std_Refresh.svg" width=16px> [Aktualisieren](Std_Refresh/de.md)** und/oder **<img src="images/TechDraw_RedrawPage.svg" width=16px> [Seite neu zeichnen](TechDraw_RedrawPage/de.md)** gedrückt werden, damit sich der Text ändert.


</div>

![](images/UpdateAnnotation.png )


<div class="mw-translate-fuzzy">



*Ändern der Beschriftung im Eigenschafteneditor*


</div>



## Hinweise


<div class="mw-translate-fuzzy">


**Hinweis:**

Einige Zeichen stören die interne Darstellung des Beschriftungstextes. Im Einzelnen sind dies die doppelten Anführungszeichen `"` sowie die Symbole kleiner als `<` und größer als `>`; diese müssen durch die HTML-Escape-Zeichen `&amp;quot;`, `&amp;lt;` und `&amp;gt;` entsprechend ersetzt werden. Siehe [Zeichenkodierungen in HTML](https://en.wikipedia.org/wiki/Character_encodings_in_HTML#HTML_character_references) für Einzelheiten.


</div>



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
