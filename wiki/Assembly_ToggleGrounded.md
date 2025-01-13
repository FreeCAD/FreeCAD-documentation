---
 GuiCommand:
   Name: Assembly ToggleGrounded
   MenuLocation: Assembly , Toggle grounded
   Workbenches: Assembly_Workbench
   Shortcut: **G**
   Version: 1.0
   SeeAlso: 
---

# Assembly ToggleGrounded

## Description

The <img alt="" src=images/Assembly_ToggleGrounded.svg  style="width:16px;"> [Assembly ToggleGrounded](Assembly_ToggleGrounded.md) tool fixes the position and orientation of a shape in relation to the coordinate system of the Assembly it belongs to.

## Usage

1.  Select one or more parts.
2.  There are several ways to invoke the tool:
    -   Press the **<img src="images/Assembly_ToggleGrounded.svg" width=16px> [Toggle grounded](Assembly_ToggleGrounded.md)** button.
    -   Select the **Assembly → <img src="images/Assembly_ToggleGrounded.svg" width=16px> Toggle grounded** option from the menu.
    -   Use the keyboard shortcut: **G**.
3.  A GroundedJoint is added for each selected part.

## Notes

-   A grounded joint will display a red lock icon in the 3D view, around the center of mass of the grounded component. To hide the lock, toggle the joint\'s **Visibility** to off.

## Properties

See also: [Property editor](Property_editor.md).

A **GroundedJoint** object is derived from an [App FeaturePython](App_FeaturePython.md) object and inherits all its properties. It also has the following additional properties:

### Data


{{TitleProperty|Ground}}

-    **Object To Ground|Link**: The object to ground.

-    **Placement|Placement**: This is where the part is grounded. See [Placement](Placement.md).




 {{Assembly_Tools_navi}}



---
⏵ [documentation index](../README.md) > [Assembly](Assembly_Workbench.md) > Assembly ToggleGrounded
