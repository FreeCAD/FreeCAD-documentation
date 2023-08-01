---
- GuiCommand:
   Name:PartDesign Revolution
   MenuLocation:Part Design → Create an additive feature → Revolution
   Workbenches:[PartDesign](PartDesign_Workbench.md)
   SeeAlso:[PartDesign Groove](PartDesign_Groove.md)
---

# PartDesign Revolution/tr

## Description


<div class="mw-translate-fuzzy">

## Giriş


</div>

![](images/PartDesign_Revolution_example.svg ) 
*Above: sketch (A) is revolved 270 degrees counter-clockwise around axis (B); resulting solid (C) is shown right.*

## Usage

1.  Select the sketch to be revolved. A face on the existing solid can alternatively be used.
2.  Press the **<img src="images/PartDesign_Revolution.svg" width=24px> '''Revolution'''** button.
3.  Set the Revolution parameters (see next section).
4.  Press **OK**.

## Options

When creating a revolution, the **Revolution parameters** dialogue offers several parameters specifying how the sketch should be revolved.

+++
| ![](images/partdesign_revolution_parameters.png ) | ### Axis                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                  |                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                  | This option specifies the axis about which the sketch is to be revolved.                                                                                                                                                                                                                                                                                                    |
|                                                                                  |                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                  | -   **Vertical sketch axis**: selects the vertical sketch axis.                                                                                                                                                                                                                                                                                                             |
|                                                                                  | -   **Horizontal sketch axis**: selects the horizontal sketch axis.                                                                                                                                                                                                                                                                                                         |
|                                                                                  | -   **Construction line**: selects a construction line contained in the sketch used by the Revolution. The drop down list will contain an entry for each construction line. The first construction line will be labelled *Construction line 1*.                                                                                                                             |
|                                                                                  | -   **Base (X/Y/Z) axis**: selects the X, Y or Z axis of the Body\'s Origin.                                                                                                                                                                                                                                                                                                |
|                                                                                  | -   **Select reference\...**: allows selection in the 3D view of an edge on the Body, or a [datum line](PartDesign_Line.md).                                                                                                                                                                                                                                        |
|                                                                                  |                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                  | ### Angle                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                  |                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                  | This controls the angle through which the revolution is to be formed, e.g. 360° would be a full, contiguous revolution. The images in the [examples](#Examples.md) section demonstrate some of the possibilities with specifying different angles. It is not possible to specify negative angles (use the **Reversed** option instead) or angles greater than 360°. |
|                                                                                  |                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                  | ### Symmetric to plane                                                                                                                                                                                                                                                                                                                                 |
|                                                                                  |                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                  | If checked, the revolution will extend half of the specified angle in both directions from the sketch plane.                                                                                                                                                                                                                                                                |
|                                                                                  |                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                  | ### Reversed                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                  |                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                  | If checked, the direction of revolution is reversed from default clockwise to counterclockwise.                                                                                                                                                                                                                                                                             |
+++

## Properties

Below are properties which can be defined after creation of the feature. Data properties *Base* and *Axis* are uneditable.

-    **Angle**: angle of rotation. See [Angle](#Angle.md).

-    **Label**: label given to the operation, can be changed at convenience.

-    **Midplane**: true or false. See [Symmetric to plane](#Symmetric_to_plane.md).

-    **Reversed**: true or false. See [Reversed](#Reversed.md).

-    **Refine**: true or false. If set to true, cleans the solid from residual edges left by features. See [Part RefineShape](Part_RefineShape.md) for more details.

## Examples

![Example revolution using a construction line as the Revolution axis: In this image the angle is 75°, revolution is about the construction line (Sketch axis 0).](images/PartDesign_Revolution_axis_fromconstructionlines1.jpg )

## Useful links 

A [detailed example of use](http://forum.freecadweb.org/viewtopic.php?f=3&t=3674) on the forum.





{{PartDesign Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Revolution/tr
