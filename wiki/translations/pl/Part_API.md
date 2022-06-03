# Part API/pl
{{VeryImportantMessage
|''(listopad 2018 r.)'' Informacje te mogą być niekompletne i nieaktualne. Najnowsze API - patrz [https   *//www.freecadweb.org/api dokumentacja API generowana automatycznie].}}

Moduł Część jest bezpośrednim połączeniem pomiędzy programem FreeCAD a jądrem OpenCasCade. Dostarcza on głównie [kształty topologiczne](TopoShape_API/pl.md), który jest głównym typem obiektu używanym przez OpenCascade. Moduł Część zawiera również wiele funkcji ułatwiających tworzenie i manipulowanie kształtami topologicznymi. Przykład   * 
```python
import Part
mycube = Part.makeBox(2,2,2)
Part.show(mycube)
```


{{APIFunction|__fromPythonOCC__|OCC.Object|Metoda pomocnicza konwersji kształtu pythonocc do kształtu wewnętrznego|A Part.Shape}}


{{APIFunction|__sortEdges__|list of edges|Metoda pomocnicza sortująca nieposortowaną listę krawędzi w taki sposób, aby po jej zakończeniu wierzchołki początkowy i końcowy dwóch kolejnych krawędzi były geometrycznie zbieżne. Zwraca ona pojedynczą listę krawędzi, a algorytm zatrzymuje się po pierwszym zestawie połączonych krawędzi, co oznacza, że lista wyjściowa może być mniejsza od wejściowej. Posortowana lista może być użyta do stworzenia linii łamanej.|a list of edges}}


{{APIFunction|__toPythonOCC__|Part.Shape|Metoda pomocnicza konwersji wewnętrznego kształtu do kształtu pythonocc|an OCC.Shape}}


{{APIFunction|cast_to_shape|Part.Shape|rzutowanie na rzeczywisty typ kształtu| }}


{{APIFunction|export|list,string|Eksportuj listę obiektów do jednego pliku.| }}


{{APIFunction|getSortedClusters|list of edges|Metoda pomocnicza do sortowania i grupowania różnych krawędzi| }}


{{APIFunction|insert|string,string|Wstaw plik ''(ścieżka podana jako pierwszy argument)'' do podanego dokumentu ''(drugi argument)''.| }}


{{APIFunction|makeBox|length,width,height,[pnt,dir]|Tworzy pudełko znajdujące się w pnt o wymiarach ''(długość,szerokość,wysokość)''. Domyślnie pnt jest wektorem (0,0,0), a dir wektorem (0,0,1).|the created shape}}


{{APIFunction|makeCircle|radius,[pnt,dir,angle1,angle2]|Tworzy okrąg o zadanym promieniu. Domyślnie pnt jest wektorem (0,0,0), dir jest wektorem (0,0,1), angle1 jest równy 0, a angle2 jest równy 360.|the created shape}}


{{APIFunction|makeCompound|list|Tworzy obiekt złożony z listy kształtów.|the created shape}}


{{APIFunction|makeCone|radius1,radius2,height,[pnt,dir,angle]|Tworzy stożek o zadanych promieniach i wysokościach. Domyślnie pnt jest wektorem (0,0,0), dir jest wektorem (0,0,1), a angle wynosi 360.|the created shape}}


{{APIFunction|makeCylinder|radius,height,[pnt,dir,angle]|Tworzy walec o zadanym promieniu i wysokości. Domyślnie pnt jest wektorem (0,0,0), dir jest wektorem (0,0,1), a angle wynosi 360.|the created shape}}


{{APIFunction|makeHelix|pitch,height,radius,[angle,lefthand,heightstyle]|Tworzy kształt spirali o zadanym skoku, wysokości i promieniu. Domyślnie jest to spirala cylindryczna prawoskrętna. Niezerowy parametr angle tworzy spiralę stożkową.  Lefthand True tworzy spiralę lewoskrętną.  Heightstyle ma zastosowanie tylko do helis stożkowych. Heightstyle {{False}} ''(domyślnie)'' spowoduje, że parametr height będzie interpretowany jako długość boku bazowego frustum.  Heightstyle {{True}} spowoduje, że parametr height będzie interpretowany jako pionowa wysokość helisy.  Pitch jest "metrycznym skokiem" ''(wyprzedzenie/obrót)''. Dla helisy stożkowej, radius jest promieniem mniejszym.|the created shape}}


{{APIFunction|makeLine|(x1,y1,z1),(x2,y2,z2)|Makes a line of two points|the created shape}}


{{APIFunction|makeLoft|shapelist<profiles>,[boolean<solid>,boolean<ruled>]|Tworzy wyciągnięty kształt używając listy profili. Opcjonalnie uczyń wynik bryłą ''(vs powierzchnia/powłoka)'' lub uczyń wynik powierzchnią obrobioną.|the created shape}}


{{APIFunction|makePlane|length,width,[pnt,dir]|Tworzy płaszczyznę. Domyślnie pnt jest wektorem (0,0,0) a dir jest wektorem (0,0,1).|the created shape}}


{{APIFunction|makePolygon|list|Tworzy wielokąt z listy wektorów|the created shape}}


{{APIFunction|makeRevolution|Curve,[vmin,vmax,angle,pnt,dir]|Tworzy obrócony kształt przez obrót krzywej lub jej części wokół osi określonej przez ''(pnt,dir)''. Domyślnie vmin/vmax są ustawione na granice krzywej, kąt wynosi 360, pnt jest wektorem (0,0,0), a dir jest wektorem (0,0,1).|the created shape}}


{{APIFunction|makeRuledSurface|Edge or Wire,Edge or Wire|Tworzy powierzchnię obrysowaną z dwóch krawędzi lub linii łamanych. Jeśli używane są linie łamane, to muszą one mieć taką samą liczbę krawędzi.|the created shape}}


{{APIFunction|makeShell|list|Tworzy powłokę z listy ścian.    Uwaga   * Wynikowa powłoka powinna być foremna.   Powłoki inne niż foremne nie są dobrze obsługiwane.|the created shape}}


{{APIFunction|makeSolid|Part.Shape|Tworzy bryłę z powłok wewnątrz kształtu.|the created shape}}


{{APIFunction|makeSphere|radius,[center_pnt, axis_dir, V_startAngle, V_endAngle, U_angle]|Tworzy sferę ''(lub częściową sferę)'' o zadanym promieniu. Domyślnie center_pnt jest wektorem (0,0,0), axis_dir jest wektorem (0,0,1), V_startAngle jest równe 0, V_endAngle jest równe 90, a U_angle jest równe 360.|the created shape}}


{{APIFunction|makeTorus|radius1,radius2,[pnt,dir,angle1,angle2,angle]|Tworzy torus o zadanych promieniach i kątach. Domyślnie pnt jest wektorem (0,0,0),dir jest wektorem (0,0,1),angle1 jest 0,angle2 jest 360 i angle jest 360.|the created shape}}


{{APIFunction|makeTube|edge,float|Tworzy rurę.|the created shape}}


{{APIFunction|open|string|Tworzy nowy dokument i wczytuje plik do dokumentu.| }}


{{APIFunction|read|string|Wczytuje plik i zwraca kształt.|a shape}}


{{APIFunction|show|shape|Dodaje kształt do aktywnego dokumentu lub tworzy go, jeśli dokument nie istnieje.| }}


 

[Category   *API](Category_API.md) [Category   *Poweruser Documentation](Category_Poweruser_Documentation.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [API](Category_API.md) > [Poweruser Documentation](Category_Poweruser Documentation.md) > [Part](Part_Workbench.md) > Part API/pl
