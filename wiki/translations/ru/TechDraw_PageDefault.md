---
- GuiCommand:/ru
   Name/ru:Вставить страницу по умолчанию
   Name:TechDraw_PageDefault
   MenuLocation:TechDraw → Вставить страницу по умолчанию
   Workbenches:[TechDraw](TechDraw_Workbench/ru.md)
   SeeAlso:[Вставить страницу используя шаблон](TechDraw_PageTemplate/ru.md), [Шаблоны TechDraw](TechDraw_Templates/ru.md)
---

## Описание

The New Default tool creates a new Page object using the the template file specified in the [TechDraw Preferences](TechDraw_Preferences.md).

<img alt="" src=images/A4_LandscapeTD.svg  style="width:400px;"> 
*Default template that comes with TechDraw: A4 page in landscape orientation, with editable text fields*

## Применение

-   Press the **<img src="images/TechDraw_PageDefault.svg" width=16px> [Insert Default Page](TechDraw_PageDefault.md)** button. (An active document must exist.)

## Примечания

-   If a Page is marked as \"do not keep updated\" either through the KeepUpdated Property or by the setting in Preferences, it will ignore changes in the 3D model. You may notice anomalies (missing geometry, missing Dimension values, etc) in the appearance of the Page. These will correct themselves once the Page is updated. The Page will have this icon <img alt="" src=images/TechDraw_Tree_Page_Unsync.svg  style="width:32px;"> in the tree while updating is suspended. This setting also affects the startup process. If the Page is marked \"do not keep updated\" it will not be drawn at program start.

If the default template is not specified in your user configuration file `user.cfg`, the tool will try 
```python
$INSTALL_DIR/Mod/TechDraw/Templates/A4_LandscapeTD.svg
```

Where `$INSTALL_DIR` is the directory where FreeCAD was installed, for example 
```python
/usr/share/freecad/Mod/TechDraw/Templates/A4_LandscapeTD.svg
```

## Свойства

-    **Projection Type**: Default projection type (First or Third Angle) for this Page.

-    **Keep Updated**: If false, Page is not updated with changes to the 3D model. Useful for complicated/slow drawings. See Notes.

-    **Template**: A link to this Page\'s [Template](TechDraw_Templates.md) object.

-    **Views**: A list of links to the Views on this Page.

-    **Scale**: Default scale for Views in this Page.

## Программирование


**См. так же:**

[TechDraw API](TechDraw_API/ru.md) и [Основы составления скриптов FreeCAD](FreeCAD_Scripting_Basics/ru.md).

The New Default tool can be used in [macros](Macros.md) and from the [Python](Python.md) console by using the following functions: 
```python
page = FreeCAD.ActiveDocument.addObject('TechDraw::DrawPage','Page')
template = FreeCAD.ActiveDocument.addObject('TechDraw::DrawSVGTemplate','Template')
template.Template = templateFileSpec
page.Template = FreeCAD.ActiveDocument.Template
```

-   Creates a new Page in the current document

### Editable text fields 


**See also:**

[TechDraw Templates](TechDraw_Templates.md) for more information on creating templates.

Once a new page has been created, its `Template` attribute holds an `EditableTexts` dictionary with the name of the editable fields (keys) and their textual values. Copy this dictionary to a variable, make changes, and then re-assign the dictionary to the `EditableTexts` attribute to see the changes.


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
