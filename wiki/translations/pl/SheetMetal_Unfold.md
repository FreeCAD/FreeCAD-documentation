---
 GuiCommand:
   Name: SheetMetal Unfold
   Name/pl: Arkusz Blachy: Rozwiń
   MenuLocation: SheetMetal , Rozwiń
   Workbenches: SheetMetal_Workbench/pl
   Shortcut: **U**
   SeeAlso: SheetMetal_UnattendedUnfold/pl
---

# SheetMetal Unfold/pl



## Opis

Polecenie <img alt="" src=images/SheetMetal_Unfold.svg  style="width:24px;"> **Rozwiń** rozkłada obiekt z blachy.



## Użycie

1.  Wybierz płaską powierzchnię części z blachy.
2.  Aktywuj polecenie <img alt="" src=images/SheetMetal_Unfold.svg  style="width:16px;"> [Rozwiń](SheetMetal_Unfold.md) używając jednego z poniższych sposobów:
    -   Przycisk **<img src="images/_SheetMetal_Unfold.svg_" width=16px> '''Rozwiń'''**.
    -   Polecenie menu **SheetMetal → <img src="images/SheetMetal_Unfold.svg" width=16px> Rozwiń**.
    -   Skrót klawiaturowy: **U**.
3.  Dostosuj opcje rozkładania w [Panelu zadań](Task_panel/pl.md) poprzez:
    -   Wybranie opcji rzutowania szkicu rozwinięcia.
    -   Wybranie metody obliczania zgięcia ze współczynnikiem K:
        - Użyj [Material Arkusza definicji](https://github.com/shaise/FreeCAD_SheetMetal#material-definition-sheet).
        - Wybierz samodzielnie [Współczynnik K](https://github.com/shaise/FreeCAD_SheetMetal#terminology), a następnie normę [ANSI lub DIN](https://de.wikipedia.org/wiki/Biegeverkürzung#Korrektur_durch_den_sog._k-Faktor) do zastosowania.



## Właściwości

Zapoznaj się również z informacjami na stronie: [Edytor właściwości](Property_editor/pl.md).

Obiekt **Rozwiń bezobsługowo** środowiska Arkusz Blachy wywodzi się z obiektu [Część: Cecha](Part_Feature/pl.md) i dziedziczy wszystkie jego właściwości. Posiada on również następujące dodatkowe właściwości:



### Dane


{{Properties_Title|Podstawowe}}

-    **Etykieta|String**: Wartość domyślna: {{value|Rozwiń}} *(+ kolejny numer dla drugiego i kolejnych elementów)*.
    Nazwa edytowalna przez użytkownika, może to być dowolny ciąg znaków UTF8.



## Ograniczenia

-   Blacha powinna mieć stałą grubość.
-   Płaskie powierzchnie nie powinny zawierać linii podziału.
-   Płaskie powierzchnie muszą być prawdziwie płaskie i nie mogą być aproksymacjami krzywych złożonych.
-   Powierzchnie kątów gięcia muszą być prawdziwie cylindryczne i nie mogą być aproksymacjami krzywych złożonych.
-   Funkcja Rozwiń nie jest parametryczna. Jeśli model zostanie zmodyfikowany, należy go ponownie rozłożyć.



---
⏵ [documentation index](../README.md) > [SheetMetal](Category_SheetMetal.md) > [Addons](Category_Addons.md) > [External Command Reference](Category_External Command Reference.md) > SheetMetal Unfold/pl
