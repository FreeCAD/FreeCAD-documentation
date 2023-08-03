---
 GuiCommand:
   Name: PartDesign AdditivePipe
   Name/pl: PartDesign AdditivePipe
   MenuLocation: Projekt Części , Utwórz cechę przez dodanie , Uzupełnianie wyciągnięciem wzdłuż ścieżki
   Workbenches: PartDesign_Workbench/pl
   Version: 0.17
   SeeAlso: PartDesign_AdditiveLoft/pl, PartDesign_SubtractivePipe/pl
---

# PartDesign AdditivePipe/pl



## Opis

**Wyciągnięcie wzdłuż ścieżki** utworzy bryłę w aktywnej Zawartości poprzez przeciągnięcie jednego lub więcej szkiców *(zwanych również przekrojami)* wzdłuż otwartej lub zamkniętej ścieżki. Jeśli bryła zawiera już elementy, dodane wyciągnięcie zostanie z nimi połączone.

![](images/PartDesign_AdditivePipe_example.svg ) 
*Po lewej: przekroje ''(A)'' i ''(B)'', które mają zostać poprowadzone wzdłuż ścieżki ''(C)'', wyciągnięcie wynikowe po prawej.*



## Użycie

Powyższy przykładowy obraz przedstawia dwa różne kształty przekroju. Poniższy tekst opisuje procedurę tylko dla jednego kształtu. Pozwoli to uzyskać część o takim samym przekroju wzdłuż całej ścieżki.

1.  Utwórz dwa oddzielne szkice,
    -   jeden dla ścieżki, np. dwie linie połączone krzywą, jak na powyższym obrazku,
    -   jeden dla kształtu przekroju, np. okrąg, jak pierwszy kształt na powyższym obrazku. Zamiast szkicu można również użyć ściany obiektu 3D. *({{Version/pl|0.20}})*
2.  **Ułóż** poprawnie dwa kształty w oknie widoku 3D. Zaleca się umieszczenie punktu odniesienia przekroju na linii ścieżki. W większości przypadków oba szkice powinny być *ortogonalne*. Można to zrobić za pomocą funkcji \"Tryb odłączenia\" *(spraw, by oba szkice były widoczne za pomocą klawisza **Spacja**. Wybierz szkic przekroju. Wybierz Własciwości/Zakłdadka Dane/Tryb odłączenia. Kliknij pojawiający się przycisk **...** po prawej stronie. W oknie dialogowym Dołączenie wybierz wierzchołek szkicu ścieżki i wybierz odpowiedni tryb, aby prawidłowo wyrównać oba szkice)*.
3.  Naciśnij przycisk **<img src="images/PartDesign_AdditivePipe.svg" width=24px> '''Uzupełnianie wyciągnięciem wzdłuż ścieżki'''**.
4.  W oknie dialogowym **Wybierz cechę** wybierz szkic, który ma zostać użyty jako przekrój i kliknij przycisk **OK**.
    -   Alternatywnie, szkic lub ściana obiektu 3D ({{Version/pl|0.20}}) może zostać wybrana przed naciśnięciem przycisku Uzupełnianie wyciągnięciem wzdłuż ścieżki. W takim przypadku nie pojawi się okno dialogowe \"Wybierz cechę\".
5.  W oknie *Parametry wyciągnięcia* w *Ścieżce do przeciągnięcia* naciśnij przycisk **Obiekt**.
6.  Wybierz szkic, który ma zostać użyty jako ścieżka w oknie widoku 3D. W tym przypadku cały szkic zostanie użyty jako ścieżka.
    -   Alternatywnie można wybrać pojedyncze krawędzie szkicu, naciskając przycisk **Dodaj krawędź** i wybierając krawędzie w oknie widoku 3D. Należy pamiętać, że dla każdej krawędzi trzeba ponownie nacisnąć przycisk **Dodaj krawędź**. Musisz wybrać ciągłą linię bez rozgałęzień.
7.  Pozostałe ustawienia powinny w większości przypadków działać z ustawieniami domyślnymi.
8.  Kliknij **OK**.

Aby użyć więcej niż jednego przekroju, zacznij od pierwszego szkicu przekroju, jak opisano powyżej. Następnie w sekcji *Przekształcenie sekcji* ustaw tryb przekształcenia na *Sekcja wielokrotna*. Naciśnij **Dodaj profil sekcji**, a następnie wybierz szkic w oknie[Widoku 3D](3D_view/pl.md). Powtórz tę czynność dla każdej dodatkowej sekcji przekroju.



## Opcje

**Przekształcenie sekcji**:

-   Wybierz **Stały**, aby użyć pojedynczego profilu
-   Wybierz **Sekcja wielokrotna**, aby użyć wielu profili

**Kierunek sekcji profilu**:

-   Standardowy

    :   Utrzymuje kształt przekroju prostopadle do ścieżki. Jest to ustawienie domyślne.
-   Stały
    -   Orientacja ustalona przez pierwszy profil pozostaje stała przez cały czas. Wyłącza to wyrównanie do wektora normalnego ścieżki. Oznacza to, że kształt przekroju nie będzie obracał się wraz ze ścieżką. Przeciągnij wzdłuż okręgu, aby zobaczyć efekt.
-   Freneta
    -   Stwórz możliwie najmniejsze skręcenie profilu. Więcej informacji można znaleźć na stronie [Wzory Freneta-Serreta](https://en.wikipedia.org/wiki/Frenet%E2%80%93Serret_formulas).
-   Pomocniczy
    -   Określ ścieżkę pomocniczą do prowadzenia profilu.
    -   Dla każdego punktu **P** wzdłuż ścieżki wyciągnięcia, będzie odpowiadał punkt **Q** na ścieżce pomocniczej.
    -   W miarę przeciągania profilu zostanie on przekształcony w taki sposób, że linia **PQ** będzie normalną ścieżki przeciągania.
    -   Jeśli ustawiona jest opcja **Krzywoliniowość**, punkty **Q** są skalowane proporcjonalnie wzdłuż ścieżki, niezależnie od jej długości.
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

-    **Styczna łuku**: przyjmuje wartość {{true/pl}} lub {{false/pl}} *(domyślnie)*. Wartość true rozszerza ścieżkę o krawędzie styczne.

-    **Pomocnicza styczna łuku**: przyjmuje wartość {{true/pl}} lub {{false/pl}} *(domyślnie)*. Wartość {{true/pl}} rozszerza ścieżkę pomocniczą o krawędzie styczne.

-    **Pomocnicza krzywoliniowa**: przyjmuje wartość {{true/pl}} lub {{false/pl}} *(domyślnie)*. Wartość {{true/pl}} oblicza normalną między jednakowo odległymi punktami na obu grzbietach.

-    **Tryb**: tryb profilu. Zobacz [Opcje](#Opcje.md).

-    **Binormal**: wektor binormalny dla odpowiedniego trybu orientacji.

-    **Przejście**: tryb przejścia. Dostępne opcje to *Przekształcony*, *Ostry narożnik* lub *Zaokrąglenie*.

-    **Przekształcenie**: *Stały* używa pojedynczego przekroju. *Sekcja wielokrotna* wykorzystuje dwa lub więcej przekrojów. *Liniowy*, *Kształt litery S* i *Interpolacja* obecnie nie działają.



## Uwagi

-   Aby lepiej kontrolować kształt obiektu wyciągnięcia, zaleca się, aby wszystkie przekroje miały taką samą liczbę segmentów. Na przykład, dla przejścia pomiędzy prostokątem i okręgiem, okrąg powinien być podzielony na 4 połączone łuki.
-   Można tworzyć przejście od lub w kierunku pojedynczego [wierzchołka](Glossary#V.md) ze szkicu lub bryły. <small>(v0.20)</small> .
-   Po wybraniu [wierzchołka](Glossary#V.md) jako sekcji, musi to być ostatnia sekcja przejścia. W przeciwnym razie bryła przejścia składałaby się z dwóch brył połączonych w jednym punkcie. Naruszałoby to definicję obiektu 3D w jądrze CAD. Kolejność sekcji można zmienić, przeciągając je na liście.
-   Ścieżka może pochodzić tylko z jednego szkicu, elementu lub Łącznika kształtu. Jeśli chcesz przeciągnąć wzdłuż kilku krawędzi z różnych szkiców, użyj narzędzia **[<img src=images/PartDesign_SubShapeBinder.svg style="width:16px">. [Łącznik kształtów podrzędnych](PartDesign_SubShapeBinder/pl.md)**.
-   Ścieżka nie może zawierać rozgałęzień, trójników itp. Pętle są dozwolone.
-   Może to prowadzić do problemów, jeśli przekrój nie jest prostopadły do ścieżki w przestrzeni 3D.
-   Przekrój nie może leżeć na tej samej płaszczyźnie, co przekrój bezpośrednio go poprzedzający.
-   Przekroje nie mogą zawierać rozłącznych lub przecinających się pętli.





{{PartDesign Tools navi

}}



---
⏵ [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign AdditivePipe/pl
