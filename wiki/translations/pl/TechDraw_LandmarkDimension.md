---
- GuiCommand:/pl
   Name:TechDraw LandmarkDimension
   Name/pl:Rysunek Techniczny: Wymiar przestrzenny
   MenuLocation:Rysunek Techniczny → Wymiary → Wstaw wymiar przestrzenny - EXPERYMENTALNE
   Workbenches:[Rysunek Techniczny](TechDraw_Workbench/pl.md)
   Version:0.19
   SeeAlso:[Wstaw wymiar poziomy](TechDraw_HorizontalDimension/pl.md), [Wstaw wymiar pionowy](TechDraw_VerticalDimension/pl.md)
---

# TechDraw LandmarkDimension/pl



## Opis

Narzędzie **Wymiar przestrzenny** dodaje wymiar liniowy do widoku. Wymiar jest oparty na dwóch punktach **cecha** *(Draft.Point lub Part.Vertex)* z modelu 3D. Uwaga: punkty muszą być obiektami **cecha**, które występują w [widoku drzewa](Tree_view/pl.md) modelu. Losowe wierzchołki z kształtu nie będą odpowiednie.

Celem tego narzędzia jest zapewnienie obejścia problemu uszkodzenia wymiarów spowodowanego przez \"[Problem nazewnictwa topologicznego](Topological_naming_problem/pl.md)\". Punkty źródłowe powinny używać [Wyrażeń](Expressions/pl.md) lub innego mechanizmu wiążącego, aby ustalić ich położenie. Ponieważ punkty są [Obiektami dokumentu](App_DocumentObject/pl.md), a nie komponentami kształtu, ich nazwa nie zmienia się przy ponownych obliczeniach, a więc łatwo je znaleźć.

Zobacz stronę [Rysunek Techniczny: Wymiar długości](TechDraw_LengthDimension/pl#Ograniczenia.md) , aby dowiedzieć się więcej na temat wymiarów i nazewnictwa topologicznego.

Wymiar przestrzenny generalnie zachowuje się jak każdy inny wymiar.



## Użycie

1.  Wybierz dwa obiekty punktów w [widoku drzewa](Tree_view/pl.md) lub oknie [widoku 3D](3D_view/pl.md).
2.  Wybierz również widok, do którego ma zostać dodany wymiar.
3.  Naciśnij przycisk **<img src="images/TechDraw_LandmarkDimension.svg" width=16px> [Wstaw wymiar przestrzenny - EKSPERYMENTALNE](TechDraw_LandmarkDimension/pl.md)** lub wybierz z menu **Rysunek Techniczny → Wymiary → Wstaw wymiar przestrzenny**.
4.  Wymiar zostanie dodany do widoku. Tekst wymiaru może być przeciągany na żądaną pozycję.



## Ograniczenia

Narzędzie Wymiar przestrzenny jest początkowo zawężone do wymiarów \"Odległość\". Inne typy mogą być dodane, jeśli zapotrzebowanie na nie będzie uzasadnione.



## Właściwości

Funkcja **Wymiar przestrzenny** nie wprowadza żadnych nowych właściwości.



## Tworzenie skryptów 

Zobacz również stronę: [Dokumentacja API generowana automatycznie](https://freecad.github.io/SourceDoc/) oraz [Podstawy pisania skryptów dla FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Narzędzie **Wymiar przestrzenny** może być używane w [makrodefinicjach](macros/pl.md) i z konsoli [Python](Python/pl.md) za pomocą następujących funkcji:


```python
dim1 = FreeCAD.ActiveDocument.addObject('TechDraw::LandmarkDimension','Landmark')
dim1.Type = "Distance"
dim1.References2D=[(TDView, 'Vertex1')]
dim1.References3D=[(Point3d1, 'Vertex1')]
dim1.References3D=[(Point3d2, 'Vertex1')]
rc = page.addView(dim1)
```


<div class="mw-translate-fuzzy">





</div>


{{TechDraw Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw LandmarkDimension/pl
