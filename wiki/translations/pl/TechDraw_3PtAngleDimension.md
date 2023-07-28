---
- GuiCommand:/pl
   Name:TechDraw 3PtAngleDimension
   Name/pl:Rysunek Techniczny: Wstaw trzy punktowy wymiar kąta
   MenuLocation:Rysunek Techniczny → Wymiary → Wstaw trzy punktowy wymiar kąta
   Workbenches:[Rysunek Techniczny](TechDraw_Workbench/pl.md)
   Version:0.18
   SeeAlso:[Wstaw wymiar kąta](TechDraw_AngleDimension/pl.md)
---

# TechDraw 3PtAngleDimension/pl



## Opis

Narzędzie **Wstaw trzy punktowy wymiar kąta** dodaje wymiar kąta do widoku. Wymiar pokazuje kąt wewnętrzny między trzema punktami.

<img alt="" src=images/TechDraw_Dimension_Angle3Pt_example.png  style="width:200px;"> 
*Pomiar kąta między trzema punktami.*



## Użycie

1.  Wybierz punkty lub krawędzie, które definiują pomiar.
2.  Jeśli zaznaczyłeś geometrię w widoku 3D: dodaj właściwy widok Rysunku Technicznego do zaznaczenia, wybierając go w oknie [Widoku drzewa](Tree_view/pl.md).
3.  Istnieje kilka sposobów wywołania narzędzia:
4.  Naciśnij przycisk **<img src="images/TechDraw_3PtAngleDimension.svg" width=16px> '''Wstaw trzy punktowy wymiar kąta'''**.

-   Wybierz opcję z menu **Rysunek Techniczny → Wymiary → <img src="images/TechDraw_3PtAngleDimension.svg" width=16px> Wstaw trzy punktowy wymiar kątaa**.

1.  Do widoku zostanie dodany wymiar.
2.  Wymiar można przeciągnąć do żądanej pozycji.
3.  Jeśli to konieczne, dodaj tolerancje, jak opisano na stronie [Wymiarowanie geometrii i tolerancja](TechDraw_Geometric_dimensioning_and_tolerancing/pl#Tolerancja.md).



### Wyświetlanie pomiarów 3D 

Zapoznaj się również z informacjami na stronie [Wstaw wymiar długości](TechDraw_LengthDimension/pl#Wyświetlanie_pomiarów_3D.md)



### Zmiana właściwości 

Aby zmienić właściwości obiektu wymiaru, kliknij dwukrotnie na niego w rysunku lub w [widoku drzewa](Tree_view/pl.md). Spowoduje to otwarcie okna [dialogowego wymiaru](TechDraw_LengthDimension/pl#Okno_dialogowe.md).



## Ograniczenia

Obiekty wymiarowe są podatne na \"[problem nazewnictwa topologicznego](Topological_naming_problem/pl.md)\". Zobacz stronę [Wstaw wymiar długości](TechDraw_LengthDimension/pl.md), aby uzyskać więcej informacji.



## Uwagi

Zapoznaj się również informacjami na stroni e[Wymiar długości](TechDraw_LengthDimension/pl#Uwagi.md).



## Właściwości

Zobacz stronę [Wymiar długości](TechDraw_LengthDimension/pl#W.C5.82a.C5.9Bciwo.C5.9Bci.md).



## Tworzenie skryptów 

Zobacz również stronę: [Dokumentacja API generowana automatycznie](https://freecad.github.io/SourceDoc/) oraz [Podstawy pisania skryptów dla FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Narzędzie **Wstaw trzy punktowy wymiar kąta** może być używane w [makrodefinicjach](Macros/pl.md) i z konsoli [Python](Python/pl.md) za pomocą następujących funkcji:


```python
dim1 = FreeCAD.ActiveDocument.addObject('TechDraw::DrawViewDimension','Dimension')
dim1.Type = "Angle3Pt"
dim1.References2D=[(view1, 'Vertex1',(view1, 'Vertex4'),(view1, 'Vertex2'))]
rc = page.addView(dim1)
```





{{TechDraw Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw 3PtAngleDimension/pl
