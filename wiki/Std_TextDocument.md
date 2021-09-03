---
- GuiCommand:
   Name:Std TextDocument
   MenuLocation:Tools → Add text document
   Workbenches:All
   Version:0.19
   SeeAlso:[Draft ShapeString](Draft_ShapeString.md), [Draft Text](Draft_Text.md)
---

## Description

The **Std TextDocument** command creates an object capable of holding arbitrary text. This element can be used to write general information or documentation about the model.

## Usage

1.  Select the {{MenuCommand|Tools → Add text document}} option from the menu.
2.  Double-click the newly created object in the [tree view](tree_view.md) to open a tab in which to write text.
3.  Add text.
4.  Close the tab and save the file when asked.

## Properties

### View


{{TitleProperty|Editor}}

-    **Font Name|Font**: a font name, for example, {{Value|Ubuntu Mono}}.

-    **Font Size|Float**: a font size in points, for example, {{Value|11}}.

-    **Read Only|Bool**: it defaults to `False`. If set to `True` the text cannot be edited.

-    **Syntax Highlighter|Enumeration**: it defaults to {{Value|None}}. If set to {{Value|Python}}, the text will be highlighted like the [Python console](Python_console.md).

## Scripting


**See also:**

[FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md), and [scripted objects](scripted_objects.md).

See [Part Feature](Part_Feature.md) for the general information on adding objects to a document.

An `App::TextDocument` object is created with the `addObject()` method of the document. Once a TextDocument exists, its textual information is stored in its `Text` attribute. This attribute can be used in other objects, for example, as the string in a **<img src="images/Draft_ShapeString.svg" width=16px> [Draft ShapeString](Draft_ShapeString.md)**.

 
```python
import FreeCAD as App
import Draft

doc = App.newDocument()
obj = App.ActiveDocument.addObject("App::TextDocument", "Text_document")
obj.Text = "textual information"
App.ActiveDocument.recompute()

obj2 = Draft.makeShapeString(obj.Text, "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 10)
App.ActiveDocument.recompute()
```




 {{Std Base navi}}  
