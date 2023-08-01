---
- GuiCommand:
   Name:PartDesign InvoluteGear
   Icon:PartDesign_InternalExternalGear.svg
   MenuLocation:Part Design → Involute gear...
   Workbenches:[PartDesign](PartDesign_Workbench.md)
   SeeAlso:[FCGear Workbench](FCGear_Workbench.md)
---

# PartDesign InvoluteGear

## Description

This tool allows you to create a 2D profile of an involute gear or spline. This 2D profile is fully parametric, and can be padded with the [PartDesign Pad](PartDesign_Pad.md) or [PartDesign AdditiveHelix](PartDesign_AdditiveHelix.md) feature.

For more detailed information see Wikipedia\'s entries for: [Gear](https://en.wikipedia.org/wiki/Gear) and [Involute Gear](https://en.wikipedia.org/wiki/Involute_gear)

 <img alt="" src=images/PartDesign_Involute_Gear_01.png  style="width:200px;"> 

## Usage

### Create the profile 

1.  Optionally activate the correct body.
2.  Go to the menu **Part Design → [<img src=images/PartDesign_InternalExternalGear.svg style="width:16px"> Involute gear...**.
3.  Set the Involute parameters.
4.  Click **OK**.
5.  If there was no active body: drag and drop the gear into a body for the application of further features like padding.

### Create a spur gear 

1.  Select the gear profile in the [Tree view](Tree_view.md).
2.  Press the **<img src="images/PartDesign_Pad.svg" width=16px> [PartDesign Pad](PartDesign_Pad.md)** button.
3.  Set the pad\'s **Length** to the desired face width of the gear.
4.  Click **OK**.

### Create a helical gear 

1.  Select the gear profile in the [Tree view](Tree_view.md).
2.  Press the **<img src="images/PartDesign_AdditiveHelix.svg" width=16px> [PartDesign AdditiveHelix](PartDesign_AdditiveHelix.md)** button.
3.  Choose as Axis the normal of the gear profile, that is **Normal sketch axis** <small>(v0.20)</small> . (In earlier versions the **Base Z axis** can be used as long as the profile\'s plane has not been altered.)
4.  Choose a **Height-Turns** mode.
5.  Set the **Height** to the desired face width of the gear.
6.  To set the desired helical angle an [Expression](Expressions.md) for the **Turns** is required.
    1.  Click the blue <img alt="" src=images/Bound-expression.svg  style="width:16px;"> icon at the right of the input field.
    2.  Enter the following formula: `Height * tan(25°) / (InvoluteGear.NumberOfTeeth * InvoluteGear.Modules * pi)`, where `25°` is an example for the desired helical angle (also known as beta-value) and `InvoluteGear` is the **Name** of the profile.
    3.  Click **OK** to close the formula editor.
7.  Click **OK** to close the task panel.

Hint: To make the helical angle an accessible parameter, use a *dynamic property*:

1.  Select the profile.
2.  In the [Property editor](Property_editor.md) activate the **Show all** option in the context menu.
3.  Again in the context menu, select **Add Property**. Note: this entry is only available when **Show all** is active.
4.  In the **Add Property** dialog:
    1.  Choose `App::PropertyAngle` as Type.
    2.  Set `Gear` as Group.
    3.  Set `HelicalAngle` as Name (without a space).
    4.  Click **OK**.
5.  Now a new property **Helical Angle** (space added automatically), with an initial value of `0.0°`, becomes available.
6.  Assign the desired helical angle to the new property.
7.  In the formula of the **Turns** property of the AdditiveHelix, you can now reference `InvoluteGear.HelicalAngle` instead of the hard coded value of e.g. `25°`; again assuming `InvoluteGear` is the **Name** of the profile.

### Cut a hub for an involute splined shaft 


<small>(v0.21)</small> 

1.  Activate the correct body.
2.  Create an internal involute gear profile with the required number of grooves and adapt the values of pressure angle, addendum-, dedendum- and root fillet coefficient. See also the table in [Notes](#Notes.md) below for feasible values. For example:
    -   
        **External Gear**
        
        : False

    -   
        **Number Of Teeth**
        
        : 12

    -   
        **Pressure Angle**
        
        : 37.5°

    -   
        **Addendum Coefficient**
        
        : 0.45

    -   
        **Dedendum Coefficient**
        
        : 0.7

    -   
        **Root Fillet Coefficient**
        
        : 0.3
3.  Select the gear profile in the [Tree view](Tree_view.md).
4.  Press the **<img src="images/PartDesign_Pocket.svg" width=16px> '''Pocket'''** button.
5.  Set the pocket\'s **Type** to **Through All**.
6.  Check the pocket\'s **Symmetric To Plane** option.
7.  Click **OK**.

## Properties

-    **Addendum Coefficient**: The height of the tooth from the pitch circle up to its tip, normalized by the module. Default is 1.0 for the standard full-depth system. <small>(v0.21)</small> 

-    **Dedendum Coefficient**: The height of the tooth from the pitch circle down to its root, normalized by the module. Default is 1.25 for the standard full-depth system. <small>(v0.21)</small> 

-    **External Gear**: True or false.

-    **High Precision**: True or false.

-    **Modules**: Pitch diameter divided by the number of teeth.

-    **Number Of Teeth**: Sets the number of teeth.

-    **Pressure Angle**: Acute angle between the line of action and a normal to the line connecting the gear centers. Default is 20 °. See [Involute gear](https://en.wikipedia.org/wiki/Involute_gear).

-    **Profile Shift Coefficient**: The distance by which the reference profile is shifted outwards, normalized by the module. Default is zero. Profile shift may be positive or negative. <small>(v0.21)</small> 

-    **Root Fillet Coefficient**: The radius of the fillet at the root of the tooth, normalized by the module. Default is 0.38 as defined by the ISO rack. <small>(v0.21)</small> 

## Notes

-   In order for two gears to mesh they need to share the same module and pressure angle. [Expressions](Expressions.md) may help to ensure consistency. Their center distance needs to be `(NumberOfTeeth + OtherGear.NumberOfTeeth) * Modules / 2` (that is in case of the sum profile shift being zero). Subtract the number of teeth in case of an internal gear.

-   Profile shifting can be used to prevent undercut on gears with a small number of teeth. Another application is to adjust the center distance of two gears with a given number of teeth and module.

-   When visually checking for proper meshing or interferences a much lower value for **Deviation** is helpful, e.g. 0.05 instead of the default 0.5. Otherwise the representation in the [3D view](3D_view.md) may be too coarse.

-   For standard gears the most common pressure angle is 20 °, followed by 14,5 °. Other applications, notably [splines](https://en.wikipedia.org/wiki/Spline_(mechanical)), use higher angles.

-   The standard full-depth system uses an addendum coefficient of 1.0 and a dedendum coefficient of 1.25, resulting in a clearance of 0.25 (the difference between the addendum of the one gear and the dedendum of the other). The actual tooth length is the sum of both coefficients, multiplied by the module.

-   Tooth length reduction may be required to prevent undercut or to strengthen the teeth (see [stub teeth](https://khkgears.net/new/gear_knowledge/gear-nomenclature/stub-teeth.html)). For internal gears the addendum (here pointing inwards) may need shortening to avoid certain interferences or non-involute flanks; when indicated in combination with longer teeth of the pinion.

-   For splined shafts and hubs ISO 4156 defines the following parameters:

:   {\| class=\"wikitable\"

\|- ! Pressure Angle !! 30 ° (flat root) !! 30 ° (fillet root) !! 37,5 ° !! 45 ° \|- \| Addendum Coefficient \|\| 0.5 \|\| 0.5 \|\| 0.45 \|\| 0.4 \|- \| Dedendum Coefficient \|\| 0.75 \|\| 0.9 \|\| 0.7 \|\| 0.6 \|- \| Root Fillet Coefficient \|\| 0.2 \|\| 0.4 \|\| 0.3 \|\| 0.25 \|}

## Limitations

-   It is currently not possible to adjust the tooth thickness. Tooth and tooth space are distributed equally on the pitch circle. Thus the only way to control backlash is to adjust the center distance in a gear paring.
-   There is currently no [undercut](https://www.tec-science.com/mechanical-power-transmission/involute-gear/undercut/) in the generated gear profile. That means gears with a low number of teeth can interfere with the teeth of the mating gear. The lower limit depends on the **Pressure Angle** and is around 17 teeth for 20° and 32 for 14.5°. Most practical applications tolerate a missing undercut for gears a little smaller than this theoretical limit though.

## Tutorials

Video: [How to make gears in FreeCAD](https://www.youtube.com/watch?v=8VNhTrnFMfE)

## Related

-   [FCGear Workbench](FCGear_Workbench.md)




 {{PartDesign Tools navi}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign InvoluteGear
