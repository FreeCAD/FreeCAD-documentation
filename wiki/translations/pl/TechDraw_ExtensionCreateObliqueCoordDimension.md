---
- GuiCommand:
   Name: TechDraw ExtensionCreateObliqueCoordDimension
   Name/pl: Rysunek Techniczny: Rozszerzenie Seria wymiarów kaskadowych ukośnie
   MenuLocation: Rysunek Techniczny -> Rozszerzenia: Wymiary -> Seria wymiarów ukośnie
   Workbenches: TechDraw_Workbench/pl
   Shortcut: 
   Version: 0.20
   SeeAlso: TechDraw_ExtensionCreateHorizCoordDimension/pl, TechDraw_ExtensionCreateVertCoordDimension/pl
---

# TechDraw ExtensionCreateObliqueCoordDimension/pl



## Opis

Narzędzie **Seria wymiarów kaskadowych ukośnie** tworzy ukośne wymiary współrzędnych: wiele równomiernie rozmieszczonych wymiarów zaczynających się od tej samej linii bazowej.

<img alt="" src=images/TechDraw_ExtensionCreateObliqueCoordDimensionExample.png  style="width:400px;"> 
*Po prawej utworzony ciąg wymiarów*



## Użycie

1.  Opcjonalnie określ odstęp kaskadowy za pomocą narzędzia <img alt="" src=images/TechDraw_ExtensionSelectLineAttributes.svg  style="width:16px;"> [Wybierz atrybuty linii](TechDraw_ExtensionSelectLineAttributes/pl.md).
2.  Wybierz trzy lub więcej wierzchołków.
3.  Kolejność wyboru pierwszych dwóch wierzchołków określa położenie linii bazowej. Jeśli wierzchołek wybrany jako pierwszy znajduje się na lewo od drugiego, linia bazowa jest tworzona w wierzchołku najbardziej wysuniętym na lewo, w przeciwnym razie jest tworzona w wierzchołku najbardziej wysuniętym na prawo.
4.  Pierwsze dwa wierzchołki definiują również kierunek.
5.  Narzędzie można wywołać na kilka sposobów:
    -   Naciśnięcie przycisku **<img src="images/TechDraw_ExtensionCreateObliqueCoordDimension.svg" width=16px> '''Seria wymiarów kaskadowych ukośnie'''**.
    -   Wybierz opcję z menu **Rysunek Techniczny → Rozszerzenia: Wymiary → <img src="images/TechDraw_ExtensionCreateObliqueCoordDimension.svg" width=16px> Seria wymiarów kaskadowych ukośnie**.
6.  Tworzone są wymiary współrzędnych z wyśrodkowanymi tekstami wymiarowania.





{{TechDraw_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw ExtensionCreateObliqueCoordDimension/pl
