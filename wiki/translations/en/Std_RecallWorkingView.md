---
- GuiCommand:
   Name:Std RecallWorkingView
   MenuLocation:View → Standard views → Recall working view
   Workbenches:All
   Shortcut:**End**
   Version:1.0
   SeeAlso:[Std StoreWorkingView](Std_StoreWorkingView.md), [Std FreezeViews](Std_FreezeViews.md)
---

# Std RecallWorkingView/en

## Description

The **Std RecallWorkingView** recalls the active [3D view](3D_view.md)\'s stored working view. For more information see [Std StoreWorkingView](Std_StoreWorkingView.md).

## Usage

1.  Make sure a [3D view](3D_view.md) is active for which the [Std StoreWorkingView](Std_StoreWorkingView.md) command has been used at least once.
2.  There are several ways to invoke the command:
    -   Select the **View → Standard views → Recall working view** option from the menu.
    -   Use the keyboard shortcut: **End**.

## Scripting


**See also:**

[FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

To recall the stored working view of the active 3D view:


```python
import FreeCADGui

FreeCADGui.runCommand("Std_RecallWorkingView", 0)
```





{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std RecallWorkingView/en
