---
- GuiCommand:/ru
   Name:Std_Copy
   Name/ru:Копировать
   MenuLocation:Правка → Копировать
   Workbenches:Все
   Shortcut:**Ctrl**+**C**
   SeeAlso:[Вырезать](Std_Cut/ru.md), [Вставить](Std_Paste/ru.md), [Дублировать выбранное](Std_DuplicateSelection/ru.md)
---

## Описание

Команда **Вырезать** копирует объект(ы) в Буфер обмена.

## Применение

1.  Select one or more objects.
2.  There are several ways to invoke the command:
    -   Press the **<img src="images/Std_Copy.svg" width=16px> [Std Copy](Std_Copy.md)** button.
    -   Select the {{MenuCommand|Edit → <img src="images/Std_Copy.svg" width=16px> Copy}} option from the menu.
    -   Select the {{MenuCommand|<img src="images/Std_Copy.svg" width=16px> Copy}} option from the [Tree view](Tree_view.md) context menu.
    -   Use the keyboard shortcut: **Ctrl**+**C**.
3.  If the objects have dependencies that have not been selected, a dialog box will prompt you to specify which should be included.

## Примечания

-   When you are working in a FreeCAD text window, an input box or a spreadsheet, the standard keyboard shortcut **Ctrl**+**C**, in almost all cases, does not call the **Std Copy** command but uses the Copy function from the OS instead.
-   It is not possible to copy-paste native objects between FreeCAD and other applications.

## Программирование

Команда \"Копировать\" может быть применена, только после выбора одного или нескольких объектов в [Дереве проекта](Tree_view/ru.md):


```python
FreeCADGui.runCommand('Std_Copy')
FreeCADGui.runCommand('Std_Paste')
```

Выбор объектов перед операцией копирования может быть сделан как вручную (используя мышь), так и программно, через [Python консоль](Python_console/ru.md).
Больше о выборе объектов через программный код, можно узнать в [методах выбора](Selection_methods/ru.md).





{{Std Base navi

}}  
