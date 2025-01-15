---
 GuiCommand:
   Name: Sketcher Split
   Name/pl: Szkicownik: Podziel krawędź
   MenuLocation: Szkic , Narzędzia szkicownika , Podziel krawędź
   Workbenches: Sketcher_Workbench/pl
   Shortcut: **G** **Z**
   Version: 0.20
   SeeAlso: Sketcher_Trimming/pl
---

# Sketcher Split/pl



## Opis

Narzędzie <img alt="" src=images/Sketcher_Split.svg  style="width:24px;"> **Podziel krawędź** dzieli krawędź. Jeśli krawędź jest krzywą zamkniętą *(np. okrąg, elipsa lub krzywa złozona okresowa)*, jest ona konwertowana na krzywą otwartą *(odpowiednio łuk, łuk elipsy lub krzywa złozona nieokresowa)*.



## Użycie

Zapoznaj się również z informacjami na stronie [Pomoce kreślarskie](Sketcher_Workbench/pl#Pomoce_kreślarskie.md).

1.  Istnieje kilka sposobów wywołania narzędzia:
    -   Naciśnij przycisk **<img src="images/Sketcher_Split.svg" width=16px> '''Podziel krawędź'''**.
    -   Wybierz z menu opcję **Szkic → Narzędzia szkicownika → <img src="images/Sketcher_Split.svg" width=16px> Podziel krawędź**.
    -   Użyj skrótu klawiaturowego: **G**, a następnie **Z**.
2.  Jeśli istnieje poprzednie zaznaczenie, zostanie ono usunięte. Narzędzie nie akceptuje wcześniejszego zaznaczenia.
3.  Kursor zmieni się w krzyżyk z ikoną narzędzia.
4.  Kliknij krawędź w miejscu, w którym ma zostać podzielona.
5.  Jeśli oryginalna krawędź jest linią lub krzywą otwartą, utworzone zostaną dwie nowe krawędzie połączone wiązaniem [zbieżności punktów](Sketcher_ConstrainCoincident/pl.md). W przypadku krzywych zamkniętych tworzona jest nowa krzywa otwarta, a nowy punkt nie otrzymuje wiązania zbieżności. Istniejące wiązania są przenoszone na nowe krawędzie. Zobacz [Uwagi](#Uwagi.md).
6.  To narzędzie zawsze działa w trybie kontynuacji: opcjonalnie kontynuuj dzielenie krawędzi.
7.  Aby zakończyć, kliknij w pustym obszarze w oknie [widoku 3D](3D_view/pl.md), kliknij prawym przyciskiem myszy lub naciśnij **Esc**, lub uruchom inne narzędzie do tworzenia geometrii lub wiązań.



## Uwagi

-   Wiązanie [zbieżności](Sketcher_ConstrainCoincident/pl.md) jest stosowane do punktów środkowych nowych łuków.
-   Wiązania [promienia](Sketcher_ConstrainRadius/pl.md) i [średnicy](Sketcher_ConstrainDiameter.md) są kopiowane do nowych łuków *(co powoduje redundancję)*.
-   Wiązania zbieżności i [punkt na obiekcie](Sketcher_ConstrainPointOnObject/pl.md) są przenoszone do najbliższej nowej krawędzi.
-   Więzy [poziomu](Sketcher_ConstrainHorizontal/pl.md) i [pionu](Sketcher_ConstrainVertical/pl.md) między punktami są przenoszone do najbliższej nowej krawędzi.
-   Wiązania poziome i pionowe dołączone do linii są kopiowane do nowych segmentów linii.
-   Wiązania [równoległości](Sketcher_ConstrainParallel/pl.md) i [prostopadłości](Sketcher_ConstrainPerpendicular/pl.md) są kopiowane do nowych segmentów linii, dla nowych łuków są one kopiowane tylko do najbliższego.
-   Wiązania [odległość pozioma](Sketcher_ConstrainDistanceX/pl.md), [odległość pionowa](Sketcher_ConstrainDistanceY/pl.md) i [odległość](Sketcher_ConstrainDistance/pl.md) są przenoszone na najbliższą nową krawędź.
-   Wiązania [kąta](Sketcher_ConstrainAngle/pl.md), [symetrii](Sketcher_ConstrainSymmetric/pl.md) i [zablokowania](Sketcher_ConstrainBlock/pl.md) nie są obecnie przenoszone.



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher Split/pl
