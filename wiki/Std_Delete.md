---
- GuiCommand:
   Name:Std Delete
   MenuLocation:Edit → Delete
   Workbenches:All
   Shortcut:**Del**
---

# Std Delete

## Description

The **Std Delete** command deletes selected objects.

## Usage

1.  Select one or more objects.
2.  There are several ways to invoke the command:
    -   Select the **Edit → <img src="images/Std_Delete.svg" width=16px> Delete** option from the menu.
    -   Select the **<img src="images/Std_Delete.svg" width=16px> Delete** option from the [Tree view](Tree_view.md) context menu or [3D view](3D_view.md) context menu.
    -   Use the keyboard shortcut: **Del**.

## Scripting


**See also:**

[FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

To delete an object use the `removeObject` method of the document object.

 
```python
import FreeCAD

FreeCAD.ActiveDocument.removeObject("myObjectName")
```




 {{Std Base navi}}

---
[documentation index](../README.md) > Std Delete
