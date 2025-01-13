---
 GuiCommand:
   Name: Assembly CreateJointSlider
   MenuLocation: Assembly , Create Slider Joint
   Workbenches: Assembly_Workbench
   Shortcut: **S**
   Version: 1.0
   SeeAlso: 
---

# Assembly CreateJointSlider

## Description

The <img alt="" src=images/Assembly_CreateJointSlider.svg  style="width:24px;"> [Assembly CreateJointSlider](Assembly_CreateJointSlider.md) tool creates a Slider joint (also called a prismatic joint) between two selected parts, allowing a linear movement along a single axis while restricting rotation.

## Usage

1.  Optionally select two geometric entities of two different shapes. Other selections will be rejected.
2.  There are several ways to invoke the tool:
    -   Press the **<img src="images/Assembly_CreateJointSlider.svg" width=16px> [Create Slider Joint](Assembly_CreateJointSlider.md)** button.
    -   Select the **Assembly → <img src="images/Assembly_CreateJointSlider.svg" width=16px> Create Slider Joint** option from the menu.
    -   Use the keyboard shortcut: **S**.
3.  The **Create Joint** dialog opens in the [Task panel](Task_panel.md) listing the pre-selected entities.
4.  For further steps see [Assembly CreateJointFixed](Assembly_CreateJointFixed#Usage.md).

## Properties

See also: [Property editor](Property_editor.md).

A **Slider** object is derived from an [App FeaturePython](App_FeaturePython.md) object and inherits all its properties. See [Assembly CreateJointFixed](Assembly_CreateJointFixed#Properties.md) for additional properties.




 {{Assembly_Tools_navi}}



---
⏵ [documentation index](../README.md) > [Assembly](Assembly_Workbench.md) > Assembly CreateJointSlider
