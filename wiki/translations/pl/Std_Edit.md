---
- GuiCommand:/pl
   Name:Std Edit
   Name/pl:Edycja
   MenuLocation:Edycja → Przełącz tryb edycji
   Workbenches:Wszystkie
---

## Opis

Polecenie **Std: Edycja** aktywuje lub dezaktywuje tryb edycji obiektu.

## Użycie

1.  Jeśli żaden obiekt nie znajduje się w trybie edycji: wybierz pojedynczy obiekt.
2.  Wybierz z menu **Edycja → <img src="images/Std_Edit.svg" width=16px> Przełącz tryb edycji**.
3.  Aktywowany jest tryb edycji wybranego obiektu lub dezaktywowany dotychczasowy tryb edycji.

## Uwagi

-   Niektóre narzędzia będą wyłączone *(wyszarzone)* w interfejsie użytkownika, gdy tryb edycji obiektu jest aktywny.
-   Nie wszystkie typy obiektów posiadają tryb edycji.
-   Funkcjonalność dostępna w trybie edycji zależy od typu obiektu.
-   Tryb edycji można uruchomić również poprzez dwukrotne kliknięcie obiektu w [Widoku drzewa](Tree_view/pl.md).

## Tworzenie skryptów 


**Zobacz również:**

[FreeCAD podstawy tworzenia skryptów](FreeCAD_Scripting_Basics/pl.md).

Aby włączyć tryb edycji obiektu należy użyć metody `setEdit` obiektu dokumentu. Ta metoda nie jest dostępna, jeśli FreeCAD jest uruchomiony w trybie konsoli.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.setEdit("myObjectName",0)
```

Drugim argumentem jest Tryb edycji. Dostępne są następujące opcje:

0 = Domyślnie
1 = Przekształcenie
2 = Przycinanie
3 = Kolor

Aby wyłączyć tryb edycji obiektu należy użyć metody `resetEdit` obiektu dokumentu.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.resetEdit()
```





{{Std Base navi

}}  
