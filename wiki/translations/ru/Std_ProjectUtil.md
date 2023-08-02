---
- GuiCommand:
   Name: Std ProjectUtil
   MenuLocation: Tools -> Project utility...
   Workbenches: All
---

# Std ProjectUtil/ru



## Описание

With the **Std ProjectUtil** command you can extract files from a FreeCAD project file (***.FCStd**), which is in fact a [ZIP](https://en.wikipedia.org/wiki/Zip_(file_format)) file, and, after manual edits, create a new project file from them.

![](images/Project_utility_en.png ) 
*The Project utility dialog box*



## Применение

### Extract project 

1.  Select the **Tools → <img src="images/Std_ProjectUtil.svg" width=16px> Project utility...** option from the menu.
2.  The Project utility dialog box opens.
3.  Press the **...** button to the right of **Extract project → Source**.
4.  Select the ***.FCStd** file you want to edit.
5.  Press the **...** button to the right of **Extract project → Destination**.
6.  Select a folder where the project file should be extracted. It is advisable to select an empty folder.
7.  Press the **Extract** button.
8.  Press the **Close** button to close the dialog box.

### Manual edits 

It is important to realize that the files inside a FreeCAD project file are interlinked. Only editing a single file will typically lead to errors. To make consistent edits across multiple files use a good code editor, such as [Notepad++](http://notepad-plus-plus.org/) (for the Windows OS) or [Notepadqq](https://notepadqq.com/s/) (for Linux OS).



### Создание проекта 

1.  Select the **Tools → <img src="images/Std_ProjectUtil.svg" width=16px> Project utility...** option from the menu.
2.  The Project utility dialog box opens.
3.  Press the **...** button to the right of **Create project → Source**.
4.  Select the **Document.xml** file. The command will be automatically find all linked files.
5.  Press the **...** button to the right of **Create project → Destination**.
6.  Select a folder where the new project file should be created.
7.  Press the **Create** button.
8.  A new project file with a fixed name, **project.fcstd**, is created in the selected folder. There is no warning if a file with that name already exists.
9.  Optionally check the {{CheckBox|TRUE|Load project file after creation}} checkbox.
10. Press the **Close** button to close the dialog box.



## Примечания

-   For more information about the FreeCAD project file format see [File Format FCStd](File_Format_FCStd.md).





{{Std Base navi

}}



---
⏵ [documentation index](../README.md) > Std ProjectUtil/ru
