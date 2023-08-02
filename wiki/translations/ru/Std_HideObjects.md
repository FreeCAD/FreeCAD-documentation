---
- GuiCommand:
   Name: Std HideObjects
   Name/ru: Std HideObjects
   MenuLocation: Вид -> Видимость -> Скрыть все объекты
   Workbenches: All
   SeeAlso: Std_ToggleVisibility/ru, Std_ShowSelection/ru, Std_HideSelection/ru, Std_ToggleObjects/ru, Std_ShowObjects/ru
---

# Std HideObjects/ru

## Описание

The **Std HideObjects** command hides all objects belonging to the active document in [3D views](3D_view.md).

## Применение

1.  Выберите пункт меню **Вид → Видимость → <img src="images/Std_HideObjects.svg" width=16px> Скрыть все объекты**.

## Примечания

-   Invisible objects are displayed with a greyed out label and a greyed out icon in the [Tree view](Tree_view.md).
-   The action of this command cannot be undone with [Std Undo](Std_Undo.md).
-   The visibility of an object can also be changed through its related **Visibility** property in the [Property editor](Property_editor.md) or the [Combo view](Combo_view.md).

## Программирование


**Смотрите так же:**

[Основы составления скриптов в FreeCAD](FreeCAD_Scripting_Basics/ru.md).

Пример скрипта см. в описании команды [\"Видимость\"](Std_ToggleVisibility/ru.md).





{{Std Base navi

}}



---
⏵ [documentation index](../README.md) > Std HideObjects/ru
