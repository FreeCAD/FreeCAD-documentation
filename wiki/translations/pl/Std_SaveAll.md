---
- GuiCommand:/pl
   Name:Std SaveAll
   Name/pl:Std: Zapisz wszystkie
   MenuLocation:Plik → Zapisz wszystkie
   Workbenches:wszystkie
   SeeAlso:[Zapisz](Std_Save/pl.md)
---

# Std SaveAll/pl

## Opis

Polecenie **Zapisz wszystkie** powoduje zapisanie wszystkich otwartych dokumentów.

## Użycie

1.  Wybierz z menu opcję **Plik → <img src="images/Std_SaveAll.svg" width=16px> Zapisz wszystkie**.
2.  W przypadku nowych dokumentów: wprowadź nazwę pliku w oknie dialogowym i naciśnij przycisk **Zapisz**.

## Opcje

-   W przypadku zapisywania nowego dokumentu: naciśnij przycisk **Esc** lub przycisk **Anuluj** aby przerwać wykonywanie polecenia.

## Ustawienia

-   Przechowywana jest ostatnio używana lokalizacja pliku: **Przybory → Edycja parametrów ... → BaseApp → Preferences → General → FileOpenSavePath**.

## Tworzenie skryptów 


**Zobacz również:**

[FreeCAD podstawy tworzenia skryptów](FreeCAD_Scripting_Basics/pl.md).

Aby zapisać dokument, należy użyć metody `save` obiektu *document*. Nowy dokument musi być najpierw zapisany za pomocą metody `saveAs` obiektu *document*. Przykład skryptu można znaleźć na stronie opisującej opcję [Nowy](Std_New/pl#Tworzenie_skrypt.C3.B3w.md).





{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std SaveAll/pl
