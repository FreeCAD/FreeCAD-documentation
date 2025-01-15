---
 GuiCommand:
   Name: Std ToggleSelectability
   Name/ru: Std ToggleSelectability
   MenuLocation: Вид , Видимость , Откл/вкл выделяемость
   Workbenches: All
---

# Std ToggleSelectability/ru



## Описание

The **Std ToggleSelectability** command toggles the selectability of objects in [3D views](3D_view.md).



## Применение

1.  Select one or more objects.
2.  There are several ways to invoke the command:
    -   Select the **View → Visibility → <img src="images/Std_ToggleSelectability.svg" width=16px> Toggle selectability** option from the menu.
    -   Select the **<img src="images/Std_ToggleSelectability.svg" width=16px> Toggle selectability** option from the [Tree view](Tree_view.md) context menu or 3D view context menu.



## Примечания

-   The selectability of an object can also be changed through its related **Selectable** property in the [Property editor](Property_editor.md).

## Scripting


<div class="mw-translate-fuzzy">


**Смотрите так же:**

[Основы составления скриптов в FreeCAD](FreeCAD_Scripting_Basics/ru.md).


</div>

The `Selectable` property of an object determines its selectability.


```python
import FreeCADGui

obj = FreeCADGui.ActiveDocument.myObjectName

obj.Selectable = not obj.Selectable
```


<div class="mw-translate-fuzzy">





</div>



---
⏵ [documentation index](../README.md) > Std ToggleSelectability/ru
