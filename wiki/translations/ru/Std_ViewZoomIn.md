---
 GuiCommand:
   Name: Std ViewZoomIn
   Name/ru: Увеличить
   MenuLocation: Вид , Масштаб‏‎ , Увеличить
   Workbenches: All
   Shortcut: **Ctrl**+**+**
   SeeAlso: Std_ViewZoomOut/ru, Std_ViewBoxZoom/ru
---

# Std ViewZoomIn/ru



## Описание

The **Std ViewZoomIn** command zooms in in the active [3D view](3D_view.md).



## Применение

1.  There are several ways to invoke the command:
    -   Select the **View → Zoom → <img src="images/Std_ViewZoomIn.svg" width=16px> Zoom In** option from the menu.
    -   Use the keyboard shortcut: **Ctrl**+**+**.



## Примечания

-   With almost all [mouse navigation styles](Mouse_navigation.md) it is also possible to zoom with the scroll wheel of the mouse.



## Настройки

See also: [Preferences Editor](Preferences_Editor.md).

-   The zoom factor can be changed: **Edit → Preferences... → Display → Navigation → Zoom step**. This setting also affects scroll wheel zoom.

## Scripting


<div class="mw-translate-fuzzy">


**Смотрите так же:**

[Основы составления скриптов в FreeCAD](FreeCAD_Scripting_Basics/ru.md).


</div>

Use the `zoomIn` method of the View object to zoom in. The `zoomOut` method is also available.


```python
import FreeCADGui

view = FreeCADGui.ActiveDocument.ActiveView
view.zoomIn()
```





{{Std_Base_navi

}}



---
⏵ [documentation index](../README.md) > Std ViewZoomIn/ru
