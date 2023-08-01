---
- GuiCommand:/pl
   Name:Std Open
   Name/pl:Std: Otwórz
   MenuLocation:Plik → Otwórz ...
   Workbenches:wszystkie
   Shortcut:**Ctrl**+**O**
   SeeAlso:[Importuj](Std_Import/pl.md), [Nowy](Std_New/pl.md)
---

# Std Open/pl

## Opis

Polecenie **Std: Otwórz** otwiera plik. Jeśli plik nie jest natywnym plikiem FreeCAD *(\*.FCStd)*, jego geometria zostanie zaimportowana do nowego dokumentu. Zobacz stronę [Std: Importuj](Std_Import/pl.md), aby uzyskać więcej informacji.

## Użycie

1.  Istnieje kilka sposobów na wywołanie tego polecenia:
    -   Naciśnij przycisk **<img src="images/Std_Open.svg" width=16px> [Otwórz](Std_Open/pl.md)**.
    -   Wybierz z menu opcję **Plik → <img src="images/Std_Open.svg" width=16px> Otwórz ...** opcję z menu.
    -   Użyj skrótu klawiaturowego: **Ctrl** + **O**.
2.  Opcjonalnie wybierz odpowiedni format pliku w oknie dialogowym.
3.  Wybierz plik.
4.  Naciśnij przycisk **Otwórz**.

## Opcje

-   Naciśnij przycisk **Esc** lub przycisk **Anuluj** aby przerwać wykonywanie polecenia.

## Ustawienia

-   Przechowywana jest ostatnio używana lokalizacja pliku: **Przybory → Edycja parametrów ... → BaseApp → Preferences → General → FileOpenSavePath**.

## Tworzenie skryptów 


**Zobacz również:**

[FreeCAD podstawy tworzenia skryptów](FreeCAD_Scripting_Basics/pl.md).

Aby otworzyć dokument, należy użyć metody `open(filepath)` lub metody `openDocument(filepath, [hidden<nowiki>=</nowiki>False])` aplikacji FreeCAD.

Wymienione metody tworzą i zwracają dokument oraz wczytują do niego plik projektu. Argument `filepath` musi być łańcuchem wskazującym na istniejący plik. Jeśli plik nie istnieje lub nie można go wczytać, zostanie wywołany wyjątek wejścia / wyjścia. W takim przypadku utworzony dokument zostanie zachowany, ale będzie pusty. Jeśli zostanie użyta opcja `hidden<nowiki>=</nowiki>True`, dokument nie będzie wyświetlany w GUI i nie pojawi się dla niego żadna zakładka. Umożliwia to wykonywanie automatycznych operacji na dokumencie i zamykanie go bez zakłócania pracy interfejsu użytkownika.

Przykład skryptu można znaleźć na stronie opisującej opcję [Nowy](Std_New/pl#Tworzenie_skrypt.C3.B3w.md).





{{Std Base navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > Std Open/pl
