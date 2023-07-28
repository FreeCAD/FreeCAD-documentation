---
- GuiCommand:/pl
   Name:TechDraw ExtensionCreateVertCoordDimension
   Name/pl:Rysunek Techniczny: Rozszerzenie Seria wymiarów kaskadowych pionowo
   MenuLocation:Rysunek Techniczny → Rozszerzenia: Wymiary → Seria wymiarów kaskadowych pionowo
   Workbenches:[Rysunek Techniczny](TechDraw_Workbench/pl.md)
   Shortcut:
   Version:0.20
   SeeAlso:[Seria wymiarów kaskadowych poziomo](TechDraw_ExtensionCreateHorizCoordDimension/pl.md), [Seria wymiarów kaskadowych ukośnie](TechDraw_ExtensionCreateObliqueCoordDimension/pl.md)
---

# TechDraw ExtensionCreateVertCoordDimension/pl



## Opis

Narzędzie **Seria wymiarów kaskadowych pionowo** tworzy pionowe wymiary współrzędnych: wiele równomiernie rozmieszczonych wymiarów zaczynających się od tej samej linii bazowej.

<img alt="" src=images/TechDraw_ExtensionCreateVertCoordDimensionExample.png  style="width:400px;"> 
*Po prawej utworzony ciąg wymiarów*



## Użycie

1.  Opcjonalnie określ odstęp kaskadowy za pomocą narzędzia <img alt="" src=images/TechDraw_ExtensionSelectLineAttributes.svg  style="width:16px;"> [Wybierz atrybuty linii](TechDraw_ExtensionSelectLineAttributes/pl.md).
2.  Wybierz trzy lub więcej wierzchołków.
3.  Kolejność wyboru pierwszych dwóch wierzchołków określa położenie linii bazowej. Jeśli wierzchołek wybrany jako pierwszy znajduje się poniżej drugiego, linia bazowa jest tworzona w najniższym wierzchołku, w przeciwnym razie jest tworzona w najwyższym wierzchołku.
4.  Narzędzie można wywołać na kilka sposobów:
    -   Naciśnij przycisk **<img src="images/TechDraw_ExtensionCreateVertCoordDimension.svg" width=16px> '''Seria wymiarów kaskadowych pionowo'''**.
    -   Wybierz opcję z menu **Rysunek Techniczny → Rozszerzenia: Wymiary → <img src="images/TechDraw_ExtensionCreateVertCoordDimension.svg" width=16px> Seria wymiarów kaskadowych pionowo**.
5.  Tworzone są wymiary współrzędnych z wyśrodkowanymi tekstami wymiarowania.





{{TechDraw_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw ExtensionCreateVertCoordDimension/pl
