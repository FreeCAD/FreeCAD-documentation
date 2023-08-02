---
- GuiCommand:
   Name: TechDraw PageDefault
   MenuLocation: TechDraw -> Page -> Insert Default Page
   Workbenches: TechDraw_Workbench
   SeeAlso: TechDraw_PageTemplate, TechDraw_Templates
---

# TechDraw PageDefault/en

## Description

The **TechDraw PageDefault** tool creates a new Page object using the the template file specified in the [TechDraw Preferences](TechDraw_Preferences.md).

<img alt="" src=images/A4_LandscapeTD.svg  style="width:400px;"> 
*Default template that comes with TechDraw: A4_LandscapeTD.svg*

## Usage

1.  An active document must exist.
2.  There are several ways to invoke the tool:
    -   Press the **<img src="images/TechDraw_PageDefault.svg" width=16px> [Insert Default Page](TechDraw_PageDefault.md)** button.
    -   Select the **TechDraw → Page → <img src="images/TechDraw_PageDefault.svg" width=16px> Insert Default Page** option from the menu.

## Notes

-   If a Page is marked as \"do not keep updated\" either through its **Keep Updated** property, through the **Toggle Keep Updated** option from its window context menu, or by the setting in the Preferences, it will ignore changes in the 3D model. You may notice anomalies (missing geometry, missing Dimension values, etc) in the appearance of the Page. These will correct themselves once the Page is updated with the [Redraw Page](TechDraw_RedrawPage.md) tool. The Page will have this icon <img alt="" src=images/TechDraw_Tree_Page_Unsync.svg  style="width:24px;"> in the [Tree view](Tree_view.md) while updating is suspended. This setting also affects the startup process. If a Page is marked as \"do not keep updated\" it will not be drawn at program start.

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
    

## Properties

### Data


{{TitleProperty|Base}}

-    **Projection Type**: Default projection type (First or Third Angle) for this Page.


{{TitleProperty|Page}}

-    **Keep Updated**: If false, the Page is not updated with changes to the 3D model. Useful for complicated/slow drawings. See [Notes](#Notes.md).

-    **Template**: A link to this Page\'s [Template](TechDraw_Templates.md) object.

-    **Views**: A list of links to the Views on this Page.

-    **Scale**: Default scale for Views in this Page.

-    **Next Balloon Index**: Auto-numbering for Balloons.

### View


{{TitleProperty|Grid}}

-    **Show Grid**: Show a grid over this Page. <small>(v0.20)</small> 

-    **Grid Spacing**: Distance between grid lines. <small>(v0.20)</small> 

## Scripting

See [TechDraw PageTemplate](TechDraw_PageTemplate#Scripting.md).





{{TechDraw Tools navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw PageDefault/en
