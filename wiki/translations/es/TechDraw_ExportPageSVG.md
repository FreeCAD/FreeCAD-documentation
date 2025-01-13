---
 GuiCommand:
   Name: TechDraw ExportPageSVG
   MenuLocation: TechDraw , Page , Export Page as SVG
   Workbenches: TechDraw_Workbench
   SeeAlso: TechDraw_Templates, Draft_SVG
---

# TechDraw ExportPageSVG/es



## Descripción

The **TechDraw ExportPageSVG** tool saves the current drawing page as an [SVG](SVG.md) file.



## Utilización

1.  If there are multiple drawing pages in the document: optionally activate the desired page by selecting it in the [Tree view](Tree_view.md).
2.  There are several ways to invoke the tool:
    -   Press the **<img src="images/TechDraw_ExportPageSVG.svg" width=16px> [Export Page as SVG](TechDraw_ExportPageSVG.md)** button.
    -   Select the **TechDraw → Page  → <img src="images/TechDraw_ExportPageSVG.svg" width=16px> Export Page as SVG** option from the menu.
    -   If a page is displayed in the [Main view area](Main_view_area.md): right-click the page\'s window and select the **Export SVG** option from the context menu.
3.  If there are multiple drawing pages in the document and you have not yet activated a page, the **Page Chooser** dialog box opens:
    1.  Select the desired page.
    2.  Press the **OK** button.
4.  The **Export page as SVG** dialog box opens.
5.  Select a location and file name.



## Notas

-   [TechDraw Hatch](TechDraw_Hatch.md) patterns are not exported to [SVG](SVG.md) due to a limitation in Qt4\'s SVG support.
-   Text positions and sizes are not correct in the exported file. Using the \"system\" default font in the drawing improves the size problem considerably.



## Guión


**Ver también:**

[DibujoTécnico API](TechDrawGui_API/es.md), y [Fundamentos de scripting de FreeCAD](FreeCAD_Scripting_Basics/es.md).

The SaveSVG tool can be used in [macros](Macros.md) and from the [Python](Python.md) console by using the following functions:


```python
TechDrawGui.exportPageAsSvg(DrawPageObject,FilePath)
```

Note that the FreeCADGui module must be active to use this function.


<div class="mw-translate-fuzzy">





</div>


{{TechDraw_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw ExportPageSVG/es
