---
- TutorialInfo:   Topic: Sketcher
   Level: Beginner
   Time: 15 minutes
   Author:[http://freecadweb.org/wiki/index.php?title=User:Drei Drei]
   FCVersion:0.16 or above
   Files:
}}

### Introduction

This tutorial is meant to introduce the reader to the basic workflow of the [PartDesign Workbench](PartDesign_Workbench.md). The reader will see how to create 3D objects based on Sketches, perform subtraction operations and how to replicate specific features in a pattern.

<img alt="" src=images/Sketcher_tutorial_result.png  style="width:480px;">

### Requirements

-   FreeCAD version 0.17 or above
-   The reader has finished the [Basic Sketcher Tutorial](Basic_Sketcher_Tutorial.md)

### Procedure

#### Creating 3D geometry 

The purpose of the **PartDesign Workbench** is to allow the user to create geometry in 3D space. As such, it is equipped with tools to make use of sketches and convert them to 3D objects.

To achieve this, two tools are exist: <img alt="" src=images/PartDesign_Pad.svg  style="width:32px;"> [Pad](PartDesign_Pad.md) and <img alt="" src=images/PartDesign_Revolution.svg  style="width:32px;"> [Revolution](PartDesign_Revolution.md). Alongside their subtractive counterparts (<img alt="" src=images/PartDesign_Pocket.svg  style="width:32px;"> [Pocket](PartDesign_Pocket.md) and <img alt="" src=images/PartDesign_Groove.svg  style="width:32px;"> [Groove](PartDesign_Groove.md)) they make up most of the common actions used by this workbench.

1.  Switch to the PartDesign Workbench
2.  With the sketch selected in the [tree view](tree_view.md), press **[PartDesign Body](File:PartDesign_Body.svg   16px]] [[PartDesign_Body.md)**, choose the default XY-plane, and press **OK**. The sketch should appear now inside the Body.
3.  Select <img alt="" src=images/PartDesign_Pad.svg  style="width:32px;"> [Pad](PartDesign_Pad.md)
4.  Set the distance to 5 mm
5.  Select **Ok**

Another way to create 3D geometry is with the <img alt="" src=images/PartDesign_Revolution.svg  style="width:32px;"> [Revolution](PartDesign_Revolution.md) tool.

<img alt="" src=images/PartDesign_revolution_exercise.png  style="width:480px;">

1.  Create a new body **[PartDesign Body](File:PartDesign_Body.svg   16px]] [[PartDesign_Body.md)**, and then a sketch based on the image above.
2.  The sketch can be on any plane, but should be co-incident with the horizontal axis.
3.  Select <img alt="" src=images/PartDesign_Revolution.svg  style="width:32px;"> [Revolution](PartDesign_Revolution.md)
4.  Set the \"Axis\" to the \"Horizontal Sketch Axis\"
5.  Set the angle to 360°

#### Subtracting Features 

We\'ll begin by creating a sketch with the shape we want to subtract.

1.  Select the top flat face of the \"Revolution\"
2.  Select <img alt="" src=images/Sketcher_NewSketch.svg‎‎  style="width:32px;"> [New sketch](Sketcher_NewSketch.md)
3.  Select <img alt="" src=images/Sketcher_External.svg  style="width:32px;"> [External Geometry](Sketcher_External.md)
4.  Approach the edge of the pad. An arc should be highlighted
5.  Select the arc. An arc of a different color should appear in the sketch
6.  Create a hexagon centered on the same point as the arc and set the radius of the reference circle to 5 mm


{{Message| '''External Geometry'''
When a 3D element has been created it is possible to create references to it within a sketch.
# Select <img src="images/Sketcher_External.svg" width=32px> [External Geometry](Sketcher_External.md).
# Approach the element that you wish to reference, the edge of a '''Pad''' for example.
# Click on it
# New elements of a different color should appear on the sketch in the location of the feature you wish to reference.
---

# PartDesign tutorial/en

 
<img alt="" src=images/PartDesign_pocket_exercise.png  style="width:480px;">

Afterwards, we\'ll proceed to apply a **Pocket** feature.

1.  Select the sketch
2.  Select <img alt="" src=images/PartDesign_Pocket.svg  style="width:32px;"> [Pocket](PartDesign_Pocket.md)
3.  Set the distance to **Through all**

#### Pattern Features 

Recall the extruded profile that was created at the start of the tutorial.

1.  Select the top face of the object
2.  Create a new Sketch
3.  Create reference geometry linked to the top arm of the figure
4.  Create a circle constrained to the center of the reference arc
5.  Set its radius to 3 mm
6.  Pocket the sketch through all the workpiece

Instead of creating a circle for each hole in the sketch, we will introduce the concept of **Pattern Features**. These tools operate by replicating a feature in the workpiece that has already been created and that we wish to reproduce in a linear or circular arrangement. We will use a combination of **Linear** and **Polar** pattern features simulatneously to obtain the final workpiece.

1.  Select the Pocket feature that we just created in the **Tree View**
2.  Select <img alt="" src=images/PartDesign_MultiTransform.svg  style="width:32px;"> [MultiTransform](PartDesign_MultiTransform.md)

In the Combo View we are now asked to introduce the **Transformations** that we desire. Notice that in the **MultiTransform parameters** menu we see that FreeCAD has identified the Pocket as the **Original feature** and a second box requests us to **Right click it** to introduce the pattern features.

1.  Right click the box
2.  Select **Add Linear Pattern**
3.  Set the **Direction** to **Vertical Sketch Axis**
4.  Set length to 10 mm
5.  Leave occurrences at 2
6.  Click OK
7.  Right click the box again to add a **Polar Pattern**. Notice that the 3D view has now added the linear pattern.
8.  Set occurrences to 5
9.  Click OK twice

After completing this task you should have the following result.

<img alt="" src=images/PartDesign_multitransform_exercise.png  style="width:480px;">

If not, re-edit the MultiTransform operation by double clicking on it in the Tree View. Check both pattern features to detect necessary modifications, such as the **Axis** and if the **Direction** needs to be reversed.

We are now finished with the basic workflow for the [PartDesign Workbench](PartDesign_Workbench.md).



---
⏵ [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign tutorial/en
