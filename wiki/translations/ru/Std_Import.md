---
- GuiCommand:/ru
   Name:Std Import
   Name/ru:Std Import
   MenuLocation:Файл → Импортировать
   Workbenches:All
   Shortcut:**Ctrl**+**I**
   SeeAlso:[Std Open](Std_Open/ru.md), [Import Export](Import_Export/ru.md), [Import Export Preferences](Import_Export_Preferences/ru.md)
---

# Std Import/ru


</div>

## Описание

The **Std Import** command imports geometry from a different file format into the active document. Many file formats are supported and for some formats multiple import options exist. See [Import Export](Import_Export.md) for more information.

## Применение

1.  There are several ways to invoke the command:
    -   Select the **File → <img src="images/Std_Import.svg" width=16px> Import...** option from the menu.
    -   Use the keyboard shortcut: **Ctrl**+**I**.
2.  Optionally select the correct file format in the dialog box.
3.  Select a file.
4.  Press the **Open** button.

## Опции

-   Нажмите **Esc** или кнопку **Отмена**, чтобы отменить выполнение команды.

## Примечания

-   To convert an imported [mesh object](Mesh_Workbench.md) into a solid see the [Import from STL or OBJ](Import_from_STL_or_OBJ.md) tutorial.
-   To import into a new document you can use the [Std Open](Std_Open.md) command.
-   Some workbenches have additional import commands. See: [Import Export](Import_Export.md).

## Настройки

-   См. так же: [Настройки Импорта Экспорта](Import_Export_Preferences/ru.md).
-   Путь к последнему файлу к которому была применена данная команда сохраняется в параметр: **Инструменты → Редактор параметров... → BaseApp → Preferences → General → FileOpenSavePath**.
-   Путь к последнему импортированному файлу сохраняется в параметр: **Инструменты → Редактор параметров... → BaseApp → Preferences → General → FileImportFilter**.





{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [File_Formats](Category_File_Formats.md) > Std Import/ru
