# SheetMetal Examples/en
{{TOCright}}

## Introduction

The <img alt="" src=images/Sheetmetal_workbench_icon.svg  style="width   *24px;"> [SheetMetal workbench](SheetMetal_Workbench.md) (an [external workbench](External_workbenches.md) available through the [Addon Manager](Std_AddonMgr.md)) has grown quite powerful and merits to be appropriately documented.

To avoid the overcrowding of the tool pages with examples this page was added to collect parts showing and explaining special SheetMetal features.

Planned phases to generate content   *

1.  Collecting pictures
2.  Adding workflow descriptions
3.  Adding more detailed tutorials

## Hinge

<img alt="" src=images/SheetMetal_Example-01.png  style="width   *400px;">
<img alt="" src=images/SheetMetal_Example-01a.png  style="width   *200px;"> <img alt="" src=images/SheetMetal_Example-01b.png  style="width   *200px;"> <img alt="" src=images/SheetMetal_Example-01c.png  style="width   *200px;"> <img alt="" src=images/SheetMetal_Example-01d.png  style="width   *200px;"> 
*Workflow Hinge   *
**<img src="images/SheetMetal_AddBase.svg" width=16px> [Make Base Wall](SheetMetal_AddBase.md)*,
{{Button|<img src="images/PartDesign_Pocket.svg" width=16px> [PartDesign Pocket](PartDesign_Pocket.md)**,
**<img src="images/PartDesign_Hole.svg" width=16px> [PartDesign Hole](PartDesign_Hole.md)**,
**<img src="images/SheetMetal_Unfold.svg" width=16px> [Unfold](SheetMetal_Unfold.md)**.
}}


<div class="mw-collapsible mw-collapsed">

### Hinge step by step 


<div class="mw-collapsible-content toccolours">

1.  Create a profile (a line and a tangent arc), preferably using the <img alt="" src=images/Workbench_Sketcher.svg  style="width   *16px;"> [Sketcher Workbench](Sketcher_Workbench.md).
2.  Activate the <img alt="" src=images/SheetMetal_AddBase.svg  style="width   *16px;"> [Make Base Wall](SheetMetal_AddBase.md) command to create a BaseBend object.
3.  Edit the BaseBend object\'s parameters   *
    -   Set **Mid Plane** to `True`to let the profile extend symmetrically to both sides of the sketch plane.
    -   Set **radius** and **thickness** to values of your choice.
4.  Create a cut-out contour with the <img alt="" src=images/Workbench_Sketcher.svg  style="width   *16px;"> [Sketcher Workbench](Sketcher_Workbench.md).
5.  Use the <img alt="" src=images/PartDesign_Pocket.svg  style="width   *16px;"> [PartDesign Pocket](PartDesign_Pocket.md) command to cut off one half of the Round bit.
6.  Create a hole pattern with the <img alt="" src=images/Workbench_Sketcher.svg  style="width   *16px;"> [Sketcher Workbench](Sketcher_Workbench.md).
7.  Use the <img alt="" src=images/PartDesign_Hole.svg  style="width   *16px;"> [PartDesign Hole](PartDesign_Hole.md) command. Avoid the countersink and counterbore options to keep the body unfoldable.
8.  Activate the <img alt="" src=images/SheetMetal_Unfold.svg  style="width   *16px;"> [Unfold](SheetMetal_Unfold.md) command to get an Unfold object.
9.  Done!


</div>


</div>

## Paper clip 

<img alt="" src=images/SheetMetal_Example-02.png  style="width   *400px;">
<img alt="" src=images/SheetMetal_Example-02a.png  style="width   *200px;"> <img alt="" src=images/SheetMetal_Example-02b.png  style="width   *200px;"> <img alt="" src=images/SheetMetal_Example-02c.png  style="width   *200px;"> <img alt="" src=images/SheetMetal_Example-02d.png  style="width   *200px;"> 
*Workflow Paper Clip   *
**<img src="images/SheetMetal_AddBase.svg" width=16px> [Make Base Wall](SheetMetal_AddBase.md)*,
{{Button|<img src="images/SheetMetal_SketchOnSheet.svg" width=16px> [Sketch on Sheet](SheetMetal_SketchOnSheet.md)**,
clone, flip and fuse,
**<img src="images/SheetMetal_Unfold.svg" width=16px> [Unfold](SheetMetal_Unfold.md)**.
}}


<div class="mw-collapsible mw-collapsed">

### Paper clip step by step 


<div class="mw-collapsible-content toccolours">

1.  Create a profile, preferably using the <img alt="" src=images/Workbench_Sketcher.svg  style="width   *16px;"> [Sketcher Workbench](Sketcher_Workbench.md) on the XZ plane.
    <img alt="Profile sketch" src=images/SheetMetal_Example-02e.png  style="width   *300px;">
2.  Activate the <img alt="" src=images/SheetMetal_AddBase.svg  style="width   *16px;"> [Make Base Wall](SheetMetal_AddBase.md) command to create a BaseBend object.
3.  Edit the BaseBend object\'s parameters in the properties panel   *
    <img alt="BaseBend object and highlighted sketch" src=images/SheetMetal_Example-02f.png  style="width   *200px;">
    -   Set **Mid Plane** to `True`to let the profile extend symmetrically to both sides of the sketch plane.
    -   Set **length** to 32 mm.
    -   Set **radius** to 2 mm.
    -   Set **thickness** to 0.3 mm.
4.  Select the face between the round sections and activate the <img alt="" src=images/Workbench_Sketcher.svg  style="width   *16px;"> [Sketcher Workbench](Sketcher_Workbench.md).
    <img alt="Face to support the sketch" src=images/SheetMetal_Example-02g.png  style="width   *200px;">
5.  To hide the curled part use the <img alt="" src=images/Sketcher_ViewSection.svg  style="width   *16px;"> [Sketcher View section](Sketcher_ViewSection.md) command.
6.  Create the cut-out contour.
    <img alt="Cut-out contour" src=images/SheetMetal_Example-02h.png  style="width   *" height="240px;"> <img alt="Cut-out contour slightly touching the selected face" src=images/SheetMetal_Example-02i.png  style="width   *" height="240px;">
7.  Finish the sketch using the <img alt="" src=images/Sketcher_LeaveSketch.svg  style="width   *16px;"> [Sketcher Leave sketch](Sketcher_LeaveSketch.md) command.
8.  Select the face again and add the Cut-out sketch to the selection.
    <img alt="Face and sketch selected" src=images/SheetMetal_Example-02j.png  style="width   *200px;">
9.  Use the <img alt="" src=images/SheetMetal_SketchOnSheet.svg  style="width   *16px;"> [Sketch on Sheet](SheetMetal_SketchOnSheet.md) command to cut around the curled bit.
    <img alt="Finished first half" src=images/SheetMetal_Example-02b.png  style="width   *200px;">
10. One side is finished. We now need to find a way to mirror the body.

**Potential mirror options   ***

-   The <img alt="" src=images/PartDesign_Mirrored.svg  style="width   *16px;"> [PartDesign Mirrored](PartDesign_Mirrored.md) command fails because it cannot handle SheetMetal features for some reason. So that does not work.
-   The <img alt="" src=images/Part_Mirror.svg  style="width   *16px;"> [Part Mirror](Part_Mirror.md) command creates a mirrored part, but this is no longer unfoldable. So that does not work either.
-   One way that can work is to use a clone. This still can\'t be mirrored, but it can use axial symmetry (turn it 180°).
-   Another way that works is to use a link object.

**Mirror using a clone   ***

1.  Select the body from the tree view.
2.  Use the <img alt="" src=images/PartDesign_Clone.svg  style="width   *16px;"> [PartDesign Clone](PartDesign_Clone.md) command. It adds a new body containing a clone object.
    To apply a 180° turn set the **Angle** under the Placement property of either the body or the clone to 180°. (Z axis is default and should be fine if you started on the XZ plane as described).
    <img alt="Cloned half" src=images/SheetMetal_Example-02b.png  style="width   *200px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="Flipped cloned half" src=images/SheetMetal_Example-02l.png  style="width   *200px;">
3.  With the body still active, use the <img alt="" src=images/PartDesign_Boolean.svg  style="width   *16px;"> [PartDesign Boolean operation](PartDesign_Boolean.md) command to add the body of the clone and fuse both halves.
    <img alt="Fused halves" src=images/SheetMetal_Example-02c.png  style="width   *200px;">
4.  Activate the <img alt="" src=images/SheetMetal_Unfold.svg  style="width   *16px;"> [Unfold](SheetMetal_Unfold.md) command to get an Unfold object.
    <img alt="Clip and Unfold object" src=images/SheetMetal_Example-02m.png  style="width   *200px;"> <img alt="Unfold object" src=images/SheetMetal_Example-02d.png  style="width   *200px;">
5.  Done!

**Mirror using a link object   ***

1.  Select the body from the tree view.
2.  Use the <img alt="" src=images/Std_LinkMake.svg  style="width   *16px;"> [Make link](Std_LinkMake.md) command. This adds a new link object.
3.  Duplicate the link object by setting the property **Element Count** to 2.
4.  To apply a 180° turn set the **Angle** under the Placement property of either of the sub-linked objects to 180°. (Z axis is default and should be fine if you started on the XZ plane as described).
5.  Select both sub-linked objects in the tree view.
6.  Activate the <img alt="" src=images/Part_Fuse.svg  style="width   *16px;"> [Part Fuse](Part_Fuse.md) command to fuse both halves.
    <img alt="Fused halves" src=images/SheetMetal_Example-02c.png  style="width   *200px;">
7.  Activate the <img alt="" src=images/SheetMetal_Unfold.svg  style="width   *16px;"> [Unfold](SheetMetal_Unfold.md) command to get an Unfold object.
    <img alt="Clip and Unfold object" src=images/SheetMetal_Example-02m.png  style="width   *200px;"> <img alt="Unfold object" src=images/SheetMetal_Example-02d.png  style="width   *200px;">
8.  Done!


</div>


</div>

## Omega clamp 

<img alt="" src=images/SheetMetal_Example-03.png  style="width   *400px;">
<img alt="" src=images/SheetMetal_Example-03a.png  style="width   *200px;"> <img alt="" src=images/SheetMetal_Example-03b.png  style="width   *200px;"> <img alt="" src=images/SheetMetal_Example-03.png  style="width   *200px;"> <img alt="" src=images/SheetMetal_Example-03c.png  style="width   *200px;"> 
*Workflow Omega Clip   *
**<img src="images/SheetMetal_AddBase.svg" width=16px> [Make Base Wall](SheetMetal_AddBase.md)*,
{{Button|<img src="images/PartDesign_Hole.svg" width=16px> [PartDesign Hole](PartDesign_Hole.md)**,
**<img src="images/PartDesign_Fillet.svg" width=16px> [PartDesign Fillet](PartDesign_Fillet.md)**,
**<img src="images/SheetMetal_Unfold.svg" width=16px> [Unfold](SheetMetal_Unfold.md)**.
}}

## Hex bowl 

<img alt="" src=images/SheetMetal_Example-04.png  style="width   *400px;">
<img alt="" src=images/SheetMetal_Example-04a.png  style="width   *200px;"> <img alt="" src=images/SheetMetal_Example-04b.png  style="width   *200px;"> <img alt="" src=images/SheetMetal_Example-04.png  style="width   *200px;"> <img alt="" src=images/SheetMetal_Example-04c.png  style="width   *200px;"> 
*Workflow Hex Bowl   *
**<img src="images/SheetMetal_AddBase.svg" width=16px> [Make Base Wall](SheetMetal_AddBase.md)*,
{{Button|<img src="images/SheetMetal_AddWall.svg" width=16px> [Make Wall](SheetMetal_AddWall.md)**,
6x **<img src="images/SheetMetal_AddCornerRelief.svg" width=16px> [Add Corner Relief](SheetMetal_AddCornerRelief.md)**,
**<img src="images/SheetMetal_Unfold.svg" width=16px> [Unfold](SheetMetal_Unfold.md)**.
}}

<img alt="" src=images/SheetMetal_Example-04d.png  style="width   *200px;">

When a Corner Relief is added (right side) it can be necessary to adjust the value of the **Size** property.

## Pen clip 

<img alt="" src=images/SheetMetal_Example-05.png  style="width   *400px;">
<img alt="" src=images/SheetMetal_Example-05a.png  style="width   *200px;"> <img alt="" src=images/SheetMetal_Example-05b.png  style="width   *200px;"> <img alt="" src=images/SheetMetal_Example-05c.png  style="width   *200px;"> <img alt="" src=images/SheetMetal_Example-05d.png  style="width   *200px;"> <img alt="" src=images/SheetMetal_Example-05.png  style="width   *200px;"> <img alt="" src=images/SheetMetal_Example-05e.png  style="width   *200px;"> 
*Workflow Pen Clip   *
**<img src="images/SheetMetal_AddBase.svg" width=16px> [Make Base Wall](SheetMetal_AddBase.md)*,
{{Button|<img src="images/PartDesign_Pocket.svg" width=16px> [PartDesign Pocket](PartDesign_Pocket.md)**,
3x **<img src="images/SheetMetal_AddWall.svg" width=16px> [Make Wall](SheetMetal_AddWall.md)**,
**<img src="images/SheetMetal_Unfold.svg" width=16px> [Unfold](SheetMetal_Unfold.md)**.
}}

## Extend face example 

<img alt="" src=images/SheetMetal_Example-06.png  style="width   *400px;">
<img alt="" src=images/SheetMetal_Example-06a.png  style="width   *200px;"> <img alt="" src=images/SheetMetal_Example-06b.png  style="width   *200px;"> <img alt="" src=images/SheetMetal_Example-06c.png  style="width   *200px;"> <img alt="" src=images/SheetMetal_Example-06.png  style="width   *200px;"> <img alt="" src=images/SheetMetal_Example-06d.png  style="width   *200px;"> 
*Workflow Extend Face Example   *
**<img src="images/SheetMetal_AddBase.svg" width=16px> [Make Base Wall](SheetMetal_AddBase.md)*,
{{Button|<img src="images/SheetMetal_AddWall.svg" width=16px> [Make Wall](SheetMetal_AddWall.md)**,
**<img src="images/SheetMetal_Extrude.svg" width=16px> [Extend Face](SheetMetal_Extrude.md)**,
**<img src="images/SheetMetal_Extrude.svg" width=16px> [Extend Face](SheetMetal_Extrude.md)**,
**<img src="images/SheetMetal_Unfold.svg" width=16px> [Unfold](SheetMetal_Unfold.md)**.
}}

For the second use of **Extend Face** a Sketch with two contours is used for shape of the extension(s); and with the value of \"use subtraction\" set to true it provides the shape for the cut-outs, as well

## USB shield contact 

<img alt="" src=images/SheetMetal_Example-07.png  style="width   *400px;">
<img alt="" src=images/SheetMetal_Example-07a.png  style="width   *200px;"> <img alt="" src=images/SheetMetal_Example-07b.png  style="width   *200px;"> <img alt="" src=images/SheetMetal_Example-07c.png  style="width   *200px;"> <img alt="" src=images/SheetMetal_Example-07d.png  style="width   *200px;"> <img alt="" src=images/SheetMetal_Example-07.png  style="width   *200px;"> <img alt="" src=images/SheetMetal_Example-07e.png  style="width   *200px;"> 
*Workflow USB shield contact   *
**<img src="images/SheetMetal_AddBase.svg" width=16px> [Make Base Wall](SheetMetal_AddBase.md)*,
{{Button|<img src="images/SheetMetal_Extrude.svg" width=16px> [Extend Face](SheetMetal_Extrude.md)**,
**<img src="images/PartDesign_Pocket.svg" width=16px> [PartDesign Pocket](PartDesign_Pocket.md)**,
**<img src="images/SheetMetal_Extrude.svg" width=16px> [Extend Face](SheetMetal_Extrude.md)**,
**<img src="images/SheetMetal_AddWall.svg" width=16px> [Make Wall](SheetMetal_AddWall.md)**,
**<img src="images/SheetMetal_Unfold.svg" width=16px> [Unfold](SheetMetal_Unfold.md)**.
}}

(The pull relief is just an artistic expression of what could be hidden inside a real plug)

## SheetMetal properties 

This section tries to explain the properties of each SheetMetal object with simple images, where applicable.


<div class="mw-collapsible mw-collapsed">

### BaseBend object <img alt="" src=images/SheetMetal_AddBase.svg  style="width   *24px;"> 


<div class="mw-collapsible-content toccolours">

<img alt="" src=images/SheetMetal_Example-08a.png  style="width   *200px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="" src=images/SheetMetal_Example-08b.png  style="width   *200px;">



*Selected sketch + 
**<img src="images/SheetMetal_AddBase.svg" width=16px> [Make Base Wall](SheetMetal_AddBase.md)* 
→ BaseBend object with default settings**

<img alt="" src=images/SheetMetal_Example-08b.png  style="width   *200px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="" src=images/SheetMetal_Example-08c.png  style="width   *200px;">



*Edit **length*   * Default length → Reduced length**

<img alt="" src=images/SheetMetal_Example-08d.png  style="width   *200px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="" src=images/SheetMetal_Example-08h.png  style="width   *200px;">



*Switch **Mid Plane* from {{False** to `True`   * Extrusion in one direction → Symmetric extrusion}}

<img alt="" src=images/SheetMetal_Example-08d.png  style="width   *200px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="" src=images/SheetMetal_Example-08e.png  style="width   *200px;">



*Switch **Reverse* from {{False** to `True`   * Default direction → Inverted direction}}

<img alt="" src=images/SheetMetal_Example-08e.png  style="width   *200px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="" src=images/SheetMetal_Example-08f.png  style="width   *200px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="" src=images/SheetMetal_Example-08g.png  style="width   *200px;">



*Select **Bend Side*   * {{value|Outside** (default) → {{value|Inside}} → {{value| Middle}}}}

<img alt="" src=images/SheetMetal_Example-08e.png  style="width   *200px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="" src=images/SheetMetal_Example-08i.png  style="width   *200px;">



*Edit **radius*   * Default radius → Enlarged radius.<br>
This property is the inner radius of the bends created at the vertices where two edges in the sketch have a non-tangential transition.**

<img alt="" src=images/SheetMetal_Example-08e.png  style="width   *200px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="" src=images/SheetMetal_Example-08j.png  style="width   *200px;">



*Edit **thickness*   * Default Thickness → Enlarged thickness**


</div>


</div>


<div class="mw-collapsible mw-collapsed">

### Bend object <img alt="" src=images/SheetMetal_AddWall.svg  style="width   *24px;"> 


<div class="mw-collapsible-content toccolours">

A Bend object consists of sets of one cylindrical bend and one planar strip each. Each pair extends from a selected edge of a blank.

<img alt="" src=images/SheetMetal_Example-09a.png  style="width   *200px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="" src=images/SheetMetal_Example-09b.png  style="width   *200px;">



*Selected edges + 
**<img src="images/SheetMetal_AddWall.svg" width=16px> [Make Wall](SheetMetal_AddWall.md)* 
→ Bend objects with default settings <br>
(Two Bend objects in two separate bodies.)**

Edit **radius** to vary the inner radius of all bends supplied by a Bend object. (See BaseBend object above)

Edit **length** to vary the length of all planar strips extending from the bends of a Bend object.

   *   Don\'t confuse the **length** with a flange length which is the sum of this length, radius, and thickness (90° only).

<img alt="" src=images/SheetMetal_Example-09b.png  style="width   *200px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="" src=images/SheetMetal_Example-09c.png  style="width   *200px;">



*Switch **invert* from {{FALSE** to `True`   *Default flanges (Bend objects) → Inverted flanges}}

<img alt="" src=images/SheetMetal_Example-09c.png  style="width   *200px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="" src=images/SheetMetal_Example-09d.png  style="width   *200px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="" src=images/SheetMetal_Example-09e.png  style="width   *200px;">



*Edit **angle*   *Default angle (90°) → Enlarged angle → Decreased angle**

We don\'t have to care about trimming the edges, because **Auto Miter** is activated by default.
If deactivated, the result would look like this   *

<img alt="" src=images/SheetMetal_Example-09m.png  style="width   *200px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="" src=images/SheetMetal_Example-09f.png  style="width   *200px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="" src=images/SheetMetal_Example-09g.png  style="width   *200px;">



*Switch **Auto Miter* from {{TRUE** to `False`   * Default angle (90°) → Enlarged angle → Decreased angle<br>
(Auto Miter has no effect on single flanges)}}

To manually miter a flange edge **miterangle1** and **miterangle2** are used   *

<img alt="" src=images/SheetMetal_Example-09m.png  style="width   *200px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="" src=images/SheetMetal_Example-09n.png  style="width   *200px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="" src=images/SheetMetal_Example-09o.png  style="width   *200px;">



*Edit **miterangle1* and {{PropertyData|miterangle2**   * No miter (default) → Differently mitered edges, positive angle → Symmetrically mitered edges, negative angles}}

Mitering only effects the planar strips, not the bends.

   *   (It takes the whole edge into account and so cannot be used to chamfer flange edges)

To display the different choices of **Bend Type** we introduce an auxiliary cuboid that extrudes from the same outline as the blank and has the same height as the Bend object (its flange length).

<img alt="" src=images/SheetMetal_Example-09h.png  style="width   *200px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="" src=images/SheetMetal_Example-09i.png  style="width   *200px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="" src=images/SheetMetal_Example-09j.png  style="width   *200px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="" src=images/SheetMetal_Example-09k.png  style="width   *200px;">



*Select **Bend Type*   * {{value|Material Outside** (default) → {{value|Material Inside}} → {{value|Thickness Outside}} → {{value|Offset}}}}

-   Outside   * The bend starts at the selected edge (The whole Bend object lies outside the cuboid).
-   Inside   * The outer side of the bend ends on the cuboid surface (The whole Bend object lies inside the cuboid).
-   Thickness Outside   * The inner side of the bend ends on the cuboid surface (only the planar strip is protruding from the cuboid surface).
-   Offset   * According to the value of **offset** the bend is moved in outward direction from its default position.

   *   An extension is inserted for positive values (high-lighted strip).
   *   Negative values are allowed to move the bend inwards.

If we don\'t want to use the whole length of an edge we can use **gap1** and **gap2**.

<img alt="" src=images/SheetMetal_Example-09c.png  style="width   *200px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="" src=images/SheetMetal_Example-09l.png  style="width   *200px;">



*Edit **gap1* and {{PropertyData|gap2**   * Default flanges → Flanges with different values for gap1 and gap2}}

If the length of a gap reaches or extends the value of **min Relief Gap**, a relief will be added to the gap.
Reliefs are controlled by **relief Type**, **reliefd** (relief depth), and **reliefw** (relief width) which are enabled only when a gap value is set.

<img alt="" src=images/SheetMetal_Example-09p.png  style="width   *200px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="" src=images/SheetMetal_Example-09q.png  style="width   *200px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="" src=images/SheetMetal_Example-09r.png  style="width   *200px;">



*Edit **reliefd* and {{PropertyData|reliefw**   * Default values → Relief depth enlarged → Relief depth and width enlarged}}

<img alt="" src=images/SheetMetal_Example-09r.png  style="width   *200px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="" src=images/SheetMetal_Example-09s.png  style="width   *200px;">



*Switch **relief Type* from {{value|Rectangle** to {{value|Round}}   * Default rectangular relief → Round relief}}

The round option will only be applied, if the relief depth is larger than the relief width.

Switch **Use Relief Factor** from `False` (default) to `True` to set the values of **reliefd** and **reliefw** automatically. Both are set to the object\'s (inherited) thickness multiplied by the value of **Relief Factor**.

   *   In this case the round option is useless, since the relief depth is as large as the relief width. (See above)

A new property **Length Spec** <small>(v1.0)</small>  enables us to choose how to measure the length of the Bend object   *

<img alt="" src=images/SheetMetal_Example-09t.png  style="width   *500px;"> 
*Side view of four 120° flanges with default length (10 mm) and different **Length Spec* values   * <br> {{value|Leg** (default), {{value|Outer Sharp}}, {{value|Inner Sharp}}, {{value|Tangential}}}}

With the {{value|Tangential}} option selected the property **length** is the equivalent of the flange length.


{{value|Outer Sharp}}

and {{value|Tangential}} are identical for 90° angles.


</div>


</div>


<div class="mw-collapsible mw-collapsed">

### Extend object <img alt="" src=images/SheetMetal_Extrude.svg  style="width   *24px;"> 


<div class="mw-collapsible-content toccolours">

An Extend object extends a sheet metal plate at one or more selected edge faces or edges.

<img alt="" src=images/SheetMetal_Example-10a.png  style="width   *200px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="" src=images/SheetMetal_Example-10b.png  style="width   *200px;">



*Selected edge face and edges + 
**<img src="images/SheetMetal_Extrude.svg" width=16px> [Extend Face](SheetMetal_Extrude.md)* 
→ One Extend object with default settings.**

A first issue occurs here   * Although the property **Refine** is set to `True` two of the extensions still show their seam lines. Only the extension of the last selected element will be refined.

To refine all extensions they have to be created separately   *

<img alt="" src=images/SheetMetal_Example-10c.png  style="width   *200px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="" src=images/SheetMetal_Example-10d.png  style="width   *200px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="" src=images/SheetMetal_Example-10e.png  style="width   *200px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="" src=images/SheetMetal_Example-10f.png  style="width   *200px;">



*3x Selected edge face or edge + 
**<img src="images/SheetMetal_Extrude.svg" width=16px> [Extend Face](SheetMetal_Extrude.md)* 
→ Three Extend objects completely refined and with default settings.**

Altered properties apply to all edges listed in the related **base Object** of the Extension object.

Edit **length** to adjust the length of the extension.

<img alt="" src=images/SheetMetal_Example-10h.png  style="width   *200px;"> <img alt="" src=images/SheetMetal_Example-10g.png  style="width   *200px;">



*Edit **gap1* and {{PropertyData|gap2** to reduce the width of the extension.<br>
Left   * Extension object with 3 edges. Right   * One of the Extension objects with one single edge.}}

Link a sketch to the property **Sketch** to shape an extension. The properties **length**, **gap1** and **gap2** will be ignored once a sketch is linked. (This seems not to work with still unbent blanks).

<img alt="" src=images/SheetMetal_Example-10i.png  style="width   *200px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="" src=images/SheetMetal_Example-10j.png  style="width   *200px;">



*A selected sketch lying on the flange to be extended → Resulting extension*

It is plain to see that it doesn\'t matter which edge was selected for the Extend object, the shape of the flange is changed wherever sketch geometry protrudes, the new shape can even contain parts that are disconnected from the original flange. Multiple outlines are no problem, but the flange is not cut into.

This example shows that designers are responsible for their construction and shouldn\'t rely on the results of their tools, which do not make sense in this case. The Sketch attached to a flange face is problematic as well due to the toponaming problem, but for this a solution is in sight.

But there are better use cases for this tool involving almost closed shapes such as one of the examples on the [SheetMetal Extrude](SheetMetal_Extrude.md) page   *

<img alt="" src=images/SheetMetal_Example-10k.png  style="width   *200px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="" src=images/SheetMetal_Example-10l.png  style="width   *200px;">



*An almost closed profile → The added default extension is fused with the opposite side creating a closed profile (a tube) that is not unfoldable*

<img alt="" src=images/SheetMetal_Example-10l.png  style="width   *200px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="" src=images/SheetMetal_Example-10m.png  style="width   *200px;">



*Link a rectangular sketch to the property **Sketch*   * Closed profile → Profile with rectangular extension, still fused**

<img alt="" src=images/SheetMetal_Example-10m.png  style="width   *200px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="" src=images/SheetMetal_Example-10n.png  style="width   *200px;">



*Switch **Use Subtraction* to {{true** to provide a (hardly visible) default gap between the Extension object and the opposite side, then increase **Offset** to widen the gap   *<br>
Fused profile → Profile with interlocking extension, this final result is unfoldable}}


</div>


</div>

[Category   *SheetMetal](Category_SheetMetal.md) [Category   *Addons](Category_Addons.md) [Category   *External Command Reference](Category_External_Command_Reference.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [SheetMetal](Category_SheetMetal.md) > [Addons](Category_Addons.md) > [External Command Reference](Category_External Command Reference.md) > SheetMetal Examples/en
