# Draft tutorial/sv



<div class="mw-translate-fuzzy">


{{TutorialInfo/sv
|Topic= Drafting
|Level= Beginner
|Time= 20 minutes
|Author=[http://freecadweb.org/wiki/index.php?title=User:Drei Drei]
|FCVersion=0.16 or above
|Files=
}}


</div>

## Introduction

This tutorial was originally written by Drei, and it was rewritten and illustrated by vocx.

This tutorial is meant to introduce the reader to the basic workflow of the <img alt="" src=images/Workbench_Draft.svg  style="width:24px;"> [Draft Workbench](Draft_Workbench.md).

The reader will practice:

-   creation of lines, arcs, and polygons
-   the use of working planes
-   the creation of dimensions, text, and shapestrings
-   the creation of a technical drawing

This tutorial uses the notation {{Value|(x, y, z)}} to denote the coordinates required to define points in an object. The default unit is millimeters {{Value|mm}}.

<img alt="" src=images/00_Dr01_Draft_Tutorial_final.png  style="width:" height="400px;"> 
*Final drawing including various Draft objects.*

## Setup

1\. Open FreeCAD, create a new empty document with **File → <img src=images/Std_New.svg style="width:16px"> [New](Std_New.md)**.

:   1.1. Switch to the <img src=images/Workbench_Draft.svg style="width:Draft Workbench](Draft_Workbench.md) from the [workbench selector](Std_Workbench.md), or the menu **View → Workbench → [16px"> Draft**.
:   1.2. Make sure you understand how to use the [property editor](property_editor.md), particularly the **Data** and **View** tabs to change the properties. When changing properties, you may have to do a **<img src="images/Std_Refresh.svg" width=16px> [Std Refresh](Std_Refresh.md)** action to see the result in the [3D view](3D_view.md).
:   1.3. Since the Draft objects are planar shapes, they are better viewed from the top. Use **<img src=images/Std_ViewTop.svg style="width:16px"> [View top](Std_ViewTop.md)** to set the [3D view](3D_view.md).
:   1.4. Although it is not used in this tutorial, the Draft grid is helpful to position geometrical elements. Use **<img src=images/Draft_SelectPlane.svg style="width:16px"> <img src=images/Draft_ToggleGrid.svg style="width:SelectPlane](Draft_SelectPlane.md)** to set both the working plane and the grid, and then show and hide the grid with **[16px"> [Toggle grid](Draft_ToggleGrid.md)**.

## Snap toolbar 

2\. The [Draft Snap toolbar](Draft_Snap.md) is normally activated when you switch to the [Draft Workbench](Draft_Workbench.md).

:   2.1. To make sure it is always there, go to the [Draft Preferences](Draft_Preferences.md), **Edit → Preferences → Draft → Grid and snapping tab**.
:   2.2. Verify that the **Show Draft Snap toolbar** is active.

You can also change the visibility and properties of the Draft grid in this same window.

## Working planes 

Most Draft objects are planar shapes so they are naturally based on a **working plane**. A working plane can be one of the main XY, XZ, and YZ global coordinate planes, or it can be a plane that is parallel to them with a positive or negative offset, or it can be a plane defined by the face of a solid object.

3\. Press **<img src=images/Draft_SelectPlane.svg style="width:16px"> <img src=images/Draft_SelectPlane.svg style="width:SelectPlane](Draft_SelectPlane.md)**, or go to the menu **Utilities → [16px"> [Select plane](Draft_SelectPlane.md)**, to open the working plane [task panel](task_panel.md).

:   3.1. Press **<img src=images/Std_ViewTop.svg style="width:16px"> Top (XY)**.

Before pressing the button, you can also change the value of the offset in millimeters, as well as the grid spacing, the main lines and snapping radius.

## Lines and arcs 

4\. We will create arcs and lines.

:   4.1. Press **<img src=images/Draft_Arc.svg style="width:16px"> [Arc](Draft_Arc.md)**.
:   4.2. Set the **Center** to {{Value|(0, 0, 0)}}, and press **Enter**.
:   4.3. Set the **Radius** to {{Value|30 mm}}, and press **Enter**.
:   4.4. Set the **Start angle** to {{Value|60.0°}}, and press **Enter**.
:   4.5. Set the **Aperture angle** to {{Value|60.0°}}, and press **Enter**.
:   4.6. Repeat the same procedure for a second arc with a radius of {{Value|25 mm}}, the other properties are the same.

5\. We will now create a closed profile by tying the arcs with lines.

:   5.1. Press **<img src=images/Draft_Line.svg style="width:16px"> [Line](Draft_Line.md)**.
:   5.2. In the <img src=images/Draft_Snap_Lock.svg style="width:Snap toolbar](Draft_Snap.md) make sure **[16px"> <img src=images/Draft_Snap_Endpoint.svg style="width:Toggle snap](Draft_Snap_Lock.md)** is active, and only **[16px"> [Endpoint](Draft_Snap_Endpoint.md)** as well. As you move the pointer onto the arc and close to one of its endpoints, the <img alt="" src=images/Draft_Snap_Endpoint.svg  style="width:24px;"> [Endpoint](Draft_Snap_Endpoint.md) icon should appear. Also, the target point is emphasized with a large white dot. Click to select this point.
:   5.3. Move the pointer to the closest endpoint of the other arc to tie the two arcs together.
:   5.4. Repeat the process for the other side of the arc to close the profile.

<img alt="" src=images/01_Dr01_Draft_Arc_profile.png  style="width:" height="400px;"> 
*Closed profile created by two arcs and two lines.*

## Fusing or compounding 

We now have several objects in the [tree view](tree_view.md) that form a closed profile. However, this profile is still composed of disconnected objects; each of them can be edited and moved independently of the others. It is possible to continue working with the elements in this way, but it is also possible to fuse them into a single object.

6a. Note that fusing the objects into a single object will create an object that is no longer parametric, so their properties cannot be modified further.

:   6a.1. Select all four objects in the [tree view](tree_view.md), or by holding **Ctrl** and picking them in the [3D view](3D_view.md).
:   6a.2. With these objects selected, click on **<img src=images/Draft_Upgrade.svg style="width:16px"> [Upgrade](Draft_Upgrade.md)**.
:   6a.3. This will upgrade the four objects into a single {{Value|Wire}}.

6b. If you wish to maintain the parametric nature of the objects you can create a compound instead.

:   6b.1. Switch to the <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Part Workbench](Part_Workbench.md).
:   6b.2. With these objects selected, click on **<img src=images/Part_Compound.svg style="width:16px"> [Part Compound](Part_Compound.md)**.

## Rectangles, circles, and polygons 

7\. We will draw a rectangular frame. (Switch back to the <img alt="" src=images/Workbench_Draft.svg  style="width:24px;"> [ Draft Workbench](Draft_Workbench.md).)

:   7.1. Press **<img src=images/Draft_Rectangle.svg style="width:16px"> [Rectangle](Draft_Rectangle.md)**.
:   7.2. Enter the values of the first point {{Value|(-100, -60, 0)}}, and press **Enter**.
:   7.3. Make sure the **Relative** option is unchecked, as we will use absolute units. You may press **R** in the keyboard to quickly toggle this option on and off.
:   7.4. Enter the values for the second point {{Value|(140, 90, 0)}}, and press **Enter**.

A rectangle is created. Go in the [property editor](Property_editor.md) to change its properties. If you don\'t want the rectangle to create a face, set **Make Face** to `False`. If you want to make a face, but see only the wires of that object, keep **Make Face** to `True` but set the **Display Mode** to {{Value|Wireframe}}.

8\. We will draw a circle.

:   8.1. Press **<img src=images/Draft_Circle.svg style="width:16px"> [Circle](Draft_Circle.md)**.
:   8.2. Enter the values of the center {{Value|(0, 0, 0)}}, and press **Enter**.
:   8.3. Set the radius to {{value|15 mm}}, and press **Enter**.

9\. We will draw a regular polygon.

:   9.1. Press **<img src=images/Draft_Polygon.svg style="width:16px"> [Polygon](Draft_Polygon.md)**.
:   9.2. Enter the values of the center {{Value|(0, 0, 0)}}, and press **Enter**.
:   9.3. Set the number of sides to {{Value|6}}, and press **Enter**.
:   9.4. Set the radius to {{Value|50 mm}}, and press **Enter**.

Again, you may change the **Make Face** and **Display Mode** properties in the [property editor](property_editor.md) if you want.

The rectangle, the circle, the polygon, and most other objects created with the [Draft Workbench](Draft_Workbench.md) share many data and view properties because they are derived from the same base class, [Part Part2DObject](Part_Part2DObject.md).

<img alt="" src=images/02_Dr01_Draft_Rectangle_circle_polygon.png  style="width:" height="400px;"> 
*Rectangle, circle and polygon added.*

## Arrays

Arrays are used to replicate an object several times in an orthogonal direction (X, Y, Z), around a revolution axis, or along a path.

10\. We will create a polar array.

:   10.1. Select the {{Value|Wire}} object that was previously created with the **<img src=images/Draft_Upgrade.svg style="width:16px"> <img src=images/Part_Compound.svg style="width:Upgrade](Draft_Upgrade.md)** tool, or the {{Value|Compound}} created with the **[16px"> [Part Compound](Part_Compound.md)** tool.
:   10.2. Press **<img src=images/Draft_PolarArray.svg style="width:16px"> [PolarArray](Draft_PolarArray.md)**.
:   10.3. Adjust the polar angle to {{Value|360°}}.
:   10.4. Set the number of elements to {{Value|4}}.
:   10.5. Enter the values for the center of rotation {{Value|(0, 0, 0)}}, and press **Enter**.

The array object shows copies of the object around the origin.

<img alt="" src=images/03_Dr01_Draft_PolarArray.png  style="width:" height="400px;"> 
*Polar array of the small profile centered around the origin.*

## Dimensions

Linear dimensions work best when using the appropriate [Draft Snap](Draft_Snap.md) methods to select points and edges to measure. However, they can also be created by specifying absolute coordinates.

11\. Create dimensions for the different objects.

:   11.1. Press **<img src=images/Draft_Dimension.svg style="width:16px"> [Dimension](Draft_Dimension.md)**.
:   11.2. Pick the first point. In this tutorial the first point will always be the origin {{Value|(0, 0, 0)}}.
:   11.3. In the <img src=images/Draft_Snap_Lock.svg style="width:Snap toolbar](Draft_Snap.md) make sure **[16px"> <img src=images/Draft_Snap_Midpoint.svg style="width:Toggle snap](Draft_Snap_Lock.md)** is active, and only **[16px"> [Midpoint](Draft_Snap_Midpoint.md)** as well. As you move the pointer to the top edge of the polygon, the <img alt="" src=images/Draft_Snap_Midpoint.svg  style="width:24px;"> [Midpoint](Draft_Snap_Midpoint.md) icon should appear; click to select this point.
:   11.4. Move the cursor to the right to specify the location of the dimension, then click to set the final position, around {{Value|(100, 20, 0)}}. The dimension will automatically show the length value measured between the two points.
:   11.5. Select the dimension object in the [tree view](tree_view.md), and in the [property editor](Property_editor.md), change **Font Size** to {{Value|6 mm}}, set **Ext Lines** to {{Value|45 mm}}, and **Show Unit** to `False`.

12\. Repeat the process for the two arcs of the closed profile. The first point of the measurement will still be the origin, and the second point will use the <img alt="" src=images/Draft_Snap_Midpoint.svg  style="width:24px;"> [Midpoint](Draft_Snap_Midpoint.md) of the arc.

13\. Repeat the process for the circle located in the center. The first point of the measurement will still be the origin. To select the second point make sure **<img src=images/Draft_Snap_Lock.svg style="width:16px"> <img src=images/Draft_Snap_Angle.svg style="width:Toggle snap](Draft_Snap_Lock.md)** is active, and only **[16px"> [Angle](Draft_Snap_Angle.md)** as well. As you move the pointer to the top of the circle, the <img alt="" src=images/Draft_Snap_Angle.svg  style="width:24px;"> [Angle](Draft_Snap_Angle.md) icon should appear; click to select this point. Then move the cursor to the right, and click to fix the dimension.

Remember to adjust the **Font Size**, and other properties to see the dimension correctly.

<img alt="" src=images/04_Dr01_Draft_Dimension.png  style="width:" height="400px;"> 
*Dimensions that measure the vertical distance from the origin to the top of the circle, arcs, and polygon.*

## Texts and ShapeStrings 

14\. Text objects are simple planar figures that are created in the [3D view](3D_view.md) but don\'t have an actual \"[shape](Shape.md)\" underneath. This means that they cannot be used in complex operations with shapes like extrusions or boolean operations.

:   14.1. Press **<img src=images/Draft_Text.svg style="width:16px"> [Text](Draft_Text.md)**.
:   14.2. Select the reference point in the <img src=images/Draft_Snap_Lock.svg style="width:3D view](3D_view.md). In the [Snap toolbar](Draft_Snap.md) make sure **[16px"> <img src=images/Draft_Snap_Midpoint.svg style="width:Toggle snap](Draft_Snap_Lock.md)** is active, and only **[16px"> [Midpoint](Draft_Snap_Midpoint.md)** as well. Move the pointer to the top edge of the highest arc, so that the <img alt="" src=images/Draft_Snap_Midpoint.svg  style="width:24px;"> [Midpoint](Draft_Snap_Midpoint.md) icon appears; click to select this point.
:   14.3. Enter the desired **Text**, and press **Enter** once to start a new line; add more lines of text as needed.
:   14.4. When you are ready to finish with edition, press **Enter** twice.
:   14.5. Select the text object in the [tree view](tree_view.md), and in the [property editor](Property_editor.md), change **Font Size** to {{Value|6 mm}}, and **Justification** to {{Value|Center}}.

15\. ShapeString objects are shapes made of primitive wires that follow the lines indicated by a certain font. This means that these objects have a real \"[shape](Shape.md)\" underneath, and thus can be used in complex operations like extrusions and boolean operations.

:   15.1. Press **<img src=images/Draft_ShapeString.svg style="width:16px"> [ShapeString](Draft_ShapeString.md)**.
:   15.2. Move the pointer to the desired location in the [3D view](3D_view.md) above the regular polygon, and click once. This will fix the base point for the ShapeString. The coordinates may be entered manually as well, for example, {{Value|(-20, 65, 0)}}.
:   15.3. Enter the desired **String**, and choose the desired **Height**.
:   15.4. If there is no default font file, you must click on the ellipsis **...** to open a dialog window to choose the font location in the system.
:   15.5. When a valid font file has been specified, you may proceed to click **OK** or press **Enter**.

<img alt="" src=images/05_Dr01_Draft_Text_ShapeString.png  style="width:" height="400px;"> 
*Text and ShapeString objects added.*

To extrude letters and engrave them on to solids, see the [Draft ShapeString tutorial](Draft_ShapeString_tutorial.md).

## Creating technical drawings 

As it is now, the objects that we have created can be saved, exported to other formats like [SVG](SVG.md) or [DXF](DXF.md), or printed.

If you wish, you may create a technical drawing to display these objects together with additional information like a frame.

Before doing anything, hide the Draft grid by pressing **<img src=images/Draft_ToggleGrid.svg style="width:16px"> [Toggle  grid](Draft_ToggleGrid.md)**.

16\. Switch to the <img alt="" src=images/Workbench_TechDraw.svg  style="width:24px;"> [TechDraw Workbench](TechDraw_Workbench.md).

:   16.1. Create a standard page by pressing **<img src=images/TechDraw_PageDefault.svg style="width:16px"> [TechDraw PageDefault](TechDraw_PageDefault.md)**.
:   16.2. In the <img src=images/TechDraw_ActiveView.svg style="width:tree view](tree_view.md) select all objects created, except for the Page, and then press **[16px"> [TechDraw ActiveView](TechDraw_ActiveView.md)**. Press **OK** with the default options; it may take a few seconds to create the view in the page.
:   16.3. Selecting the Page object in the [tree view](tree_view.md) will automatically display the Page in the main window. With the Page selected, go to the [property editor](Property_editor.md), and change **Scale** to {{Value|0.75}}.
:   16.4. Expand the Page object in the [tree view](tree_view.md) to select the ActiveView object. With this view selected, go to the [property editor](Property_editor.md), and change **Scale Type** to {{Value|Page}}.
:   16.5. Recompute the model by using **<img src=images/Std_Refresh.svg style="width:16px"> [Refresh](Std_Refresh.md)** or pressing **F5**.
:   16.6. Hide the frames of the objects by pressing **<img src=images/TechDraw_ToggleFrame.svg style="width:16px"> [TechDraw ToggleFrame](TechDraw_ToggleFrame.md)**.

Learn more about the [TechDraw Workbench](TechDraw_Workbench.md) by reading the [Basic TechDraw Tutorial](Basic_TechDraw_Tutorial.md).

<img alt="" src=images/06_Dr01_Draft_TechDraw_page.png  style="width:" height="400px;"> 
*TechDraw page with a projection of the shapes created with the Draft Workbench.*

TechDraw works best with objects that have a [Part TopoShape](Part_TopoShape.md). Since some objects from Draft, like [Draft Texts](Draft_Text.md) and [Draft Dimensions](Draft_Dimension.md), don\'t have such \"[shapes](Shape.md)\", some operations of TechDraw don\'t work with these elements.

Tools like **<img src=images/TechDraw_ActiveView.svg style="width:16px"> <img src=images/TechDraw_DraftView.svg style="width:TechDraw ActiveView](TechDraw_ActiveView.md)**, **[16px"> <img src=images/TechDraw_ArchView.svg style="width:TechDraw DraftView](TechDraw_DraftView.md)**, and **[16px"> [TechDraw ArchView](TechDraw_ArchView.md)** work by receiving an internal SVG image that is generated by internal Draft functions; therefore, TechDraw doesn\'t have much control about how these views are displayed. More integration of Draft and TechDraw is a work in progress.

## Final remarks 

The [Draft Workbench](Draft_Workbench.md) in many ways is similar to the [Sketcher Workbench](Sketcher_Workbench.md), as both are intended to produce 2D shapes. The main difference is in the way each workbench handles coordinate systems, and how the objects are positioned. In Draft, objects are freely positioned in the global coordinates system, usually snapping their points to a grid, or to other objects. In Sketcher, a \"[sketch object](Sketch.md)\" defines a local coordinate system which serves as the reference for all geometrical elements within that sketch. Moreover, the sketch relies on \"constraints\" to define the final position of its points.

-   The [Draft Workbench](Draft_Workbench.md) is intended for 2D drawings which are suitable to be drawn on a grid. The [Arch Workbench](Arch_Workbench.md) mostly builds on top of the tools defined in the [Draft Workbench](Draft_Workbench.md).

-   The [Sketcher Workbench](Sketcher_Workbench.md) is intended for 2D drawings that require precise relationships between its points. It does not rely on a grid, but on rules of positioning (constraints) to determine where the points and edges will be placed. The [Sketcher Workbench](Sketcher_Workbench.md) is mostly used together with the [PartDesign Workbench](PartDesign_Workbench.md) for the creation of solid [bodies](Body.md).

-   It is possible to transform a Draft object into a <img src=images/Draft_Draft2Sketch.svg style="width:Sketch](Sketch.md), and the other way around, using the **[16px"> [Draft Draft2Sketch](Draft_Draft2Sketch.md)** tool.


{{Tutorials navi

}}  
