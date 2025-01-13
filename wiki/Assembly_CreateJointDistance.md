---
 GuiCommand:
   Name: Assembly CreateJointDistance
   MenuLocation: Assembly , Create Distance Joint
   Workbenches: Assembly_Workbench
   Shortcut: **D**
   Version: 1.0
   SeeAlso: 
---

# Assembly CreateJointDistance

## Description

The <img alt="" src=images/Assembly_CreateJointDistance.svg  style="width:24px;"> [Assembly CreateJointDistance](Assembly_CreateJointDistance.md) tool creates a Distance joint between two selected parts, fixing the distance between both parts.

## Usage

1.  Optionally select two geometric entities of two different shapes. Other selections will be rejected.
2.  There are several ways to invoke the tool:
    -   Press the **<img src="images/Assembly_CreateJointDistance.svg" width=16px> [Create Distance Joint](Assembly_CreateJointDistance.md)** button.
    -   Select the **Assembly → <img src="images/Assembly_CreateJointDistance.svg" width=16px> Create Distance Joint** option from the menu.
    -   Use the keyboard shortcut: **D**.
3.  The **Create Joint** dialog opens in the [Task panel](Task_panel.md) listing the pre-selected entities.
4.  For further steps see [Assembly CreateJointFixed](Assembly_CreateJointFixed#Usage.md).

## Notes

Tool tip says a distance of 0 results in a co-planar joint between the selected planar elements, or a tangent joint between a cylindrical and a planar element. Neither seems to work in weekly build 0.22.-.37645.

## Properties

See also: [Property editor](Property_editor.md).

A **Distance** object is derived from an [App FeaturePython](App_FeaturePython.md) object and inherits all its properties. See [Assembly CreateJointFixed](Assembly_CreateJointFixed#Properties.md) for additional properties.




 {{Assembly_Tools_navi}}



---
⏵ [documentation index](../README.md) > [Assembly](Assembly_Workbench.md) > Assembly CreateJointDistance
