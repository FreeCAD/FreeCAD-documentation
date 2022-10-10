---
- TutorialInfo   *   Topic   *Modeling
   Level   *Beginner
   Author   *heda
   Time   *2 hours
   FCVersion   *0.19 or above
   Files   *
   SeeAlso   *[Creating a simple part with PartDesign](Creating_a_simple_part_with_PartDesign.md), [Creating a simple part with Draft and Part WB](Creating_a_simple_part_with_Draft_and_Part_WB.md)
---

# Creating a simple part with Part WB/en





## Introduction

This tutorial aims to be used as a first introduction to 3D modeling using the [Part Workbench](Part_Workbench.md) ![](images/Switch_PartWorkbench.JPG ) of FreeCAD. After having finished this tutorial you should be able to make simple 3D models by using primitives like cubes, cylinders, etc with a technique called [Constructive Solid Geometry](https   *//en.wikipedia.org/wiki/Constructive_solid_geometry), short **CSG** modeling. Another way to create 3D models is by using a 2D shape by for example extruding or revolving the 2D shape in 3D space. For an introduction of that technique please follow the sister-tutorial *[Creating a simple part with PartDesign](Creating_a_simple_part_with_PartDesign.md)*. The two tutorials intentionally have exactly the same model generated, this presents the beginner with a hands on experience of the two different techniques and how they are implemented in FreeCAD. The definition of the two techniques can be viewed as strictly divided from a semantic point of view, however there is nothing directly hindering a mix of the techniques when creating models. There are some caveats to watch out for when mixing modeling techniques, those are mainly related to aspects of how FreeCAD is programmed. There is a [third tutorial](Creating_a_simple_part_with_Draft_and_Part_WB.md) intended as a first introduction to a mixed modeling example. That tutorial uses the **Draft Workbench** to create a 2D profile utilized to extrude a solid in the **Part Workbench** to make the same model as in this tutorial.

Before you start please have a look at how to **[navigate](Mouse_navigation.md)** in 3D space. When hoovering over the mouse model selector in the lower right corner of the FreeCAD window, a cheat-sheet of the current mouse model appears as in the picture below.

![](images/T101pwb00-01_navi.png )

Many newcomers to CAD programs get stuck while learning the software, if that happens to you, please go ahead and search the wiki or forum for further information -- chances are that others also have been stuck on the same specific thing in the past so there is already an answer to your specific question. Or make a post on the forum with your questions or findings. The forum has several threads where users are helped to complete all sorts of different tasks, those threads are often similar to tutorials, and often have specific illustrations included.

### The tutorial covers 

-   The model to make
-   Using the Part Workbench to create and manipulate the primitive building blocks
-   Changing the color and transparency
-   A different way to locate the hole
-   Making the hole a countersunk hole
-   Making a hollow piece
-   A different way to position the chamfer
-   Editing dimensions
-   Organizing the tree a bit differently
-   Wrapping up

## The model to make 

<img alt="" src=images/GGTuto1_Vue.PNG  style="width   *372px;">

![](images/T101pwb01-02_dims.png )

## Using the Part Workbench to create and manipulate the primitive building blocks 

Create a new document and save it directly under a new name, it is good practice to make sure that you save the document at regular intervals, or just before larger operations. Then switch to the **[Part Workbench](Part_Workbench.md)** using either the [workbench selector](Getting_started#Exploring_the_interface.md) (labeled 10 in the linked image) or by going to the **View → Workbench** menu. FreeCAD will start with toolbars at the top, the combo view to the left and the 3D view at the right.

### Create the main solid block 

Press <img alt="" src=images/Part_Box.svg  style="width   *24px;"> [Box](Part_Box.md) to make a default solid cube. The cube appears in the [3D view](3D_view.md) and also as a new object in the [Tree view](Tree_view.md) in the sidebar.

Press <img alt="" src=images/Std_ViewIsometric.svg  style="width   *24px;"> [Isometric](Std_ViewIsometric.md) to see the cube in 3D.

![](images/T101pwb01-03_cube1.png )

Select the cube in the [Tree view](Tree_view.md), it becomes green in the 3D view. Below the tree view you will now see that the cube by default is created with the dimensions **Length x Width x Height** as *10 x 10 x 10 mm*. Change those dimensions to **100 x 30 x 50** as per the initial drawing of the model.

![](images/T101pwb01-04_cubedims.png )

When changing a property, like *Length* through the spinbox, one can either enter the values, or use the scroll-wheel to tick values up or down. The arrows for ticking values up or down can of course also be used. In the right most picture above, the *Height* property is in edit mode, rolling the scroll wheel when the mouse is over that cell will change the value by one up or down.

Click <img alt="" src=images/Std_ViewFitAll.svg  style="width   *24px;"> **[Fit all](Std_ViewFitAll.md)** to see the whole cube.

![](images/T101pwb01-05_cube2.png )

### Create the fillet 

To make the filleted corner, in the toolbar press <img alt="" src=images/Part_Fillet.svg  style="width   *24px;"> **[Fillet](Part_Fillet.md)** which opens the *task panel* for fillets in the [combo view](Combo_view.md) to the side. Change the *radius* spinbox to 20 mm, then in the 3D view, select the width edge to the upper right and click **OK**.

![](images/T101pwb01-06_filletrad.png )

The *task panel* closes and you are back to the Tree view which now has a fillet object instead of the earlier cube.

### Visibility of children 

Click the plus sign/caret to expand the children of the fillet, which in this case is the *cube* we created earlier, but it is grayed out. Select the cube and press the space bar -- this toggles visibility so the cube is now visible again and the icon is no longer grayed out. To deselect the cube click in a blank area in the Tree view or the 3D view.

![](images/T101pwb01-07_fillet.png )

### Create the chamfer 

Next is to create the 30 degree *chamfer*, start by toggling the visibility of the child cube of the fillet. There is a chamfer tool in [Part Workbench](Part_Workbench.md), but instead of using it we will make the chamfer with another block and a boolean cut.

Create a new <img alt="" src=images/Part_Box.svg  style="width   *24px;"> **[Box](Part_Box.md)** with dimensions 60 x 30 x 30. Change the **placement angle** to -30 degrees.

![](images/T101pwb01-08_chamfer1.png )

The placement angle is using the **placement vector** (Axis) as axis of rotation. The default is the z-axis, which is not matching our target direction, changing the placement vector to the **y-axis** produces the desired orientation of the cutting tool for the chamfer.

![](images/T101pwb01-09_chamfer2.png )

The same placement can be attained with other values as well, the simplest alternative example of a placement that is the same is an angle of +30 degrees and a y-axis of -1.

#### Python console 

Furthermore the position needs to be adjusted, looking at the drawing of the finished part, there is no direct dimension to use for the intended translation upwards. Since the upward dimension is the one needed, we have to calculate it. Let's make use of the built in **[Python console](Python_console.md)** for those calculations, it is basic trigonometry. If the FreeCAD Python console is not visible for you, just right-click in an empty space in the toolbar area and check the *Python console* and it should appear in the workspace, when there you should as well add the **[report view](Report_view.md)** if not already visible. The *report view* most of the times provides useful information or even hints of what to do next for different commands.

![](images/T101pwb01-10_pyconsole.png )

After importing the **[math](https   *//docs.python.org/3/library/math.html#module-math)** module from the standard libraries in python we can use the formula *(50 - math.tan(math.radians(30)) \* 50)* to find the distance in z-direction that the block should be moved. Copy the result of the formula from the Python console and paste it into the z position for **Cube001**. The *tool* to use for the chamfer *cut* is now properly oriented and positioned.

![](images/T101pwb01-11_chamfer3.png )

#### Expressions

One does not have to use the Python console to do the calculation, In most cases when dealing with numeric parametric values, FreeCAD has a short-cut to a built-in calculator. It is called **[Expressions](Expressions.md)** in FreeCAD, you can enter the *expression mode* by first clicking in the spinbox for the z-position, a small blueish circular icon will appear at the right side.

![](images/T101pwb01-12_expression1.png )

Clicking that icon opens new window *Formula editor* where formulas and expressions can be entered as shown below. Using expressions is a powerful tool, since one can access parameters from the model, effectively making all parameters in the model available as variables to be used when creating an expression. In short, in our formula, instead of entering the number 50 when in the formula editor, we could enter a *named parameter* holding the value 50 from the cube, with the benefit that if we change the cube *height*, the position of the chamfer will automatically follow. The value of 50 in the current model is referred to as *Cube.Length*, i.e. the *Length* property of the *Cube* feature. Further information on this can be found on the wiki.

![](images/T101pwb01-13_expression2.png )

To make the cut, with the **Ctrl** key pressed down first select the **Fillet** in the Tree view and then the latest created cube (named **Cube001**) and finally in the toolbar press the <img alt="" src=images/Part_Cut.svg  style="width   *24px;"> **[Cut](Part_Cut.md)** button. Your Tree view should now again be a single object in the root called **Cut**.

![](images/T101pwb01-14_model1.png )

#### The toolbars 

A sidenote on the toolbars, since they are the typical avenue to invoke commands. Although there is a basic setting for the layout of the toolbars, the actual layout on your computer could turn out to be less than ideal. In such cases it is easy to adjust. Consider the upper section of the below image. There are two rows of toolbars and only a limited number of the [Part Workbench](Part_Workbench.md) toolbar buttons are visible. The simplest way to see more toolbar buttons is to maximize the FreeCAD window, unless it already is maximized of course.

More common is to adjust the layout of the toolbars to suit your needs and your specific computer. The repositioning is done with the handle on the left of each toolbar. You can just click and drag the handle to a new location. In the lower section of the below image the toolbar positions have been adjusted, revealing their full content. Changes to toolbar positions are persistent through sessions.

![](images/T101pwb01-141_toolbars.png )

#### The measurement tool 

The **[measurement tool](Part_Workbench#Measure.md)** in the **Part Workbench** can be used to check that our calculation and placement of the chamfer is correct. Press the <img alt="" src=images/Part_Measure_Linear.svg  style="width   *24px;"> **[Measure Linear](Part_Measure_Linear.md)** button and a *task panel* opens up, then select the 2 endpoints of one side of the chamfer.

![](images/T101pwb01-15_model1measure1.png )

It checks out with an x dimension of 50 mm, clear the measurement and close the dialogue.

### Create the hole 

To make the hole, press the <img alt="" src=images/Part_Cylinder.svg  style="width   *24px;"> **[Cylinder](Part_Cylinder.md)** button, set the *radius* to 5 mm and *height* to 50 mm.

![](images/T101pwb01-16_cyl1.png )

Next we need to position the hole according to the dimensions in the drawing. Change the view to <img alt="" src=images/Std_ViewTop.svg  style="width   *24px;"> **[Top](Std_ViewTop.md)** view, then right-click the **Cylinder** in the Tree view and select **Transform** from the pop-up menu.

![](images/T101pwb01-17_cyl1translate.png )

Change the *Translation increment* to 5 and use the red and green arrow to position the cylinder in the right position, moving it 15 mm in y and 65 in x by dragging the arrow ends with the mouse. Click **OK** to close the *Transform* dialogue. To make the hole press the **Ctrl** key and select the **Cut** and **Cylinder** in the Tree view, then press the <img alt="" src=images/Part_Cut.svg  style="width   *24px;"> **[Cut](Part_Cut.md)** button in the toolbar. Your Tree view should once again have a single object in the root called **Cut001**.

Congratulations, the model is now ready.

![](images/T101pwb01-18_model1complete.png )

With the basic model ready, let us explore different ways to alter this model, some examples are related to the appearance, additional features, or simply a different way to do the same.

## Changing the color and transparency 

There are several different ways one can change the appearance of objects, for this case, let\'s use the view tab in the property part of the combo view. First select the object in the Tree view and then edit any property like line color, shape color or transparency via the **view tab** (found at the bottom of the *combo view*).

![](images/T101pwb02-01_appearance1.png )

Unfortunately when the object is selected it is a bit hard to see how it will look when tuning the new appearance. To see the final result one has to deselect the object. Here is the new look of the model, where one now can see the through hole also in the iso-view. Another way to edit the appearance is via the **View → ![](images/)_Appearance...** menu.

![](images/T101pwb02-02_appearance2.png )

## A different way to locate the hole 

Do a *save-as* under a new name. Then delete the cut that added the hole and move the cylinder back to zero position. Your model should look like the below picture, which is the starting point for using a different technique to locate the hole at the center of the upper face. Note that the color is back to the default gray, the change in appearance we did was on the cut object which now is deleted.

![](images/T101pwb03-01_cyl.png )

This time the <img alt="" src=images/Workbench_Draft.svg  style="width   *24px;"> **[Draft Workbench](Draft_Workbench.md)** will be used to locate the hole. The hole is as before to be located at the center of the upper face, which is the same as the midpoint of the diagonal of the upper face.

Start by switching the workbench to **Draft**, it might be that a *grid* appears in the 3D view, the grid visibility can be toggled with <img alt="" src=images/Draft_ToggleGrid.svg  style="width   *24px;"> [Toggle Grid](Draft_ToggleGrid.md) in the toolbar. When making use of the **[snap](Draft_Snap.md)** functionality in the **Draft Workbench** it helps to only have the *snap types* of interest enabled. This time it is sufficient to leave *endpoint, midpoint and circle center enabled*, so the settings for snapping should look something like below.

![](images/T101pwb03-02_snap.png )

Finding the point to place the center of the cylinder could be done by making a diagonal as helpline and use the center of the cylinder and midpoint of the diagonal to identify the points to move between, however it turns out that we do not even need to make any helplines, we can snap on already existing solid geometry.

Select the **Cylinder** in the Tree view (it turns green in the 3D view) and press the <img alt="" src=images/Draft_Move.svg  style="width   *24px;"> **[Move](Draft_Move.md)** button in the toolbar. A *task panel* opens for moving objects, make sure that *Copy* is unchecked.

![](images/T101pwb03-03_move.png )

Then move the mouse to the upper face of the cylinder so that you see a *white dot* in the center of the circle as per the left picture below, this together with the center symbol next to the mouse pointer means that a left button mouse click will snap to the white point.

![](images/T101pwb03-04_snapselect.png )

When you have the white dot on the upper face, click the left mouse button, and repeat for the upper square face of the main solid, like the right picture above, and confirm the choice with a left mouse button click. The snap function makes use of *mass-center* for any type of face, and in this case the mass center is the same as the geometrical center that is sought after. You will by now have noticed that the move of the cylinder is animated, so you always see what is about to happen.

Repeating the step of the **boolean cut** from earlier once again will make the through hole that completes the model. Using the **linear measurement tool** in the Part Workbench, a check that the hole is correctly placed is done. The measurement can only be done between *points*, so the measurement is done from main body zero to the seam point of the cylinder, meaning that the correct distance is 70 mm instead of the 65 that is on the drawing to account for the extra radius that is included in the distance.

![](images/T101pwb03-05_modelmeasure.png )

## Making the hole a countersunk hole 

Switch back to the [Part Workbench](Part_Workbench.md) and create a *cone* by pressing the <img alt="" src=images/Part_Cone.svg  style="width   *24px;"> **[Cone](Part_Cone.md)** button in the toolbar. Change *radius1* to 0 mm and *radius2* to 7 mm -- this will give a 2 mm *countersink* on the radius. Making the *height* of the cone 7 mm results in a 90 degree top angle of the cone, or 45 degree countersink angle. Worth to note is that again one could as well use the <img alt="" src=images/Part_Chamfer.svg  style="width   *24px;"> [Chamfer](Part_Chamfer.md) operation.

When working with FreeCAD you will continuously be faced with several different ways to achieve seemingly the same result. There is hardly any absolute truth in what is the right way to achieve a particular end result -- however when looking in a specific context one specific workflow can be more flexible, allow for later features to actually be used etc. How you build 3D models will evolve over time as you along the way learn more and more about the features and capabilities of FreeCAD.

![](images/T101pwb04-01_cone.png )

Translate the cone so that it is *concentric* with the hole and *coplanar* with the main solid upper surface. Use any method described earlier in this tutorial to accomplish that.

In the picture below the move is made with *Transform* and an *increment* setting of 1 mm, since the cone has a characteristic dimension of 7 mm, meaning that the earlier increment setting of 5 mm will not allow for correct positioning. The <img alt="" src=images/Std_DrawStyleWireFrame.svg  style="width   *24px;"> **[Wireframe](Std_DrawStyle#Wireframe.md)** rendering is used to easier see that the cone is in the right position.

![](images/T101pwb04-02_conetranslate.png )

To complete the model, let\'s make use of the <img alt="" src=images/Part_Boolean.svg  style="width   *24px;"> **[Boolean](Part_Boolean.md)** command instead of first selecting objects and apply a specific boolean operation. Press the toolbar button and a *task panel* opens as per the below picture to the left.

![](images/T101pwb04-03_boolean.png )

Three items needs to be specified, the *operation type*, the *first shape* and the *second shape*. The cone is supposed to be cut, this is called *Difference* in this command, instead of *Cut*. The first shape is our **Cut001**, it is listed under *compounds*, since it is build from several solids. The second shape is the **Cone**. Once the correct settings are made for the command, click the **Apply** button to execute the operation. This has all been done in the picture to the right, and there one can also see that a *compound* **Cut002** is now listed, this is our final model shape. After having changed the appearance the final model looks like this.

![](images/T101pwb04-04_modelcomplete.png )

## Making a hollow piece 

Do a *save-as* under a new name. FreeCAD has all of the typical operations of a 3D modeller, one of them is <img alt="" src=images/Part_Thickness.svg  style="width   *24px;"> **[Thickness](Part_Thickness.md)**, which is used to *hollow out* parts.

Rotate the view so that the bottom face of the model is visible.

![](images/T101pwb05-01_frombottom.png )

Select the *bottom face* of the model, then in the [Part Workbench](Part_Workbench.md) select <img alt="" src=images/Part_Thickness.svg  style="width   *24px;"> **[Thickness](Part_Thickness.md)** and the screen should look like below.

![](images/T101pwb05-02_thickness_cmd.png )

Click **OK**, as you can see there is now a *radius* on the hollowed out part.

![](images/T101pwb05-03_thickness_dimension.png )

Moreover, when taking a measurement of the width of the part, it is now 32 mm, so the *thickness* has been applied *outwards*. Let's edit that, double-click the model in the Tree view and modify the *join-type* settings to *intersection* and the *thickness* setting to -1.

![](images/T101pwb05-04_thickness_modify.png )

Now the outer width of the part is 30 mm, same as before and the corners are all sharp corners.

![](images/T101pwb05-05_thickness_modified.png )

## A different way to position the chamfer 

Do a *save-as* under a new name. Then delete features so that the model looks like below.

![](images/T101pwb06-01_startingpoint.png )

Make a **Cube** with dimensions **30x30x60**, ending up like below.

![](images/T101pwb06-02_with_cube.png )

Change the **placement** by first rotating -120 degrees around the Y-axis.

![](images/T101pwb06-03_rotated_cube.png )

Finally, change the position to **X=50** and **Z=50** and make the *cut* to produce the same result as earlier.

![](images/T101pwb06-04_cube_cut.png )

This once again highlights that there are always several ways to produce the same outcome, which is a recurring theme when it comes to 3D modeling. When it comes to basic geometries or solids, one can use different workbenches in FreeCAD as well as different commands and still have the same outer shape of a solid. You simply need to find your own way to a set of preferred tools and workflow that you are comfortable in using. Modeling in parametric 3D is a process of constant learning, and takes practice to master.

## Editing dimensions, face colors and TNP 

FreeCAD is a parametric 3D modeler, this allows you to change any *placement* or *dimension* and the model will update accordingly. In general this works, but it is possible to break a model when edited -- for example when a fillet is based on an edge that no longer exists due to editing. When a model breaks during editing, it is referred to as **TNP, [Topological Naming Problem](Topological_naming_problem.md)**.

Go ahead and experiment with changing dimensions and placements to see if you can break the model, do not forget to recalculate the model after changes if required. This can be done with the <img alt="" src=images/Std_Refresh.svg  style="width   *24px;"> [Refresh](Std_Refresh.md) button in the toolbar, if the icon is grayed out it is not needed to refresh the object.

### Reposition the cylinder 

Here is an example of the cylinder moved from the center to one side of the main body by using *Transform* on the cylinder. As can be seen in the picture, the cone is still in the original position, not affected by the move of the cylinder.

![](images/T101pwb07-01_cylindermoved.png )

When you move the cylinder and break through the outer surface, in version 0.19 you are loosing part of the color settings on your model. FreeCAD reverts to the user default settings for shape colors and transparency in the 3D view, however the **Cut002** shape still shows the colors and transparency that it had before as seen in below picture.

### Fixing the colors 

![](images/T101pwb07-02_wrongcolor.png )

Here is one way to get it back. First change *transparency* one tick up or down and then back, that brings back the transparency. You can do the same trick on *shape color*. Another way to get the color back is to *right-click* **Cut002** in the Tree view and select **Set Colors** in the context menu. In the *task panel* that displays, click **Set to Default**, that brings back the color to the one set in the view-properties.

![](images/T101pwb07-03_set_colors.png )

The **Set Colors** command allows you to select individual faces of a shape and set a unique color on the selected faces.

### Multiple solids 

Another example where the cube that is making the chamfer has been translated and rotated.

![](images/T101pwb07-04_3solids.png )

As can be seen when repositioning the chamfer in this way, the end result is *3 disjoint solids*. [Part Workbench](Part_Workbench.md) allows this, [PartDesign Workbench](PartDesign_Workbench.md) does not, either you will get an *multiple solids error* or it will simply not render all solids.

### TNP

Going back to the original completed model, let's explore how the faces are named.

Here the **[selection view](Selection_view.md)** has been made active, just to show clearly what is selected and not, also coloring is adjusted so that the selection is easier to see.

![](images/T101pwb07-05_face2and9.png )

Selecting one side face and the cylinder inner face gives that they are internally called face *2* and *9*, where face *2* is the side face. Face numbering can be different for you.

Moving the cylinder so that the cavity ends up on the side face, and doing the selection of faces now gives a different number for the cylindrical face.

![](images/T101pwb07-06_newfacenumbers.png )

Face 2 is the right side of the original face 2, the left side of former face 2 is now face 8. The cylindrical part was face 9, but is now face 7. FreeCAD reassigns the numbering and the order is not necessarily preserved. The total face count in the first model is 10, in the version with the cylindrical face piercing the side face, the total face count is 11. So obviously face numbering has to change when the so called *topology* changes. This probably feels like a minute detail, but turns out to be quite important in parametric 3D CAD. Imagine that you have used the cylindrical face as reference for another feature, it used to be called face 9, but is now called face 8. The reference to the intended cylindrical surface is lost. Since FreeCAD, at least in currently released versions does not keep track of the *intended face*, it only keeps track of the *numbered face*, a model breaks when a reference is made to a face that later is renumbered. This is called **TNP, [Topological Naming Problem](Topological_naming_problem.md)**.

You are encouraged to learn how to avoid broken models due to TNP, further reading can be done [elsewhere on the wiki](Topological_naming_problem.md), which largely focuses on a *sketch driven* workflow, the underlying mechanism is the same though. The renumbering described here for faces goes for all geometrical entities, faces, edges and vertexes.

## Organizing the tree a bit differently 

Do a *save-as* under a new name. Then delete all the cuts ending up with a model looking like below.

![](images/T101pwb08-01_primitives.png )

When using the **Part Workbench** and modelling feature rich solids, the tree structure of a solid can become hard to decipher. So far we have created one primitive / feature and applied a boolean operation. In the Part Workbench one can bundle primitives into one boolean operation. In our case we have the cylinder, cone and cube that are all a cut boolean operation.

Instead of making a cut for each primitive, we can first apply a boolean union, <img alt="" src=images/Part_Fuse.svg  style="width   *24px;"> **[Fuse](Part_Fuse.md)** the primitives intended for the boolean cut, and then make the *cut* between the **Fillet** and the **Fusion**.

Using this approach, the Tree view ends up looking like below, which is just a different way of building the same model. Compare this with the original Tree view, none is better than the other, however when making more complex models, one approach over the other can have benefits in ease of modifying/reorganizing the model if needed.

![](images/T101pwb08-02_fused.png )

## Wrapping up 

Having gone through the tutorial you are now briefly acquainted with the user interface of FreeCAD and you have learned the basics in using the **Part Workbench**. You should now be able to build simple models after your own liking. The **Part Workbench** is one of the workbenches that can be used to create solids, the **PartDesign Workbench** is another. The different workbenches have different capabilities and workflows. Learning FreeCAD in full, especially considering all add-ons and macros takes years, so keep on exploring new and different ways of making models -- take different tutorials on the wiki, the learning never stops when working with FreeCAD. It is suggested that you learn *sketches* and the **PartDesign Workbench** next if your focus is on creating solids. If your focus is modelling buildings your next learning should be the **Draft** and **Arch** workbenches.

At last, FreeCAD is made by volunteers in their spare time. If you want to further advance FreeCAD's capabilities, consider [contributing](Help_FreeCAD.md) to FreeCAD, for example by improving the documentation.

[Category   *Part](Category_Part.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Part](Category_Part.md) > Creating a simple part with Part WB/en
