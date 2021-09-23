# Std ViewRotateLeft/ro
---
- GuiCommand:   Name:Std_RotateLeft   Workbenches:All   SeeAlso:...---


</div>


<div class="mw-translate-fuzzy">

**Rezumat**


</div>


<div class="mw-translate-fuzzy">

De completat


</div>

## Usage


<div class="mw-translate-fuzzy">

-   Press **Shift** + **Left** or go to **View → Standard views → Rotate Left**.


</div>

## Scripting


**See also:**

[FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

To rotate the view to the left use the `viewRotateLeft` method of the ActiveView object. This method is not available if FreeCAD is in console mode.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.ActiveView.viewRotateLeft()
FreeCADGui.ActiveDocument.ActiveView.getCameraOrientation()
```





{{Std Base navi

}}

---
[documentation index](../README.md) > Std ViewRotateLeft/ro
