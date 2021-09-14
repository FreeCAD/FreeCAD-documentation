---
- GuiCommand:
   Name:TechDraw DetailView
   MenuLocation:TechDraw → Insert Detail View
   Workbenches:[TechDraw](TechDraw_Workbench.md)
   SeeAlso:[TechDraw View](TechDraw_View.md), [TechDraw Projection Group](TechDraw_ProjectionGroup.md)
---

## Description

The Detail tool creates a view of small area of an existing view.

![](images/ViewDetail.png ) *Detail view with circular viewbox of an existing view*

## Usage

-   Select a view in the page or tree.
-   Press the **<img src="images/TechDraw_DetailView.svg" width=16px> [Insert Detail View](TechDraw_DetailView.md)** button to create the detail view.
-   In the appearing task dialog you can define the radius of the view box, the scale and the view position. For the latter you can do this
    -   either by changing the coordinates
    -   or by pressing the button **Drag Highlight**. In this case the detail origin border is highlighted bold and with the label *drag*. Click on the border or the label, keep the mouse button pressed and drag it to the position you like. Finally release the mouse to accept the change.

The Detail view can be displayed within a round or square view box. This is controlled by the [preferences](TechDraw_Preferences#Annotation.md) setting **Detail View Outline Shape**.

## Properties

### Detail View 

-    **BaseView**: The view on which this Detail view is based.

-    **Anchor Point**: The center of the Detail view within the **BaseView**.

-    **Radius**: The size of the area in the **BaseView** that is displayed in the Detail view.

-    **Scale Type**: Type of the scale. The choices are:

    -   *Page*: The scale factor of the drawing [Page](TechDraw_PageDefault.md) is used
    -   *Automatic*: In case the detail view would be larger than the page, it will be scaled down to fit into the page
    -   *Custom*: A custom scale factor set by **Scale**

-    **Scale**: Magnification level.

-    **Reference**: An identifier to indicate the area of the **BaseView** that is displayed.

### Base View 

A Detail view inherits all applicable properties of the view specified as **BaseView**. In the properties of this view you can change the appearance of the detail outline:

-    **Highlight Adjust**: Clockwise rotation angle of the Detail view.

-    **Highlight Line Color**: Line color for the outline shape. Default setting for this is the setting **Detail Highlight** in the [TechDraw preferences](TechDraw_Preferences.md).

-    **Highlight Line Style**: Line style for the outline shape. Default setting for this is the setting **Detail Highlight Style** in the [TechDraw preferences](TechDraw_Preferences.md).

## Scripting


**See also:**

[TechDraw API](TechDraw_API.md) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

The Detail tool can be used in [macros](Macros.md) and from the [Python](Python.md) console by using the following functions:


```python
Detail = FreeCAD.ActiveDocument.addObject('TechDraw::DrawViewDetail','Detail')
...TBA
```

## Tricks

-   The space around the view outline and the view object border is by default a white area. This means it covers everything behind it. Sometimes there is not enough space on the page and you can save space by reducing this unnecessary white area.

This is done by putting the Detail view into a [clip group](TechDraw_ClipGroup.md):

![](images/TechDraw_DetailClipped.png ) *Detail view in a clip group*

-   For detail views with a round outline, the position of the reference label in the base view can be changed via the base view property **Highlight Adjust**.

## Notes

-   [A good discussion about setting the Anchor](https://www.forum.freecadweb.org/viewtopic.php?f=35&t=34055#p285281)





{{TechDraw Tools navi

}} 
