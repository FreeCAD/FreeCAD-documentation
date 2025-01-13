# Manual:Creating and manipulating geometry/pl
{{Manual:TOC}}

W poprzednich rozdziałach omówiliśmy różne środowiska pracy we FreeCAD i sposób, w jaki każde z nich wprowadza swoje własne narzędzia i typy geometrii. Te same zasady odnoszą się do pracy z FreeCAD za pomocą skryptów Pythona.

Zauważyliśmy również, że większość środowisk pracy w FreeCAD opiera się na jednym podstawowym module: [16px](Plik:Workbench_Part.svg.md) [środowisku pracy Część](Part_Workbench/pl.md). Wiele innych środowisk pracy, takich jak [16px](Plik:Workbench_Draft.svg.md) [Rysunek Roboczy](Draft_Workbench/pl.md), wykorzystuje narzędzia i geometrię środowiska Część, co jest dokładnie tym, co zrobimy w tym rozdziale - użyjemy Pythona do tworzenia i manipulowania geometrią środowiska pracy Część.

Aby rozpocząć pracę z geometrią środowiska pracy Część w Pythonie, musimy wykonać skryptowy odpowiednik przełączenia się na środowisko pracy Część: zaimportować moduł Część.


```python
import Part 
```

Poświęć chwilę na eksplorację modułu Część, wpisując **Part.** w konsoli Pythona i przeglądając dostępne metody oraz atrybuty w oknie autouzupełniania. To świetny sposób na zapoznanie się z funkcjonalnością, jaką oferuje ten moduł. Znajdziesz wiele przydatnych funkcji, takich jak makeBox i makeCircle, które pozwalają szybko tworzyć figury geometryczne i obiekty za pomocą jednego polecenia. Wiele z tych funkcji oferuje również opcjonalne parametry, dając Ci precyzyjną kontrolę nad wymiarami i umiejscowieniem.

Spędzenie czasu na przeglądaniu zawartości modułu nie tylko pomoże Ci zrozumieć, jakie narzędzia są dostępne, ale także da Ci wgląd w to, jak działa środowisko pracy Część \"od środka\". Ta podstawowa wiedza okaże się nieoceniona, gdy przejdziemy do tworzenia i manipulowania geometrią za pomocą skryptów. Wpisz następujące polecenie


```python
Part.makeBox(3,5,7) 
```

Ta komenda tworzy prostopadłoscian 3D, znany również jako prostokątny graniastosłup, o określonych wymiarach. Pierwszy parametr, 3, definiuje długość prostopadłościanu wzdłuż osi X. Drugi parametr, 5, ustawia szerokość wzdłuż osi Y, a trzeci parametr, 7, określa wysokość wzdłuż osi Z. Chociaż ta funkcja generuje geometrię prostopadłościanu, nie dodaje go automatycznie do aktywnego dokumentu FreeCAD. W konsoli Pythona zobaczysz:


```python
<Solid object at 0x5f43600> 
```

Wynik **\<Solid object at 0x5f43600\>** wskazuje, że obiekt typu Część: Kształt został utworzony w pamięci. Jest to obiekt geometryczny przechowywany pod określonym adresem pamięci, który jest pokazany przez wartość szesnastkową (0x5f43600). Ważne jest jednak, aby zrozumieć, że to, co stworzyliśmy, nie jest jeszcze obiektem dokumentu FreeCAD - istnieje tylko jako surowy kształt geometryczny w pamięci.

To rozróżnienie podkreśla fundamentalną koncepcję w FreeCAD: obiekty i ich geometria są niezależne. Obiekt dokumentu FreeCAD działa jako kontener, który przechowuje kształt. Te obiekty dokumentu mogą mieć dodatkowe właściwości, takie jak Długość, Szerokość i Wysokość, i mogą być parametryczne. Obiekty parametryczne dynamicznie przeliczają swoją geometrię (lub kształt) za każdym razem, gdy jedna z ich właściwości ulega zmianie. Na przykład, zmiana długości parametrycznego pudełka spowoduje automatyczne odtworzenie jego kształtu z zaktualizowaną wartością.

W tym przypadku ręcznie stworzyliśmy kształt za pomocą funkcji **Part.makeBox()**. Ten kształt jest obiektem nieparametrycznym, co oznacza, że nie będzie się automatycznie aktualizować w zależności od żadnych właściwości - jest statyczny, chyba że będziemy nim manipulować programowo. Aby uczynić ten kształt częścią aktywnego dokumentu FreeCAD, należałoby przypisać go do obiektu dokumentu (takiego jak **Part::Feature**), co połączyłoby go z interfejsem graficznym i umożliwiło wyświetlanie oraz zarządzanie nim w środowisku FreeCAD.

Ta rozdzielność między kształtami a obiektami dokumentu to cecha, która sprawia, że FreeCAD jest bardzo wszechstronny, umożliwiając użytkownikom manipulowanie kształtami programowo i integrowanie ich w razie potrzeby w przepływie pracy modelowania parametrycznego.

Teraz możemy łatwo utworzyć \"ogólny\" obiekt dokumentu w bieżącym dokumencie (upewnij się, że masz otwarty przynajmniej jeden nowy dokument) i nadać mu kształt prostopadłościanu, jak to zrobiliśmy wcześniej:


```python
boxShape = Part.makeBox(3,5,7)
myObj = FreeCAD.ActiveDocument.addObject("Part::Feature","MyNewBox")
myObj.Shape = boxShape
FreeCAD.ActiveDocument.recompute()
```

Oto szczegółowe wyjaśnienie poprzednich poleceń:

-   **boxShape = Part.makeBox(3,5,7)**: Tworzy trójwymiarowy prostopadłościan o wymiarach 3x5x7 (długość, szerokość i wysokość) i przechowuje go jako kształt środowiska pracy Część w zmiennej boxShape. Ten kształt istnieje tylko w pamięci i nie jest jeszcze częścią dokumentu FreeCAD.

-   **myObj = FreeCAD.ActiveDocument.addObject(\"Part::Feature\", \"MyNewBox\")**: Dodaje nowy obiekt typu Part::Feature o nazwie \"MyNewBox\" do aktywnego dokumentu FreeCAD i przypisuje go do zmiennej myObj. Nowy obiekt pojawi się w drzewie dokumentów FreeCAD.

-   **myObj.Shape = boxShape**: Łączy geometrię boxShape z właściwością Shape obiektu myObj, integrując geometrię z dokumentem FreeCAD.

-   **FreeCAD.ActiveDocument.recompute()**: Aktualizuje dokument, aby odzwierciedlić zmiany, zapewniając, że nowy obiekt i jego geometria pojawią się w interfejsie graficznym.

Zauważ, jak obsłużyliśmy **myObj.Shape**. Zrobiliśmy to w sposób podobny do poprzedniego rozdziału, gdzie zmienialiśmy inne właściwości obiektu, takie jak **box.Height = 5**. W rzeczywistości **Shape** jest również właściwością, podobnie jak **Height**. Jednak zamiast liczby, **Shape** wymaga obiektu typu Część: Kształt. W następnym rozdziale przyjrzymy się bliżej, jak te obiekty parametryczne są tworzone.

Na razie przyjrzyjmy się szczegółowo obiektom typu Part Shape. W rozdziale poświęconym tradycyjnemu modelowaniu w <img alt="" src=images/Workbench_Part.svg  style="width:16px;"> [środowisku pracy Część](Part_Workbench/pl.md) wprowadziliśmy tabelę wyjaśniającą, jak tworzona jest geometria Część: Kształty i jakie składają się na nią komponenty, takie jak **wierzchołki**, **krawędzie** i **powierzchnie**. Te same komponenty są dostępne podczas pracy z obiektami typu Część: Kształty w Pythonie, co umożliwia szczegółowe badanie i manipulowanie geometrią. Obiekty Część: Kształty w FreeCAD zawsze posiadają następujące atrybuty:

-   **Wierzchołki**: Punkty w przestrzeni 3D, które definiują narożniki lub końce geometrii.
-   **Krawędzie**: Proste lub zakrzywione linie łączące dwa wierzchołki.
-   **Linie**: Zamknięte lub otwarte pętle utworzone przez jedną lub więcej połączonych krawędzi.
-   **Powierzchnie**: Powierzchnie zamknięte przez jedną lub więcej linii.
-   **Powłoki**: Grupy połączonych powierzchni, tworzące ciągłą powierzchnię.
-   **Bryły**: Objętości 3D zamknięte przez jedną lub więcej powłok.

Wszystkie te atrybuty są reprezentowane jako listy w Pythonie. Każda lista może zawierać dowolną liczbę elementów lub być pusta, w zależności od badanej geometrii. Na przykład, sześcian będzie miał osiem **wierzchołków**, dwanaście **krawędzi**, sześć **powierzchni**, jedną **powłokę** i jedną **bryłę**, podczas gdy linia będzie miała tylko dwa **wierzchołki** i jedną **krawędź**, a wszystkie inne atrybuty będą puste. Te komponenty są podstawowymi elementami geometrii środowiska pracy Część i mogą być dostępne oraz manipulowane programistycznie. Zrozumienie, jak one współdziałają, daje potężną kontrolę nad tworzeniem i modyfikowaniem modeli 3D. Możemy uzyskać dostęp do tych list w następujący sposób:


```python
print(boxShape.Vertexes)
print(boxShape.Edges)
print(boxShape.Wires)
print(boxShape.Faces)
print(boxShape.Shells)
print(boxShape.Solids)
```

Znajdźmy pole każdej powierzchni naszej bryły w kształcie prostopadłościanu: (Upewnij się, że druga linia jest odpowiednio wcięta, tak jak poniżej. Naciśnij Enter dwa razy po ostatniej linii, aby uruchomić polecenie Pythona.)


```python
for f in boxShape.Faces:
   print(f.Area)
```

Albo, dla każdej krawędzi, jej punkt początkowy i końcowy:


```python
for e in boxShape.Edges:
   print("New edge")
   print("Start point:")
   print(e.Vertexes[0].Point)
   print("End point:")
   print(e.Vertexes[1].Point)
```

Jak widzisz, jeśli nasz boxShape posiada atrybut **Vertexes**, każdy z brzegów boxShape posiada również atrybut **Vertexes**. Jak możemy się spodziewać, boxShape będzie posiadał 8 wierzchołków, podczas gdy krawędź będzie miała tylko 2, obie będące częścią listy tych 8.

Zawsze możemy sprawdzić, jaki jest rodzaj kształtu:


```python
print(boxShape.ShapeType)
print(boxShape.Faces[0].ShapeType)
print(boxShape.Vertexes[2].ShapeType)
```

Oto krótkie wyjaśnienie powyższych poleceń:

-   **print(boxShape.ShapeType)**: Wyświetla typ najwyższego poziomu kształtu reprezentowanego przez **boxShape**. W tym przypadku, ponieważ **boxShape** został utworzony jako pudełko za pomocą **Part.makeBox**, wynik będzie \"Solid\", co wskazuje, że kształt jest obiektem 3D typu bryła.

-   **print(boxShape.Faces\[0\].ShapeType)**: Uzyskuje dostęp do pierwszej powierzchni w liście **Faces** obiektu **boxShape** (indeks 0) i wypisuje jej typ. Dla prostopadłościanu każda ściana to płaska powierzchnia, więc wynikiem będzie \"Face\".

-   **print(boxShape.Vertexes\[2\].ShapeType)**: Uzyskuje dostęp do trzeciego wierzchołka w liście **Vertexes** obiektu **boxShape** (indeks 2) i wypisuje jego typ. Ponieważ jest to konkretny punkt w przestrzeni 3D, wynikiem będzie \"Vertex\".

Aby podsumować koncepcję Part Shapes: Wszystko zaczyna się od **Vertexes**, najbardziej podstawowych elementów geometrii. Używając jednego lub dwóch **Vertexes**, można stworzyć **Edge** (zauważ, że pełne okręgi wymagają tylko jednego **Vertex**). Jeden lub więcej **Edges** może utworzyć **Wire**, który może być otwarty lub zamknięty. Gdy masz jeden lub więcej zamkniętych **Wires**, możesz stworzyć **Face**. Dodatkowe **Wires** wewnątrz głównego **Wire** będą działać jako \"otwory\" w **Face**. Łącząc jedną lub więcej **Faces**, można stworzyć **Shell**, który jest zasadniczo zbiorem połączonych powierzchni. Jeśli **Shell** jest całkowicie zamknięty i szczelny, można go użyć do utworzenia **Solid**---obiektu 3D o objętości. Wreszcie, dowolna liczba kształtów dowolnego typu, w tym **Vertexes**, **Edges**, **Wires**, **Faces**, **Shells** lub **Solids**, może być grupowana w **Compound**, który działa jako pojemnik dla wielu kształtów.

Możemy teraz próbować tworzyć złożone kształty od podstaw, konstruując wszystkie ich elementy jeden po drugim. Na przykład, spróbujmy stworzyć taką objętość:

![](images/Exercise_python_03.jpg )

Zaczniemy od stworzenia takiego planarnego kształtu:

![](images/Wire.png )

Po pierwsze, stwórzmy cztery punkty bazowe:


```python
V1 = FreeCAD.Vector(0,10,0)
V2 = FreeCAD.Vector(30,10,0)
V3 = FreeCAD.Vector(30,-10,0)
V4 = FreeCAD.Vector(0,-10,0)
```

Następnie możemy utworzyć dwa segmenty liniowe:

![](images/Line.png )


```python
L1 = Part.LineSegment(V1,V2)
L2 = Part.LineSegment(V4,V3)
```

Zauważ, że nie musieliśmy tworzyć **Vertexes** w sposób jawny. Zamiast tego mogliśmy bezpośrednio tworzyć **Part.LineSegments** przy użyciu **FreeCAD Vectors**. Dzieje się tak, ponieważ na tym etapie pracujemy z geometrią podstawową, a nie rzeczywistymi **Edges**. **Part.LineSegment**, jak również **Part.Circle**, **Part.Arc**, **Part.Ellipse** czy **Part.BSpline**, definiują podstawową geometrię, ale same w sobie nie generują krawędzi. W FreeCAD krawędzie są zawsze tworzone z takiej geometrii podstawowej, która jest przechowywana w atrybucie **Curve** krawędzi. Oznacza to, że krawędź jest zasadniczo opakowaniem wokół geometrii podstawowej, dziedziczącym jej właściwości. Jeśli masz krawędź, możesz uzyskać dostęp do jej podstawowej geometrii, odnosząc się do atrybutu **Curve**. Następujące polecenie:


```python
print(Edge.Curve) 
```

pozwala zrozumieć podstawową strukturę krawędzi i sposób jej konstrukcji. Teraz wróćmy do naszego ćwiczenia i kontynuujmy budowanie segmentów łuków. Aby stworzyć łuk, potrzebujemy trzech punktów: punktu początkowego, punktu końcowego oraz punktu środkowego, który określa krzywiznę. W tym celu możemy użyć funkcji **Part.Arc**, która przyjmuje te trzy punkty jako dane wejściowe i generuje geometrię podstawową dla łuku.

![](images/Circel.png )


```python
VC1 = FreeCAD.Vector(-10,0,0)
C1 = Part.Arc(V1,VC1,V4)
VC2 = FreeCAD.Vector(40,0,0)
C2 = Part.Arc(V2,VC2,V3)
```

Teraz mamy dwie linie *(L1 i L2)* i dwa łuki *(C1 i C2)*. Musimy zamienić je na krawędzie:


```python
E1 = Part.Edge(L1)
E2 = Part.Edge(L2)
E3 = Part.Edge(C1)
E4 = Part.Edge(C2)
```

Alternatywnie, geometrie bazowe mają również funkcję **toShape()**, która robi dokładnie to samo:


```python
E1 = L1.toShape()
E2 = L2.toShape()
 ...
```

Kiedy już będziemy mieli serię krawędzi, możemy teraz stworzyć **Wire**, podając listę krawędzi. Musimy jednak zwrócić uwagę na kolejność. Zwróćcie też uwagę na nawiasy.


```python
W = Part.Wire([E1,E4,E2,E3]) 
```

I możemy sprawdzić, czy nasza polilinia została prawidłowo wykonana, i czy jest prawidłowo zamknięta:


```python
print( W.isClosed() ) 
```

Instrukcja wydrukuje {{Value|True}} lub {{Value|False}}. Aby utworzyć **Face**, potrzebujemy **zamkniętej polilinii**, więc zawsze warto to sprawdzić przed wykonaniem powierzchni. Teraz możemy stworzyć taką powierzchnię, nadając jej pojedynczą polilinię *(lub listę polilinii, jeśli chcemy uzyskać otwory)*:


```python
F = Part.Face(W) 
```

Potem go wyciągamy:


```python
P = F.extrude(FreeCAD.Vector(0,0,10)) 
```

Należy pamiętać, że P to już **Solid**:


```python
print(P.ShapeType) 
```

To dlatego, że kiedy wyciągamy pojedynczą powierzchnię, zawsze otrzymujemy bryłę. Nie miałoby to miejsca, na przykład, gdybyśmy zamiast tego wyciągnęli polilinię:


```python
S = W.extrude(FreeCAD.Vector(0,0,10))
print(S.ShapeType)
```

Co oczywiście da nam pustą powłokę, z brakującą górną i dolną powierzchnią.

Teraz, gdy mamy nasz ostateczny kształt, chcemy go zobaczyć na ekranie! Stwórzmy więc ogólny obiekt, i przypiszmy do niego naszą nową bryłę:


```python
myObj2 = FreeCAD.ActiveDocument.addObject("Part::Feature","My_Strange_Solid")
myObj2.Shape = P
FreeCAD.ActiveDocument.recompute()
```

Alternatywnie, Środowisko pracy Part dostarcza również skrót, który przyspiesza powyższą operację *(ale nie możesz wybrać nazwy obiektu)*:


```python
Part.show(P) 
```

Wszystko to, oraz wiele więcej, zostało szczegółowo wyjaśnione na stronie [Skrypty danych topologicznych](Topological_data_scripting/pl.md), wraz z przykładami.

**Więcej informacji:**

-   [Środowisko pracy Part](Part_Workbench/pl.md)
-   [Skrypty danych topologicznych](Topological_data_scripting/pl.md)



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Python Code](Category_Python Code.md) > Manual:Creating and manipulating geometry/pl
