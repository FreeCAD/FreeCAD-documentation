---
- GuiCommand:
   Name:TechDraw PageDefault
   MenuLocation:TechDraw → Insert Default Page
   Workbenches:[TechDraw](TechDraw_Workbench.md)
   SeeAlso:[TechDraw PageTemplate](TechDraw_PageTemplate.md), [TechDraw Templates](TechDraw_Templates.md)
---

# TechDraw PageDefault/es

## Descripción

The New Default tool creates a new Page object using the the template file specified in the [TechDraw Preferences](TechDraw_Preferences.md).

<img alt="" src=images/A4_LandscapeTD.svg  style="width:400px;"> 
*Default template that comes with TechDraw: A4 page in landscape orientation, with editable text fields*

## Utilización

-   Press the **<img src="images/TechDraw_PageDefault.svg" width=16px> [Insert Default Page](TechDraw_PageDefault.md)** button. (An active document must exist.)

## Notas

-   If a Page is marked as \"do not keep updated\" either through the KeepUpdated Property or by the setting in Preferences, it will ignore changes in the 3D model. You may notice anomalies (missing geometry, missing Dimension values, etc) in the appearance of the Page. These will correct themselves once the Page is updated with the [Redraw Page](TechDraw_RedrawPage.md) tool. The Page will have this icon <img alt="" src=images/TechDraw_Tree_Page_Unsync.svg  style="width:24px;"> in the tree while updating is suspended. This setting also affects the startup process. If the Page is marked \"do not keep updated\" it will not be drawn at program start.

-   If the default template is not specified in your user configuration file `user.cfg`, the tool will try:

:   
    
```python
    $INSTALL_DIR/Mod/TechDraw/Templates/A4_LandscapeTD.svg
    
```
    





:   Where `$INSTALL_DIR` is the directory where FreeCAD was installed, for example:
:   
    
```python
    /usr/share/freecad/Mod/TechDraw/Templates/A4_LandscapeTD.svg
    
```
    

## Propiedades

### Data


{{TitleProperty|Base}}

-    **Projection Type**: Default projection type (First or Third Angle) for this Page.


{{TitleProperty|Page}}

-    **Keep Updated**: If false, the Page is not updated with changes to the 3D model. Useful for complicated/slow drawings. See Notes.

-    **Template**: A link to this Page\'s [Template](TechDraw_Templates.md) object.

-    **Views**: A list of links to the Views on this Page.

-    **Scale**: Default scale for Views in this Page.

-    **Next Balloon Index**: Auto-numbering for Balloons.

### View


{{TitleProperty|Grid}}

-    **Show Grid**: Show a grid over this Page. <small>(v0.20)</small> 

-    **Grid Spacing**: Distance between grid lines in mm. <small>(v0.20)</small> 

## Guión


**See also:**

[TechDraw API](TechDraw_API.md) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

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



---
![](images/Right_arrow.png) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw PageDefault/es
