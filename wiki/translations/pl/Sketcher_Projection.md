---
 GuiCommand:
   Name: Sketcher Projection
   Name/pl: Szkicownik: Rzutowanie
   MenuLocation: Szkic , Narzędzia szkicownika , Utwórz geometrię zewnętrzną rzutowania
   Workbenches: Sketcher_Workbench/pl
   Shortcut: **G** **X**
   Version: 1.1
   SeeAlso: Sketcher_ToggleConstruction/pl
---

# Sketcher Projection/pl



## Opis

Narzędzie <img alt="" src=images/Sketcher_Projection.svg  style="width:24px;"> [Rzutowanie](Sketcher_Projection/pl.md) rzutuje na płaszczyznę szkicu ściany i/lub krawędzie należące do obiektów poza szkicem. Rzutowana geometria jest nazywana \"geometrią zewnętrzną\". Pozostaje ona parametrycznie powiązana ze swoimi obiektami źródłowymi. Geometria zewnętrzna jest oznaczona dedykowanym [kolorem](Sketcher_Preferences/pl#Wygląd.md) (domyślnie magenta) i typem linii. Może być geometrią definiującą widoczną poza szkicem lub geometrią konstrukcyjną niewidoczną poza szkicem.



## Użycie

1.  Istnieje kilka sposobów na uruchomienie narzędzia:
    -   Naciśnij przycisk **<img src="images/Sketcher_Projection.svg" width=16px> [Utwórz zewnętrzną geometrię rzutowania](Sketcher_Projection.md)**.
    -   Wybierz opcję **Sketcher → Narzędzia szkicownika → <img src="images/Sketcher_Projection.svg" width=16px> Utwórz zewnętrzną geometrię rzutowania** z menu.
    -   Kliknij prawym przyciskiem myszy w [widoku 3D](3D_view.md) i wybierz opcję **<img src="images/Sketcher_Projection.svg" width=16px> Utwórz zewnętrzną geometrię rzutowania** z menu kontekstowego.
    -   Użyj skrótu klawiaturowego: **G**, a następnie **X**.
2.  Kursor zmienia się na krzyżyk z ikoną narzędzia.
3.  Wybierz jedną lub więcej zewnętrznych ścian, krawędzi i/lub wierzchołków. Zobacz [Uwagi](#Notes.md).
4.  Tworzona jest zewnętrzna geometria.
5.  To narzędzie zawsze działa w trybie ciągłym: opcjonalnie kontynuuj wybieranie zewnętrznych ścian, wierzchołków i/lub krawędzi.
6.  Aby zakończyć, kliknij prawym przyciskiem myszy, naciśnij **Esc** lub uruchom inne narzędzie do tworzenia geometrii lub więzów.



## Uwagi

-   Wszystkie krawędzie ściany są rzutowane na płaszczyznę szkicu.
-   Geometria zewnętrzna jest tworzona jako definiująca lub konstrukcyjna w zależności od statusu narzędzia [Przełącz tryb konstrukcji](Sketcher_ToggleConstruction/pl.md). To narzędzie może też przełączać tryb poszczególnych krawędzi. Zaznacz opcję **Edycja → Preferencje... → Szkicownik → Ogólne → Zawsze dodawaj geometrię zewnętrzną jako geometrię odniesienia** aby ignorować status tego narzędzia i zawsze dodawać geometrię zewnętrzną jako geometrię odniesienia (konstrukcyjną).



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher Projection/pl
