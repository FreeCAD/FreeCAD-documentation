---
 GuiCommand:
   Name: Assembly CreateJointGears
   MenuLocation: Assembly , Create Gear/Belt Joint , Create Gears Joint
   Workbenches: Assembly_Workbench
   Shortcut: 
   Version: 1.0
   SeeAlso: 
---

# Assembly CreateJointGears

## Description

The <img alt="" src=images/Assembly_CreateJointGears.svg  style="width:24px;"> [Assembly CreateJointGears](Assembly_CreateJointGears.md) tool creates a gears joint that couples the rotation of two parts of two different revolute joints. In connection with the already existing joints this joint can be used to simulate spur gears, bevel gears, crown gears, friction wheel gears, etc.

## Usage

1.  Optionally select two geometric entities of two different parts that have previously been used to define two Revolute joints.
2.  There are several ways to invoke the tool:
    -   Press the **<img src="images/Assembly_CreateJointGears.svg" width=16px> [Create Gears Joint](Assembly_CreateJointGears.md)** button.
    -   Select the **Assembly → Create Gear/Belt Joint → <img src="images/Assembly_CreateJointGears.svg" width=16px> Create Gears Joint** option from the menu.
3.  The **Create Joint** dialog opens in the [Task panel](Task_panel.md) listing the pre-selected entities.
4.  For further steps see [Assembly CreateJointFixed](Assembly_CreateJointFixed#Usage.md).

## Notes

-   Radius1 and Radius2 refer to the pitch circle of gears or the outer diameter of friction wheels. They store their values in the **Distance** and **Distance2** properties and they define the ratio between both rotations.
-   Since the values of both radii have no influence on the distance between the rotation axes and the units are canceled anyway you may consider to enter diameter values, or the number of teeth (no need to find the pitch diameter of bevel gears then) for both radii.
-   Use the same value for both radii to connect both ends of a flexible shaft (if the rotations don\'t match, either reverse one Revolute joint or use the Belt joint instead of this one).

## Properties

See also: [Property editor](Property_editor.md).

A **Gears** object is derived from an [App FeaturePython](App_FeaturePython.md) object and inherits all its properties. See [Assembly CreateJointFixed](Assembly_CreateJointFixed#Properties.md) for additional properties.




 {{Assembly_Tools_navi}}



---
⏵ [documentation index](../README.md) > [Assembly](Assembly_Workbench.md) > Assembly CreateJointGears
