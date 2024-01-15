---
 TutorialInfo:r
   Topic:  ShapeString 
   Level:  Beginner
   Time: 30 minutes
   Author: r-frank
   FCVersion: 0.16.6704
   Files: https://github.com/FreeCAD/Examples/blob/master/Draft_Shapestring_Tutorial_Examples/Draft_Shapestring_Tutorial_Text.FCStd?raw=true Draft_Shapestring_Text
---

# Draft ShapeString tutorial/tr




<div class="mw-translate-fuzzy">




</div>




<div class="mw-translate-fuzzy">

## Giriş


</div>

This tutorial was originally written by Roland Frank (†2017, r-frank), and it was rewritten and re-illustrated by vocx.

This tutorial describes a method to create 3D text and use it with solid objects in the <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Part Workbench](Part_Workbench.md). We will discuss how to

-   insert outlined text with the **<img src="images/Draft_ShapeString.svg" width=16px> [Draft ShapeString](Draft_ShapeString.md)** tool,
-   extrude it to be a 3D solid with **[<img src=images/Part_Extrude.svg style="width:16px"> [Part Extrude](Part_Extrude.md)**,
-   position it in 3D space using [placement](Placement.md), and **[<img src=images/Draft_Move.svg style="width:16px"> [Draft Move](Draft_Move.md)** (it uses a sketch as auxiliary geometry), and
-   engrave the text by applying a boolean **[<img src=images/Part_Cut.svg style="width:16px"> [Part Cut](Part_Cut.md)**.

To use ShapeStrings inside the <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [PartDesign Workbench](PartDesign_Workbench.md), the process is essentially the same as with the Part Workbench, but the ShapeString is placed inside the [PartDesign Body](PartDesign_Body.md) to extrude it. Go to the end of this tutorial for more information.

![](images/08_T04_Part_ShapesString_Extrude_final_cut.png ) 
*Final model of the engraved text.*

The [Sketcher Workbench](Sketcher_Workbench.md) is used briefly to draw an auxiliary line. More information about the tools of this workbench can be found in

-   [Basic Sketcher tutorial](Basic_Sketcher_Tutorial.md)
-   [Sketcher reference](Sketcher_reference.md)

## Setup

1\. Open FreeCAD, create a new empty document with **File → [<img src=images/Std_New.svg style="width:16px"> [New](Std_New.md)**, and switch to the [Part Workbench](Part_Workbench.md).

:   1.1. Press the **[<img src=images/Std_ViewIsometric.svg style="width:16px"> [View isometric](Std_ViewIsometric.md)** button, or press **0** in the numerical pad of your keyboard, to change the view to isometric to visualize the 3D solids better.
:   1.2. Press the **[<img src=images/Std_ViewFitAll.svg style="width:16px"> [View fit all](Std_ViewFitAll.md)** button whenever you add objects in order to pan and zoom the [3D view](3D_view.md) so that all elements are seen in the view.
:   1.3. Hold **Ctrl** while you click to select multiple items. If you selected something wrong or want to de-select everything, just click on empty space in the [3D view](3D_view.md).

## Create the basic shape 

2\. Insert a primitive cube by clicking on **<img src="images/Part_Box.svg" width=16px> [Box](Part_Box.md)**.

:   2.1. Select `Cube` in the [tree view](Tree_view.md).
:   2.2. Change the dimensions in the **Data** tab of the [property editor](Property_editor.md).
:   2.3. Change **Width** to `31 mm`.

3\. Create a chamfer.

:   3.1. Select the upper edge (`Edge6`) on the front face of the `Cube` in the [3D view](3D_view.md).
:   3.2. Press **<img src="images/Part_Chamfer.svg" width=16px> [Chamfer](Part_Chamfer.md)**.
:   3.3. In the **Chamfer edges** [task panel](Task_panel.md) go to **Selection**, choose **Select edges**. As **Chamfer type** choose `Equal distance`, then set **Length** to `5 mm`.
:   3.4. Press **OK**. This will create a `Chamfer` object.
:   3.5. In the [tree view](Tree_view.md), select `Chamfer`, in the **View** tab change the value of **Line Width** to `2.0`.

![](images/01_T04_Part_Cube_base_long.png ) 
*Base object created from a cube and a chamfer operation.*

## Insert the ShapeString 

4\. Switch to the [Draft Workbench](Draft_Workbench.md).

:   4.1. Make sure nothing is selected in the [tree view](Tree_view.md).
:   4.2. Establish the working plane to XY (Top) by clicking on **[<img src=images/Draft_SelectPlane.svg style="width:16px"> [SelectPlane](Draft_SelectPlane.md)** and pressing **[<img src=images/View-top.svg style="width:16px"> [Top (XY)](Std_ViewTop.md)**.

5\. Insert the text \"FreeCAD\".

:   5.1. Click on **[<img src=images/Draft_ShapeString.svg style="width:16px"> [ShapeString](Draft_ShapeString.md)**.
:   5.2. Change **X** to `0 mm`.
:   5.3. Change **Y** to `0 mm`.
:   5.4. Change **Z** to `0 mm`.
:   5.5. Or press **Reset point**.
:   5.6. Change **String** to `FreeCAD`; change **Height** to `5 mm`; change **Tracking** to `0 mm`.
:   5.7. Make sure **Font file** points to a valid font, for example, `/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf`. Press the ellipsis **...** to open the operating system\'s dialog to find a font.

    :   
        **Note:**
        
        for more details about working with fonts please refer to the [Draft ShapeString Notes](Draft_ShapeString#Notes.md) section.
:   5.8. Press **OK**. This will create a `ShapeString` object.
:   5.9. Recompute the document by pressing **[<img src=images/Std_Refresh.svg style="width:16px"> [Refresh](Std_Refresh.md)**.
:   5.10. In the [tree view](Tree_view.md), select `ShapeString`, in the **View** tab change the value of **Line Width** to `2.0`.
:   5.11. In the [tree view](Tree_view.md), select `Chamfer`, in the **View** tab change the value of **Visibility** to `false`, or press **Space** in the keyboard. This will hide the object, so you can see the `ShapeString` better.
:   5.12. To see the ShapeString from above change the view by pressing **[<img src=images/View-top.svg style="width:16px"> [Top (XY)](Std_ViewTop.md)**, or **2** in the keyboard.
:   5.13. To restore the view to isometric, press **[<img src=images/Std_ViewIsometric.svg style="width:16px"> [View isometric](Std_ViewIsometric.md)**, or **0** in the keyboard.

![](images/02_T04_Part_ShapeString.png ) 
*Text created as a ShapeString, that is, as a collection of edges in a plane.*

## Create the solid 3D text 

6\. Switch back to the [Part Workbench](Part_Workbench.md).

:   6.1. In the [tree view](Tree_view.md), select `ShapeString`, then press **[<img src=images/Part_Extrude.svg style="width:16px"> [Extrude](Part_Extrude.md)**.
:   6.2. In the **Extrude** [task panel](Task_panel.md) go to **Direction**, choose **Along normal**; in **Length**, set **Along** to `1 mm`; also tick the **Create solid** option.
:   6.3. Press **OK**. This will create an `Extrude` object.
:   6.4. In the [tree view](Tree_view.md), select `Extrude`, in the **View** tab change the value of **Line Width** to `2.0`.

![](images/03_T04_Part_ShapeString_Extrude.png ) 
*Text created as a ShapeString, and turned into a solid by extrusion.*

## Insert auxiliary sketch for positioning 

Now we will draw a simple sketch that will be used as auxiliary geometry to position the ShapeString extrusion.

7\. In the [tree view](Tree_view.md), select `Extrude`, and press **Space** in the keyboard to make it invisible.

8\. Switch to the [Sketcher Workbench](Sketcher_Workbench.md).

9\. In the [tree view](Tree_view.md), select `Chamfer`, and press **Space** in the keyboard to make it visible.

:   9.1. Choose the sloped face created by the chamfer operation (`Face3`).
:   9.2. Click on **[<img src=images/Sketcher_NewSketch.svg style="width:16px"> [NewSketch](Sketcher_NewSketch.md)**. In the **Sketch attachment** dialog, select `FlatFace`, and press **OK**.
:   9.3. The view should adjust automatically so that the camera is parallel to the selected face.
:   9.4. Draw a horizontal line in a general position on top of the face. The length is not important; we are just interested in its position.
:   9.5. Constrain the left endpoint to be `2.5 mm` away from the local X axis and from the local Y axis, using **[<img src=images/Sketcher_ConstrainDistanceX.svg style="width:16px"> [ConstrainDistanceX](Sketcher_ConstrainDistanceX.md)** and **[<img src=images/Sketcher_ConstrainDistanceY.svg style="width:16px"> [ConstrainDistanceY](Sketcher_ConstrainDistanceY.md)**.
:   9.6. Since the sketch is just an auxiliary object, we don\'t need to have it fully constrained. You can do this if you wish by assigning a fixed distance, say, `20 mm`, again with **[<img src=images/Sketcher_ConstrainDistanceX.svg style="width:16px"> [ConstrainDistanceX](Sketcher_ConstrainDistanceX.md)**.
:   9.7. Close the sketch.

<img alt="" src=images/04_T04_Part_ShapeString_support_sketch.png  style="width:500px;"> 
*Line being created with the sketcher, with constraints.*

<img alt="" src=images/05_T04_Part_ShapeString_support_sketch_3D.png  style="width:500px;"> 
*Sketch line created on top of the solid face, to be used as reference guide for positioning the extruded text.*

## Positioning the solid text in 3D space 

10\. In the [tree view](Tree_view.md), select `Extrude`, and press **Space** in the keyboard to make it visible.

11\. With `Extrude` still selected, in the **Data** tab of the [property editor](property_editor.md), click on the **Placement** value so the ellipsis button **...** appears on the right and click on that button.

:   11.1. Tick the option **Apply incremental changes**.
:   11.2. Change the **Rotation** to `Rotation axis with angle`; **Axis** to `Z` (by setting the `X`, `Y` and `Z` values of the axis inputboxes to `0`, `0` and `1` respectively, `Z` is the third inputbox), and **Angle** to `90 deg`, then click on **Apply**. This will apply a rotation around the Z-axis, and will reset the **Angle** field to zero.
:   11.3. Change the **Rotation** to `Rotation axis with angle`; **Axis** to `Y` (by setting the `X`, `Y` and `Z` values of the axis inputboxes to `0`, `1` and `0` respectively), and **Angle** to `45 deg`, then click on **Apply**. This will apply a rotation around the Y-axis, and will reset the **Angle** field to zero.
:   11.4. Click on **OK** to close the dialog.

12\. Switch again to the [Draft Workbench](Draft_Workbench.md).

:   12.1. Switch to \"Wireframe\" draw style with **View → [Draw style](Std_DrawStyle.md) → [<img src=images/DrawStyleWireFrame.svg style="width:16px"> Wireframe**, or press the **[<img src=images/DrawStyleWireFrame.svg style="width:16px"> [Wireframe](Std_DrawStyle.md)** button in the view toolbar. This will allow you to see the objects behind other objects.
:   12.2. Make sure the [Draft Snap](Draft_Snap.md) \"Snap to endpoint\" method is active. This can be done from the menu **Draft → Snapping → [<img src=images/Draft_Snap_Lock.svg style="width:16px"> [Toggle On/Off](Draft_Snap_Lock.md)**, and then ** → [<img src=images/Draft_Snap_Endpoint.svg style="width:16px"> [Endpoint](Draft_Snap_Endpoint.md)**, or by pressing the **[<img src=images/Draft_Snap_Lock.svg style="width:16px"> [ToggleSnap](Draft_Snap_Lock.md)** and **[<img src=images/Draft_Snap_Endpoint.svg style="width:16px"> [Snap endpoint](Draft_Snap_Endpoint.md)** buttons in the Snap toolbar.

13\. In the [tree view](Tree_view.md), select `Extrude`.

:   13.1. Click on **[<img src=images/Draft_Move.svg style="width:16px"> [Move](Draft_Move.md)**.
:   13.2. In the [3D view](3D_view.md) click on the upper left corner point of the `Extrude` object (1), and then click on the leftmost point in the line drawn with the sketcher (2).
:   13.3. If **[<img src=images/Draft_Snap_Endpoint.svg style="width:16px"> [Snap endpoint](Draft_Snap_Endpoint.md)** is active, as soon as you move the pointer close to a vertex, you should see that it attaches to it exactly.
:   
    **Note:**if you have problems snapping to vertices, make sure only the **[<img src=images/Draft_Snap_Endpoint.svg style="width:16px"> [Snap endpoint](Draft_Snap_Endpoint.md)** method is enabled. Having multiple snapping methods active at the same time may make it difficult to select the right feature.
:   13.4. The extruded text should now be inside the body of the `Chamfer` object.

![](images/06_T04_Part_ShapeString_move.svg ) 
*The extruded ShapeString should be moved to the position of the sketched line that lies on the face of the base body.*

![](images/07_T04_Part_ShapesString_Extrude_in_place.png ) 
*Extruded ShapeString positioned in the `Chamfer*.`

## Creating engraved text 

14\. Switch back to the [Part Workbench](Part_Workbench.md).

:   14.1. Switch to \"As is\" draw style with **View → [Draw style](Std_DrawStyle.md) → [<img src=images/DrawStyleAsIs.svg style="width:16px"> As is**, or press the **[<img src=images/DrawStyleAsIs.svg style="width:16px"> [As is](Std_DrawStyle.md)** button in the view toolbar. This will show all objects with the normal shading and color.
:   14.2. In the [tree view](Tree_view.md), select `Sketch`, and press **Space** in the keyboard to make it invisible.

15\. In the [tree view](Tree_view.md) select `Chamfer` first, and then `Extrude`.

:   15.1. Then press **[<img src=images/Part_Cut.svg style="width:16px"> [Cut](Part_Cut.md)**. This will create a `Cut` object. This is the final object.
:   
    **Note:**the order in which you select the objects is important for the cut operation. The base object is selected first, and the subtracting object comes at the end.
:   15.2. In the [tree view](Tree_view.md), select `Cut`, in the **View** tab change the value of **Line Width** to `2.0`.

![](images/08_T04_Part_ShapesString_Extrude_final_cut.png ) 
*Final model of a filleted cube, with carved text created from a ShapeString, Extrude, and boolean Cut operations.*

## Engraving 3D text with the PartDesign Workbench 

A similar process as described above can be done with the [PartDesign Workbench](PartDesign_Workbench.md).

1.  Create the **[<img src=images/Draft_ShapeString.svg style="width:16px"> [Draft ShapeString](Draft_ShapeString.md)** first.
2.  Create a **[<img src=images/PartDesign_Body_Tree.svg style="width:16px"> [PartDesign Body](PartDesign_Body.md)**, make it active, and add a base solid by adding primitives, or using a Sketch and extruding it with **[<img src=images/PartDesign_Pad.svg style="width:16px"> [PartDesign Pad](PartDesign_Pad.md)**.
3.  Move the `ShapeString` object into the active body.
4.  Attach the `ShapeString` object to one of the faces of the solid, or to a **[<img src=images/PartDesign_Plane.svg style="width:16px"> [PartDesign Plane](PartDesign_Plane.md)**, using **[<img src=images/Part_EditAttachment.svg style="width:16px"> [Part EditAttachment](Part_EditAttachment.md)**.
5.  Now create a **[<img src=images/PartDesign_Pad.svg style="width:16px"> [PartDesign Pad](PartDesign_Pad.md)** or a **[<img src=images/PartDesign_Pocket.svg style="width:16px"> [PartDesign Pocket](PartDesign_Pocket.md)** from the `ShapeString`, in order to produce an additive or a subtractive [feature](PartDesign_Feature.md) of the base body, respectively.

See the forum thread, [How to use ShapeStrings in PartDesign](https://forum.freecadweb.org/viewtopic.php?f=3&t=36623).

## Notes

-   To create curved text you can use <img alt="" src=images/FCCircularTextButtom.png  style="width:32px;"> [Macro FCCircularText](Macro_FCCircularText.md).
-   To import text from an SVG file look at the [Import text and geometry from Inkscape](Import_text_and_geometry_from_Inkscape.md) tutorial.


 {{PartDesign Tools navi}} {{Sketcher Tools navi}}



---
⏵ [documentation index](../README.md) > [Part](Category_Part.md) > [PartDesign](Category_PartDesign.md) > [Sketcher](Category_Sketcher.md) > [Draft](Draft_Workbench.md) > Draft ShapeString tutorial/tr
