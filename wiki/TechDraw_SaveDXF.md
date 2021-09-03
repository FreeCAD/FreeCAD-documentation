---
- GuiCommand:
   Name:TechDraw ExportPageDXF
   MenuLocation:TechDraw → Export Page as DXF
   Workbenches:[TechDraw](TechDraw_Workbench.md)
   Version:0.18
   SeeAlso:[TechDraw Export Page as SVG](TechDraw_ExportPageSVG.md), [Draft DXF](Draft_DXF.md)
---

## Description

The ExportPageDXF tool saves a drawing page as a [DXF](DXF.md) file.

## Usage

1.  Select a Page in the tree view, if the document contains multiple pages.
2.  Press the **<img src="images/TechDraw_ExportPageDXF.svg" width=16px> [Export Page as DXF](TechDraw_ExportPageDXF.md)** button.
3.  Select a location and file name.

### Limitations

-   Radial and Diameter dimensions will only export properly if they are \"inside\" the arc.
-   Scaling is not supported. The DXF will be drawn in the actual size of the TechDraw page.
-   Units are not supported. The DXF will be drawn in millimeters (mm). Dimension text will be shown exactly as displayed in TechDraw.
-   TechDraw can\'t export a [Insert Draft Workbench Object](TechDraw_DraftView.md) or an [Insert Arch Workbench Object](TechDraw_ArchView.md) to DXF. These views are [SVG](SVG.md) elements generated internally by the [Draft Workbench](Draft_Workbench.md), so there is no geometrical shape to export. To export a view as DXF, it must have been created with [Insert View](TechDraw_View.md) or [Insert Projection Group](TechDraw_ProjectionGroup.md). For example, select an [Arch SectionPlane](Arch_SectionPlane.md), then use [Draft Shape2DView](Draft_Shape2DView.md) to create a flat projection shape, and then use [Insert View](TechDraw_View.md) on this object. Alternatively, select the objects from the tree view or the 3D viewport, and export to DXF using {{MenuCommand|File → [Export](Std_Export.md)}}.
-   The title block of a page is an [SVG](SVG.md) template as well, so it will not be exported to DXF either.
-   In general, TechDraw can only export to DXF those elements that are supported by the `Import::ImpExpDxfWrite` class of the [Import Module](Import_Module.md).

## Notes

-   This function exports the R12 (AC1009) and R14 (AC1014) versions of [DXF](DXF.md).
    -   R12 is an older, simpler version of the standard, but should be readable by most other software.
    -   R14 is the default version. It includes support for splines and ellipses among other things.
-   These parameters affect the output:
    -   
        {{MenuCommand|Tools → Edit parameters → BaseApp/Preferences/Mod/Import → DxfVersionOut}}
        
        . This is an integer value. Valid entries are 12 or 14. The default is 14.

    -   
        {{MenuCommand|Tools → Edit parameters → BaseApp/Preferences/Mod/Import → DiscretizeEllipses}}
        
        . This is a boolean value. If `True`, splines and ellipses are converted to polylines; if `False`, splines and ellipses are written as splines and ellipses objects. The default is `False`. If the DxfVersionOut parameter is 12, splines and ellipses are always converted to polylines.

    -   
        {{MenuCommand|Tools → Edit parameters → BaseApp/Preferences/Mod/Import → maxsegmentlength}}
        
        . This is a float value. If splines and ellipses are converted to polylines this parameter determines the segment length.

## Scripting


**See also:**

[TechDrawGui API](TechDrawGui_API.md) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

The SaveDXF tool can be used in [macros](Macros.md) and from the [Python](Python.md) console by using the following functions:

 
```python
TechDraw.writeDXFPage(page,filename)
```




 {{TechDraw Tools navi}}  
