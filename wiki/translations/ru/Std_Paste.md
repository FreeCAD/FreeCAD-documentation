---
- GuiCommand:/ru
   Name:Std_Paste
   Name/ru:Вставить
   MenuLocation:Правка → Вставка
   Workbenches:Все
   Shortcut:**Ctrl**+**V**
   SeeAlso:[Вырезать](Std_Cut/ru.md), [Копировать](Std_Copy/ru.md), [Дублировать выбранное](Std_DuplicateSelection/ru.md)
---

## Описание

Команда **Вставить** вставляет объекты из буфера обмена в активный документ.

## Применение

1.  There are several ways to invoke the command:
    -   Press the **<img src="images/Std_Paste.svg" width=16px> [Std Paste](Std_Paste.md)** button.
    -   Select the **Edit → <img src="images/Std_Paste.svg" width=16px> Paste** option from the menu.
    -   Select the **<img src="images/Std_Paste.svg" width=16px> Paste** option from the [Tree view](Tree_view.md) context menu. Note that this option is only available when an exiting object has been selected.
    -   Use the keyboard shortcut: **Ctrl**+**V**.

## Примечания

-   FreeCAD will automatically change the internal names and, depending on the preferences, labels of objects to avoid name conflicts.
-   A spreadsheet cell alias that already exists in the spreadsheet will not be pasted.
-   When you are working in a FreeCAD text window, an input box or a spreadsheet, the standard keyboard shortcut **Ctrl**+**V**, in almost all cases, does not call the **Std Paste** command but uses the Paste function from the OS instead.
-   It is not possible to copy-paste native objects between FreeCAD and other applications.

## Настройки

-   Дублирование меток возможно, если **Инструменты → Редактор параметров... → BaseApp → Preferences → → Document → DuplicateLabels** равно `True`. Этот параметр также можно изменить в [Редакторе настроек](Preferences_Editor/ru#Документ.md).

## Программирование

The **Std Paste** command can be applied only after running the **[Std Copy](Std_Copy.md)** command:


```python
FreeCADGui.runCommand('Std_Copy')
FreeCADGui.runCommand('Std_Paste')
```





{{Std Base navi

}}  
