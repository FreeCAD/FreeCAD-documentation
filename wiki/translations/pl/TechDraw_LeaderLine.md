---
- GuiCommand:
   Name:TechDraw LeaderLine
   MenuLocation:TechDraw → Add Lines → Add Leaderline to View
   Workbenches:[TechDraw](TechDraw_Workbench.md)
   Version:0.19
   SeeAlso:[TechDraw Rich Text Annotation](TechDraw_RichTextAnnotation.md), [TechDraw Welding Symbol](TechDraw_WeldSymbol.md), [TechDraw Line Group](TechDraw_LineGroup.md)
---

# TechDraw LeaderLine/pl

## Description

The LeaderLine tool adds a line to a View. Other annotation objects (such as [Rich Text Annotations](TechDraw_RichTextAnnotation.md)) can be connected to the leaderline to form complex annotations.

![](images/TechDraw_LeaderLine_sample.png ) *Leaderline added to View001*

## Usage

1.  Select a view.
2.  Press the **<img src="images/TechDraw_LeaderLine.svg" width=16px> Add Leaderline to View** button. A dialog will open allowing to draw the leaderline and assigning end symbols to the line.
3.  Click on **Pick points** and then click into the page to define the starting point of the line.
4.  Move the mouse and click on another point to create a line. Hold **Ctrl** to snap to multiples of 22.5° angles.
5.  Now you can either
    1.  finish the line drawing by double-clicking or pressing **Save Points**.
    2.  add further points to define more line segments.
6.  To finish the creation, press **OK** to close the dialog.

**Note:** If you did not define any points when creating the leaderline, a short line will be placed at the center of the view.

### Editing

1.  Select the Leaderline in the document tree and double-click on it.
2.  A dialog will open where you can change the appearance.
3.  To edit the points, click on **Edit points** and the line points become visible in the drawing.
4.  Drag the points to a place you like and finish the change by clicking on **Save changes**.

## Properties

-    **X,Y**: The point at which the leaderline is connected to the View.

-    **Leader Parent**: The View to which the leader is attached.

-    **Start Symbol**: The symbol at the start: <img alt="" src=images/Arrownone.svg  style="width:20px;"> None, <img alt="" src=images/Arrowfilled.svg  style="width:20px;"> Filled Arrow, <img alt="" src=images/Arrowopen.svg  style="width:20px;"> Open Arrow, <img alt="" src=images/Arrowtick.svg  style="width:20px;"> Tick, <img alt="" src=images/Arrowdot.svg  style="width:20px;"> Dot, <img alt="" src=images/arrowopendot.svg  style="width:20px;"> Open Circle, <img alt="" src=images/arrowfork.svg  style="width:20px;"> Fork, <img alt="" src=images/arrowpyramid.svg  style="width:20px;"> Filled Triangle

-    **End Symbol**: The symbol at the end.

-    **WayPoints**: Nodes on the leaderline.

-    **Scalable**: Leader scales with Leader Parent.

-    **Auto Horizontal**: Forces last leaderline segment to be horizontal.

-    **Color**: Pen colour for the leaderline.

-    **Line Style**: 0 NoLine, 1 <img alt="" src=images/Continuous-line.svg  style="width:20px;"> Continuous, 2 <img alt="" src=images/Dash-line.svg  style="width:20px;"> Dash, 3 <img alt="" src=images/Dot-line.svg  style="width:20px;"> Dot, 4 <img alt="" src=images/DashDot-line.svg  style="width:20px;"> DashDot, 5 <img alt="" src=images/DashDotDot-line.svg  style="width:20px;"> DashDotDot

-    **Line Width**: Width of leaderline.

## Scripting


**See also:**

[TechDraw API](TechDraw_API.md) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

The LeaderLine tool can be used in [macros](Macros.md) and from the [Python](Python.md) console by using the following functions:


```python
myPage = FreeCAD.ActiveDocument().Page
myBase = FreeCAD.ActiveDocument().View
leaderObj = FreeCAD.ActiveDocument.addObject('TechDraw::DrawLeaderLine','DrawLeaderLine')
FreeCAD.activeDocument().myPage.addView(leaderObj)
FreeCAD.activeDocument().leaderObj.LeaderParent = myBase
#first waypoint is always (0,0,0)  
#rest of waypoints are positions relative to (0,0,0)
leaderObj.WayPoints = [p0,p1,p2]
leaderObj.X = 5
leaderObj.Y = 5
```

## Notes

-   You can edit a Leaderline by double clicking on it in the tree view. Double clicking in the graphics area is not yet supported. The line segment(s) can be edited by pressing **Edit points**. To exit the point editing, press **Save changes** or **Discard changes**.
-   If you did not define any points when creating the leaderline, a short line will be placed at the center of the view. You can later not add further points.
-   By default the [preferences](TechDraw_Preferences.md) option **Leader Line Auto Horizontal** is activated. Therefore the last line segment will be horizontal. So if you only have one segment, you get a horizontal line, no matter where you picked the second point.
-   You can turn off the auto horizontal feature for existing Leaderlines changing the **Auto Horizontal** property.





{{TechDraw Tools navi

}}

---
[documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw LeaderLine/pl
