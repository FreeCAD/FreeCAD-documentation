---
- GuiCommand:/pl
   Name:Std Redo
   Name/pl:Std: Przywróć
   MenuLocation:Edycja → Przywróć
   Workbenches:wszystkie
   Shortcut:**Ctrl** + **Y**
   SeeAlso:[Cofnij](Std_Undo/pl.md)
---

# Std Redo/pl

## Opis

Polecenie **Ponów** odwraca działanie polecenia [Cofnij](Std_Undo/pl.md).

## Użycie

1.  Istnieje kilka sposobów na wywołanie polecenia:
    -   Naciśnij przycisk **<img src="images/Std_Redo.svg" width=16px> [Ponów](Std_Redo/pl.md)**.
    -   Wybierz z menu opcję **Edycja → <img src="images/Std_Redo.svg" width=16px> Ponów**.
    -   Użyj skrótu klawiaturowego: **Ctrl** + **Y**.

## Opcje

-   Aby przywrócić wiele czynności, kliknij na małą czarną strzałkę w dół po prawej stronie przycisku **<img src="images/Std_Redo.svg" width=16px> [Ponów](Std_Redo/pl.md)** i wybierz odpowiednią pozycję z listy.

## Ustawienia

-   Funkcję Cofnij / Ponów można wyłączyć, ustawiając parametr **Przybory → Edycja parametrów... → BaseApp → Preferencje → Dokument → UżywanieUndo** na wartość {{FALSE/pl}}, ale nie jest to zalecane. To ustawienie można również zmienić w [Edytorze ustawień](Preferences_Editor/pl#Dokument.md).
-   Maksymalna liczba kroków Cofnij / Ponów jest kontrolowana przez parametr **Przybory → Edycja parametrów... → BaseApp → Preferencje → Dokument → MaxUndoSize**. Ustawienie to można również zmienić w [Edytorze ustawień](Preferences_Editor/pl#Dokument.md).

## Tworzenie skryptów 


**Zobacz również:**

[FreeCAD podstawy tworzenia skryptów](FreeCAD_Scripting_Basics/pl.md).

Aby ponownie wykonać czynność, która właśnie została cofnięta, należy użyć metody `redo` obiektu dokumentu.


```python
import FreeCAD

FreeCAD.ActiveDocument.redo()
```





{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std Redo/pl
