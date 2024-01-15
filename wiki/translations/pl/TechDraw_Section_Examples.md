# TechDraw Section Examples/pl
## Wprowadzenie

Środowisko pracy <img alt="" src=images/Workbench_TechDraw.svg  style="width:24px;"> [Rysunek Techniczny](TechDraw_Workbench/pl.md) poczyniło duży krok naprzód w kwestii generowania **widoków przekrojów**. Aby nie przeciążać stron referencyjnych, intencją tej strony jest podanie przykładów i dostarczenie właściwego nazewnictwa dla wykonywanych zadań.

Robię, co mogę, aby znaleźć poprawne terminy, ale ponieważ nie jestem anglistą, to twoja kolej, aby naprawić moje błędy, jeśli je znajdziesz.



## Przekroje

Przekroje służą do zaglądania do wnętrza obiektu, aby pokazać szczegóły, które w innym przypadku są niewidoczne lub trudne do rozpoznania. Zazwyczaj na rysunku znajdują się widoki pokazujące obiekt z co najmniej dwóch kierunków. Jeśli jest podany przekrój, jego położenie i orientacja są wskazane linią przekroju w jednym z widoków.

W programie FreeCAD nie jest możliwe bezpośrednie rysowanie linii przekroju, FreeCAD opiera się na [panelu zadań](Task_panel/pl.md) *(zobacz [Widok przekroju](TechDraw_SectionView/pl#Użycie.md) i [Przekrój złożony](TechDraw_ComplexSection/pl#Użycie.md))*.



## Przykładowe obiekty 

Ten obiekt nie ma żadnego zastosowania poza opisem różnych reprezentacji sekcji.

<img alt="" src=images/TechDraw_ExampleSection-01.png  style="width:400px;"> 
*Trzy widoki i obraz przestrzenny obiektu*



## Przekrój podstawowy 

Narzędzie <img alt="" src=images/TechDraw_SectionView.svg  style="width:24px;"> [Widok przekroju](TechDraw_SectionView/pl.md) tworzy prosty przekrój, który wykorzystuje pojedynczą płaszczyznę do przecięcia obiektu.

Narzędzie wymaga widoku bazowego (właściwość **Widok bazowy**) do pozycjonowania płaszczyzny przekroju. Oś pionowa płaszczyzny przekroju jest zawsze normalną widoku podstawowego, a oś pozioma płaszczyzny przekroju jest równoległa do linii przekroju. Zazwyczaj widok przekroju jest zorientowany tak, że jego oś pozioma jest również równoległa do linii przekroju. Kąt pomiędzy linią przekroju a osią poziomą widoku podstawowego jest kontrolowany przez widżety w obszarze **Ustaw kierunek widoku** panelu zadań narzędzia:

<img alt="" src=images/TechDraw_ComplexSection_Taskview2.png  style="width:200px;">

Pole **Wyświetl kierunek jako kąt** pozwala na ustawienie dowolnego kąta. Do ustawienia predefiniowanych kątów można użyć czterech przycisków:

<img alt="" src=images/Section-up.svg  style="width:32px;"> 90° 
*(w górę)*, <img alt="" src=images/Section-down.svg  style="width:32px;"> 270° *(w dół)*, <img alt="" src=images/Section-left.svg  style="width:32px;"> 180° *(w lewo)*, <img alt="" src=images/Section-right.svg  style="width:32px;"> 0° *(w prawo)*



### Przekrój poziomy 

Przekrój A-A *(widok od dołu w górę)*

<img alt="" src=images/TechDraw_ExampleSection-02.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/TechDraw_ExampleSection-03.png  style="width:200px;"> 
*Widok podstawowy + <img src="images/Section-up.svg" width=24px> → Widok podstawowy i przekroju A-A w swojej domyślnej pozycji*

<img alt="" src=images/TechDraw_ExampleSection-04.png  style="width:200px;"> 
*Widok podstawowy i przekroju A-A we właściwym położeniu.*

Przekrój B-B *(widok od góry w dół)*

<img alt="" src=images/TechDraw_ExampleSection-02.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/TechDraw_ExampleSection-05.png  style="width:200px;"> 
*Widok podstawowy + <img src="images/Section-down.svg" width=24px> → Widok podstawowy i przekroju B-B w swojej domyślnej pozycji*

<img alt="" src=images/TechDraw_ExampleSection-06.png  style="width:200px;"> 
*Widok podstawowy i przekroju B-B we właściwym położeniu*



### Przekrój pionowy 

Przekrój C-C *(widok od prawej w lewo)*

<img alt="" src=images/TechDraw_ExampleSection-02.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/TechDraw_ExampleSection-07.png  style="width:200px;"> 
*Widok podstawowy + <img src="images/Section-left.svg" width=24px> → Widok podstawowy i przekroju C-C w swojej domyślnej pozycji*

<img alt="" src=images/TechDraw_ExampleSection-08.png  style="width:300px;"> 
*Widok podstawowy i przekroju C-C we właściwym położeniu*

Przekrój D-D *(widok od lewej w prawo)*

<img alt="" src=images/TechDraw_ExampleSection-02.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/TechDraw_ExampleSection-09.png  style="width:200px;"> 
*Widok podstawowy + <img src="images/Section-right.svg" width=24px> → Widok podstawowy i przekroju D-D w swojej domyślnej pozycji*

<img alt="" src=images/TechDraw_ExampleSection-10.png  style="width:300px;"> 
*Widok podstawowy i przekroju D-D we właściwym położeniu*



### Przekrój dowolny 

Przekrój E-E *(widok przekroju pod dowolnym kątem)*

<img alt="" src=images/TechDraw_ExampleSection-02.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/TechDraw_ExampleSection-11.png  style="width:200px;"> 
*Widok z podstawy + wartość "Wyświetl kierunek jako kąt" ustawiona na {{Value|30°* → widok podstawowy i przekrój E-E w pozycji domyślnej}}

<img alt="" src=images/TechDraw_ExampleSection-12.png  style="width:300px;"> 
*Widok podstawowy i przekroju E-e we właściwym położeniu*

Domyślnie płaszczyzna przekroju przechodzi przez środek ramki ograniczającej widoku *(w tym przypadku pokrywający się ze środkiem ciężkości obiektu)*. Aby uzyskać przekrój przesunięty musimy zmienić wartości w obszarze **Lokalizacja płaszczyzny przekroju**.

<img alt="" src=images/TechDraw_ExampleSection-16.png  style="width:300px;">

<img alt="" src=images/TechDraw_ExampleSection-17.png  style="width:300px;"> 
*Tutaj linia przekroju została przesunięta o 22 mm w kierunku X i 14 mm w kierunku Y ''(bez dowodu, że linia przechodzi przez środki otworów)''. Automatycznie generowana wartość Z nie ma w tym przypadku żadnego znaczenia.*



### Widok pomocniczy 

W programie FreeCAD brakuje narzędzia do wyprowadzania widoków pomocniczych z widoku podstawowego, ale funkcja <img alt="" src=images/TechDraw_SectionView.svg  style="width:24px;"> [Widok przekroju](TechDraw_SectionView/pl.md) również sobie z tym poradzi:

Używając przekroju E-E z góry i zmieniając wymienione wartości na X = {{Value|40 mm}} i Y = {{Value|-23 mm}} przekrój nie przecina już obiektu i staje się zamiast tego widokiem pomocniczym. Uwaga: zachowaj ostrożność podczas zmiany wartości, duże kroki mogą spowodować awarię programu FreeCAD!

<img alt="" src=images/TechDraw_ExampleSection-12.png  style="width:300px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/TechDraw_ExampleSection-18.png  style="width:300px;"> 
*Przekrój E-E jak w powyższym przykładzie + przesunięta linia / płaszczyzna przekroju → Widok E*

Etykieta została wyedytowana. Linia przekroju i jedna strzałka muszą być ukryte w kolejnych krokach, ponieważ pojedyncza strzałka wystarczy, aby prawidłowo zdefiniować widok pomocniczy.



### Uwagi

-   Zastosowane wersje:
    -   Przykłady zostały utworzone przy użyciu wydania weekly build 0.21 - 31155 z wybranym pierwszym kątem i ISO.
    -   C-C, D-D, i E-E: domyślne Pozycje zostały zaktualizowane, aby wyświetlić aktualne domyślne rozmieszczenie *(weekly build 0.21 - 31709) (aktualizacja 2023-02-03)*.
-   Przy tej okazji zdałem sobie sprawę, że poziome i pionowe linie środkowe są zorientowane według strony, ale nie widoku i dlatego nie można ich użyć do wyrównania widoku podstawowego i widoku przekroju, czego bym oczekiwał.
-   Zastosowanie przesunięcia do linii / płaszczyzny przekroju jest nieco skomplikowane, ponieważ można je przesuwać tylko wzdłuż osi globalnych, a nie według *(lokalnych)* osi widoku.



## Przekroje podstawowe w praktyce 



### Przekrój pojedynczy 

Jeżeli na rysunku jest tylko jeden widok przekroju i widać wyraźnie, że obiekt jest przecięty wzdłuż linii środkowej, można pominąć linię przekroju, w tym strzałki, oraz tytuł widoku.

<img alt="" src=images/TechDraw_ExampleSection-13.png  style="width:300px;"> <img alt="" src=images/TechDraw_ExampleSection-14.png  style="width:300px;"> 
*Oba rysunki są zgodne z normą*



### Przekrój wewnętrzny 

Widok przekroju może być zintegrowany z widokiem podstawowym. W tym przypadku również nie są wymagane strzałki i tytuł.

<img alt="" src=images/TechDraw_ExampleSection-15.png  style="width:200px;">



## Przekrój złożony 

Narzędzie <img alt="" src=images/TechDraw_ComplexSection.svg  style="width:24px;"> [Wstaw przekrój złożony](TechDraw_ComplexSection/pl.md) tworzy złożony przekrój, taki jak przekrój wyrównany lub przesunięty, który używa więcej niż jednej płaszczyzny do przecięcia obiektu.

Narzędzie wymaga widoku bazowego *(właściwość **Widok podstawowy**)*, aby umieścić kilka połączonych płaszczyzn przekroju do przecięcia obiektu, są one zdefiniowane przez polilinię 3D. *(To narzędzie może również obsługiwać krzywe, ale zakrzywione przekroje są raczej nietypowe)*.

Osie pionowe płaszczyzn przekroju są zawsze równoległe do normalnej widoku podstawowego. Ich osie poziome pochodzą od powiązanych segmentów polilinii 3D. Orientacja widoku Przekrój zależy od jednego z segmentów polilinii 3D, a wpływ na nią mają widżety znajdujące się w obszarze opcji **Ustaw kierunek widoku** panelu zadań narzędzia:

<img alt="" src=images/TechDraw_ComplexSection_Taskview1.png  style="width:" height="250px;"> <img alt="" src=images/TechDraw_ComplexSection_Taskview2.png  style="width:" height="250px;">

To narzędzie udostępnia 3 opcje w polu **Technika rzutowania** do obsługi segmentów linii przekroju:

-    {{Value|Odsunięcie}}: wyświetlane są tylko odcinki prostopadłe do kierunku widoku (domyślnie).

-    {{Value|Wyrównane}}: wszystkie odcinki są wyświetlane w rzeczywistej długości.

-    {{Value|Nie równolegle}}: wszystkie odcinki są wyświetlane wzdłuż tego samego kierunku patrzenia. W zależności od kąta pomiędzy segmentem a kierunkiem patrzenia, rzut może być krótszy niż obszar cięcia. Odcinki równoległe do kierunku patrzenia tworzą pojedynczą linię.



### Odsunięcie przekroju 

Część odsunięta zaczyna się od widoku bazowego plus polilinia 3D, zobaczmy <img alt="" src=images/PartDesign_NewSketch.svg  style="width:16px;"> [szkic](PartDesign_NewSketch/pl.md) tego przypadku.

<img alt="" src=images/TechDraw_ExampleSection-02.png  style="width:200px;"> <img alt="" src=images/Arch_Add.svg  style="width:16px;"> <img alt="" src=images/TechDraw_ExampleSection-19.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/TechDraw_ExampleSection-20.png  style="width:200px;"> 
*Widok podstawowy + szkic + "Technika rzutowania" ustawiona na {{Value|Odsunięcie* + "Wyświetl kierunek jako kąt" ustawione na {{Value|30°}} → Widok podstawowy i przekrój G-G w pozycji domyślnej}}

Kąt kierunku widoku musi być ustawiony na odpowiednią wartość, aby uniknąć nieoczekiwanych rezultatów.

<img alt="" src=images/TechDraw_ExampleSection-21.png  style="width:300px;"> 
*Widok podstawy i przekrój G-G we właściwym położeniu*



### Wyrównanie przekroju 

Wyrównanie przekroju również rozpoczyna się od widoku podstawowego i polilinii 3D.

<img alt="" src=images/TechDraw_ExampleSection-02.png  style="width:200px;"> <img alt="" src=images/Arch_Add.svg  style="width:16px;"> <img alt="" src=images/TechDraw_ExampleSection-22.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/TechDraw_ExampleSection-23.png  style="width:200px;"> 
*Widok podstawowy + szkic + "Technika rzutowania" ustawiona na {{Value|Wyrównanie* + <img src="images/Section-right.svg" width=24px> ''(lub "Wyświetl kierunek jako kąt" ustawione na {{Value|30°}})'' → Widok podstawowy i przekrój H-H w pozycji domyślnej}}

Kąt kierunku widoku można ustawić za pomocą <img alt="" src=images/Section-right.svg  style="width:24px;"> i <img alt="" src=images/Section-left.svg  style="width:24px;"> dla orientacji przybliżonej. Należy go odgadnąć i ustawić na najlepiej pasującą wartość albo wynik może być nieoczekiwany.

<img alt="" src=images/TechDraw_ExampleSection-24.png  style="width:300px;"> 
*Widok podstawy i przekrój H-H, jeśli parametr "Wyświetl kierunek jako kąt" jest ustawiony na wartość {{Value|30°*. (równolegle do dolnego odcinka linii przekroju). Odcinek został przesunięty do właściwej pozycji}}

Jeśli kąt kierunku widoku jest ustawiony nieprawidłowo, wynik może wyglądać następująco:

<img alt="" src=images/TechDraw_ExampleSection-25.png  style="width:200px;"> 
*Strzałki po obu stronach linii przekroju powodują dziwny rzut, parametr "Wyświetl kierunek jako kąt" jest ustawiony na wartość {{Value|90°*}}



### Widok pomocniczy 

Narzędzie <img alt="" src=images/TechDraw_ComplexSection.svg  style="width:24px;"> [Wstaw przekrój złożony](TechDraw_ComplexSection/pl.md) może, podobnie jak <img alt="" src=images/TechDraw_SectionView.svg  style="width:24px;"> [Wstaw widok przekroju](TechDraw_SectionView/pl.md), tworzyć widoki pomocnicze z widoków bazowych:

Widok pomocniczy rozpoczyna się od widoku podstawowego i pojedynczej linii 3D umieszczonej na zewnątrz obiektu.

<img alt="" src=images/TechDraw_ExampleSection-02.png  style="width:200px;"> <img alt="" src=images/Arch_Add.svg  style="width:16px;"> <img alt="" src=images/TechDraw_ExampleSection-26.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/TechDraw_ExampleSection-27.png  style="width:300px;"> 
*Widok podstawowy + linia w 3D → Widok I*

Wartość **Wyświetl kierunek jako kąt** musi być ręcznie wyodrębniona z linii 3D. Etykieta została wyedytowana. Linia przekroju i jedna strzałka muszą zostać ukryte w kolejnych krokach, ponieważ pojedyncza strzałka wystarczy, aby prawidłowo zdefiniować widok pomocniczy.



### Przekrój nie równoległy 

Przekrój nie równoległy jest mieszanką przekrojów wyrównanych i przesuniętych.

<img alt="" src=images/TechDraw_ExampleSection-02.png  style="width:200px;"> <img alt="" src=images/Arch_Add.svg  style="width:16px;"> <img alt="" src=images/TechDraw_ExampleSection-30.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/TechDraw_ExampleSection-31.png  style="width:250px;"> 
*Widok podstawowy + szkic → Widok podstawowy i przekrój K-K obrócony o -85° i przesunięty*

Kierunek strzałki powinien być poziomy, ale narzędzie nie działało, gdy wartość **Wyświetl kierunek jako kąt** była ustawiona na {{Value|0°}}. Tak więc szkic został obrócony o 5° i wartość wspomnianego kąta również została ustawiona na wartość {{Value|5°}}.



### Porównanie przekroju nie równoległego z odsunięciem i wyrównaniem 

<img alt="" src=images/TechDraw_ExampleSection-32.png  style="width:400px;"> 
*Widok podstawowy i przekrój K-K w 3 wersjach: "Odsunięcie": niebieskie zakreskowanie, "Nie równoległy": czarne zakreskowanie, "Wyrównany": czerwone zakreskowanie*

Z jakiegoś powodu, jeśli wartość **Wyświetl kierunek jako kąt** wyrównanego przekroju jest ustawiona dokładnie na {{Value|5°}}, wynik jest błędny. Dopiero po edycji przekroju i zaakceptowaniu dziwnej wartości {{Value|5.14°}}, na którą w jakiś sposób ustawiony jest kąt, wyświetlany jest prawidłowy wynik.

<img alt="" src=images/TechDraw_ExampleSection-33.png  style="width:400px;"> 
*Tak jak powyżej z parametrem "Wyświetl kierunek jako kąt" ustawionym dokładnie na wartość {{Value|5°*: kierunek widoku drugiego segmentu od góry jest odwrócony ''(widoczny jest wał)''}}



### Przekrój złożony w jednej linii 

Długość *(szerokość)* złożonego przekroju zależy od długości użytej linii w widoku 3D, ale wyniki różnią się od przekroju Odsuniętego do przekroju Nie równoległego:

<img alt="" src=images/TechDraw_ExampleSection-34.png  style="width:400px;"> <img alt="" src=images/TechDraw_ExampleSection-35.png  style="width:400px;"> 
*Dwa przekroje oparte na tej samej linii w widoku 3D.<br>
Po lewej: Przekrój Odsunięty pokazuje segment między strzałkami jako przekrój, podczas gdy reszta obiektu pozostaje nieprzycięta.<br>
Po prawej: Przekrój Nie równoległy pokazuje tylko przekrój między strzałkami i pomija resztę obiektu.*



## Przekroje złożone w praktyce 



### Pół przekrój 

Widok pokazujący symetryczny obiekt przecięty po jednej stronie linii środkowej i nieprzecięty po drugiej. Głębokość jest zwykle określona przez inną linię środkową.

<img alt="" src=images/TechDraw_ExampleSection-28.png  style="width:200px;"> <img alt="" src=images/TechDraw_ExampleSection-29.png  style="width:200px;"> <img alt="" src=images/TechDraw_ExampleSection-36.png  style="width:170px;"> 
*Z lewej i pośrodku: Widok odsunięcia przekroju z i bez strzałek, linii przekroju i tytułu, oba są zgodne ze standardem.<br>
Po prawej: Widok odsunięcia przekroju oparty na alternatywnej linii przekroju, patrz przekrój M-M powyżej.*



### Uwagi 

-   Użyte wersje:
    -   Przykłady zostały stworzone przy użyciu weekly build 0.21 - 31155 z wybranym pierwszym kątem i ISO.
    -   Weekly build 0.21 - 31340 dla M-M.
-   Kierunek widoku *(orientacja strzałek)* musi być określony indywidualnie.
-   Wszystkie przekroje złożone muszą być obracane samodzielnie.
-   Wartość **Wyświetl kierunek jako kąt** równa dokładnie {{Value|0°}} nie działa dla odcinków przesuniętych *(180° też?)*.
-   Wartość **Wyświetl kierunek jako kąt** zostanie zresetowana do dziwnej wartości, gdy widok sekcji zostanie aktywowany do edycji.



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw Section Examples/pl
