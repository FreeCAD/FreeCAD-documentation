# <img alt="" src=images/BIM_tutorial_screenshot.png  style="width:1024px;"> BIM ingame tutorial/it


{{BIMTutorialAction|descr=This is the in-game tutorial of the [BIM Workbench](BIM_Workbench.md). It is not meant to be read here on the wiki, but rather to be started from inside FreeCAD, in the BIM workbench, under menu '''Help → BIM tutorial'''. It includes a series of steps to be completed by the user. Each step is terminated by an instance of the [<nowiki>{{BIMTutorialAction|descr|goal1|test1|goal2|test2}}</nowiki>](Template_BIMTutorialAction.md) template, which informs of the condition that need to be met. Images should be 300px wide. No SVG images should be used on this page, as they are not supported by the QTextBrowser widget}}



### Benvenuti nell\'ambiente BIM! 

<img alt="" src=images/BIM_Tutorial_title.jpg  style="width:300px;">

This tutorial will walk you through the different functionalities of the [BIM Workbench](BIM_Workbench.md) and help you to get on track by modeling a very simple pavilion building. It should take between one and two hours to complete entirely, depending on your previous experience with 3D applications.

You can pause the tutorial at any time and resume it later by selecting **Help → BIM Tutorial** again.

Some steps of this tutorial require you to take actions. Those will be indicated below this text box, with an icon showing if the task has been completed or not. But since we are good people here at FreeCAD, it is not mandatory to complete the actions in order to advance through these pages. You can just browse through the tutorial and skip actions at your convenience.

#### About FreeCAD versions 

This tutorial is written for the [most recent development version of FreeCAD available](Download.md) (currently 1.1.0dev). The BIM workbench, however, is made to be compatible with any version of FreeCAD. If you are using a FreeCAD version older than the one indicated here, some BIM tools might look different, work differently or even be unavailable. Refer to the [documentation](BIM_Workbench.md) to know more in case of doubt.

#### Note

This tutorial is still being written, and is therefore **incomplete**! If you have suggestions or things you find unclear, why not help us to make it better on the [FreeCAD forum](https://forum.freecad.org/viewforum.php?f=23)!


{{BIMTutorialAction|descr=No action to perform for this step}}

### Set FreeCAD up 

FreeCAD has a large preferences system with many options to set, located under menu **Edit → Preferences**. Each additional workbench can add more preferences pages, which makes it very complex.

The BIM workbench provides a [simplified setup window](BIM_Setup.md), which allows to quickly set some of the most useful preferences for BIM work. The BIM preferences window is located under menu **Manage → BIM Setup** (you can also click the corresponding button on the Manage toolbar):

<img alt="" src=images/BIM_Tutorial_01.jpg  style="width:300px;">

Open the simplified BIM preferences screen now, and set the different options to your liking.

In case of need, hover the mouse over any option or setting to see a description of what it is used for:

<img alt="" src=images/BIM_Tutorial_02.jpg  style="width:300px;">

In this tutorial, we will work in centimeters. Therefore, we recommend that you set your preferred working units to **centimeters** and the default size of a grid square to **10 cm**. These settings can be changed at any time from the working plane button located on the main toolbar, and the units indicator located on the status bar (bottom right):

<img alt="" src=images/BIM_tutorial_14.jpg  style="width:300px;">


{{BIMTutorialAction|goal1=Open the BIM setup screen|test1=True if hasattr(FreeCADGui,"BIMSetupDialog") else False|goal2=Set preferred working units to centimeters and the default size of a grid square to 10 cm|test2=True if ((FreeCAD.ParamGet("User parameter:BaseApp/Preferences/Units").GetInt("UserSchema",0) == 4) and (FreeCAD.ParamGet("User parameter:BaseApp/Preferences/Mod/Draft").GetString("gridSpacing") == '10.00 cm')) else False}}

### Create a new document 

If you just installed FreeCAD, you are probably currently looking at the **FreeCAD Start Page**:

<img alt="" src=images/BIM_tutorial_13.jpg  style="width:300px;">

The start page lists the latest documents you have been working with, and, on its different tabs, explains how to get help. But in order to start working, we need to create a new, empty **document**. If you haven\'t done it yet, create now a new document by using the \"Create new\...\" item of the start page, or by navigating to menu **File → New**:

<img alt="" src=images/BIM_tutorial_09.jpg  style="width:300px;">

You will then find yourself in the 3D space of FreeCAD, ready to work:

<img alt="" src=images/BIM_tutorial_10.jpg  style="width:300px;">


{{BIMTutorialAction|goal1=Create a new document|test1=True if FreeCAD.ActiveDocument else False}}

### Navigating in the 3D view 

There are several ways to interact with the mouse in FreeCAD. These are called [navigation styles](Mouse_navigation.md). You can change the current navigation style anytime by clicking on the navigation style button in the status bar. Hovering the mouse over that button will also show you what each mouse button does. Several of them are made to match other well-known applications. Choose one you are comfortable with.

<img alt="" src=images/BIM_Tutorial_03.jpg  style="width:300px;">

Controlling how you look at your model in the 3D view can be done in multiple ways: Using the **mouse** (depending on the navigation style you chose), the **keyboard** (explore the contents of the **View** menu to find out more), or the [Navigation Cube](Navigation_Cube.md) (click the different arrows and faces of the cube to align the view).

<img alt="" src=images/BIM_Tutorial_04.jpg  style="width:300px;">


{{BIMTutorialAction|goal1=Choose a navigation style|test1=True|goal2=Set yourself in Top view|test2=True if FreeCADGui.ActiveDocument.ActiveView.getViewDirection().getAngle(FreeCAD.Vector(0,0,-1)) < 0.01 else False}}

### Reorganize the interface 

All panels and toolbars in FreeCAD can be moved and reorganized. Larger panels can also be joined by dragging and dropping them on another one. If your screen is too small to display all the toolbars and their contents (truncated toolbars will appear with a \>\> sign), it might be a good idea to move them to a better position.

<img alt="" src=images/BIM_Tutorial_05.jpg  style="width:300px;">

Toolbars and panels can also be turned on and off from the **View** menu.

The BIM workbench also features switch buttons in the status bar, that turns additional panels like selection view, report view and python console on and off. These panels are often useful while working with FreeCAD, but they use precious screen space. You can usually turn everything off until you need them. Remember that error messages are printed in the report window, so in case anything goes wrong, be sure to have a look there.

<img alt="" src=images/BIM_tutorial_17.jpg  style="width:300px;">


{{BIMTutorialAction|descr=No action to perform for this step}}

### The BIM workbench tools 

The [BIM Workbench](BIM_Workbench.md) contains tools borrowed from other workbenches such as [Draft](Draft_Workbench.md) or [Part](Part_Workbench.md), as well as its own tools. These are organized in several categories. Each category has a menu and a toolbar. Take a moment to explore the contents of the menus described below.

#### 2D Drafting 

These tools allow you to draw flat objects, such as lines, polylines, rectangles, arcs, etc\... that will become the bases of your BIM objects. For example, you can use a polyline to define the base trace of a wall, or a rectangle as a profile for a beam. All 2D objects are created in the current [working plane](Draft_SelectPlane.md).

<img alt="" src=images/BIM_Tutorial_35.jpg  style="width:300px;">

#### 3D/BIM

This category contains tools to create BIM objects such as [walls](Arch_Wall.md) or [windows](Arch_Window.md), and generic, non-BIM 3D objects such as [boxes](BIM_Box.md), that you can turn into BIM objects later on. The result is different if you use the tool with an object selected or not. If not, you will be presented with a creation interface. If you have selected an object before running the tool, an object of the corresponding type will be created using the selected object as a base.

<img alt="" src=images/BIM_Tutorial_33.jpg  style="width:300px;">

A typical example is to press the [wall](Arch_Wall.md) button with a selected [line](Draft_Line.md) or [polyline](Draft_Wire.md). A wall will be created automatically, using the line or polyline as its baseline.

Non-BIM objects, including objects made in other workbenches, can be turned into BIM objects anytime, by selecting them and pressing any of the BIM tool buttons.

#### Annotation

These tools produce annotative objects such as dimensions, texts, labels or grids, that are not used for modeling but to annotate your models and produce understandable drawings.

<img alt="" src=images/BIM_Tutorial_34.jpg  style="width:300px;">

#### Snapping

These tools turn [snapping](Draft_Snap.md) positions on/off. Like in most BIM applications, each additional snapping position adds calculation time when drawing, so it is best to only keep the ones you need turned on.

#### Modify

These tools modify existing objects. They contain usual transformation tools such as Move or Rotate, plus a series of others that only work for specific object types.

#### Manage

This category contains general management tools. Most of them allow you to edit BIM properties of a large group of objects simultaneously, without the need to select them.

Each tool contained in these menus has its own documentation page that describes in detail how it works and what options are available. They are listed on the [BIM Workbench documentation](BIM_Workbench.md) page, which is also accessible from the **Help** menu, or by using menu **Help → What\'s this?** and clicking on any toolbar button.


{{BIMTutorialAction|descr=No action to perform for this step}}

### Prepare your working space 

There are many ways to create BIM objects in FreeCAD. You can use the native [BIM tools](BIM_Workbench.md) from this workbench, or use any other FreeCAD tool from other [workbenches](Workbenches.md). Both the *2D Drafting* and the *3D/BIM* tools from this workbench, unlike other workbenches such as Part Design, make extensive use of **working planes** and **snapping**.

The [working plane](Draft_SelectPlane.md) is where your next objects will be created. You can set it to one of the basic orthogonal planes (ground, front, side), or use any selected face to define the current working plane. You can also use [Working Plane Proxies](Draft_WorkingPlaneProxy.md) from menu **Utils** to store a specific working plane position inside your model. [Building Parts](Arch_BuildingPart.md) also contain an implicit working plane position. Changing the current working plane is done by pressing the working plane button on the BIM toolbar. The **grid** always reflects where the working plane is.

As you will have noticed, view angle and working plane are not tied together. You can work on your working plane from any view angle.

Set the working plane in \"Top\" mode now:

<img alt="" src=images/BIM_Tutorial_06.jpg  style="width:300px;">

The [snapping tools](Draft_Snap.md) allow you to place new objects and points precisely according to existing geometry. However, enabling many snapping locations might slow down the drawing operations, so it is wise to only enable the snapping tools you intent to use. Take a moment to review what each of them does, so when needed you will know which can be disabled.

<img alt="" src=images/BIM_Tutorial_07.jpg  style="width:300px;">

Take special notice of the last one, the **working plane snapping** tool, as it will force any snapped point to lie on the working plane, thus preventing you to snap above or under the working plane. You will often need to turn it on or off, depending on the operation you are performing.


{{BIMTutorialAction|goal1=Set the working plane in "Top" (XY) mode|test1=True if ((FreeCAD.DraftWorkingPlane.axis.getAngle(FreeCAD.Vector(0,0,1)) < 0.01) and (FreeCAD.DraftWorkingPlane.weak == False)) else False|goal2=Review the different snapping tools|test2=True}}

### Draw a first wall 

Let\'s start building our pavilion by creating some walls. Walls can be made either directly with the [wall](Arch_Wall.md) tool, or by first drawing 2D objects such as [lines](Draft_Line.md), [wires](Draft_Wire.md) (polylines) or [sketches](Sketcher_NewSketch.md), that will define the baseline of our walls. When you have such a baseline object selected, pressing the Wall tool will automatically convert it into a wall.

First, zoom out until a good part or all of the grid is seen. This will make it much easier to see what we are doing:

<img alt="" src=images/BIM_tutorial_15.jpg  style="width:300px;">

Then, press the <img alt="" src=images/Arch_Wall.png  style="width:16px;"> **Wall** button from the toolbar (or choose menu item **3D/BIM → Wall**). Click two points on the grid, vertically aligned, distant by **300 cm**. Pressing SHIFT after the first point has been clicked will help you to keep your wall horizontal or vertical. The side panel will inform you of the length of wall while drawing.

<img alt="" src=images/BIM_tutorial_16.jpg  style="width:300px;">

If you created a wrong wall, no worries! Simply delete it or undo it (menu **Edit → Undo**) and try again.


{{BIMTutorialAction|goal1=Create a wall|test1=bool(len([o for o in FreeCAD.ActiveDocument.Objects if "MakeBlocks" in o.PropertiesList]) == 1)}}

### Draw a second wall 

Make a second, horizontal wall of 4 meters (or 400 centimeters) long. Select the <img alt="" src=images/Arch_Wall.png  style="width:16px;"> **Wall** tool again, pan and zoom out until you see a good area of the grid, and pick two points from the grid to define the start and end points of the new wall:

<img alt="" src=images/BIM_tutorial_11.jpg  style="width:300px;">

After they are created, select both walls by pressing CTRL and clicking them both in the 3D view or in the [tree view](Document_structure.md), and adjust their **height** property to 2.5 meters and their **width** to 20 centimeters (or any other measurement you are comfortable with, if working in another unit), so they look like this (Use the mouse to rotate the view, according to the navigation style you choose):

<img alt="" src=images/BIM_tutorial_08.jpg  style="width:300px;">

You can always correct or change properties after a wall or any other BIM object has been created. By expanding the wall object in the tree view, then double-clicking the baseline of the wall, you can also modify its base 2D object. Most BIM objects in FreeCAD are based on another object, such as a baseline or a profile.

<img alt="" src=images/BIM_tutorial_12.jpg  style="width:300px;">

#### Important note 

You will notice that some property changes, in FreeCAD, don\'t reflect immediately on the object in the 3D view. Instead, the object is marked with a \"to be recomputed\" blue mark in the tree:

<img alt="" src=images/BIM_Tutorial_20.jpg  style="width:300px;">

The reason for this is that a FreeCAD document can be a very complex chain of inter-dependent objects. Updating one can trigger an update on many others, and therefore take a long time. To avoid this, some operations simply mark the object to be recomputed, and you trigger the recomputation yourself by using menu **Edit → Refresh** or pressing **Ctrl+R**.


{{BIMTutorialAction|goal1=Create two orthogonal wall objects|test1=bool(len([o for o in FreeCAD.ActiveDocument.Objects if "MakeBlocks" in o.PropertiesList]) == 2)|goal2=Set their height to 2.50 meters and width to 20 centimeters|test2=bool(len([o for o in FreeCAD.ActiveDocument.Objects if "MakeBlocks" in o.PropertiesList and o.Height.Value == 2500 and o.Width.Value == 200]) == 2)}}

### Don\'t forget to save the file regularly! 

Like any other computer application, FreeCAD is subject to failing or crashing, specially when we have little experience with it. Saving your file often is a very good habit to take in these early moments. FreeCAD also has an auto-saving mechanism, that you can set up under menu **Edit → Preferences → General → Document**.

Save your file now by using menu **File → Save**.


{{BIMTutorialAction|goal1=Save your file|test1=bool(FreeCAD.ActiveDocument.FileName)}}

### Draw a roof slab 

We will now place a roof slab on top of our walls. Instead of drawing the slab directly, like we did with the walls, we will here first draw a rectangle, then turn the rectangle into a slab. We will now explore two methods to do so, both are useful to know, so we suggest you to try one first, then undo it (or reload the file), and try the other method.

#### Method 1: Draw the slab on the ground, then move it into position 

It is often convenient to consider the top XY plane (the ground plane) as a kind of \"drawing board\", where we will be building our objects, and move then next to their correct position. There is an additional advantage here, our working plane is already in \"Top\" mode, so we don\'t need to change it.

Set yourself in top view, zoom out a bit until you see both walls, and draw a rectangle encompassing them both. Press the <img alt="" src=images/Draft_Rectangle.png  style="width:16px;"> **Rectangle** button from the toolbar (or choose menu item **2D Drafting → Rectangle**):

<img alt="" src=images/BIM_Tutorial_18.jpg  style="width:300px;">

Rotate your view to inspect the results. By default, the rectangle is filled with a face. This can be changed by changing the **Make Face** property of our rectangle to False. For the slab we are going to build, this has no impact, for other types of objects, however, the base object being a polyline or a face can make a difference.

<img alt="" src=images/BIM_Tutorial_19.jpg  style="width:300px;">

The next step is to build a slab by *extruding* it with our rectangle as its base *profile*. In FreeCAD, structural objects such as columns, beams, or slabs are all created using the same object called a **Structure**. After a structural object is created, setting its **IFC Type** property to the desired type (column, slab, etc\...) is all that is needed to change its type.

Make sure our rectangle is selected, then press the <img alt="" src=images/BIM_Slab.png  style="width:16px;"> **Slab** button from the toolbar (or choose menu item **3D/BIM → Slab**). As stated above, this can also be done with the Column or Beam tools, as they all produce the same type of object. After our object is created, we need to make the following changes to its properties:

-   Set its **Height** to **20 cm**
-   Verify its **IFC Type** is set to **Slab**

Now we need to move our new roof slab to its correct position, that is, above the walls. So we need to move it upwards, in the Z direction, by a distance of 250 cm, which is the height of our walls. We can simply edit the **Placement** property of our slab, expand its **Position** attribute, and set the value of **z** to 250 cm. Our slab is now well in place:

<img alt="" src=images/BIM_Tutorial_21.jpg  style="width:300px;">

Another way to move our slab to its correct position, is to use the <img alt="" src=images/Draft_Move.png  style="width:16px;"> **Move** tool from the **Modify** menu. For that, we need to set our working plane in a vertical plane first, by pressing the <img alt="" src=images/Draft_SelectPlane.png  style="width:16px;"> **working plane** button (make sure you don\'t have any face selected), and setting it to **XZ (Front)**. By setting ourselves in front view (press key **1**), we can now select the slab, press the <img alt="" src=images/Draft_Move.png  style="width:16px;"> **Move** button, and move our slab by clicking one of its base points, and, with **Shift** pressed to restrict the movement vertically, click one point on top of the walls:

<img alt="" src=images/BIM_Tutorial_23.jpg  style="width:300px;">

#### Method 2: Draw the slab directly in the correct plane 

Another useful method is directly working on the intended plane. We can easily set the working plane to the top surface of the walls, which is where we want our slab. Selecting a face and pressing the <img alt="" src=images/Draft_SelectPlane.png  style="width:16px;"> **working plane** button sets the working plane to coincide with the selected face. Select the top face of the wall and set it as the current working plane. The placement of the grid moves to show the current working plane.

<img alt="" src=images/BIM_Tutorial_22.jpg  style="width:300px;">

Everything we draw from now on will happen in that plane. If you like, you can now set yourself in top view, but this is not necessary. Once your working plane is set, and if **working plane snapping** is enabled, you can draw directly in any type of 3D view.

Once our rectangular *profile* is drawn, we can follow the same method as in method one to create a slab (select it, press the **Structure** button, adjust its properties).


{{BIMTutorialAction|goal1=Create a rectangle|test1=bool(len([o for o in FreeCAD.ActiveDocument.Objects if "Rectangle" in o.Name]) == 1)|goal2=Create a 20 cm thick slab|test2=bool(len([o for o in FreeCAD.ActiveDocument.Objects if "IfcType" in o.PropertiesList and o.IfcType == "Slab" and o.Height.Value == 200]) == 1)}}

### Create a metallic column 

Let\'s add a metallic column to give better support to our slab. Make sure the working plane is in Top mode, let\'s start by putting ourselves in top view (press key **2**), and turn the slab off, so we see better what\'s underneath. Select the slab, and press the **Space** key to turn its display off.

In FreeCAD, it is very easy to turn objects or groups on and off, and the tree shows you clearly what is shown and what is hidden. Be sure to use that often!

The **Column** tool (as well as the Beam tool) has some built-in profiles that we will use now. Make sure nothing is selected, then press the Column button. In the **Structure options**, select the category **CHS** (for \"Circular Hollow Section\"; RHS stands for \"Rectangular Hollow Section\", HEA, HEB, etc. are various \"H\" sections, etc.):

<img alt="" src=images/BIM_Tutorial_24.jpg  style="width:300px;">

And click a point to place your column, more or less at this position. Make sure the new column has an IFC Type of \"Column\" and give it a Height of 250 cm to make it the same height as our walls.

<img alt="" src=images/BIM_Tutorial_25.jpg  style="width:300px;">

The default CHS preset has a diameter option of 21.3 mm, which is too thin to support our concrete roof slab. Fortunately, as everything is parametric, it is easy to change the diameter. Expand the new structural object in the tree view, and you will find its profile object, named CHS21.3x2.6\_. Change its diameter to 12 cm and its thickness to 8 mm. Now we have a strong enough column. Notice that you can specify units on the fly and switch between 0.8 cm and 8 mm without issue. FreeCAD will take care of conversion.

#### Add a support plate 

We need a way to attach our metal column to the concrete slab. So let\'s add a plate to its top, which can be bolted to the concrete slab. This will illustrate how you can easily modify BIM objects and create the very precise ones you need.

Let\'s start by changing the height of our column from 250 cm to 249 cm, to give it a space for a 1 cm-thick plate. Then draw a 20 cm x 20 cm rectangle, either on the ground plane or by setting the top of the column as the current working plane, as we learned in the previous step. Use the **Move** tool, with midpoint and center snaps turned on, if needed, to center the rectangle over the column center.

Using the Slab tool again, create a structural object from the rectangle, give it a height of 1 cm, and move it to a height of 249 cm:

<img alt="" src=images/BIM_Tutorial_26.jpg  style="width:300px;">

Now let\'s add our plate to the column. BIM objects in FreeCAD have two properties named **Additions** and **Subtractions** that can receive objects that need to be unioned or subtracted to/from them. To add the plate to our column, select the plate, then, with **Ctrl** pressed, select the column and use the <img alt="" src=images/Arch_Add.png  style="width:16px;"> **Add** tool from the **Modify** menu. Our plate is now part of the column:

<img alt="" src=images/BIM_Tutorial_27.jpg  style="width:300px;">

By starting from simple shapes as *profiles*, and adding or subtracting objects, we can quickly create very complex BIM objects. Note that the Additions and Subtractions of a given BIM object can easily be changed by double-clicking them in the tree view and using the Add and Remove buttons there. The same object can also be used as an addition or subtraction to several other objects.

<img alt="" src=images/BIM_Tutorial_28.jpg  style="width:300px;">


{{BIMTutorialAction|goal1=Create a CHS tubular column|test1=bool(len([o for o in FreeCAD.ActiveDocument.Objects if "CHS" in o.Label]) == 1)|goal2=Add a 20 cm x 20 cm plate to the column|test2=bool(len([o for o in FreeCAD.ActiveDocument.Objects if "Shape" in o.PropertiesList and (FreeCAD.Units.Quantity("300 cm^3") < o.Shape.Volume < FreeCAD.Units.Quantity("500 cm^3"))]) == 1)}}

### Add a door 

Like columns and beams, doors and windows are created from the same [Window](Arch_Window.md) object in FreeCAD. Only their IFC type changes. They can be independent or, if an object is selected when running the tool, inserted in another BIM object, in which case they will automatically create a hole through it.

Let\'s insert a 80 cm x 210 cm glass door in one of our walls. Start by placing the working plane on a face of a wall, which will make it easier to precisely place our door:

<img alt="" src=images/BIM_Tutorial_29.jpg  style="width:300px;">

Then, with the wall selected, select **Door** from the **BIM** menu. Select the **Glass door** preset, and set the **Width** to 80 cm and **Height** to 210 cm. You can set the other values as you like:

<img alt="" src=images/BIM_Tutorial_30.jpg  style="width:300px;">

Click a point on the base of the wall where you wish to place the window. This can be difficult, as the grid lines don\'t necessarily correspond to the wall edges. Press the **Q** key while you have an active snap at a grid intersection, and press it again with an active snap on the bottom of the wall. FreeCAD will create a new snap point where their horizontal/vertical axis intersect. Use this to find a suitable point:

<img alt="" src=images/BIM_Tutorial_31.jpg  style="width:300px;">

If your door didn\'t get placed correctly, try the **Move** tool to move it to its correct position. Otherwise use undo or delete it from the model tree and try again.

When everything is done, you should obtain a door properly inserted into its wall:

<img alt="" src=images/BIM_Tutorial_32.jpg  style="width:300px;">


{{BIMTutorialAction|goal1=Create a glass door|test1=bool(len([o for o in FreeCAD.ActiveDocument.Objects if "Window" in o.Name]) == 1)}}

### Organizing our model 

We now have in our model a growing collection of BIM objects. It is time to tidy things up. Creating well organized models, easily understandable by others, is a very important part of building quality BIM models.

A first very simple and very good habit to take is to give proper and meaningful **names** to our objects, so we can easily identify them in the tree view later on. To rename an object, right-click it in the tree view and choose **Rename**. A model where components are easily identifiable by others is a huge part of what makes a good BIM model.

Another interesting operation to do is **grouping**. Groups allow you to organize your objects in the tree view, like files and folders. An object can only belong to one group. Groups are created by right-clicking the document root or any other group in the tree view, and selecting **Create group**. You can then drag objects in and out of groups in the tree view.

A third way to organize things is by using **layers**. Layers are independent of groups, you can use both systems at the same time if you wish. Like groups, layers allow you to easily turn on/off a series of objects, but unlike groups, they cannot be stacked inside one another. They also allow you to override visual settings such as the color and line width of their child objects. Layers are created and managed using the Layers manager tool found under menu **Manage → Manage layers\...**. Objects are added or removed by dragging them in and out of layers in the tree view. The **Layer selector** on the main toolbar allows you to set a current layer. After doing so, any new 2D or BIM object will automatically be placed in that layer.

Finally, BIM applications usually allow you to group objects into **levels** (or storeys) and **buildings**. FreeCAD offers these tools as well under the **3D/BIM** menu. Like beams and columns, levels and buildings use the same object type called [Building Part](Arch_BuildingPart.md) with a different IFC type. They work the same way as groups, once created, you can drag and drop any object in and out of it. Building Parts are compatible with groups, so you can place groups inside them.

<img alt="" src=images/BIM_Tutorial_36.jpg  style="width:300px;">

Building Parts have many other uses, refer to their [documentation](Arch_BuildingPart.md) to know more.

Create a Building Part now by selecting **Level** from the **3D/BIM** menu. Make sure its IFC type is set to **Building Storey**, and drag all our other root BIM objects (no need to do so with included objects like the door or the plate of the column) into it, that is, our two walls, the roof slab and the metal column.

Note that, as Building Parts are generic building components, you are not forced to organize your model by levels in FreeCAD. You can choose to group your elements differently. But the IFC format expects things to be grouped by level, so if you plan to use that format, it is best to consider your Building Parts as levels.


{{BIMTutorialAction|goal1=Create a level|test1=bool(len([o for o in FreeCAD.ActiveDocument.Objects if "BuildingPart" in o.Name]) == 1)|goal2=Add the four other root BIM objects to it|test2=bool(len([o for o in FreeCAD.ActiveDocument.Objects if "BuildingPart" in o.Name and (len(o.Group) == 4)]) == 1)}}

### Adding section planes 

One of the most common operations performed on a BIM model is to extract 2D drawings from it, such as plans or elevations. There are several ways to do that in FreeCAD, depending on the result you wish to obtain. Basically, you have two choices:

-   Producing the 2D result inside the 3D space. This is useful if you wish to rework it there, build further on it or better control how it is exported to formats like [DXF](Draft_DXF.md) or [DWG](FreeCAD_and_DWG_Import.md).
-   Creating 2D views on a [TechDraw sheet](TechDraw_Workbench.md) that is better suited for impression or export to PDF.

In both cases, it starts with placing a [Section Plane](Arch_SectionPlane.md) in your model:

<img alt="" src=images/BIM_Tutorial_37.jpg  style="width:300px;">

1.  Select the Level object that contains your objects, that we created in the last step
2.  Add a Section Plane from menu **Annotations → Section Plane**

Section planes don\'t cut through the whole model, but only through objects in their **Objects** property. You can select the Section Plane to check and change the contents of this property anytime.

By default, the new section plane will be placed in the middle of the selected object or its contents, and will look downwards, as to create a floor plan view. But the section plane is an object like any other and can be moved and rotated to do what you need. Place it horizontally to create a plan view, vertically inside your model to create a section, or outside the model to create an elevation.


{{BIMTutorialAction|goal1=Select the main Building Part|test1=bool(len([o for o in FreeCADGui.Selection.getSelection() if "BuildingPart" in o.Name]) == 1)|goal2=Create a section plane|test2=bool(len([o for o in FreeCAD.ActiveDocument.Objects if "Section" in o.Name and (len(o.Objects) == 1) and ("BuildingPart" in o.Objects[0].Name)]) == 1)}}

### Extracting 2D views as geometry 

Once your section plane is in place, we can now create 2D geometry from what it sees using the [Shape2DView](Draft_Shape2DView.md) tool:

<img alt="" src=images/BIM_Tutorial_38.jpg  style="width:300px;">

1.  Select the section plane
2.  Create a Shape 2D View using **Modify → Shape 2D View**
3.  Our view object is hidden under the walls. Hide the level and the section plane by selecting them both in the tree view and pressing the space bar, so we can see our result better:

<img alt="" src=images/BIM_Tutorial_39.jpg  style="width:300px;">

The 2D view we created is an all-in-one 2D object and will be located on the (0,0) ground plane in the model. It can be moved around, and will be recalculated if the model changes.

To create thicker lines for cut areas, you can create another Shape 2D view, and set its **Projection Mode** property to \"Cutlines\" or \"Cutfaces\", and its **In Place** property to \"False\". You will then have two objects, one for viewed lines and one for cut lines, for which you can give different line thicknesses.


{{BIMTutorialAction|goal1=Select the section plane|test1=bool(len([o for o in FreeCADGui.Selection.getSelection() if "Section" in o.Name]) == 1)|goal2=Create a Shape 2D View|test2=bool(len([o for o in FreeCAD.ActiveDocument.Objects if "Shape2DView" in o.Name]) == 1)}}

### Annotating and exporting to 2D CAD formats 

You can place [Texts](Draft_Text.md), [Labels](Draft_Label.md) (text with line and arrow), [Dimensions](Draft_Dimension.md) on anything in the model space: Either directly on the 3D model, or on the 2D view that we created in the step above. The choice is yours, depending on what you wish to achieve. If you leave the 2D view exactly under the 3D model, you might also want to do both in one go.

![](images/BIM_Tutorial_34.jpg )

Annotations (texts, labels, dimensions) will be placed on the current **Working Plane**. Be sure to place your working plane where you want your annotations. You can this way place annotations in any plane of the 3D space: Horizontally or vertically. You can also move or rotate them after creation.

Let\'s place a horizontal dimension between the extremities of our two walls:

![](images/BIM_Tutorial_40.jpg )

1.  Set the **working plane** to **Top** position
2.  Orient your view to be able to view the base of both walls
3.  Choose menu **Annotations** → <img alt="" src=images/Draft_Dimension.png  style="width:16px;"> [Dimension](Draft_Dimension.md)
4.  Click a first point at the extremity of the left wall
5.  Press **SHIFT** to constrain the dimension vertically or horizontally
6.  Click a second point at the extremity of the right wall
7.  Click a third point to indicate where to place the dimension line

[Dimensions](Draft_Dimension.md) have a lot of settings to tweak their aspect and the size and type of the text and arrow. You can set your preferred defaults under menu **Edit → Preferences → Draft → Texts and dimensions**.

Now let\'s add a text:

![](images/BIM_Tutorial_41.jpg )

1.  Choose menu **Annotations** → <img alt="" src=images/Draft_Text.png  style="width:16px;"> [Text](Draft_Text.md)
2.  Click a location in the 3D view to place the text
3.  Write the text you wish, for example **Pavilion**, then click the **Create text** button or press Enter twice.

A good idea is to create **Groups** for the different sets of annotations (plan, section, different scales, etc\...):

1.  Create a group by right-clicking the document root and select **Create group**, rename it to \"Annotations\"
2.  Select the annotations we created above in the tree and drag and drop them into the group

#### Exporting to DXF 

2D objects such as lines or circles or 2D views as we created above or annotations are very suited to export to traditional 2D CAD formats such as [DXF or DWG](Draft_DXF.md). The DWG format requires an additional piece of software to be installed on your system, check the [instructions](Draft_DXF.md) to do that if needed.

Let\'s try to export our 2D work to DXF:

1.  Select the 2D view, the dimension and the text
2.  Select menu **File → Export**, choose the **Autodesk DXF**format, a file name, and press **Export**

If you don\'t use any 2D CAD program, there are several free and open-source applications that can open DXF files (apart from FreeCAD itself, of course!) such as [LibreCAD](https://librecad.org/) and [QCAD CE](https://qcad.org/).

![](images/BIM_Tutorial_42.jpg )


{{BIMTutorialAction|goal1=Create a dimension|test1=bool(len([obj for obj in FreeCAD.ActiveDocument.Objects if "Dimension" in obj.Name]))|goal2=Create a text|test2=bool(len([obj for obj in FreeCAD.ActiveDocument.Objects if "Text" in obj.Name]))}}

### Creating 2D geometry on a printable sheet 

Printable sheets are created and managed with the [TechDraw Workbench](TechDraw_Workbench.md). Let\'s create a new sheet and place a view of our model on it:

1.  Switch to the **TechDraw Workbench**
2.  Create a new empty sheet using the default template from menu **TechDraw → Page → Insert Default Page**
3.  Select the section plane and create a view on the page using **TechDraw → Views From Other Workbenches → Insert BIM Workbench Object**
4.  Change the **Scale** property of your Arch View.

\... To be continued


{{BIMTutorialAction|descr=No action to perform for this step}}

### Exporting an IFC file 

[IFC, or Industry Foundation Classes](https://en.wikipedia.org/wiki/Industry_Foundation_Classes), is a protocol and file format for exchanging BIM models between applications. By saving your model as an IFC file, you will be able to open it in most or all other open-source or proprietary BIM applications out there.

IFC import/export operations in FreeCAD are performed by an external piece of software called [IfcOpenShell](http://www.ifcopenshell.org/). Read the [Arch IFC](Arch_IFC.md) page to learn more about how to install it.

Once IfcOpenShell is installed, exporting your model as an IFC file is as simple as selecting the objects you wish to export, or just the top container (group or Building Part) that contains all other objects you wish to export, and use menu **File → Export** and choose the IFC file format.

Finally, once you have exported an IFC file, it is always a good idea to inspect it before sending it to other people, to make sure the model looks good and no object is missing. There are many free IFC viewer applications available on the internet for many platforms. A good, open-source viewer that works on all platforms is [IFC++](http://ifcquery.com/). If you want to use the IFC file for further editing [Bonsai](https://bonsaibim.org) might be useful.

To test the structure and validity of your model for IFC export run the **Manage → Preflight checks\...** tool. This will be discussed in the next section.


{{BIMTutorialAction|goal1=Open the BIM preflight tool and run all the tests|test1=True if (hasattr(FreeCADGui,"BIMPreflightDone") and (FreeCADGui.BIMPreflightDone == True)) else False}}

### Managing BIM properties 

A huge part of what makes a good BIM model are the non-geometry properties that you can give to your objects, such as type, material, or properties specific to a certain type. For example, a wall can be marked as load-bearing or not. Or as exterior or interior. The [IFC format](https://en.wikipedia.org/wiki/Industry_Foundation_Classes) is very rich in that regard. The amount of specifications and properties you want to give your objects depends mostly on your needs and how you work with others and what they expect your BIM model to contain.

One thing is important to keep in mind: all BIM/Arch objects in FreeCAD support the full set of IFC properties. Other FreeCAD objects, such as those modeled with other workbenches, will also be exported to IFC but you cannot change any of their IFC properties. You can however convert any FreeCAD object to a BIM object by selecting the object and using **3D/BIM → Create Component**.

The main pieces of information you can give your objects are:

#### Name and description 

This seems obvious, but the simplest way to make your model more understandable to others is to properly name each of your objects, and, if relevant, add a description. This is done simply by selecting an object, and pressing **F2**, or change its **Label** property to rename it. The Description will be found among the object properties.

#### The BIM/IFC type 

This is the most fundamental piece of information. In FreeCAD, an object created with the wall tool will have its IFC type set to \"Wall\" by default. But you can change this anytime. So you can use the wall tool to model a beam for example. You only need to change its IFC type after creating it. To change the IFC type of an object, select it, find its **IFC Type** in its properties, and change to another type from the drop-down list.

You can also bulk-manage names, types and materials of several objects at a time using the IFC elements manager found under menu **Manage → Manage IFC elements\...**.

#### Materials

Each object of a construction has a material. So it makes sense to give each object of your model a proper material, such as concrete or wood. To attribute a material to an object, select the object, and use the [materials manager](Arch_SetMaterial.md) from menu **Manage → Material**.

#### Properties

Each BIM object can also receive additional properties, for example to indicate that a wall is load-bearing or not. IFC allows you to add custom properties to just anything, but most types such as Wall or Beam also have special, predefined sets of properties, usually named Pset_WallCommon or Pset_BeamCommon. You can choose to add these sets to your objects, modify the value of the properties contained in the set, or add your custom properties. Managing the IFC properties for a selected object or bulk edit the properties of several objects at a time is done using the properties manager under menu **Manage → Manage IFC properties\...**.

#### Quantities

Quantities such as length or width or height of a wall can also be specifically written to an IFC file. They are not linked to the geometry of the object, so when meeting such quantities in an IFC file there is no guarantee that they reflect the actual object geometry. However, these quantities allow applications that are not able to process the geometry, such as spreadsheet applications, to know the principal dimensions of objects. You can check which quantities will be exported to IFC using the quantities manager found under menu **Manage → Manage IFC quantities\...**.

#### BIM Preflight tool 

The IFC format has many particularities and sometimes the application you will be opening your IFC file with or the person who will receive your IFC file will have further requirements. Becoming a fluent BIM modeller often means to get familiar with all these particularities and what needs to be added or specified to your BIM model. The BIM workbench of FreeCAD provides a [BIM Preflight](BIM_Preflight.md) tool that allows you to check your model for several of these particularities and most common requirements, and help you decide what to include in your model or not.


{{BIMTutorialAction|descr=No action to perform for this step}}

### Explore other BIM tools and other workbenches 

Take a moment to explore the other available BIM tools. Remeber that some are still not finished, and might not do everything you expect from them. Use the \"What\'s this?\" button found in menu **Help** to open the help page of any tool. The [FreeCAD forum](https://forum.freecadweb.org) is also always a good place to search or ask when encountering a specific problem you cannot solve.

FreeCAD is a big family of workbenches, and tools from other workbenches often come in handy. As we saw above, almost any object created from other workbenches can be turned into a valid BIM object, simply using the **3D/BIM → Generic 3D tools → Component** tool and giving it the correct IFC type.

There are more tutorials about BIM and other workbenches in the [Tutorials](Tutorials.md) section of the [FreeCAD documentation](https://wiki.freecadweb.org), and a complete video series of [BIM tutorials](https://www.youtube.com/playlist?list=PLmKdGVtV5Vnt2cj4IZIv9FM39QHaE1ZaU) on youtube.


{{BIMTutorialAction|descr=No action to perform for this step}}

### Help FreeCAD to become a better tool! 

FreeCAD is free software developed by an enthusiastic community of users, some of whom develop code, and many others who contribute in one form or another to make the software better by writing documentation, finding and reporting bugs, submitting ideas, writing tutorials, and many other things. The more and more active we are, the faster the software gets developed further. Why not join us? A good place to start is the [BIM section on the FreeCAD forum](https://forum.freecad.org/viewforum.php?f=23). See you there!


{{BIMTutorialAction|descr=No action to perform for this step}}



---
⏵ [documentation index](../README.md) > [Tutorials](Category_Tutorials.md) > [BIM](BIM_Workbench.md) > BIM ingame tutorial/it
