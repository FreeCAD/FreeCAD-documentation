---
- GuiCommand   *
   Name   *TechDraw PageTemplate
   MenuLocation   *TechDraw → Insert Page using Template
   Workbenches   *[TechDraw](TechDraw_Workbench.md)
   SeeAlso   *[TechDraw PageDefault](TechDraw_PageDefault.md), [TechDraw Templates](TechDraw_Templates.md)
---

# TechDraw PageTemplate

## Description

The New Pick tool creates a new Page object using the template file selected from a dialog.

The starting directory for the dialog can be specified in the [TechDraw Preferences](TechDraw_Preferences.md).

 <img alt="" src=images/A4_Landscape_ISO7200_Pep.svg  style="width   *400px;">

 
*One of the templates that comes with TechDraw   * A4 ISO 7200_Pep, page in landscape orientation, with editable text fields*

## Usage

-   Press the **<img src="images/TechDraw_PageTemplate.svg" width=16px> [Insert Page using Template](TechDraw_PageTemplate.md)** button

## Properties

See [TechDraw PageDefault](TechDraw_PageDefault#Properties.md).

## Scripting


**See also   ***

[TechDraw API](TechDraw_API.md) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

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




 {{TechDraw Tools navi}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw PageTemplate
