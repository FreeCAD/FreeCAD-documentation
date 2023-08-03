---
 GuiCommand:
   Name: Sketcher CreateBSplineByInterpolation
   Name/pl: Szkicownik: Krzywa złozona przez interpolację
   MenuLocation: Szkic , Elementy geometryczne szkicownika , Krzywa złożona przez węzły
   Workbenches: Sketcher_Workbench/pl
   Shortcut: **G** **B** **I**
   Version: 0.21
   SeeAlso: Sketcher_CreatePeriodicBSpline/pl
---

# Sketcher CreateBSplineByInterpolation/pl



## Opis

Narzędzie to tworzy krzywą złożoną przechodzącą przez podane punkty. Więcej informacji na temat krzywych złożonych można znaleźć na stronie opisującej [Krzywe złożone](B-Splines/pl.md).



## Użycie

1.  Naciśnij przycisk **[<img src=images/Sketcher_CreateBSplineByInterpolation.svg style="width:16px"> '''Utwórz krzywą złożona przez interpolację'''**.
2.  Utwórz serię punktów, klikając w oknie [widoku 3D](3D_view/pl.md). Gdy polecenie jest aktywne, utworzone punkty są połączone liniami prostymi.
3.  Opcjonalnie naciśnij klawisz **M** przed zakończeniem wprowadzania, aby zdefiniować krotność węzła w ostatnim zdefiniowanym punkcie *(pamiętaj, że nie zawsze może to być przestrzegane, zobacz akapit [Ograniczenia](#Ograniczenia.md) aby poznać szczegóły)*.
4.  Opcjonalnie naciśnij klawisz **Backspace** przed zakończeniem wprowadzania danych, aby usunąć ostatnio utworzony punkt kontrolny.
5.  Kliknij prawym przyciskiem myszy, aby zakończyć wprowadzanie danych i wygenerować krzywą.
6.  W zależności od preferencji narzędzie może pozostać aktywne w celu wykreślenia nowej krzywej. Kliknij ponownie prawym przyciskiem myszy, aby zakończyć polecenie.



## Uwagi

Zobacz stronę [Krzywa złożona przez punkty kontrolne](Sketcher_CreateBSpline/pl#Uwagi.md).



## Ograniczenia

-   Wynikowa krzywa nie różni się niczym od *(niejednolitej)* krzywej zdefiniowanej za pomocą punktów kontrolnych. Obowiązują więc wszystkie powiązane z nią więzy. Zobacz stronę [Krzywa złożona przez punkty kontrolne](Sketcher_CreateBSpline/pl#Ograniczenia.md) aby poznać szczegóły.
-   Utworzone krzywe złożone są zawsze sześcienne *(tj. o stopniu 3)*.
-   Zdefiniowana krotność może nie zawsze być przestrzegana:
    -   Dla krzywej okresowej, pierwszy węzeł *(zbieżny z ostatnim)* zawsze ma krotność 2.
    -   Dla krzywej nieokresowej, pierwszy i ostatni węzeł zawsze ma krotność 4.
    -   Jeśli punkty tuż przed i tuż za mają wartość krotności większą lub równą 3, element między nimi jest w pełni ciągły, a ten *(środkowy)* punkt będzie związany tylko za pomocą więzu punkt-na-obiekcie. Jeśli potrzebny jest węzeł, rozważ użycie narzędzia wstawiania węzła.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CreateBSplineByInterpolation/pl
