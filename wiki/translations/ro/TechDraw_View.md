---
 GuiCommand:
   Name/ro: Noua vedere TechDraw
   MenuLocation: TechDraw , Insert View
   Workbenches: TechDraw Workbench
   SeeAlso: TechDraw_ProjectionGroup, TechDraw_SectionView
---

# TechDraw View/ro


</div>



## Descriere

Instrumentul Vizualizare adaugă o reprezentare a unuia sau mai multor obiecte pe o pagină de desen. Acesta este blocul de bază al modulului TechDraw. La plupart des autres vues proviennent de NewView.

![](images/TechDraw_View_example.png )

The **TechDraw View** tool adds a representation of one or more objects to a Drawing page. <small>(v1.0)</small> : It can create a [Projection Group Item (a single view)](#Properties_Projection_Group_Item.md), a [Projection Group](TechDraw_ProjectionGroup.md), a [Spreadsheet View](TechDraw_SpreadsheetView.md), an [Arch View](TechDraw_ArchView.md), a [Symbol](TechDraw_Symbol.md) or an [Image View](TechDraw_Image.md).

In {{VersionMinus|0.21}} the tool can only create a [Part View](#Properties_Part_View.md), which is very similar to a Projection Group Item.

![](images/TechDraw_View_example.png ) 
*View of a solid box with hidden lines*

## Usage Projection Group Item and Projection Group 

1.  Optionally rotate the [3D view](3D_view.md). The camera direction in the 3D view can be used to set the projection direction of the primary view.
2.  Select one or more objects with a **Shape** property in the 3D view or [Tree view](Tree_view.md). You can also select [Std Parts](Std_Part.md) or [Std Groups](Std_Group.md) that contain such objects. When selecting in the 3D view the first selected face can be used to set the projection direction of the primary view. Do not select objects by picking a face in the 3D view if you want to use the current camera direction.
3.  If there are multiple drawing pages in the document: optionally add the desired page to the selection by selecting it in the [Tree view](Tree_view.md).
4.  There are several ways to invoke the tool:
    -   Press the **<img src="images/TechDraw_View.svg" width=16px> [Insert View](TechDraw_View.md)** button.
    -   Select the **TechDraw → TechDraw Views → <img src="images/TechDraw_View.svg" width=16px> Insert View** option from the menu.
5.  If there are multiple drawing pages in the document, and if no page is displayed in the [Main view area](Main_view_area.md) and you have not yet selected a page, the **Page Chooser** dialog box opens:
    1.  Select the desired page.
    2.  Press the **OK** button.
6.  The **Part View** task panel opens. <small>(v1.0)</small> 
7.  Optionally adjust the parameters:
    -   **Scale**: select {{Value|Page}}, {{Value|Automatic}} or {{Value|Custom}}. If the last option is selected: enter the scale numerator and denominator.
    -   **Direction**: use the available buttons to adjust the projection direction and rotation of the primary view:
        -   The **[#.## #.## #.##]** button in the center shows the current projection direction. The initial value depends on the **Use 3d Camera Direction** [preference](TechDraw_Preferences#General.md). Press the button to adjust the view direction and rotation manually.
        -   Press the **<img src="images/Arrow-up.svg" width=16px>**, **<img src="images/Arrow-down.svg" width=16px>**, **<img src="images/Arrow-left.svg" width=16px>** or **<img src="images/Arrow-right.svg" width=16px>** button to rotate the projection direction 90° around the horizontal or vertical axis of the view.
        -   Press the **<img src="images/Arrow-cw.svg" width=16px>** or **<img src="images/Arrow-ccw.svg" width=16px>** button to rotate the view 90° around the projection direction.
        -   Press the **<img src="images/TechDraw_ProjFront.svg" width=16px>** button to set projection direction of the primary view to the standard [front view](Std_ViewFront.md).
        -   Press the **<img src="images/TechDraw_CameraOrientation.svg" width=16px>** button to set it to the first selected face, if available, or else to the current camera direction.
    -   **Secondary Projections**: optionally create secondary projections in addition to the primary view. At least one secondary projection has to be specified for all controls in this section to be displayed.
8.  After changing some parameters pressing the **Apply** button can be required to update the view(s).
9.  Press the **OK** button.
10. A [Projection Group Item](#Properties_Projection_Group_Item.md) or, if there are one or more secondary projections, a [Projection Group](TechDraw_ProjectionGroup.md) is inserted.

![](images/TechDraw_View_Taskpanel.png ) 
*Part View [task panel](Task_panel.md)*

## Usage other view types 


<small>(v1.0)</small> 

1.  Optionally select a [spreadsheet](Spreadsheet_CreateSheet.md) in the [Tree view](Tree_view.md) or an [Arch section plane](Arch_SectionPlane.md) in the [3D view](3D_view.md) or Tree view.
2.  Follow steps 3, 4 and 5 as explained [above](#Usage_Projection_Group_Item_and_Projection_Group.md).
3.  If you have not selected a spreadsheet or an Arch section plane:
    1.  A warning dialog box opens.
    2.  Check the **Do not show this message again** checkbox to avoid this dialog box in the future.
    3.  Press the **OK** button.
    4.  A file browser opens.
    5.  Select an SVG or image file.
4.  A [Spreadsheet View](TechDraw_SpreadsheetView.md), an [Arch View](TechDraw_ArchView.md), a [Symbol](TechDraw_Symbol.md) or an [Image View](TechDraw_Image.md) is inserted.
5.  In case of a Spreadsheet View: adjust the cell range of the view by changing its **Cell Start** and **Cell End** properties.
6.  In case of a Symbol or Image View: optionally change its **Scale** property to adjust its size.

## Properties Part View 

See also: [Property editor](Property_editor.md).

A Part View, formally a {{Incode|TechDraw::DrawViewPart}} object, has the following properties:

### Data


{{TitleProperty|Base}}

-    **X|Distance**: The view\'s horizontal position on the page. (1)

-    **Y|Distance**: The view\'s vertical position on the page. (1)

-    **Lock Position|Bool**: Prevents Views from being dragged in the Gui when `True`. The View can still be moved by changing X,Y properties. (1)

-    **Rotation|Angle**: Counterclockwise rotation of the View on the page in degrees. (1)

-    **Scale Type|Enumeration**: The scale type. Options: (1)

    -   
        {{Value|Page}}
        
        : Use the [Page](TechDraw_PageDefault.md)\'s scale setting.

    -   
        {{Value|Automatic}}
        
        : Fit the view to the page.

    -   
        {{Value|Custom}}
        
        : Use the scale defined by **Scale**.

-    **Scale|FloatConstant**: The view will be rendered on the page in Scale:1 ratio to the Source. (1)

-    **Caption|String**: Optional short text caption. (1)


{{TitleProperty|Cosmetics}}

-    **Cosmetic Vertexes|TechDraw::PropertyCosmeticVertexList|Hidden**
    

-    **Cosmetic Edges|TechDraw::PropertyCosmeticEdgeList|Hidden**
    

-    **Center Lines|TechDraw::PropertyCenterLineList|Hidden**
    

-    **Geom Formats|TechDraw::PropertyGeomFormatList|Hidden**
    


{{TitleProperty|HLR Parameters}}

-    **Coarse View|Bool**: If `True`, TechDraw will use a polygon approximation to calculate drawing geometry. If `False`, TechDraw will use a precision algorithm. CoarseView can be much faster for complex models. The quality of the drawing is reduced, since every curve is approximated as a series of short line segments. Vertices are not displayed in CoarseView since each short segment would result in two new Vertices and the display becomes cluttered. Linear Dimensions can be added to a CoarseView, but are unlikely to be useful.

-    **Smooth Visible|Bool**: Visible Smooth lines on/off.

-    **Seam Visible|Bool**: Visible Seam lines on/off.

-    **Iso Visible|Bool**: Visible Isometric(u,v) lines on/off.

-    **Hard Hidden|Bool**: Hidden lines on/off.

-    **Smooth Hidden|Bool**: Hidden Smooth lines on/off.

-    **Seam Hidden|Bool**: Hidden Seam lines on/off.

-    **Iso Hidden|Bool**: Hidden Isometric(u,v) lines on/off.

-    **Iso Count|Integer**: Number of Isometric(u,v) lines to draw on each face.

-    **Scrub Count|Integer**: The number of times FreeCAD should try to clean the HLR result. <small>(v0.21)</small> 


{{TitleProperty|Projection}}

-    **Source|LinkList**: Links to the drawable objects to be depicted.

-    **XSource|XLinkList**: Links to the drawable objects in an external file.

-    **Direction|Vector**: This vector controls the direction from which you are viewing the object. +X is right, -X is left, +Y is rear, -Y is front (looking into the screen), +Z is up and -Z is down. So a Front view is (0,-1,0) and an isometric view is (1,-1,1).

-    **XDirection|Vector**: This vector controls the rotation of the view around the Direction.

-    **Perspective|Bool**: `True` for perspective projection, `False` for orthogonal projection.

-    **Focus|Distance**: Distance from camera to projection plane for perspective projections. Needs to be adjusted to fit the object. Too far and the perspective is lost, too close and the object is distorted.

### View


{{TitleProperty|Base}}

-    **Keep Label|Bool**: Always show view label if `True`. (1)

-    **Stack Order|Integer**: Over or under lap relative to other views. (1) <small>(v0.21)</small> 


{{TitleProperty|Broken View}}

-    **Break Line Style|Enumeration**: Set break line style if applicable. <small>(v1.0)</small> 

-    **Break Line Type|Enumeration**: Adjusts the type of break line depiction on broken views if applicable: {{Value|None}}, {{Value|ZigZag}} or {{Value|Simple}}. <small>(v1.0)</small> 


{{TitleProperty|Decoration}}

-    **Arc Center Marks|Bool**: Circular arc center marks on/off.

-    **Center Scale|Float**: Circular arc center mark size adjustment, if enabled.

-    **Horiz Center Line|Bool**: Show a horizontal centerline through the view.

-    **Show All Edges|Bool**: Temporarily show invisible lines.

-    **Vert Center Line|Bool**: Show a vertical centerline through the view.


{{TitleProperty|Faces}}

-    **Face Color|Color**: Set color of faces. <small>(v1.0)</small> 

-    **Face Transparency|Percent**: Set transparency of faces. <small>(v1.0)</small> 


{{TitleProperty|Highlight}}

-    **Highlight Adjust|Float**: Adjust the rotation of the Detail highlight if applicable.

-    **Highlight Line Color|Color**: Set the highlight line color if applicable.

-    **Highlight Line Style|Enumeration**: Set the highlight line style if applicable.


{{TitleProperty|Lines}}

-    **Extra Width|Length**: Not implemented yet.

-    **Hidden Width|Length**: The thickness of hidden lines, if enabled.

-    **Iso Width|Length**: The thickness of isometric(u,v) surface lines and Dimension lines.

-    **Line Width|Length**: The thickness of visible lines. See [Line Groups](TechDraw_LineGroup.md).


{{TitleProperty|Section Line}}

-    **Include Cut Line|Bool**: Show/hide section cut line if applicable. <small>(v1.0)</small> 

-    **Section Line Color|Color**: Set the section line color if applicable.

-    **Section Line Marks|Bool**: Show/hide marks at direction changes for Complex Section if applicable. <small>(v0.21)</small> 

-    **Section Line Style|Enumeration**: Set the section line style if applicable.

-    **Show Section Line|Bool**: Show/hide the section line if applicable.

\(1\) Aceste proprietăți sunt comune tuturor tipurilor de vizualizare.

## Properties Projection Group Item 

See also: [Property editor](Property_editor.md).

A Projection Group Item, formally a {{Incode|TechDraw::DrawProjGroupItem}} object, is derived from a [Part View](#Properties_Part_View.md), formally a {{Incode|TechDraw::DrawViewPart}} object, and inherits all its properties. It also has the following additional properties:

### Data 


{{TitleProperty|Base}}

-    **Type|Enumeration**: The view type ({{Value|Front}}, {{Value|Left}}, etc.).

-    **Rotation Vector|Vector**: Deprecated use **XDirection** instead.

## Properties Projection Group 

See [TechDraw ProjectionGroup](TechDraw_ProjectionGroup#Properties.md).

## Properties Spreadsheet View 

See [TechDraw SpreadsheetView](TechDraw_SpreadsheetView#Properties.md).

## Properties Arch View 

See [TechDraw ArchView](TechDraw_ArchView#Properties.md).

## Properties Symbol 

See [TechDraw Symbol](TechDraw_Symbol#Properties.md).

## Properties Image View 

See [TechDraw Image](TechDraw_Image#Properties.md).



## Script

Vederile pot fi adăugate la Pages utilizând Python.

See also: [Autogenerated API documentation](https://freecad.github.io/SourceDoc/) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

A Part View can be created with [macros](Macros.md) and from the [Python](Python.md) console by using the following functions:


```python
import FreeCAD as App

doc = App.ActiveDocument
box = doc.addObject("Part::Box", "Box")

page = doc.addObject("TechDraw::DrawPage", "Page")
template = doc.addObject("TechDraw::DrawSVGTemplate", "Template")
template.Template = App.getResourceDir() + "Mod/TechDraw/Templates/A4_LandscapeTD.svg"
page.Template = template

# Toggle the visibility of the page to ensure its width and height are updated (hack):
page.Visibility = False
page.Visibility = True

view = doc.addObject("TechDraw::DrawViewPart", "View")
page.addView(view)
view.Source = [box]
view.Direction = (0, 0, 1)

view.X = page.PageWidth / 2
view.Y = page.PageHeight / 2

doc.recompute()
```


<div class="mw-translate-fuzzy">





</div>


{{TechDraw_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw View/ro
