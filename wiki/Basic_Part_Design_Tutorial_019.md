---
 TutorialInfo:
   Topic: Modeling
   Level: Beginner
   Author: Carlo Dormeletti <br>Ed Williams <br>Roy 043 
   Time: 1 hour
   FCVersion: 0.19 or higher
   SeeAlso: Basic_Part_Design_Tutorial
---

# Basic Part Design Tutorial 019

 



## Introduction

*This is an updated version of the [Basic Part Design Tutorial](Basic_Part_Design_Tutorial.md).*

 ![](images/Pd_tut_final_solid.png ) 

This tutorial introduces users to the [Part Design Workbench](PartDesign_Workbench.md). In this tutorial we will create a 3D solid model of the part shown in the image above. In the [drawing](TechDraw_Workbench.md) at the end of this paragraph all the necessary dimensions to complete the task are given.

We will start by creating a core solid shape from a base Sketch and then build on that shape, adding what are known as features. These features will either add material to, or remove material from the solid by use of additional sketches and accompanying feature operations.

We will follow some of the techniques described in [Advice for creating stable models](Feature_editing#Advice_for_creating_stable_models.md):

-   We will use a **master sketch**.
-   **Named constraints** will be used to hold dimensions that can be referenced later in the model construction.
    For instance, to change the model width from 53 mm, as in the technical drawing, to 55 mm we need only modify the **Length** value of the appropriate **named constraint** in the **master sketch** and the whole model will modify accordingly. This is *parametric* design in action.
-   **External geometries** are potentially subject to the [Topological Naming Problem](Topological_naming_problem.md). We will use them only when strictly necessary and will attempt to reference to the most **stable** elements available. Referencing edges and vertices of sketches is normally more stable than referencing edges and vertices of generated solid geometry.

This Tutorial will not use every feature and tool available in the Part Design Workbench, but will provide a basic foundation upon which users can build their knowledge and skills.

Feel free to signal any errors or problems in this forum thread: [New Part Design Tutorial for FC 019 and 020](https://forum.freecad.org/viewtopic.php?f=36&t=73235).

 <img alt="" src=images/Tutorial_Drawing_Sheet.png  style="width:900px;"> 

## Preliminary notes 

-   This tutorial will provide detailed instructions when it describes an operation for the first time. Subsequent operations will have a more concise description. When in doubt, find the operation that contains the more detailed description. For instance, when creating a sketch for the first time the process of choosing the sketch plane will be explained in detail, for subsequent sketches it will not.
-   All mentioned tools can be accessed from toolbars and from the menu.
-   This tutorial assumes that {{CheckBox|TRUE|Auto constraints}} in the Sketcher\'s **Edit controls** window is checked. This ensures that some constraints are applied automatically. Otherwise you will need to apply them yourself.
-   If the Sketcher Solver detects a redundant constraint it will turn the sketch orange in color. Before further constraints are added, redundant constraints should be removed. Redundant constraints are shown in the task panel, click the blue reference and press **Delete**.
-   The color mentioned above is a default color, it can be changed in the preferences. The same applies to the other colors mentioned in this tutorial.
-   You exit a Sketcher drawing tool by pressing the **Esc** key or by right-clicking an empty area of the [3D view](3D_view.md). The mouse cursor will change to the standard arrow cursor. If you press **Esc** an additional time you will exit sketch edit mode. To return to the editor, click the Model tab, then either double-click the Sketch element in the [Tree view](Tree_view.md), or right-click it and select **Edit sketch** from the context menu. To avoid leaving edit mode when pressing **Esc** too often, change the **Esc can leave sketch edit mode** preference, see [Sketcher Preferences](Sketcher_Preferences#General.md).
-   It\'s possible that some elements in a task panel, for instance the **OK** button, are not visible if the panel is not wide enough. You can make it wider by dragging its right border. Place your mouse pointer over the border, when the pointer changes to a two-way arrow, hold down the left mouse button and drag.
-   A **&gt;&gt;** button in a toolbar indicates that the toolbar is truncated. You can either use the mentioned button to expand it, or move the toolbar to a position where more room is available. To move a toolbar place your mouse pointer over the grip before the first icon in the toolbar, hold down the left mouse button and drag.
-   During the v0.21 development cycle a new icon was introduced for the [Sketcher Create polyline](Sketcher_CreatePolyline.md) tool: <img alt="" src=images/Sketcher_CreatePolyline.svg  style="width:24px;">. The old icon looks like this: <img alt="" src=images/Sketcher_CreatePolyline_rel_0.20.svg  style="width:24px;">. In this tutorial we will use the new icon.
-   See [Part Design Workbench Concepts](Part_and_PartDesign#PartDesign_Workbench_Concepts.md) for some conceptual background.
-   See the [Sketcher WorkBench](Sketcher_Workbench.md) for a more detailed explanation of some of the terminology used here.

## Startup

First make sure you are in the <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [Part Design Workbench](PartDesign_Workbench.md). If required select it from the [Workbench dropdown list](Std_Workbench.md). Once there, you will want to create a new document if you have not done so already. It is a good habit to save your work often, so first save the new document, giving it any name you choose.

All work in Part Design begins with a [body](Glossary#Body.md). Click <img alt="" src=images/PartDesign_Body.svg  style="width:24px;"> [Create new body](PartDesign_Body.md) to create and activate one. Note that it is also possible to skip this step: when creating a sketch using the Part Design <img alt="" src=images/PartDesign_NewSketch.svg  style="width:24px;"> [Create sketch](PartDesign_NewSketch.md) tool, if no existing body is found, a new one is automatically created and activated.

## Master sketch 

The master sketch contains the model\'s rectangular base shape and two **named constraints** that will supply correct dimensions to other parts of the model: **length** that will contain 53 mm (the result of adding the 39 mm dimension to the two 7 mm sides), and **width** that will contain 26 mm. To be able to take advantage of the model\'s symmetry in later steps, the top edge of the rectangle will be centered around the origin with a symmetrical constraint.

**Sketch**

 <img alt="Fig: MS1" src=images/Pd_start_00.png  style="width:300px;"> <img alt="Fig: MS2" src=images/Pd_tut_sketch_start.png  style="width:300px;"> <img alt="Fig: MS3" src=images/Pd_tut_sel_points_h.png  style="width:300px;"> <img alt="Fig: MS4" src=images/Pd_tut_rect_h_dim_end.png  style="width:300px;"> <img alt="Fig: MS5" src=images/Pd_tut_rect04.png  style="width:300px;"> <img alt="Fig: MS6" src=images/Pd_tut_rect_v3.png  style="width:300px;"> 

**Step A: Create the sketch**

1.  Click <img alt="" src=images/PartDesign_NewSketch.svg  style="width:24px;"> [Create sketch](PartDesign_NewSketch.md). This will create the sketch within the just created body. It will be named **Sketch**.
2.  A task panel like **Fig: MS1** will open where you have to choose to which plane the sketch will be attached.
    1.  Select **XY_Plane** from the list or select that plane in the [3D view](3D_view.md).
    2.  Click **OK**.
3.  FreeCAD automatically switches to the <img alt="" src=images/Workbench_Sketcher.svg  style="width:24px;"> [Sketcher Workbench](Sketcher_Workbench.md).
4.  The sketch is opened in edit mode: you will see something like **Fig: MS2**. The X and Y axis of the sketch are indicated as well as its origin (the red point).

**Step B: Add geometry**

1.  Click <img alt="" src=images/Sketcher_CreateRectangle.svg  style="width:24px;"> [Create rectangle](Sketcher_CreateRectangle.md).
2.  While the tool is active the cursor has this appearance:
    ![](images/Pd_tut_rec_cursor.png )
3.  Pick two points to create a rectangle roughly centered around the **Y axis** similar to **Fig: MS3**. Note:
    -   Don\'t place points on an axis as the Solver will automatically apply constraints that will create problems later.
    -   The dimensions of the rectangle are unimportant at this point. They will be assigned using constraints in a later step.
4.  Once done, press **Esc** or right-click to exit the tool.

**Step C: Assign a horizontal distance constraint**

1.  Select the line defined by **P2** and **P3** in **Fig: MS3**.
2.  Click <img alt="" src=images/Sketcher_ConstrainDistanceX.svg  style="width:24px;"> [Horizontal distance constraint](Sketcher_ConstrainDistanceX.md):
    1.  A dimension will appear between the endpoints of the selected line. This dimension is the current distance.
    2.  Additionally a dialog will appear:
        ![](images/Pd_tut_rect03.png )
    3.  Assign **Length = 53 mm**.
    4.  To be able to reference this dimension later a name is required. You are free to use any name, it need only be unique within the sketch. Assign **Name = length**.
    5.  Click **OK**.
3.  The result should resemble **Fig: MS4**

**Step D: Assign a symmetrical constraint**

1.  Select points **P2** and **P3** of the rectangle.
2.  Select the **origin** of the sketch. Note: the selection order of the points is important.
3.  Click <img alt="" src=images/Sketcher_ConstrainSymmetric.svg  style="width:24px;"> [Symmetrical constraint](Sketcher_ConstrainSymmetric.md).
4.  You will end up with something that resembles **Fig: MS5**.

**Step E: Assign a vertical distance constraint**

:   Assign a vertical distance constraint following the same procedure as used for the previous horizontal distance constraint:

1.  Select the line defined by **P3** and **P4** in **Fig: MS3**.
2.  Click <img alt="" src=images/Sketcher_ConstrainDistanceY.svg  style="width:24px;"> [Vertical distance constraint](Sketcher_ConstrainDistanceY.md):
    1.  Assign **Length = 26 mm**
    2.  Assign **Name = width**.
    3.  Click **OK**.
3.  The result should resemble **Fig: MS6**.
4.  The sketch is fully constrained now:
    -   The lines in the sketch are bright green.
    -   The **Solver messages** section of the task panel displays **Fully constrained**.
    -   If you select any line or vertex of the sketch and try to drag it, it won\'t move.

**Step F: Close the sketch**

:   Click **Close** at the top of the [tasks panel](Task_panel.md) to leave sketch edit mode.

 

## Main profile 

The main profile is created by [padding](PartDesign_Pad.md) a new sketch.

**Sketch001**

 <img alt="Fig. MP1" src=images/OffsetSketch001.png  style="width:240px;"> <img alt="Fig: MP2" src=images/Pd_tut_side_fc.png  style="width:240px;"> 

**Step A: Create the sketch**

:   Click <img alt="" src=images/PartDesign_NewSketch.svg  style="width:24px;"> [Create sketch](PartDesign_NewSketch.md) and create a sketch attached to the **YZ_Plane**. FreeCAD will assign the name **Sketch001**.

**Step B: Add geometry**

1.  Click <img alt="" src=images/Sketcher_CreatePolyline.svg  style="width:24px;"> [Create polyline](Sketcher_CreatePolyline.md) and make a shape like in **Fig: MP1**.
2.  The labels P1, P2 etc. will not appear in the sketch. They were added for reference.
3.  For the last point of the final segment make sure to pick the first point of the shape. The point will change color and you will see the symbol for a <img alt="" src=images/Sketcher_ConstrainCoincident.svg  style="width:24px;"> [Coincident constraint](Sketcher_ConstrainCoincident.md) appear near the cursor. Coincident constraints have to be explicit. Just having two points visually coincident is not sufficient.
4.  Press **Esc** or right-click to exit the tool.

**Step C: Assign constraints**

1.  The three vertical and horizontal constraints you see in the image should have been added automatically provided you drew those lines that way. If you didn\'t you need to add them.
2.  Select the point **P2** and the **Y axis** and apply a <img alt="" src=images/Sketcher_ConstrainPointOnObject.svg  style="width:24px;"> [Point onto object constraint](Sketcher_ConstrainPointOnObject.md).
3.  Select the **origin** and the point **P1** and apply a <img alt="" src=images/Sketcher_ConstrainHorizontal.svg  style="width:24px;"> [Horizontal constraint](Sketcher_ConstrainHorizontal.md). Why not a <img alt="" src=images/Sketcher_ConstrainCoincident.svg  style="width:24px;"> [Coincident constraint](Sketcher_ConstrainCoincident.md)? you might ask. Try it (and undo). The sketch will turn orange and a solver message **Redundant constraints** will appear. Because the line P1 to P2 has already been constrained to be vertical, the only remaining degree of freedom is P1\'s Y coordinate. The coincidence constraint sets both the X and Y coordinates to zero, but the X coordinate is already determined. The horizontal constraint, on the other hand, only sets the Y coordinate to zero, which is sufficient.
4.  Select the line defined by the points **P2** and **P3**, apply a <img alt="" src=images/Sketcher_ConstrainDistanceX.svg  style="width:24px;"> [Horizontal distance constraint](Sketcher_ConstrainDistanceX.md), and assign **Length = 5 mm**.
5.  Select the line defined by the points **P1** and **P2**, apply a <img alt="" src=images/Sketcher_ConstrainDistanceY.svg  style="width:24px;"> [Vertical distance constraint](Sketcher_ConstrainDistanceY.md), and assign **Length = 26 mm**.
6.  Select the line defined by the points **P1** and **P4** and apply a <img alt="" src=images/Sketcher_ConstrainDistanceX.svg  style="width:24px;"> [Horizontal distance constraint](Sketcher_ConstrainDistanceX.md):
    1.  For this value you will use a **named constraint** using [Expressions](Expressions.md). To do so you have to click the little button in the **Length** input field: <img alt="" src=images/Bound-expression.svg  style="width:24px;">.
    2.  You will be presented with a new dialog named **Formula editor** that contains an input field and a **Result:** label, similar to the image below:
        ![](images/Pd_tut_expressions.png )
        When you start typing in the input field, you will be presented with some autocompletions.
    3.  Select the label of the sketch. In our case we want **>.**. Note the period after the label.
    4.  To select the **named constraint** \"width\", you first have to enter **Constraints.** with the period. Here autocomplete works.
    5.  To add \"width\", as yet autocompletion is not available, so complete the cell to read **>.Constraints.width**. If all went well the red error message after **Result:** has been replaced by the correct value as in the image below:
        ![](images/Pd_tut_expression_end.png )
    6.  Click **OK** to close the **Formula editor** dialog.
    7.  Click **OK** to close the **Insert length** dialog.
7.  You should have a fully constrained sketch similar to **Fig: MP2**.
8.  Note the different colors used for distance constraints assigned using expressions, and those assigned specifying a length.

**Step D: Close the sketch**

:   Click **Close** at the top of the [tasks panel](Task_panel.md) to leave sketch edit mode.

**Pad**

<img alt="Fig: MP3" src=images/Pd_tut_pad1.png  style="width:240px;">

1.  Make sure **Sketch001** is selected.
2.  Click <img alt="" src=images/PartDesign_Pad.svg  style="width:24px;"> [Pad](PartDesign_Pad.md):
    1.  The **Pad parameters** task panel opens.
    2.  For **Type** select {{ComboBox|Dimension}}.
    3.  For **Length** again use an expression, but this time enter **>.Constraints.length**. This should evaluate to 53 mm.
    4.  Select {{CheckBox|TRUE|Symmetric to plane}}.
    5.  Click **OK** to close the task panel.
3.  You should now have a solid as shown in **Fig: MP3**.

 

## Corner cutouts 

For the corner cutouts two features are added to the model. A [pocket](PartDesign_Pocket.md), based on another sketch, is used to create the first cutout, and this feature is then [mirrored](PartDesign_Mirrored.md).

**Sketch002**

 <img alt="Fig: CC1" src=images/Pd_tut_sk2_start.png  style="width:300px;"> <img alt="Fig: CC2" src=images/Pd_tut_sk2_eg01.png  style="width:300px;"> <img alt="Fig: CC3" src=images/Pd_tut_sk2_end.png  style="width:300px;"> 

**Step A: Hide the solid**

:   Hide the just created solid: Select **Pad** and click the **Spacebar**.

**Step B: Create the sketch**

:   Click <img alt="" src=images/PartDesign_NewSketch.svg  style="width:24px;"> [Create sketch](PartDesign_NewSketch.md) and create a sketch attached to the **XZ_Plane**. The sketch will be named **Sketch002**.

**Step C: Add geometry**

1.  Select <img alt="" src=images/Sketcher_CreateRectangle.svg  style="width:24px;"> [Create rectangle](Sketcher_CreateRectangle.md), and create a rectangle. Do not create it too near an axis, to avoid any automatic constraints that would make it difficult to move it into the correct position later.
2.  Exit the tool.

**Step D: Assign dimensional constraints**

1.  Select one of the horizontal lines, apply a <img alt="" src=images/Sketcher_ConstrainDistanceX.svg  style="width:24px;"> [Horizontal distance constraint](Sketcher_ConstrainDistanceX.md), and assign a value of **11 mm**.
2.  Select one of the vertical lines, apply a <img alt="" src=images/Sketcher_ConstrainDistanceY.svg  style="width:24px;"> [Vertical distance constraint](Sketcher_ConstrainDistanceY.md), and assign a value of **5 mm**.
3.  You should obtain something similar to **Fig: CC1**.

**Step E: Close the sketch**

:   Click **Close**. **Sketch002** is not fully constrained at this stage.

**Step F: Make previous sketches visible**

:   To use [external geometry](Sketcher_External.md), the sketches whose elements we want to reference must be visible. Make sure **Sketch** and **Sketch001** are both visible. Use the **Spacebar** to toggle visibility if needed. Expand the **Pad** node in the [Tree view](Tree_view.md) to access **Sketch001**.

**Step G: Add external geometry and fully constrain the sketch**

1.  Double click **Sketch002** to enter edit mode.
2.  Rotate the view so you can clearly see the points as shown in **Fig: CC2**. This will ease subsequent steps. Note that the rectangle\'s initial position may be different in your sketch.
3.  Click <img alt="" src=images/Sketcher_External.svg  style="width:24px;"> [External geometry](Sketcher_External.md).
4.  While the tool is active the cursor has this appearance:
    ![](images/Pd_tut_eg_cursor.png )
5.  Select point **P1** in **Fig: CC2**. The selected point is added to the sketch as external geometry. In the **Elements** section of the task panel it will appear with a purple X icon or, <small>(v0.21)</small> , a purple dot icon.
6.  With the tool still active select point **P2** in **Fig: CC2**. This external geometry should also appear in the **Elements** section.
7.  Exit the tool.
8.  Select point **P1** and point **P3** and apply a <img alt="" src=images/Sketcher_ConstrainVertical.svg  style="width:24px;"> [Vertical constraint](Sketcher_ConstrainVertical.md). The rectangle will be aligned with the X position of **P1**.
9.  Select point **P2** and point **P3** and apply a <img alt="" src=images/Sketcher_ConstrainHorizontal.svg  style="width:24px;"> [Horizontal constraint](Sketcher_ConstrainHorizontal.md). The rectangle will be aligned with the Y position of **P2**.
10. You should have a fully constrained sketch similar to **Fig: CC3**.

**Step H: Close the sketch**

:   Click **Close**.

**Pocket**

 <img alt="Fig: CC4" src=images/Pd_tut_pck01.png  style="width:300px;"> <img alt="Fig: CC5" src=images/Pd_tut_pck02-mir.png  style="width:300px;"> 

To create the cutouts we will use the <img alt="" src=images/PartDesign_Pocket.svg  style="width:24px;"> [Pocket](PartDesign_Pocket.md) tool. This tool is the opposite of the Pad tool. Whereas the Pad tool adds material, the Pocket tool removes material.

1.  Select **Sketch002**.
2.  Click <img alt="" src=images/PartDesign_Pocket.svg  style="width:24px;"> [Pocket](PartDesign_Pocket.md):
    1.  The **Pocket parameters** task panel opens.
    2.  Select **Type** {{ComboBox|Through all}}.
    3.  Check {{CheckBox|TRUE|Reversed}}
    4.  Click **OK**.
3.  You should have something that resembles **Fig: CC4**

**Mirror**

Instead of creating another sketch and pocketing it, we take advantage of the model\'s symmetry about the YZ plane and use <img alt="" src=images/PartDesign_Mirrored.svg  style="width:24px;"> [Mirrored](PartDesign_Mirrored.md) to create the second cutout.

1.  Select **Pocket**.
2.  Click <img alt="" src=images/PartDesign_Mirrored.svg  style="width:24px;"> [Mirrored](PartDesign_Mirrored.md):
    1.  The **Mirrored parameters** task panel opens.
    2.  Select **Plane** {{ComboBox|Vertical sketch axis}} from the pulldown menu. The plane will be defined by this axis (the Y axis) and also by the Z axis of the sketch. Note that selecting **Base YZ Plane** would have the same result.
    3.  Click **OK**.
3.  You should now have a part that looks like **Fig: CC5**.

 

## Sides

The sides are created in a similar manner, but instead of removing material we will add material with a [pad](PartDesign_Pad.md) feature.

**Sketch003**

 <img alt="Fig: SD1" src=images/Pd_tut_sk3_1.png  style="width:300px;"> <img alt="Fig: SD2" src=images/Pd_tut_pad001.png  style="width:300px;"> <img alt="Fig: SD3" src=images/Pd_tut_pad02-mir.png  style="width:300px;"> 

1.  Make sure **Sketch** is visible, and **Mirrored** is hidden.
2.  Click <img alt="" src=images/PartDesign_NewSketch.svg  style="width:24px;"> [Create sketch](PartDesign_NewSketch.md) and create a new sketch attached to the **XY_Plane**. The sketch will be named **Sketch003**.
3.  Click <img alt="" src=images/Sketcher_CreateRectangle.svg  style="width:24px;"> [Create rectangle](Sketcher_CreateRectangle.md) and create a rectangle similar to the smaller rectangle in **Fig: SD1**. Because the rectangle is offset from the X axis this should not trigger an automatic <img alt="" src=images/Sketcher_ConstrainPointOnObject.svg  style="width:24px;"> [Point onto object constraint](Sketcher_ConstrainPointOnObject.md).
4.  Exit the tool.
5.  Click <img alt="" src=images/Sketcher_External.svg  style="width:24px;"> [External geometry](Sketcher_External.md).
6.  Select the point **P1** as shown in **Fig: CC2**.
7.  Exit the tool.
8.  Apply these constraints:
    1.  Select one of the horizontal lines, apply a <img alt="" src=images/Sketcher_ConstrainDistanceX.svg  style="width:24px;"> [Horizontal distance constraint](Sketcher_ConstrainDistanceX.md), and assign a value of **7 mm**.
    2.  Select one of the vertical lines, apply a <img alt="" src=images/Sketcher_ConstrainDistanceY.svg  style="width:24px;"> [Vertical distance constraint](Sketcher_ConstrainDistanceY.md), and assign this expression: **>.Constraints.width**.
    3.  Select the **top-left** point of the created rectangle (marked **TL** in **Fig: SD1**) and the newly added **external geometry point** and apply a <img alt="" src=images/Sketcher_ConstrainCoincident.svg  style="width:24px;"> [Coincident constraint](Sketcher_ConstrainCoincident.md).
9.  The sketch should be fully constrained now.
10. Click **Close**.

**Pad001**

1.  Select **Sketch003**.
2.  Click <img alt="" src=images/PartDesign_Pad.svg  style="width:24px;"> [Pad](PartDesign_Pad.md):
    1.  Assign **Type =** {{ComboBox|Dimension}}.
    2.  Assign **Length = 16.7 mm**
    3.  Click **OK**.
3.  You should have a result as shown in **Fig: SD2**

**Mirrored001**

1.  Select **Pad001**.
2.  Click <img alt="" src=images/PartDesign_Mirrored.svg  style="width:24px;"> [Mirrored](PartDesign_Mirrored.md):
    1.  Make sure **Plane** {{ComboBox|Vertical sketch axis}} is selected.
    2.  Click **OK**.
3.  You should now have a part that looks like **Fig: SD3**.

**Note**

Our two mirror operations have a common symmetry plane, so we could have made our model a little simpler by combining them. We would:

1.  Omit the first **Mirror** operation.
2.  Select both **Pad001** and **Pocket** in step 1 of the above **Mirrored001** operation.

This emphasizes the important concept that we are mirroring the selected features (the operations we performed on the body, in the selected order), not the body itself.

 

## Center hole 

Now it is time for the most challenging part of our modeling, a challenge that arises because some of the dimensions of the center hole are defined along the slanted face. If you use this face, created by padding **Sketch001**, as a reference for the next sketch, you expose yourself to the [Topological Naming Problem](Topological_naming_problem.md). A better solution is to reference **Sketch001** itself.

**Sketch004**

 <img alt="Fig: CH1" src=images/Pd_tut_cen01.png  style="width:240px;"> <img alt="Fig: CH2" src=images/Pd_tut_cen02.png  style="width:240px;"> 

1.  Make **Sketch001** visible, and hide **Sketch** and **Mirrored001**.
2.  Click <img alt="" src=images/PartDesign_NewSketch.svg  style="width:24px;"> [Create sketch](PartDesign_NewSketch.md) and create a new sketch attached to the **YZ_Plane**. The sketch will be named **Sketch004**.
3.  Click <img alt="" src=images/Sketcher_CreatePolyline.svg  style="width:24px;"> [Create polyline](Sketcher_CreatePolyline.md) and trace a polyline like that indicated by the points **P1**, **P2**, **P3** and **P4** in **Fig: CH1**.
4.  Remember to close the polyline by picking the first point. This will create the required <img alt="" src=images/Sketcher_ConstrainCoincident.svg  style="width:24px;"> [Coincident constraint](Sketcher_ConstrainCoincident.md).
5.  Exit the tool.
6.  Check the applied constraints:
    -   Delete the redundant <img alt="" src=images/Sketcher_ConstrainVertical.svg  style="width:24px;"> [Vertical constraint](Sketcher_ConstrainVertical.md) applied to the line defined by **P1** and **P2**.
    -   Make sure a <img alt="" src=images/Sketcher_ConstrainHorizontal.svg  style="width:24px;"> [Horizontal constraint](Sketcher_ConstrainHorizontal.md) has been applied to the lines defined by **P1** and **P4**, and **P2** and **P3**.
    -   Make sure a <img alt="" src=images/Sketcher_ConstrainPointOnObject.svg  style="width:24px;"> [Point onto object constraint](Sketcher_ConstrainPointOnObject.md) has been applied to **P1** and the **Y axis**, and to **P2** and the **Y axis**.
7.  Click <img alt="" src=images/Sketcher_External.svg  style="width:24px;"> [External geometry](Sketcher_External.md)
8.  Select the line defined by **EGP1** and **EGP2** in **Sketch001**, indicated by the purple color in **Fig: CH2**.
9.  Exit the tool.
10. Apply a <img alt="" src=images/Sketcher_ConstrainPointOnObject.svg  style="width:24px;"> [Point onto object constraint](Sketcher_ConstrainPointOnObject.md) to **P3** and the **external geometry**, and repeat this for **P4**. This will make the line defined by **P3** and **P4** coincident with the line defined by **EGP1** and **EGP2**.
11. Select the line **P3** to **P4**, apply a <img alt="" src=images/Sketcher_ConstrainDistance.svg  style="width:24px;"> [Distance constraint](Sketcher_ConstrainDistance.md), and assign 
**Length = 17 mm**
12. Select the points **EGP2** and **P4**, apply a <img alt="" src=images/Sketcher_ConstrainDistance.svg  style="width:24px;"> [Distance constraint](Sketcher_ConstrainDistance.md), and assign **Length = 7 mm**.
13. This will result in a fully constrained sketch like **Fig: CH2**.
14. Click **Close**.
15. Hide **Sketch001**.

**Pocket001**

1.  Select **Sketch004**.
2.  Click <img alt="" src=images/PartDesign_Pocket.svg  style="width:24px;"> [Pocket](PartDesign_Pocket.md):
    1.  Select **Type** {{ComboBox|Two Dimensions}}.
    2.  Assign **8.5 mm** to **Length** and **2nd length**.
    3.  Click **OK**.
3.  Select the newly created **Pocket001**.
4.  Change its **Refine** property to **True**.

**Notes**

1.  For **Pocket001** we could have alternatively used **Type** {{ComboBox|Dimension}}, checked **Symmetric to Plane**, and entered **17 mm** for the **Length** value.
2.  **Refine** will try to remove seams left by previous operations. It is advisable to only refine the final solid, as some operations can fail if a previous feature has been refined. However, there are also cases where refine can make an operation succeed. So in case of problems check this property and test. Unfortunately there is not yet a general rule to follow.

 

## Result

The model is complete. It should look like the image below.

Finally, select **Sketch** in the [Tree view](Tree_view.md) and on the Data tab of the [Property editor](Property_editor.md) look for **Sketch → Constraints**. Expand that node and changed the **length** and **width** constraints. The model should change parametrically.

 ![](images/Pd_tut_final_solid.png ) 

 {{PartDesign Tools navi}} {{Sketcher Tools navi}}



---
⏵ [documentation index](../README.md) > [PartDesign](Category_PartDesign.md) > [Sketcher](Category_Sketcher.md) > Basic Part Design Tutorial 019
