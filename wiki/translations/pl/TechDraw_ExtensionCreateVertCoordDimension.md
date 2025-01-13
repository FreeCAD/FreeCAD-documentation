---
 GuiCommand:
   Name: TechDraw ExtensionCreateVertCoordDimension
   Name/pl: Rysunek Techniczny: Rozszerzenie Seria wymiarów kaskadowych pionowo
   MenuLocation: Rysunek Techniczny , Rozszerzenia: Wymiary , Seria wymiarów kaskadowych pionowo
   Workbenches: TechDraw_Workbench/pl
   Shortcut: 
   Version: 0.20
   SeeAlso: TechDraw_ExtensionCreateHorizCoordDimension/pl, TechDraw_ExtensionCreateObliqueCoordDimension/pl
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
    -   
        {{Version/pl|1.0}}
        
        : Jeśli [preferencja](TechDraw_Preferences/pl#Wymiary.md) **Narzędzie wymiarowania** jest ustawiona na {{Value|Narzędzie pojedyncze}} (domyślnie): kliknij na strzałce skierowanej w dół po prawej stronie od przycisku **<img src="images/TechDraw_Dimension.svg" width=|x16px><img src="images/Toolbar_flyout_arrow.svg" width=x16px>** i wybierz opcję **<img src="images/TechDraw_ExtensionCreateVertCoordDimension.svg" width=16px> Seria wymiarów kaskadowych pionowo** z listy rozwijanej.

    -   Jeśli ta preferencja ma inną wartość (i {{VersionMinus/pl|0.21}}): wciśnij przycisk **<img src="images/TechDraw_ExtensionCreateVertCoordDimension.svg" width=16px> [Seria wymiarów kaskadowych pionowo](TechDraw_ExtensionCreateVertCoordDimension/pl.md)**.

    -   Wybierz opcję z menu **Rysunek Techniczny → Rozszerzenia: Wymiary → <img src="images/TechDraw_ExtensionCreateVertCoordDimension.svg" width=16px> Seria wymiarów kaskadowych pionowo**.
5.  Tworzone są wymiary współrzędnych z wyśrodkowanymi tekstami wymiarowania.





{{TechDraw_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw ExtensionCreateVertCoordDimension/pl
