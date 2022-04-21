---
- GuiCommand:/de
   Name:Std ToggleSelectability
   Name/de:Std AuswählbarkeitUmschalten
   MenuLocation:Ansicht → Sichtbarkeit → Selektierbarkeit an/aus
   Workbenches:Alle
---

# Std ToggleSelectability/de

## Beschreibung

Der Befehl **Std AuswählbarkeitUmschalten** schaltet die Auswählbarkeit von Objekten in den [3D-Ansichten](3D_view.md) um.

## Anwendung

1.  Select one or more objects.
2.  There are several ways to invoke the command:
    -   Select the **View → Visibility → <img src="images/Std_ToggleSelectability.svg" width=16px> Toggle selectability** option from the menu.
    -   Select the **<img src="images/Std_ToggleSelectability.svg" width=16px> Toggle selectability** option from the [Tree view](Tree_view.md) context menu. This option is not available in the [PartDesign Workbench](PartDesign_Workbench.md).
    -   Select the **<img src="images/Std_ToggleSelectability.svg" width=16px> Toggle selectability** option from the 3D view context menu.

## Hinweise

-   The selectability of an object can also be changed through its related **Selectable** property in the [Property editor](Property_editor.md) or the [Combo view](Combo_view.md).

## Skripten


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
![](images/Right_arrow.png) [documentation index](../README.md) > Std ToggleSelectability/de
