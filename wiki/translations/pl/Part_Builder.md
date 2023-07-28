---
- GuiCommand:/pl
   Name:Part Shapebuilder
   Name/pl:Część: Konstruktor
   MenuLocation:Część → Konstruktor kształtu ...
   Workbenches:[Część](Part_Workbench/pl.md)
   SeeAlso:[Utwórz geometrie pierwotne](Part_CreatePrimitives/pl.md)
---

# Part Builder/pl



## Opis

Narzędzie to służy do tworzenia bardziej złożonych kształtów z różnych geometrycznych prymitywów parametrycznych.



## Użycie

Narzędzie to może tworzyć następujące obiekty:



### Krawędź z dwóch wierzchołków 

1.  Wybierz dwa wierzchołki
2.  Kliknij na przycisk **Utwórz**

![](images/Edge_from_verts-1.gif )



### Polilinia z krawędzi 

1.  Wybierz zestaw sąsiadujących krawędzi w oknie [widoku 3D](3D_view/pl.md).
2.  kliknij na przycisk **Utwórz**

![](images/Wire_from_edges-1.gif )



### Ściana z wierzchołków 

1.  Wybierz wierzchołki wyznaczające granice ściany w oknie [widoku 3D](3D_view/pl.md).
2.  Wybierz czy ściana ma być planarna
3.  Kliknij na przycisk **Utwórz**
4.  Obiekt zostanie utworzony w oknie [widoku 3D](3D_view/pl.md) i zostanie umieszczony na liście [widoku drzewa](Tree_view/pl.md).



### Ściana z krawędzi 

1.  Wybierz zamknięty zbiór krawędzi wyznaczających granice ściany oknie [widoku 3D](3D_view/pl.md).
2.  Wybierz czy ściana ma być planarna
3.  Kliknij na przycisk **Utwórz**
4.  Obiekt zostanie utworzony w oknie [widoku 3D](3D_view/pl.md) i zostanie umieszczony na liście [widoku drzewa](Tree_view/pl.md).



### Powłoka ze ściany 

1.  Wybierz ściany w oknie [widoku 3D](3D_view/pl.md),
2.  Wybierz czy kształt powinien być udoskonalony,
3.  Wybierz czy wszystkie ściany mają być zawarte w powłoce,
4.  Kliknij na przycisk **Utwórz**,
5.  Obiekt zostanie utworzony w oknie [widoku 3D](3D_view/pl.md) i zostanie umieszczony w [widoku drzewa](Tree_view/pl.md).



### Bryła z powłoki 

1.  Wybierz czy kształt ma być udoskonalony.
2.  Kliknij na przycisk **Utwórz**,
3.  Obiekt zostanie utworzony w oknie [widoku 3D](3D_view/pl.md) i zostanie umieszczony w [widoku drzewa](Tree_view/pl.md).



## Uwagi

Jednym z możliwych rozwiązań może być przepływ pracy:

-   Narysuj szkielet modelu o wybranym kształcie za pomocą narzędzi <img alt="" src=images/Workbench_Draft.svg  style="width:24px;"> [Środowiska pracy Rysunek Roboczy](Draft_Workbench/pl.md) *(np. linii i linii łamanej)*.
-   Utwórz wszystkie powierzchnie z powierzchnią od krawędzi.
-   Utwórz powłokę na powierzchni.
-   Utwórz bryłę z powłoki.



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Builder/pl
