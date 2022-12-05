---
- GuiCommand:/pl
   Name:Std Export
   Name/pl:Std: Eksportuj
   MenuLocation:Plik → Eksportuj...
   Workbenches:wszystkie
   Shortcut:**Ctrl** + **E**
   SeeAlso:[Eksportuj do PDF](Std_PrintPdf/pl.md), [Import Eksport](Import_Export/pl.md), [Ustawienia dla Importu i Eksportu](Import_Export_Preferences/pl.md)
---

# Std Export/pl

## Opis

Polecenie **Exportuj** eksportuje wybrane obiekty do innego formatu pliku. Obsługiwanych jest wiele formatów plików, a dla niektórych formatów istnieje wiele opcji eksportu. Zobacz [Import eksport](Import_Export/pl.md) aby uzyskać więcej informacji.

## Użycie

1.  Wybierz jeden lub więcej obiektów. Aby uniknąć eksportu niewidocznych lub zduplikowanych obiektów:
    -   Uważaj, kiedy używasz kombinacji **Ctrl** + **A** do zaznaczania wszystkich obiektów. Spowoduje to również zaznaczenie obiektów niewidocznych.
    -   Wybierz [Zawartość](PartDesign_Body/pl.md), wybierając tylko samą zawartość lub jej ostatnią cechę.
    -   Wybierz [Std: Grupę](Std_Group/pl.md) lub [Std: Część](Std_Part/pl.md), wybierając tylko sam obiekt nadrzędny lub znajdujące się w nim obiekty.
    -   Nie używaj polecenia [Std: Zaznacz wszystko](Std_SelectAll/pl.md), ponieważ wybierze ono również elementy podrzędne Zawartości.
    -   Z tego samego powodu należy unikać polecenia [Zaznacz obszar](Std_BoxSelection/pl.md) w wersji FreeCAD 0.18 i wcześniejszych.
2.  Istnieje kilka sposobów na wywołanie tej komendy:
    -   Wybierz z menu opcję **Plik → <img src="images/Std_Export.svg" width=16px> Eksportuj ...**.
    -   Użyj skrótu klawiszowego: **Ctrl** + **E**.
3.  Wybierz odpowiedni format pliku w oknie dialogowym.
4.  Wprowadź nazwę pliku.
5.  Wciśnij przycisk **Zapisz**.

## Opcje

-   Naciśnij przycisk **Esc** lub przycisk **Anuluj** aby przerwać wykonywanie polecenia.

## Uwagi

-   Aby wyeksportować [obiekt siatki](Mesh_Workbench/pl.md) do pliku w formacie bryły, musi on zostać najpierw skonwertowany. Zobacz poradnik [Import z formatu STL lub OBJ](Import_from_STL_or_OBJ/pl.md).
-   Niektóre Środowiska pracy posiadają dodatkowe polecenia eksportu. Zobacz: [Import eksport](Import_Export/pl.md).

## Ustawienia

-   Zobacz: [Ustawienia Importu i Eksportu](Import_Export_Preferences/pl.md).
-   Zapamiętana jest ostatnio używana lokalizacja pliku: **Przybory → Edycja parametrów... → BaseApp → Preferences → General → FileOpenSavePath**.
-   Zapamiętany jest ostatni używany filtr eksportu: **Przybory → Edycja parametrów... → BaseApp → Preferences → General → FileExportFilter**.





{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [File_Formats](Category_File_Formats.md) > Std Export/pl
