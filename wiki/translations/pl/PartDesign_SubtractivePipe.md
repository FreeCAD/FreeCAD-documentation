---
- GuiCommand:
   Name:PartDesign SubtractivePipe
   Name/pl:Projekt Części: Odejmowanie wyciągnięciem wzdłuż ścieżki
   MenuLocation:Projekt Części - Utwórz cechę przez odjęcie - Odejmowanie wyciągnięciem wzdłuż ścieżki
   Workbenches:[Projekt Części](PartDesign_Workbench/pl.md)
   Version:0.17
   SeeAlso:[Uzupełnianie wyciągnięciem wzdłuż ścieżki](PartDesign_AdditivePipe/pl.md), [Odejmowanie wyciągnięciem przez profile](PartDesign_SubtractiveLoft/pl.md)
---

# PartDesign SubtractivePipe/pl



## Opis

Funkcja **Odejmowanie wyciągnięciem wzdłuż ścieżki** tworzy bryłę odejmującą w aktywnej Zawartości poprzez przeciągnięcie jednego lub więcej szkiców *(zwanych również przekrojami)* wzdłuż otwartej lub zamkniętej ścieżki. Jej kształt jest następnie odejmowany od istniejącej bryły. Odejmowanie wyciągnięciem wzdłuż ścieżki jest często używane w połączeniu z funkcją [Helisy](Part_Helix/pl.md) środowiska Część i [Łącznik kształtu](PartDesign_ShapeBinder.md) w celu utworzenia gwintu. Zobacz stronę [Poradnik: Tworzenie gwintów](Thread_for_Screw_Tutorial/pl.md) aby uzyskać szczegółowe informacje na ten temat.



## Użycie

1.  Naciśnij przycisk **<img src="images/PartDesign_SubtractivePipe.svg" width=24px> '''Odejmowanie wyciągnięciem wzdłuż ścieżki'''**.
2.  W oknie dialogowym **Wybierz cechę** wybierz szkic, który ma zostać użyty jako pierwszy przekrój i kliknij przycisk **OK**.
    -   Alternatywnie, szkic lub ścianę obiektu 3D *({{Version/pl|0.20}})* można wybrać przed naciśnięciem przycisku Odejmowanie wyciągnięciem wzdłuż ścieżki.
3.  W oknie **Parametrach wyciągnięcia** w sekcji *Profil* naciśnij przycisk **Obiekt**.
4.  Wybierz szkic, który ma zostać użyty jako ścieżka w oknie widoku 3D:
    -   Alternatywnie można wybrać krawędzie bryły, naciskając przycisk **Dodaj krawędź** i wybierając krawędzie w widoku 3D.
5.  Aby użyć więcej niż jednego przekroju, w sekcji *Przekształcenie sekcji* ustaw tryb przekształcenia na *Przekrój wielokrotny*. Naciśnij **Dodaj sekcję**, a następnie wybierz szkic w oknie widoku 3D. Powtórz dla każdego dodatkowego przekroju.
6.  W razie potrzeby ustaw opcje i kliknij **OK**.



## Opcje

**Przekształcenie sekcji**:

-   Wybierz **Stały**, aby użyć pojedynczego profilu
-   Wybierz **Sekcja wielokrotna**, aby użyć wielu profili

**Orientacja przekroju**:

-   Standardowy
    -   Utrzymuje kształt przekroju prostopadle do ścieżki. Jest to ustawienie domyślne.
-   Stały
    -   Orientacja ustalona przez pierwszy profil pozostaje stała przez cały czas. Wyłącza to wyrównanie do wektora normalnego ścieżki. Oznacza to, że kształt przekroju nie będzie obracał się wraz ze ścieżką. Przeciągnij wzdłuż okręgu, aby zobaczyć efekt.
-   Freneta.
    -   Stwórz możliwie najmniejsze skręcenie profilu. Więcej informacji można znaleźć na stronie [Wzory Freneta-Serreta](https://en.wikipedia.org/wiki/Frenet%E2%80%93Serret_formulas).
-   Pomocniczy
    -   Określ ścieżkę pomocniczą do prowadzenia profilu.
    -   Dla każdego punktu **P** wzdłuż ścieżki przeciągania, będzie odpowiadał punkt **Q** na ścieżce pomocniczej.
    -   W miarę przeciągania profilu zostanie on przekształcony w taki sposób, że linia **PQ** będzie normalną ścieżki przeciągania.
    -   Jeśli ustawiona jest opcja **Krzywoliniowość**, punkty **Q** są skalowane proporcjonalnie wzdłuż ścieżki przeciągania, niezależnie od jej długości.
-   Binormalny
    -   Określ wektor binormalny w X, Y i Z.

**Przejście narożnika**

-   Przekształcony
-   Ostry narożnik
-   Zaokrąglenie



## Właściwości

-    **Etykieta**: nazwa nadana operacji, nazwa ta może być dowolnie zmieniana.

-    **Ulepsz**: przyjmuje wartość {{true/pl}} lub {{false/pl}}. Jeśli jest ustawiona na {{true/pl}}, czyści bryłę z resztkowych krawędzi pozostawionych przez elementy. Zobacz stronę [Udoskonal kształt](Part_RefineShape/pl.md) aby uzyskać więcej szczegółów.

-    **Sekcja**: lista użytych przekrojów.

-    **Styczna łuku**: przyjmuje wartość {{true/pl}} lub {{false/pl}} *(domyślnie)*. Wartość {{true/pl}} rozszerza ścieżkę o krawędzie styczne.

-    **Pomocnicza styczna łuku**: przyjmuje wartość {{true/pl}} lub {{false/pl}} *(domyślnie)*. Wartość true rozszerza ścieżkę pomocniczą o krawędzie styczne.

-    **Pomocnicza krzywoliniowa**: przyjmuje wartość {{true/pl}} lub {{false/pl}} *(domyślnie)*. Wartość {{true/pl}} oblicza normalną między jednakowo odległymi punktami na obu grzbietach.

-    **Tryb**: tryb profilu. Zobacz [Opcje](#Opcje.md).

-    **Binormal**: wektor binormalny dla odpowiedniego trybu orientacji.

-    **Przejście**: tryb przejścia. Dostępne opcje to *Przekształcony*, *Ostry narożnik* lub *Zaokrąglenie*.

-    **Przekształcenie**: *Stały* używa pojedynczego przekroju. *Sekcja wielokrotna* wykorzystuje dwa lub więcej przekrojów. *Liniowy*, *Kształt litery S* i *Interpolacja* obecnie nie działają.



## Uwagi

-   Aby lepiej kontrolować kształt obiektu wyciągnięcia, zaleca się, aby wszystkie przekroje miały taką samą liczbę segmentów. Na przykład, dla przejścia pomiędzy prostokątem i okręgiem, okrąg powinien być podzielony na 4 połączone łuki.
-   Można tworzyć przejście od lub w kierunku pojedynczego [wierzchołka](Glossary#V.md) ze szkicu lub bryły. <small>(v0.20)</small> .
-   Po wybraniu [wierzchołka](Glossary#V.md) jako sekcji, w większości przypadków musi to być ostatnia sekcja przejścia. Kolejność sekcji można zmienić, przeciągając je na liście.
-   Ścieżka może pochodzić tylko z jednego szkicu, elementu lub Łącznika kształtu. Jeśli chcesz przeciągnąć wzdłuż kilku krawędzi z różnych szkiców, użyj narzędzia **[<img src=images/PartDesign_SubShapeBinder.svg style="width:16px">. [Łącznik kształtów podrzędnych](PartDesign_SubShapeBinder/pl.md)**.
-   Ścieżka nie może zawierać rozgałęzień, trójników itp. Pętle są dozwolone.
-   Może to prowadzić do problemów, jeśli przekrój nie jest prostopadły do ścieżki w przestrzeni 3D.
-   Przekrój nie może leżeć na tej samej płaszczyźnie, co przekrój bezpośrednio go poprzedzający.
-   Przekroje nie mogą zawierać rozłącznych lub przecinających się pętli.





{{PartDesign Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign SubtractivePipe/pl
