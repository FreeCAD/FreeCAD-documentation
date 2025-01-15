---
 GuiCommand:
   Name: Sketcher Intersection
   Name/pl: Szkicownik: Przecięcie
   MenuLocation: Szkic , Narzędzia szkicownika , Utwórz geometrię zewnętrzną przecięcia
   Workbenches: Sketcher_Workbench/pl
   Shortcut: **G** **I**
   Version: 1.1
   SeeAlso: Sketcher_ToggleConstruction/pl
---

# Sketcher Intersection/pl



## Opis

Narzędzie <img alt="" src=images/Sketcher_Intersection.svg  style="width:24px;"> [Przecięcie](Sketcher_Intersection/pl.md) przecina płaszczyzną szkicu ściany i/lub krawędzie należące do obiektów poza szkicem. Geometria przecięcia jest nazywana \"geometrią zewnętrzną\". Pozostaje ona parametrycznie powiązana ze swoimi obiektami źródłowymi. Geometria zewnętrzna jest oznaczona dedykowanym [kolorem](Sketcher_Preferences/pl#Wygląd.md) (domyślnie magenta) i typem linii. Może być geometrią definiującą widoczną poza szkicem lub geometrią konstrukcyjną niewidoczną poza szkicem.



## Użycie

1.  Istnieje kilka sposobów na uruchomienie narzędzia:
    -   Naciśnij przycisk **<img src="images/Sketcher_Intersection.svg" width=16px> [Utwórz zewnętrzną geometrię przecięcia](Sketcher_Intersection/pl.md)**.
    -   Wybierz opcję **Sketcher → Narzędzia szkicownika → <img src="images/Sketcher_Intersection.svg" width=16px> Utwórz zewnętrzną geometrię przecięcia** z menu.
    -   Kliknij prawym przyciskiem myszy w [widoku 3D](3D_view/pl.md) i wybierz opcję **<img src="images/Sketcher_Intersection.svg" width=16px> Utwórz zewnętrzną geometrię przecięcia** z menu kontekstowego.
    -   Użyj skrótu klawiaturowego: **G**, a następnie **I**.
2.  Kursor zmienia się na krzyżyk z ikoną narzędzia.
3.  Wybierz jedną lub więcej zewnętrznych ścian i/lub krawędzi. Zobacz [Uwagi](#Uwagi.md).
4.  Tworzona jest zewnętrzna geometria.
5.  To narzędzie zawsze działa w trybie ciągłym: opcjonalnie kontynuuj wybieranie zewnętrznych ścian i/lub krawędzi.
6.  Aby zakończyć, kliknij prawym przyciskiem myszy, naciśnij **Esc** lub uruchom inne narzędzie do tworzenia geometrii lub więzów.



## Uwagi

-   Wybór śiany tworzy jedną lub więcej krawędzi, wybór krawędzi tworzy jeden lub więcej punktów. Geometria nie dotykająca płaszczyzny szkicy jest ignorowana.
-   Geometria zewnętrzna jest tworzona jako definiująca lub konstrukcyjna w zależności od statusu narzędzia [Przełącz tryb konstrukcji](Sketcher_ToggleConstruction/pl.md). To narzędzie może też przełączać tryb poszczególnych krawędzi. Zaznacz opcję **Edycja → Preferencje... → Szkicownik → Ogólne → Zawsze dodawaj geometrię zewnętrzną jako geometrię odniesienia** aby ignorować status tego narzędzia i zawsze dodawać geometrię zewnętrzną jako geometrię odniesienia (konstrukcyjną).



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher Intersection/pl
