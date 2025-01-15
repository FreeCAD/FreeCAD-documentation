---
 GuiCommand:
   Name: Std_Open
   Name/ru: Открыть...
   MenuLocation: Std_File_Menu/ru , Открыть...
   Workbenches: All
   Shortcut: **Ctrl**+**O**
   SeeAlso: Std_Import/ru,<br>Std_New/ru
---

# Std Open/ru



## Описание

The **Std Open** command opens a file. If the file is not a native FreeCAD file (\*.FCStd) its geometry will be imported into a new document. See [Std Import](Std_Import.md) for more information.



## Применение

1.  There are several ways to invoke the command:
    -   Press the **<img src="images/Std_Open.svg" width=16px> [Open...](Std_Open.md)** button.
    -   Select the **File → <img src="images/Std_Open.svg" width=16px> Open...** option from the menu.
    -   Use the keyboard shortcut: **Ctrl**+**O**.
2.  Optionally select the correct file format in the dialog box.
3.  Select a file.
4.  Press the **Open** button.



## Опции

-   Нажмите **Esc** или кнопку **Отмена**, чтобы отменить выполнение команды.



## Программирование


<div class="mw-translate-fuzzy">


**Смотрите так же:**

[Основы составления скриптов в FreeCAD](FreeCAD_Scripting_Basics/ru.md).


</div>

To open a document use the `open(filepath)` method or the `openDocument(filepath, [hidden<nowiki>=</nowiki>False])` method of the FreeCAD application.

These methods create and return a document and load a project file into it. The `filepath` argument must be a string pointing to an existing file. If the file doesn\'t exist or the file cannot be loaded an I/O exception is thrown. In this case the created document is kept, but will be empty. If `hidden<nowiki>=</nowiki>True` is used, the document won\'t be displayed in the GUI and no tab will appear for it. This allows performing automatic operations on a document and closing it without disrupting the user interface.

Примеры составления скрипта смотри в описании команды [\"Создать\"](Std_New#Scripting/ru.md).


<div class="mw-translate-fuzzy">





</div>



---
⏵ [documentation index](../README.md) > Std Open/ru
