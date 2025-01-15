---
 GuiCommand:
   Name: Std Export
   Name/ru: Std Export
   MenuLocation: Файл , Экспорт
   Workbenches: All
   Shortcut: **Ctrl**+**E**
   SeeAlso: Std_PrintPdf/ru, Import_Export/ru, Import_Export_Preferences/ru
---

# Std Export/ru


</div>



## Описание

The **Std Export** command exports selected objects to a different file format. Many file formats are supported and for some formats multiple export options exist. See [Import Export](Import_Export.md) for more information.



## Применение

1.  Select one or more objects. To avoid exporting invisible or duplicate objects:
    -   Be careful when you use **Ctrl**+**A** to select all objects. This will also select invisible objects.
    -   Select a [PartDesign Body](PartDesign_Body.md) by only picking the body itself or its last feature.
    -   Select a [Std Group](Std_Group.md) or a [Std Part](Std_Part.md) by only picking the parent object itself or the objects nested inside it.
    -   Do not use the [Std SelectAll](Std_SelectAll.md) command as it will also select sub-elements of PartDesign Bodies.
2.  There are several ways to invoke the command:
    -   Select the **File → <img src="images/Std_Export.svg" width=16px> Export...** option from the menu.
    -   Use the keyboard shortcut: **Ctrl**+**E**.
3.  Select the correct file format in the dialog box.
4.  Enter a filename.
5.  Press the **Save** button.



## Опции

-   Нажмите **Esc** или кнопку **Отмена**, чтобы отменить выполнение команды.



## Примечания

-   To export a [mesh object](Mesh_Workbench.md) to a solid file format it must first be converted. See the [Import from STL or OBJ](Import_from_STL_or_OBJ.md) tutorial.
-   Some workbenches have additional export commands. See [Import Export](Import_Export.md).



## Настройки


<div class="mw-translate-fuzzy">

-   См. так же: [Настройки Импорта Экспорта](Import_Export_Preferences/ru.md).
-   Путь к последнему файлу к которому была применена данная команда сохраняется в параметр: **Инструменты → Редактор параметров... → BaseApp → Preferences → General → FileOpenSavePath**.
-   Путь к последнему экспортированному файлу сохраняется в параметр: **Инструменты → Редактор параметров... → BaseApp → Preferences → General → FileExportFilter**.


</div>



---
⏵ [documentation index](../README.md) > [File_Formats](Category_File_Formats.md) > Std Export/ru
