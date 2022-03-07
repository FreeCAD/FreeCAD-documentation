---
- GuiCommand:/de
   Name:TechDraw PageTemplate
   Name/de:TechDraw SeitenVorlage
   MenuLocation:TechDraw → Seite aus Vorlage einfügen
   Workbenches:[TechDraw](TechDraw_Workbench/de.md)
   SeeAlso:[TechDraw Standardseite](TechDraw_PageDefault/de.md), [TechDraw Vorlagen](TechDraw_Templates/de.md)
---

# TechDraw PageTemplate/de


</div>

## Beschreibung

Das Neue Auswahl Werkzeug erstellt ein neues Seitenobjekt unter Verwendung der in einem Dialogfeld ausgewählten Vorlagendatei.

Das Startverzeichnis für das Dialogfenster kann in den [TechDraw Einstellungen](TechDraw_Preferences/de.md) festgelegt werden.

<img alt="" src=images/A4_Landscape_ISO7200_Pep.svg  style="width:400px;">



*Eine der Vorlagen, die mit TechDraw geliefert wird: A4 ISO 7200_Pep, Seite im Querformat, mit editierbaren Textfeldern*

## Anwendung

-   Drücke die **<img src="images/TechDraw_PageTemplate.svg" width=16px> [Seite mittels Vorlage einfügen](TechDraw_PageTemplate/de.md)** Schaltfläche

## Eigenschaften

See [TechDraw PageDefault](TechDraw_PageDefault#Properties.md).

## Skripten


**Siehe auch:**

[TechDraw Anwendungsschnittstelle](TechDraw_API/de.md) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Das Neue Auswahl Werkzeug kann in [Makros](Macros/de.md) und von der [Python](Python/de.md) Konsole aus mit den folgenden Funktionen verwendet werden: 
```python
templateFileSpec = QtGui.QFileDialog.getOpenFileName(self.baseWidget,
                                                     dialogCaption, 
                                                     dialogDir,
                                                     dialogFilter)
page = FreeCAD.ActiveDocument.addObject('TechDraw::DrawPage','Page')
template = FreeCAD.ActiveDocument.addObject('TechDraw::DrawSVGTemplate','Template')
template.Template = templateFileSpec
page.Template = FreeCAD.ActiveDocument.Template
```

-   Erstellt eine neue Seite im aktuellen Dokument

### Editierbare Textfelder 


**Siehe auch:**

[TechDraw Vorlagen](TechDraw_Templates/de.md) für mehr Informationen zur Erstellung von Vorlagen.

Siehe die Informationen in [Standardseite einfügen](TechDraw_PageDefault/de.md), um die editierbaren Textfelder in einer Seitenvorlage programmtechnisch zu ändern.





{{TechDraw Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw PageTemplate/de
