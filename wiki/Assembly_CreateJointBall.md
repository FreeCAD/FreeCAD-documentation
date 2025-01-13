---
 GuiCommand:
   Name: Assembly CreateJointBall
   MenuLocation: Assembly , Create Ball Joint
   Workbenches: Assembly_Workbench
   Shortcut: **B**
   Version: 1.0
   SeeAlso: 
---

# Assembly CreateJointBall

## Description

The <img alt="" src=images/Assembly_CreateJointBall.svg  style="width:24px;"> [Assembly CreateJointBall](Assembly_CreateJointBall.md) tool creates a Ball joint (spherical joint) between two selected parts at a single point, allowing free rotation around the point while keeping both parts connected at this point.

## Usage

1.  Optionally select two geometric entities of two different shapes. Other selections will be rejected.
2.  There are several ways to invoke the tool:
    -   Press the **<img src="images/Assembly_CreateJointBall.svg" width=16px> [Create Ball Joint](Assembly_CreateJointBall.md)** button.
    -   Select the **Assembly → <img src="images/Assembly_CreateJointBall.svg" width=16px> Create Ball Joint** option from the menu.
    -   Use the keyboard shortcut: **B**.
3.  The **Create Joint** dialog opens in the [Task panel](Task_panel.md) listing the pre-selected entities.
4.  For further steps see [Assembly CreateJointFixed](Assembly_CreateJointFixed#Usage.md).

## Properties

See also: [Property editor](Property_editor.md).

A **Ball** object is derived from an [App FeaturePython](App_FeaturePython.md) object and inherits all its properties. See [Assembly CreateJointFixed](Assembly_CreateJointFixed#Properties.md) for additional properties.




 {{Assembly_Tools_navi}}



---
⏵ [documentation index](../README.md) > [Assembly](Assembly_Workbench.md) > Assembly CreateJointBall
