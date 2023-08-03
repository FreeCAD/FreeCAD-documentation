---
 GuiCommand:
   Name: Std ShowObjects
   Name/ru: Std ShowObjects
   MenuLocation: Вид , Видимость , Показать все объекты
   Workbenches: All
   SeeAlso: Std_ToggleVisibility/ru, Std_ShowSelection/ru, Std_HideSelection/ru, Std_ToggleObjects/ru, Std_HideObjects/ru
---

# Std ShowObjects/ru

## Описание

The **Std ShowObjects** command shows all objects belonging to the active document in [3D views](3D_view.md). Be careful when you use this command as it will also show sub-elements of [PartDesign bodies](PartDesign_Body.md) and objects used for [Part Booleans](Part_Boolean.md). In most cases these should stay invisible.

## Применение

1.  Выберите пункт меню **Вид → Видимость → <img src="images/Std_ShowObjects.svg" width=16px> Показать все объекты**.

## Примечания

-   The action of this command cannot be undone with [Std Undo](Std_Undo.md).
-   The visibility of an object can also be changed through its related **Visibility** property in the [Property editor](Property_editor.md) or the [Combo view](Combo_view.md).

## Программирование


**Смотрите так же:**

[Основы составления скриптов в FreeCAD](FreeCAD_Scripting_Basics/ru.md).

Пример скрипта см. в описании команды [\"Видимость\"](Std_ToggleVisibility/ru.md).





{{Std Base navi

}}



---
⏵ [documentation index](../README.md) > Std ShowObjects/ru
