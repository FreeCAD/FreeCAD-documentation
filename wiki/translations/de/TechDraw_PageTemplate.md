---
- GuiCommand:
   Name:TechDraw PageTemplate
   Name/de:TechDraw Seitenvorlage
   MenuLocation:TechDraw → Page → Neues Zeichnungsblatt aus einer Vorlage erstellen
   Workbenches:[TechDraw](TechDraw_Workbench/de.md)
   SeeAlso:[TechDraw Standardseite](TechDraw_PageDefault/de.md), [TechDraw Vorlagen](TechDraw_Templates/de.md)
---

# TechDraw PageTemplate/de



## Beschreibung

Das Werkzeug **TechDraw Seitenvorlage** erstellt ein neues Page-Objekt (Zeichnungsblatt) unter Verwendung der in einem Dialogfeld ausgewählten Vorlagendatei.

Das Startverzeichnis für das Dialogfeld kann in den [TechDraw Einstellungen](TechDraw_Preferences/de.md) festgelegt werden.

<img alt="" src=images/A4_Landscape_ISO7200_Pep.svg  style="width:400px;"> 
*Eine der Vorlagen, die TechDraw mitgeliefert: A4_Landscape_ISO7200_Pep.svg*



## Anwendung

1.  Ein aktives Dokument muss vorhanden sein.
2.  Es gibt mehrere Möglichkeiten, das Werkzeug aufzurufen:
    -   Die Schaltfläche **<img src="images/TechDraw_PageTemplate.svg" width=16px> [Neues Zeichnungsblatt aus einer Vorlage erstellen](TechDraw_PageTemplate/de.md)** drücken.
    -   Den Menüeintrag **TechDraw → Page → <img src="images/TechDraw_PageTemplate.svg" width=16px> Neues Zeichnungsblatt aus einer Vorlage erstellen** auswählen.



## Eigenschaften

Siehe [TechDraw Standardseite](TechDraw_PageDefault/de#Eigenschaften.md).



## Skripten

Siehe auch: [Autogenerierte API Dokumentation](https://freecad.github.io/SourceDoc/) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Ein Zeichnungsblatt, das auf einer ausgewählten Vorlage basiert, kann mit [Makros](Macros/de.md) und von der [Python](Python/de.md)-Konsole aus mit den folgenden Funktionen erstellt werden:


```python
import FreeCAD as App
from PySide import QtGui

doc = App.ActiveDocument
default_dir = App.getResourceDir() + "Mod/TechDraw/Templates"
param = App.ParamGet("User parameter:BaseApp/Preferences/Mod/TechDraw/Files")
template_dir = param.GetString("TemplateDir", default_dir)

template_file = QtGui.QFileDialog.getOpenFileName(QtGui.QApplication.activeWindow(),
                                                  "Select a Template File", 
                                                  template_dir,
                                                  "Template (*.svg)")
                                                  
page = doc.addObject("TechDraw::DrawPage", "Page")
template = doc.addObject("TechDraw::DrawSVGTemplate", "Template")
template.Template = template_file[0]
page.Template = template

doc.recompute()
```



### Editierbare Textfelder 


**Siehe auch:**

[TechDraw Vorlagen](TechDraw_Templates/de.md) für mehr Informationen zur Erstellung von Vorlagen.

Sobald ein neues Blatt erstellt wurde, enthält sein Attribut `Template` ein Wörterbuch (Dictionary-Objekt) `EditableTexts` mit den Namen der editierbaren Felder (Keys) und ihren Textinhalten (Values). Dieses Wörterbuch kann in eine Variable kopiert, geändert und dann erneut dem Attribut `EditableTexts` zugewiesen werden, um die Änderungen darzustellen.


```python
page = FreeCAD.ActiveDocument.Page
texts = page.Template.EditableTexts

for key, value in texts.items():
    print("{0} = {1}".format(key, value))

texts["FC-Title"] = "The title of my page"
page.Template.EditableTexts = texts
```





{{TechDraw Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw PageTemplate/de
