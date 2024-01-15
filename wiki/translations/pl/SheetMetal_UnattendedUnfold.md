---
 GuiCommand:
   Name: SheetMetal UnattendedUnfold
   Name/pl: Arkusz Blachy: Rozwiń bez nadzoru
   MenuLocation: SheetMetal , Rozwiń bez nadzoru
   Workbenches: SheetMetal_Workbench/pl
   Shortcut: **U**
   SeeAlso: SheetMetal_Unfold/pl
---

# SheetMetal UnattendedUnfold/pl



## Opis

Polecenie <img alt="" src=images/SheetMetal_UnattendedUnfold.svg  style="width:24px;"> **Rozwiń bez nadzoru** rozkłada obiekt z blachy.

Polecenie to nie jest dostępne domyślnie, zobacz [Uwagi](#Uwagi.md).

Jeśli bryła nadrzędna wybranej powierzchni płaskiej została wcześniej poddana rozkładaniu, narzędzie to pominie menu w panelu zadań. W przeciwnym razie zostanie wyświetlony komunikat o błędzie z prośbą o \"ustawienie współczynnika K\" lub \"użycie arkusza definicji materiału\".

Przy pierwszym użyciu komendy <img alt="" src=images/SheetMetal_Unfold.svg  style="width:16px;"> [Rozwiń](SheetMetal_Unfold/pl.md) etykieta Zawartości nadrzędnej otrzymała przyrostek *(taki jak **\_material_0.5din**)* i po tym jest gotowa do użycia z tym narzędziem.



## Użycie

1.  Wybierz jedną płaską powierzchnię części z blachy.
2.  Aktywuj polecenie <img alt="" src=images/SheetMetal_UnattendedUnfold.svg  style="width:16px;"> **Rozwiń bez nadzoru** używając do tego celu jednego z poniższych sposobów:
    -   Przycisk **<img src="images/_SheetMetal_UnattendedUnfold.svg_" width=16px> '''Rozwiń bez nadzoru'''**.
    -   Opcja menu **SheetMetal → <img src="images/SheetMetal_UnattendedUnfold.svg" width=16px> Rozwiń bez nadzoru**.
    -   Skrót klawiaturowy: **U**.



## Uwagi

Aby udostępnić to polecenie, należy najpierw włączyć tryb inżynieryjny w preferencjach. Przejdź do **Edycja → Preferencje ... → SheetMetal → Ustawienie ogólne** i ustaw **Tryb UX inżynierski** na {{Value|Właczone}}. Zmiana tej preferencji wymaga ponownego uruchomienia FreeCAD.



## Właściwości

Zapoznaj się również z informacjami na stronie: [Edytor właściwości](Property_editor/pl.md).

Obiekt **Rozwiń bez nadzoru** środowiska Arkusz Blachy wywodzi się z obiektu [Część: Cecha](Part_Feature/pl.md) i dziedziczy wszystkie jego właściwości. Posiada on również następujące dodatkowe właściwości:



### Dane


{{Properties_Title|Podstawowe}}

-    **Etykieta|String**: Wartość domyślna: {{value|Rozwiń}} *(+ kolejny numer dla drugiego i kolejnych elementów)*.
    Nazwa edytowalna przez użytkownika, może to być dowolny ciąg znaków UTF8.



## Ograniczenia

Zapoznaj się także z informacjami na stronie <img alt="" src=images/SheetMetal_Unfold.svg  style="width:16px;"> [Rozwiń](SheetMetal_Unfold/pl.md) gdzie znajdziesz informację o ograniczeniach.



---
⏵ [documentation index](../README.md) > [SheetMetal](Category_SheetMetal.md) > [Addons](Category_Addons.md) > [External Command Reference](Category_External Command Reference.md) > SheetMetal UnattendedUnfold/pl
