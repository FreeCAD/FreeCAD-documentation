---
 GuiCommand:
   Name: Std ProjectInfo
   Name/pl: Std: Informacja o projekcie
   MenuLocation: Plik , Informacja o projekcie ...
   Workbenches: wszystkie
   SeeAlso: Std_New/pl
---

# Std ProjectInfo/pl



## Opis

Polecenie **Informacja o projekcie** wyświetla okno dialogowe ze szczegółowymi informacjami o aktywnym dokumencie. Niektóre z tych informacji można edytować.



## Użycie

1.  Wybierz z menu opcję **Plik → <img src="images/Std_ProjectInfo.svg" width=16px> Informacje o projekcie ...**.
2.  Wyskakuje okno dialogowe z następującymi informacjami:
    -   **Nazwa**: Nazwa dokumentu. *Nie edytowalne*. Odpowiada właściwości Etykieta dokumentu, którą można zmienić w [Edytorze właściwości](Property_editor/pl.md).
    -   **Ścieżka**: Pełna ścieżka dostępu do pliku. Puste, jeśli dokument nie został zapisany. *Nie edytowalne*.
    -   **UUID**: FreeCAD automatycznie wpisuje wartość sumy kontrolnej. *Nie edytowalne*.
    -   **Wersja programu**: Wersja FreeCAD użyta do zapisania pliku. Puste, jeśli plik nie został zapisany. *Nie można edytować.*
    -   **System jednostek**: System jednostek dokumentu. *Wartość początkowa zależy od [Domyślny układ jednostek](Preferences_Editor/pl#Ogólne_2.md).* {{Version/pl|1.0}}.
    -   **Utworzony przez**: Wprowadź nazwisko autora. *Może być wstępnie ustawiony*.
    -   **Data utworzenia**: FreeCAD automatycznie wpisuje poprawną datę. *nie edytowalne*.
    -   **Ostatnio zmodyfikowany przez**: Wprowadź nazwę autora. *Może być wstępnie ustawiony.*
    -   **Data ostatniej modyfikacji**: FreeCAD automatycznie wprowadza poprawną datę. *Nie można edytować.*
    -   **Firma**: Wprowadź nazwę firmy. *Może być wstępnie ustawiona*.
    -   **Informacje o licencji**: Wybierz licencję z rozwijanego menu. *Może być wstępnie ustawiona.*
    -   **Adres URL licencji**: Adres URL zmieni się wraz z wybraną licencją, ale może zostać nadpisany. *Może być wstępnie ustawiony.*
    -   **Komentarz**: Wprowadź dowolny komentarz, który może mieć zastosowanie.
3.  Wprowadź wymagane informacje i naciśnij przycisk **OK**.



## Opcje

-   Naciśnij przycisk **Esc** lub przycisk **Anuluj** aby przerwać wykonywanie polecenia.



## Ustawienia

Zapoznaj się z informacjami na stronie: [Edytor preferencji](Preferences_Editor/pl.md).

-   Wartości dla nazwisk autorów, nazwy firmy i informacji o licencji można wstępnie ustawić w **Edycja → Preferencje ... → Ogólne → Dokument → Prawa autorskie i licencja**.



---
⏵ [documentation index](../README.md) > Std ProjectInfo/pl
