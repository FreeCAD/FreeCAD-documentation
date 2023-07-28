# TechDraw Templates
## Description

Every TechDraw page is based on a Template object. The Template controls paper size and contains fixed text graphics and text, for example, a page frame or border.

The Template can also contain editable text fields for attributes like *Title*, *Subtitle*, *Author*, *Date*, *Scale*, *Weight*, *Drawing number* and *Sheet*.

Templates are [SVG](SVG.md) files which can be created and modified outside of FreeCAD, with an application such as [Inkscape](https://en.wikipedia.org/wiki/Inkscape).

## Properties

-    **Orientation**: Portrait or Landscape.

-    **Width**: Paper width in mm.

-    **Height**: Paper height in mm.

-    **Page Result**: A copy of the original Template file including all changes to editable texts. This allows users who may not have a copy of the Template file to see the Page as intended. Not typically useful for end users.

-    **Template**: a) A pointer to the copy of the original Template file which is incorporated into this \*.FCStd file, or b) a filepath to a template accessible on the current machine. Use the file selection ellipsis (\...) to change to a different template.

## Select a different template file 

To select a different template for a drawing:

1.  Locate the desired Page object in the [Tree view](Tree_view.md).
2.  Expand the Page node if necessary.
3.  Select the Template object.
4.  In the [Property editor](Property_editor.md) click in the **Template** property field.
5.  Press the **...** (ellipsis) button that appears.
6.  A file dialog opens the folder the current template is located in. If the Page was created in the current FreeCAD session this will be the default template folder (as set in the [TechDraw Preferences](TechDraw_Preferences#Files.md)).
7.  Optionally browse to another folder.
8.  Select a different template file.
9.  Press the **OK** button.

If you have modified a template file and want to update a Page created in the current FreeCAD session that uses this template, temporarily select a different file first, and then select the modified file again.

## Custom Templates 

A limited number of pre-formatted templates in various standard page sizes are included with FreeCAD. These are found in

 
```python
$INSTALL_DIR/Mod/TechDraw/Templates/
```

Where `$INSTALL_DIR` is the directory where FreeCAD was installed, for example

 
```python
/usr/share/freecad/Mod/TechDraw/Templates/
```

Custom templates can also be specified as a default in the [TechDraw Preferences](TechDraw_Preferences.md).

See also [How to make a custom TechDraw template](TechDraw_TemplateHowTo.md), or, if you prefer script generated templates, [TechDraw TemplateGenerator](TechDraw_TemplateGenerator.md) and [Macro TemplateHelper](Macro_TemplateHelper.md).

## Notes

-   TechDraw Templates are not entirely interchangeable with [Drawing Templates](Drawing_templates.md). In general, Drawing templates will work in TechDraw, but there may be problems with editable text.

-   Svg transform clauses **will cause problems** in custom templates. See a Stackoverflow discussion on [removing transform clauses in SVG files](https://stackoverflow.com/questions/13329125/removing-transforms-in-svg-files).

-   The **xml:space=\"preserve\"** clause sometimes causes problems with text size and positioning. It is best to avoid/remove this clause from your custom template\'s SVG code.

-   Templates work best when they contain no extraneous SVG code (called \"garbage SVG\" by some). There is a good article on [removing garbage from SVG here](https://freecad-gost.ru/news/gost-templates-techdraw-09-01-2020/). The article is in Russian.




 {{TechDraw Tools navi}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw Templates
