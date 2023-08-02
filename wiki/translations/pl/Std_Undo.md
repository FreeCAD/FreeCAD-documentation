---
- GuiCommand:
   Name: Std Undo
   Name/pl: Std: Cofnij
   MenuLocation: Edycja -> Cofnij
   Workbenches: wszystkie
   Shortcut: **Ctrl**+**Z**
   SeeAlso: Std_Redo/pl
---

# Std Undo/pl

## Opis

Polecenie **Cofnij** cofa ostatnią czynność

## Użycie

1.  Istnieje kilka sposobów na wywołanie polecenia:
    -   Naciśnij przycisk **<img src="images/Std_Undo.svg" width=16px> [Cofnij](Std_Undo.md)**.
    -   Wybierz z menu opcję **Edycja → <img src="images/Std_Undo.svg" width=16px> Cofnij**.
    -   Użyj skrótu klawiaturowego: **Ctrl** + **Z**.

## Opcje

-   Aby cofnąć wiele czynności, kliknij na małą czarną strzałkę w dół po prawej stronie przycisku **<img src="images/Std_Undo.svg" width=16px> [Std Cofnij](Std_Undo.md)** i wybierz odpowiednią pozycję z listy.

## Ustawienia

-   Funkcję Cofnij / Ponów można wyłączyć, ustawiając parametr **Przybory → Edycja parametrów... → BaseApp → Preferencje → Dokument → UżywanieUndo** na wartość {{FALSE/pl}}, ale nie jest to zalecane. To ustawienie można również zmienić w [Edytorze ustawień](Preferences_Editor/pl#Dokument.md).
-   Maksymalna liczba kroków Cofnij / Ponów jest kontrolowana przez parametr **Przybory → Edycja parametrów... → BaseApp → Preferencje → Dokument → MaxUndoSize**. Ustawienie to można również zmienić w [Edytorze ustawień](Preferences_Editor/pl#Dokument.md).

## Tworzenie skryptów 


**Zobacz również:**

[FreeCAD podstawy tworzenia skryptów](FreeCAD_Scripting_Basics/pl.md).

Aby cofnąć ostatnią czynność, należy użyć metody `undo` obiektu dokumentu.


```python
import FreeCAD

FreeCAD.ActiveDocument.undo()
```

Gdy FreeCAD działa w trybie czysto konsolowym *(CLI)*, mechanizm cofania / przywracania nie jest domyślnie włączony. Musi on być jawnie aktywowany dla każdego dokumentu.


```python
import FreeCAD

FreeCAD.ActiveDocument.UndoMode = 1
```





{{Std Base navi

}}



---
⏵ [documentation index](../README.md) > Std Undo/pl
