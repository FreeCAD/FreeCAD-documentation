---
- GuiCommand:/pl
   Name:Std Save
   Name/pl:Std: Zapisz
   MenuLocation:Plik → Zapisz
   Workbenches:wszystkie
   Shortcut:**Ctrl** + **S**
   SeeAlso:[Zapisz jako ...](Std_SaveAs/pl.md), [Zapisz jako kopię...](Std_SaveCopy/pl.md), [Zapisz wszystkie](Std_SaveAll/pl.md)
---

# Std Save/pl

## Opis

Polecenie **Zapisz** powoduje zapisanie aktywnego dokumentu.

## Użycie

1.  Istnieje kilka sposobów na wywołanie tego polecenia:
    -   Naciśnij przycisk **<img src="images/Std_Save.svg" width=16px> [Zapisz](Std_Save.md)**.
    -   Wybierz z menu opcję **Plik → <img src="images/Std_Save.svg" width=16px> Zapisz ...** opcję z menu.
    -   Użyj skrótu klawiaturowego: **Ctrl** + **S**.
2.  W przypadku nowych dokumentów: wprowadź nazwę pliku w oknie dialogowym i naciśnij przycisk **Zapisz**.

## Opcje

-   W przypadku zapisywania nowego dokumentu: naciśnij przycisk **Esc** lub przycisk **Anuluj** aby przerwać wykonywanie polecenia.

## Uwagi

-   Tego polecenia można również użyć do zapisania grafów zależności. Zobacz informacje na stronie [Graf zależności](Std_DependencyGraph/pl.md).

## Ustawienia

-   Przechowywana jest ostatnio używana lokalizacja pliku: **Przybory → Edycja parametrów ... → BaseApp → Preferences → General → FileOpenSavePath**.

## Tworzenie skryptów 


**Zobacz również:**

[FreeCAD podstawy tworzenia skryptów](FreeCAD_Scripting_Basics/pl.md).

Aby zapisać dokument, należy użyć metody `save` obiektu *document*. Nowy dokument musi być najpierw zapisany za pomocą metody `saveAs` obiektu *document*. Przykład skryptu można znaleźć na stronie opisującej opcję [Nowy](Std_New/pl#Tworzenie_skrypt.C3.B3w.md).





{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std Save/pl
