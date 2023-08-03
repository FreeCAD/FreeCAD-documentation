---
 GuiCommand:
   Name: Std MergeProjects
   Name/ru: Std MergeProjects
   MenuLocation: Файл , Объединить проект 
   Workbenches: All
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

## Scripting


**See also:**

[FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

To merge a project use the {{Incode|mergeProject}} method of the document object.


```python
import FreeCAD

FreeCAD.ActiveDocument.mergeProject("Path_to_FCStd_project_file")
```





{{Std Base navi

}}



---
⏵ [documentation index](../README.md) > Std MergeProjects/ru
