# PartDesign Examples/pl
## Wprowadzenie

Czasami potrzebna jest wskazówka, jak potężne jest dane narzędzie, bez zbyt wielu wyjaśnień.

Jest to zbiór przykładów, które można osiągnąć za pomocą określonych narzędzi. Szczegółowe objaśnienia można znaleźć w opisach narzędzi oraz w Internecie, gdzie można znaleźć odpowiednie poradniki.



## Wyciągnięcie

<img alt="" src=images/PartDesign_Pad.svg  style="width:24px;"> [Wyciągnięcie](PartDesign_Pad/pl.md) to narzędzie do tworzenia obiektów typu wyciągnięcie, które są obiektami o budowie graniastosłupa, takimi jak walce, stożki, sześciany, kliny \...

Każdy obiekt jest oparty na konturze *(żółtym)*, który określa kształt przekroju *(najlepiej wykonać go za pomocą środowiska pracy [Szkicownik](Sketcher_Workbench/pl.md))*.

Kontur jest przeciągany wzdłuż kierunku *(wyciskany)*, aby nadać obiektowi grubość lub długość.
Domyślnie jest to normalny kierunek płaszczyzny zawierającej kontur *(płaszczyzny szkicu)*. Kierunek można opcjonalnie zmienić, edytując parametry w panelu właściwości lub wybierając osobną linię prostą *(białą)*.


<div class="mw-collapsible mw-collapsed">

**Galeria**


<div class="mw-collapsible-content toccolours">



### Bryły pierwotne oparte o kształt wielokąta 

++++
| **Walec**                 | <img alt="Walec" src=images/PartDesign_ExamplePad-01.png  style="width:200px;">                                 | -   Kontur: **okrąg**.                                      |
++++
| **Sześcian**              | <img alt="Sześcian" src=images/PartDesign_ExamplePad-02.png  style="width:200px;">                           | -   Kontur: **kwadrat**.                                    |
|                           |                                                                                             | -   Długość wyciągnięcia: równa długości krawędzi kwadratu. |
++++
| **Prostopadłościan**      | <img alt="Prostopadłościan" src=images/PartDesign_ExamplePad-03.png  style="width:200px;">           | -   Kontur: **prostokąt**.                                  |
++++
| **Graniastosłup foremny** | <img alt="Graniastosłup foremny" src=images/PartDesign_ExamplePad-04.png  style="width:200px;"> | -   Kontur: **sześciokąt**.                                 |
++++
| **Klin**                  | <img alt="Klin" src=images/PartDesign_ExamplePad-05.png  style="width:200px;">                                   | -   Kontur: **trójkąt**.                                    |
++++



### Profile oparte o kształt graniastosłupa 

++++
| **profil L**          | <img alt="L-profile" src=images/PartDesign_ExamplePad-06.png  style="width:200px;">               | -   Kontur: kształt litery **L**.                                                  |
|                       |                                                                                   |                                                                                    |
|                       |                                                                                   | :                                                                                  |
++++
| **profil C**          | <img alt="C-profile" src=images/PartDesign_ExamplePad-07.png  style="width:200px;">               | -   Kontur: kształt litery **C**.                                                  |
++++
| **profil Z**          | <img alt="Z-profile" src=images/PartDesign_ExamplePad-11.png  style="width:200px;">               | -   Kontur: kształt litery **Z**.                                                  |
++++
| **profil T**          | <img alt="T-profile" src=images/PartDesign_ExamplePad-09.png  style="width:200px;">               | -   Kontur: kształt litery **T**.                                                  |
++++
| **profil dwuteownik** | <img alt="Double-T-profile" src=images/PartDesign_ExamplePad-10.png  style="width:200px;"> | -   Kontur: kształt litery **H**, z szerokością kołnierza \< odsunięcia kołnierza. |
++++
| **profil H**          | <img alt="H-profile" src=images/PartDesign_ExamplePad-08.png  style="width:200px;">               | -   Kontur: kształt litery *H*, gdzie szerokość = wysokość.                        |
++++


</div>


</div>



## Wyciągnięcie po ścieżce 

<img alt="" src=images/PartDesign_AdditivePipe.svg  style="width:24px;"> [Wyciągnięcie po ścieżce](PartDesign_AdditivePipe/pl.md) to narzędzie do tworzenia obiektów wyciągnięcia po ścieżce, takich jak obiekty przeciągania, obiekty wytłaczania, obiekty obrotu, cylindry, stożki, sześciany, piramidy, kule \...

Każdy obiekt jest oparty na co najmniej dwóch liniach *(najlepiej wykonanych za pomocą środowiska pracy [Szkicownik](Sketcher_Workbench/pl.md))*:

-   Jeden kontur *(żółty)*, do definiowania kształtu przekroju.
-   Jedna ścieżka *(biała)*, po której można się poruszać.

Nietrudno się zorientować, że niektóre obiekty można tworzyć także za pomocą innych narzędzi, ale czy bez tych przykładów domyśliłbyś się, jak wszechstronne jest to narzędzie?


<div class="mw-collapsible mw-collapsed">

**Galeria**


<div class="mw-collapsible-content toccolours">



### Obiekty koliste 

Proste obiekty utworzone przeciąganiem przez obrót

++++
| **Sfera**         | <img alt="Sfera" src=images/PartDesign_ExampleSphere-01.png  style="width:200px;">                                    | -   Kontur: **łuk o kącie 180°** oraz **linia** łącząca punkty końcowe.                                                                                          |
|                   |                                                                                                   | -   Ścieżka: pełny **okrąg**.                                                                                                                                    |
++++
| **Segment sfery** | <img alt="Segment sfery 240°" src=images/PartDesign_ExampleSphere-02.png  style="width:200px;">          | -   Kontur: **łuk o kącie 180°\'\' i**linia\'\'\' łącząca punkty końcowe.                                                                                        |
|                   |                                                                                                   | -   Ścieżka: **łuk o kącie 240°**.                                                                                                                               |
|                   |                                                                                                   |                                                                                                                                                                  |
|                   |                                                                                                   | :   Funkcja ta może tworzyć odcinki o dowolnym kącie z wyjątkiem dokładnie 180°, ponieważ ma problem z płaszczyzną początkową i końcową będącą współpłaszczyzną. |
++++
| **Połowa sfery**  | <img alt="Połowa sfery" src=images/PartDesign_ExampleSphere-03.png  style="width:200px;">                      | -   Kontur: **łuk o kącie 90°** i dwie prostopadłe **linie** łączące punkty końcowe.                                                                             |
|                   |                                                                                                   | -   Ścieżka: pełny **okrąg**.                                                                                                                                    |
++++
| **Torus**         | <img alt="Torus" src=images/PartDesign_ExampleTorus-01.png  style="width:200px;">                                     | -   Kontur: pełny **okrąg**.                                                                                                                                     |
|                   |                                                                                                   | -   Ścieżka: pełny **okrąg**.                                                                                                                                    |
++++
| **Stożek**        | <img alt="Stożek" src=images/PartDesign_ExampleTorus-04.png  style="width:200px;">                                   | -   Kontur: **trójkąt** z jedną krawędzią leżącą na linii środkowej.                                                                                             |
|                   |                                                                                                   | -   Ścieżka: pełny **okrąg**.                                                                                                                                    |
++++
| **Walec**         | <img alt="Walec" src=images/PartDesign_ExampleTorus-02.png  style="width:200px;">                                     | -   Kontur: **prostokąt** z jedną krawędzią leżącą na linii środkowej.                                                                                           |
|                   |                                                                                                   | -   Ścieżka: pełny **okrąg**.                                                                                                                                    |
++++
| **Rura**          | <img alt="Rura *(wydrążony walec)*" src=images/PartDesign_ExampleTorus-03.png  style="width:200px;"> | -   Kontur: **prostokąt**.                                                                                                                                       |
| wydrążony walec   |                                                                                                   | -   Ścieżka: pełny **okrąg**.                                                                                                                                    |
++++



### Obiekty graniastosłupowe 

Proste obiekty utworzone przeciąganiem

++++
| **Walec**                   | <img alt="Walec" src=images/PartDesign_ExamplePrism-01.png  style="width:200px;">                                           | -   Kontur: **koło**.                                                    |
|                             |                                                                                                         | -   Ścieżka: prosta **linia**.                                           |
++++
| **Sześcian**                | <img alt="Sześcian" src=images/PartDesign_ExamplePrism-02.png  style="width:200px;">                                     | -   Kontur: **kwadrat**.                                                 |
|                             |                                                                                                         | -   Ścieżka: prosta **linia**, tej samej długości co krawędzie kwadratu. |
++++
| **Prostopadłościan**        | <img alt="Prostopadłościan" src=images/PartDesign_ExamplePrism-03.png  style="width:200px;">                     | -   Kontur: **prostokąt**.                                               |
|                             |                                                                                                         | -   Ścieżka: prosta **linia**.                                           |
++++
| **Klin**                    | <img alt="Klin" src=images/PartDesign_ExamplePrism-04.png  style="width:200px;">                                             | -   Kontur: **trójkąt**.                                                 |
|                             |                                                                                                         | -   Ścieżka: prosta **linia**.                                           |
++++
| Regularny **Graniastosłup** | <img alt="Regularny Graniastosłup" src=images/PartDesign_ExamplePrism-05.png  style="width:200px;">       | -   Kontur: regularny **sześciokąt**.                                    |
|                             |                                                                                                         | -   Ścieżka: prosta **linia**.                                           |
++++
| Graniastosłupy gwiaździste  | <img alt="Graniastosłupy gwiaździste" src=images/PartDesign_ExamplePrism-06.png  style="width:200px;"> | -   Kontur: regularny **kształt gwiazdy**.                               |
|                             |                                                                                                         | -   Ścieżka: prosta **linia**.                                           |
++++
| Belka dwuteowa              | <img alt="Belka dwuteowa" src=images/PartDesign_ExamplePrism-07.png  style="width:200px;">                         | -   Kontur: **profil belki**                                             |
|                             |                                                                                                         | -   Ścieżka: prosta **linia**.                                           |
++++



### Obiekty stożkowe 

++++
| **Stożek**            | <img alt="Stożek" src=images/PartDesign_ExampleConic-01.png  style="width:200px;">                               | -   Kontury: Podstawa: pełne **koło**, Góra: **punkt**.            |
|                       |                                                                                               | -   Ścieżka: prosta **linia**.                                     |
|                       |                                                                                               |                                                                    |
|                       |                                                                                               | :   *(Punkt wierzchołka jest punktem końcowym linii pomocniczej)*. |
++++
| **Ostrosłup**         | <img alt="Ostrosłup" src=images/PartDesign_ExampleConic-02.png  style="width:200px;">                         | -   Kontury: Podstawa: **kwadrat**, Góra: **punkt**.               |
|                       |                                                                                               | -   Ścieżka: prosta **linia**                                      |
|                       |                                                                                               |                                                                    |
|                       |                                                                                               | :   *(Punkt wierzchołka jest punktem końcowym linii pomocniczej)*. |
++++
| Ostrosłup przechylony | <img alt="Ostrosłup przechylony" src=images/PartDesign_ExampleConic-03.png  style="width:200px;"> | -   Kontury: Podstawa: **kwadrat**, Góra: **punkt**.               |
|                       |                                                                                               | -   Ścieżka: prosta **linia**.                                     |
|                       |                                                                                               |                                                                    |
|                       |                                                                                               | :   *(Punkt wierzchołka jest punktem końcowym ścieżki)*.           |
++++



### Obiekty zakrzywione 

++++
| **Wąż**                | <img alt="Wąż" src=images/PartDesign_ExampleSweep-01.png  style="width:200px;">                               | -   Kontury: dwa współśrodkowe **okręgi**.                      |
| (Rura)                 |                                                                                         | -   Ścieżka: zakrzywiona **linia**.                             |
++++
| Kwadratowa **rura**    | <img alt="Square Pipe" src=images/PartDesign_ExampleSweep-02.png  style="width:200px;">               | -   Kontury: dwa współśrodkowe **kwadraty**.                    |
|                        |                                                                                         | -   Ścieżka: zakrzywiona **linia**.                             |
++++
| **Polilinia**          | <img alt="Wire" src=images/PartDesign_ExampleSweep-04.png  style="width:200px;">                             | -   Kontur: **okrąg**.                                          |
|                        |                                                                                         | -   Ścieżka: zakrzywiona **linia**.                             |
++++
| Róg                    | <img alt="Róg" src=images/PartDesign_ExampleSweep-03.png  style="width:200px;">                               | -   Kontury: Podstawa: **okrąg**, Góra: *(mniejszy)* **okrąg**. |
|                        |                                                                                         | -   Ścieżka: zakrzywiona **linia**.                             |
++++
| Legendarny             | <img alt="Klucz sześciokątny" src=images/PartDesign_ExampleSweep-05.png  style="width:200px;"> | -   Kontur: *sześciokąt*.                                       |
| **Klucz sześciokątny** |                                                                                         | -   Ścieżka: zakrzywiona **linia**.                             |
++++



### Obiekty spiralne i walcowate 

++++
| Sprężyna spiralna      | <img alt="Sprężyna" src=images/PartDesign_ExampleSpring-01.png  style="width:200px;">                     | -   Kontur: **okrąg**.                                                                                                                |
|                        |                                                                                          | -   Ścieżka: <img alt="" src=images/Part_Helix.svg  style="width:16px;"> [Helisa](Part_Helix/pl.md) środowiska Część.                    |
++++
| Sprężyna włosowa       | <img alt="Sprężyna balansowa" src=images/PartDesign_ExampleSpring-03.png  style="width:200px;"> | -   Kontur: **prostokąt**.                                                                                                            |
| Sprężyna balansowa     |                                                                                          | -   Ścieżka: <img alt="" src=images/Part_Spiral.svg  style="width:16px;"> [Spirala](Part_Spiral.md) środowiska Część.                   |
++++
| **Sprężyna spiralna**, | <img alt="Sprężyna spiralna" src=images/PartDesign_ExampleSpring-04.png  style="width:200px;">   | -   Kontur: **prostokąt**.                                                                                                            |
| Sprężyna stożkowa      |                                                                                          | -   Ścieżka: <img alt="" src=images/Part_Helix.svg  style="width:16px;"> [Helisa](Part_Helix/pl.md) środowiska Część z kątem nachylenia. |
++++



### Obiekty przejściowe 

++++
| Kwadrat w koło           | <img alt="Obiekt przejścia z krzywą" src=images/PartDesign_ExampleTrans-01.png  style="width:200px;"> | -   Kontury: Początkowy: **kwadrat**, Końcowy: **koło**.     |
| za pośrednictwem ścieżki |                                                                                                       | -   Ścieżka: zakrzywiona **linia**.                          |
++++
| Kwadrat w koło           | <img alt="Obiekt przejścia prosty" src=images/PartDesign_ExampleTrans-02.png  style="width:200px;">     | -   Kontury: Początkowy: **kwadrat**, Końcowy: **koło**.     |
| bezpośrednio             |                                                                                                       | -   Ścieżka: prosta **linia**.                               |
++++
| Wielokąt w gwiazdę       | <img alt="Wielokąt do gwiazdy" src=images/PartDesign_ExampleTrans-03.png  style="width:200px;">             | -   Kontury: Początkowy: **wielokąt**, Końcowy: **gwiazda**. |
|                          |                                                                                                       | -   Ścieżka: prosta **linia**.                               |
++++



### Opcje



#### Przejścia narożników 

Polilinia może być użyta jako ścieżka, a właściwość **Przejście** wpływa na kształty narożników.

Transformowany wymaga szczególnej uwagi, ponieważ może wytwarzać płaskie obszary, dla których grubość wynosi 0.

++++
| Parametr                 | Widok Iso                                                                                                                | Widok z góry                                                                                                                   |
+==========================+==========================================================================================================================+================================================================================================================================+
| **Przekształcony**       | <img alt="Przekształcony widok Iso" src=images/PartDesign_ExampleProperty-01.png  style="width:200px;">                   | <img alt="Przekształcony widok z góry" src=images/PartDesign_ExampleProperty-02.png  style="width:200px;">                   |
|                          |                                                                                                                          |                                                                                                                                |
|                          | :   Wewnętrzne i zewnętrzne narożniki są krawędziami.                                                                    | :   Kształt podstawowy nie jest zgodny z orientacją linii.                                                                     |
++++
| **Prawy narożnik**       | <img alt="Widok Iso prawego rogu" src=images/PartDesign_ExampleProperty-03.png  style="width:200px;">                       | <img alt="Widok z góry prawego narożnika" src=images/PartDesign_ExampleProperty-04.png  style="width:200px;">             |
|                          |                                                                                                                          |                                                                                                                                |
|                          | :   Wewnętrzne i zewnętrzne narożniki to krawędzie.                                                                      | :   Podstawowy kształt jest zgodny z orientacją linii.                                                                         |
++++
| **Zaokrąglony narożnik** | <img alt="Widok Iso zaokrąglonego narożnika" src=images/PartDesign_ExampleProperty-05.png  style="width:200px;"> | <img alt="Widok z góry zaokrąglonego narożnika" src=images/PartDesign_ExampleProperty-06.png  style="width:200px;"> |
|                          |                                                                                                                          |                                                                                                                                |
|                          | :   Narożniki leżące poza ścieżką są zaokrąglone.                                                                        | :   Podstawowy kształt jest zgodny z orientacją linii.                                                                         |
++++



#### Tryb orientacji 

++++
| Parametr        | Widok Iso                                                                                                               | Widok z góry                                                                                                                          |
+=================+=========================================================================================================================+=======================================================================================================================================+
| **Standardowy** | <img alt="Standardowy widok Iso" src=images/PartDesign_ExampleProperty-07.png  style="width:200px;">                        | <img alt="Standardowy widok od góry" src=images/PartDesign_ExampleProperty-08.png  style="width:200px;">                              |
|                 |                                                                                                                         |                                                                                                                                       |
|                 | :   Położenie i orientacja podążają za ścieżką.                                                                         | :   *(Jeśli obiekt jest skręcony w nieoczekiwany sposób, wypróbuj parametr \"Frenet\")*                                               |
|                 | :                                                                                                                       |                                                                                                                                       |
++++
| **Ustalony**    | <img alt="Ustalony widok Iso" src=images/PartDesign_ExampleProperty-09.png  style="width:200px;">                              | <img alt="Ustalony widok z góry" src=images/PartDesign_ExampleProperty-10.png  style="width:200px;">                                      |
|                 |                                                                                                                         |                                                                                                                                       |
|                 | :   Położenie podąża za ścieżką, a orientacja pozostaje taka sama jak kształt podstawowy.                               | :   Może to prowadzić do samoczynnych przecięć, które prowadzą do dalszych błędów: w tym przypadku do powstania ściany widmo.         |
++++
| **Frenet**      | <img alt="Widok Frenet iso" src=images/PartDesign_ExampleProperty-07.png  style="width:200px;">                                  | <img alt="Widok Frenet z góry" src=images/PartDesign_ExampleProperty-08.png  style="width:200px;">                                          |
|                 |                                                                                                                         |                                                                                                                                       |
|                 | :   Położenie i orientacja podążają za ścieżką, w oparciu o inny algorytm niż Standardowy.                              | :   Podstawowy kształt jest zgodny z orientacją linii.                                                                                |
++++
| **Pomocniczy**  | <img alt="Widok pomocniczy Iso" src=images/PartDesign_ExampleProperty-11._png  style="width:200px;">                         | <img alt="Widok pomocniczy z góry" src=images/PartDesign_ExampleProperty-12._png  style="width:200px;">                                 |
|                 |                                                                                                                         |                                                                                                                                       |
|                 | :   Lokalizacja podąża ścieżką ze skrętem wokół ścieżki, która jest kontrolowana przez krzywą pomocniczą *(niebieską)*. | :   *(Trudno to rozpoznać, ale istnieje kąt między płaszczyznami krzywej pomocniczej i ścieżki, który jest odpowiedzialny za skręt)*. |
++++
| **Binormalny**  |                                                                                                                         |                                                                                                                                       |
++++


</div>


</div>



---
⏵ [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Examples/pl
