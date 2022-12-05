---
- GuiCommand:/pl
   Name:PartDesign AdditiveLoft
   Name/pl:Projekt Części: Uzupełnianie wyciągnięciem przez profile
   MenuLocation:Projekt Części → Utwórz cechę przez dodanie → Uzupełnianie wyciągnięciem przez profile
   Workbenches:[Projekt Części](PartDesign_Workbench/pl.md)
   Version:0.17
   SeeAlso:[Uzupełnianie wyciągnięciem po ścieżce](PartDesign_AdditivePipe/pl.md), [Odejmowanie wyciągnięciem przez profile](PartDesign_SubtractiveLoft/pl.md)
---

# PartDesign AdditiveLoft/pl

## Opis

**Uzupełnianie wyciągnięciem przez profile** tworzy bryłę w aktywnej Zawartości poprzez wykonanie przejścia pomiędzy dwoma lub więcej szkicami *(zwanymi również przekrojami poprzecznymi)*. Jeżeli Zawartość zawiera już elementy, to wyciągnięcie zostanie z nimi połączone.

![](images/PartDesign_AddLoft_example.png ) 
*Po lewej: przekroje ''(A)'', ''(B)'' i ''(C)''
Po prawej: utworzone wyciągnięcie.*

## Użycie

### Przepływ pracy na podstawie okienka dialogowego 

1.  Naciśnij przycisk **[<img src=images/PartDesign_AdditiveLoft.svg style="width:24px"> [Uzupełnianie wyciągnięciem przez profile](PartDesign_AdditiveLoft/pl.md)**.
2.  W oknie dialogowym **Wybierz cechę** wybierz szkic, który ma być użyty jako obiekt profilu bazowego i kliknij **OK**.
    -   Alternatywnie, przed naciśnięciem przycisku Uzupełnianie wyciągnięciem przez profile można wybrać pojedynczy szkic lub ścianę obiektu 3D *({{Version/pl|0.20}})*.
3.  W **Parametrach wyciągnięcia przez profile** naciśnij przycisk **Dodaj sekcję profilu**
4.  Wybierz następny szkic w oknie [widoku 3D](3D_view/pl.md). Powtórz powyższe czynności, aby wybrać więcej szkiców w kolejności, w jakiej chcesz, aby były poddawane wyciągnięciu. *(Możesz zmienić kolejność sekcji w dowolnym momencie później w oknie dialogowym wyciągnięcia, przeciągając sekcje na liście do pożądanej pozycji.{{Version/pl|0.19}})*.
5.  Ustaw opcje w razie potrzeby i kliknij **OK**.

### Przepływ pracy oparty na wyborze 


{{Version/pl|0.19}}

1.  Wybierz kilka szkiców. Ważne jest, w jakiej kolejności je wybierzesz:
    -   Szkic wybrany jako pierwszy stanie się obiektem profilu bazowego w następnym kroku
    -   Szkice wybrane po pierwszym staną się sekcjami wyciągnięcia. Również tutaj ważna jest kolejność wyboru: szkic wybrany jako drugi stanie się pierwszą sekcją wyciągnięcia, szkic wybrany jako trzeci stanie się drugą sekcją i tak dalej. *(Możesz zmienić kolejność sekcji w dowolnym momencie później w oknie dialogowym wyciągnięcia, przeciągając sekcje na liście na żądaną pozycję.{{Version/pl|0.19}})*
    -   Pierwszy lub ostatni wybór może być również ścianą obiektu 3D *({{Version/pl|0.20}})*
2.  Naciśnij przycisk **[<img src=images/PartDesign_AdditiveLoft.svg style="width:24px"> [Uzupełnianie wyciągnięciem przez profile ](PartDesign_AdditiveLoft/pl.md)**.
3.  Ustaw opcje, jeśli to konieczne i kliknij **OK**.

## Opcje

-   **Powierzchnia prostokreślna**: tworzy proste przejścia między przekrojami poprzecznymi. Nie ma zastosowania dla wyciągnięcia z dwoma przekrojami. Jeśli opcja nie jest zaznaczona, przejścia będą gładkie.
-   **Zamknięty**: powoduje przejście z ostatniego przekroju do pierwszego, tworząc pętlę.

## Właściwości

-    **Label**: nazwa nadana operacji, nazwa ta może być zmieniona w dogodnym momencie.

-    **Sections**: zawiera listę użytych sekcji.

-    **Ruled**: zobacz akapit [Opcje](#Opcje.md).

-    **Closed**: zobacz akapit [Opcje](#Opcje.md).

-    **Refine**: przyjmuje wartości {{true/pl}} lub {{false/pl}}. Jeżeli ustawimy na wartość prawda, to funkcja wyczyści bryłę z resztek krawędzi pozostawionych przez cechy. Zobacz [Udoskonal kształt](Part_RefineShape/pl.md) aby uzyskać więcej szczegółów.

-    **Profile**: obiekt profilu bazowego patrz wyciągnięcie.

-    **Midplane**: nie ma zastosowania.

-    **Reversed**: nie ma zastosowania.

-    **Up To Face**: nie ma zastosowania.

-    **Allow Multi Face**: nie ma zastosowania.

## Uwagi

-   Aby lepiej kontrolować kształt wyciągnięcia, zaleca się, aby wszystkie przekroje miały taką samą liczbę segmentów. Na przykład, dla przejścia pomiędzy prostokątem a okręgiem, okrąg powinien być rozbity na cztery połączone łuki.
-   Możesz wykonać wyciągnięcie z lub w kierunku pojedynczego [wierzchołka](Glossary#V.md) ze szkicu lub bryły. {{Version/pl|0.20}}
-   [Wierzchołki](Glossary#V.md) mogą być tylko początkiem lub końcem wyciągnięcia. W przeciwnym razie bryła poddasza składałaby się z dwóch brył połączonych w jednym punkcie. Naruszałoby to definicję obiektu 3D zawartą w jądrze CAD.
-   Profil nie może znajdować się na tej samej płaszczyźnie co profil bezpośrednio go poprzedzający.
-   Jeśli szkic ma geometrię wewnętrzną, czyli wyciągnięcie ma mieć otwór, to kolejność tworzenia geometrii szkicu, powinna być taka sama dla wszystkich profili: Albo zacznij pracę z wszystkimi profilami geometrii wewnętrznej, albo zewnętrznej. W przeciwnym razie może powstać nieprawidłowe wyciągnięcie, w którym krzyżują się ściany wewnętrzne i zewnętrzne.
-   Nie jest możliwe wyciąganie pętli rozłącznych lub krzyżujących się.
-   Niektóre tryby awarii spowodują, że część będzie wyświetlona w kolorze czarnym.

## Odnośniki internetowe 

-   Artykuł [Szczegóły techniczne wyciągnięcia przez profile](Part_Loft_Technical_Details/pl.md) wyjaśnia jak jest tworzone [Odejmowanie wyciągnięciem przez profile](Part_Loft/pl.md) środowiska Część. Znaczna część jego zawartości dotyczy również funkcji Uzupełnianie wyciągnięciem przez profile.





{{PartDesign Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign AdditiveLoft/pl
