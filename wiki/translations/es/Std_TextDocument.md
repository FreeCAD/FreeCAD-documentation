---
 GuiCommand:
   Name: Std TextDocument
   MenuLocation: Tools , Add text document
   Workbenches: All
   Version: 0.19
   SeeAlso: Draft ShapeString, Draft Text
---

# Std TextDocument/es



## Descripción

The **Std TextDocument** command creates an object capable of holding arbitrary text. This element can be used to write general information or documentation about the model.



## Uso

1.  Select the **Tools → <img src="images/Std_TextDocument.svg" width=16px> Add text document** option from the menu.
2.  Double-click the newly created object in the [Tree view](Tree_view.md) to open a tab in which to write text.
3.  Add text.
4.  Close the tab and save the file when asked.



## Propiedades



### Vista


{{TitleProperty|Editor}}

-    **Font Name|Font**: a font name, for example, {{Value|Ubuntu Mono}}.

-    **Font Size|Float**: a font size in points, for example, {{Value|11}}.

-    **Read Only|Bool**: it defaults to `False`. If set to `True` the text cannot be edited.

-    **Syntax Highlighter|Enumeration**: it defaults to {{Value|None}}. If set to {{Value|Python}}, the text will be highlighted like the [Python console](Python_console.md).



## Programación


<div class="mw-translate-fuzzy">


**Ver también:**

[Conceptos básicos de scripting en FreeCAD](FreeCAD_Scripting_Basics/es.md), y [Objetos con scripting](scripted_objects/es.md).


</div>

See [Part Feature](Part_Feature.md) for the general information on adding objects to a document.

An `App::TextDocument` object is created with the `addObject()` method of the document. Once a TextDocument exists, its textual information is stored in its `Text` attribute. This attribute can be used in other objects, for example, as the string in a **<img src="images/Draft_ShapeString.svg" width=16px> [Draft ShapeString](Draft_ShapeString.md)**.


```python
import FreeCAD as App
import Draft

doc = App.newDocument()
obj = doc.addObject("App::TextDocument", "Text_document")
obj.Text = "textual information"
doc.recompute()

obj2 = Draft.makeShapeString(obj.Text, "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 10)
doc.recompute()
```





{{Std_Base_navi

}}



---
⏵ [documentation index](../README.md) > Std TextDocument/es
