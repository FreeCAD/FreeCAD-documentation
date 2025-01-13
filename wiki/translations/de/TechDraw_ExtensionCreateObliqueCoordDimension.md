---
 GuiCommand:
   Name: TechDraw ExtensionCreateObliqueCoordDimension
   Name/de: TechDraw ErgänzungSchrägeKoordinatenmaße
   MenuLocation: TechDraw , Ergänzungen: Maße , Schräge Koordinatenmaße erstellen
   Workbenches: TechDraw_Workbench/de
   Shortcut: 
   Version: 0.20
   SeeAlso: TechDraw_ExtensionCreateHorizCoordDimension/de, TechDraw_ExtensionCreateVertCoordDimension/de
---

# TechDraw ExtensionCreateObliqueCoordDimension/de



## Beschreibung

Das Werkzeug **TechDraw ErgänzungSchrägeKoordinatenmaße** erzeugt eine schräge Stufenbemaßung: mehrere Maße in gleichem Abstand mit der gleichen Basislinie.

<img alt="" src=images/TechDraw_ExtensionCreateObliqueCoordDimensionExample.png  style="width:400px;"> 
*Rechts die erzeugten Maße*



## Anwendung

1.  Wahlweise kann der Abstand zwischen den Maßen mit dem Werkzeug <img alt="" src=images/TechDraw_ExtensionSelectLineAttributes.svg  style="width:16px;"> [TechDraw ErgänzungLinienmerkmaleAuswählen](TechDraw_ExtensionSelectLineAttributes/de.md) festgelegt werden.
2.  Drei oder mehr Knotenpunkte auswählen.
3.  Die Reihenfolge der Auswahl der beiden ersten Knotenpunkte bestimmt die Position der Basislinie. Wenn der erste gewählte Knotenpunkt links vom zweiten liegt, dann ist die Basislinie beim ganz linken Knotenpunkt , sonst beim ganz rechten Knotenpunkt.
4.  Die beiden zuerst gewählten Knotenpunkte bestimmen auch die Richtung der Maße.
5.  Es gibt mehrere Möglichkeiten das Werkzeug aufzurufen:
    -   
        {{Version/de|1.0}}
        
        : Ist die [Einstellung](TechDraw_Preferences/de#Maßeinträge.md) **Maß-Werkzeuge** auf {{Value|Einzelnes Werkzeug}} (Standardeinstellung) gesetzt: Den Nach-unten-Pfeil rechts neben der Schaltfläche **<img src="images/TechDraw_Dimension.svg" width=|x16px> <img src="images/Toolbar_flyout_arrow.svg" width=x16px>** drücken und die Menüoption **<img src="images/TechDraw_ExtensionCreateObliqueCoordDimension.svg" width=16px> Schräge Koordinatenmaße erstellen** in der Ausklappliste auswählen.

    -   Hat die Einstellung einen anderen Wert (und in {{VersionMinus/de|0.21}}): Die Schaltfläche **<img src="images/TechDraw_ExtensionCreateObliqueCoordDimension.svg" width=16px> [Schräge Koordinatenmaße erstellen](TechDraw_ExtensionCreateObliqueCoordDimension/de.md)** drücken.

    -   Den Menüeintrag **TechDraw → Ergänzungen: Maße → <img src="images/TechDraw_ExtensionCreateObliqueCoordDimension.svg" width=16px> Schräge Koordinatenmaße erstellen** auswählen.
6.  Stufenmaße mit zentrierten Maßzahlen werden eingefügt.





{{TechDraw_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw ExtensionCreateObliqueCoordDimension/de
