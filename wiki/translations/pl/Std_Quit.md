---
- GuiCommand:/pl
   Name:Std Quit
   Name/pl:Std: Zakończ
   MenuLocation:Plik → Zakończ
   Workbenches:Wszystkie
   Shortcut:**Alt** + **F4**
   SeeAlso:[Zamknij aktywne okno](Std_CloseActiveWindow/pl.md)
---

# Std Quit/pl

## Opis

Polecenie **Zakończ** zamyka aplikację FreeCAD i opcjonalnie umożliwia zapisanie niezapisanych dokumentów.

## Użycie

1.  Istnieje kilka sposobów wywołania tego polecenia:
    -   Wybierz opcję **Plik → <img src="images/Std_Quit.svg" width=16px> Zakończ** z menu.
    -   Użyj skrótu klawiaturowego: **Alt** + **F4**.
2.  Jeśli istnieją niezapisane dokumenty, pojawi się okno dialogowe z prośbą o ich zapisanie:
    -   Naciśnij przycisk **Zapisz**, aby zapisać aktywny dokument. W razie potrzeby wprowadź najpierw nazwę pliku.
    -   Naciśnij przycisk **Porzuć**, aby odrzucić aktywny dokument i utracić wszystkie zmiany.

## Opcje

-   Jeśli istnieje wiele niezapisanych dokumentów: zaznacz pole wyboru {{CheckBox|TRUE|Zastosuj dla wszystkich}}, aby uniknąć wyświetlania monitów dla każdego niezapisanego dokumentu osobno.
-   Jeśli istnieją niezapisane dokumenty: naciśnij przycisk **Esc** lub **Anuluj**, aby przerwać wykonywanie polecenia.

## Ustawienia

-   Przechowywana jest ostatnio używana lokalizacja pliku: **Przybory → Edycja parametrów ... → BaseApp → Preferences → General → FileOpenSavePath**.





{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std Quit/pl
