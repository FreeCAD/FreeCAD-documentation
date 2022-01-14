# Topological data scripting/pl
{{TOCright}}

## Wprowadzenie

Tutaj wyjaśnimy Ci jak kontrolować środowisko [Część](Part_Workbench/pl.md) bezpośrednio z interpretera FreeCAD Python, lub z dowolnego zewnętrznego skryptu. Przejrzyj sekcję [ o skryptach](Power_users_hub/pl.md) oraz strony [Podstawy tworzenia skryptów FreeCAD](FreeCAD_Scripting_Basics/pl.md), jeśli potrzebujesz więcej informacji na temat działania skryptów Pythona w FreeCAD. Jeśli jesteś początkującym użytkownikiem środowiska Python, dobrze jest najpierw przeczytać [Wprowadzenie do środowiska Python](Introduction_to_Python/pl.md).

## Zobacz również 

-   [Skrypty w środowisku Część](Part_scripting/pl.md)
-   [OpenCASCADE](OpenCASCADE/pl.md)

## Schemat klas 

To jest [Unified Modeling Language *(UML)*](http://en.wikipedia.org/wiki/Unified_Modeling_Language) przegląd najważniejszych klas modułu Część: ![klasy Python, modułu Część](images/Part_Classes.jpg ) {{Top}}

### Geometria

Obiekty geometryczne są elementami składowymi wszystkich obiektów topologicznych:

-   **Geom** Klasa bazowa obiektów geometrycznych.
-   **Linia** Linia prosta w przestrzeni 3D, zdefiniowana przez punkt początkowy i punkt końcowy.
-   **Okrąg** Okrąg lub odcinek okręgu zdefiniowany przez punkt środkowy oraz punkt początkowy i końcowy.
-   I tak dalej.


{{Top}}

### Topologia

Dostępne są następujące typy danych topologicznych:

-   **Złożenie** Grupa obiektów topologicznych dowolnego typu.
-   **Bryła złożona** Bryła złożona to zbiór brył połączonych ścianami. Rozszerza pojęcia WIRE i SHELL na bryły.
-   **Bryła** Część przestrzeni ograniczona powłokami. Jest trójwymiarowa.
-   **Powłoka** Zbiór ścian połączonych krawędziami. Powłoka może być otwarta lub zamknięta.
-   **Ścina** W 2D jest częścią płaszczyzny, w 3D jest częścią powierzchni. Jego geometria jest ograniczona *(przycięta)* przez kontury. Jest dwuwymiarowa.
-   **Linia łamana** *(polilinia)* Zbiór krawędzi połączonych wierzchołkami. Może to być kontur otwarty lub zamknięty, w zależności od tego, czy krawędzie są połączone, czy nie.
-   **Krawędź** Element topologiczny odpowiadający krzywej ograniczonej. Krawędź jest na ogół ograniczona wierzchołkami. Ma jeden wymiar.
-   **Wierzchołek** Element topologiczny odpowiadający punktowi. Ma zero wymiarów.
-   **Kształt** Termin ogólny obejmujący wszystkie powyższe.


{{Top}}

## Przykład: Utwórz prostą topologię 

![Linia łamana](images/Wire.png )

Stworzymy teraz topologię poprzez skonstruowanie jej z prostszej geometrii. Jako studium przypadku użyjemy części widocznej na rysunku, która składa się z czterech wierzchołków, dwóch łuków i dwóch linii. {{Top}}

### Tworzenie geometrii 

Najpierw tworzymy odrębne części geometryczne tej linii łamanej. Upewniamy się, że części, które mają być później połączone, mają wspólne wierzchołki.

Więc najpierw tworzymy punkty:


```python
import Part
from FreeCAD import Base
V1 = Base.Vector(0, 10, 0)
V2 = Base.Vector(30, 10, 0)
V3 = Base.Vector(30, -10, 0)
V4 = Base.Vector(0, -10, 0)
```


{{Top}}

### Łuk

![Okrąg](images/Circel.png )

Dla każdego łuku potrzebujemy punktu pomocniczego:


```python
VC1 = Base.Vector(-10, 0, 0)
C1 = Part.Arc(V1, VC1, V4)
VC2 = Base.Vector(40, 0, 0)
C2 = Part.Arc(V2, VC2, V3)
```


{{Top}}

### Linia

![Linia](images/Line.png )

Odcinki linii można utworzyć z dwóch punktów:


```python
L1 = Part.LineSegment(V1, V2)
L2 = Part.LineSegment(V3, V4)
```


{{Top}}

### Połącz wszystko w całość 

Ostatnim krokiem jest zestawienie geometrycznych elementów bazowych razem i uzyskanie kształtu topologicznego:


```python
S1 = Part.Shape([C1, L1, C2, L2])
```


{{Top}}

### Utwórz graniastosłup 

Teraz wyciągnij linę łamaną w odpowiednim kierunku i stwórz rzeczywisty kształt 3D:


```python
W = Part.Wire(S1.Edges)
P = W.extrude(Base.Vector(0, 0, 10))
```


{{Top}}

### Pokaż to wszystko 


```python
Part.show(P)
```


{{Top}}

## Utwórz podstawowe kształty 

Możesz łatwo tworzyć podstawowe obiekty topologiczne za pomocą metod `make...()` z modułu Część:


```python
b = Part.makeBox(100, 100, 100)
Part.show(b)
```

Niektóre dostępne metody `make...()`:

-    `makeBox(l, w, h, [p, d])`Tworzy sześcian znajdujący się w punkcie p i skierowany w kierunku d o wymiarach *(l,w,h)*.

-    `makeCircle(radius)`Tworzy okrąg o zadanym promieniu.

-    `makeCone(radius1, radius2, height)`. Tworzy stożek o podanych promieniach i wysokościach.

-    `makeCylinder(radius, height)`. Tworzy walec o zadanym promieniu i wysokości.

-    `makeLine((x1, y1, z1), (x2, y2, z2))`Tworzy prostą z dwóch punktów.

-    `makePlane(length, width)`Tworzy płaszczyznę o określonej długości i szerokości.

-    `makePolygon(list)``makePolygon(list)` Tworzy wielokąt z listy punktów.

-    `makeSphere(radius)`Tworzy sferę o zadanym promieniu.

-    `makeTorus(radius1, radius2)`Tworzy torus o podanych promieniach.

Zobacz stronę [skrypty środowiska Część](Part_API/pl.md) aby zobaczyć pełną listę dostępnych metod modułu Część. {{Top}}

## Import modułów 

Najpierw musimy zaimportować moduł Część, abyśmy mogli korzystać z jego zawartości w środowisku Python. Zaimportujemy również moduł Base z wnętrza modułu FreeCAD:


```python
import Part
from FreeCAD import Base
```


{{Top}}

### Utwórz wektor 

[Wektory](http://en.wikipedia.org/wiki/Euclidean_vector) są jedną z najważniejszych informacji przy tworzeniu kształtów. Zazwyczaj zawierają trzy liczby *(ale niekoniecznie zawsze)*: współrzędne kartezjańskie X, Y i Z. Tworzysz wektor w ten sposób:


```python
myVector = Base.Vector(3, 2, 0)
```

Właśnie utworzyliśmy wektor o współrzędnych X = 3, Y = 2, Z = 0. W module Part, wektory są używane wszędzie. Kształty części używają również innego rodzaju reprezentacji punktów zwanej Vertex, która jest po prostu kontenerem dla wektora. Dostęp do wektora wierzchołka uzyskujesz w następujący sposób:


```python
myVertex = myShape.Vertexes[0]
print(myVertex.Point)
> Vector (3, 2, 0)
```


{{Top}}

### Utwórz krawędź 

Krawędź to nic innego jak linia z dwoma wierzchołkami:


```python
edge = Part.makeLine((0, 0, 0), (10, 0, 0))
edge.Vertexes
> [<Vertex object at 01877430>, <Vertex object at 014888E0>]
```

Uwaga: Możesz również utworzyć krawędź poprzez przekazanie dwóch wektorów:


```python
vec1 = Base.Vector(0, 0, 0)
vec2 = Base.Vector(10, 0, 0)
line = Part.LineSegment(vec1, vec2)
edge = line.toShape()
```

Możesz znaleźć długość i środek krawędzi w ten sposób:


```python
edge.Length
> 10.0
edge.CenterOfMass
> Vector (5, 0, 0)
```


{{Top}}

### Wyświetl kształt na ekranie 

Do tej pory utworzyliśmy obiekt krawędziowy, ale nie pojawia się on nigdzie na ekranie. Dzieje się tak dlatego, że scena 3D FreeCAD wyświetla tylko to, co każesz jej wyświetlić. Aby to zrobić, użyjemy prostej metody:


```python
Part.show(edge)
```

Funkcja show tworzy obiekt w naszym dokumencie FreeCAD i przypisuje mu nasz kształt \"krawędzi\". Używaj jej zawsze wtedy, gdy chcesz wyświetlić swoje dzieło na ekranie. {{Top}}

### Utwórz linie łamaną 

Linia łamana jest linią o wielu krawędziach i może być utworzona z listy krawędzi lub nawet z listy linii łamanych:


```python
edge1 = Part.makeLine((0, 0, 0), (10, 0, 0))
edge2 = Part.makeLine((10, 0, 0), (10, 10, 0))
wire1 = Part.Wire([edge1, edge2]) 
edge3 = Part.makeLine((10, 10, 0), (0, 10, 0))
edge4 = Part.makeLine((0, 10, 0), (0, 0, 0))
wire2 = Part.Wire([edge3, edge4])
wire3 = Part.Wire([wire1, wire2])
wire3.Edges
> [<Edge object at 016695F8>, <Edge object at 0197AED8>, <Edge object at 01828B20>, <Edge object at 0190A788>]
Part.show(wire3)
```


`Part.show(wire3)`

wyświetli 4 krawędzie, z których składa się nasza linia łamana. Inne przydatne informacje mogą być łatwo pobrane:


```python
wire3.Length
> 40.0
wire3.CenterOfMass
> Vector (5, 5, 0)
wire3.isClosed()
> True
wire2.isClosed()
> False
```


{{Top}}

### Utwórz ścianę 

Tylko ściany utworzone z linii łamanych będą poprawne. W tym przykładzie linia łamana3 jest zamknięta, ale linia łamana2 nie jest *(patrz wyżej)*:


```python
face = Part.Face(wire3)
face.Area
> 99.99999999999999
face.CenterOfMass
> Vector (5, 5, 0)
face.Length
> 40.0
face.isValid()
> True
sface = Part.Face(wire2)
sface.isValid()
> False
```

Tylko twarze będą posiadać obszar, linie łamane i krawędzie nie. {{Top}}

### Utwórz okrąg 

Okrąg może być utworzony w ten sposób:


```python
circle = Part.makeCircle(10)
circle.Curve
> Circle (Radius : 10, Position : (0, 0, 0), Direction : (0, 0, 1))
```

Jeśli chcesz utworzyć go w określonej pozycji i z określonym kierunkiem:


```python
ccircle = Part.makeCircle(10, Base.Vector(10, 0, 0), Base.Vector(1, 0, 0))
ccircle.Curve
> Circle (Radius : 10, Position : (10, 0, 0), Direction : (1, 0, 0))
```

okrąg zostanie utworzony w odległości 10 od początku X i będzie skierowany na zewnątrz wzdłuż osi X. Uwaga: `makeCircle()` akceptuje tylko `Base.Vector()` dla parametrów position i parametry jako wektory normalne, a nie krotki. Możesz również utworzyć część okręgu przez podanie kąta początkowego i końcowego:


```python
from math import pi
arc1 = Part.makeCircle(10, Base.Vector(0, 0, 0), Base.Vector(0, 0, 1), 0, 180)
arc2 = Part.makeCircle(10, Base.Vector(0, 0, 0), Base.Vector(0, 0, 1), 180, 360)
```

Kąty powinny być podane w stopniach. Jeśli masz radiany, po prostu przekonwertuj je za pomocą wzoru: `degrees <nowiki>=</nowiki> radians * 180/pi` lub za pomocą modułu `math` Pythona:


```python
import math
degrees = math.degrees(radians)
```


{{Top}}

### Utwórz łuk wzdłuż punktów 

Niestety nie ma funkcji `makeArc()`, ale mamy funkcję `Part.Arc()` do tworzenia łuku przez trzy punkty. Tworzy ona obiekt łuku łączący punkt początkowy z punktem końcowym przez punkt środkowy. Funkcja `toShape()` obiektu arc musi zostać wywołana, aby otrzymać obiekt krawędzi, tak samo jak w przypadku użycia `Part.LineSegment` zamiast `Part.makeLine`.


```python
arc = Part.Arc(Base.Vector(0, 0, 0), Base.Vector(0, 5, 0), Base.Vector(5, 5, 0))
arc
> <Arc object>
arc_edge = arc.toShape()
Part.show(arc_edge)
```

Funkcja `Arc()` akceptuje tylko `Base.Vector()` dla punktów, a nie dla krotek. Możesz również uzyskać łuk używając części okręgu:


```python
from math import pi
circle = Part.Circle(Base.Vector(0, 0, 0), Base.Vector(0, 0, 1), 10)
arc = Part.Arc(circle,0,pi)
```

Łuki są poprawnymi krawędziami, tak jak linie, więc mogą być również używane w poliliniach. {{Top}}

### Utwórz wielokąt 

Wielokąt jest po prostu polilinią o wielu prostych krawędziach. Funkcja `makePolygon()` przyjmuje listę punktów i tworzy polilinię przechodzącą przez te punkty:


```python
lshape_wire = Part.makePolygon([Base.Vector(0, 5, 0), Base.Vector(0, 0, 0), Base.Vector(5, 0, 0)])
```


{{Top}}

### Utwórz krzywą Béziera 

Krzywe Béziera są używane do modelowania gładkich krzywych przy użyciu serii biegunów *(punktów)* i opcjonalnych wag. Poniższa funkcja tworzy krzywą `Part.BezierCurve()` z serii punktów `FreeCAD.Vector()`. Uwaga: przy \"pobieraniu\" i \"ustawianiu\" pojedynczego bieguna lub wagi, indeksy zaczynają się od 1, a nie od 0.


```python
def makeBCurveEdge(Points):
   geomCurve = Part.BezierCurve()
   geomCurve.setPoles(Points)
   edge = Part.Edge(geomCurve)
   return(edge)
```


{{Top}}

### Utwórz płaszczyznę 

Płaszczyzna jest płaską prostokątną powierzchnią. Metoda używana do jej utworzenia to `makePlane(length, width, [start_pnt, dir_normal])`. Domyślnie start\_pnt = Vector(0, 0, 0) i dir\_normal = Vector(0, 0, 1). Użycie dir\_normal = Vector(0, 0, 1) spowoduje utworzenie płaszczyzny zwróconej w dodatnim kierunku osi Z, natomiast dir\_normal = Vector(1, 0, 0) utworzy płaszczyznę zwróconą w dodatnim kierunku osi X:


```python
plane = Part.makePlane(2, 2)
plane
> <Face object at 028AF990>
plane = Part.makePlane(2, 2, Base.Vector(3, 0, 0), Base.Vector(0, 1, 0))
plane.BoundBox
> BoundBox (3, 0, 0, 5, 0, 2)
```


`BoundBox`

jest prostopadłościanem zamykającym płaszczyznę o przekątnej zaczynającej się w punkcie (3, 0, 0) i kończącej w punkcie (5, 0, 2). W tym przypadku grubość `BoundBox` wzdłuż osi Y wynosi zero, ponieważ nasz kształt jest całkowicie płaski.

Uwaga: `makePlane()` akceptuje tylko `Base.Vector()` dla start\_pnt i dir\_normal, a nie krotki. {{Top}}

### Utwórz elipsę 

Istnieje kilka sposobów na utworzenie elipsy:


```python
Part.Ellipse()
```

Tworzy elipsę o wartości promienia głównego 2 i promienia mniejszego 1, o środku w punkcie (0, 0, 0).


```python
Part.Ellipse(Ellipse)
```

Tworzy kopię podanej elipsy.


```python
Part.Ellipse(S1, S2, Center)
```

Tworzy elipsę wyśrodkowaną w punkcie Center, gdzie płaszczyzna elipsy jest określona przez Center, S1 i S2, jej oś główna jest określona przez Center i S1, jej promień główny jest odległością pomiędzy Center i S1, a jej promień mniejszy jest odległością pomiędzy S2 i osią główną.


```python
Part.Ellipse(Center, MajorRadius, MinorRadius)
```

Tworzy elipsę o promieniach MajorRadius i MinorRadius, znajdującą się w płaszczyźnie zdefiniowanej przez środek i normalną (0, 0, 1).


```python
eli = Part.Ellipse(Base.Vector(10, 0, 0), Base.Vector(0, 5, 0), Base.Vector(0, 0, 0))
Part.show(eli.toShape())
```

W powyższym kodzie przekazaliśmy S1, S2 i środek. Podobnie jak `Arc`, `Ellipse` tworzy obiekt elipsy, a nie krawędzi, więc musimy go przekonwertować na krawędź używając `toShape()` do wyświetlenia.

Uwaga: `Ellipse()` akceptuje tylko `Base.Vector()` dla punktów, a nie dla krotek.


```python
eli = Part.Ellipse(Base.Vector(0, 0, 0), 10, 5)
Part.show(eli.toShape())
```

Dla powyższego konstruktora elipsy przekazaliśmy center, MajorRadius oraz MinorRadius. {{Top}}

### Utwórz torusa 

Używając `makeTorus(radius1, radius2, [pnt, dir, angle1, angle2, angle])`. Domyślnie pnt = Vector(0, 0, 0), dir = Vector(0, 0, 1), angle1 = 0, angle2 = 360 i angle = 360. Rozważmy torus jako małe koło, które porusza się po dużym okręgu. Radius1 jest promieniem dużego okręgu, radius2 jest promieniem małego okręgu, pnt jest środkiem torusa, a dir jest kierunkiem normalnej. angle1 i angle2 są kątami w stopniach dla małego okręgu; ostatni parametr angle jest po to, by zrobić przekrój torusa:


```python
torus = Part.makeTorus(10, 2)
```

Powyższy kod utworzy torus o średnicy {{Value|20}} *(promień 10)* i grubości {{Value|4}} *(promień małego okręgu 2)*


```python
tor=Part.makeTorus(10, 5, Base.Vector(0, 0, 0), Base.Vector(0, 0, 1), 0, 180)
```

Powyższy kod utworzy wycinek torusa.


```python
tor=Part.makeTorus(10, 5, Base.Vector(0, 0, 0), Base.Vector(0, 0, 1), 0, 360, 180)
```

Powyższy kod utworzy połowę torusa; tylko ostatni parametr jest zmieniony, tzn. pozostałe kąty są domyślne. Nadanie kąta 180 spowoduje utworzenie torusa od 0 do 180, czyli jego połowę. {{Top}}

### Utwórz sześcian lub prostopadłościan 

Przy użyciu `makeBox(length, width, height, [pnt, dir])`. Domyślnie pnt = Vector(0, 0, 0) i dir = Vector(0, 0, 1).


```python
box = Part.makeBox(10, 10, 10)
len(box.Vertexes)
> 8
```


{{Top}}

### Utwórz sferę 

Przy użyciu `makeSphere(radius, [pnt, dir, angle1, angle2, angle3])`. Domyślnie pnt = Vector(0, 0, 0), dir = Vector(0, 0, 1), angle1 = -90, angle2 = 90 i angle3 = 360. Kąt1 i kąt2 to pionowe minimum i maksimum sfery, kąt3 to średnica sfery.


```python
sphere = Part.makeSphere(10)
hemisphere = Part.makeSphere(10, Base.Vector(0, 0, 0), Base.Vector(0, 0, 1), -90, 90, 180)
```


{{Top}}

### Utwórz walec 

Przy użyciu `makeCylinder(radius, height, [pnt, dir, angle])`. Domyślnie pnt = Vector(0, 0, 0), dir = Vector(0, 0, 1) i angle = 360. 
```python
cylinder = Part.makeCylinder(5, 20)
partCylinder = Part.makeCylinder(5, 20, Base.Vector(20, 0, 0), Base.Vector(0, 0, 1), 180)
```{{Top}}

### Utwórz stożek 

Przy użyciu `makeCone(radius1, radius2, height, [pnt, dir, angle])`. Domyślnie pnt = Vector(0, 0, 0), dir = Vector(0, 0, 1) i angle = 360. 
```python
cone = Part.makeCone(10, 0, 20)
semicone = Part.makeCone(10, 0, 20, Base.Vector(20, 0, 0), Base.Vector(0, 0, 1), 180)
```{{Top}}

## Modyfikuj kształty 

Kształty można modyfikować na kilka sposobów. Niektóre z nich to proste operacje przekształcania, takie jak przesuwanie lub obracanie kształtów, inne są bardziej złożone, np. łączenie i odejmowanie jednego kształtu od drugiego. {{Top}}

## Operacje przekształcenia 

### Przekształcanie kształtu 

Przesunięcie to czynność polegająca na przeniesieniu kształtu z jednego miejsca w drugie. Każdy kształt *(krawędź, ściana, sześcian, itd\...)* może być przesunięty w ten sam sposób: 
```python
myShape = Part.makeBox(2, 2, 2)
myShape.translate(Base.Vector(2, 0, 0))
``` Spowoduje to przesunięcie naszego kształtu \"myShape\" o 2 jednostki w kierunku X. {{Top}}

### Obrót kształtu 

Aby obrócić kształt, należy określić środek obrotu, oś i kąt obrotu: 
```python
myShape.rotate(Base.Vector(0, 0, 0),Base.Vector(0, 0, 1), 180)
``` Powyższy kod obróci kształt o 180 stopni wokół osi Z. {{Top}}

### Przekształcenia macierzowe 

Macierz jest bardzo wygodnym sposobem przechowywania przekształceń w świecie 3D. W pojedynczej macierzy można ustawić wartości przesunięcia, obrotu i skalowania, które mają być zastosowane do obiektu. Na przykład: 
```python
myMat = Base.Matrix()
myMat.move(Base.Vector(2, 0, 0))
myMat.rotateZ(math.pi/2)
``` Uwaga: Macierze FreeCAD działają w radianach. Ponadto, prawie wszystkie operacje na macierzach, które przyjmują wektor, mogą również przyjmować trzy liczby, więc te dwie linie robią to samo: 
```python
myMat.move(2, 0, 0)
myMat.move(Base.Vector(2, 0, 0))
``` Kiedy nasza macierz jest już ustalona, możemy ją zastosować do naszego kształtu. FreeCAD udostępnia dwie metody, aby to zrobić: `transformShape()` oraz `transformGeometry()`. Różnica jest taka, że w przypadku pierwszej z nich mamy pewność, że nie wystąpią żadne deformacje *(patrz poniżej [Skalowanie kształtu](#Skalowanie_kszta.C5.82tu.md))*. Naszą transformację możemy zastosować w ten sposób: 
```python
myShape.transformShape(myMat)
``` lub 
```python
myShape.transformGeometry(myMat)
```{{Top}}

### Skalowanie kształtu 

Skalowanie kształtu jest bardziej niebezpieczną operacją, ponieważ w przeciwieństwie do przesunięcia czy obrotu, skalowanie nierównomierne *(z różnymi wartościami dla X, Y i Z)* może zmienić strukturę kształtu. Na przykład, skalowanie koła z większą wartością w poziomie niż w pionie przekształci je w elipsę, która zachowuje się matematycznie zupełnie inaczej. Do skalowania nie możemy użyć metody `transformShape()`, musimy użyć `transformGeometry()`: 
```python
myMat = Base.Matrix()
myMat.scale(2, 1, 1)
myShape=myShape.transformGeometry(myMat)
```{{Top}}

## Operacje logiczne 

### Operacja odjęcia 

Odejmowanie kształtu od innego nazywane jest w FreeCAD \"cięciem\" i odbywa się w następujący sposób: 
```python
cylinder = Part.makeCylinder(3, 10, Base.Vector(0, 0, 0), Base.Vector(1, 0, 0))
sphere = Part.makeSphere(5, Base.Vector(5, 0, 0))
diff = cylinder.cut(sphere)
```{{Top}}

### Przecięcie

W ten sam sposób przecięcie dwóch kształtów nazywane jest \"częścią wspólną\" i jest wykonywane w ten sposób: 
```python
cylinder1 = Part.makeCylinder(3, 10, Base.Vector(0, 0, 0), Base.Vector(1, 0, 0))
cylinder2 = Part.makeCylinder(3, 10, Base.Vector(5, 0, -5), Base.Vector(0, 0, 1))
common = cylinder1.common(cylinder2)
```{{Top}}

### Połączenie

Połączenie nazywa się \"scaleniem\" i działa w ten sam sposób: 
```python
cylinder1 = Part.makeCylinder(3, 10, Base.Vector(0, 0, 0), Base.Vector(1, 0, 0))
cylinder2 = Part.makeCylinder(3, 10, Base.Vector(5, 0, -5), Base.Vector(0, 0, 1))
fuse = cylinder1.fuse(cylinder2)
```{{Top}}

### Przekrój

\"Przekrój\" jest punktem przecięcia bryły z płaszczyzną. Zwraca krzywą przecięcia, krzywą złożoną utworzoną z krawędzi. 
```python
cylinder1 = Part.makeCylinder(3, 10, Base.Vector(0, 0, 0), Base.Vector(1, 0, 0))
cylinder2 = Part.makeCylinder(3, 10, Base.Vector(5, 0, -5), Base.Vector(0, 0, 1))
section = cylinder1.section(cylinder2)
section.Wires
> []
section.Edges
> [<Edge object at 0D87CFE8>, <Edge object at 019564F8>, <Edge object at 0D998458>, 
 <Edge  object at 0D86DE18>, <Edge object at 0D9B8E80>, <Edge object at 012A3640>, 
 <Edge object at 0D8F4BB0>]
```{{Top}}

### Wyciąganie

Wyciąganie to czynność \"wypychania\" płaskiego kształtu w określonym kierunku, w wyniku czego powstaje pełna bryła. Pomyśl o kole, które staje się rurką poprzez \"wypychanie\" go na zewnątrz: 
```python
circle = Part.makeCircle(10)
tube = circle.extrude(Base.Vector(0, 0, 2))
``` Jeśli twój okrąg jest pusty, otrzymasz pustą rurkę. Jeśli twój okrąg jest w rzeczywistości dyskiem z wypełnioną powierzchnią, otrzymasz pełny walec: 
```python
wire = Part.Wire(circle)
disc = Part.Face(wire)
cylinder = disc.extrude(Base.Vector(0, 0, 2))
```{{Top}}

## Badanie kształtów 

Możesz łatwo zbadać topologiczną strukturę danych: 
```python
import Part
b = Part.makeBox(100, 100, 100)
b.Wires
w = b.Wires[0]
w
w.Wires
w.Vertexes
Part.show(w)
w.Edges
e = w.Edges[0]
e.Vertexes
v = e.Vertexes[0]
v.Point
``` Wpisując powyższe linie w interpreterze Python, uzyskasz dobre zrozumienie struktury obiektów Część. Tutaj, nasze polecenie `makeBox()` utworzyło bryłę. Ta bryła, jak wszystkie bryły typu Część, zawiera ściany. Ściany zawsze zawierają linie łamane *(polilinie)*, które są listą krawędzi ograniczających daną ścianę. Każda ściana ma co najmniej jedną zamkniętą linię łamaną *(może mieć ich więcej, jeśli posiada otwór)*. W liniach łamanych możemy oglądać każdą krawędź z osobna, a wewnątrz każdej krawędzi możemy zobaczyć wierzchołki. Proste krawędzie mają oczywiście tylko dwa wierzchołki. {{Top}}

### Analiza krawędzi 

W przypadku krawędzi, która jest arbitralną krzywą, najprawdopodobniej chcesz dokonać dyskretyzacji. W FreeCAD krawędzie są parametryzowane przez ich długości. Oznacza to, że możesz przejść po krawędzi/krzywej przez jej długość: 
```python
import Part
box = Part.makeBox(100, 100, 100)
anEdge = box.Edges[0]
print(anEdge.Length)
``` Teraz możesz uzyskać dostęp do wielu właściwości krawędzi, używając długości jako pozycji. Oznacza to, że jeśli krawędź ma długość 100mm, to pozycja początkowa wynosi 0, a końcowa 100. 
```python
anEdge.tangentAt(0.0)          # tangent direction at the beginning
anEdge.valueAt(0.0)            # Point at the beginning
anEdge.valueAt(100.0)          # Point at the end of the edge
anEdge.derivative1At(50.0)     # first derivative of the curve in the middle
anEdge.derivative2At(50.0)     # second derivative of the curve in the middle
anEdge.derivative3At(50.0)     # third derivative of the curve in the middle
anEdge.centerOfCurvatureAt(50) # center of the curvature for that position
anEdge.curvatureAt(50.0)       # the curvature
anEdge.normalAt(50)            # normal vector at that position (if defined)
```{{Top}}

### Użycie zaznaczenia 

Tutaj widzimy teraz, jak możemy wykorzystać wybór, który użytkownik przeprowadził w przeglądarce. Najpierw tworzymy sześcian i pokazujemy go w przeglądarce. 
```python
import Part
Part.show(Part.makeBox(100, 100, 100))
Gui.SendMsgToActiveView("ViewFit")
``` Teraz wybierz kilka ścian lub krawędzi. Za pomocą tego skryptu możesz przejść po wszystkich zaznaczonych obiektach i ich elementach podrzędnych: 
```python
for o in Gui.Selection.getSelectionEx():
    print(o.ObjectName)
    for s in o.SubElementNames:
        print("name: ", s)
        for s in o.SubObjects:
            print("object: ", s)
``` Wybierz kilka krawędzi, a ten skrypt obliczy ich długość: 
```python
length = 0.0
for o in Gui.Selection.getSelectionEx():
    for s in o.SubObjects:
        length += s.Length

print("Length of the selected edges: ", length)
```{{Top}}

## Przykład: Butelka OCC 

Typowym przykładem, który można znaleźć na stronie [OpenCasCade Technology](https://www.opencascade.com/doc/occt-6.9.0/overview/html/occt__tutorial.html) jest sposób na zbudowanie butelki. Jest to dobre ćwiczenie również dla programu FreeCAD. W rzeczywistości, jeśli będziesz śledził nasz przykład poniżej i stronę OCC jednocześnie, zobaczysz jak dobrze struktury OCC są zaimplementowane w FreeCAD. Skrypt jest dołączony do instalacji FreeCAD *(w folderze {{FileName|Mod/Part}})* i może być wywołany z interpretera Python przez wpisanie: 
```python
import Part
import MakeBottle
bottle = MakeBottle.makeBottle()
Part.show(bottle)
```{{Top}}

### Skrypt

Na potrzeby tego poradnika rozważymy okrojoną wersję skryptu. W tej wersji butelka nie będzie wydrążona, a szyjka butelki nie będzie gwintowana. 
```python
import Part, math
from FreeCAD import Base

def makeBottleTut(myWidth = 50.0, myHeight = 70.0, myThickness = 30.0):
    aPnt1=Base.Vector(-myWidth / 2., 0, 0)
    aPnt2=Base.Vector(-myWidth / 2., -myThickness / 4., 0)
    aPnt3=Base.Vector(0, -myThickness / 2., 0)
    aPnt4=Base.Vector(myWidth / 2., -myThickness / 4., 0)
    aPnt5=Base.Vector(myWidth / 2., 0, 0)

    aArcOfCircle = Part.Arc(aPnt2, aPnt3, aPnt4)
    aSegment1=Part.LineSegment(aPnt1, aPnt2)
    aSegment2=Part.LineSegment(aPnt4, aPnt5)

    aEdge1=aSegment1.toShape()
    aEdge2=aArcOfCircle.toShape()
    aEdge3=aSegment2.toShape()
    aWire=Part.Wire([aEdge1, aEdge2, aEdge3])

    aTrsf=Base.Matrix()
    aTrsf.rotateZ(math.pi) # rotate around the z-axis

    aMirroredWire=aWire.copy()
    aMirroredWire.transformShape(aTrsf)
    myWireProfile=Part.Wire([aWire, aMirroredWire])

    myFaceProfile=Part.Face(myWireProfile)
    aPrismVec=Base.Vector(0, 0, myHeight)
    myBody=myFaceProfile.extrude(aPrismVec)

    myBody=myBody.makeFillet(myThickness / 12.0, myBody.Edges)

    neckLocation=Base.Vector(0, 0, myHeight)
    neckNormal=Base.Vector(0, 0, 1)

    myNeckRadius = myThickness / 4.
    myNeckHeight = myHeight / 10.
    myNeck = Part.makeCylinder(myNeckRadius, myNeckHeight, neckLocation, neckNormal)
    myBody = myBody.fuse(myNeck)

    return myBody

el = makeBottleTut()
Part.show(el)
```{{Top}}

### Szczegółowe objaśnienia 


```python
import Part, math
from FreeCAD import Base
```

Potrzebny nam będzie oczywiście moduł `Part`, ale także moduł `FreeCAD.Base`, który zawiera podstawowe struktury FreeCAD, takie jak wektory i macierze.


```python
def makeBottleTut(myWidth = 50.0, myHeight = 70.0, myThickness = 30.0):
    aPnt1=Base.Vector(-myWidth / 2., 0, 0)
    aPnt2=Base.Vector(-myWidth / 2., -myThickness / 4., 0)
    aPnt3=Base.Vector(0, -myThickness / 2., 0)
    aPnt4=Base.Vector(myWidth / 2., -myThickness / 4., 0)
    aPnt5=Base.Vector(myWidth / 2., 0, 0)
```

Tutaj definiujemy naszą funkcję `makeBottleTut`. Funkcja ta może być wywołana bez argumentów, tak jak zrobiliśmy to powyżej, w tym przypadku zostaną użyte domyślne wartości dla szerokości, wysokości i grubości. Następnie definiujemy kilka punktów, które zostaną użyte do budowy naszego profilu bazowego.


```python
    ...
    aArcOfCircle = Part.Arc(aPnt2, aPnt3, aPnt4)
    aSegment1=Part.LineSegment(aPnt1, aPnt2)
    aSegment2=Part.LineSegment(aPnt4, aPnt5)
```

Tutaj definiujemy geometrię: łuk, złożony z trzech punktów, oraz dwa odcinki linii, złożone z dwóch punktów.


```python
    ...
    aEdge1=aSegment1.toShape()
    aEdge2=aArcOfCircle.toShape()
    aEdge3=aSegment2.toShape()
    aWire=Part.Wire([aEdge1, aEdge2, aEdge3])
```

Pamiętasz różnicę między geometrią a kształtami? Tutaj budujemy kształty z naszej geometrii konstrukcyjnej. Trzy krawędzie *(krawędzie mogą być proste lub zakrzywione)*, następnie linia łamana wykonana z tych trzech krawędzi.


```python
    ...
    aTrsf=Base.Matrix()
    aTrsf.rotateZ(math.pi) # rotate around the z-axis

    aMirroredWire=aWire.copy()
    aMirroredWire.transformShape(aTrsf)
    myWireProfile=Part.Wire([aWire, aMirroredWire])
```

Do tej pory zbudowaliśmy tylko połowę profilu. Zamiast budować cały profil w ten sam sposób, możemy po prostu zrobić lustrzane odbicie tego, co zrobiliśmy i skleić obie połówki. Najpierw utworzymy macierz. Macierz jest bardzo popularnym sposobem na zastosowanie transformacji do obiektów w świecie 3D, ponieważ może ona zawierać w jednej strukturze wszystkie podstawowe transformacje, jakim mogą podlegać obiekty 3D (przesuwanie, obracanie i skalowanie). Po utworzeniu macierzy odbijamy ją w lustrze, następnie tworzymy kopię naszej linii łamanej i nakładamy na nią macierz transformacji. Mamy teraz już dwie linie, z których możemy utworzyć trzecią, gdyż linie to tak naprawdę listy krawędzi.


```python
    ...
    myFaceProfile=Part.Face(myWireProfile)
    aPrismVec=Base.Vector(0, 0, myHeight)
    myBody=myFaceProfile.extrude(aPrismVec)

    myBody=myBody.makeFillet(myThickness / 12.0, myBody.Edges)
```

Teraz, gdy mamy już zamkniętą linię łamaną, można ją przekształcić w ścianę. Gdy mamy już ścianę, możemy ją wyciągnąć. W ten sposób tworzymy bryłę. Następnie nakładamy na nasz obiekt małe, ładne zaokrąglenie, ponieważ zależy nam na dobrym projekcie, prawda? 
```python
    ...
    neckLocation=Base.Vector(0, 0, myHeight)
    neckNormal=Base.Vector(0, 0, 1)

    myNeckRadius = myThickness / 4.
    myNeckHeight = myHeight / 10.
    myNeck = Part.makeCylinder(myNeckRadius, myNeckHeight, neckLocation, neckNormal)
``` W tym momencie korpus naszej butelki jest już gotowy, ale musimy jeszcze stworzyć szyjkę. Tworzymy więc nową bryłę, z walcem. 
```python
    ...
    myBody = myBody.fuse(myNeck)
``` Obsługa operacji scalenia jest bardzo wydajna. Zajmie się sklejaniem tego, co trzeba skleić i usuwaniem części, które trzeba usunąć. 
```python
    ...
    return myBody
``` Następnie zwracamy naszą bryłę typu Część jako wynik naszej funkcji. 
```python
el = makeBottleTut()
Part.show(el)
``` Na koniec wywołujemy funkcję, aby faktycznie utworzyć część, a następnie uczynić ją widoczną. {{Top}}

## Przykład: Sześcian z otworami 

Oto kompletny przykład budowy sześcianu z otworami.

Konstrukcja jest wykonywana po jednym boku na raz. Kiedy kostka jest gotowa, zostaje wydrążona przez wycięcie w niej walca. 
```python
import Part, math
from FreeCAD import Base

size = 10
poly = Part.makePolygon([(0, 0, 0), (size, 0, 0), (size, 0, size), (0, 0, size), (0, 0, 0)])

face1 = Part.Face(poly)
face2 = Part.Face(poly)
face3 = Part.Face(poly)
face4 = Part.Face(poly)
face5 = Part.Face(poly)
face6 = Part.Face(poly)
     
myMat = Base.Matrix()

myMat.rotateZ(math.pi / 2)
face2.transformShape(myMat)
face2.translate(Base.Vector(size, 0, 0))

myMat.rotateZ(math.pi / 2)
face3.transformShape(myMat)
face3.translate(Base.Vector(size, size, 0))

myMat.rotateZ(math.pi / 2)
face4.transformShape(myMat)
face4.translate(Base.Vector(0, size, 0))

myMat = Base.Matrix()

myMat.rotateX(-math.pi / 2)
face5.transformShape(myMat)

face6.transformShape(myMat)               
face6.translate(Base.Vector(0, 0, size))

myShell = Part.makeShell([face1, face2, face3, face4, face5, face6])   
mySolid = Part.makeSolid(myShell)

myCyl = Part.makeCylinder(2, 20)
myCyl.translate(Base.Vector(size / 2, size / 2, 0))

cut_part = mySolid.cut(myCyl)

Part.show(cut_part)
```{{Top}}

## Wczytywanie i zapisywanie 

Jest kilka sposobów na zapisanie swojej pracy. Możesz oczywiście zapisać swój dokument FreeCAD, ale możesz również zapisać obiekty typu [Część](Part_Workbench/pl.md) bezpośrednio do popularnych formatów CAD, takich jak BREP, IGS, STEP i STL.

Zapisywanie kształtu do pliku jest łatwe. Dla wszystkich obiektów kształtu dostępne są metody `exportBrep()`, `exportIges()`, `exportStep()` oraz `exportStl()`. Tak więc, wykonując: 
```python
import Part
s = Part.makeBox(10, 10, 10)
s.exportStep("test.stp")
``` zapisze naszą kostkę do pliku STEP. Aby wczytać plik BREP, IGES lub STEP: 
```python
import Part
s = Part.Shape()
s.read("test.stp")
``` Aby przekonwertować plik STEP na plik IGS: 
```python
 import Part
 s = Part.Shape()
 s.read("file.stp")       # incoming file igs, stp, stl, brep
 s.exportIges("file.igs") # outbound file igs
```{{Top}}





{{Powerdocnavi

}}

[<img src="images/Property.png" style="width:16px"> Developer Documentation](Category_Developer_Documentation.md) [<img src="images/Property.png" style="width:16px"> Python Code](Category_Python_Code.md)

---
[documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > Topological data scripting/pl
