---
 GuiCommand:
   Name: TechDraw DetailView
   MenuLocation: TechDraw , TechDraw Views , Insert Detail View
   Workbenches: TechDraw_Workbench
   SeeAlso: TechDraw_View, TechDraw_ProjectionGroup
---

# TechDraw DetailView/en

## Description

The **TechDraw DetailView** tool creates a view of a small area of an existing view.

![](images/ViewDetail.png ) 
*Detail view with a circular outline*

## Usage

1.  Select a base view for the detail view.
2.  There are several ways to invoke the tool:
    -   Press the **<img src="images/TechDraw_DetailView.svg" width=16px> [Insert Detail View](TechDraw_DetailView.md)** button.
    -   Select the **TechDraw → TechDraw Views → <img src="images/TechDraw_DetailView.svg" width=16px> Insert Detail View** option from the menu.
3.  A highlight outline is added to the base view, a detail view is added to the page, and a task panel opens.
4.  For clarity it is best to move the detail view so that it no longer overlaps the base view: hold down the left mouse button on its frame or label and drag it to a new position.
5.  To change the position of the highlight outline do one of the following:
    -   Move the outline by dragging:
        1.  Press the **Drag Highlight** button.
        2.  The outline is marked on the page and a temporary *drag* label is added.
        3.  Hold down the left mouse button on the outline itself, or on that label, and drag the outline to a new position.
    -   Move the outline by coordinate input:
        1.  Change the X and Y coordinates in the task panel. The coordinates are relative to the center of the base view.
6.  Optionally change the **Radius** of the detail view.
7.  Optionally change the **Scale Type** and **Scale Factor** of the detail view. See [TechDraw View](TechDraw_View#Properties.md) for more information.
8.  Specify a **Reference** label. This label will be displayed near the highlight outline.
9.  Press the **OK** button.

## Notes

-   To edit a detail view double-click it in the [Tree view](Tree_view.md).
-   The outlines of detail views can be round or square. This is controlled by the **Detail View Outline Shape** [preference](TechDraw_Preferences#Annotation.md).
-   [Forum topic with a good discussion about setting the anchor.](https://www.forum.freecadweb.org/viewtopic.php?f=35&t=34055#p285281)

## Properties Detail View 

See also [TechDraw View](TechDraw_View#Properties.md).

### Data


{{TitleProperty|Detail}}

-    **Base View|Link**: The view on which the detail view is based.

-    **Anchor Point|Vector**: The center of the detail view within the **Base View**.

-    **Radius|Float**: The size of the area in the **Base View** that is displayed in the detail view.

-    **Reference|String**: An identifier for the detail view in the **Base View**.

## Properties Base View 

A detail view inherits all applicable properties of its **Base View**. In the properties of that view you can change the appearance of the detail outline:

### View


{{TitleProperty|Hightlight}}

-    **Highlight Adjust|Float**: See [TechDraw View](TechDraw_View#View.md)

-    **Highlight Line Color|Color**: Idem.

-    **Highlight Line Style|Enumeration**: Idem.





{{TechDraw Tools navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw DetailView/en
