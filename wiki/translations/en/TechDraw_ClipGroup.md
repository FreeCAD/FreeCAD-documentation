---
- GuiCommand:
   Name:TechDraw ClipGroup
   MenuLocation:TechDraw - Clipped Views - Insert Clip Group
   Workbenches:[TechDraw](TechDraw_Workbench.md)
   SeeAlso:[TechDraw Add Clip Group](TechDraw_ClipGroupAdd.md), [TechDraw Remove Clip Group](TechDraw_ClipGroupRemove.md)
---

# TechDraw ClipGroup/en

## Description

The **TechDraw ClipGroup** tool creates a clipping window which can contain Views.

![](images/TechDraw_Clipview.png ) 
*Viewport window clipping different existing views*

## Usage

1.  If there are multiple drawing pages in the document: optionally activate the desired page by selecting it in the [Tree view](Tree_view.md).
2.  There are several ways to invoke the tool:
    -   Press the **<img src="images/TechDraw_ClipGroup.svg" width=16px> [Insert Clip Group](TechDraw_ClipGroup.md)** button.
    -   Select the **TechDraw → Clipped Views → <img src="images/TechDraw_ClipGroup.svg" width=16px> Insert Clip Group** option from the menu.
3.  If there are multiple drawing pages in the document and you have not yet activated a page, the **Page Chooser** dialog box opens: <small>(v0.20)</small> 
    1.  Select the desired page.
    2.  Press the **OK** button.

## Properties

-    **Width**: The width of the clipping window in units

-    **Height**: The height of the clipping window in units

-    **ShowFrame**: When true, show a frame around the clipping window

-    **ShowLabels**: When true, show the Labels of the Views within the clipping window. **NOTE:** removed in v0.19.

-    **Views**: The Views contained in the clipping window





{{TechDraw Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw ClipGroup/en
