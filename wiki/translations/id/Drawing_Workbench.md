# Drawing Workbench/id
**Development of the [[Drawing Workbench]] stopped in FreeCAD 0.16, and the new [[TechDraw Workbench]] aiming to replace it was introduced in v0.17. Both workbenches are still provided in v0.17, but the Drawing Workbench may be removed in future releases.**

<img alt="Drawing workbench icon" src=images/Workbench_Drawing.svg  style="width:128px;">

## Introduction

The Drawing module allows you to put your 3D work on paper. That is, to put views of your models in a 2D window and to insert that window in a drawing, for example a sheet with a border, a title and your logo and finally print that sheet.


{{TOCright}}

<img alt="" src=images/Drawing_extraction.png  style="width:600px;">

## Tools

These are tools for creating, configuring and exporting 2D drawing sheets

-   <img alt="" src=images/Drawing_New.png  style="width:32px;"> [Open scalable vector graphic](Drawing_Open_SVG.md): Opens a drawing sheet previously saved as an SVG file

-   <img alt="" src=images/Drawing_Landscape_A3.png  style="width:32px;"> [New A3 landscape drawing](Drawing_Landscape_A3.md): Creates a new drawing sheet from FreeCAD\'s default A3 template

-   <img alt="" src=images/Drawing_View.png  style="width:32px;"> [Insert a view](Drawing_View.md): Inserts a view of the selected object in the active drawing sheet

-   <img alt="" src=images/Drawing_Annotation.png  style="width:32px;"> [Annotation](Drawing_Annotation.md): Adds an annotation to the current drawing sheet

-   <img alt="" src=images/Drawing_Clip.png  style="width:32px;"> [Clip](Drawing_Clip.md): Adds a clip group to the current drawing sheet

-   <img alt="" src=images/Drawing_Openbrowser.png  style="width:32px;"> [Open Browser](Drawing_Openbrowser.md): Opens a preview of the current sheet in the browser

-   <img alt="" src=images/Drawing_Orthoviews.png  style="width:32px;"> [Ortho Views](Drawing_Orthoviews.md): Automatically creates orthographic views of an object on the current drawing sheet

-   <img alt="" src=images/Drawing_Symbol.png  style="width:32px;"> [Symbol](Drawing_Symbol.md): Adds the contents of a SVG file as a symbol on the current drawing sheet

-   <img alt="" src=images/Drawing_DraftView.png  style="width:32px;"> [Draft View](Draft_Drawing.md): Inserts a special Draft view of the selected object in the current drawing sheet

-   <img alt="" src=images/Drawing_SpreadsheetView.png  style="width:32px;"> [Spreadsheet View](Drawing_SpreadsheetView.md): Inserts a view of a selected spreadsheet in the current drawing sheet

-   <img alt="" src=images/Drawing_Save.png  style="width:32px;"> [Save sheet](Drawing_Save.md): Saves the current sheet as a SVG file

-   [Project Shape](Drawing_ProjectShape.md): Creates a projection of the selected object (Source) in the 3D view.

-    **Note:**the [Draft Drawing](Draft_Drawing.md) tool is used with [Draft objects](Draft_Workbench.md). It has some additional capabilities over the Drawing tools, and supports specific objects like [Draft dimensions](Draft_Dimension.md).

## Workflow

The document contains a 3D shape object (leg) from which we want to produce a drawing. Therefore a \"Page\" is created. A page it\'s instantiated from a template, for example, the \"A3\_Landscape\" template. The template is an [SVG](SVG.md) document which can hold a page frame, a logo, and other elements.

In this page we can insert one or more views. Each view has a position on the page, a scale factor, and additional properties. Every time the page or the view or the referenced object changes, the page is regenerated and the page display updated.

## Scripting

At the moment the graphical user interface workflow is very limited, so the scripting API is more interesting.

See the [Drawing API example](Drawing_API_example.md) page for a description of the functions used to create drawing pages and views.

The macro [CartoucheFC](Macro_CartoucheFC.md) allows you to create a custom information box on an A3 landscape page.

## Templates

FreeCAD comes bundled with a set of default templates, but you can find more on the [Drawing templates](Drawing_templates.md) page.

## Extending the Drawing Module 

Some notes on the programming side of the drawing module will be added to the [Drawing Documentation](Drawing_Documentation.md) page. This is to help quickly understand how the drawing module works, enabling programmers to rapidly start programming for it.

## Tutorials

-   [Drawing tutorial](Drawing_tutorial.md)

## External links 

-   [Intro to mechanical drawing on Youtube - by Normal Universe](https://www.youtube.com/watch?v=1Hm5Zyjmjac)


{{docnav/id|Part Workbench/id|Raytracing Workbench/id}}


{{Drawing Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Obsolete Workbenches](Category_Obsolete Workbenches.md) > [Drawing](Category_Drawing.md) > Drawing Workbench/id
