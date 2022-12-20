---
- GuiCommand:/pl
   Name:Std ProjectUtil
   Name/pl:Std: Narzędzia projektu
   MenuLocation:Przybory → Narzędzia projektu ...
   Workbenches:wszystkie
---

# Std ProjectUtil/pl

## Opis

Za pomocą polecenia **Narzędzia projektu** można wyodrębnić pliki z pliku projektu FreeCAD *(***.FCStd**), który w rzeczywistości jest plikiem \[<https://en.wikipedia.org/wiki/Zip_(file_format)>* ZIP\], i po ręcznej edycji utworzyć z nich nowy plik projektu.

![](images/Project_utility_en.png ) 
*Okno dialogowe Narzędzia projektu*

## Użycie

### Wyodrębnienie projektu 

1.  Wybierz z menu opcję **Przybory → <img src="images/Std_ProjectUtil.svg" width=16px> Narzędzie projektu ...**.
2.  Otworzy się okno dialogowe Narzędzie projektu.
3.  Naciśnij przycisk **...** po prawej stronie **Wyodrębnij projekt → Źródło**.
4.  Wybierz plik ***.FCStd**, który chcesz edytować.
5.  Naciśnij przycisk **...** po prawej stronie **Wyodrębnij projekt → Miejsce docelowe**.
6.  Wybierz folder, do którego ma zostać wyodrębniony plik projektu. Wskazane jest wybranie pustego folderu.
7.  Naciśnij przycisk **Rozpakuj**.
8.  Naciśnij przycisk **Zamknij**, aby zamknąć okno dialogowe.

### Edycja ręczna 

It is important to realize that the files inside a FreeCAD project file are interlinked. Only editing a single file will typically lead to errors. To make consistent edits across multiple files use a good code editor, such as [Notepad++](http://notepad-plus-plus.org/) (for the Windows OS) or [Notepadqq](https://notepadqq.com/s/) (for Linux OS).

### Create project 

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

## Uwagi

-   For more information about the FreeCAD project file format see [File Format FCStd](File_Format_FCStd.md).





{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std ProjectUtil/pl
