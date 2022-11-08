---
- GuiCommand   *
   Name   *TechDraw SectionView
   MenuLocation   *TechDraw → Insert Section View
   Workbenches   *[TechDraw](TechDraw_Workbench.md)
   SeeAlso   *[TechDraw ComplexSection](TechDraw_ComplexSection.md), [TechDraw View](TechDraw_View.md), [TechDraw Projection Group](TechDraw_ProjectionGroup.md)
---

# TechDraw SectionView/es

## Descripción

The Section tool creates a cross section view based on an existing part view.

<img alt="" src=images/TechDraw_Section_example.png  style="width   *250px;"> 
*Sectioning an already placed view, which shows the internal holes and a shaded cut surface*

## Utilización

1.  Select a part view in the 3D window or tree.
2.  Press the **<img src="images/TechDraw_SectionView.svg" width=16px> [Insert Section View](TechDraw_SectionView.md)** button
3.  A dialog will open which will help calculate the various Section properties. The dialog calculates reasonable starting points for SectionNormal and view Direction, but these may be changed after creation for special needs.
4.  If you make a mistake, or change your mind while setting up the Section parameters, press the **Reset** button, and you can start over.

![](images/TechDraw_Section_Taskview.png ) 
*Taskview to define the sectional cut of a view*

## Properties Section View 

See also [TechDraw View](TechDraw_View#Properties.md).

### Datos


{{TitleProperty|Cut Surface Format}}

-    **Cut Surface Display|Enumeration**   * Appearance of the cut surface. Options   *

    -   
        {{Value|Hide}}
        
           * Hides the cut surface, only the outline will be displayed.

    -   
        {{Value|Color}}
        
           * Colors the cut surface using the setting of **Cut Surface Color** in the [TechDraw preferences](TechDraw_Preferences.md).

    -   
        {{Value|SvgHatch}}
        
           * Hatches the section cut using a [hatch](TechDraw_Hatch.md)

    -   
        {{Value|PatHatch}}
        
           * Hatches the section cut using a [geometric hatch](TechDraw_GeometricHatch.md)

-    **File Hatch Pattern|File**   * Full path to SVG hatch pattern file.

-    **File Geom Pattern|File**   * Full path to PAT pattern file.

-    **Svg Included|FileIncluded**   * Full path to the included SVG hatch pattern file.

-    **Pat Included|FileIncluded**   * Full path to the included PAT pattern file.

-    **Name Geom Pattern|String**   * Name of the PAT pattern to use.

-    **Hatch Scale|Float**   * Hatch pattern size adjustment.


{{TitleProperty|Section}}

-    **Section Symbol|String**   * The identifier for this section.

-    **Base View|Link**   * The view on which this section is based.

-    **Section Normal|Vector**   * A vector describing the direction normal to the cutting plane.

-    **Section Origin|Vector**   * A vector describing a point on the cutting plane. Typically the centroid of the original part.

-    **Section Direction|Vector**   * The direction in the Base View for this section.

-    **Fuse Before Cut|Bool**   * Fuse the source shapes before performing the section cut.

### Vistas


{{TitleProperty|Cut Surface}}

-    **Cut Surface Color|Color**   * Solid color for surface highlight. Used if **Cut Surface Display** is set to {{Value|Color}}.

-    **Show Cut Surface|Bool|Hidden**   * Show/hide the cut surface.


{{TitleProperty|Surface Hatch}}

-    **Geom Hatch Color|Color**   * The color of the Geometric hath pattern.

-    **Hatch Color|Color**   * The color of the Svg hatch pattern.

-    **Hatch Cut Surface|Bool|Hidden**   * Hatch the cut surface.

-    **Weight Pattern|Float**   * Line weight of the Geometric hatch pattern.

## Properties Base View 

A Section view inherits all applicable properties of the view specified as **Base View**. In the properties of this view you can change the appearance of the section line   *

-    **Section Line Color**   * The section line color.

-    **Section Line Style**   * The section line style.

The default settings for these parameters are set via the settings **Section Line** and **Section Line Style** in the [TechDraw preferences](TechDraw_Preferences.md).

## Notas

-   **Section Line Format**   * both the traditional section line format (as depicted above), and the \"reference arrow method\" are supported. This option is controlled by the Preference setting \"Mod/TechDraw/Format/SectionFormat\" (see [Std_DlgParameter](Std_DlgParameter.md)). 0 for traditional line, 1 for reference arrow method.
-   **CutSurfaceDisplay**   * the cut surface can be hidden, painted in a solid color, hatched using an Svg pattern (default) or hatched using a PAT pattern. See [Hatching](TechDraw_Hatching.md).
-   **FuseBeforeCut**   * the section operation sometimes fails to cut the source shapes. If FuseBeforeCut is true, the source shapes are merged into a single shape before the section operation is attempted. If you encounter problems with the section operation, try flipping this value.

## Scripting


**See also   ***

[TechDraw API](TechDraw_API.md) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

The New Section tool can be used in [macros](Macros.md) and from the [Python](Python.md) console by using the following functions   *


```python
view = FreeCAD.ActiveDocument.addObject('TechDraw   *   *DrawViewPart','View')
rc = page.addView(view)
view.Source = box
view.Direction = (0.0,0.0,1.0)

section = FreeCAD.ActiveDocument.addObject('TechDraw   *   *DrawViewSection','Section')
rc = page.addView(section)
section.Source = box
section.BaseView = view
section.Direction = (0.0,1.0,0.0)
section.SectionNormal = (0.0,0.0,1.0)
section.SectionOrigin = (5.0,5.0,5.0)
```


<div class="mw-translate-fuzzy">





</div>


{{TechDraw Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw SectionView/es
