# Sketcher Examples
## Introduction

I think the <img alt="" src=images/Workbench_Sketcher.svg  style="width:24px;"> [Sketcher Workbench](Sketcher_Workbench.md) needs some examples that are not detailed tutorials or videos\...

## Film hinge 

A film hinge is the tiny piece of bendable plastic that connects the two sides of an injection moulded object such as a conduit with a lid, or both halves of a dust protecting plug enclosure.

This example uses some kind of master sketch to stack some dependent sketches upon it. It also shows how to attach and animate a simple clip based on <img alt="" src=images/Workbench_PartDesign.svg  style="width:16px;"> [PartDesign](PartDesign_Workbench.md) features and <img alt="" src=images/Workbench_Sketcher.svg  style="width:16px;"> [Sketcher](Sketcher_Workbench.md) constraints. The use of <img alt="" src=images/Bound-expression.svg  style="width:16px;"> [expressions](Expressions.md) as described below requires FreeCAD **V 0.21 or higher**.

### Basic sketch 

Usually an object is modelled in closed condition. Later the moving part has to be flipped over by 180° to be moulded in open condition.
The bendable strip is represented by a circular arc for the closed condition and by a straight line for the open condition both having the same start point.
The midpoint of a line connecting both end points indicates the position of the flipping axis, which is normal to the sketch plane. (It is placed on the sketch origin so that the global axis standing normal to the sketch plane can be used as flipping axis)


<div class="mw-collapsible mw-collapsed">

(Some hidden extra explanation and workflow description can be expanded over there \--\>

 <img alt="" src=images/Sketcher_ExampleHinge-01.gif  style="width:400px;">  
*Master sketch and the animated final film hinge (click on the image if the animation has stopped after some repetitions)*


<div class="mw-collapsible-content toccolours">

For a semi circle, the arc length is the radius multiplied by Pi (**l = r \* Pi**). The radius is named NeutralRadius and the line is called DevelopedLength. An expression for the DevelopedLength relates both values: `.Constraints.NeutralRadius * pi`

:   Within the same sketch an expression starts with a `.` followed by ValueType.ValueName to address another value.


</div>

### Intermediate sketch 

The arc of this film hinge has a constant length and a variable radius. One input is the NeutralRadius of the basic sketch; to have it at hand in this sketch, it is linked as <img alt="" src=images/Sketcher_External.svg  style="width:16px;"> [external geometry](Sketcher_External.md) having a reference dimension called ReferenceRadius


<div class="mw-collapsible-content toccolours">

A pie segment of construction geometry displays the relation between the arc and the radius for a given angle.
**InputLength = ReferenceRadius \* Pi**
and
**ArcLength = DynamicRadius \* Pi \* ArcAngle / 180°**
with constant length results in:
**ReferenceRadius \* Pi = DynamicRadius \* Pi \* ArcAngle / 180°**
And with Pi eliminated we get:
**ReferenceRadius = DynamicRadius \* ArcAngle / 180°** or **DynamicRadius = ReferenceRadius \* 180° / ArcAngle**

:   The <img alt="" src=images/Bound-expression.svg  style="width:16px;"> [expression](Expressions.md) for the DynamicRadius value: `.Constraints.ReferenceRadius * 180 ° / .Constraints.ArcAngle`

A film hinge is usually symmetric and so another arc with the same center point called HalfArc is used for the output and represents one half of the hinge arc.

:   The <img alt="" src=images/Bound-expression.svg  style="width:16px;"> [expression](Expressions.md) for the HalfArc value: `.Constraints.ArcAngle / 2`


</div>

 <img alt="" src=images/Sketcher_ExampleHinge-02.png  style="width:400px;">  
*Intermediate sketch showing the DynamicRadius of the hinge arc of 4 (mm) at a given angle of 45° (and the half arc for output)*

### Film hinge sketch 

This sketch defines the thickness and the adjacent geometry of the film hinge. Therefore we load the half arc of the intermediate sketch as external geometry to use it as the base for the film part. (a fraction of 180° in this case)

This film hinge is intended to keep the connected parts touching each other when closed. This can be achieved by calculating a circular arc of the needed length then create a strip with constant thickness and finally apply fillets where the strip meets the object halves. The last step somehow shortens the loop, but in the real world this is not a problem, because the arc will never be circular and so the fillets have an influence on the arc\'s curvature but not on its functionality.

 <img alt="" src=images/Sketcher_ExampleHinge-03.png  style="width:400px;">  
*Hinge sketch showing the outline of the hinge based on the external geometry from the half arc of the intermediate sketch*

 <img alt="" src=images/Sketcher_ExampleHinge-04.png  style="width:300px;"> <img alt="" src=images/Sketcher_ExampleHinge-05.png  style="width:300px;">  
*Left: <img src="images/PartDesign_Pad.svg" width=16px> [padded](PartDesign_Pad.md) half hinge with sketch visible. Right: half hinge with added <img src="images/PartDesign_Fillet.svg" width=16px> [fillet](PartDesign_Fillet.md)*

 <img alt="" src=images/Sketcher_ExampleHinge-06.png  style="width:300px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Sketcher_ExampleHinge-07.png  style="width:300px;">  
*Half hinge with selected mirror plane → <img src="images/PartDesign_Mirrored.svg" width=16px> [mirrored](PartDesign_Mirrored.md) film hinge*

Hint: <img alt="" src=images/Part_Mirror.svg  style="width:16px;"> [Part Mirror](Part_Mirror.md) only accepts the three basic planes and so can not be used in such a case.

:   (In retrospect it was a wise decision to start this example with the combination of PartDesign and Sketcher.)

Finally two parameters define the size of the film hinge:

-   the NeutralRadius of the basic sketch
-   the thickness value of the film hinge sketch

### Bending the film hinge 

The bend angle is controlled by the constraint ArcAngle of the intermediate sketch and can be altered in its property editor.
But we are proper designers and have named our sketches constraints and dimensions properly and so can address the controlling angle via Python.
Some basic lines of code to be embedded in a GUI context could look like this:

 
```python
doc=App.ActiveDocument
sketch=doc.getObjectsByLabel('IntermediateSketch')[0]
 ...
sketch.getDatum('ArcAngle')
 ...
sketch.setDatum('ArcAngle',App.Units.Quantity('50.000000 deg'))
doc.recompute(None,True,True)
```


<div class="mw-collapsible-content toccolours">

A short explanation:

-    {{Incode|doc {{=}}App.ActiveDocument}}: To address the active document by an alias called **doc**

-    {{Incode|sketch {{=}}doc.getObjectsByLabel(\'IntermediateSketch\')\[0\]}}: To address the relevant sketch by the alias **sketch**.

    :   The method **getObjectsByLabel()** returns a list of objects and we have to suffix index {{value|0}} to pick the first object in the list. (We do not expect any other object having the same label and so do not have to care about other items in the list.)

-    {{Incode|sketch.getDatum('ArcAngle')}}: Returns the current value of the dimensional constraint **ArcAngle** (to the Report view)

-    {{Incode|sketch.setDatum('ArcAngle', App.Units.Quantity('50.0 deg'))}}: Sets the value of **ArcAngle** to {{value|50°}}

-    {{Incode|doc.recompute(None,True,True)}}: To update the whole document to show the changes of dependant geometry as well.


</div>

### Connecting geometry 

Two halves of a clip stuff are waiting to get attached to the hinge, one on the static side and one on the movable side.

 <img alt="" src=images/Sketcher_ExampleHinge-08.png  style="width:300px;">  
*Two halves of a simple clip*


<div class="mw-collapsible-content toccolours">

The static side is easy:

1.  Activate the body and adjust the position and orientation properties in the properties editor until it matches with the film hinge.
2.  Activate the hinge body.
3.  Select the <img alt="" src=images/PartDesign_Boolean.svg  style="width:16px;"> [PartDesign Boolean](PartDesign_Boolean.md) tool with the (default) Fuse option.
4.  In the dialog press the **Add body** button.
5.  select the **body** of the static half of the clip.
6.  Press OK to finish and close the dialog.


</div>

 <img alt="" src=images/Sketcher_ExampleHinge-09.png  style="width:300px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Sketcher_ExampleHinge-10.png  style="width:300px;">  
*Film hinge and static half in modelling position → film hinge with relocated and <img src="images/PartDesign_Boolean.svg" width=16px> [fused](PartDesign_Boolean.md) static half*


<div class="mw-collapsible-content toccolours">

But the moving side is different: The related half of the clip geometry has to move into the right position before a (re-) calculation of a Fuse operation gets started.

At this point I\'m missing an \"Attachment with offset\" function like that of Assembly3 to attach the clip geometry to one of the moving faces. But after a bit of experimenting and tweaking I found out:

-   <img alt="" src=images/Std_Part.svg  style="width:16px;"> [Std Part](Std_Part.md) and <img alt="" src=images/PartDesign_Body.svg  style="width:16px;"> [PartDesign Body](PartDesign_Body.md) containers are not supported by <img alt="" src=images/Part_EditAttachment.svg  style="width:16px;"> [Part Attachment](Part_EditAttachment#Limitations.md).

:   While it is possible to use Attachment to align them, the attachment won\'t be parametrically linked.

-   Attachment can be applied to a PartDesign feature. This and features depending on it are repositioned according to the base geometry. But!:
    -   Independent PartDesign features won\'t move and so it will change the resulting shape and break it in the end.
    -   We are advised to keep features independent to avoid impacts due to the [Topological naming problem](Topological_naming_problem.md).
-   <img alt="" src=images/PartDesign_Clone.svg  style="width:16px;"> [PartDesign Clone](PartDesign_Clone.md) creates a body with a single feature that can be use with Attachment.

With that in mind, a workflow could look like this:

1.  Select the body of the movable half.
2.  Use the <img alt="" src=images/PartDesign_Clone.svg  style="width:16px;"> [Create a clone](PartDesign_Clone.md) command.
3.  In the new body select the Clone object in the Tree view.
4.  Use the <img alt="" src=images/Part_EditAttachment.svg  style="width:16px;"> [Part Attachment](Part_EditAttachment.md) tool to add attachment properties to the Clone object.
5.  The Attachment dialog opens.
    -   Select a vertex for the origin.
    -   Select an edge for the first direction.
    -   Select an edge for the second direction.
    -   Probe the attachment modes to find the best fitting one.
    -   Tweak rotation and coordinate values until until the geometry is in modelling position again.
6.  Press OK to close the dialog.
7.  With the hinge body still active select the <img alt="" src=images/PartDesign_Boolean.svg  style="width:16px;"> [PartDesign Boolean](PartDesign_Boolean.md) tool.
8.  In the dialog press the **Add body** button.
9.  select the body of the movable half .
10. Press OK to finish and close the dialog.


</div>


</div>

 <img alt="" src=images/Sketcher_ExampleHinge-14.png  style="width:300px;">  
*The movable half will be <img src="images/Part_EditAttachment.svg" width=16px> [attached](Part_EditAttachment.md) to a corner of the movable hinge side (Map Mode OXZ: vertex, edge, edge)*

In retrospect it would have been wiser to provide the attachment geometry with the IntermediateSketch to avoid another source of the [Topological naming problem](Topological_naming_problem.md).

 <img alt="" src=images/Sketcher_ExampleHinge-11.png  style="width:300px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Sketcher_ExampleHinge-12.png  style="width:300px;">  
*The clip so far and the movable half in modelling position → finished clip with <img src="images/Part_EditAttachment.svg" width=16px> [attached](Part_EditAttachment.md) and <img src="images/PartDesign_Boolean.svg" width=16px> [fused](PartDesign_Boolean.md) movable half*

Now the result should be a single solid clip, that can be closed and opened by changing the ArcAngle of the film hinge. Allowed angles: 0.1° to 180°, the film section must not get straight, and more than closed doesn\'t make sense. (At 180° the object may get fused at tangent or overlapping areas, but a little extra gap could help if that is not acceptable.)

 <img alt="" src=images/Sketcher_ExampleHinge-13.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Sketcher_ExampleHinge-15.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Sketcher_ExampleHinge-16.png  style="width:200px;">  
*Clip almost closed → Clip half closed → Clip in mould condition*

 {{PartDesign Tools navi}} {{Sketcher Tools navi}}



---
⏵ [documentation index](../README.md) > [PartDesign](Category_PartDesign.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher Examples
