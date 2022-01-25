---
- GuiCommand:/de
   Name:TechDraw Annotation
   Name/de:TechDraw Anmerkung
   MenuLocation:TechDraw → Anmerkungen → Anmerkung einfügen
   Workbenches:[TechDraw](TechDraw_Workbench/de.md)
   SeeAlso:[Entwurf Text](Draft_Text/de.md), [Draft FormZeichenkette](Draft_ShapeString/de.md)
---

# TechDraw Annotation/de

## Beschreibung

Das Anmerkungswerkzeug fügt einen Textblock zu einem Zeichnungsblatt hinzu.

<img alt="" src=images/AnnotationSample.png  style="width:250px;"> 
*Anmerkung in einer Zeichnungsseite*

## Anwendung

1.  Wenn du mehrere Zeichnungsseiten in Ihrem Dokument haben, musst du die gewünschte Seite im Baum auswählen.
2.  Drücke die **<img src="images/TechDraw_Annotation.svg" width=24px> [Anmerkung einfügen](TechDraw_Annotation/de.md)** Schaltfläche
3.  Ein Textblock mit *Standardtext* wird auf der Seite erscheinen. Verwende den Eigenschaftseditor, um den Text zu ändern. Ziehe die Anmerkung an die gewünschte Position.
4.  Möglicherweise musst du auf **<img src="images/Std_Refresh.svg" width=16px> [Aktualisieren](Std_Refresh/de.md)** und/oder **<img src="images/TechDraw_RedrawPage.svg" width=16px> [Seite neu zeichnen](TechDraw_RedrawPage/de.md)**, damit sich dein Text ändert.

![](images/UpdateAnnotation.png ) 
*Ändern der Anmerkung über den Eigenschaftseditor*


**Hinweis:**

Einige Zeichen stören die interne Darstellung des Anmerkungstextes. Im Einzelnen sind dies die doppelten Anführungszeichen `"`, weniger als `<` und mehr als `>` Symbole; diese müssen durch HTML Escape Zeichen, `&amp;quot;`, `&amp;lt;` und `&amp;gt;` ersetzt werden. Siehe [Zeichenkodierungen in HTML](https://en.wikipedia.org/wiki/Character_encodings_in_HTML#HTML_character_references) für Einzelheiten.

## Eigenschaften

Die Anmerkung übernimmt alle anwendbaren grundlegenden Ansichtseigenschaften außer **Maßstab**. Verwende stattdessen die **TextGröße** Eigenschaft.

-    **Text**: Der anzuzeigende Text.

-    **Font**: Der Name der zu verwendenden Schriftart. Für Anmerkungen wird die beste Übereinstimmung der installierten Schriftarten verwenden.

-    **TextColor**: Die Farbe des Textes.

-    **TextSize**: Die Größe des Textes.

-    **MaxWidth**: Die maximale Breite des Anmerkungsblocks. -1 gibt keine maximale Breite an.

-    **LineSpace**: Einstellung des Zeilenabstands (%).

-    **TextStyle**: \"Normal\", \"Fett\", \"Kursiv\", \"Fett-Kursiv\"

## Skripten


**Siehe auch:**

[TechDraw Anwendungsschnittstelle](TechDraw_API/de.md) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Das Neue Anmerkungswerkzeug kann in [Makros](Macros/de.md) und aus der [Python](Python/de.md) Konsole mit den folgenden Funktionen verwendet werden:


```python
anno = FreeCAD.ActiveDocument.addObject('TechDraw::DrawViewAnnotation','TestAnno')
anno.Text = ['Different Text']
anno.TextStyle = 'Bold'
rc = page.addView(anno)
```

## Hinweise


<div class="mw-translate-fuzzy">





</div>


{{TechDraw Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw Annotation/de
