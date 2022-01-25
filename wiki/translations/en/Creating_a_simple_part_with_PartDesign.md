---
- TutorialInfo:   Topic:Modeling
   Level:Beginner
   Author:GlouGlou
   Time:1 hour
   FCVersion:0.17 or above
   Files:[https://github.com/FreeCAD/Examples/blob/master/Creating_a_simple_PartDesign_Body.FCStd Creating a simple PartDesign Body.FCStd]
---

# Creating a simple part with PartDesign/en





![](images/GGTuto1_Vue.PNG )

This tutorial aims to teach FreeCAD beginners a few basic features through an example. After covering the basics in the [User hub](User_hub.md), you will be able to model a first part step by step.

**We will cover in this tutorial in particular:**

-   Using [Part Design workbench](PartDesign_Workbench.md), tracing the sketch.
-   Using Pad and Pocket features.
-   Changing color and transparency.
-   Moving the part manually.
-   Displaying reference dimensions in the sketch.
-   Editing one or more dimensions.
-   Using external geometry feature and using a reference plane to centre a hole.

### Using [Part Design workbench](PartDesign_Workbench.md), tracing the sketch 

Create a new document and switch to the **[<img src=images/Workbench_PartDesign.svg style="width:24px"> '''Part Design workbench'''** using either the [workbench selector](Getting_started#Exploring_the_interface.md) (labelled 10 in the linked image) or by going to the *View → Workbench* menu. FreeCAD will start with toolbars at the top, the combo view to the left and the 3D view at the right.

**Create body:**

Press <img alt="" src=images/PartDesign_Body.svg  style="width:24px;"> [Create body](PartDesign_Body.md). ***Note:** do not confuse the Body, which icon is blue, with the Part container which icon is yellow.* In the Model tab under the Combo View sidebar, a new object labelled \"Body\" appears under the document label, which is currently \"Unnamed\" since we haven\'t saved our document yet. The Body is a container in which Part Design features are sequentially arranged to form a single solid. It contains its own reference axes and planes. It will be highlighted in light blue in the Model tree, which means that it is active, that is to say that we can edit the elements it contains as well as add new elements to it. If it\'s not highlighted, double-click it or right-click and select *Toggle active body* in the contextual menu. In front of the Body label, there is a blue icon identical to the one above, and an arrow or a plus sign, depending on your operating system. Clicking on the arrow or plus sign in front of Body expands its content. At this point, it only contains an element labelled *Origin*. In front of this *Origin* is also an arrow or plus sign. Click on it to expand its content. It reveals the aforementioned reference axes and planes as shown in the image below:

![](images/PartDesign_Body_tree_Unnamed.png ) *The newly created active Body with its content expanded.*

The *Origin* is greyed out, which indicates that its content is not visible in the 3D view. You can make *Origin*\'s content visible in the 3D view by selecting *Origin* and pressing the spacebar on your keyboard. *Origin* will now show black in the tree. Press the spacebar again to hide its content in the 3D view. Click again on the arrow or plus sign in front of *Origin* to collapse its content in the Model tree.

Before we continue, let\'s take the opportunity to rename the Body.

**Rename body:**

In the Model tree, click on the Body with the right mouse button. Select Rename and type a name, for example \"Body part1\" and press **Enter** to validate.

**Create sketch:**

We will now trace the sketch which defines the general shape of the part. A sketch is a diagram describing a profile to be applied to a feature in order to produce a shape. It can be either \"positive\" or \"additive\", like a pad for example; or \"negative\" or \"subtractive\", like a pocket.

Here, since the part\'s general shape is regular along the Y axis, we will create the Pad along this axis.

Press <img alt="" src=images/Sketcher_NewSketch.svg  style="width:24px;"> [New sketch](Sketcher_NewSketch.md). The Combo View now switches to the **Tasks** tab and displays the *Select feature* dialog. This dialog expects the selection of a plane to which to attach our sketch, and lists the available planes. Select *XZ\_Plane (Base plane)* and press **OK**. The interface now changes, the Sketcher now takes over and its toolbars appear above the 3D view. We find ourselves on the XZ plane of the body to trace the sketch.

To aid with sketching, set the following options in \"Edit controls\" in the Tasks panel to the left:

-   Show grid: checked
-   Grid size: 10 mm
-   Auto constraints: checked

We will trace the following sketch:

![](images/GGTuto1_0.PNG )

**Let\'s start with the first segments:**

Select the <img alt="" src=images/Sketcher_Line.svg  style="width:24px;"> [Line](Sketcher_CreateLine.md) tool. Click on the origin point, first making sure that a small red dot appears besides and to the right of the mouse pointer. Click next on the X axis about 10 squares to the right or at about 100 mm. If the segment is not exactly 100 mm at this point, it does not matter, we will later give it a fixed dimension that will constrain this length.

Do the same for the other segments, try to aim at the points that you have created which must light up in yellow. Which means that these points will be coincident. You should get pretty much this:

![](images/GGTuto1_1.PNG )

Note the small red lines above and beside the segments you have drawn: these are horizontal and vertical constraints. Your lines are forced to stay either horizontal or vertical. Note also the symbol in the form of a small arc on the left: it means that the point is fixed to the Z axis.

Now pick different line segments with the left mouse button and while keeping the left button pressed, drag the mouse to try to move them: some are free, others not.

**Applying constraints:**

At the top of the combo box, in the Tasks panel, you can read the number of degrees of freedom of the already sketched elements: it must be about 6, the objective of the constraints is to reduce the number of degrees of freedom to 0.

The slanted line should be free to rotate at this time: we will give it an angle constraint to fix it.

Click on the slanted line, then the bottom line; once selected these lines will turn dark green; then click the <img alt="" src=images/Constraint_InternalAngle.svg  style="width:24px;"> [Constrain internal angle](Sketcher_ConstrainAngle.md) icon.

![](images/GGTuto1_2.PNG )

Enter a value of 30°. Both lines have a fixed angle now. The constraint was created to the left of the sketch; with the mouse, move it inside the profile.

We will now constrain the bottom line with a dimension: select it then click on <img alt="" src=images/Constraint_HorizontalDistance.svg  style="width:24px;"> [Constrain horizontal distance](Sketcher_ConstrainDistanceX.md).

Enter a value of 100 mm. The vertical line on the right now aligns exactly with the grid\'s 10th square to the right of the origin.

Let\'s set the overall height to the profile by selecting the highest point on the left then the origin point. Click on <img alt="" src=images/Constraint_VerticalDistance.svg  style="width:24px;"> [constrain vertical distance](Sketcher_ConstrainDistanceY.md), enter a value of 50 mm.

Do the same for the horizontal length of the sloped line with another 50 mm horizontal distance constraint.

Move the dimensions away from the profile for better visibility. You should now have something like this:

![](images/GGTuto1_3.PNG )

Notice that the number of degrees of freedom reduced to 2. These are the ends still open.

**Tracing the arc**

Click on <img alt="" src=images/Sketcher_Arc.svg  style="width:24px;"> [Arc](Sketcher_CreateArc.md), position the center at approximately x = 80 y = 30; then click to define the first starting point of the arc on the upper horizontal line\'s right end point; then click to define the end of the arc to the right vertical line\'s upper end point (make sure the points are highlighted in yellow before clicking).

Give the radius a radius constraint: select the arc, then click on <img alt="" src=images/Constraint_Radius.svg  style="width:24px;"> [Constrain radius](Sketcher_ConstrainRadius.md) then enter a value of 20 mm.

Now let\'s make the arc tangent to the lines it\'s connected to: select the arc, then the top line, then click on <img alt="" src=images/Constraint_Tangent.svg  style="width:24px;"> [Constrain tangent](Sketcher_ConstrainTangent.md). A *Constraint substitution* message appears, click **OK**. Do the same for the tangent constraint on the other side of the arc.

We proceeded in two stages to create the sketch, but we could also have traced the profile completely before constraining it fully.

**Fully constrained sketch:**

If you worked well, you should get this:

![](images/GGTuto1_4.PNG )

The sketch has become green, which means that it is fully constrained. There is no longer any ambiguity, everything is perfectly defined. This is confirmed by the solver message at the top left. Also note that the center of the arc has moved slightly, indeed giving these last three constraints, FreeCAD has calculated the true position of the center.

If your sketch is not yet green, one or more points are not coincident (2 points can be superimposed yet not be coincident). Make a small window (capture window) around a point to select, and create a <img alt="" src=images/Constraint_PointOnPoint.svg  style="width:24px;"> [Coincident constraint](‎Sketcher_ConstrainCoincident.md). 
*Note: don\'t mistake the Coincident constraint for the Sketcher Point; while their icons are very similar, the latter has a larger icon; it adds a lone point in the sketch.*

Proceed in the same way with all the points.

If your sketch is still not green, verify that all lines (but the slanted one) have either a <img alt="" src=images/Constraint_Horizontal.svg  style="width:24px;"> [Horizontal](Sketcher_ConstrainHorizontal.md) or <img alt="" src=images/Constraint_Vertical.svg  style="width:24px;"> [Vertical](Sketcher_ConstrainVertical.md) constraint, and add if necessary.

### Using Pad and Pocket features 

Click on **Close** in the Tasks tab, at the top left corner. We automatically exit the Sketcher workbench, and the Part Design workbench is activated again. The Combo View switches back to the Model tab. If you left your *Body part1* expanded, you will see a new **Sketch** element below *Origin*, and nested under the Body.

At this point, let\'s save our document. Give it a name (for example \"tutorial1\", or any name that you find relevant). It is good practice to save your document often, for example after completing a sketch or a feature.

Click on <img alt="" src=images/Std_ViewIsometric.svg  style="width:24px;"> **Isometric view** then <img alt="" src=images/Std_ViewFitAll.svg  style="width:24px;"> [Fit all](Std_ViewFitAll.md), which gives a centered 3D isometric view.

Click on <img alt="" src=images/PartDesign_Pad.svg  style="width:24px;"> [Pad](PartDesign_Pad.md), enter a length of 30 mm. Click **OK**, the shape is completed. In the Model tree, a **Pad** object (that we call feature) appears instead of the Sketch. In fact, it has claimed Sketch, since it is based on it; clicking on the arrow or plus sign in front of *Pad* to expand it will reveal the Sketch underneath, which was automatically made hidden (its label is grayed out).

Note that the shape created forms a solid.

![](images/GGTuto1_5.PNG )

**Creating the hole**

Click on the top (square) side of the part and click the <img alt="" src=images/Sketcher_NewSketch.svg  style="width:24px;"> icon to create a new sketch. FreeCAD creates a new sketch attached to this face. So we are on a plane parallel to the absolute plane XY, but offset in height from the height of the piece, i.e. 50 mm.

You can switch the 3D window to an isometric view <img alt="" src=images/Std_ViewIsometric.svg  style="width:24px;"> or stay in top view <img alt="" src=images/Std_ViewTop.svg  style="width:24px;">. At any time, you can return to Sketch view (the view is oriented to face the sketch plane) using the <img alt="" src=images/Sketcher_ViewSketch.svg  style="width:24px;"> [Sketcher ViewSketch](Sketcher_ViewSketch.md) icon.

Note that the origin of this new sketch is that of the body. They may be different, but here are confounded with the absolute origin.

With the <img alt="" src=images/Sketcher_Circle.svg  style="width:24px;"> [Circle](Sketcher_CreateCircle.md) tool, click roughly in the center of the face and make a circle of any radius.

Select the circle then create a <img alt="" src=images/Constraint_Radius.svg  style="width:24px;"> [Radius constraint](Sketcher_ConstrainRadius.md), enter a value of 5 mm.

Select the center of the circle then create a <img alt="" src=images/Sketcher_ConstrainLock.svg  style="width:24px;"> [Lock constraint](Sketcher_ConstrainLock.md); double-click on the horizontal dimension and enter -65 mm (here we indicate a position relative to the origin of the sketch). Do the same for the vertical dimension (-15 mm). The circle takes its correct position and the sketch becomes green, indicating it is fully constrained:

![](images/GGTuto1_6.PNG )

Close the sketch; in the Model tree, a new **Sketch001** object has appeared below Pad. While Sketch001 is still selected, click on <img alt="" src=images/PartDesign_Pocket.svg  style="width:24px;"> [Pocket](PartDesign_Pocket.md).

Pocket is a feature called \"subtractive\", it removes material from our part, here in the form of a cylinder since the sketch is a circle. Set \"Through all\" to completely cut the part. Press **OK** to complete. In the Model tree, a new element labelled **Pocket** appears at the bottom of the Body part1, and claims Sketch001.

### Changing color and transparency 

It is possible to change the color of the part, it is often useful to distinguish a part among others. The transparency of the piece can also be modified, which is useful for visualizing its internals.

Select the **Body part1** body; make sure that the Model tab of the Combo View is selected and go to the lower part of the Combo View, then click on the View tab; locate the *Shape Color* property; you may need to use the vertical scroll bar to the right to find it. \'\'You can also widen the Property column: hover your mouse pointer over the separating line between the *Property* and *Value* headers; when the pointer turns into a double-sided arrow, press and hold your left mouse button and drag sideways, then release.\'\' In the right column, click on the gray square, which opens the **Select Color** dialog. Pick another color then click OK. Next, again in the View tab, change the value of Transparency, for example to 50 and press **Enter** to complete (0 = totally opaque, 100 = totally transparent).

The hole is now visible inside the part. This is often useful for seeing the hidden or internal faces of the model.

You can also vary \"Line Color\" and \"Line Width\" to change the line thickness and the color of the part outline.

### Manually move the part 

Go to the *View* menu and select *Toggle axis cross*. These are the absolute axes. You should see in the 3D view, the 3 axes X, Y, Z in red, green and blue. This landmark will help us to orient ourselves in space. This landmark is fixed and immutable, it is either the view that rotates or the object that rotates in this space.

Select the Body; at the bottom of the Combo View on the left, you can see this (the *Data* tab needs to be on the foreground, you may need to click on the *Data* tab to make it visible):

![](images/GGTuto1_10.PNG )

Click on the three small dots, i.e., the ellipsis (if they don\'t appear, click on the Value section of the **Placement** field); this opens a new dialog in the Tasks panel. Using the arrows you can vary the position and angles of the part. It is actually the position of the body (so its origin) that moves in space, the orientation of the 3D view does not change.

Another method: in the Combo View, select the Body and click on the right button of the mouse, then select *Transform*. A view like this appears:

![](images/GGTuto1_11.PNG )

Hold and drag the cones along the axes or the spheres to move the body in all directions.

Validate. Then reset angles and coordinates to 0.

### Displaying reference dimensions in the sketch 

It may be useful to know the dimensions of some parts of the sketch, from the internal calculation of FreeCAD. It can be used just for reference, or use them later to set other dimensions for example.

In the Model tree, if necessary expand *Body part1* then *Pad* to show the first Sketch. Double-click on it (or right-click and select *Edit sketch* in the contextual menu) then click on <img alt="" src=images/Sketcher_ToggleConstraint.svg  style="width:24px;"> [Toggle Constraint](Sketcher_ToggleDrivingConstraint.md). (**Note:** depending on your computer display resolution, this icon may not be visible. At the right end of the Constraints toolbar, you may find a **»** button. Click on it to expand and access collapsed icons.) From now on, we can create reference dimensions rather than dimensional constraints: they will be blue and will have no influence on the shapes of the sketch from which they come, they are calculated automatically.

You can display these dimensions for example:

![](images/GGTuto1_7.PNG )

We can see for example that the arc has a length of 20 since it\'s tangent with the edges.

We can also see that FreeCAD calculates the left face (50-50xTAN 30 °), as well as the distance dimension of the axis of the arc with the origin.

### Editing one or more dimensions 

During modeling, you can vary the dimensions of the model. It\'s very simple: for the thickness of the piece, double-click Pad, then enter a new value, 40mm for example. In the lower part of the combo view, you can change this value as well. Validate, the shape of the object has changed.

Do the same for the total length of the piece: double-click on Sketch, then double-click on the 100 mm dimensional constraint, change it to 110 mm then validate.

We can see that the piece was enlarged, but the hole is no longer centered in the middle of the top face. That\'s because it has been constrained to the sketch origin. Which does not necessarily correspond to what one would like, the hole should remain in the center, whatever the size of the face.

### Center the hole 

**First method using external geometry.**

Edit again the sketch of the hole and erase its horizontal and vertical distance constraints.

Then click on <img alt="" src=images/Sketcher_External.svg  style="width:24px;"> [External Geometry](Sketcher_External.md).

We will now create two lines in the sketch, but extracted from a shape (or feature) external to this one and previously defined: that of the Pad.

Click on a vertical edge at the top of the part. For example, the edge slope side.

A new magenta line will appear above the edge. Repeat for the other edge, on the rounded side.

We can now use these lines (and especially their end points) to centre the circle, however we must add two construction lines: for example the diagonals.

Click on <img alt="" src=images/Sketcher_AlterConstruction.svg  style="width:24px;"> [Construction Mode](Sketcher_ToggleConstruction.md), we switch to construction mode: the lines will be blue and will be discarded outside of the sketch editing mode. They will allow to fix the center of the circle. Create the diagonals in the same way that you drew the first lines. Make sure all points are coincident.

Then select the center of the circle, then the two blue diagonal lines and click on <img alt="" src=images/Constraint_PointOnObject.svg  style="width:24px;"> [Point on object](Sketcher_ConstrainPointOnObject.md), the circle must be centred at the intersection of the diagonals, that is at the center of the face. The sketch must be green, completely constrained (it is essential). Note that besides the radius of the circle, it is no longer necessary to create dimensional constraints.

Please note that in addition to switching the the toolbar to construction mode, the <img alt="" src=images/Sketcher_AlterConstruction.svg  style="width:24px;"> [Construction Mode](Sketcher_ToggleConstruction.md) button can also switch individual Sketcher elements to construction mode if they have been selected. If you accidentally switch an element to construction mode, you may get an error when you exit the sketch.

![](images/GGTuto1_8.PNG )

Leave the sketch, we see that the circle is well centred. (The pocket feature was not deleted, but modified). If you change the dimensions of the part again, the thickness or the length, the circle will remain centered on the face.

**Avoid construction lines:**

It is often possible to avoid creating construction lines. You can edit the sketch again, erase the construction lines and use a <img alt="" src=images/Constraint_Symmetric.svg  style="width:24px;"> [Symmetric constraint](Sketcher_ConstrainSymmetric.md) between the two opposite vertices of the external geometry lines and the centre of the circle (select points in this order):

![](images/GGTuto1_12.PNG )

We get exactly the same result for the position of the hole. In fact, thanks to the constraints available in the Sketcher workbench, there are many possible methods. This example shows that it is often better to choose the simplest method, thus limiting the number of objects created as well as the errors that might result.

**Second method using a datum plane.**

Here is another, faster method that is possible since version 0.17: the use of a datum plane and its attachment.

Start by erasing the \"Pocket\" function as well as the sketch of the hole. Select the top face and click <img alt="" src=images/PartDesign_Point.svg  style="width:24px;"> [Datum point](PartDesign_Point.md): create a datum point in the active body. The attachment mode chosen must be \"Center of mass\".

As the face is rectangular, its center of mass corresponds to the center of its diagonals. Validate, and a datum point is created.

Select the top face again and while holding down the CTRL key, select the point you just created in the Model tree, release CTRL and click <img alt="" src=images/PartDesign_Plane.svg  style="width:24px;"> [Datum plane](PartDesign_Plane.md). A reference plane is created with the origin of the point. Click OK.

It is now very easy to center the circle! Select from the Model tree or in the 3D view the plane you created, and click on <img alt="" src=images/Sketcher_NewSketch.svg  style="width:24px;"> [Create a sketch](Sketcher_NewSketch.md), a sketch is created with as origin, the origin of the plane. Then just trace the 5 mm radius circle on this origin, then validate (the sketch must be green imperatively).

You get with \"Pocket\", as created previously, the hole and it will always be centered.

![](images/GGTuto1_9.PNG )

This tutorial is completed, save this file, you can have fun exploring various features. Change other dimensions, make other shapes, put other holes on other faces, it is when making mistakes that we progress!

You can also continue with this other tutorial of a slightly more complicated part:

[Basic Part Design Tutorial](Basic_Part_Design_Tutorial.md)


 {{PartDesign Tools navi}} {{Sketcher Tools navi}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Tutorials](Category_Tutorials.md) > [PartDesign](Category_PartDesign.md) > [Sketcher](Category_Sketcher.md) > Creating a simple part with PartDesign/en
