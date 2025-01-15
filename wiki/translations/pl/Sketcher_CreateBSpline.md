---
 GuiCommand:
   Name: Sketcher CreateBSpline
   Name/pl: Szkicownik: Utwórz krzywą złożoną
   MenuLocation: Szkic , Elementy geometryczne szkicownika , Utwórz krzywą złożoną
   Workbenches: Sketcher_Workbench/pl
   Shortcut: **G** **B** **B**
   Version: 0.17
   SeeAlso: Sketcher_CreatePeriodicBSpline/pl
---

# Sketcher CreateBSpline/pl



## Opis

Narzędzie <img alt="" src=images/Sketcher_CreateBSpline.svg  style="width:24px;"> **Utwórz krzywą złożoną** tworzy krzywą złożoną z jej punktów kontrolnych. {{Version/pl|1.0}}: Lub opcjonalnie z węzłów.

![](images/Sketcher_CreateBSpline_Example.png ) 
*Krzywa złożona ''(biała)'' zdefiniowana przez 5 punktów kontrolnych. <br>
Wielokąt kontrolny ''(zielony)'' łączy punkty kontrolne ''(zaznaczone ciemnożółtymi okręgami wagowymi)''.<br>
Liczba 3 ''(zielona, bez nawiasów)'' pośrodku odnosi się do [stopnia](Sketcher_BSplineIncreaseDegree/pl#Opis.md) B-splajnu.<br>
Liczby ''(1)'' i ''(4)'' ''(zielone, w nawiasach okrągłych)'' odnoszą się do [krotności](Sketcher_BSplineDecreaseKnotMultiplicity/pl#Opis.md) punktów węzłów.<br>
Liczby [1,00] ''(zielone, w nawiasach kwadratowych)'' odnoszą się do wag punktów kontrolnych.*



## Użycie

Zapoznaj się również z informacjami na stronie [Pomoce kreślarskie](Sketcher_Workbench/pl#Pomoce_kreślarskie.md).

1.  Istnieje kilka sposobów wywołania narzędzia:
    -   Wciśnij przycisk **<img src="images/Sketcher_CreateBSpline.svg" width=16px> [Krzywa złożona przez punkty kontrolne](Sketcher_CreateBSpline/pl.md)**.
    -   Wybierz z menu opcję **Szkic → Elementy geometryczne szkicownika → <img src="images/Sketcher_CreateBSpline.svg" width=16px> Utwórz krzywą złożoną**.
    -   Kliknij prawym przyciskiem myszy w [widoku 3D](3D_view.md) i wybierz opcję **<img src="images/Sketcher_CreateBSpline.svg" width=16px> Utwórz krzywą złożoną** z menu kontekstowego. {{Version/pl|1.0}}
    -   Użyj skrótu klawiaturowego: **G**, następnie **B**, a następnie **B**.
2.  Kursor zmieni się w krzyżyk z ikoną narzędzia.
3.  Sekcja **Parametry krzywej złożonej** ({{Version/pl|1.0}}) zostanie dodana w górnej części [okna dialogowego Szkicownika](Sketcher_Dialog/pl.md).
4.  Opcjonalnie, wciśnij klawisz **M** lub wybierz z listy rozwijanej w sekcji parametrów aby zmienić tryb narzędzia:
    -   <img alt="" src=images/Sketcher_CreateBSpline.svg  style="width:16px;"> **Przez punkty kontrolne**:
        1.  Opcjonalnie, zmień **Stopień** (możliwe również po wskazaniu punktów):
            -   Wprowadź liczbę większą niż zero.
            -   Wciśnij klawisz **U** aby zwiększyć stopień.
            -   Wciśnij klawisz **J** aby zmniejszyć stopień.
    -   <img alt="" src=images/Sketcher_CreateBSplineByInterpolation.svg  style="width:16px;"> **Przez węzły**: {{Version/pl|1.0}}
        1.  Krzywe złożone przez węzły są zawsze tworzone ze stopniem 3. Ale ich stopień można później zmienić. Zobacz [Uwagi](#Uwagi.md).
5.  Opcjonalnie, wciśnij klawisz **R** lub zaznacz pole **Okresowy** aby utworzyć zamkniętą krzywą złożoną (możliwe również po wskazaniu punktów). {{Version/pl|1.0}}
6.  Wybierz kilka punktów.
7.  Opcjonalnie, wciśnij klawisz **F** przed zakończeniem aby usunąć ostatni punkt. {{Version/pl|1.0}}
8.  Kliknij prawym przyciskiem myszy lub wciśnij klawisz **Esc** aby zakończyć wprowadzanie.
9.  Krzywa złożona zostanie utworzona razem z zestawem wewnętrznej geometrii (okręgi wag i węzły).
10. Jeśli narzędzie działa w [trybie kontynuacji](Sketcher_Workbench/pl#Tryby_kontynuacji.md):
    1.  Opcjonalnie, kontynuuj tworzenie krzywych złożonych.
    2.  Aby zakończyć, kliknij prawym przyciskiem myszy lub wciśnij klawisz **Esc** bądź uruchom narzędzie do tworzenia innej geometrii lub wiązań.



## Uwagi

-   Elementy wewnętrznej geometrii można usunąć. Ich odtworzenie jest możliwe w dowolnym momencie przy pomocy narzędzia [Pokaż / ukryj geometrię wewnętrzną](Sketcher_RestoreInternalAlignmentGeometry/pl.md).
-   Istnieje możliwość zdefiniowania wagi punktów kontrolnych poprzez zmianę rozmiarów promieni okręgów wagowych. Należy najpierw usunąć wiązania równościowe na okręgach. Wiązanie promienia jest dowolne, waga punktów kontrolnych będzie określona przez względne promienie okręgów. Działa to podobnie do grawitacji: im większy jest okrąg w stosunku do pozostałych, tym bardziej krzywa będzie przyciągana do punktu kontrolnego.
-   Stopień utworzonej krzywej złożonej można [zwiększyć](Sketcher_BSplineIncreaseDegree/pl.md) lub [zmniejszyć](Sketcher_BSplineDecreaseDegree/pl.md). Krotność węzłów również można [zwiększyć](Sketcher_BSplineIncreaseKnotMultiplicity/pl.md) lub [zmniejszyć](Sketcher_BSplineIncreaseKnotMultiplicity/pl.md).
-   Widoczność [stopi](Sketcher_BSplineDegree/pl.md), [wielokąta kontrolnego](Sketcher_BSplinePolygon/pl.md), [grzebienia krzywizny](Sketcher_BSplineComb/pl.md), [wielokrotności węzłów](Sketcher_BSplineKnotMultiplicity/pl.md) i [wag punktów kontrolnych](Sketcher_BSplinePoleWeight/pl.md) można włączać / wyłączać z paska narzędzi [Widok szkicu](Sketcher_Workbench/pl#Widok_szkicu.md).



## Ograniczenia

-   Kilka typów wiązań nie jest obecnie obsługiwanych.
-   Zdefiniowana krotność węzłów nie zawsze musi być respektowana:
    -   Dla krzywej okresowej, pierwszy węzeł (współbieżny z ostatnim) zawsze ma krotność 2.
    -   Dla krzywej nieokresowej, pierwszy i ostatni węzeł mają krotność 4.
    -   Jeśli punkty tuż przed i tuż po mają krotności \>=3, fragment między nimi jest w pełni ciągły i ten (środkowy) punkt będzie związany tylko wiązaniem punk-na-obiekcie. Jeśli potrzebny jest węzeł, rozważ użycie narzędzia [Wstaw węzeł krzywej złożonej](Sketcher_BSplineInsertKnot/pl.md).



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CreateBSpline/pl
