---
- GuiCommand:/pl
   Name:SheetMetal Forming
   Name/pl:Formowanie blach
   MenuLocation:SheetMetal → Wykonaj formowanie na ścianie
   Workbenches:[Blacha](SheetMetal_Workbench/pl.md)
   Shortcut:**M** **F**
---

# SheetMetal Forming/pl

## Opis

Polecenie <img alt="" src=images/SheetMetal_Forming.svg  style="width:24px;"> **Formowanie blach** tworzy wytłoczenie w powierzchni blachy przy użyciu oddzielnego obiektu bryłowego.

Tylna ściana bryły definiującej kształt oraz ściana, która ma zostać wytłoczona, są używane do pozycjonowania i orientowania bryły, tzn. ich lokalne układy współrzędnych będą miały domyślnie ten sam początek i tę samą orientację. Kąt wokół osi Z oraz przesunięcia w kierunku X, Y i Z można zmienić, zmieniając ich wartości w [Edytorze właściwości](Property_editor/pl.md).

Można dodać szkic, aby zwielokrotnić i rozłożyć wytłoczony kształt w regularne lub nieregularne wzory *(używając punktów środkowych okręgów lub łuków)*.

Mały prezentacja mozliwości, które mogą być tworzone:

<img alt="" src=images/SheetMetal_Forming-08.png  style="width:200px;"> <img alt="" src=images/SheetMetal_Forming-09.png  style="width:200px;"> <img alt="" src=images/SheetMetal_Forming-10.png  style="width:200px;"> <img alt="" src=images/SheetMetal_Forming-11.png  style="width:200px;"> 
*wgłębienia, żaluzje, rysowane wycięcia, mostki*

## Użycie

Upewnij się, że bryła zawierająca obiekt, który ma zostać wytłoczony, jest aktywną bryłą. W razie potrzeby kliknij na nią dwukrotnie w [Widoku drzewa](Tree_view/pl.md).

### Wgłębienia

1.  Wybierz powierzchnię obiektu Arkusz blachy, która ma zostać wytłoczona.
2.  Przytrzymaj wciśnięty klawisz **Ctrl** *(lub **Command** w systemie macOS)*.
3.  Dodaj do zaznaczenia \"dolną powierzchnię\" *(tylną stronę)* bryły definiującej kształt.
4.  Zwolnij klawisz **Ctrl** *(lub przycisk **polecenia**)*.
5.  Aktywuj narzędzie <img alt="" src=images/SheetMetal_Forming.svg  style="width:24px;">[Formowanie blach](SheetMetal_Forming/pl.md) za pomocą jednej z poniższych czynności:
    -   Przycisk **<img src="images/SheetMetal_Forming.svg" width=24px> [Formowanie blach](SheetMetal_Forming/pl.md)**.
    -   W menu należy wybrać **SheetMetal → <img src="images/SheetMetal_Forming.svg" width=24px> Wykonaj formowanie w ścianie**.
    -   Skrót klawiaturowy: **M** a następnie **F**.

### Żaluzje

1.  Wybierz powierzchnię obiektu Arkusz blachy, która ma zostać wytłoczona.
2.  Przytrzymaj wciśnięty klawisz **Ctrl** *(lub **Command** w systemie macOS)*.
3.  Dodaj do zaznaczenia \"dolną powierzchnię\" *(tylną stronę)* bryły definiującej kształt.
4.  Dodaj do zaznaczenia \"boczną ścianę\" przylegającą do dolnej ściany, aby wskazać miejsce cięcia.
5.  Zwolnij klawisz **Ctrl** *(lub klawisz **Command**)*.
6.  Aktywuj narzędzie <img alt="" src=images/SheetMetal_Forming.svg  style="width:16px;"> [Formowanie blach](SheetMetal_Forming/pl.md) *(patrz wyżej)*.

### Mostki

1.  Wybierz powierzchnię obiektu Arkusz blachy, który ma zostać wytłoczony.
2.  Przytrzymaj wciśnięty klawisz **Ctrl** *(lub **Command** w systemie macOS)*.
3.  Dodaj do zaznaczenia \"dolną powierzchnię\" *(tylną stronę)* bryły definiującej kształt.
4.  Dodaj do zaznaczenia \"boczną ścianę\" przylegającą do dolnej ściany, aby wskazać miejsce pierwszego cięcia.
5.  Dodaj do zaznaczenia \"przeciwległą ścianę boczną\" przylegającą do dolnej ściany, aby wskazać miejsce drugiego cięcia.
6.  Zwolnij klawisz **Ctrl** *(lub klawisz **Command**)*.
7.  Aktywuj narzędzie <img alt="" src=images/SheetMetal_Forming.svg  style="width:24px;"> [Formowanie blach](SheetMetal_Forming/pl.md) *(patrz wyżej)*.

### Rysowane wycięcia 

1.  Wybierz powierzchnię obiektu Arkusz blachy, który ma zostać wytłoczony.
2.  Przytrzymaj wciśnięty klawisz **Ctrl** *(lub **Command** w systemie macOS)*.
3.  Dodaj do zaznaczenia \"dolną powierzchnię\" (tylną) bryły definiującej kształt.
4.  Dodaj do zaznaczenia \"górną ścianę\" naprzeciwko dolnej, aby zaznaczyć obszar, który ma zostać wycięty.
5.  Zwolnij klawisz **Ctrl** *(lub klawisz **Command**)*.
6.  Aktywuj narzędzie <img alt="" src=images/SheetMetal_Forming.svg  style="width:24px;">. [Formowanie blachy](SheetMetal_Forming/pl.md) *(patrz wyżej)*.

### Powielanie i tworzenie wzoru 

Aby powielić i nadać wzór wytłoczonemu elementowi, można dodać **szkic** zawierający okręgi i łuki do właściwości obiektu **Formowanie Ściany** **Szkic**. Szkic wzoru musi być *współpłaszczyznowy* z powierzchnią, która ma podlegać wytłoczeniu.

Punkty środkowe okręgów lub łuków są używane do zapewnienia pozycji do umieszczenia wystąpień wytłoczonego elementu, nie mają one wpływu na orientację wystąpień.

Orientacja nadal zależy od orientacji pierwszej wybranej ściany.

### Dodawanie zaokrągleń 

1.  Przełącz się na środowisko pracy <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [Projekt Części](PartDesign_Workbench/pl.md),
2.  Wybierz krawędź na górnej stronie obiektu Arkusza blachy, aby otrzymać zaokrąglenie
3.  Aktywuj funkcję <img alt="" src=images/PartDesign_Fillet.svg  style="width:24px;"> [Zaokrąglenie](PartDesign_Fillet/pl.md) za pomocą jednej z poniższych metod:
    -   Przycisk na pasku narzędzi **<img src="images/PartDesign_Fillet.svg" width=16px> [Zaokrąglenie](PartDesign_Fillet/pl.md)**.
    -   Opcja menu **Projekt Części → Zastosuj funkcje ulepszenia → <img src="images/PartDesign_Fillet.svg" width=24px> Zaokrąglenie**.
4.  Ustaw właściwość **Dopracuj** obiektu Zaokrąglenie na {{TRUE/pl}}. Jest to ważne dla następnego zaokrąglenia.
5.  Wybierz krawędź w dolnej części obiektu Arkusz blachy, która ma zostać zaokrąglona.
6.  Aktywuj <img alt="" src=images/PartDesign_Fillet.svg  style="width:16px;"> [Zaokrąglenie](PartDesign_Fillet/pl.md) *(patrz wyżej)*.

## Uwagi

Geometria wytłoczona nie ogranicza się do ścian planarnych i połączeń cylindrycznych, dlatego po zastosowaniu takiej geometrii na obiekcie typu Arkusz blachy **obiekt nie będzie już rozkładalny**.

Formowanie można wyłączyć *(ustawiając właściwość **Pomiń cechę** na wartość {{True}})* w celu rozłożenia obiektu, ale zaokrąglenia tracą swoje definiujące krawędzie i wyświetlają błąd, gdy formowanie jest ponownie włączone.

Formowanie i zaokrąglenia powinny być ostatnimi krokami przy tworzeniu obiektu typu arkusz blachy.

## Właściwości

Zobacz również stronę: [Edytor właściwości](Property_editor/pl.md).

Obiekt Formowanie blach wywodzi się z obiektu [Część: Cecha](Part_Feature/pl.md) i dziedziczy wszystkie jego właściwości. Posiada on również następujące dodatkowe właściwości:

### Dane


{{Properties_Title|Podstawowe}}

-    **Etykieta|String**: Wartość domyślna: {{value|WallForming}} *(+ kolejny numer dla drugiej i następnych pozycji)*.

Edytowalna przez użytkownika nazwa tego obiektu, może to być dowolny ciąg znaków UTF8.

-    **Podstawa Cecha|Link|hidden**: Cecha bazowa. Link do elementu nadrzędnego.

-    **_Zawartość|LinkHidden|hidden**:


{{Properties_Title|Parametry}}

-    **Pomiń cechę|Bool**: \" Wyklucz cechę formowania\". Domyślna wartość to {{FALSE/pl}}.

-    **kąt|Angle**: \" Kąt położenia narzędzia\". Domyślny kąt: {{value|0,00°}}.

-    **obiekt Bazowy|LinkSub**: \"Obiekt bazowy\". Link do powierzchni planarnej, która ma zostać wytłoczona.

-    **offset|VectorDistance**: \" Odsunięcie od środka ściany\". Domyślnie: {{value|[0,00 mm, 0,00 mm, 0,00 mm]}}.

-    **grubość|Distance**: \" Grubość arkusza blachy\". Grubość **Cecha bazowa||hidden**:.

-    **Obiekt narzędzia|LinkSub**: \"Obiekt narzędzia formującego\". Link do powierzchni planarnej używanej do pozycjonowania narzędzia do formowania.


{{Properties_Title|Parametry1}}

-    **Szkic|Link**: \"Szkic punktu na blasze\". Link do szkicu zawierającego informacje jak zwielokrotnić i rozmieścić wystąpienia narzędzia formującego. *(Punkty środkowe okręgów i łuków są używane do tworzenia i pozycjonowania tych wystąpień)*.

## Przykład

<img alt="" src=images/SheetMetal_Forming-01.png  style="width:300px;"> <img alt="" src=images/SheetMetal_Forming-02.png  style="width:300px;"> 
*Sześciokątna miska z wytłoczonym środkiem*

### Przygotowanie


<div class="mw-collapsible mw-collapsed">


<div class="mw-collapsible-content">

Ta miska jest wykonana ze złożenia przedmiotu z blachy z kształtem do wytłoczenia, oba muszą być wcześniej przygotowane.

Tutaj nie ma potrzeby pracy z szkicami współplanarnymi.

<img alt="" src=images/SheetMetal_Forming-03.png  style="width:200px;"> 
*Arkusz blachy metalowej miski i obiekt do wytłaczania*

### Przepływ pracy 

1.  Wybierz ściankę obiektu arkusza blachy, który ma zostać wytłoczony
2.  Wybierz **tylną stronę** bryły definiującej kształt  *(Pamiętaj, że zarówno obiekt, który ma być wytłoczony **jak i** bryła definiująca kształt muszą być zaznaczone. Aktywuj metodę wielokrotnego wyboru odpowiednią dla Twojego systemu operacyjnego: <img alt="" src=images/SheetMetal_Forming-04.png  style="width:240px;">
3.  Naciśnij przycisk  lub użyj skrótu klawiaturowego:  <img alt="" src=images/SheetMetal_Forming-05.png  style="width:240px;">
4.  Zaokrąglij ostre krawędzie:
    -   Odwróć miskę i wybierz jedną lub więcej krawędzi dla mniejszych promieni wewnętrznych
    -   Naciśnij przycisk <img alt="" src=images/SheetMetal_Forming-12.png  style="width:240px;"> **\--\>** <img alt="" src=images/SheetMetal_Forming-02.png  style="width:240px;">
    -   Odwróć ponownie miskę i wybierz jedną lub więcej krawędzi dla większych promieni zewnętrznych
    -   Naciśnij przycisk <img alt="" src=images/SheetMetal_Forming-13.png  style="width:240px;"> **\--\>** <img alt="" src=images/SheetMetal_Forming-01.png  style="width:240px;">   Gotowe!  
5.  Zmiana orientacji i położenia *(należy to zrobić przed rozpoczęciem zaokrąglania)*
    -   Aktywuj obiekt <img alt="" src=images/SheetMetal_Forming.svg  style="width:24px;"> WallForming w [Widoku drzewa](Tree_view/pl.md)
    -   Ustawić wartość właściwości  <img alt="" src=images/SheetMetal_Forming-14.png  style="width:240px;">
    -   Ustaw wartość właściwości  <img alt="" src=images/SheetMetal_Forming-06.png  style="width:240px;">  Tutaj widać wyraźnie, że nie ma sensu przesuwać wytłoczonej geometrii poza wybraną ścianę.  
    -   Ustawienie wartości właściwości  <img alt="" src=images/SheetMetal_Forming-07.png  style="width:240px;">  Przynajmniej FreeCAD nie zawiesza się, gdy część ma dwie bryły\...  
6.  Kilka wskazówek
    1.  Wysokość bryły definiującej określa głębokość wytłoczonego kształtu. \</Oznacza to, że zmiana parametru **odsunięcie, z** w celu zmiany głębokości nie przyniesie oczekiwanych rezultatów.
    2.  Wytłoczona geometria jest wykonana z obiektu typu powłoka, tzn. ma stałą grubość. \</Dlatego bryła definiująca musi być odsunięta, w przeciwnym razie narzędzie nie utworzy wytłoczenia.
    3.  Jeśli zewnętrzne krawędzie zostaną najpierw zaokrąglone, może to spowodować rozerwanie obiektu na kilka kawałków, jeśli promienie będą miały zbyt duże wartości.


</div>


</div>



---
![](images/Right_arrow.png) [documentation index](../README.md) > [SheetMetal](Category_SheetMetal.md) > [Addons](Category_Addons.md) > [External Command Reference](Category_External Command Reference.md) > SheetMetal Forming/pl
