---
- GuiCommand:
   Name:TechDraw SectionView
   MenuLocation:TechDraw → Insert Section View
   Workbenches:[TechDraw](TechDraw_Workbench.md)
   SeeAlso:[TechDraw View](TechDraw_View.md), [TechDraw Projection Group](TechDraw_ProjectionGroup.md)
---

# TechDraw SectionView/en

## Description

The Section tool creates a cross section view based on an existing part view.

<img alt="" src=images/TechDraw_Section_example.png  style="width:250px;"> 
*Sectioning an already placed view, which shows the internal holes and a shaded cut surface*

## Usage

1.  Select a part view in the 3D window or tree.
2.  If you have multiple drawing pages in your document, you will also need to select the desired page in the tree.
3.  Press the **<img src="images/TechDraw_SectionView.svg" width=16px> [Insert Section View](TechDraw_SectionView.md)** button
4.  A dialog will open which will help calculate the various Section properties. The dialog calculates reasonable starting points for SectionNormal and view Direction, but these may be changed after creation for special needs.
5.  If you make a mistake, or change your mind while setting up the Section parameters, press the **Reset** button, and you can start over.

![](images/TechDraw_Section_Taskview.png ) 
*Taskview to define the sectional cut of a view*

## Properties

### Data

#### Section

-    **Base View**: The view on which this section is based.

-    **Section Normal**: A vector describing the direction normal to the cutting plane.

-    **Section Origin**: A vector describing a point on the cutting plane. Typically the centroid of the original part.

-    **Fuse Before Cut**: Fuse the source shapes before performing the section cut.

#### Cut Surface Format 

-    **Cut Surface Display**: Appearance of cut surface. Options:

    -   *Hide* Hides the cut surface, only the outline will be displayed.
    -   *Color*: Colors the cut surface using the setting of **Cut Surface Color** in the [TechDraw preferences](TechDraw_Preferences.md).
    -   *SvgHatch*: Hatches the section cut using a [hatch](TechDraw_Hatch.md)
    -   *PatHatch*: Hatches the section cut using a [geometric hatch](TechDraw_GeometricHatch.md)

-    **File Hatch Pattern**: Full path to SVG hatch pattern file.

-    **File Geom Pattern**: Full path to PAT pattern file.

-    **Svg Included**: Full path to the included SVG hatch pattern file.

-    **Pat Included**: Full path to the included PAT pattern file.

-    **Name Geom Pattern**: Name of PAT pattern to use (ignored for the *SvgHatch* setting of **Cut Surface Display**).

### View

#### Cut Surface 

-    **Cut Surface Color**: Solid color for surface highlight. Used if **Cut Surface Display** is set to *Color*.

#### Surface Hatch 

-    **Hatch Color**: Color for surface hatch lines.

-    **Weight Pattern**: Line weight for surface hatch lines.

### Base View 

A Section view inherits all applicable properties of the view specified as **BaseView**. In the properties of the view you can change the appearance of the section line:

-    **Section Line Color**: Color for the section line.

-    **Section Line Style**: Style for the section line.

The default settings for these parameters are set via the settings **Section Line** and **Section Line Style** in the [TechDraw preferences](TechDraw_Preferences.md).

## Scripting


**See also:**

[TechDraw API](TechDraw_API.md) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

The New Section tool can be used in [macros](Macros.md) and from the [Python](Python.md) console by using the following functions:


```python
view = FreeCAD.ActiveDocument.addObject('TechDraw::DrawViewPart','View')
rc = page.addView(view)
view.Source = box
view.Direction = (0.0,0.0,1.0)

section = FreeCAD.ActiveDocument.addObject('TechDraw::DrawViewSection','Section')
rc = page.addView(section)
section.Source = box
section.BaseView = view
section.Direction = (0.0,1.0,0.0)
section.SectionNormal = (0.0,0.0,1.0)
section.SectionOrigin = (5.0,5.0,5.0)
```

## Notes

-   **Section Line Format**: both the traditional section line format (as depicted above), and the \"reference arrow method\" are supported. This option is controlled by the Preference setting \"Mod/TechDraw/Format/SectionFormat\" (see [Std\_DlgParameter](Std_DlgParameter.md)). 0 for traditional line, 1 for reference arrow method.
-   **CutSurfaceDisplay**: the cut surface can be hidden, painted in a solid color, hatched using an Svg pattern (default) or hatched using a PAT pattern. See [Hatching](TechDraw_Hatching.md).
-   **FuseBeforeCut**: the section operation sometimes fails to cut the source shapes. If FuseBeforeCut is true, the source shapes are merged into a single shape before the section operation is attempted. If you encounter problems with the section operation, try flipping this value.





{{TechDraw Tools navi

}}

---
[documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw SectionView/en
