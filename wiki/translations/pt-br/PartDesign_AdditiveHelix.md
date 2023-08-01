---
- GuiCommand:
   Name:PartDesign AdditiveHelix
   MenuLocation:Part Design - Create an additive feature - Additive helix
   Workbenches:[PartDesign](PartDesign_Workbench.md)
   Version:0.19
   SeeAlso:[PartDesign SubtractiveHelix](PartDesign_SubtractiveHelix.md)
---

# PartDesign AdditiveHelix/pt-br

## Description

The **AdditiveHelix** tool creates a solid by sweeping a selected sketch or 2D object along a helix path.

<img alt="" src=images/PartDesign_AdditiveHelix_example_overview.png  style="width:650px;">

*The profile (B), is swept around axis (A) in order to produce the solid helix (C)*

## Usage

1.  Select the sketch to be swept into a helix. A face on the existing solid can alternatively be used.
2.  Press the **<img src="images/PartDesign_AdditiveHelix.svg" width=16px> [PartDesign AdditiveHelix](PartDesign_AdditiveHelix.md)** button.
3.  Set the Helix parameters (see next section).
4.  Inspect the Helix in the view window, to ensure that the parameters do not result in a self intersecting helix.
5.  Press **OK**.

## Options

When creating an Additive Helix, the **Helix parameters** dialogue offers several parameters specifying how the sketch should be swept.

![](images/PartDesign_AdditiveHelix_taskpanel.png )

### Axis

This option specifies the axis about which the sketch is to be swept.

-   **Normal sketch axis**: selects the normal of the sketch that runs through the sketch origin as axis. <small>(v0.20)</small> 
-   **Vertical sketch axis**: selects the vertical sketch axis. This is the default for new helices.
-   **Horizontal sketch axis**: selects the horizontal sketch axis.
-   **Construction line**: selects a construction line contained in the sketch used by the Helix. The drop down list will contain an entry for each construction line. The first construction line created in the sketch will be labelled *Construction line 1*.
-   **Base (X/Y/Z) axis**: selects the X, Y or Z axis of the Body\'s Origin;
-   **Select reference\...**: allows selection in the 3D view of an edge on the Body, or a [datum line](PartDesign_Line.md).

### Mode

This controls what parameters will be used to define the helix. The choices are:

-   **Pitch-Height-Angle**: definition via the height per turn and the overall height
-   **Pitch-Turns-Angle**: definition via the height per turn and the number of turns
-   **Height-Turns-Angle**: definition via the overall height and the number of turns
-   **Height-Turns-Growth** <small>(v0.20)</small> : definition via the overall height, the number of turns and the growth of the helical radius. So a Height of zero leads to a path in form of a spiral. A Height and Growth of zero to leads to a path in form of a circle.

### Pitch

The distance between turns in the helix.

### Height

The height of the helix (center-center).

### Turns

The number of turns in the helix. Define as Height/Pitch

### Cone Angle 

Angle of the cone that forms a hull around the helix. Allowable range: \[-89°, +89°\].

### Left handed 

If checked, the turning direction of helix is reversed from default clockwise to counterclockwise.

### Reversed

If checked, the axis direction of helix is reversed from default.

### Update view 

If checked, the helix will be shown in the view, and updated automatically on every change of the parameters.

## Preferences

-   An additive helix that does not intersect the body will be visible in the preview if **Tools → Edit parameters... → BaseApp → Preferences → Mod → PartDesign → AdditiveHelixPreview** is set to `True`. The default for this preference is `False`. <small>(v0.20)</small> 

## Properties

-    **Pitch**: The axial distance between two turns.

-    **Height**: The total length of the helix (not accounting for the extent of the profile)

-    **Turns**: The number of turns (does not need to be a whole number)

-    **Left Handed**: See [Left Handed](#Left_handed.md).

-    **Reversed**: See [Reversed](#Reversed.md).

-    **Angle**: The rate at which the radius of the helix increase along the axis. Allowable range: \[-89°, +89°\].

-    **Reference axis**: The helix axis

-    **Mode**: The helix input mode (pitch-height, pitch-turns, turns-height)

-    **Outside**: Not used (Used in SubtractiveHelix)

-    **Has Been Edited**: If false, the tool will propose an initial value for pitch based on the profile bounding box, so that self intersection is avoided.

-    **Refine**: true or false. If set to true, cleans the solid from residual edges left by features. See [Part RefineShape](Part_RefineShape.md) for more details.

-    **Profile**: Either a sketch containing a closed contour, or a face.

-    **Midplane**: Not used.

-    **Up to face**: Not used.

-    **Allow multiple face**: Not used.

## Examples

![Example helix using a [B-spline](images/Sketcher_CreateBSpline.md) in the sketch](PartDesign_AdditiveHelix_example_bspline.png )

![Example helix where the helix axis is normal to the sketch plane resulting in a \"Pad with twist\" effect.](images/PartDesign_AdditiveHelix_example_twisting_pad.png )





{{PartDesign Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign AdditiveHelix/pt-br
