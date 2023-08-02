---
- GuiCommand:
   Name: Std CloseAllWindows
   Name/pl: Std: Zamknij wszystkie okna
   MenuLocation: Plik -> Zamknij wszystkie
   Workbenches: wszystkie
   SeeAlso: Std_CloseActiveWindow/pl
---

# Std CloseAllWindows/pl

## Opis

Polecenie **Zamknij wszystkie okna** powoduje zamknięcie wszystkich okien, a tym samym zamknięcie całego dokumentu.

## Użycie

1.  Wybierz z menu opcję **Plik → <img src="images/Std_CloseAllWindows.svg" width=16px> Zamknij wszystkie**.
2.  Jeśli istnieją niezapisane dokumenty, pojawi się okno dialogowe z prośbą o ich zapisanie:
    -   Naciśnij przycisk **Zapisz**, aby zapisać aktywny dokument. W razie potrzeby wprowadź najpierw nazwę pliku.
    -   Naciśnij przycisk **Porzuć zmiany**, aby odrzucić aktywny dokument i utracić wszystkie zmiany.

## Opcje

-   Po wyświetleniu okna dialogowego: naciśnij przycisk **Esc** lub **Anuluj**, aby przerwać wykonywanie polecenia.
-   Jeśli istnieje wiele niezapisanych dokumentów: zaznacz pole wyboru {{CheckBox|TRUE|Zastosuj odpowiedź do wszystkich}}, aby uniknąć wyświetlania monitów dla każdego niezapisanego dokumentu osobno.

## Uwagi

-   Dokument można również zamknąć, klikając go prawym przyciskiem myszy w oknie [Widoku drzewa](Tree_view.md) i wybierając z menu kontekstowego polecenie **Zamknij dokument**.

## Ustawienia

-   Przechowywana jest ostatnio używana lokalizacja pliku: **Przybory → Edycja parametrów ... → BaseApp → Preferences → General → FileOpenSavePath**.

## Tworzenie skryptów 


**Zobacz również:**

[FreeCAD podstawy tworzenia skryptów](FreeCAD_Scripting_Basics/pl.md).

Aby zamknąć dokument, należy użyć metody `closeDocument` aplikacji FreeCAD. Przykład skryptu można znaleźć na stronie opisującej opcję [Nowy](Std_New/pl#Tworzenie_skrypt.C3.B3w.md).





{{Std Base navi

}}



---
⏵ [documentation index](../README.md) > Std CloseAllWindows/pl
