---
- GuiCommand   */ru
   Name/ru   *Вставить страницу используя шаблон
   Name   *TechDraw_PageTemplate
   MenuLocation   *TechDraw → Вставить страницу используя шаблон
   Workbenches   *[TechDraw](TechDraw_Workbench/ru.md)
   SeeAlso   *[Вставить страницу по умолчанию](TechDraw_PageDefault/ru.md), [Шаблоны](TechDraw_Templates/ru.md)
---

# TechDraw PageTemplate/ru


</div>

## Описание

The New Pick tool creates a new Page object using the template file selected from a dialog.

The starting directory for the dialog can be specified in the [TechDraw Preferences](TechDraw_Preferences.md).

<img alt="" src=images/A4_Landscape_ISO7200_Pep.svg  style="width   *400px;">



*One of the templates that comes with TechDraw   * A4 ISO 7200_Pep, page in landscape orientation, with editable text fields*

## Применение

-   Press the **<img src="images/TechDraw_PageTemplate.svg" width=16px> [Insert Page using Template](TechDraw_PageTemplate.md)** button

## Свойства

See [TechDraw PageDefault](TechDraw_PageDefault#Properties.md).

## Программирование


**См. так же   ***

[TechDraw API](TechDraw_API/ru.md) и [Основы составления скриптов FreeCAD](FreeCAD_Scripting_Basics/ru.md).

The New Pick tool can be used in [macros](Macros.md) and from the [Python](Python.md) console by using the following functions   * 
```python
templateFileSpec = QtGui.QFileDialog.getOpenFileName(self.baseWidget,
                                                     dialogCaption, 
                                                     dialogDir,
                                                     dialogFilter)
page = FreeCAD.ActiveDocument.addObject('TechDraw   *   *DrawPage','Page')
template = FreeCAD.ActiveDocument.addObject('TechDraw   *   *DrawSVGTemplate','Template')
template.Template = templateFileSpec
page.Template = FreeCAD.ActiveDocument.Template
```

-   Creates a new Page in the current document

### Editable text fields 


**See also   ***

[TechDraw Templates](TechDraw_Templates.md) for more information on creating templates.

See the information in [Insert Default Page](TechDraw_PageDefault.md) to programmatically change the editable text fields in a page template.





{{TechDraw Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw PageTemplate/ru
