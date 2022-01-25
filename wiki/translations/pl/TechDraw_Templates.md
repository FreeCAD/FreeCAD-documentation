# TechDraw Templates/pl
{{TOCright}}

## Overview

Every TechDraw page is based on a Template object. The Template controls paper size and contains fixed text graphics and text, for example, a page frame or border.

The Template can also contain editable text fields for attributes like *Title*, *Subtitle*, *Author*, *Date*, *Scale*, *Weight*, *Drawing number* and *Sheet*.

Templates are [SVG](SVG.md) files which can be created and modified outside of FreeCAD, with an application such as [Inkscape](https://en.wikipedia.org/wiki/Inkscape).

## Properties

-    **Orientation**: Portrait or Landscape.

-    **Width**: Paper width in mm.

-    **Height**: Paper height in mm.

-    **Page Result**: A copy of the original Template file including all changes to editable texts. This allows users who may not have a copy of the Template file to see the Page as intended. Not typically useful for end users.

-    **Template**: a) A pointer to the copy of the original Template file which is incorporated into this \*.FCSTD file, or b) a filepath to a template accessible on the current machine. Use the file selection ellipsis (\...) to change to a different template.

## Changing Template File 

To change the template of a drawing

1.  click the desired page in the tree
2.  if not already open the tree should open a small sub-tree with several leaves
3.  Select the Template leaf
4.  in the property panel/Data Tab/Template is the path to the template file. To change the file press the ellipsis button (\'\...\'). This will open your default template folder (as set in Preferences/TechDraw).
5.  select another template file.

The new file will be opened directly.

When you want to update a changed template file note that you have to load another file before you can select the same file again. This is because the selection of the same file is ignored.

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

See also [How to make a custom TechDraw template](TechDraw_TemplateHowTo.md).

## Notes

-   TechDraw Templates are not entirely interchangeable with [Drawing Templates](Drawing_templates.md). In general, Drawing templates will work in TechDraw, but there may be problems with editable text.

-   Svg transform clauses **will cause problems** in custom templates. See a Stackoverflow discussion on [removing transform clauses in SVG files](https://stackoverflow.com/questions/13329125/removing-transforms-in-svg-files).

-   The **xml:space=\"preserve\"** clause sometimes causes problems with text size and positioning. It is best to avoid/remove this clause from your custom template\'s SVG code.

-   Templates work best when they contain no extraneous SVG code (called \"garbage SVG\" by some). There is a good article on [removing garbage from SVG here](https://freecad-gost.ru/news/gost-templates-techdraw-09-01-2020/). The article is in Russian.





{{TechDraw Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw Templates/pl
