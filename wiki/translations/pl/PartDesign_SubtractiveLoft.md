---
- GuiCommand   */pl
   Name   *PartDesign SubtractiveLoft
   Name/pl   *Projekt Części   * Odejmowanie wyciągnięciem przez profile
   MenuLocation   *Projekt Części → Utwórz cechę przez odjęcie → Odejmowanie wyciągnięciem przez profile
   Workbenches   *[Projekt Części](PartDesign_Workbench/pl.md)
   Version   *0.17
   SeeAlso   *[Wyciągnięcie przez profile](PartDesign_AdditiveLoft/pl.md), [Odejmowanie wyciągnięciem wzdłuż ścieżki](PartDesign_SubtractivePipe/pl.md)
---

# PartDesign SubtractiveLoft/pl

## Opis

**Odejmowanie wyciągnięciem przez profile** tworzy w aktywnej Zawartości bryłę do odjęcia poprzez przejście pomiędzy dwoma lub więcej szkicami *(zwanymi również przekrojami)*. Jej kształt jest następnie odejmowany od istniejącej bryły.

## Użycie

### Przepływ pracy pa podstawie okienka dialogowego 

1.  Naciśnij przycisk **[<img src=images/PartDesign_SubtractiveLoft.svg style="width   *24px"> [Odejmowanie wyciągnięciem przez profile](PartDesign_SubtractiveLoft/pl.md)**.
2.  W oknie dialogowym **Wybierz cechę** wybierz szkic, który ma być użyty jako obiekt profilu bazowego i kliknij na przycisk **OK**.
    -   Alternatywnie można wybrać pojedynczy szkic lub ścianę obiektu 3D ({{Version/pl|0.20}}) przed naciśnięciem przycisku wyciągnięcia.
3.  W sekcji **Parametry wyciągnięcia przez profile** naciśnij przycisk **Dodaj sekcję profilu**.
4.  Wybierz następny szkic w oknie [widoku 3D](3D_view/pl.md). Powtórz tę czynność, aby wybrać więcej szkiców w kolejności, w jakiej mają być poddawane rzutowaniu. *(Kolejność sekcji można zmienić w dowolnym momencie, później w oknie dialogowym wyciągnięcia, przeciągając sekcje z listy na żądaną pozycję {{Version/pl|0.19}})*.
5.  Ustaw opcje w razie potrzeby i kliknij **OK**.

### Przepływ pracy pa podstawie zaznaczania 


{{Version/pl|0.19}}

1.  Wybierz kilka szkiców. Nie jest ważne, w jakiej kolejności je wybierzesz   *
    -   Szkic wybrany jako pierwszy stanie się obiektem profilu bazowego w następnym kroku
    -   Szkice wybrane po pierwszym staną się profilami wyciągnięcia. Również tutaj ważna jest kolejność wyboru   * szkic wybrany jako drugi stanie się pierwszą sekcją wyciągnięcia, szkic wybrany jako trzeci stanie się drugą sekcją itd. *(Kolejność sekcji można zmienić w dowolnym momencie później, w oknie dialogowym wyciągnięcia, przeciągając sekcje z listy na żądaną pozycję)*. {{Version/pl|0.19}}
    -   Pierwszy lub ostatni wybór może być również ścianą obiektu 3D *({{Version/pl|0.20}})*.
2.  Naciśnij przycisk **[<img src=images/PartDesign_SubtractiveLoft.svg style="width   *24px"> [Odejmowanie wyciągnięciem przez profile](PartDesign_SubtractiveLoft/pl.md)**.
3.  Ustaw opcje, jeśli potrzebujesz i kliknij **OK**.

## Opcje

-   **Powierzchnia prostokreślna**   * tworzy proste przejścia między przekrojami poprzecznymi. Nie ma zastosowania dla wyciągnięcia z dwoma przekrojami. Jeśli opcja nie jest zaznaczona, przejścia będą gładkie.
-   **Zamknięty**   * powoduje przejście z ostatniego przekroju do pierwszego, tworząc pętlę.

## Właściwości

-    **Etykieta**   * name given to the operation, this name can be changed at convenience.

-    **Sekcja**   * lista używanych profili.

-    **Prostokreślny**   * patrz [Opcje](#Opcje.md).

-    **Zamknięty**   * Patrz [Opcje](#Opcje.md).

-    **Płaszczyzna środkowa**   * nie dotyczy.

-    **Odwrócony**   * nie dotyczy.

-    **Udoskonal**   * przyjmuje wartość {{true/pl}} lub {{false/pl}}. Jeśli ustawiono na true, oczyszcza bryłę z resztek krawędzi pozostawionych przez elementy. Sprawdź stronę [Część   * Udoskonal kształt](Part_RefineShape/pl.md) aby uzyskać więcej szczegółów.

## Uwagi

-   Aby lepiej kontrolować kształt wyciągnięcia, zaleca się, aby wszystkie przekroje miały taką samą liczbę segmentów. Na przykład, dla wyciągnięcia pomiędzy prostokątem a okręgiem, okrąg powinien być podzielony na 4 połączone łuki.
-   Można wykonać rzutowanie z lub w kierunku pojedynczego [wierzchołka](Glossary/pl#V.md) ze szkicu lub bryły. {{Version/pl|0.20}}
-   [Wierzchołek](Glossary/pl#V.md) może w większości przypadków być tylko początkiem lub końcem poddasza.
-   Profil nie może leżeć na tej samej płaszczyźnie, co profil bezpośrednio go poprzedzający.
-   Jeśli szkic ma geometrię wewnętrzną, tzn. wyciągnięcie ma mieć otwory, to kolejność tworzenia geometrii szkicu powinna być taka sama dla wszystkich przekrojów   * Albo rozpocznij wszystkie sekcje od geometrii wewnętrznej, albo rozpocznij je wszystkie od zewnętrznej. W przeciwnym razie może powstać niepoprawne wyciągnięcie, w którym przecinają się ściany wewnętrzne i zewnętrzne.
-   Nie można wykonywać wyciągnięcia dla pętli rozłącznych lub krzyżujących się.

## Odnośniki internetowe 

-   Artykuł [Szczegóły techniczne wyciągnięcia przez profile](Part_Loft_Technical_Details/pl.md) wyjaśnia jak [Część   * Odejmowanie wyciągnięciem przez profile](Part_Loft/pl.md) jest tworzone, duża część jego zawartości jest odpowiednia dla omawianej funkcji.





{{PartDesign Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign SubtractiveLoft/pl
