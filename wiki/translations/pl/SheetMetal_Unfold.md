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
2.  To polecenie można wywołać na kilka sposobów:
    -   Wciśnij przycisk **<img src="images/_SheetMetal_Unfold.svg_" width=16px> '''Rozwiń'''**.
    -   Wybierz opcję **SheetMetal → <img src="images/SheetMetal_Unfold.svg" width=16px> Rozwiń** z menu.
    -   Kliknij prawym przyciskiem myszy w [widoku drzewa](Tree_view/pl.md) lub [widoku 3D](3D_view/pl.md) i wybierz opcję **Sheet Metal → <img src="images/SheetMetal_Unfold.svg" width=16px> [Rozwiń](SheetMetal_Unfold.md)** z menu kontekstowego.
    -   Użyj skrótu klawiaturowego: **U**.
3.  Otwarty zostanie [panel zadań](Task_panel/pl.md) **Unfold sheet metal object**.
4.  Dostosuj opcje rozwijania w [panelu zadań](Task_panel/pl.md):
    -   Opcjonalnie aktywuj opcje rzutowania szkicu rozwinięcia i ustaw kolory.
    -   Opcjonalnie aktywuj opcję eksportu.
    -   Jeśli nie używasz **Material Definition Sheet** (zobacz [Uwagi](#Uwagi.md)):
        1.  Ustaw opcję **Material Definition Sheet** na {{Value|Manual K-Factor}}.
        2.  Opcjonalnie przełącz przyciski ANSI i DIN (zobacz [Uwagi](#Uwagi.md)).
        3.  Dostosuj wartość Manual K-Factor (zobacz [Uwagi](#Uwagi.md)).
    -   Opcjonalnie dostosuj przezroczystość obiektu Unfold.
5.  Wciśnij przycisk **OK** aby zakończyć polecenie i zamknąć panel zadań.
6.  Utworzony zostanie obiekt **Unfold**.
7.  Opcjonalnie dostosuj parametry w [Edytorze właściwości](Property_editor/pl.md).



## Uwagi

-   Zobacz sekcje [Material Definition Sheet](https://github.com/shaise/FreeCAD_SheetMetal#material-definition-sheet) i [K-factor](https://github.com/shaise/FreeCAD_SheetMetal#physical-material-definitions) strony projektu aby uzyskać więcej informacji.
-   Wyjaśnienie różnych zakresów wartości ISO i ANSI współczynników K można znaleźć w tabeli na [tej](https://de.wikipedia.org/wiki/Biegeverkürzung#Korrektur_durch_den_sog._k-Faktor) stronie (po niemiecku).



## Właściwości

Zapoznaj się również z informacjami na stronie: [Edytor właściwości](Property_editor/pl.md).

Obiekt **Rozwiń** środowiska Arkusz Blachy wywodzi się z obiektu [Część: Cecha](Part_Feature/pl.md) i dziedziczy wszystkie jego właściwości. Nie ma on dodatkowych właściwości.



## Ograniczenia

-   Blacha powinna mieć stałą grubość.
-   Płaskie powierzchnie nie powinny zawierać linii podziału.
-   Płaskie powierzchnie muszą być prawdziwie płaskie i nie mogą być aproksymacjami krzywych złożonych.
-   Powierzchnie kątów gięcia muszą być prawdziwie cylindryczne i nie mogą być aproksymacjami krzywych złożonych.
-   Wersje przed 0.5.00: Funkcja Rozwiń nie jest parametryczna. Jeśli model zostanie zmodyfikowany, należy go ponownie rozłożyć.



---
⏵ [documentation index](../README.md) > [SheetMetal](Category_SheetMetal.md) > [Addons](Category_Addons.md) > [External Command Reference](Category_External%20Command%20Reference.md) > SheetMetal Unfold/pl
