---
- TutorialInfo   *   Topic   *Assembly3, a kinematic skeleton
   Level   *Basic knowledge of Assembly3 and Sketcher tools is helpful
   FCVersion   *0.20 and later
   Time   *40 minutes
   Author   *[FBXL5](User_FBXL5.md)
---

# Tutorial KinematicSkeleton

 



## Introduction

This tutorial is about how to set up a simple 2D mechanism and attach 3D objects, mainly with the tools from the external <img alt="" src=images/Assembly3_workbench_icon.svg  style="width   *16px;"> [Assembly3 Workbench](Assembly3_Workbench.md).

This tutorial does not use the skeleton sketch principle. See [notes](Assembly3_ConstraintAngle#Notes.md) for reasons.

Instead we will use <img alt="" src=images/PartDesign_Body.svg  style="width   *16px;"> [PartDesign Bodies](PartDesign_Body.md) containing only one <img alt="" src=images/Workbench_Sketcher.svg  style="width   *16px;"> [Sketch](Sketcher_Workbench.md) each, to build a 2D mechanism, a **multi sketch skeleton**.

The dimensions and the colours as well are taken from the [SolveSpace tutorial](http   *//solvespace.com/linkage.pl) which is referred to on the Assembly3 GitHub page [Create-Skeleton-Sketch](https   *//github.com/realthunder/FreeCAD_assembly3/wiki/Create-Skeleton-Sketch).

## Multi sketch skeleton 

This so called multi sketch skeleton consists of several individual <img alt="" src=images/PartDesign_Body.svg  style="width   *16px;"> [Bodies](PartDesign_Body.md) and an <img alt="" src=images/Assembly_New_Assembly.svg‎‎  style="width   *16px;"> [Assembly](Assembly3_CreateAssembly.md) container. To be able to attach further objects each body is put into a separate Assembly container.

### 2D Body objects 

The bodies or rather their contours that are used with this assembly   *

-   A base plate (green)
-   A crank (blue)
-   Two movable plates (red and grey)
-   Four connecting rods (white, yellow, purple, and brown)

<img alt="" src=images/Assembly3_SketchSkeleton-01.png  style="width   *400px;"> 
*All eight sketches individually coloured and manually positioned by moving their parent bodies *

The geometry can deviate from the real part\'s shape, except the position of the joint defining geometry.

### Assembly containers 

#### Parent Assembly 

To fix or control the positions of all bodies we need an <img alt="" src=images/Assembly_New_Assembly.svg‎‎  style="width   *16px;"> Assembly object. It adds an assembly branch to the [Tree View](Tree_View.md).

-   Press the **<img src="images/Assembly_New_Assembly.svg‎‎" width=16px> [Create assembly](Assembly3_CreateAssembly.md)** button to create an Assembly branch in the [Tree View](Tree_View.md).

#### Sub-Assemblies 

Repeat above action to create an Assembly object for each Body and drag the Body into its Parts container. Then fix the Body to its Assembly   *

1.  Activate the Assembly object (double-click).
2.  Select a circle/arc belonging the Body object.
3.  Press the **<img src="images/Assembly_ConstraintLock.svg‎‎" width=16px> [Create "Locked" contraint](Assembly3_ConstraintLock.md)** button to fix the Body in its sub-assembly.

The Crank-Assembly e.g. should look like this   *

<img alt="" src=images/Assembly3_SketchSkeleton-25.png  style="width   *500px;"> 
*The Crank's sub-assembly branch in the Tree view and the Crank with its locked Element in the 3D view*

#### Assembly tree 

In the Tree view drag all sub-assembly branches into the Parts container of the parent Assembly object.

<img alt="" src=images/Assembly3_SketchSkeleton-26.png  style="width   *300px;"> 
*Assembly branch in the Tree view*

Now they are ready to get arranged.

### Fixed base plate 

At first we need a fixed part. To fix the Base completely we would usually select a face, but in this case a circle will do as well.

1.  Select a circle of the Base.
2.  Press the **<img src="images/Assembly_ConstraintLock.svg‎‎" width=16px> [Create "Locked" contraint](Assembly3_ConstraintLock.md)** button to fix the Base.

<img alt="" src=images/Assembly3_SketchSkeleton-02.png  style="width   *300px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="" src=images/Assembly3_SketchSkeleton-03.png  style="width   *300px;"> 
*Selected circle → Fixed Base with the created Element object and element coordinate system (ECS) displayed (green)*

### Joints

For hinge-like joints we select one circle of each sketch and use the <img alt="" src=images/Assembly_ConstraintCoincidence.svg‎‎  style="width   *16px;"> [Plane Coincidence](Assembly3_ConstraintCoincidence.md) constraint. It does not only set both Element\'s XY planes coplanar, but set their Z axes colinear, too.

1.  Select a circle of each object to connect.
2.  Press the **<img src="images/Assembly_ConstraintCoincidence.svg‎‎" width=16px> [Create "Plane Coincidence" contraint](Assembly3_ConstraintCoincidence.md)** button.

#### Base - Crank joint 

<img alt="" src=images/Assembly3_SketchSkeleton-04.png  style="width   *300px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="" src=images/Assembly3_SketchSkeleton-05.png  style="width   *300px;"> 
*Circles on Base and Crank selected → Relocated Crank with the created Element objects and ECSs displayed (green)*

#### Base - UpperPlate joint 

<img alt="" src=images/Assembly3_SketchSkeleton-06.png  style="width   *300px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="" src=images/Assembly3_SketchSkeleton-07.png  style="width   *300px;"> 
*Circles on Base and Upper Plate selected → Relocated Upper Plate*

Previously created joints are represented by their constraint representations (red).

#### Base - Upper Plate joint 

<img alt="" src=images/Assembly3_SketchSkeleton-08.png  style="width   *300px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="" src=images/Assembly3_SketchSkeleton-09.png  style="width   *300px;"> 
*Circles on Crank and Rod 1 selected → Relocated Rod 1 and tilted Crank*

#### Upper Plate - Rod 1 joint 

The last link in a kinematic chain connects two Elements with their Z directions already defined and a <img alt="" src=images/Assembly_ConstraintPointOnLine.svg‎‎  style="width   *16px;"> [Point on line](Assembly3_ConstraintPointOnLine.md) constraint is all we need.

1.  Select a circle of each object to connect.
2.  Press the **<img src="images/Assembly_ConstraintPointOnLine.svg‎‎" width=16px> [Create "PointOnLine" contraint](Assembly3_ConstraintPointOnLine.md)** button.

<img alt="" src=images/Assembly3_SketchSkeleton-10.png  style="width   *300px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="" src=images/Assembly3_SketchSkeleton-11.png  style="width   *300px;"> 
*Circles on Upper Plate and Rod 1 selected → Relocated Rod 1, and tilted Crank and Upper Plate*

If there are 3 joints in line (those belonging to Crank and Rod 1), the solver might fail to rearrange the objects. In such case we need to help the solver and tilt one object (e.g. the Crank) manually using the <img alt="" src=images/Assembly_AxialMove.svg  style="width   *16px;"> [Axial move](Assembly3_AxialMove.md) tool.

#### Upper Plate - Rod 2 joint 

Another kinematic (sub-)chain starts with <img alt="" src=images/Assembly_ConstraintCoincidence.svg‎‎  style="width   *16px;"> [Plane Coincidence](Assembly3_ConstraintCoincidence.md) constraints.

<img alt="" src=images/Assembly3_SketchSkeleton-12.png  style="width   *300px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="" src=images/Assembly3_SketchSkeleton-13.png  style="width   *300px;"> 
*Circles on Upper Plate (or Base) and Rod 2 selected → Relocated Rod 2*

#### Rod 2 - Lower Plate joint 

<img alt="" src=images/Assembly3_SketchSkeleton-14.png  style="width   *300px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="" src=images/Assembly3_SketchSkeleton-15.png  style="width   *300px;"> 
*Circles on Rod 2 and Lower Plate selected → Relocated Lower Plate and tilted Rod 2*

#### Upper Plate - Rod 3 joint 

<img alt="" src=images/Assembly3_SketchSkeleton-16.png  style="width   *300px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="" src=images/Assembly3_SketchSkeleton-17.png  style="width   *300px;"> 
*Circles on Upper Plate and Rod 3 selected → Relocated Rod 3 and rearranged upper kinematic sub-chain*

#### Lower Plate - Rod 3 joint 

And this kinematic (sub-)chain ends with a <img alt="" src=images/Assembly_ConstraintPointOnLine.svg‎‎  style="width   *16px;"> [Point on line](Assembly3_ConstraintPointOnLine.md) constraint, too.

<img alt="" src=images/Assembly3_SketchSkeleton-18.png  style="width   *300px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="" src=images/Assembly3_SketchSkeleton-19.png  style="width   *300px;"> 
*Circles on Lower Plate and Rod 3 selected → Relocated Rod 3 and rearranged ukinematic sub-chains*

To connect both kinematic sub-chains we use Rod 4 with a <img alt="" src=images/Assembly_ConstraintCoincidence.svg‎‎  style="width   *16px;"> [Plane Coincidence](Assembly3_ConstraintCoincidence.md) constraint on one end and a <img alt="" src=images/Assembly_ConstraintPointOnLine.svg‎‎  style="width   *16px;"> [Point on line](Assembly3_ConstraintPointOnLine.md) constraint on the other.

#### Crank - Rod 4 joint 

<img alt="" src=images/Assembly3_SketchSkeleton-20.png  style="width   *300px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="" src=images/Assembly3_SketchSkeleton-21.png  style="width   *300px;"> 
*Circles on Crank and Rod 4 selected → Relocated Rod 4*

#### Lower Plate - Rod 4 joint 

<img alt="" src=images/Assembly3_SketchSkeleton-22.png  style="width   *300px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="" src=images/Assembly3_SketchSkeleton-23.png  style="width   *300px;"> 
*Circles on Lower Plate and Rod 4 selected → Relocated Rod 4 and final layout of kinematic assembly*

### Actuator

Since Assembly3 doesn\'t provide any means to control kinematic assemblies, we need external assistance such as this [kinematic controller](Tutorial_KinematicController.md). To use this controller we need to mark one constraint\'s label with the suffix {{Incode|"Driver"}} to make it a driving constraint. It may be separated by a {{Incode|"."}} or {{Incode|"-"}} for clarity, as the controller will only check if the label ends with {{Incode|"Driver"}}.

Thus the Base-Crank joint will be labeled {{Incode|Base-Crank.Driver}}.

### Finished skeleton 

The finished kinematic assembly with deactivated representation of Elements and Constraints should look like this   *

<img alt="" src=images/Assembly3_SketchSkeleton-24.png  style="width   *500px;"> 
*Finished assembly in the [Tree view](Tree_view.md) and the [3D view](3D_view.md)*

<img alt="" src=images/Assembly3_SketchSkeleton-27.gif  style="width   *500px;"> 
*GIF animation made from an image sequence from this [kinematic controller](Tutorial_KinematicController.md)*

## Attaching 3D geometry 

My expectations about attaching a new object to a base object belonging to a kinematic assembly were something like   *

-   Put the new object into the base objects Parts container.
-   Position the new object in relation to the base object.
-   Fix the relative offset and orientation using the Attachment constraint.

But that would have been too easy.

The <img alt="" src=images/Assembly_ConstraintAttachment.svg‎‎  style="width   *16px;"> [Assembly3 ConstraintAttachment](Assembly3_ConstraintAttachment.md) tool, like any Assembly3 constraint tool, relies on the use of Element objects and their element coordinate systems (ECSs) for positioning tasks.

And so attaching objects is just another way to say adding objects to a (sub-) assembly.

Let\'s attach Rod 4-3D to Rod 4 for example   *

The objects have a different orientation and the 3D object should have an offset from the 2D object.

1.  Put the new object into the base objects Parts container.
2.  Select two corresponding circles or arcs.
3.  Press the **<img src="images/Assembly_ConstraintAttachment.svg‎‎" width=16px> [Create "Attachment" contraint](Assembly3_ConstraintAttachment.md)**.

   *   <img alt="" src=images/Assembly3_SketchSkeleton-28.png  style="width   *200px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="" src=images/Assembly3_SketchSkeleton-29.png  style="width   *200px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="" src=images/Assembly3_SketchSkeleton-30.png  style="width   *200px;">



*Rod 4 (locked) and Rod 4-3D → Selected arcs → Relocated Rod 4-3D (both ECSs are in the same place with identical orientation)*

It is now plain to see that the <img alt="" src=images/Assembly_ConstraintAttachment.svg‎‎  style="width   *16px;"> [Assembly3 ConstraintAttachment](Assembly3_ConstraintAttachment.md) tool ignores the offset and orientation between both objects.

However the position is already defined as we wanted and so we only need to adapt the angle manually and define the desired offset   *

-   Set the **Offset, Angle** of the first Element in the Attachment container to match the orientation.
-   Set the **Offset, Position, z** of the same Element to apply an offset.

In case we set the properties of the second Element, the movement of angle and offset would go in the opposite direction.

   *   <img alt="" src=images/Assembly3_SketchSkeleton-30.png  style="width   *200px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="" src=images/Assembly3_SketchSkeleton-31.png  style="width   *200px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="" src=images/Assembly3_SketchSkeleton-32.png  style="width   *200px;">



*As attached → Angle adapted → Offset defined*

If there is a 3D object attached to each 2D object, it could look like this   *

<img alt="" src=images/Assembly3_SketchSkeleton-33.gif  style="width   *500px;">

## Notes

The section about attaching 3D geometry just scratches the surface of extending a sub-assembly and other constraints or combinations of constraints can be more suitable than the attachment constraint.

It is important to move such a kinematic assembly with tiny steps or the solver will give up and fail. It is almost impossible to use <img alt="" src=images/Assembly_Move.svg‎‎  style="width   *16px;"> [Move part](Assembly3_MovePart.md) or <img alt="" src=images/Assembly_AxialMove.svg‎‎  style="width   *16px;"> [Axial move](Assembly3_AxialMove.md) for this task.

The <img alt="" src=images/Assembly_ConstraintCoincidence.svg‎‎  style="width   *16px;"> [Assembly3\_ConstraintCoincidence](Assembly3_ConstraintCoincidence.md) constraint is used to drive the kinematic assembly, its property **Angle** (enabled by the property **Lock Angle**) accepts positive or negative floating point numbers greater than 360 and so could do several full turns.



---
![](images/Right_arrow.png) [documentation index](../README.md) > Tutorial KinematicSkeleton
