---
- GuiCommand:/ru
   Name:Std DuplicateSelection
   Name/ru:Std DuplicateSelection
   MenuLocation:Правка → Дублировать выбранное
   Workbenches:Все
   SeeAlso:[Std Cut](Std_Cut.md), [Копировать](Std_Copy/ru.md), [Вставить](Std_Paste/ru.md)
---


</div>

## Описание

The **Std DuplicateSelection** command duplicates objects within the active document.

## Применение

1.  Select one or more objects.
2.  Select the {{MenuCommand|Edit → Duplicate selected object}} option from the menu.
3.  If the objects have dependencies that have not been selected, a dialog box will prompt you to specify which should be included.

## Примечания

-   FreeCAD will automatically change the internal names and, depending on the preferences, labels of objects to avoid name conflicts.

## Настройки

-   Duplicate labels are allowed if {{MenuCommand|Tools → Edit parameters... → BaseApp → Preferences → Document → DuplicateLabels}} is set to `True`. This setting can also be changed in the [Preferences Editor](Preferences_Editor#Document.md).

## Scripting

The **Std DuplicateSelection** command can be applied after selecting one or more objects in the [Tree view](Tree_view.md):


```python
FreeCADGui.runCommand('Std_DuplicateSelection')
```

The selection can be manual (by using the mouse), or via the [Python console](Python_console.md).
To know more about selecting objects programmatically, refer to [Selection methods](Selection_methods.md).





{{Std Base navi

}}  
