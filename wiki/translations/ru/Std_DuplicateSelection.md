---
- GuiCommand:
   Name/ru: Дублировать выбранное
   Name: Std_DuplicateSelection
   MenuLocation: Правка -> Дублировать выбранное
   Workbenches: All
   SeeAlso: Std_Cut/ru, Std_Copy/ru, Std_Paste/ru
---

# Std DuplicateSelection/ru

## Описание

The **Std DuplicateSelection** command duplicates objects within the active document.

## Применение

1.  Select one or more objects.
2.  Select the **Edit → Duplicate selected object** option from the menu.
3.  If the objects have dependencies that have not been selected, a dialog box will prompt you to specify which should be included.

## Примечания

-   FreeCAD will automatically change the internal names and, depending on the preferences, labels of objects to avoid name conflicts.

## Настройки

-   Duplicate labels are allowed if **Tools → Edit parameters... → BaseApp → Preferences → Document → DuplicateLabels** is set to `True`. This setting can also be changed in the [Preferences Editor](Preferences_Editor#Document.md).





{{Std Base navi

}}



---
⏵ [documentation index](../README.md) > Std DuplicateSelection/ru
