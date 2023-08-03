---
 GuiCommand:
   Name: Part Measure Linear
   Name/pl: Część: Pomiar liniowy
   MenuLocation: Pomiary , Pomiar liniowy
   Workbenches: Part_Workbench/pl
   SeeAlso: Std_MeasureDistance/pl, Draft_Dimension/pl
---

# Part Measure Linear/pl



## Opis

To polecenie mierzy odległość między dwoma wybranymi elementami topologicznymi *(wierzchołek, krawędź, ściana)* i wyświetla pomiary w oknie [widoku 3D](3D_view/pl.md). Wyświetlana jest najmniejsza odległość między dwoma elementami i pomiary delta *(odległości równoległe do globalnych osi X, Y, Z)*.

Wygląd pomiarów można zmienić w [ustawieniach](PartDesign_Preferences/pl#Pomiary.md).

<img alt="" src=images/MeasureLinear3D1.png  style="width:400px;"> <img alt="" src=images/MeasureLinearDelta1.PNG  style="width:400px;">



## Użycie

1.  Wybierz dowolną kombinację dwóch elementów: wierzchołków, krawędzi, ścian.
2.  Polecenie można wywołać na kilka sposobów:
    -   Naciśnij przycisk **<img src="images/Part_Measure_Linear.svg" width=16px> '''Pomiar liniowy'''**.
    -   Wybierz z menu opcję **Pomiary → <img src="images/Part_Measure_Linear.svg" width=16px> Pomiar liniowy**.
3.  Alternatywnie polecenie można uruchomić bez wcześniejszego wyboru. Otworzy się wówczas okno dialogowe wyboru w [Panelu zadań](Task_panel/pl.md). Widżet sterowania zawiera również przyciski do resetowania wyboru, przełączania wyświetlania pomiarów w oknie [widoku 3D](3D_view/pl.md) i usuwania wszystkich pomiarów.
4.  Pomiary są automatycznie usuwane podczas zamykania dokumentu.



## Uwagi

-   Nie można używać narzędzi przyciągania środowiska pracy [Rysunek Roboczy](Draft_Workbench/pl.md) z tym poleceniem.
-   Aby dodać wymiary do rysunków, użyj narzędzi wymiarowych środowiska pracy [Rysunek Techniczny](TechDraw_Workbench/pl.md).
-   Aby uzyskać bardziej wszechstronne narzędzia pomiarowe, zainstaluj środowisko pracy <img alt="" src=images/Manipulator_workbench_icon.svg  style="width:24px;"> [Manipulator](Manipulator_Workbench/pl.md) *(środowisko [zewnętrzne](External_workbenches/pl.md))*.



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Measure Linear/pl
