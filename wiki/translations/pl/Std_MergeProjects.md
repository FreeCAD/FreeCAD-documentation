---
- GuiCommand:/pl
   Name:Std MergeProjects
   Name/pl:Std: Scal projekt
   MenuLocation:Plik → Scal projekt ...
   Workbenches:wszystkie
---

# Std MergeProjects/pl



## Opis

Polecenie **Scal projekt** dodaje zawartość pliku FreeCAD do aktywnego dokumentu.



## Użycie

1.  Wybierz z menu opcję **Plik → <img src="images/Std_MergeProjects.svg" width=16px> Scal projekt ...**.
2.  Wprowadź nazwę pliku w oknie dialogowym.
3.  Naciśnij przycisk **Otwórz**.



## Opcje

-   Naciśnij przycisk **Esc** lub przycisk **Anuluj** aby przerwać wykonywanie polecenia.



## Uwagi

-   Projekt nie może być łączony z samym sobą, wybieranie bieżącego pliku jest niedozwolone.
-   FreeCAD automatycznie zmieni wewnętrzne nazwy oraz, w zależności od preferencji, etykiety obiektów, aby uniknąć konfliktów nazw.



## Ustawienia

-   Przechowywana jest ostatnio używana lokalizacja pliku: **Przybory → Edycja parametrów ... → BaseApp → Preferencje → Ogólne → FileOpenSavePath**.
-   Duplikaty etykiet są dozwolone, jeśli parametr **Przybory → Edycja parametrów ... → BaseApp → Preferencje → Dokument → DuplicateLabels** jest ustawiony na wartość {{TRUE/pl}}. To ustawienie można również zmienić w [Edytorze ustawień](Preferences_Editor/pl#Dokument.md).

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
![](images/Right_arrow.png) [documentation index](../README.md) > Std MergeProjects/pl
