---
- GuiCommand:
   Name:TechDraw ExtensionCreateHorizCoordDimension
   Name/pl:Rysunek Techniczny: Rozszerzenie Seria wymiarów kaskadowych poziomo
   MenuLocation:Rysunek Techniczny → Rozszerzenia: Wymiary → Seria wymiarów poziomo
   Workbenches:[Rysunek Techniczny](TechDraw_Workbench/pl.md)
   Shortcut:
   Version:0.20
   SeeAlso:[Seria wymiarów kaskadowych pionowo](TechDraw_ExtensionCreateVertCoordDimension/pl.md), [Seria wymiarów kaskadowych ukośnie](TechDraw_ExtensionCreateObliqueCoordDimension/pl.md)
---

# TechDraw ExtensionCreateHorizCoordDimension/pl



## Opis

Narzędzie **Seria wymiarów kaskadowych poziomo** tworzy poziome wymiary współrzędnych: wiele równomiernie rozmieszczonych wymiarów zaczynających się od tej samej linii bazowej.

<img alt="" src=images/TechDraw_ExtensionCreateHorizCoordDimensionExample.png  style="width:400px;"> 
*Po prawej utworzony ciąg wymiarów*



## Użycie

1.  Opcjonalnie określ odstęp kaskadowy za pomocą narzędzia <img alt="" src=images/TechDraw_ExtensionSelectLineAttributes.svg  style="width:16px;"> [Wybierz atrybuty linii](TechDraw_ExtensionSelectLineAttributes.md).
2.  Wybierz trzy lub więcej wierzchołków.
3.  Kolejność wyboru pierwszych dwóch wierzchołków określa położenie linii bazowej. Jeśli wierzchołek wybrany jako pierwszy znajduje się na lewo od drugiego, linia bazowa jest tworzona w wierzchołku najbardziej wysuniętym na lewo, w przeciwnym razie jest tworzona w wierzchołku najbardziej wysuniętym na prawo.
4.  Narzędzie można wywołać na kilka sposobów:
    -   Naciśnij przycisk **<img src="images/TechDraw_ExtensionCreateHorizCoordDimension.svg" width=16px> '''Seria wymiarów kaskadowych poziomo'''**.
    -   Wybierz opcję z menu **Rysunek Techniczny → Rozszerzenia: Wymiary → <img src="images/TechDraw_ExtensionCreateHorizCoordDimension.svg" width=16px> Seria wymiarów kaskadowych poziomo**.
5.  Tworzone są wymiary współrzędnych z wyśrodkowanymi tekstami wymiarowania.





{{TechDraw_Tools_navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw ExtensionCreateHorizCoordDimension/pl
