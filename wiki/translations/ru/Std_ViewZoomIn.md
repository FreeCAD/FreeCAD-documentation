---
- GuiCommand:/ru
   Name:Std ViewZoomIn
   Name/ru:Увеличить
   MenuLocation:Вид → Масштаб‏‎ → Увеличить
   Workbenches:All
   Shortcut:**Ctrl**+**+**
   SeeAlso:[Уменьшить](Std_ViewZoomOut/ru.md), [Увеличить область](Std_ViewBoxZoom/ru.md)
---

# Std ViewZoomIn/ru

## Описание

The **Std ViewZoomIn** command zooms in in the active [3D view](3D_view.md).

## Применение

1.  There are several ways to invoke the command:
    -   Select the **View → Zoom → <img src="images/Std_ViewZoomIn.svg" width=16px> Zoom In** option from the menu.
    -   Use the keyboard shortcut: **Ctrl**+**+**.

## Примечания

-   It is also possible to zoom with the mouse scroll wheel.

## Настройки

-   The zoom factor can be changed in the preferences: **Edit → Preferences... → Display → Navigation → Zoom step**. This setting also affects scroll wheel zoom. See [Preferences Editor](Preferences_Editor#Navigation.md).

## Scripting


**Смотрите так же:**

[Основы составления скриптов в FreeCAD](FreeCAD_Scripting_Basics/ru.md).

To zoom in use the `zoomIn` method of the ActiveView object. This method is not available if FreeCAD is in console mode.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.ActiveView.zoomIn()
```





{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std ViewZoomIn/ru
