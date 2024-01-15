---
 GuiCommand:
   Name: TechDraw LandmarkDimension
   Name/pl: Rysunek Techniczny: Wstaw wymiar przestrzenny
   MenuLocation: Rysunek Techniczny , Wymiary , Wstaw wymiar przestrzenny - EXPERYMENTALNE
   Workbenches: TechDraw_Workbench/pl
   Version: 0.19
   SeeAlso: TechDraw_HorizontalDimension/pl, TechDraw_VerticalDimension/pl
---

# TechDraw LandmarkDimension/pl



## Opis

Narzędzie **Wstaw wymiar przestrzenny** dodaje wymiar liniowy do widoku. Wymiar jest oparty na dwóch obiektach punktowych ([Punkt](Draft_Point/pl.md) środowiska Rysunek Roboczy lub [Punkt](Part_Point/pl.md) środowiska Część lub [Punkt](PartDesign_Point/pl.md))\'\' środowiska pracy Projekt Części z modelu 3D.

Celem tego narzędzia jest zapewnienie obejścia problemu uszkodzenia wymiarów spowodowanego przez \"[Problem nazewnictwa topologicznego](Topological_naming_problem/pl.md)\". Punkty źródłowe powinny używać [Wyrażeń](Expressions/pl.md) lub innego mechanizmu wiążącego, aby ustalić ich położenie. Ponieważ punkty są [Obiektami dokumentu](App_DocumentObject/pl.md), a nie komponentami kształtu, ich nazwa nie zmienia się przy ponownych obliczeniach, a więc łatwo je znaleźć.

Zobacz stronę [Wstaw wymiar długości](TechDraw_LengthDimension/pl#Ograniczenia.md) , aby dowiedzieć się więcej na temat wymiarów i nazewnictwa topologicznego.



## Użycie

1.  Wybierz dwa obiekty punktowe w oknie [widoku 3D](3D_view/pl.md) lub [Widoku drzewa](Tree_view/pl.md).
2.  Dodaj właściwy widok Rysunku Technicznego do zaznaczenia, wybierając go w oknie [Widoku drzewa](Tree_view/pl.md).
3.  Istnieje kilka sposobów wywołania narzędzia:
    -   Naciśnij przycisk **<img src="images/TechDraw_LandmarkDimension.svg" width=16px> '''Wstaw wymiar przestrzenny'''**.
    -   Wybierz z menu opcję **Rysunek Techniczny → Wymiary → <img src="images/TechDraw_LandmarkDimension.svg" width=16px> Wstaw wymiar przestrzenny**.
4.  Wymiar zostanie dodany do widoku.
5.  Wymiar można przeciągnąć do żądanej pozycji.
6.  W razie potrzeby dodaj tolerancje zgodnie z opisem na stronie [Wymiatrowanie i tolerancja](TechDraw_Geometric_dimensioning_and_tolerancing/pl#Tolerancja.md).



### Zmiana właściwości 

Aby zmienić właściwości obiektu wymiaru, kliknij dwukrotnie na niego w rysunku lub w [widoku drzewa](Tree_view/pl.md). Spowoduje to otwarcie okna [dialogowego wymiaru](TechDraw_LengthDimension/pl#Okno_dialogowe.md).



## Ograniczenia

Narzędzie W**Wstaw wymiar przestrzenny** jest początkowo zawężone do wymiarów \"Odległość\". Inne typy mogą być dodane, jeśli zapotrzebowanie na nie będzie uzasadnione.



## Uwagi

Zapoznaj się również informacjami na stroni e[Wymiar długości](TechDraw_LengthDimension/pl#Uwagi.md).



## Właściwości

Zobacz stronę [Wymiar długości](TechDraw_LengthDimension/pl#W.C5.82a.C5.9Bciwo.C5.9Bci.md).



## Tworzenie skryptów 

Zobacz również stronę: [Dokumentacja API generowana automatycznie](https://freecad.github.io/SourceDoc/) oraz [Podstawy pisania skryptów dla FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Narzędzie **Wstaw wymiar przestrzenny** może być używane w [makrodefinicjach](macros/pl.md) i z konsoli [Python](Python/pl.md) za pomocą następujących funkcji:


```python
dim1 = FreeCAD.ActiveDocument.addObject("TechDraw::LandmarkDimension", "Landmark")
dim1.Type = "Distance"
dim1.References2D = [(TDView, "Vertex1")]
dim1.References3D = [(Point3d1, "Vertex1")]
dim1.References3D = [(Point3d2, "Vertex1")]
page.addView(dim1)
```





{{TechDraw Tools navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw LandmarkDimension/pl
