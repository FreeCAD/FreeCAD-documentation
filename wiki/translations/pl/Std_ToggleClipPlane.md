---
 GuiCommand:
   Name: Std ToggleClipPlane
   Name/pl: Płaszczyzna przecinająca
   MenuLocation: Widok , Płaszczyzna tnąca‏‎
   Workbenches: wszystkie
   SeeAlso: Part_SectionCut/pl
---

# Std ToggleClipPlane/pl



## Opis

Polecenie przełącz *Płaszczyznę przecinającą* tymczasowo ukrywa obiekty i ich części po jednej stronie maksymalnie trzech wirtualnych płaszczyzn w aktywnym [widoku 3D](3D_view/pl.md).

![](images/Std_ToggleClipPlane_example.png ) 
*Przycięty pusty obiekt.*

![](images/Std_ToggleClipPlane_Dialog.png ) 
*Okienko dialogowe funkcji przycinania*



## Użycie

1.  Wybierz z menu opcję **Widok → <img src="images/Std_ToggleClipPlane.svg" width=16px> Płaszczyzna tnąca**.
2.  W okienku dialogowym Przycinania wykonaj jedną z poniższych czynności:
    -   Zaznacz jedno lub więcej pól wyboru {{CheckBox|TRUE|Utnij względem X}} do {{CheckBox|TRUE|Utnij względem Z}}.
        -   Opcjonalnie zmień odległość *(odległości)* przesunięcia.
        -   Opcjonalnie wciśnij przycisk*(i)* **Obróć**, aby zmienić bok płaszczyzny przycinania obiekty są ukryte.
    -   Zaznacz pole wyboru {{CheckBox|TRUE|Przycinanie względem dowolnego kierunku}}.
        -   Opcjonalnie zmień dystans przesunięcia.
        -   Wykonaj jedną z poniższych czynności:
            -   Naciśnij przycisk **Widok**, aby użyć kierunku bieżącego widoku.
            -   Zaznacz pole wyboru {{CheckBox|TRUE|Dostosuj do kierunku wyświetlania}}, aby użyć kierunku, który dynamicznie dostosowuje się do zmian widoku.
            -   Określ kierunek, wprowadzając współrzędne X, Y i Z wektora normalnego.
3.  Opcjonalnie zmień widok, aby sprawdzić model.
4.  Wciśnij przycisk **Zamknij**, aby zamknąć panel zadań i zakończyć polecenie.



## Uwagi

-   Aby wyraźnie odróżnić wnętrze częściowo przyciętych przedmiotów, należy zmienić ich **oświetlenie** ustawiając na *jedna stronę*. Kolor wewnętrznej strony ich powierzchni będzie wtedy zależał od ustawień podświetlenia: **Edycja → Preferencje → Wyświetlanie → 3D View → Włącz podświetlenie - Intensywność podświetlenia**. Zobacz [Edytor ustawień](Preferences_Editor/pl#3D_View.md).





{{Std_Base_navi

}}



---
⏵ [documentation index](../README.md) > Std ToggleClipPlane/pl
