# Manual:Creating and manipulating geometry/pl
{{Manual:TOC/pl}}

W poprzednich rozdziałach dowiedzieliśmy się o różnych środowiskach pracy programu FreeCAD oraz o tym, jak każde z nich stosuje swoje własne narzędzia i typy geometrii. Ta sama koncepcja obowiązuje przy pracy z kodem Pythona.

Zauważyliśmy również, że zdecydowana większość środowisk pracy FreeCAD zależy od bardzo fundamentalnego elementu: Środowiska pracy [Część](Part_Workbench/pl.md). W rzeczywistości, wiele innych środowisk pracy, takich jak [Rysunek Roboczy](Draft_Workbench/pl.md) i [Arch](Arch_Workbench.md), wykonuje dokładnie to, co zrobimy w tym rozdziale: używa kodu Python do tworzenia i manipulowania geometrią Części.

Więc pierwszą rzeczą, którą musimy zrobić, aby pracować z geometrią części, jest wykonanie w środowisku Python odpowiednika przejścia do Środowiska pracy Part: zaimportuj moduł Part:


```python
import Part 
```

Poświęć minutę na zapoznanie się z zawartością modułu Część, wpisując Part i przeglądając różne dostępne metody. Moduł Część oferuje kilka wygodnych funkcji, takich jak makeBox, makeCircle, itp\... które natychmiast zbudują dla Ciebie obiekt. Spróbuj na przykład tego:


```python
Part.makeBox(3,5,7) 
```

Kiedy naciśniesz **Enter** po wpisaniu powyższej linii, nic nie pojawi się w widoku 3D, ale w konsoli Python zostanie wydrukowane coś takiego:


```python
<Solid object at 0x5f43600> 
```

W tym właśnie miejscu pojawia się ważna koncepcja. To, co tu stworzyliśmy, jest Kształtem Części. Nie jest to obiekt dokumentu FreeCAD *(jeszcze)*. W programie FreeCAD, obiekty i ich geometrie są niezależne. Pomyśl o obiekcie dokumentu FreeCAD jako o kontenerze, który będzie posiadał kształt. Obiekty parametryczne będą miały również właściwości takie jak długość i szerokość oraz będą *przeliczać* swój kształt w locie, gdy tylko jedna z tych właściwości ulegnie zmianie. To, co zrobiliśmy tutaj, to ręczne obliczenie kształtu.

Możemy teraz w prosty sposób stworzyć \"ogólny\" obiekt dokumentu w bieżącym dokumencie *(upewnij się, że masz otwarty przynajmniej jeden nowy dokument)* i nadaj mu kształt pudełka, taki jak ten, który właśnie stworzyliśmy:


```python
boxShape = Part.makeBox(3,5,7)
myObj = FreeCAD.ActiveDocument.addObject("Part::Feature","MyNewBox")
myObj.Shape = boxShape
FreeCAD.ActiveDocument.recompute()
```

Zwróć uwagę, jak obchodziliśmy się z **myObj.Shape**, zauważ, że robimy to dokładnie tak samo, jak robiliśmy to w poprzednim rozdziale, kiedy zmienialiśmy inne właściwości obiektu, takie jak **box.Height = 5**. W rzeczywistości, **Kształt** jest również właściwością, podobnie jak **Wysokość**. Tylko bierze ona obiekt Part Shape, a nie liczbę. W następnym rozdziale lepiej przyjrzymy się temu, jak te parametryczne obiekty są konstruowane.

Na razie przyjrzyjmy się bardziej szczegółowo naszym Kształtom Części. Na końcu rozdziału o [Podręcznik:Modelowanie tradycyjne, według CSG](Manual:Traditional_modeling,_the_CSG_way/pl.md) pokazaliśmy tabelę, która wyjaśnia, jak konstruowane są Kształty Części oraz ich różne komponenty *(wierzchołki, krawędzie, powierzchnie, itp.)*. Dokładnie te same komponenty istnieją tutaj i mogą być pobrane z Pythona. Kształty Części posiadają zawsze następujące atrybuty: wierzchołki, krawędzie, obwiednie, powierzchnie, powłoki i bryły. Wszystkie z nich są listami, które mogą zawierać dowolną liczbę pozycji lub mogą pozostać puste:


```python
print(boxShape.Vertexes)
print(boxShape.Edges)
print(boxShape.Wires)
print(boxShape.Faces)
print(boxShape.Shells)
print(boxShape.Solids)
```

Na przykład, znajdźmy powyżej obszar każdej z powierzchni kształtu naszego sześcianu: *(Pamiętaj o wcięciu drugiego wiersza, tak jak pokazano poniżej. Naciśnij dwukrotnie klawisz Enter po ostatnim wierszu, aby uruchomić polecenie środowiska Python)*.


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

Jak widzisz, jeśli nasz boxShape posiada atrybut **Vertexes**, każdy z brzegów boxShape posiada również atrybut **Vertexes**. Jak możemy się spodziewać, boxShape będzie posiadał 8 wierzchołków, podczas gdy krawędź będzie miała tylko 2, są częścią listy tych ośmiuj.

Zawsze możemy sprawdzić, jaki jest rodzaj kształtu:


```python
print(boxShape.ShapeType)
print(boxShape.Faces[0].ShapeType)
print(boxShape.Vertexes[2].ShapeType)
```

Wróćmy więc do tematu Kształty części: Wszystko zaczyna się od Wierzchołków. Z jednym lub dwoma wierzchołkami tworzysz krawędź *(pełne koła mają tylko jeden wierzchołek)*. Z jedną lub kilkoma krawędziami tworzysz obwiednię. Z pojedynczą lub kilkoma zamkniętymi obwiedniami tworzysz powierzchnię czołową *(dodatkowe obwiednie stają się \"otworami\" w powierzchni czołowej)*. Z jedną lub kilkoma powierzchniami tworzysz Powłokę. Gdy powłoka jest całkowicie zamknięta *(wodoszczelna)*, można z niej utworzyć bryłę. I wreszcie, można połączyć dowolną liczbę dowolnych kształtów, które następnie nazywa się Związkiem.

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

Zauważ, że nie musieliśmy tworzyć wierzchołków. Mogliśmy natychmiast stworzyć Part.LineSegmenty za pomocą FreeCAD Vectors. To dlatego, że tutaj nie stworzyliśmy jeszcze Krawędzi. Part.LineSegment *(jak również Part.Circle, Part.Arc, Part.Ellipse czy Part.BSpline)* nie tworzy krawędzi, ale raczej bazową geometrię, na której zostanie utworzony obiekt Edge. Krawędzie są zawsze tworzone z takiej geometrii bazowej, która jest zapisana w atrybucie Curve. Więc jeśli masz krawędzie, to zrób to:


```python
print(Edge.Curve) 
```

pokaże Ci, jaki to rodzaj obiektu Edge, tzn. czy jest oparty na linii, łuku, itd\... Ale wróćmy do naszego ćwiczenia, i zbudujmy segmenty łuku. Do tego będziemy potrzebowali trzeciego punktu, więc możemy użyć wygodnego Part.Arc, który pobiera 3 punkty:

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

Kiedy już będziemy mieli serię krawędzi, możemy teraz stworzyć obwiednię, podając jej listę krawędzi. Musimy jednak zwrócić uwagę na kolejność. Zwróćcie też uwagę na nawiasy.


```python
W = Part.Wire([E1,E4,E2,E3]) 
```

I możemy sprawdzić, czy nasza obwiednia została prawidłowo wykonana, i czy jest prawidłowo zamknięta:


```python
print( W.isClosed() ) 
```

Instrukcja wydrukuje {{Value|True}} lub {{Value|False}}. Aby wykonać powierzchnię, potrzebujemy zamkniętej obwiedni, więc zawsze warto to sprawdzić przed wykonaniem powierzchni. Teraz możemy stworzyć taką powierzchnię, nadając jej pojedynczą obwiednię *(lub listę obwiedni, jeśli chcemy uzyskać otwory)*:


```python
F = Part.Face(W) 
```

Potem go wyciągamy:


```python
P = F.extrude(FreeCAD.Vector(0,0,10)) 
```

Należy pamiętać, że P jest już bryłą:


```python
print(P.ShapeType) 
```

To dlatego, że kiedy wyciągamy pojedynczą powierzchnię, zawsze otrzymujemy bryłę. Nie miałoby to miejsca, na przykład, gdybyśmy zamiast tego wyciągnęli obwiednię:


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
![](images/Right_arrow.png) [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Python Code](Category_Python Code.md) > Manual:Creating and manipulating geometry/pl
