---
 GuiCommand:
   Name: Std MergeProjects
   Name/pl: Std: Scal projekt
   MenuLocation: Plik , Scal projekt ...
   Workbenches: wszystkie
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



## Tworzenie skryptów 


**Zobacz również:**

[FreeCAD podstawy tworzenia skryptów](FreeCAD_Scripting_Basics/pl.md).

Aby scalić obiekt, należy użyć metody `mergeProject` obiektu *document*.


```python
import FreeCAD

FreeCAD.ActiveDocument.mergeProject("Path_to_FCStd_project_file")
```





{{Std Base navi

}}



---
⏵ [documentation index](../README.md) > Std MergeProjects/pl
