---
- GuiCommand:
   Name:Std ViewRotateRight
   MenuLocation:View → Standard views → Rotate Right
   Workbenches:All
   Shortcut:**Shift**+**Right**
   SeeAlso:[Std ViewRotateLeft](Std_ViewRotateLeft.md)
---

# Std ViewRotateRight/ro


<div class="mw-translate-fuzzy">

**Rezumat**


</div>


<div class="mw-translate-fuzzy">

De completat


</div>

## Usage


<div class="mw-translate-fuzzy">

-   Press **Shift** + **Right** or go to **View → Standard views → Rotate Right**.


</div>

## Scripting


**See also:**

[FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

To rotate the view to the right use the `viewRotateRight` method of the ActiveView object. This method is not available if FreeCAD is in console mode.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.ActiveView.viewRotateRight()
FreeCADGui.ActiveDocument.ActiveView.getCameraOrientation()
```





{{Std Base navi

}}

---
[documentation index](../README.md) > Std ViewRotateRight/ro
