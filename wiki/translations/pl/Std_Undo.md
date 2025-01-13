---
 GuiCommand:
   Name: Std Undo
   Name/pl: Std: Cofnij
   MenuLocation: Edycja , Cofnij
   Workbenches: wszystkie
   Shortcut: **Ctrl**+**Z**
   SeeAlso: Std_Redo/pl
---

# Std Undo/pl



## Opis

Polecenie **Cofnij** cofa ostatnią czynność



## Użycie

1.  Istnieje kilka sposobów na wywołanie polecenia:
    -   Wciśnij przycisk **<img src="images/Std_Undo.svg" width=16px> [Cofnij](Std_Undo/pl.md)**.
    -   Wybierz z menu opcję **Edycja → <img src="images/Std_Undo.svg" width=16px> Cofnij**.
    -   Użyj skrótu klawiszowego: **Ctrl** + **Z**.



## Opcje

-   Aby cofnąć wiele czynności, kliknij na małą czarną strzałkę w dół po prawej stronie przycisku **<img src="images/Std_Undo.svg" width=16px> [Std Cofnij](Std_Undo/pl.md)** i wybierz odpowiednią pozycję z listy.



## Ustawienia

Zobacz też: [Edytor preferencji](Preferences_Editor/pl.md).

-   Funkcję Cofnij / Ponów można wyłączyć, odznaczając opcję **Edycja → Preferencje... → Ogólne → Dokument → Używanie Cofnij/Ponów w dokumentach**, ale nie jest to zalecane.
-   Maksymalna liczba kroków Cofnij / Ponów jest kontrolowana przez opcję **Edycja → Preferencje... → Ogólne → Dokument → Maksymalna liczba kroków Cofnij/Ponów**.



## Tworzenie skryptów 

Zobacz również stronę: [Dokumentacja API generowana automatycznie](https://freecad.github.io/SourceDoc/) oraz [Podstawy pisania skryptów dla FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Aby cofnąć ostatnią czynność, należy użyć metody `undo` obiektu dokumentu. Dostępny jest też jej odpowiednik w postaci metody `redo`.


```python
import FreeCAD

FreeCAD.ActiveDocument.undo()
```

Gdy FreeCAD działa w trybie czysto konsolowym *(CLI)*, mechanizm cofania / przywracania nie jest domyślnie włączony. Musi on być jawnie aktywowany dla każdego dokumentu.


```python
import FreeCAD

FreeCAD.ActiveDocument.UndoMode = 1
```





{{Std_Base_navi

}}



---
⏵ [documentation index](../README.md) > Std Undo/pl
