---
- GuiCommand:
   Name:Std SaveAs
   Name/pl:Std: Zapisz jako
   MenuLocation:Plik → Zapisz jako ...
   Workbenches:wszystkie
   SeeAlso:[Zapisz jako kopię](Std_SaveCopy/pl.md), [Zapisz](Std_Save/pl.md)
---

# Std SaveAs/pl

## Opis

Polecenie **Zapisz jako** zapisuje aktywny dokument w pliku pod nową nazwą.

## Użycie

1.  Wybierz z menu opcję **Plik → <img src="images/Std_SaveAs.svg" width=16px> Zapisz jako ...**.
2.  Wprowadź nazwę pliku w oknie dialogowym.
3.  Naciśnij przycisk **Zapisz**.

## Opcje

-   Naciśnij przycisk **Esc** lub przycisk **Anuluj** aby przerwać wykonywanie polecenia.

## Uwagi

-   Tego polecenia można również użyć do zapisania grafów zależności. Zobacz informacje na stronie [Graf zależności](Std_DependencyGraph/pl.md).

## Ustawienia

-   Przechowywana jest ostatnio używana lokalizacja pliku: **Przybory → Edycja parametrów ... → BaseApp → Preferences → General → FileOpenSavePath**.

## Tworzenie skryptów 


**Zobacz również:**

[FreeCAD podstawy tworzenia skryptów](FreeCAD_Scripting_Basics/pl.md).

Aby zapisać dokument pod nową nazwą, należy użyć metody `saveAs` obiektu *document*. Przykład skryptu można znaleźć na stronie opisującej opcję [Nowy](Std_New/pl#Tworzenie_skrypt.C3.B3w.md).





{{Std Base navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > Std SaveAs/pl
