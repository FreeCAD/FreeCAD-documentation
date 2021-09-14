---
- GuiCommand:/ru
   Name/ru:Дублировать выбранное
   Name:Std_DuplicateSelection
   MenuLocation:Правка → Дублировать выбранное
   Workbenches:All
   SeeAlso:[Вырезать](Std_Cut/ru.md), [Копировать](Std_Copy/ru.md), [Вставить](Std_Paste/ru.md)
---

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

## Программирование

The **Std DuplicateSelection** command can be applied after selecting one or more objects in the [Tree view](Tree_view.md):


```python
FreeCADGui.runCommand('Std_DuplicateSelection')
```

The selection can be manual (by using the mouse), or via the [Python console](Python_console.md).
To know more about selecting objects programmatically, refer to [Selection methods](Selection_methods.md).





{{Std Base navi

}}  
