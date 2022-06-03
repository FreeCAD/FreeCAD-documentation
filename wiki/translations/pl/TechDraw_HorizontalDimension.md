---
- GuiCommand   */pl
   Name   *TechDraw HorizontalDimension
   Name/pl   *Rysunek Techniczny   * Wstaw wymiar poziomy
   MenuLocation   *Rysunek Techniczny → Wymiary → Wstaw wymiar poziomy
   Workbenches   *[Rysunek Techniczny](TechDraw_Workbench/pl.md)
   Shortcut   ***Shift** + **H**
   SeeAlso   *[Wymiar długości](TechDraw_LengthDimension/pl.md), [Wstaw wymiar pionowy](TechDraw_VerticalDimension/pl.md)
---

# TechDraw HorizontalDimension/pl

## Opis

Narzędzie Wymiar poziomy dodaje wymiar poziomy do widoku. Może to być odległość między dwoma wierzchołkami, długość jednej krawędzi lub odległość pozioma między dwoma krawędziami. Początkowo będzie to odległość rzutowana *(tzn. taka, jak na rysunku)*, ale można ją zmienić na rzeczywistą odległość 3D za pomocą narzędzia **<img src="images/TechDraw_LinkDimension.svg" width=16px> [Powiązanie wymiaru](TechDraw_LinkDimension/pl.md)**.

<img alt="" src=images/TechDraw_Dimension_Horizontal_example.png  style="width   *200px;"> 
*Wymiar długości odnoszący się do dwóch dowolnych węzłów widoku. Odległość jest mierzona w poziomie.*

## Użycie

1.  Wybierz wierzchołki lub krawędzie, które definiują Twój pomiar.
2.  Naciśnij przycisk **<img src="images/TechDraw_HorizontalDimension.svg" width=16px> [Wstaw wymiar poziomy](TechDraw_HorizontalDimension/pl.md)**.
3.  Do widoku zostanie dodany wymiar. Wymiar można przeciągnąć do żądanej pozycji.
4.  Jeśli to konieczne, dodaj tolerancje, jak opisano na stronie [Wymiarowanie geometrii i tolerancja](TechDraw_Geometric_dimensioning_and_tolerancing/pl#Tolerancja.md).

Aby zmienić właściwości obiektu wymiaru, kliknij dwukrotnie na niego w rysunku lub w [widoku drzewa](Tree_view/pl.md). Spowoduje to otwarcie okna [dialogowego wymiaru](TechDraw_LengthDimension/pl#Okno_dialogowe.md).

## Ograniczenia

Obiekty wymiarowe są podatne na \"[problem nazewnictwa topologicznego](Topological_naming_problem/pl.md)\". Zobacz stronę [Wymiar długości](TechDraw_LengthDimension/pl.md), aby uzyskać więcej informacji.

## Właściwości

Zobacz stronę [Wymiar długości](TechDraw_LengthDimension/pl#W.C5.82a.C5.9Bciwo.C5.9Bci.md).

## Tworzenie skryptów 


**Zobacz również   ***

[TechDraw API](TechDraw_API.md) i [Podstawy tworzenia skryptów FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Narzędzie **Wymiar poziomy** może być używane w [makrodefinicjach](Macros/pl.md) i z konsoli [Python](Python/pl.md) za pomocą następujących funkcji   *


```python
dim1 = FreeCAD.ActiveDocument.addObject('TechDraw   *   *DrawViewDimension','Dimension')
dim1.Type = "DistanceX"
dim1.References2D=[(view1, 'Edge1')]
rc = page.addView(dim1)
```





{{TechDraw Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw HorizontalDimension/pl
