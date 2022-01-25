---
- GuiCommand:
   Name:TechDraw ToggleFrame
   MenuLocation:TechDraw → Turn View Frames On/Off
   Workbenches:[TechDraw](TechDraw_Workbench.md)
   SeeAlso:[TechDraw View](TechDraw_View.md), [TechDraw Projection Group](TechDraw_ProjectionGroup.md)
---

# TechDraw ToggleFrame/pl

## Description

The Toggle tool turns the display of View frames, labels and vertices on or off.

<img alt="" src=images/TechDraw_ToggleFrame.png  style="width:400px;"> 
*View of the solid projection with frames turned on and turned off*

## Usage

1.  If you have multiple drawing pages in your document, you will need to select the desired page in the tree.
2.  Press the **<img src="images/TechDraw_ToggleFrame.svg" width=16px> [Turn View Frames On/Off](TechDraw_ToggleFrame.md)** button.
3.  If View frames are currently visible, they will disappear. If View frames are not visible, they will appear.
4.  It is possible for different Views to be in different states of frame display. If this happens, press the **<img src="images/TechDraw_ToggleFrame.svg" width=16px> [Turn View Frames On/Off](TechDraw_ToggleFrame.md)** button once or twice to resynchronize the Views.

## Background

The dotted view frame and the vertex dots are just for reference, they aren\'t actually part of the drawing, so you won\'t see them once you export the page as PDF or SVG.

The suggested workflow is to use **<img src="images/TechDraw_ToggleFrame.svg" width=16px> [Turn View Frames On/Off](TechDraw_ToggleFrame.md)** to deactivate the frame surrounding the view, and also the additional dots. With the dots, use the measurement tools to select the correct edges to measure, then toggle the frame (and dots) off to see the final result. Not satisfied? Toggle the frame (and dots) on again, select other vertices and create new measurements, then toggle the frame off again.

You can adjust the size of the vertex dots in the [TechDraw Preferences/Scale tab](TechDraw_Preferences#Scale.md). Please do not set their size to zero, just small or big enough so it\'s comfortable for you to pick them up.

## Scripting


**See also:**

[TechDraw API](TechDraw_API.md) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

The Toggle tool currently doesn\'t have a programming interface.





{{TechDraw Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw ToggleFrame/pl
