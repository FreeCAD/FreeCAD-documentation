---
- GuiCommand:
   Name: Std ToggleSelectability
   MenuLocation: View -> Visibility -> Toggle selectability
   Workbenches: All
---

# Std ToggleSelectability/en

## Description

The **Std ToggleSelectability** command toggles the selectability of objects in [3D views](3D_view.md).

## Usage

1.  Select one or more objects.
2.  There are several ways to invoke the command:
    -   Select the **View → Visibility → <img src="images/Std_ToggleSelectability.svg" width=16px> Toggle selectability** option from the menu.
    -   Select the **<img src="images/Std_ToggleSelectability.svg" width=16px> Toggle selectability** option from the [Tree view](Tree_view.md) context menu. This option is not available in the [PartDesign Workbench](PartDesign_Workbench.md).
    -   Select the **<img src="images/Std_ToggleSelectability.svg" width=16px> Toggle selectability** option from the 3D view context menu.

## Notes

-   The selectability of an object can also be changed through its related **Selectable** property in the [Property editor](Property_editor.md) or the [Combo view](Combo_view.md).

## Scripting


**See also:**

[FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

The `Selectable` property of an object determines its selectability.


```python
import FreeCADGui

obj = FreeCADGui.ActiveDocument.myObjectName

if obj.Selectable == True:
  obj.Selectable = False
else:
  obj.Selectable = True
```





{{Std Base navi

}}



---
⏵ [documentation index](../README.md) > Std ToggleSelectability/en
