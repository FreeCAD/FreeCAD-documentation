---
- GuiCommand:/ru
   Name/ru:Вставить Вид сечения
   Name:TechDraw_SectionView
   MenuLocation:TechDraw → Вставить Вид сечения
   Workbenches:[TechDraw](TechDraw_Workbench/ru.md)
   SeeAlso:[Вставить Вид](TechDraw_View/ru.md), [Вставить группу проекций](TechDraw_ProjectionGroup/ru.md)
---

# TechDraw SectionView/ru


</div>

## Описание

The <img alt="" src=images/TechDraw_SectionView.svg  style="width:24px;"> **TechDraw SectionView** tool inserts a cross-section view based on an existing part view.

<img alt="" src=images/TechDraw_section_ANSI.png  style="width:350px;"> <img alt="" src=images/TechDraw_section_ISO.png  style="width:350px;"> 
*Sectioning an already placed view, which shows the internal holes and a hatched cut surface.<br>
The top image shows the ANSI arrow format.<br>
The bottom image shows the ISO arrow format.
*

## Применение

1.  Select a part view in the [3D view](3D_view.md) or [Tree view](Tree_view.md).
2.  There are several ways to invoke the tool:
    -   Press the **<img src="images/TechDraw_SectionView.svg" width=16px> [Insert Section View](TechDraw_SectionView.md)** button.
    -   Select the **TechDraw → <img src="images/TechDraw_SectionView.svg" width=16px> Insert Section View** option from the menu.
3.  A task panel will open which will help calculate the various properties. Reasonable values for the view Direction are calculated, but these can be changed.

![](images/TechDraw_Section_Taskview.png ) 
*Taskview to define the sectional cut of a view*

## Properties Section View 

See also [TechDraw View](TechDraw_View#Properties.md).

### Данные


{{TitleProperty|Cut Operation}}

-    **Fuse Before Cut|Bool**: Fuse the source shapes before performing the section cut.

-    **Trim After Cut|Bool**: Additionally trim the resulting shape after the section cut to remove any unwanted pieces.


{{TitleProperty|Cut Surface Format}}

-    **Cut Surface Display|Enumeration**: Appearance of the cut surface. Options:

    -   
        {{Value|Hide}}
        
        : Hides the cut surface, only the outline will be displayed.

    -   
        {{Value|Color}}
        
        : Colors the cut surface using the setting of **Cut Surface Color** in the [TechDraw preferences](TechDraw_Preferences.md).

    -   
        {{Value|SvgHatch}}
        
        : Hatches the section cut using a [hatch](TechDraw_Hatch.md)

    -   
        {{Value|PatHatch}}
        
        : Hatches the section cut using a [geometric hatch](TechDraw_GeometricHatch.md)

-    **File Hatch Pattern|File**: Full path to SVG hatch pattern file.

-    **File Geom Pattern|File**: Full path to PAT pattern file.

-    **Svg Included|FileIncluded**: Full path to the included SVG hatch pattern file.

-    **Pat Included|FileIncluded**: Full path to the included PAT pattern file.

-    **Name Geom Pattern|String**: Name of the PAT pattern to use.

-    **Hatch Scale|Float**: Hatch pattern size adjustment.


{{TitleProperty|Section}}

-    **Section Symbol|String**: The identifier for this section.

-    **Base View|Link**: The view on which this section is based.

-    **Section Normal|Vector**: A vector describing the direction normal to the cutting plane.

-    **Section Origin|Vector**: A vector describing a point on the cutting plane. Typically the centroid of the original part.

-    **Section Direction|Enumeration**: The direction in the Base View for this section. Options: {{Value|Aligned}}, {{Value|Right}}, {{Value|Left}}, {{Value|Up}} or {{Value|Down}}.

### Вид


{{TitleProperty|Cut Surface}}

-    **Cut Surface Color|Color**: Solid color for surface highlight. Used if **Cut Surface Display** is set to {{Value|Color}}.

-    **Show Cut Surface|Bool|Hidden**: Show/hide the cut surface.


{{TitleProperty|Surface Hatch}}

-    **Geom Hatch Color|Color**: The color of the Geometric hath pattern.

-    **Hatch Color|Color**: The color of the Svg hatch pattern.

-    **Hatch Cut Surface|Bool|Hidden**: Hatch the cut surface.

-    **Weight Pattern|Float**: Line weight of the Geometric hatch pattern.

## Properties Base View 

A Section view inherits all applicable properties of the view specified as **Base View**. In the properties of this view you can change the appearance of the section line:

-    **Section Line Color**: The section line color.

-    **Section Line Style**: The section line style.

The default settings for these parameters are set via the settings **Section Line** and **Section Line Style** in the [TechDraw preferences](TechDraw_Preferences.md).

## Примечания

-   **Section Line Format**: both the traditional section line format (as depicted above), and the \"reference arrow method\" are supported. This option is controlled by the Preference setting \"Section Line Standard\" on the Annotation tab. Option \"ANSI\" uses the traditional format and option \"ISO\" uses the reference arrow format.
-   **Fuse Before Cut**: the section operation sometimes fails to cut the source shapes. If **Fuse Before Cut** is true, the source shapes are merged into a single shape before the section operation is attempted. If you encounter problems with the section operation, try flipping this value.
-   **Trim After Cut**: the section cut operation sometimes leaves behind a portion of the source shape. If **Trim After Cut** is true, an additional cut operation is performed on the result of the first cut which should remove any unwanted pieces.
-   **Cut Surface Display**: the cut surface can be hidden, painted in a solid color, hatched using an Svg pattern (default) or hatched using a PAT pattern. See [Hatching](TechDraw_Hatching.md).

## Программирование


**См. так же:**

[TechDraw API](TechDraw_API/ru.md) и [Основы составления скриптов FreeCAD](FreeCAD_Scripting_Basics/ru.md).

The New Section tool can be used in [macros](Macros.md) and from the [Python](Python.md) console by using the following functions:


```python
doc = FreeCAD.ActiveDocument
box = doc.Box
page = doc.Page

view = doc.addObject("TechDraw::DrawViewPart", "View")
page.addView(view)
view.Source = box
view.Direction = (0.0, 0.0, 1.0)

section = doc.addObject("TechDraw::DrawViewSection", "Section")
page.addView(section)
section.Source = box
section.BaseView = view
section.Direction = (0.0, 1.0, 0.0)
section.SectionNormal = (-1.0, 0.0, 0.0)

doc.recompute()
```


<div class="mw-translate-fuzzy">





</div>


{{TechDraw Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw SectionView/ru
