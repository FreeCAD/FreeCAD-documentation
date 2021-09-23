---
- GuiCommand:/ru
   Name/ru:Субтрактивная спираль
   Name:PartDesign_SubtractiveHelix
   MenuLocation:PartDesign → Create a subtractive feature → Субтрактивная спираль
   Workbenches:[PartDesign](PartDesign_Workbench/ru.md)
   Version:0.19
   SeeAlso:[Аддитивная спираль](PartDesign_AdditiveHelix/ru.md)
---

## Описание

The **SubtractiveHelix** tool modifies a solid by sweeping a selected sketch or 2D object along a helix path cutting away the material.

![](images/PartDesign_SubtractiveHelix_example_overview.png )

*The profile (B), is swept around axis (A) in order to produce the helical groove (C) in the pre-existing work piece*

## Применение

1.  Select the sketch to be swept into a helix. A face on the existing solid can alternatively be used.
2.  Press the **<img src="images/PartDesign_SubtractiveHelix.svg" width=24px> [PartDesign SubtractiveHelix](PartDesign_SubtractiveHelix.md)** button.
3.  Set the Helix parameters (see next section).
4.  Inspect the Helix in the view window, to ensure that the parameters do not result in a self intersecting helix.
5.  Press **OK**.

## Опции

When creating a SubtractiveHelix, the **Helix parameters** dialogue offers several parameters specifying how the sketch should be swept.

![](images/PartDesign_SubtractiveHelix_taskpanel.png )

### Axis

This option specifies the axis about which the sketch is to be swept.

-   **Vertical sketch axis**: selects the vertical sketch axis.
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

### Шаг

Расстояние между двумя витками спирали.

### Height

The height of the helix (center-center).

### Turns

The number of turns in the helix. Define as Height/Pitch

### Cone Angle 

The rate at which the radius of the helix increase along the axis. Allowable range: \[-89°, +89°\].

### Left handed 

If checked, the turning direction of helix is reversed from default clockwise to counterclockwise.

### Reversed

If checked, the axis direction of helix is reversed from default.

### Remove outside of profile 

If checked, the result will be the intersection of the swept profile and the preexisting body.

### Update view 

If checked, the helix will be shown in the view, and updated automatically on every change of the parameters.

## Preferences

-   A subtractive helix that does not intersect the body will be visible in the preview if **Tools → Edit parameters... → BaseApp → Preferences → Mod → PartDesign → SubtractiveHelixPreview** is set to `True`. The default for this preference is `True`. <small>(v0.20)</small> 

## Свойства

-    **Pitch**: The axial distance between two turns.

-    **Height**: The total length of the helix (not accounting for the extent of the profile)

-    **Turns**: The number of turns (does not need to be a whole number)

-    **Left Handed**:

-    **Reversed**: true or false. See [Reversed](#Reversed.md).

-    **Angle**: The rate at which the radius of the helix increase along the axis. Allowable range: \[-89°, +89°\].

-    **Reference axis**: The helix axis

-    **Mode**: The helix input mode (pitch-height, pitch-turns, turns-height)

-    **Outside**: If true, the result will be the intersection of the swept profile and the preexisting body.

-    **Has Been Edited**: If false, the tool will propose an initial value for pitch based on the profile bounding box, so that self intersection is avoided.

-    **Refine**: true or false. If set to true, cleans the solid from residual edges left by features. See [Part RefineShape](Part_RefineShape.md) for more details.

-    **Profile**: Either a sketch containing a closed contour, or a face.

-    **Midplane**: Not used.

-    **Up to face**: Not used.

-    **Allow multiple face**: Not used.





{{PartDesign Tools navi

}} 
