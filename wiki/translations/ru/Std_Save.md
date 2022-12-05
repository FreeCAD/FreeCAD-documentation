---
- GuiCommand:/ru
   Name:Std Save
   Name/ru:Std Save
   MenuLocation:[Файл](Std_File_Menu/ru.md) → Сохранить
   Workbenches:All
   Shortcut:**Ctrl**+**S**
   SeeAlso:[Сохранить как...](Std_SaveAs/ru.md), [Std SaveCopy](Std_SaveCopy/ru.md), [Std SaveAll](Std_SaveAll/ru.md)
---

# Std Save/ru


</div>

## Описание

Команда **Сохранить** сохраняет активный документ.

## Применение

1.  There are several ways to invoke the command:
    -   Press the **<img src="images/Std_Save.svg" width=16px> [Std Save](Std_Save.md)** button.
    -   Select the **File → <img src="images/Std_Save.svg" width=16px> Save** option from the menu.
    -   Use the keyboard shortcut: **Ctrl**+**S**.
2.  For new documents: enter a filename in the dialog box and press the **Save** button.

## Опции

-   Для новых документов: нажмите **Esc** или кнопку **Отмена**, чтобы прервать выполнение команды.

## Примечания

-   This command can also be used to save dependency graphs. See [Std DependencyGraph](Std_DependencyGraph.md).

## Настройки

-   Путь к последнему файлу к которому была применена данная команда сохраняется в параметр: **Инструменты → Редактор параметров... → BaseApp → Preferences → General → FileOpenSavePath**.

## Программирование


**Смотрите так же:**

[Основы составления скриптов в FreeCAD](FreeCAD_Scripting_Basics/ru.md).

To save a document use the `save` method of the document object. A new document must first be saved with the `saveAs` method of the document object. For a scripting example see [Std New](Std_New.md).





{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std Save/ru
