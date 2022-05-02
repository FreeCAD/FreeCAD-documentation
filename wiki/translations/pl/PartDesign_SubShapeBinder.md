---
- GuiCommand:/pl
   Name:PartDesign SubShapeBinder
   Name/pl:Projekt Części: Łącznik kształtów podrzędnych
   Workbenches:[Projekt Części](PartDesign_Workbench/pl.md)
   MenuLocation:Projekt Części → Utwórz łącznik kształtu obiektu podrzędnego
   Version:0.19
   SeeAlso:[Łącznik kształtu](PartDesign_ShapeBinder/pl.md), [Utwórz klon](PartDesign_Clone/pl.md)
---

# PartDesign SubShapeBinder/pl

## Opis

Narzędzie **Łącznik kształtów podrzędnych** tworzy spoiwo kształtu odwołujące się do geometrii z jednego lub więcej obiektów nadrzędnych. Narzędzie Łącznik kształtów podrzędnych jest zazwyczaj używane wewnątrz [zawartości](PartDesign_Body/pl.md) do odwoływania się do geometrii spoza Zawartości. Używanie zewnętrznej geometrii bezpośrednio w bryle jest niedozwolone i prowadzi do błędów wykraczających poza zakres. Jednak Łącznik kształtów podrzędnych może być również używany bez zagnieżdżania w Zawartości.

Łącznik kształtów podrzędnych śledzi względne rozmieszczenie geometrii, do której się odwołuje, co jest przydatne w kontekście tworzenia [złożeń](Assembly/pl.md), ale oprócz tego ma również własne umiejscowienie.

Geometria odniesienia może składać się z jednego lub wielu elementów. Każdy element może być pojedynczym obiektem *(na przykład [Zawartością](PartDesign_Body/pl.md))*, obiektem podrzędnym *(na przykład [prostopadłościanem](Part_Box/pl.md) wewnątrz obiektu [Części](Std_Part/pl.md) lub [szkicem](PartDesign_NewSketch/pl.md) lub [cechą](PartDesign_Feature/pl.md) wewnątrz bryły)* lub elementem podrzędnym *(ściana, krawędź lub wierzchołek)*. To, jaką geometrię należy wybrać, zależy od przeznaczenia Łącznika kształtów podrzędnych. W przypadku operacji typu logicznego należy wybrać bryłę. W przypadku operacji [wyciągnięcia](PartDesign_Pad/pl.md) można użyć ściany, szkicu lub polilinii planarnej. W przypadku [geometrii zewnętrznej](Sketcher_External/pl.md) w szkicu lub w celu dołączenia szkicu można użyć dowolnej kombinacji elementów podrzędnych. Elementy mogą należeć do różnych obiektów nadrzędnych, a nawet mogą należeć do bryły, w której zagnieżdżony jest Łącznik kształtów podrzędnych. Ponieważ Łącznik kształtów podrzędnych jest obiektem [bazującym na łączu](Std_LinkMake/pl.md), geometria, do której się odwołuje, może również należeć do zewnętrznego dokumentu.

<img alt="" src=images/PartDesign_SubShapeBinder_example_1.png  style="width:" height="300px;"> <img alt="" src=images/PartDesign_SubShapeBinder_example_2.png  style="width:" height="300px;"> 
*Z lewej strony dwie bryły utworzone w dwóch oddzielnych [Zawartościach](PartDesign_Body/pl.md).<br>
Z prawej strony dwie bryły Łącznika kształtów podrzędnych odwołujące się do geometrii z pierwszej bryły, zagnieżdżone w drugiej bryle i przesunięte w inne położenie.*

<img alt="" src=images/PartDesign_SubShapeBinder_example_3.png  style="width:" height="300px;"> 
*Dwa obiekty Łącznik kształtu podrzędnego są używane do utworzenia obiektu [przecięcia logicznego](PartDesign_Boolean/pl.md) i [wyciągnięcia](PartDesign_Pad/pl.md) w drugim korpusie.*

## Użycie

### W tym samym dokumencie 

1.  Jeśli w dokumencie jest wiele brył: opcjonalnie [aktywuj bryłę](PartDesign_Body/pl#Pojedyncza_ci.C4.85g.C5.82a_bry.C5.82a.md), w której ma być zagnieżdżony Łącznik kształtów podrzędnych.
2.  Wybierz wymaganą geometrię. Elementy podrzędne można wybierać tylko w oknie [widoku 3D](3D_view/pl.md).
3.  Narzędzie można wywołać na kilka sposobów:
    -   Naciśnij przycisk **<img src="images/PartDesign_SubShapeBinder.svg" width=16px> [Łącznik kształtów podrzędnych](PartDesign_SubShapeBinder/pl.md)**.

\#\* Wybierz z menu opcję **Projekt Części → <img src="images/PartDesign_SubShapeBinder.svg" width=16px> Utwórz łącznik kształtu obiektu podrzędnego**.

1.  Zostanie utworzony Łącznik kształtów podrzędnych.
2.  Jeśli w dokumencie jest tylko jeden obiekt Zawartość, obiekt Łącznik kształtów podrzędnych jest do niego automatycznie dodawany, a Zawartość zostaje automatycznie aktywowana. Jeśli tak jest, a Łącznik kształtów podrzędnych nie powinien być zagnieżdżony, można go przeciągnąć z Zawartości i upuścić na węzeł dokumentu <img alt="" src=images/Document.svg  style="width:16px;"> w oknie [widoku drzewa](Tree_view/pl.md).

### W dokumencie zewnętrznym 

1.  W razie potrzeby otwórz dokument źródłowy *(dokument zewnętrzny)* i dokument docelowy. Oba dokumenty muszą być zapisane co najmniej raz.
2.  Jeśli w dokumencie docelowym jest wiele brył: opcjonalnie aktywuj bryłę, w której ma być zagnieżdżony Łącznik kształtów podrzędnych.
3.  Wybierz żądaną geometrię w dokumencie źródłowym. Elementy podrzędne można wybrać tylko w oknie [widoku 3D](3D_view/pl.md).
4.  Przełącz się do dokumentu docelowego, klikając jego kartę w [Głównym obszarze widoku](Main_view_area/pl.md).
5.  Wywołaj narzędzie w sposób opisany powyżej.

### Zacznij od pustego Łącznika kształtów podrzędnych 

1.  Wykonaj instrukcje opisane w sekcji [W tym samym dokumencie](#W_tym_samym_dokumencie.md) powyżej, ale bez wybierania geometrii.
2.  Zostanie utworzony pusty Łącznik kształtów podrzędnych.
3.  Wybierz wymaganą geometrię. Elementy podrzędne można wybierać tylko w oknie [widoku 3D](3D_view/pl.md).
4.  W oknie [widoku drzewa](Tree_view/pl.md) przeciągnij i upuść zaznaczenie do segregatora Łącznika kształtów podrzędnych. Jeśli zaznaczyłeś elementy podrzędne, ich obiekty nadrzędne są podświetlone w oknie [widoku drzewa](Tree_view/pl.md), wskazując obiekty, które należy przeciągnąć.
5.  Opcjonalnie dodaj więcej geometrii w ten sam sposób.
6.  Aby zastąpić już istniejącą geometrię, przytrzymaj klawisz **Ctrl** podczas operacji przeciągania i upuszczania.

## Uwagi

-   Odsunięcie 2D jest obsługiwane dla niektórych typów kształtów, w tym powierzchni płaskich, krawędzi i polilinii. Ponieważ odsunięcie jest trudną operacją dla programu, nie zawsze się udaje. {{Version/pl|0.20}}
-   Łącznik kształtów podrzędnych, który nie jest zagnieżdżony w bryle, może zostać użyty jako [cecha podstawowa](PartDesign_Body/pl#W.C5.82a.C5.9Bciwo.C5.9B.C4.87_podstawowa.md) dla nowej Zawartości.
-   Właściwość **Podparcie** zawiera odnośniki do geometrii, do której się odwołujemy. Domyślnie właściwość ta jest tylko do odczytu, ale można ją zmodyfikować, postępując zgodnie z instrukcjami opisanymi w sekcji [Zacznij od pustego Łącznika kształtów podrzędnych](#Zacznij_od_pustego_.C5.81.C4.85cznika_kszta.C5.82t.C3.B3w_podrz.C4.99dnych.md).
-   Łącznik kształtów podrzędnych utworzony ze szkicu może mieć przeciwny \"kierunek narzędzia\". Na przykład [wyciągnięcie](PartDesign_Pad/pl.md) utworzone ze szkicu może rozciągać się w kierunku +Y, podczas gdy [wyciągnięcie](PartDesign_Pad/pl.md) o tych samych właściwościach utworzone z Łącznika kształtów podrzędnych rozciąga się w kierunku -Y. Przełączenie właściwości **Odwrócony** *(lub pola wyboru)* rozwiąże ten problem.

## Łącznik kształtu obiektu podrzędnego kontra łącznik kształtu 

Narzędzie Łącznik kształtów podrzędnych środowiska pracy Projekt Części i narzędzie [Łącznik kształtu](PartDesign_ShapeBinder/pl.md) są dość podobne. Ich nazwy są nieco mylące, ponieważ oba mogą odwoływać się do całych obiektów i elementów podrzędnych.

Główne różnice to:

-   Edycja obiektu Łącznik kształtu jest łatwiejsza. Dwukrotne kliknięcie na obiekt w oknie [Widok drzewa](Tree_view/pl.md) spowoduje otwarcie panelu zadań.
-   Łącznik kształtu środowiska pracy Projekt Części może odwoływać się do pojedynczego całego obiektu lub elementów podrzędnych należących do pojedynczego obiektu nadrzędnego. Łącznik kształtów podrzędnych środowiska pracy Projekt Części nie ma tych ograniczeń.
-   Tylko obiekty Łącznik kształtów podrzędnych środowiska pracy Projekt Części mogą odwoływać się do geometrii z pliku zewnętrznego.
-   Łącznik kształtów podrzędnych środowiska pracy Projekt Części zawsze śledzi względne umiejscowienie geometrii, do której się odwołuje. Dla Łącznika kształtu to zachowanie jest opcjonalne poprzez jego właściwość **Śledź podparcie**.
-   Tylko narzędzie Łącznik kształtów podrzędnych obsługuje odsunięcie 2D.

## Właściwości

Obiekt Łącznik kształtów podrzędnych środowiska Projekt Części wywodzi się z obiektu [Cecha](Part_Feature/pl.md) i dziedziczy wszystkie jego właściwości. Posiada również następujące dodatkowe właściwości:

### Dane


{{TitleProperty|Podstawowe}}

-    **Support|XLinkSubList**: podparcie geometrii.

-    **Fuse|Bool**: jeśli parametr ma wartość {{TRUE/pl}}, to łączone kształty brył zostaną scalone.

-    **Make Face|Bool**: jeśli parametr ma wartość {{TRUE/pl}}, to zostanie utworzona powierzchnia dla połączonych linii.

-    **Claim Children|PropertyBool**: jeśli parametr ten ma wartość {{TRUE/pl}}, spowoduje, że połączone obiekty będą traktowane jako elementy podrzędne w oknie [widoku drzewa](Tree_view/pl.md).

-    **Relative|Bool**: jeśli parametr będzie miał wartość {{TRUE/pl}}, to włączy względne łączenie elementów podrzędnych.

-    **Bind Mode|Enumeration**: tryb wiązania, {{value|Synchronized}}, {{Value|Frozen}}, {{Value|Detached}}.

-    **Partial Load|Bool**: jeśli parametr przyjmie wartość {{TRUE/pl}}, umożliwi to częściowe ładowanie obiektów.

-    **Context|XLink|hidden**: obiekt kontenerowy tego obiektu wiążącego.

-    **Bind Copy On Change|Enumeration**
    

-    **Refine|Bool**: jeśli parametr przyjmie wartość {{TRUE/pl}}, to nadmiarowe krawędzie zostaną usunięte *(na przykład po operacji logicznej)*. {{Version/pl|0.20}}

-    **_ Version|Integer|hidden**: wersja obiektu tego typu.

-    **_ Copied Link|XLinkSub|hidden**
    


{{TitleProperty|Cache}}

-    **Body|Matrix|ukryte**: macierz jednorodności tego obiektu.


{{TitleProperty|Wyrównanie}}

-    **Offset**: Odsunięcie 2D, które ma być zastosowane. Jeśli wartość odsunięcia = 0, nie zostanie zastosowane żadne odsunięcie. Jeśli wartość odsunięcia \< 0, wówczas odsunięcie jest stosowane do wewnątrz. {{Version/pl|0.20}}

-    **Offset Join Type**: Metoda dołączania dotycząca odsunięcia połączeń niestycznych. Metodą może być {{Value|Arcs}}, {{Value|Tangent}} lub {{Value|Intersection}}. {{Version/pl|0.20}}

-    **Offset Fill|Bool**: Jeśli parametr ten zostanie ustawiony na wartość `True`, pomiędzy nową i oryginalną linią zostanie utworzona ściana. Zobacz także właściwość **Make Face**. {{Version/pl|0.20}}

-    **Offset Open Result|Bool**: Wpływa na sposób przetwarzania otwartych polilinii. Jeśli parametr zostanie ustawiony na wartość `False`, zostanie utworzona otwarta polilinia. Jeśli {{TRUE/pl}}, powstanie zamknięta polilinia z dwustronnego odsunięcia, z zaokrągleniami wokół otwartych wierzchołków. {{Version/pl|0.20}}

-    **Offset Intersection|Bool**: Wpływa na sposób przetwarzania złożeń. Jeśli parametr ten zostanie ustawiony na wartość {{FALSE/pl}}, wszystkie elementy potomne są przetwarzane niezależnie. Jeśli {{TRUE/pl}}, a elementami potomnymi są krawędzie i polilinie, są one odsuwane w sposób zbiorczy. {{Version/pl|0.20}}

## Odnośniki internetowe 

-   [Nowa funkcja łącza kształtu podrzędnego](https://forum.freecadweb.org/viewtopic.php?t=41450), wyjaśnienie użycia z filmem.





{{PartDesign_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign SubShapeBinder/pl
