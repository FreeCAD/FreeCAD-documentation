# SheetMetal Examples/pl
{{TOCright}}

## Wprowadzenie

Środowisko pracy Arkusz Blachy stało się bardzo rozbudowane i wymaga odpowiedniej dokumentacji.

Aby uniknąć przepełnienia stron narzędziowych przykładami, dodano tę stronę w celu zebrania części pokazujących i wyjaśniających specjalne możliwości środowiska Arkusz Blachy.

Zaplanowane etapy tworzenia treści   *

1.  Zbieranie zdjęć
2.  Dodawanie opisów przepływów pracy
3.  Dodawanie bardziej szczegółowych samouczków

## Zawias

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

## Klips do papieru 

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

## Klamra Omega 

<img alt="" src=images/SheetMetal_Example-03.png  style="width   *400px;">
<img alt="" src=images/SheetMetal_Example-03a.png  style="width   *200px;"> <img alt="" src=images/SheetMetal_Example-03b.png  style="width   *200px;"> <img alt="" src=images/SheetMetal_Example-03.png  style="width   *200px;"> <img alt="" src=images/SheetMetal_Example-03c.png  style="width   *200px;"> 
*Workflow Omega Clip   *
**<img src="images/SheetMetal_AddBase.svg" width=16px> [Make Base Wall](SheetMetal_AddBase.md)*,
{{Button|<img src="images/PartDesign_Hole.svg" width=16px> [PartDesign Hole](PartDesign_Hole.md)**,
**<img src="images/PartDesign_Fillet.svg" width=16px> [PartDesign Fillet](PartDesign_Fillet.md)**,
**<img src="images/SheetMetal_Unfold.svg" width=16px> [Unfold](SheetMetal_Unfold.md)**.
}}

## Sześciokątna miska 

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

## Klips do długopisu 

<img alt="" src=images/SheetMetal_Example-05.png  style="width   *400px;">
<img alt="" src=images/SheetMetal_Example-05a.png  style="width   *200px;"> <img alt="" src=images/SheetMetal_Example-05b.png  style="width   *200px;"> <img alt="" src=images/SheetMetal_Example-05c.png  style="width   *200px;"> <img alt="" src=images/SheetMetal_Example-05d.png  style="width   *200px;"> <img alt="" src=images/SheetMetal_Example-05.png  style="width   *200px;"> <img alt="" src=images/SheetMetal_Example-05e.png  style="width   *200px;"> 
*Workflow Pen Clip   *
**<img src="images/SheetMetal_AddBase.svg" width=16px> [Make Base Wall](SheetMetal_AddBase.md)*,
{{Button|<img src="images/PartDesign_Pocket.svg" width=16px> [PartDesign Pocket](PartDesign_Pocket.md)**,
3x **<img src="images/SheetMetal_AddWall.svg" width=16px> [Make Wall](SheetMetal_AddWall.md)**,
**<img src="images/SheetMetal_Unfold.svg" width=16px> [Unfold](SheetMetal_Unfold.md)**.
}}

## Przykład przedłużenia ściany 

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

## Korpus złącza USB 

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

## Właściwości środowiska pracy Arkusz Blachy 

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

[Category   *SheetMetal](Category_SheetMetal.md) [Category   *Addons](Category_Addons.md) [Category   *External Command Reference](Category_External_Command_Reference.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [SheetMetal](Category_SheetMetal.md) > [Addons](Category_Addons.md) > [External Command Reference](Category_External Command Reference.md) > SheetMetal Examples/pl
