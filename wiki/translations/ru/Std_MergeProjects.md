---
- GuiCommand:/ru
   Name:Std MergeProjects
   Name/ru:Std MergeProjects
   MenuLocation:Файл → Объединить проект 
   Workbenches:All
---

# Std MergeProjects/ru


</div>

## Описание

Команда \"Объединить проект\...\" добавляет содержимое FreeCAD файла в текущий документ.

## Применение

1.  Select the **File → <img src="images/Std_MergeProjects.svg" width=16px> Merge project...** option from the menu.
2.  Select a FreeCAD file in the dialog box.
3.  Press the **Open** button.

## Опции

-   Нажмите **Esc** или кнопку **Отмена**, чтобы отменить выполнение команды.

## Примечания

-   A project cannot be merged with itself, selecting the current file is not allowed.
-   FreeCAD will automatically change the internal names and, depending on the preferences, labels of objects to avoid name conflicts.

## Настройки

-   The last used file location is stored: **Tools → Edit parameters... → BaseApp → Preferences → General → FileOpenSavePath**.
-   Duplicate labels are allowed if **Tools → Edit parameters... → BaseApp → Preferences → Document → DuplicateLabels** is set to `True`. This setting can also be changed in the [Preferences Editor](Preferences_Editor#Document.md).





{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std MergeProjects/ru
