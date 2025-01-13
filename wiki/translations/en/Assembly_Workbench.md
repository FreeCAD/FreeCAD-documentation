# <img alt="Assembly workbench icon" src=images/Workbench_Assembly.svg  style="width:64px;"> Assembly Workbench/en




## Introduction


<small>(v1.0)</small> 

The <img alt="" src=images/Workbench_Assembly.svg  style="width:24px;"> [Assembly Workbench](Assembly_Workbench.md) is FreeCAD\'s new built-in assembly workbench. It uses the open-source [Ondsel solver](https://github.com/Ondsel-Development/OndselSolver).

<img alt="" src=images/Assembly_Workbench_Example.png  style="width:400px;">

## Tools

### Assembly

-   <img alt="" src=images/Assembly_CreateAssembly.svg  style="width:32px;"> [Create Assembly](Assembly_CreateAssembly.md): creates a root assembly in the current document, or a sub-assembly in a pre-existing active assembly.

-   <img alt="" src=images/Assembly_InsertLink.svg  style="width:32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Insert:

  - <img alt="" src=images/Assembly_InsertLink.svg  style="width:32px;"> [Insert Component](Assembly_InsertLink.md): inserts a component into the active assembly.

  - <img alt="" src=images/Assembly_InsertNewPart.svg  style="width:32px;"> [Insert a new part](Assembly_InsertNewPart.md): inserts a new Part.

-   <img alt="" src=images/Assembly_SolveAssembly.svg  style="width:32px;"> [Solve Assembly](Assembly_SolveAssembly.md): solves the currently active assembly.

-   <img alt="" src=images/Assembly_CreateView.svg  style="width:32px;"> [Create Exploded View](Assembly_CreateView.md): creates an exploded views container in the active assembly that contains one or more exploded views.

-   <img alt="" src=images/Assembly_CreateSimulation.svg  style="width:32px;"> [Create Simulation](Assembly_CreateSimulation.md): creates a simulation of the current assembly. <small>(v1.1)</small> 

-   <img alt="" src=images/Assembly_CreateBom.svg  style="width:32px;"> [Create Bill of Materials](Assembly_CreateBom.md): creates a bill of materials (BOM) from a selected assembly or from the document.

-   <img alt="" src=images/Assembly_ExportASMT.svg  style="width:32px;"> [Export ASMT File](Assembly_ExportASMT.md): exports the currently active assembly as an ASMT file.

### Joints

-   <img alt="" src=images/Assembly_ToggleGrounded.svg  style="width:32px;"> [Toggle Grounded](Assembly_ToggleGrounded.md): fixes the position and orientation of a shape in relation to the coordinate system of the assembly it belongs to.

-   <img alt="" src=images/Assembly_CreateJointFixed.svg  style="width:32px;"> [Create a Fixed Joint](Assembly_CreateJointFixed.md): creates a joint locking two assembly parts together, preventing any movement or rotation but can be also used to define other types of joints.

-   <img alt="" src=images/Assembly_CreateJointRevolute.svg  style="width:32px;"> [Create Revolute Joint](Assembly_CreateJointRevolute.md): creates a hinged joint, allowing rotation around a single axis between two selected parts.

-   <img alt="" src=images/Assembly_CreateJointCylindrical.svg  style="width:32px;"> [Create Cylindrical Joint](Assembly_CreateJointCylindrical.md): creates a cylindrical joint between two selected parts, allowing rotation around a single axis and a movement along the same axis.

-   <img alt="" src=images/Assembly_CreateJointSlider.svg  style="width:32px;"> [Create Slider Joint](Assembly_CreateJointSlider.md): creates a slider (prismatic) joint between two selected parts, allowing a linear movement along a single axis while restricting rotation.

-   <img alt="" src=images/Assembly_CreateJointBall.svg  style="width:32px;"> [Create Ball Joint](Assembly_CreateJointBall.md): creates a spherical joint between two selected parts at a single point, allowing free rotation around the point while keeping both parts connected at this point.

-   <img alt="" src=images/Assembly_CreateJointDistance.svg  style="width:32px;"> [Create Distance Joint](Assembly_CreateJointDistance.md): creates a distance joint between two selected parts, fixing the distance between both parts.

-   <img alt="" src=images/Assembly_CreateJointParallel.svg  style="width:32px;"> [Create Parallel Joint](Assembly_CreateJointParallel.md): creates a parallel joint between two selected parts, setting the Z axes of selected coordinate systems parallel.

-   <img alt="" src=images/Assembly_CreateJointPerpendicular.svg  style="width:32px;"> [Create Perpendicular Joint](Assembly_CreateJointPerpendicular.md): creates a perpendicular joint between two selected parts, setting the Z axes of selected coordinate systems perpendicular.

-   <img alt="" src=images/Assembly_CreateJointAngle.svg  style="width:32px;"> [Create Angle Joint](Assembly_CreateJointAngle.md): creates an angle joint between two selected parts, fixing the angle between the Z axes of selected coordinate systems.

-   <img alt="" src=images/Assembly_CreateJointRackPinion.svg  style="width:32px;"> [Create Rack and Pinion Joint](Assembly_CreateJointRackPinion.md): creates a rack and pinion joint that couples the translation of a part of a slider joint and the rotation of a part of a revolute joint.

-   <img alt="" src=images/Assembly_CreateJointScrew.svg  style="width:32px;"> [Create Screw Joint](Assembly_CreateJointScrew.md): creates a screw (helical) joint that couples the translation of a part of a slider joint and the rotation of a part of a revolute joint.

-   <img alt="" src=images/Assembly_CreateJointGears.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Create Gear/Belt Joint:

  - <img alt="" src=images/Assembly_CreateJointGears.svg  style="width:32px;"> [Create Gears Joint](Assembly_CreateJointGears.md): creates a gears joint that couples the rotation of two parts of two different revolute joints.

  - <img alt="" src=images/Assembly_CreateJointBelt.svg  style="width:32px;"> [Create Belt Joint](Assembly_CreateJointBelt.md): creates a belt joint that couples the rotation of two parts of two different revolute joints.

## Preferences

-   <img alt="" src=images/Preferences-assembly.svg  style="width:32px;"> [Preferences](Assembly_Preferences.md): preferences for the Assembly workbench.

## Example crank and slider 


<div class="mw-collapsible mw-collapsed toccolours">

<img alt="" src=images/Assembly3_KinematicExample-01.png  style="width:80px;"> This example is temporary and may be removed once proper descriptions/tutorials are available.


<div class="mw-collapsible-content">

### Crank and slider assembly 

The assembly to be created consists of four parts: a Base, a Slider Rod, a Crank, and a Connecting Rod. They are connected with four joints.

<img alt="" src=images/Assembly3_KinematicExample-01.png  style="width:300px;">



*Assembled parts: Base (amber), Slider Rod (light blue), Crank (red), Connecting Rod (green)*

### Prepare parts 

In this example all parts and the assembly are created in one document.

The cylindrical geometries of the objects are either parallel or perpendicular, the rest of the shapes is not relevant for this example unless there are clashes. With this in mind you can model your own objects or create them with the Python code below. The code will create a new document with the four objects (simpler than in the images). Just copy-paste the following lines in the [Python console](Python_console.md):


```python
import FreeCAD as App
import FreeCADGui as Gui
import Part

doc = App.newDocument()

box1 = Part.makeBox(140, 40, 7, App.Vector(0, -20, 0))
cyl1 = Part.makeCylinder(4, 8, App.Vector(120, 0, 7))
box2 = Part.makeBox(20, 12, 10, App.Vector(5, -6, 7))
cyl2 = Part.makeCylinder(6, 20, App.Vector(25, 0, 17), App.Vector(-1, 0, 0))
cyl3 = Part.makeCylinder(4, 20, App.Vector(25, 0, 17), App.Vector(-1, 0, 0))
shape = box1.fuse([cyl1, box2, cyl2]).removeSplitter().cut(cyl3)
base = doc.addObject("Part::Feature", "Base")
base.Shape = shape

box1 = Part.makeBox(4, 12, 12, App.Vector(-12, -6, 0))
box2 = Part.makeBox(14, 12, 4, App.Vector(-8, -6, 0))
cyl1 = Part.makeCylinder(4, 8, App.Vector(0, 0, 4))
cyl2 = Part.makeCylinder(4, 88, App.Vector(-12, 0, 6),App.Vector(-1, 0, 0))
shape = box1.fuse([box2, cyl1, cyl2]).removeSplitter()
slider_rod = doc.addObject("Part::Feature", "SliderRod")
slider_rod.Shape = shape
slider_rod.Placement.Base = App.Vector(100, -40, 0)

cyl1 = Part.makeCylinder(7.5, 4)
box1 = Part.makeBox(15, 30, 4, App.Vector(-7.5, 0, 0))
cyl2 = Part.makeCylinder(7.5, 4, App.Vector(0, 30, 0))
cyl3 = Part.makeCylinder(4, 6, App.Vector(0, 30, 4))
cyl4 = Part.makeCylinder(4, 4)
shape = cyl1.fuse([box1, cyl2]).removeSplitter().fuse(cyl3).cut(cyl4)
crank = doc.addObject("Part::Feature", "Crank")
crank.Shape = shape
crank.Placement.Base = App.Vector(125, -70, 0)

cyl1 = Part.makeCylinder(6, 4)
box1 = Part.makeBox(50, 12, 4, App.Vector(0, -6, 0))
cyl2 = Part.makeCylinder(6, 4, App.Vector(50, 0, 0))
cyl3 = Part.makeCylinder(4, 4)
cyl4 = Part.makeCylinder(4, 4, App.Vector(50, 0, 0))
shape = cyl1.fuse([box1, cyl2]).removeSplitter().cut(cyl3.fuse(cyl4))
connecting_rod = doc.addObject("Part::Feature", "ConnectingRod")
connecting_rod.Shape = shape
connecting_rod.Placement.Base = App.Vector(25, -70, 0)

mat = base.ViewObject.ShapeAppearance[0]
mat.DiffuseColor = (0.80, 0.60, 0.15, 0.0)
base.ViewObject.ShapeAppearance = (mat,)

mat = slider_rod.ViewObject.ShapeAppearance[0]
mat.DiffuseColor = (0.55, 0.70, 0.70, 0.0)
slider_rod.ViewObject.ShapeAppearance = (mat,)

mat = crank.ViewObject.ShapeAppearance[0]
mat.DiffuseColor = (0.70, 0.30, 0.20, 0.0)
crank.ViewObject.ShapeAppearance = (mat,)

mat = connecting_rod.ViewObject.ShapeAppearance[0]
mat.DiffuseColor = (0.55, 0.70, 0.0, 0.0)
connecting_rod.ViewObject.ShapeAppearance = (mat,)

doc.recompute()
view = Gui.ActiveDocument.ActiveView
view.viewIsometric()
view.fitAll()
```

### Add an assembly 

With the <img alt="" src=images/Assembly_CreateAssembly.svg  style="width:24px;"> [Create Assembly](Assembly_CreateAssembly.md) tool add an assembly to the document.

<img alt="" src=images/Assembly_KinematicExample-01.png  style="width:200px;">



*Tree view of Parts and Assembly*

### Move the parts into the assembly 

In the [Tree view](Tree_view.md) drag and drop the parts on the Assembly object. They can now be handled by the Assembly\'s solver.

<img alt="" src=images/Assembly_KinematicExample-02.png  style="width:200px;">



*The Parts are in the Assembly container now*

### Ground a part 

To keep the assembly at the desired position, the base part should be locked, or grounded as it is called here. Select the Base in the [Tree view](Tree_view.md) or in the [3D view](3D_view.md) and use the <img alt="" src=images/Assembly_ToggleGrounded.svg  style="width:24px;"> [Toggle grounded](Assembly_ToggleGrounded.md) tool. This fixes the position of the Base in relation to the local coordinate system (LCS) of the Assembly container. A GroundedJoint object is added to the Joints container.

<img alt="" src=images/Assembly_KinematicExample-03.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly_KinematicExample-04.png  style="width:240px;">



*Expand the Joints container to find the GroundedJoint object*

### Alternative: Insert Link 

Instead of the two steps mentioned above it is also possible to use the <img alt="" src=images/Assembly_InsertLink.svg  style="width:24px;"> [Insert Link](Assembly_InsertLink.md) tool to place objects inside an assembly. The first object automatically becomes the grounded part. So you need to start with the Base object. The tool creates links and the original objects remain outside the assembly. To avoid confusion it is advisable to make them invisible.

### Apply joints 

A joint connects exactly two elements of different parts. They can optionally be selected before the desired joint tool is invoked (any number of selected elements other than two results in an empty selection). The elements define the position and orientation of a LCS represented by a filled circle on the local XY plane and three lines along the local X (red), Y (green), and Z (blue) axes.

-   A Revolute joint between Base and Crank

<img alt="" src=images/Assembly_KinematicExample-05.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly_KinematicExample-06.png  style="width:200px;">



*Selected elements + <img src="images/Assembly_CreateJointRevolute.svg" width=24px> [Create Revolute Joint](Assembly_CreateJointRevolute.md) → rearranged Crank*

Move the **Crank** using the left mouse button. Only a rotation around the pivot should be possible.

-   A Slider joint between Base and Slider Rod

<img alt="" src=images/Assembly_KinematicExample-07.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly_KinematicExample-08.png  style="width:200px;">



*Selected elements + <img src="images/Assembly_CreateJointSlider.svg" width=24px> [Create Slider Joint](Assembly_CreateJointSlider.md) → rearranged Slider Rod*

Move the **SliderRod** using the left mouse button. Only a displacement along its centerline should be possible.

-   A Revolute joint between Crank and Connecting Rod

<img alt="" src=images/Assembly_KinematicExample-09.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly_KinematicExample-10.png  style="width:200px;">



*Selected elements + <img src="images/Assembly_CreateJointRevolute.svg" width=24px> [Create Revolute Joint](Assembly_CreateJointRevolute.md) → rearranged Connecting Rod*

Move the **ConnectingRod** using the left mouse button. Only a rotation around the pivot should be possible.

<img alt="" src=images/Assembly_KinematicExample-11.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly_KinematicExample-12.png  style="width:200px;">



*If there are several joints in a line we have to help the solver find a sensible solution.<br>
If required, click and drag the parts into an easier to compute position.*

-   A Cylindrical joint between Connecting Rod and Slider Rod

<img alt="" src=images/Assembly_KinematicExample-13.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly_KinematicExample-14.png  style="width:200px;">



*Selected elements + <img src="images/Assembly_CreateJointCylindrical.svg" width=24px> [Create Cylindrical Joint](Assembly_CreateJointCylindrical.md) → finished Assembly*

In the finished assembly use the mouse pointer to drag the parts according to the used joints.

#### Note

The pin of the Slider Rod is redundantly orientated. Its centerline is parallel to the pin of the Base through the kinematic chain from Base via Crank and Connecting Rod, i.e. its local Z axis cannot rotate around any X or Y axis. The Slider joint also prevents the rotation of its Z axis around two local axes and so results in two redundantly constrained degrees of freedom. A Cylindrical joint instead of the Slider joint would only lock one rotation resulting in only a single redundantly constrained degree of freedom.

### Drive the crank 

To control the layout of the assembly by the angle between the Base and the Crank we have to change the Revolute joint between them to a Fixed joint. To do so double-click the Revolute object in the Tree view. In the dialog change Revolute to Fixed and change the Rotation value as desired (the movement should follow the mouse wheel action).

Note that a joint type change will change the joint\'s Label, but not its Name. In this case the Label is changed to \"Fixed\".

To animate the assembly we can change the Rotation (Offset1.Angle) of the Fixed joint with Python code. Just copy-paste the following lines in the Python console:


```python
import math
import FreeCAD as App
import FreeCADGui as Gui

actuator = App.ActiveDocument.getObjectsByLabel("Fixed")[0]

for angle in range(0, 361, 10):
    # A full rotation of the Crank in steps of 10°
    actuator.Offset1.Rotation.Angle = math.radians(angle)
    App.ActiveDocument.recompute()
    Gui.updateGui()
```

The end of the range must be greater than 360 to also include this angle as a valid result.


</div>


</div>

## Example universal joint 


<div class="mw-collapsible mw-collapsed toccolours">

<img alt="" src=images/Assembly_UniversalJointExample-01.png  style="width:80px;"> This example is temporary and may be removed once proper descriptions/tutorials are available.


<div class="mw-collapsible-content">

### Universal joint assembly 

<img alt="" src=images/Assembly_UniversalJointExample-01.png  style="width:300px;">

In this example a [universal joint](https://en.wikipedia.org/wiki/Universal_joint) is created.

The assembly consists of three solid parts: two identical Forks and a Cross. Two additional non solid elements, Axle1 and Axle2, representing the angled axles, are also needed. The axles and the solid parts are connected with several joints.

### Prepare parts 

In this example all parts and the assembly are created in one document.

The Python code below will create a new document with four objects (only 1 Fork). Just copy-paste the following lines in the [Python console](Python_console.md):


```python
import math
import FreeCAD as App
import FreeCADGui as Gui
import Part

doc = App.newDocument()

axle1 = doc.addObject("Part::Line", "Axle1")
axle1.X2 = -80
axle1.Y2 = 0
axle1.Z2 = 0

axle2 = doc.addObject("Part::Line", "Axle2")
axle2.X2 = 80
axle2.Y2 = 0
axle2.Z2 = 0
axle2.Placement.Rotation.Angle = math.radians(20)

sph1 = Part.makeSphere(50, App.Vector(0, 0, 0), App.Vector(-1, 0, 0), 0, 90, 360)
box1 = Part.makeBox(50, 40, 80, App.Vector(-50, -20, -40))
cyl1 = Part.makeCylinder(20, 80, App.Vector(0, 0, -40))
cyl2 = Part.makeCylinder(20, 80, App.Vector(0, 0, 0), App.Vector(-1, 0, 0))
cyl3 = Part.makeCylinder(30, 60, App.Vector(0, -30, 0), App.Vector(0, 1, 0))
box2 = Part.makeBox(30, 60, 60, App.Vector(0, -30, -30))
cyl4 = Part.makeCylinder(15, 80, App.Vector(0, 0, -40))
cyl5 = Part.makeCylinder(15, 80, App.Vector(0, 0, 0), App.Vector(-1, 0, 0))
shape = sph1.common(box1).fuse([cyl1, cyl2]).cut(cyl3.fuse([box2, cyl4, cyl5]))
fork = doc.addObject("Part::Feature", "Fork")
fork.Shape = shape.removeSplitter()
fork.Placement.Base = App.Vector(0, 100, 0)

cyl1 = Part.makeCylinder(15, 80, App.Vector(0, 0, -40))
cyl2 = Part.makeCylinder(15, 80, App.Vector(0, -40, 0), App.Vector(0, 1, 0))
shape = cyl1.fuse([cyl2])
cross = doc.addObject("Part::Feature", "Cross")
cross.Shape = shape.removeSplitter()
cross.Placement.Base = App.Vector(70, 100, 0)

mat = fork.ViewObject.ShapeAppearance[0]
mat.DiffuseColor = (0.80, 0.60, 0.15, 0.0)
fork.ViewObject.ShapeAppearance = (mat,)

mat = cross.ViewObject.ShapeAppearance[0]
mat.DiffuseColor = (0.55, 0.70, 0.70, 0.0)
cross.ViewObject.ShapeAppearance = (mat,)

doc.recompute()
view = Gui.ActiveDocument.ActiveView
view.viewIsometric()
view.fitAll()
```

### Change angle of axles 

The angle between the axles is set to 20 degrees. If you want to change this value select Axle2 and change the Placement.Angle property. This property must be changed before moving Axle2 into the assembly.

Warning: parts may collide if the angle is too large.

### Add an assembly 

With the <img alt="" src=images/Assembly_CreateAssembly.svg  style="width:24px;"> [Create Assembly](Assembly_CreateAssembly.md) tool add an assembly to the document.

### Move the axles into the assembly 

In the [Tree view](Tree_view.md) drag and drop the axles on the Assembly object.

### Ground the axles 

Select the two axles in the Tree view and use the <img alt="" src=images/Assembly_ToggleGrounded.svg  style="width:24px;"> [Toggle grounded](Assembly_ToggleGrounded.md) tool.

### Move the solids into the assembly 

For the other objects we will use the <img alt="" src=images/Assembly_InsertLink.svg  style="width:24px;"> [Insert Component](Assembly_InsertLink.md) tool:

1.  Invoke the tool.
2.  In the dialog that opens click the Cross object once, and the Fork object twice.
3.  Press the **OK** button.
4.  Make the objects outside the assembly invisible.
5.  If the objects inside the assembly overlap too much you can drag them to a new position.

### Apply joints 

-   A Revolute joint between Axle1 and Fork001

<img alt="" src=images/Assembly_UniversalJointExample-02.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly_UniversalJointExample-03.png  style="width:200px;">



*Selected elements + <img src="images/Assembly_CreateJointRevolute.svg" width=24px> [Create Revolute Joint](Assembly_CreateJointRevolute.md) + Offset of +40mm or -40mm → rearranged Fork001*

If you invoke the tool first and then select the elements, you can click near the correct endpoint of Axle1 to avoid having to enter an offset.

-   A Cylindrical joint between Fork001 and Cross001

<img alt="" src=images/Assembly_UniversalJointExample-04.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly_UniversalJointExample-05.png  style="width:200px;">



*Selected elements + <img src="images/Assembly_CreateJointCylindrical.svg" width=24px> [Create Cylindrical Joint](Assembly_CreateJointCylindrical.md) → rearranged Cross001*

-   A Cylindrical joint between Axle2 and Fork002

<img alt="" src=images/Assembly_UniversalJointExample-06.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly_UniversalJointExample-07.png  style="width:200px;">



*Selected elements + <img src="images/Assembly_CreateJointCylindrical.svg" width=24px> [Create Cylindrical Joint](Assembly_CreateJointCylindrical.md) → rearranged Fork002*

If required reverse the direction of the joint using the **<img src="images/Button_sort.svg" width=16px>** button in the task panel.

-   A Cylindrical joint between Cross001 and Fork002

<img alt="" src=images/Assembly_UniversalJointExample-08.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly_UniversalJointExample-09.png  style="width:200px;">



*Selected elements + <img src="images/Assembly_CreateJointCylindrical.svg" width=24px> [Create Cylindrical Joint](Assembly_CreateJointCylindrical.md) → rearranged Cross001 and Fork002*

### Drive the universal joint 

The universal joint can be driven by moving Fork001 with the left mouse.

If you want to check the situation at distinct rotation angles do the following:

1.  Change the Cylindrical joint between Axle1 and Fork001 to a Fixed joint.
2.  Select the Offset1.Angle property of the Fixed joint and roll the mouse wheel.
3.  The universal joint may be positioned to any angle.


</div>


</div>

## Example vise 


<div class="mw-collapsible mw-collapsed toccolours">

<img alt="" src=images/Assembly_ViseExample-01.png  style="width:80px;"> This example is temporary and may be removed once proper descriptions/tutorials are available.


<div class="mw-collapsible-content">

### Assembly of a vise 

<img alt="" src=images/Assembly_ViseExample-01.png  style="width:300px;">

In this example a [vise](https://en.wikipedia.org/wiki/Vise) is created.

The assembly consists of three solid parts: a fixed and a movable jaw and a screw with a lever. One additional non solid element, a crank, is also needed. The crank and the solid parts are connected with several joints.

A Screw Joint couples the translation of a part with a Slider Joint to the rotation of a part with a Revolute Joint. The screw part shall make both a translation and a rotation movement hence it must be a part with a Cylindrical Joint. In this assembly, the screw part will be coupled to the movable jaw with a Distance Joint, to the non solid crank with a Parallel Joint, and to the fixed jaw with a Cylindrical Joint.

### Prepare parts 

In this example all parts and the assembly are created in one document.

The Python code below will create a new document with four objects. Just copy-paste the following lines in the [Python console](Python_console.md):


```python
import math
import FreeCAD as App
import FreeCADGui as Gui
import Part

doc = App.newDocument()

box1 = Part.makeBox(95, 40, 75, App.Vector(0, -20, -22))
cyl1 = Part.makeCylinder(35, 80, App.Vector(0, -40, 53), App.Vector(0, 1, 0), 90)
box2 = Part.makeBox(20, 80, 30, App.Vector(-20, -40, 58))
cyl2 = Part.makeCylinder(15, 80, App.Vector(-15, -40, 58), App.Vector(0, 1, 0), 90)
box3 = Part.makeBox(5, 80, 15, App.Vector(-20, -40, 58))
box4 = Part.makeBox(35, 24, 24, App.Vector(0, -12, -12))
box5 = Part.makeBox(60, 34, 69, App.Vector(35, -17, -19))
cyl3 = Part.makeCylinder(20, 55, App.Vector(-20, -40, 53), App.Vector(1, 0, 0))
cyl4 = Part.makeCylinder(20, 55, App.Vector(-20, 40, 53), App.Vector(1, 0, 0))
cyl5 = Part.makeCylinder(5, 35, App.Vector(0, 0, 38), App.Vector(1, 0, 0))
box6 = Part.makeBox(7, 88, 15, App.Vector(-22, -44, 75))
box7 = Part.makeBox(95, 90, 10, App.Vector(0, -45, -32))
shape = box1.fuse([cyl1, box2, box6, box7]).cut(cyl2.fuse([box3, cyl3, cyl4, cyl5, box4, box5]))
fixedJaw = doc.addObject("Part::Feature", "FixedJaw")
fixedJaw.Shape = shape.removeSplitter()
fixedJaw.Placement.Rotation.Axis = App.Vector(0, 0, 1)
fixedJaw.Placement.Rotation.Angle = math.radians(180)

box1 = Part.makeBox(35, 40, 75, App.Vector(0, -20, -22))
cyl1 = Part.makeCylinder(35, 80, App.Vector(0, -40, 53), App.Vector(0, 1, 0), 90)
box2 = Part.makeBox(20, 80, 30, App.Vector(-20, -40, 58))
cyl2 = Part.makeCylinder(15, 80, App.Vector(-15, -40, 58), App.Vector(0, 1, 0), 90)
box3 = Part.makeBox(160, 24, 24, App.Vector(-160, -12, -12))
box4 = Part.makeBox(5, 80, 15, App.Vector(-20, -40, 58))
box5 = Part.makeBox(160, 18, 18, App.Vector(-160, -9, -9))
cyl3 = Part.makeCylinder(20, 55, App.Vector(-20, -40, 53), App.Vector(1, 0, 0))
cyl4 = Part.makeCylinder(20, 55, App.Vector(-20, 40, 53), App.Vector(1, 0, 0))
cyl5 = Part.makeCylinder(5, 35, App.Vector(0, 0, 38), App.Vector(1, 0, 0))
box6 = Part.makeBox(7, 88, 15, App.Vector(-22, -44, 75))
shape = box1.fuse([cyl1, box2, box3, box6]).cut(cyl2.fuse([box4, cyl3, cyl4, box5, cyl5]))
movableJaw = doc.addObject("Part::Feature", "MovableJaw")
movableJaw.Shape = shape.removeSplitter()
movableJaw.Placement.Base = App.Vector(150, 100, 0)

cyl1 = Part.makeCylinder(5, 190, App.Vector(0, 0, 0), App.Vector(1, 0, 0))
cyl2 = Part.makeCylinder(10, 20, App.Vector(190, 0, 0), App.Vector(1, 0, 0))
cyl3 = Part.makeCylinder(4, 100, App.Vector(200, 0, -50), App.Vector(0, 0, 1))
shape = cyl1.fuse([cyl2, cyl3])
leverScrew = doc.addObject("Part::Feature", "LeverScrew")
leverScrew.Shape = shape.removeSplitter()
leverScrew.Placement.Base = App.Vector(150, -100, 0)

wire1 = Part.makePolygon([App.Vector(0, 0, 100), App.Vector(0, 0, 0), App.Vector(100, 0, 0)])
crank = doc.addObject("Part::Feature", "Crank")
crank.Shape = wire1
crank.Placement.Base = App.Vector(0, -100, 0)

mat = fixedJaw.ViewObject.ShapeAppearance[0]
mat.DiffuseColor = (0.80, 0.60, 0.15, 0.0)
fixedJaw.ViewObject.ShapeAppearance = (mat,)

mat = movableJaw.ViewObject.ShapeAppearance[0]
mat.DiffuseColor = (0.55, 0.70, 0.70, 0.0)
movableJaw.ViewObject.ShapeAppearance = (mat,)

mat = leverScrew.ViewObject.ShapeAppearance[0]
mat.DiffuseColor = (0.70, 0.30, 0.20, 0.0)
leverScrew.ViewObject.ShapeAppearance = (mat,)

doc.recompute()
view = Gui.ActiveDocument.ActiveView
view.viewIsometric()
view.fitAll()
```

### Add an assembly 

With the <img alt="" src=images/Assembly_CreateAssembly.svg  style="width:24px;"> [Create Assembly](Assembly_CreateAssembly.md) tool add an assembly to the document.

### Move the parts into the assembly container 

In the [Tree view](Tree_view.md) drag and drop the parts on the Assembly object. They can now be handled by the Assembly\'s solver.

### Ground a part 

To keep the assembly at the desired position, the FixedJaw part should be locked, or grounded as it is called here. Select the FixedJaw in the [Tree view](Tree_view.md) or in the [3D view](3D_view.md) and use the <img alt="" src=images/Assembly_ToggleGrounded.svg  style="width:24px;"> [Toggle grounded](Assembly_ToggleGrounded.md) tool. A GroundedJoint object is added to the Joints container.

### Apply joints 

-   A Revolute joint between FixedJaw and Crank

<img alt="" src=images/Assembly_ViseExample-02.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly_ViseExample-03.png  style="width:200px;">



*Selected elements + <img src="images/Assembly_CreateJointRevolute.svg" width=24px> [Create Revolute Joint](Assembly_CreateJointRevolute.md) → rearranged Crank*

-   A Slider joint between FixedJaw and MovableJaw

<img alt="" src=images/Assembly_ViseExample-04.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly_ViseExample-05.png  style="width:200px;">



*Selected elements + <img src="images/Assembly_CreateJointSlider.svg" width=24px> [Create Slider Joint](Assembly_CreateJointSlider.md) → rearranged MovableJaw*

Set the Min length to -77 mm and the Max length to -7 mm. This limits the opening of the vise to 70 mm.

The next three joints are necessary to force the LeverScrew to: translate like the MovableJaw, rotate like the Crank, and rotate around the main axis.

-   A Distance joint between LeverScrew and MovableJaw

<img alt="" src=images/Assembly_ViseExample-06.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly_ViseExample-07.png  style="width:200px;">



*Selected elements + <img src="images/Assembly_CreateJointDistance.svg" width=24px> [Create Distance Joint](Assembly_CreateJointDistance.md) → rearranged LeverScrew*

Select two faces. Set the distance value to 20 mm.

-   A Parallel joint between LeverScrew and Crank

<img alt="" src=images/Assembly_ViseExample-08.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly_ViseExample-09.png  style="width:200px;">



*Selected elements + <img src="images/Assembly_CreateJointParallel.svg" width=24px> [Create Parallel Joint](Assembly_CreateJointParallel.md) → rearranged LeverScrew*

-   A Cylindrical joint between LeverScrew and FixedJaw

<img alt="" src=images/Assembly_ViseExample-10.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly_ViseExample-11.png  style="width:200px;">



*Selected elements + <img src="images/Assembly_CreateJointCylindrical.svg" width=24px> [Create Cylindrical Joint](Assembly_CreateJointCylindrical.md) → rearranged LeverScrew*

-   A Screw joint between MovableJaw and Crank

<img alt="" src=images/Assembly_ViseExample-12.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly_ViseExample-13.png  style="width:200px;">



*Selected elements (LeverScrew invisible) + <img src="images/Assembly_CreateJointScrew.svg" width=24px> [Create Screw Joint](Assembly_CreateJointScrew.md) → complete vise mechanism (LeverScrew visible)*

If necessary make the LeverScrew invisible during selection.

Set the Pitch radius to 5 mm

### Drive the vise 

The vise can be driven by moving Crank or MovableJaw with the left mouse.


</div>


</div>

## Example shock absorber 


<div class="mw-collapsible mw-collapsed toccolours">

<img alt="" src=images/Assembly_ShockAbsorberExample-01.png  style="width:80px;"> This example is temporary and may be removed once proper descriptions/tutorials are available.


<div class="mw-collapsible-content">

### Assembly of a shock absorber 

<img alt="" src=images/Assembly_ShockAbsorberExample.gif  style="width:300px;">

In this example a [shock absorber](https://en.wikipedia.org/wiki/Shock_absorber) is created.

The assembly consists of three solid parts: a piston, a cylinder and a spring. Three additional non solid elements, two axles and a rod are also needed. All parts are connected with several joints.

The hinge of the piston rotates around Axle2, while the hinge of the cylinder moves on an arc of circle centered on Axle1. The non solid Rod is used for this movement. The length of the Rod is the radius of the arc.

### Prepare parts 

The Python code below will create a new document with 6 objects. Create a new [macro](Macros.md) and copy-paste the code below in the Python editor (not in the Python console). Then [run the macro](Std_DlgMacroExecuteDirect.md).

The code below cannot be run from the Python console because the spring must be a [Part::FeaturePython](App_FeaturePython.md) object defined by of a class with the callback functions {{Incode|execute()}} and {{Incode|onChanged()}}. Only then can its height be changed via a property.


```python
import math
import FreeCAD as App
import FreeCADGui as Gui
import Part

doc = App.newDocument()

class Spring():
    def __init__(self, spring):
        spring.addProperty("App::PropertyLength", "Height", "Spring", "Height of the helix").Height = 200.0
        spring.Proxy = self
        spring.ViewObject.Proxy = 0
        
    def execute(self, spring):
        helix = Part.makeHelix(spring.Height/8.5, spring.Height, 35)
        startPnt = helix.Edges[0].Curve.value(0)
        section = Part.Wire([Part.Circle(startPnt, App.Vector(0, 1, 0), 5).toShape()])
        hel1 = helix.makePipeShell([section], True, True)
        box1 = Part.makeBox(80, 80, 10, App.Vector(-40, -40, -10))
        box2 = Part.makeBox(80, 80, 10, App.Vector(-40, -40, spring.Height))
        shape = hel1.cut(box1).cut(box2)
        spring.Shape = shape
        
    def onChanged(self, spring, prop):
        if prop == "Height":
            self.execute(spring) 
            
spring = doc.addObject("Part::FeaturePython", "Spring")
Spring(spring)
spring.Placement.Base = App.Vector(0, 100, 0)

axle1 = doc.addObject("Part::Line", "Axle1")
axle1.X2 = 0
axle1.Y2 = 80
axle1.Z2 = 0

axle2 = doc.addObject("Part::Line", "Axle2")
axle2.X2 = 0
axle2.Y2 = 80
axle2.Z2 = 0
axle2.Placement.Base = App.Vector(120, 0, -250)

rod = doc.addObject("Part::Line", "Rod")
rod.X2 = 100
rod.Y2 = 0
rod.Z2 = 0
rod.Placement.Base = App.Vector(0, -50, 0)

cyl1 = Part.makeCylinder(40, 10,App.Vector(0, 0, -5))
tor1 = Part.makeTorus(40, 5)
cyl2 = Part.makeCylinder(45, 5)
box1 = Part.makeBox(30, 10, 30,App.Vector(-15, -5, -35))
cyl3 = Part.makeCylinder(15, 10, App.Vector(0, -5, -35), App.Vector(0, 1, 0))
cyl4 = Part.makeCylinder(40, 5)
cyl5 = Part.makeCylinder(5, 10,App.Vector(0, -5, -35), App.Vector(0, 1, 0))
cyl6 = Part.makeCylinder(5, 130)
cyl7 = Part.makeCylinder(20, 5,App.Vector(0, 0, 130))
shape = cyl1.fuse([tor1,cyl2, box1, cyl3]).cut(cyl4.fuse([cyl5])).fuse([cyl6, cyl7])
piston = doc.addObject("Part::Feature", "Piston")
piston.Shape = shape.removeSplitter()
piston.Placement.Base = App.Vector(200, 100, -200)

cyl1 = Part.makeCylinder(40, 10,App.Vector(0, 0, -5))
tor1 = Part.makeTorus(40, 5)
cyl2 = Part.makeCylinder(45, 5)
box1 = Part.makeBox(30, 10, 30,App.Vector(-15, -5, -35))
cyl3 = Part.makeCylinder(15, 10,App.Vector(0, -5, -35), App.Vector(0, 1, 0))
cyl4 = Part.makeCylinder(40, 5)
cyl5 = Part.makeCylinder(5, 10,App.Vector(0, -5, -35), App.Vector(0, 1, 0))
cyl6 = Part.makeCylinder(25, 130)
tor2 = Part.makeTorus(20, 5,App.Vector(0, 0, 130))
cyl7 = Part.makeCylinder(20, 135)
cyl8 = Part.makeCylinder(20, 130)
cyl9 = Part.makeCylinder(5, 135)
shape = cyl1.fuse([tor1, cyl2, box1, cyl3]).cut(cyl4.fuse([cyl5])).fuse([cyl6, tor2, cyl7]).cut(cyl8.fuse([cyl9]))
cylinder = doc.addObject("Part::Feature", "Cylinder")
cylinder.Shape = shape.removeSplitter()
cylinder.Placement.Rotation.Axis = App.Vector(0, 1, 0)
cylinder.Placement.Rotation.Angle = math.pi
cylinder.Placement.Base = App.Vector(100, 100, 0)

mat = piston.ViewObject.ShapeAppearance[0]
mat.DiffuseColor = (0.80, 0.60, 0.15, 0.0)
piston.ViewObject.ShapeAppearance = (mat,)

mat = cylinder.ViewObject.ShapeAppearance[0]
mat.DiffuseColor = (0.55, 0.70, 0.70, 0.0)
cylinder.ViewObject.ShapeAppearance = (mat,)

doc.recompute()
view = Gui.ActiveDocument.ActiveView
view.viewIsometric()
view.fitAll()
```

### Add an assembly 

With the <img alt="" src=images/Assembly_CreateAssembly.svg  style="width:24px;"> [Create Assembly](Assembly_CreateAssembly.md) tool add an assembly to the document.

### Move the parts into the assembly container 

In the [Tree view](Tree_view.md) drag and drop the parts on the Assembly object. They can now be handled by the Assembly\'s solver.

### Ground the two axles 

To keep the assembly at the desired position, the two axles should be locked, or grounded as it is called here. Select the two axles in the [Tree view](Tree_view.md) or in the [3D view](3D_view.md) and use the <img alt="" src=images/Assembly_ToggleGrounded.svg  style="width:24px;"> [Toggle grounded](Assembly_ToggleGrounded.md) tool. Two GroundedJoint objects are added to the Joints container.

### Apply joints 

-   A Revolute joint between Axle2 and Piston

<img alt="" src=images/Assembly_ShockAbsorberExample-02.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly_ShockAbsorberExample-03.png  style="width:200px;">



*<img src="images/Assembly_CreateJointRevolute.svg" width=24px> [Create Revolute Joint](Assembly_CreateJointRevolute.md) + Selected elements → rearranged Piston*

-   A Slider joint between Piston and Cylinder

<img alt="" src=images/Assembly_ShockAbsorberExample-04.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly_ShockAbsorberExample-05.png  style="width:200px;">



*<img src="images/Assembly_CreateJointSlider.svg" width=24px> [Create Slider Joint](Assembly_CreateJointSlider.md) + Selected elements → rearranged and moved Cylinder*

Please pay attention to the location of the coordinate system before selecting a face. It should be in the center of each face.

Drag the Cylinder to create some distinct between it and the Piston. The supporting faces for the Spring should be visible.

-   A Distance joint between Piston and Cylinder

<img alt="" src=images/Assembly_ShockAbsorberExample-06A.png  style="width:200px;"> <img alt="" src=images/List-add.svg  style="width:16px;"> <img alt="" src=images/Assembly_ShockAbsorberExample-06B.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly_ShockAbsorberExample-07.png  style="width:200px;">



*<img src="images/Assembly_CreateJointDistance.svg" width=24px> [Create Distance Joint](Assembly_CreateJointDistance.md) + Selected faces → rearranged Cylinder Distance set to 200 mm*

Set the distance value to 200 mm.

The next two joints are necessary to force the hinge of the Cylinder to move on an arc of circle.

-   A Cylindrical joint between Axle1 and Rod

<img alt="" src=images/Assembly_ShockAbsorberExample-08.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly_ShockAbsorberExample-09.png  style="width:200px;">



*<img src="images/Assembly_CreateJointCylindrical.svg" width=24px> [Create Cylindrical Joint](Assembly_CreateJointCylindrical.md) + Selected elements → rearranged Rod*

Make sure the Z axis of the coordinate system (blue) is perpendicular to the Rod by selecting an endpoint.

-   A Revolute joint between Rod and Cylinder

<img alt="" src=images/Assembly_ShockAbsorberExample-10.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly_ShockAbsorberExample-11.png  style="width:200px;">



*<img src="images/Assembly_CreateJointRevolute.svg" width=24px> [Create Revolute Joint](Assembly_CreateJointRevolute.md) + Selected elements → rearranged Cylinder*

Again make sure the Z axis of the coordinate system (blue) is perpendicular to the Rod.

You may encounter problems with this joint. If that is the case try the following:

1.  Delete the joint.
2.  Switch to the [front view](Std_ViewFront.md).
3.  Rotate the assembly (by dragging the Piston) and rotate the Rod so that center of the hinge hole of the Cylinder lies on the Rod.
4.  Create the joint again.

The next two joints are necessary to fix the Spring to the support face.

-   A Parallel joint between Spring and Piston

<img alt="" src=images/Assembly_ShockAbsorberExample-12A.png  style="width:200px;"> <img alt="" src=images/List-add.svg  style="width:16px;"> <img alt="" src=images/Assembly_ShockAbsorberExample-12B.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly_ShockAbsorberExample-13.png  style="width:200px;">



*<img src="images/Assembly_CreateJointParallel.svg" width=24px> [Create Parallel Joint](Assembly_CreateJointParallel.md) + Selected faces → rearranged Spring*

Select the center of the support face on the Piston and the center of the bottom face of the spring. Keep the distance value 0.

-   A Fixed joint between Spring and Piston

<img alt="" src=images/Assembly_ShockAbsorberExample-14A.png  style="width:200px;"> <img alt="" src=images/List-add.svg  style="width:16px;"> <img alt="" src=images/Assembly_ShockAbsorberExample-14B.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly_ShockAbsorberExample-15.png  style="width:200px;">



*<img src="images/Assembly_CreateJointFixed.svg" width=24px> [Create Fixed Joint](Assembly_CreateJointFixed.md) + Selected elements → rearranged Spring*

Select the bottom vertex of the cylinder\'s seam in the Piston and the corner vertex in the Spring.

-   Connect the distance property of the **Distance** joint to the Spring\'s **Height** property using an [expression](Expressions.md):

1.  Select the Spring in the [Tree view](Tree_view.md).
2.  Select the blue icon <img alt="" src=images/Bound-expression.svg  style="width:16px;"> in the Height property field.
3.  Enter in the expression editor: {{Incode|<<Distance>>.Distance}}

### Drive the shock absorber 

To do so double-click the Distance object in the Tree view and change its Distance property. Recompute the document. The spring changes its length.


</div>


</div>





{{Assembly_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > Assembly Workbench/en
