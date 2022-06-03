---
- GuiCommand   *
   Name   *Std TextDocument
   MenuLocation   *Tools → Add text document
   Workbenches   *All
   Version   *0.19
   SeeAlso   *[Draft ShapeString](Draft_ShapeString.md), [Draft Text](Draft_Text.md)
---

# Std TextDocument/de


<div class="mw-translate-fuzzy">

## Beschreibung


</div>


<div class="mw-translate-fuzzy">

[Std TextDocumenterstellt](Std_TextDocument/de.md) ein Objekt, das beliebigen Text aufnehmen kann. Dieses Element kann verwendet werden, um allgemeine Informationen oder Dokumentationen über das Modell zu schreiben.


</div>


<div class="mw-translate-fuzzy">

## Anwendung


</div>


<div class="mw-translate-fuzzy">

1.  Gehe zum Menü {{MenuCommand/de|Werkzeuge → Textdokument hinzufügen}}.
2.  Doppelklicken Sie auf das neue Objekt, das in der [Baumansicht](tree_view.md) erstellt wurde, um eine Registerkarte zu öffnen, in der Du Text schreiben kannst.
3.  Text hinzufügen.
4.  Schließe die Registerkarte und speichere die Datei, wenn gefragt wird.


</div>

## Properties

### View


{{TitleProperty|Editor}}

-    **Font Name|Font**   * a font name, for example, {{Value|Ubuntu Mono}}.

-    **Font Size|Float**   * a font size in points, for example, {{Value|11}}.

-    **Read Only|Bool**   * it defaults to `False`. If set to `True` the text cannot be edited.

-    **Syntax Highlighter|Enumeration**   * it defaults to {{Value|None}}. If set to {{Value|Python}}, the text will be highlighted like the [Python console](Python_console.md).


<div class="mw-translate-fuzzy">

## Skripten


</div>


**Siehe auch   ***

[FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md), und [skriptgesteuerte Objekte](scripted_objects/de.md).

Siehe [Part Funktionen](Part_Feature/de.md) für allgemeine Informationen zum Hinzufügen von Objekten zu einem Dokument.


<div class="mw-translate-fuzzy">

Ein `App   *   *TextDocument` Objekt wird mit der `addObject()` Methode des Dokuments erstellt. Sobald ein TextDokument existiert, werden seine Textinformationen in seinem Attribut `Text` gespeichert. Dieses Attribut kann in anderen Objekten verwendet werden, z.B. als Zeichenkette in einem [Entwurf FormBand](Draft_ShapeString/de.md).


</div>


```python
import FreeCAD as App
import Draft

doc = App.newDocument()
obj = App.ActiveDocument.addObject("App   *   *TextDocument", "Text_document")
obj.Text = "textual information"
App.ActiveDocument.recompute()

obj2 = Draft.makeShapeString(obj.Text, "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 10)
App.ActiveDocument.recompute()
```





{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std TextDocument/de
