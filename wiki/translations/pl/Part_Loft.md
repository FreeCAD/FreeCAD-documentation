---
- GuiCommand:
   Name: Part Loft
   Name/pl: Part: Wyciągnij po profilach
   MenuLocation: Część -> Wyciągnięcie po profilach...
   Workbenches: Part_Workbench/pl
   Version: 0.13
   SeeAlso: Part_Sweep/pl
---

# Part Loft/pl



## Informacje ogólne 

Narzędzie **Wyciągnięcie przez profile** służy do utworzenia ściany, powłoki lub bryły z dwóch lub więcej profili. Profile mogą być punktami *(wierzchołkami)*, liniami *(krawędziami)*, poliliniami lub ścianami. Krawędzie i polilinie mogą być otwarte lub zamknięte. Istnieją różne [ograniczenia i komplikacje](Part_Loft/pl#Ograniczenia_i_komplikacje.md), patrz poniżej, jednak profile mogą pochodzić z [brył pierwotnych](Part_Workbench/pl.md) środowiska pracy Część, [obiektów](Draft_Workbench/pl.md) środowiska pracy Rysunek Roboczy oraz [Szkiców](Sketcher_Workbench/pl.md).

Wyciągnięcie przez profile ma trzy parametry: \"Powierzchnia prostokreślna\", \"Utwórz bryłę\" i \"Zamknięty\", z których każdy ma wartość {{true/pl}} lub {{false/pl}}.

Jeśli opcja **Utwórz bryłę** ma wartość {{True/pl}}, FreeCAD utworzy bryłę, jeśli profile mają zamkniętą geometrię, jeśli wartością jest {{False/pl}}, FreeCAD utworzy ścianę lub *(jeśli więcej niż jedna ściana)* powłokę dla profili otwartych lub zamkniętych.

Jeśli parametr \"powierzchnia prostokkreślna\" ma wartość {{true/pl}} FreeCAD utworzy ścianę, ściany lub bryłę z powierzchni prostokreślnych. [Strona Wiki o powierzchniach prostokreślnych](http://en.wikipedia.org/wiki/Ruled_surface).

Jeśli parametr \"Zamknięty\" ma wartość {{true/pl}}, FreeCAD próbuje połączyć ostatni profil z pierwszym profilem, aby utworzyć zamkniętą figurę.

Więcej informacji na temat sposobu łączenia profili można znaleźć na stronie [Szczegóły techniczne wyciągnięcia przez profile](Part_Loft_Technical_Details/pl.md).

![centre\|Wyciągnięcie przez profile. Z trzech profili, które są dwoma okręgami i jedną elipsą środowiska pracy Część. Parametry to Utwórz bryłę: {{CheckBox|TRUE|}} i Powierzchnia prostokreślna: {{CheckBox|TRUE|}}.](images/Part_Loft_solid_ruled_from3profiles_example_FreeCAD_0_13.jpg )



## Uwagi

-   Obiekty typu[odnośnik](App_Link/pl.md) powiązane z odpowiednimi typami obiektów oraz kontenery typu [część](App_Part/pl.md) z odpowiednimi widocznymi obiektami wewnątrz mogą być również używane jako profile i ścieżki. {{Version/pl|0.20}}



## Ograniczenia i komplikacje 

-   Wierzchołek lub punkt
    -   Wierzchołek lub punkt może być użyty tylko jako pierwszy i / lub ostatni profil na liście profili.
        -   Na przykład
            -   nie można wykonać wyciągnięcie od okręgu przez punkt do elipsy.
            -   Można jednak wykonać wyciągnięcie z punktu do okręgu, przez elipsę do innego punktu.
-   W jednym wyciągnięciu nie można mieszać profili o geometrii otwartej i zamkniętej.
    -   W jednym wyciągnięciu wszystkie profile *(linie, przewody itp.)* muszą być otwarte lub zamknięte.
        -   Na przykład
            -   FreeCAD nie może wykonać wyciągnięcia pomiędzy jednym okręgiem i jedną domyślną linią środowiska Część.
-   Cechy środowiska Rysunek Roboczy.
    -   Cechy środowiska Rysunek Roboczy mogą być bezpośrednio używane jako profile w FreeCAD {{VersionPlus/pl|0.14}}.
        -   Na przykład następujące elementy szkicu mogą być użyte jako profile w Wyciągnięciu przez profile:
            -   Szkic wielokąta,
            -   Punkt, Linia, polilinia środowiska Rysunek Roboczy,
            -   Szkic krzywej złożonej, krzywej Béziera,
            -   Szkic okręgu, elipsy, prostokąta.
-   Szkice środowiska Projekt Części.
    -   Profil można utworzyć za pomocą szkicu. Jednak tylko prawidłowy szkic zostanie wyświetlony na liście i będzie dostępny do wyboru.
    -   Szkic musi zawierać tylko jedną otwartą lub zamkniętą krzywą lub linię *(może to być wiele linii, jeśli wszystkie te linie są połączone w taki sam sposób, jak pojedyncza polilinia)*.
-   Środowisko Część.
    -   Profil może być prawidłowym prymitywem geometrycznym części, który można utworzyć za pomocą narzędzia [Utwórz geometrię pierwotną](Part_Primitives/pl.md).
        -   Na przykład następujące prymitywy geometryczne części mogą być prawidłowym profilem:
            -   Punkt *(wierzchołek)*, Linia *(krawędź)*,
            -   Helisa, Spirala,
            -   Okrąg, Elipsa;
            -   Wielokąt foremny,
            -   Płaszczyzna *(Ściana)*.

-   Zamknięte wyciągnięcie.
    -   Wyniki zamkniętych wyciągnięć przez profile mogą być nieoczekiwane - wyciągnięcie może się skręcać lub załamywać. Wyciąganie jest bardzo wrażliwe na rozmieszczenie profili i złożoność krzywych wymaganych do połączenia odpowiednich wierzchołków we wszystkich profilach.



## Przykład wyciągnięcia przez profile 

Narzędzie **Wyciągnięcie przez profile** znajduje się w środowisku pracy Część, w menu **Część → Wyciągnięcie przez profile ...**. Jest również dostępne na pasku narzędzi **Narzędzia środowiska Część**.

![](images/Part_Loft_Ikon_Ballon_Hilfe.png )

W oknie \"Wyciągnięcie przez profile\" będą dwie listy: \"Dostępne profile\" i \"Wybrane profile\".

![](images/Part_Loft_Liste3.png )

### Wybór sekcji 

W sekcji \"Dostępne profile\" wyświetlane są dostępne elementy. Dwie sekcje z tej listy muszą zostać wybrane jedna po drugiej.

![](images/Part_Loft_Liste_Auswahl_3b.png )

Następnie za pomocą przycisku niebieskiej strzałki element ten zostanie dodany do listy \"Wybrane profile\".

![](images/Part_Loft_Liste_Auswahl_3c.png )

Wybrane elementy muszą być tego samego typu.

Wskazówka: aktywne / wybrane elementy z listy są wyświetlane w oknie widoku 3D jako zaznaczone.



### Zakończenie polecenia 

Jeśli wybrano obie sekcje, polecenie można zakończyć naciskając **OK**.

![](images/Part_Loft_Liste_Auswahl_3d.png )



## Wynik

Z zamkniętych linii otrzymujemy powierzchnie, które można uznać za pobieżny wygląd brył.

![](images/Part_Loft_geschlossen.png )

Jeśli rzeczywiście konieczne jest utworzenie bryły, użyj przycisku {{CheckBox|TRUE|}} Utwórz bryłę lub po utworzeniu wyciągnięcia przejdź do jego zakładki \"Właściwości\" \"Dane\" i ustaw przełącznik \"Bryła\" na wartość {{true/pl}}.

Procedura obsługi dla otwartych polilinii jest taka sama, jak opisana powyżej.



### Zmiana wyboru sekcji 

Jeśli chcesz zmienić wybór sekcji po utworzeniu wyciągnięcia, możesz wybrać pole **Sekcje** na karcie \"Dane\" i kliknąć pojawiający się przycisk **…**. Zostanie wyświetlone okno **Łącze** z listą wszystkich możliwych do wybrania sekcji, a bieżący wybór zostanie podświetlony. Można tam usunąć lub dodać dodatkowe pozycje.

Kolejność sekcji zależy od kolejności kliknięć na liście. Jeśli chcesz wprowadzić znaczące zmiany, zaleca się najpierw odznaczenie wszystkich, a następnie rozpoczęcie wyboru we właściwej kolejności.



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Loft/pl
