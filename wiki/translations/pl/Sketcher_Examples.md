# Sketcher Examples/pl
{{TOCright}}



## Wprowadzenie

Myślę, że środowisko pracy <img alt="" src=images/Workbench_Sketcher.svg  style="width:24px;"> [Szkicownik](Sketcher_Workbench/pl.md) potrzebuje kilku przykładów, które nie są szczegółowymi poradnikami czy filmikami \...



## Zawias zwijany 

Zawias zwijany to niewielki kawałek zginanego tworzywa sztucznego, który łączy dwie strony przedmiotu formowanego wtryskowo, np. przepustu z pokrywą lub obu połówek obudowy wtyczki chroniącej przed kurzem.

Ten przykład wykorzystuje pewien rodzaj szkicu głównego, na którym umieszcza się kilka zależnych od niego szkiców. Pokazuje również jak dołączyć i animować prosty zacisk wykonany na funkcjach środowiska pracy <img alt="" src=images/Workbench_PartDesign.svg  style="width:16px;"> [Projekt Części](PartDesign_Workbench/pl.md) oraz <img alt="" src=images/Workbench_Sketcher.svg  style="width:16px;"> [Szkicownik](Sketcher_Workbench/pl.md) z wiązaniami. Zastosowanie <img alt="" src=images/Bound-expression.svg  style="width:16px;"> [wyrażeń](Expressions/pl.md) w sposób opisany poniżej wymaga programu FreeCAD w wersji **0.21** lub nowszego.



### Podstawowy szkic 

Zwykle obiekt jest modelowany w stanie zamkniętym. Później ruchoma część musi zostać odwrócona o 180°, aby uformować ją w stanie otwartym.
Zginany pasek jest reprezentowany przez okrągły łuk dla stanu zamkniętego i linię prostą dla stanu otwartego, oba mające ten sam punkt początkowy.
Punkt środkowy linii łączącej oba punkty końcowe wskazuje położenie osi odwracania, która jest normalna do płaszczyzny szkicu. *(Jest umieszczony na początku szkicu, dzięki czemu globalna oś prostopadła do płaszczyzny szkicu może być użyta jako oś odwracania)*


<div class="mw-collapsible mw-collapsed">

(Niektóre ukryte dodatkowe wyjaśnienia i opis przepływu pracy można rozwinąć tutaj \--\>

<img alt="" src=images/Sketcher_ExampleHinge-01.gif  style="width:400px;"> 
*Szkic główny i animowany zawias zacisku widok końcowy. ''(kliknij na obrazek, jeśli animacja zatrzymała się po kilku powtórzeniach)''*


<div class="mw-collapsible-content toccolours">

W przypadku półokręgu długość łuku to promień pomnożony przez Pi (*l = r \* Pi*). Promień nazywany jest Promieniem Neutralnym, a linia nazywana jest Długością rozwiniętą. Wyrażenie dla DevelopedLength odnosi się do obu wartości: `.Constraints.NeutralRadius * pi`

:   W tym samym szkicu wyrażenie zaczyna się od `.`, po którym następuje ValueType.ValueName, aby odnieść się do innej wartości.


</div>



### Szkic pośredni 

Łuk tego zwijanego zawiasu ma stałą długość i zmienny promień. Jednym z danych wejściowych jest Promień Neutralny szkicu podstawowego. Aby mieć go pod ręką w tym szkicu, jest on połączony jako <img alt="" src=images/Sketcher_External.svg  style="width:16px;"> [geometria zewnętrzna](Sketcher_External/pl.md) posiadający wymiar referencyjny o nazwie Promień Odniesienia


<div class="mw-collapsible-content toccolours">

Segment kołowy geometrii konstrukcyjnej wyświetla zależność między łukiem a promieniem dla danego kąta.
**InputLength = ReferenceRadius \* Pi**
oraz
**ArcLength = DynamicRadius \* Pi \* ArcAngle / 180°**
przy stałej długości daje:
**ReferenceRadius \* Pi = DynamicRadius \* Pi \* ArcAngle / 180°**
Natomiast po wyeliminowaniu Pi otrzymujemy:
**ReferenceRadius = DynamicRadius \* ArcAngle / 180°** lub **DynamicRadius = ReferenceRadius \* 180° / ArcAngle**

:   Wyrażenie <img alt="" src=images/Bound-expression.svg  style="width:16px;"> [expression](Expressions.md) dla wartości DynamicRadius: `.Constraints.ReferenceRadius * 180 ° / .Constraints.ArcAngle`

Zawias zwijany jest zwykle symetryczny, więc inny łuk o tym samym punkcie środkowym o nazwie HalfArc jest używany do wyjścia i reprezentuje jedną połowę łuku zawiasu.

:   <img alt="" src=images/Bound-expression.svg  style="width:16px;"> [Wyrażenie](Expressions/pl.md) dla wartości HalfArc: `.Constraints.ArcAngle / 2`.


</div>

<img alt="" src=images/Sketcher_ExampleHinge-02.png  style="width:400px;"> 
*Szkic pośredni pokazujący Promień Dynamiczny łuku zawiasu 4 ''(mm)'' przy danym kącie 45° ''(i półłuku dla wyjścia)''*



### Szkic zawiasu zwijanego 

Szkic ten definiuje grubość i przylegającą geometrię zawiasu zwijanego. W związku z tym ładujemy połowę łuku szkicu pośredniego jako geometrię zewnętrzną, aby użyć jej jako podstawy dla części zwijanej *(w tym przypadku ułamek 180°)*.

Ten zawias zwijany ma za zadanie utrzymywać połączone części stykające się ze sobą po zamknięciu. Można to osiągnąć, obliczając okrągły łuk o wymaganej długości, a następnie tworząc pasek o stałej grubości i na koniec nakładając zaokrąglenia w miejscu, w którym pasek styka się z połówkami obiektu. Ostatni krok w pewien sposób skraca pętlę, ale w prawdziwym świecie nie jest to problemem, ponieważ łuk nigdy nie będzie okrągły, więc zaokrąglenia mają wpływ na krzywiznę łuku, ale nie na jego funkcjonalność.

<img alt="" src=images/Sketcher_ExampleHinge-03.png  style="width:400px;"> 
*Szkic zawiasu przedstawiający zarys zawiasu na podstawie geometrii zewnętrznej z półłuku szkicu pośredniego*

<img alt="" src=images/Sketcher_ExampleHinge-04.png  style="width:300px;"> <img alt="" src=images/Sketcher_ExampleHinge-05.png  style="width:300px;"> 
*Po lewej: <img src="images/PartDesign_Pad.svg" width=16px> [Wyciągnięty](PartDesign_Pad/pl.md) półzawias z widocznym szkicem. Po prawej: półzawias z dodatkiem <img src="images/PartDesign_Fillet.svg" width=16px> [zaokrąglenia](PartDesign_Fillet/pl.md)*

<img alt="" src=images/Sketcher_ExampleHinge-06.png  style="width:300px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Sketcher_ExampleHinge-07.png  style="width:300px;"> 
*Półzawias z wybraną płaszczyzną lustrzaną →  zawias zwijany <img src="images/PartDesign_Mirrored.svg" width=16px> [w odbiciu lustrzanym](PartDesign_Mirrored/pl.md)*

Wskazówka: Narzędzie <img alt="" src=images/Part_Mirror.svg  style="width:16px;"> [odbicie lustrzane](Part_Mirror/pl.md) akceptuje tylko trzy podstawowe płaszczyzny, więc nie może zostać użyte w takim przypadku.

:   *(Z perspektywy czasu mądrą decyzją było rozpoczęcie tego przykładu od połączenia środowisk Projekt Części i Szkicownik)*.

Wreszcie dwa parametry definiują rozmiar zawiasu zwijanego:

-   Promień Neutralny szkicu podstawowego,
-   wartość grubości szkicu zawiasu.



### Gięcie zawiasu zwijanego 

Kąt zgięcia jest kontrolowany przez wiązanie Arc Angle szkicu pośredniego i może być zmieniany w jego edytorze właściwości.
Jesteśmy jednak dobrymi projektantami i prawidłowo nazwaliśmy nasze wiązania i wymiary szkiców, więc możemy zająć się kontrolowaniem kąta za pomocą środowiska Pyton.
Kilka podstawowych linii kodu do osadzenia w kontekście GUI może wyglądać następująco:


```python
doc=App.ActiveDocument
sketch=doc.getObjectsByLabel('IntermediateSketch')[0]
 ...
sketch.getDatum('ArcAngle')
 ...
sketch.setDatum('ArcAngle',App.Units.Quantity('50.000000 deg'))
doc.recompute(None,True,True)
```


<div class="mw-collapsible-content toccolours">

Krótkie wyjaśnienie:

-    {{Incode|doc {{=}}App.ActiveDocument}}: Aby zaadresować aktywny dokument przez alias o nazwie **doc**

-    {{Incode|sketch {{=}}doc.getObjectsByLabel(\'IntermediateSketch\')\[0\]}}: Aby zaadresować odpowiedni szkic przez alias **sketch**.

    :   Metoda **getObjectsByLabel()**\' zwraca listę obiektów i musimy dodać indeks {{value|0}}, aby wybrać pierwszy obiekt z listy. (Nie spodziewamy się żadnego innego obiektu o tej samej etykiecie, więc nie musimy dbać o inne pozycje na liście).

-    {{Incode|sketch.getDatum('ArcAngle')}}: Zwraca bieżącą wartość wiązania wymiarowego **ArcAngle** (do widoku raportu).

-    {{Incode|sketch.setDatum('ArcAngle', App.Units.Quantity('50.0 deg'))}}: Ustawia wartość **ArcAngle** na {{value|50°}}.

-    {{Incode|doc.recompute(None,True,True)}}: Aktualizuje cały dokument, aby pokazać również zmiany zależnej geometrii.


</div>



### Geometria łącząca 

Dwie połówki zacisku czekają na przymocowanie do zawiasu, jedna po stronie statycznej, druga po stronie ruchomej.

<img alt="" src=images/Sketcher_ExampleHinge-08.png  style="width:300px;"> 
*Dwie połówki prostego zacisku*


<div class="mw-collapsible-content toccolours">

Strona statyczna jest łatwa:

1.  Aktywuj zawartość i dostosuj właściwości pozycji i orientacji w edytorze właściwości, aż będzie pasował do zawiasu zwijanego.
2.  Aktywuj zawartość zawiasu.
3.  Wybierz <img alt="" src=images/PartDesign_Boolean.svg  style="width:16px;"> [Operacje logiczne](PartDesign_Boolean/pl.md) narzędzie z *(domyślną)* opcją Scalenie.
4.  W oknie dialogowym naciśnij przycisk **Dodaj zawartość**
5.  wybierz **ciało** statycznej połowy klipu.
6.  Naciśnij OK, aby zakończyć i zamknąć okno dialogowe.


</div>

<img alt="" src=images/Sketcher_ExampleHinge-09.png  style="width:300px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Sketcher_ExampleHinge-10.png  style="width:300px;"> 
*Zawias zwijany i statyczna połówka w pozycji modelowania → zawias zwijany z przeniesioną i <img src="images/PartDesign_Boolean.svg" width=16px> [scaloną](PartDesign_Boolean/pl.md) statyczną połówką*


<div class="mw-collapsible-content toccolours">

Ale ruchoma strona jest inna: powiązana połowa geometrii zacisku musi przesunąć się do właściwej pozycji, zanim rozpocznie się (ponowne) obliczanie operacji Scalenia.

W tym momencie brakuje mi funkcji \"Umocowanie z odsunięciem\", takiej jak w środowisku Złożenie 3, aby dołączyć geometrię zacisku do jednej z ruchomych ścian. Ale po odrobinie eksperymentów i poprawek znalazłem rozwiązanie:

-   <img alt="" src=images/Std_Part.svg  style="width:16px;"> [Część](Std_Part/pl.md) i <img alt="" src=images/PartDesign_Body.svg  style="width:16px;"> [Zawartość](PartDesign_Body/pl.md) środowiska Projekt Części nie są obsługiwane przez <img alt="" src=images/Part_EditAttachment.svg  style="width:16px;">. [Dołączenie](Part_EditAttachment/pl#Ograniczenia.md).

Chociaż możliwe jest użycie dołączenia do ich wyrównania, dołączenie nie będzie połączone parametrycznie.

-   Dołączenie może być zastosowany do elementu środowiska Projekt Części. Ten element i elementy od niego zależne zostaną przesunięte zgodnie z geometrią bazową. Ale!
    -   Niezależne elementy środowiska Projekt Części nie będą się przesuwać, co spowoduje zmianę wynikowego kształtu i jego złamanie.
    -   Zaleca się zachowanie niezależności elementów, aby uniknąć wpływu [problemu nazewnictwa topologicznego](Topological_naming_problem/pl.md).
-   <img alt="" src=images/PartDesign_Clone.svg  style="width:16px;"> [Klon](PartDesign_Clone/pl.md) tworzy bryłę z pojedynczą cechą, która może być użyta z dołączeniem.

Mając to na uwadze, przepływ pracy może wyglądać następująco:

1.  Wybierz Zawartość ruchomej połowy.
2.  Użyj polecenia <img alt="" src=images/PartDesign_Clone.svg  style="width:16px;"> [Utwórz klon](PartDesign_Clone/pl.md).
3.  W nowej bryle wybierz obiekt Klon w widoku Drzewa.
4.  Użyj polecenia <img alt="" src=images/Part_EditAttachment.svg  style="width:16px;"> [Dołączenie](Part_EditAttachment/pl.md), aby dodać właściwości dołączenia do obiektu Clon.
5.  Otworzy się okno dialogowe Dołączenie.
    -   Wybierz wierzchołek dla punktu odniesienia położenia.
    -   Wybierz krawędź dla pierwszego kierunku.
    -   Wybierz krawędź dla drugiego kierunku.
    -   Sprawdź tryby dołączenia, aby znaleźć najlepiej pasujący.
    -   Zmieniaj wartości obrotu i współrzędnych, aż geometria ponownie znajdzie się w pozycji modelowania.
6.  Naciśnij OK, aby zamknąć okno dialogowe.
7.  Przy wciąż aktywnej Zawartości zawiasu wybierz narzędzie <img alt="" src=images/PartDesign_Boolean.svg  style="width:16px;"> [Operacja logiczna](PartDesign_Boolean/pl.md).
8.  W oknie dialogowym naciśnij przycisk **Dodaj zawartość**.
9.  wybierz Zawartość ruchomej połówki.
10. Naciśnij przycisk OK, aby zakończyć i zamknąć okno dialogowe.


</div>


</div>

<img alt="" src=images/Sketcher_ExampleHinge-14.png  style="width:300px;"> 
*Ruchoma połowa będzie <img src="images/Part_EditAttachment.svg" width=16px>. [dołączona](Part_EditAttachment/pl.md) do rogu ruchomej strony zawiasu ''(tryb mapowania OXZ: wierzchołek, krawędź, krawędź)''.*

Z perspektywy czasu rozsądniej byłoby dostarczyć geometrię mocowania wraz ze Szkicem pośrednim, aby uniknąć kolejnego źródła [problemu nazewnictwa topologicznego](Topological_naming_problem/pl.md).

<img alt="" src=images/Sketcher_ExampleHinge-11.png  style="width:300px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Sketcher_ExampleHinge-12.png  style="width:300px;"> 
*Dotychczasowy zacisk i ruchoma połowa w pozycji modelowania → gotowy zacisk z <img src="images/Part_EditAttachment.svg" width=16px> [dołączeniem](Part_EditAttachment/pl.md) i <img src="images/PartDesign_Boolean.svg" width=16px> [scaleniem](PartDesign_Boolean/pl.md) ruchomej połówki*

Rezultatem powinien być pojedynczy klip, który można zamykać i otwierać, zmieniając kąt łuku zawiasu zwijanego. Dozwolone kąty: od 0,1° do 180°, sekcja zwijana nie może być prosta, a więcej niż zamknięta nie ma sensu. *(Przy 180° obiekt może zostać stopiony w obszarach stycznych lub nakładających się, ale niewielka dodatkowa przerwa może pomóc, jeśli jest to nie do zaakceptowania.)*

<img alt="" src=images/Sketcher_ExampleHinge-13.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Sketcher_ExampleHinge-15.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Sketcher_ExampleHinge-16.png  style="width:200px;"> 
*Zacisk prawie zamknięty → Zacisk w połowie zamknięty → Zacisk w stanie uformowanym*


{{PartDesign Tools navi

}} {{Sketcher Tools navi}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [PartDesign](Category_PartDesign.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher Examples/pl
