---
 TutorialInfo:l
   Topic: Import tekstu i geometrii z programu Inkscape
   Level: Początkujący
   Time: 30 minut
   Author: r-frank
   FCVersion: 0.16.6704
   Files: 
---

# Import text and geometry from Inkscape/pl







## Wprowadzenie

Ten samouczek ma na celu pokazanie, jak zaimportować tekst lub geometrię utworzoną w programie inkscape za pomocą formatu svg do programu FreeCAD.
Do tych operacji używane są Inkscape 0.91 i FreeCAD 0.16.6704 na Windows.



## Ogólne wskazówki dotyczące importu z Inkscape 

-   import svg we FreeCAD nie może obsłużyć pliku svg o rozdzielczości większej niż 45 dpi, więc sprawdź ustawienia w inkscape.
-   Podczas importowania obiektów ścieżek, które pojawiają się w oknie widoku 3D we FreeCAD niezbyt gładko, może to być kwestia ustawień FreeCAD dla widoku kształtu.
    -   We FreeCAD wybierz **Edycja → Preferencje ... → Projekt Części → Widok kształtu**.
    -   Jeśli chodzi o \"Tesselację\", \"Maksymalne dopuszczalne odchylenie w zależności od ramki otaczającej\", domyślną wartością jest \"0,5 %\",
    -   ustawienie tej wartości na niższą zwiększy płynność modelu w oknie widoku 3D *(i wykorzysta większą wydajność komputera)*,
    -   nie używaj wartości niższych niż \"0,01 %\", najprawdopodobniej spowoduje to awarię programu FreeCAD,
    -   w takim przypadku usunięcie \"system.cfg\" i \"user.cfg\" w katalogu użytkownika FreeCAD rozwiąże ten problem.



## Importowanie tekstu z programu inkscape 

-   W inkscape, po wstawieniu tekstu *(i być może zastosowaniu do niego efektów takich jak zginanie lub coś innego)* upewnij się, że:
    -   zaznaczyłeś tekst i wybrałeś **Ścieżka** → **Obiekt do ścieżki**,
    -   rozgrupuj obiekty,
    -   zapisz plik w formacie \"Zwykły SVG (\*.svg)\",
-   Otwórz plik we FreeCAD, wybierając opcję \"SVG jako geometria (importSVG)\".
-   Obiekt ścieżki dla każdej litery/liczby/znaku zostanie utworzony w widoku drzewa.
-   Użyj narzędzia [Ulepsz kształt](Draft_Upgrade/pl.md) na każdym obiekcie ścieżki, aby utworzyć ściany.
-   Użyj narzędzia Wyciągnij lub [Wyciągnij](Part_Extrude/pl.md) środowiska Część na powierzchniach, aby uzyskać bryły.
-   Możesz połączyć swoje obiekty lub wykonać na nich złożenia w zależności od planowanej dalszej pracy



## Importowanie geometrii z programu Inkscape 

Ponieważ inkscape i FreeCAD wydają się mieć różne podejścia do stosowania wymiarów na obiekcie svg, zalecanym przepływem pracy wydaje się być:

-   Rozgrupowanie wszystkich obiektów w Inkscape.
-   Zaznaczenie wszystkich obiektów w Inkscape.
-   Zastosowanie stylu obrysu o szerokości 0 mm *(tak, to jest zero milimetrów)* do wszystkich obiektów.
-   Zapisanie pliku w formacie \"Inkscape SVG (\*.svg)\" lub \"Zwykły SVG (\*.svg)\".
-   Otwarcie pliku w programie FreeCAD, wybierając opcję \"SVG jako geometria (importSVG)\".
-   wymiary obiektów w inkscape i FreeCAD powinny być teraz identyczne.



## Zasłużeni

Podziękowania dla użytkowników \"freecad-heini-1\" i \"herbk\" za przetestowanie i przekazanie cennych opinii.



---
⏵ [documentation index](../README.md) > [Import](Import_Workbench.md) > Import text and geometry from Inkscape/pl
