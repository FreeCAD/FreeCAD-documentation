---
- GuiCommand:
   Name:Std Edit
   Name/pl:Edycja
   MenuLocation:Edycja - Przełącz tryb edycji
   Workbenches:Wszystkie
   SeeAlso:[Tryb edycji dla uzytkownika](Std_UserEditMode/pl.md)
---

# Std Edit/pl

## Opis

Polecenie **Std: Edycja** aktywuje lub dezaktywuje tryb edycji obiektu.

## Użycie

1.  Jeśli żaden obiekt nie znajduje się w trybie edycji: wybierz pojedynczy obiekt.
2.  Wybierz z menu **Edycja → <img src="images/Std_Edit.svg" width=16px> Przełącz tryb edycji**.
3.  Aktywowany jest domyślny tryb edycji wybranego obiektu lub dezaktywowany dotychczasowy tryb edycji.

## Uwagi

-   Niektóre narzędzia będą wyłączone *(wyszarzone)* w interfejsie użytkownika, gdy tryb edycji obiektu jest aktywny.
-   Nie wszystkie typy obiektów posiadają tryb edycji.
-   Funkcjonalność dostępna w trybie edycji zależy od typu obiektu.
-   Tryb edycji można uruchomić również poprzez dwukrotne kliknięcie obiektu w [Widoku drzewa](Tree_view/pl.md).

-   Tryb edycji obiektu może być również aktywowany przez dwukrotne kliknięcie na obiekcie w [widoku drzewa](Tree_view/pl.md). W takim przypadku tryb edycji, który jest używany, może być zdefiniowany za pomocą polecenia [Std UserEditMode](Std_UserEditMode.md).

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



---
![](images/Button_right.svg) [documentation index](../README.md) > Std Edit/pl
