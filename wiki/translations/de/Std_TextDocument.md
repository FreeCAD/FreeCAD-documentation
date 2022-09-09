---
- GuiCommand   */de
   Name   *Std TextDocument
   Name/de   *Std Textdokument
   MenuLocation   *Werkzeuge → Textdokument hinzufügen
   Workbenches   *All
   Version   *0.19
   SeeAlso   *[Draft Textform](Draft_ShapeString/de.md), [Draft Text](Draft_Text/de.md)
---

# Std TextDocument/de

## Beschreibung

Der Befehl **Std Textdokument** erstellt ein Objekt, das beliebigen Text aufnehmen kann. Dieses Element kann verwendet werden, um allgemeine Informationen aufzuschreiben oder für die Dokumentation des Modells.

## Anwendung

1.  Den Menüeintrag {{MenuCommand/de|Werkzeuge → Textdokument hinzufügen}} auswählen.
2.  Das neu erstellte Objekt in der [Baumansicht](tree_view/de.md) doppelklicken, um eine Registerkarte zu öffnen, in die der Text geschrieben wird.
3.  Text hizufügen.
4.  Registerkarte schließen und die Datei speichern, wenn danach gefragt wird.

## Eigenschaften

### Ansicht


{{TitleProperty|Editor}}

-    {{PropertyView/de|Font Name|Font}}   * Schriftname, z.B. {{Value|Ubuntu Mono}}.

-    {{PropertyView/de|Font Size|Float}}   * Schrifthöhe in Punkt, z.B. {{Value|11}}.

-    {{PropertyView/de|Read Only|Bool}}   * Standardmäßig `False`. Wenn auf `True` gesetzt, kann der Text nicht editiert werden.

-    {{PropertyView/de|Syntax Highlighter|Enumeration}}   * Standardmäßig {{Value|None}}. Wenn auf {{Value|Python}} gesetzt, wird der Text wie in der [Python-Konsole](Python_console/de.md) hervorgehoben.

## Skripten


**Siehe auch   ***

[FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md), und [skriptgesteuerte Objekte](scripted_objects/de.md).

Siehe [Part Formelement](Part_Feature/de.md) für allgemeine Informationen zum Hinzufügen von Objekten zu einem Dokument.

Ein `App   *   *TextDocument`-Objekt (Textdokument) wird mit der `addObject()`-Methode des Dokuments erstellt. Sobald ein Textdokument existiert, werden seine Textinformationen in seinem Attribut `Text` gespeichert. Dieses Attribut kann in anderen Objekten verwendet werden, z.B. als Zeichenkette in einer **<img src="images/Draft_ShapeString.svg" width=16px> [Draft Textform](Draft_ShapeString/de.md)**.


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
