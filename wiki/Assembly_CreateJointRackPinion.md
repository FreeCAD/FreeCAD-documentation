---
 GuiCommand:
   Name: Assembly CreateJointRackPinion
   MenuLocation: Assembly , Create Rack and Pinion Joint
   Workbenches: Assembly_Workbench
   Shortcut: **Q**
   Version: 1.0
   SeeAlso: 
---

# Assembly CreateJointRackPinion

## Description

The <img alt="" src=images/Assembly_CreateJointRackPinion.svg  style="width:24px;"> [Assembly CreateJointRackPinion](Assembly_CreateJointRackPinion.md) tool creates a rack and pinion joint that couples the translation of a part of a slider joint and the rotation of a part of a revolute joint.

## Usage

1.  Optionally select two geometric entities of two different parts that have previously been used to define a Slider joint and a Revolute joint.
2.  There are several ways to invoke the tool:
    -   Press the **<img src="images/Assembly_CreateJointRackPinion.svg" width=16px> [Create Rack and Pinion Joint](Assembly_CreateJointRackPinion.md)** button.
    -   Select the **Assembly → <img src="images/Assembly_CreateJointRackPinion.svg" width=16px> Create Rack and Pinion Joint** option from the menu.
    -   Use the keyboard shortcut: **Q**.
3.  The **Create Joint** dialog opens in the [Task panel](Task_panel.md) listing the pre-selected entities.
4.  For further steps see [Assembly CreateJointFixed](Assembly_CreateJointFixed#Usage.md).

## Notes

-   Pitch radius refers to the pitch circle of the pinion. It is stored in the **Distance** property and is the basis to calculate the ratio between rotation and translation.

## Properties

See also: [Property editor](Property_editor.md).

A **RackPinion** object is derived from an [App FeaturePython](App_FeaturePython.md) object and inherits all its properties. See [Assembly CreateJointFixed](Assembly_CreateJointFixed#Properties.md) for additional properties.




 {{Assembly_Tools_navi}}



---
⏵ [documentation index](../README.md) > [Assembly](Assembly_Workbench.md) > Assembly CreateJointRackPinion
