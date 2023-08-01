---
- GuiCommand:
   Name: Std StoreWorkingView
   MenuLocation: View - Standard views - Store working view
   Workbenches: All
   Shortcut: **Shift**+**End**
   Version: 0.21
   SeeAlso: [Std RecallWorkingView](Std_RecallWorkingView.md), [Std FreezeViews](Std_FreezeViews.md)
---

# Std StoreWorkingView/en

## Description

The **Std StoreWorkingView** command stores the camera settings of the active [3D view](3D_view.md) in its temporary working view. This view can be recalled with the [Std RecallWorkingView](Std_RecallWorkingView.md) command.

Each 3D view has its own working view. Storing a new working view will overwrite the existing working view of the active 3D view. When a 3D view is closed its working view is lost.

## Usage

1.  Make sure a [3D view](3D_view.md) is active.
2.  There are several ways to invoke the command:
    -   Select the **View → Standard views → Store working view** option from the menu.
    -   Use the keyboard shortcut: **Shift**+**End**.

## Scripting


**See also:**

[FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

To store the current camera settings of the active 3D view in a working view:


```python
import FreeCADGui

FreeCADGui.runCommand("Std_StoreWorkingView", 0)
```





{{Std Base navi

}}



---
⏵ [documentation index](../README.md) > Std StoreWorkingView/en
