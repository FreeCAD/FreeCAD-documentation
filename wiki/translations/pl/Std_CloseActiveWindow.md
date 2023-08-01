---
- GuiCommand:
   Name: Std CloseActiveWindow
   Name/pl: Std: Zamknij aktywne okno
   MenuLocation: Plik - Zamknij
   Workbenches: wszystkie
   Shortcut: **Ctrl**+**F4**
   SeeAlso: [Zamknij wszystkie okna](Std_CloseAllWindows/pl.md)
---

# Std CloseActiveWindow/pl

## Opis

Polecenie **Zamknij aktywne okno** zamyka aktywne okno. Aby zamknąć dokument, wszystkie jego okna muszą być zamknięte.

## Użycie

1.  Istnieje kilka sposobów na wywołanie tego polecenia:
    -   Wybierz z menu opcję **Plik → <img src="images/Std_CloseActiveWindow.svg" width=16px> Zamknij**.
    -   Użyj skrótu klawiaturowego: **Ctrl** + **F4**.
2.  Aby zamknąć dokument: powtórz tę czynność dla wszystkich należących do niego okien.
3.  Podczas zamykania ostatniego okna dokumentu, który nie został zapisany, zostanie wyświetlone okno dialogowe z prośbą o jego zapisanie:
    -   Naciśnij przycisk **Zapisz**, aby zapisać dokument. W razie potrzeby wprowadź najpierw nazwę pliku.
    -   Naciśnij przycisk **Porzuć zmiany**, aby odrzucić dokument i utracić wszystkie zmiany.

## Opcje

-   Po wyświetleniu okna dialogowego: naciśnij przycisk **Esc** lub **Anuluj**, aby przerwać wykonywanie polecenia.

## Uwagi

-   Polecenie to może zamknąć tylko okna [zadokowane](Std_ViewDockUndockFullscreen/pl.md).
-   Dokument można również zamknąć, klikając go prawym przyciskiem myszy w oknie [widoku drzewa](Tree_view/pl.md) i wybierając opcję **Zamknij dokument** z menu podręcznego.

## Ustawienia

-   Przechowywana jest ostatnio używana lokalizacja pliku: **Przybory → Edycja parametrów ... → BaseApp → Preferences → General → FileOpenSavePath**.

## Tworzenie skryptów 


**Zobacz również:**

[FreeCAD podstawy tworzenia skryptów](FreeCAD_Scripting_Basics/pl.md).

Aby zamknąć dokument, należy użyć metody `closeDocument` aplikacji FreeCAD. Przykład skryptu można znaleźć na stronie opisującej opcję [Nowy](Std_New/pl#Tworzenie_skrypt.C3.B3w.md).





{{Std Base navi

}}



---
⏵ [documentation index](../README.md) > Std CloseActiveWindow/pl
