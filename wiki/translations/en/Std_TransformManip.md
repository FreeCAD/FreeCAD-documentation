---
 GuiCommand:
   Name: Std TransformManip
   MenuLocation: Edit , Transform
   Workbenches: All
   SeeAlso: Std_UserEditMode
---

# Std TransformManip/en

## Description

The **Std TransformManip** command allows you to apply rotation increments and translation increments to an object.

<img alt="" src=images/Std_TransformManip_Example.png  style="width:400px;">

## Usage

1.  Select an object with a **Placement** property. See [Notes](#Notes.md).
2.  There are several ways to invoke the command:
    -   Select the **Edit → <img src="images/Std_TransformManip.svg" width=16px> Transform** option from the menu.
    -   Select the **<img src="images/Std_TransformManip.svg" width=16px> Transform** option from the [Tree view](Tree_view.md) context menu.
    -   If [edit mode](Std_UserEditMode.md) is set to **<img src="images/Std_UserEditModeTransform.svg" width=16px> Transform** you can also double-click the object in the Tree view.
3.  The **Increments** task panel opens.
4.  Optionally adjust the increments parameters.
5.  Do one or more of the following:
    -   Press and hold the left mouse button on an axis arrow and drag to translate the object along that axis.
    -   Press and hold the left mouse button on a plane and drag to translate the object along that plane.
    -   Press and hold the left mouse button on a sphere and drag to rotate the object around that axis.
6.  Do one of the following:
    -   Press the **OK** button to confirm and finish the command.
    -   Press the **Cancel** button to revert the applied transformations and finish the command. <small>(v0.22)</small> 

## Notes

-   As soon as you rotate/move the object in the [3D view](3D_view.md), changes are applied.
-   Some objects with a **Placement** property, such as sketches, cannot be manipulated, neither can objects that are attached to other objects.
-   There is no **Cancel** button in {{VersionMinus|0.21}}, in those versions you can press the **OK** button and use the <img alt="" src=images/Std_Undo.svg  style="width:20px;"> [Undo](Std_Undo.md) command to revert changes afterwards.





{{Std Base navi

}}



---
⏵ [documentation index](../README.md) > Std TransformManip/en
