---
- GuiCommand:
   Name: TechDraw SectionView
   MenuLocation: TechDraw -> TechDraw Views -> Insert Section View
   Workbenches: TechDraw_Workbench
   SeeAlso: TechDraw_ComplexSection, TechDraw_View, TechDraw_ProjectionGroup
---

# TechDraw SectionView/es



## Descripción

The **TechDraw SectionView** tool inserts a cross-section view based on an existing part view.

<img alt="" src=images/TechDraw_section_ANSI.png  style="width:350px;">
<img alt="" src=images/TechDraw_section_ISO.png  style="width:350px;"> 
*Sectioning an already placed view, which shows the internal holes and a hatched cut surface.<br>
The top image shows the ANSI arrow format.<br>
The bottom image shows the ISO arrow format.
*



## Utilización

1.  Select a part view in the [3D view](3D_view.md) or [Tree view](Tree_view.md).
2.  There are several ways to invoke the tool:
    -   Press the **<img src="images/TechDraw_SectionView.svg" width=16px> [Insert Section View](TechDraw_SectionView.md)** button.
    -   Select the **TechDraw → TechDraw Views → <img src="images/TechDraw_SectionView.svg" width=16px> Insert Section View** option from the menu.
3.  A task panel opens which will help calculate the various properties. Reasonable values for the view Direction are calculated, but these can be changed.

![](images/TechDraw_Section_Taskview.png ) 
*Taskview to define the sectional cut of a view*

## Properties Section View 

See also [TechDraw View](TechDraw_View#Properties.md).



### Datos


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



### Vistas


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



## Notas

-   **Section Line Format**: two section line formats are supported (as depicted above) and controlled by the Preference setting \"Section Line Standard\" on the Annotation tab. The {{Value|ANSI}} option uses \"pulling arrows\" (known as the \"traditional format\" in some areas) and the {{Value|ISO}} option uses \"pushing arrows\" (also known as the \"reference arrow format\").
-   **Fuse Before Cut**: the section operation sometimes fails to cut the source shapes. If **Fuse Before Cut** is true, the source shapes are merged into a single shape before the section operation is attempted. If you encounter problems with the section operation, try flipping this value.
-   **Trim After Cut**: the section cut operation sometimes leaves behind a portion of the source shape. If **Trim After Cut** is true, an additional cut operation is performed on the result of the first cut which should remove any unwanted pieces.
-   **Cut Surface Display**: the cut surface can be hidden, painted in a solid color, hatched using an Svg pattern (default) or hatched using a PAT pattern. See [Hatching](TechDraw_Hatching.md).

## Scripting

See also: [Autogenerated API documentation](https://freecad.github.io/SourceDoc/) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

A SectionView can be created with [macros](Macros.md) and from the [Python](Python.md) console by using the following functions:


```python
doc = FreeCAD.ActiveDocument
box = doc.Box
page = doc.Page

view = doc.addObject("TechDraw::DrawViewPart", "View")
page.addView(view)
view.Source = box
view.Direction = (0, 0, 1)

section = doc.addObject("TechDraw::DrawViewSection", "Section")
page.addView(section)
section.Source = box
section.BaseView = view
section.Direction = (0, 1, 0)
section.SectionNormal = (-1, 0, 0)

doc.recompute()
```

## Examples

For some more information about section views and some use cases, have a look at: [TechDraw section examples](TechDraw_Section_Examples.md).

<img alt="" src=images/TechDraw_ExampleSection-10.png  style="width:80px;"> <img alt="" src=images/TechDraw_ExampleSection-13.png  style="width:80px;"> <img alt="" src=images/TechDraw_ExampleSection-15.png  style="width:80px;"> <img alt="" src=images/TechDraw_ExampleSection-17.png  style="width:80px;"> <img alt="" src=images/TechDraw_ExampleSection-34.png  style="width:80px;"> <img alt="" src=images/TechDraw_ExampleSection-35.png  style="width:80px;">


<div class="mw-translate-fuzzy">





</div>


{{TechDraw Tools navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw SectionView/es
