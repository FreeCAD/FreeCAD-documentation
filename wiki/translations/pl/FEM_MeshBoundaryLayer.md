---
 GuiCommand:Container|
{{GuiCommand/pl
   Name: FEM MeshBoundaryLayer
   Name/pl: Warstwa przyścienna siatki MES
   MenuLocation: Siatka , Warstwa przyścienna siatki MES
   Workbenches: FEM_Workbench/pl
   SeeAlso: FEM_tutorial/pl
}}
{{GuiCommandFemInfo/pl
   Solvers: Wszystkie
}}
---

# FEM MeshBoundaryLayer/pl



## Opis

Umożliwia ustawienie zlokalizowanego zestawu parametrów tworzenia siatki poprzez wskazanie zestawu obiektów *(wierzchołek, krawędź, ściana)* i przypisanie do nich parametrów.

Jest to szczególnie przydatne do zagęszczenia siatek w pobliżu krawędzi lub powierzchni w przypadku symulacji przepływów. Przykładowo, można skorzystać z tego narzędzia do zagęszczenia siatki w pobliżu profilu skrzydła samolotu lub przeszkody w przepływie.

Warstwa przyścienna ma tę zaletę, że tworzy silnie zdefiniowane, anizotropowe siatki. Jak nazwa wskazuje, umożliwia dokładne obliczenia w pobliżu brzegów, np. ściany gdzie występuje tarcie, generując gradient prędkości.



## Użycie

1.  Aby skorzystać z tego narzędzia, siatka musi być najpierw utworzona <img alt="" src=images/FEM_MeshGmshFromShape.svg  style="width:32px;"> [Siatka MES z kształtu przy pomocy generatora Gmsh](FEM_MeshGmshFromShape/pl.md).
    -   Zaznacz obiekt siatki w drzewie modelu i wciśnij przycisk **<img src="images/FEM_MeshBoundaryLayer.svg" width=32px> [Warstwa graniczna siatki MES](FEM_MeshBoundaryLayer/pl.md)** button.
    -   Zaznacz obiekt siatki w drzewie modelu i wybierz opcję **Siatka → <img src="images/FEM_MeshBoundaryLayer.svg" width=32px> Warstwa graniczna siatki MES** z menu.
2.  Edytuj początkowy rozmiar elementów, tempo wzrostu i liczbę warstw wzrostu.
3.  Wybierz wierzchołek, krawędź lub ścianę.
4.  Wciśnij przycisk **OK**.
5.  Zamknij okno dialogowe.

    :   Rezultat: Powinieneś zobaczyć nowy obiekt `FEMMeshBoundaryLayer` pod obiektem `FEMMeshGMSH` (zobacz przykład #3 poniżej) w aktywnym kontenerze analizy.
6.  Kliknij dwukrotnie na obiekcie `FEMMeshGMSH` w drzewie modelu i wciśnij przycisk **Zastosuj** aby wymusić ponowne przeliczenie siatki.
7.  Zamknij okno dialogowe.

Po utworzeniu siatki możesz zmienić jej właścioci przy pomocy [edytora właściwości](Property_editor/pl.md). Po zmianie właściwości należy ponownie otworzyć okno dialogowe Gmsh i wcisnąć przycisk **Zastosuj**. (możesz zostawić okno dialogowe otwarte podczas zmieniana właściwości).

Możesz utworzyć tyle różnych warstw przyściennych, ile potrzeba.



## Przykłady wizualne 

<img alt="" src=images/FEMMeshBoundaryLayer_Example1.png.png  style="width:300px;"> 
*Przykład 1: Początkowa rzadka siatka FEMMeshGMSH dla przypadku 2D*

<img alt="" src=images/FEMMeshBoundaryLayer_Example2.png.png  style="width:300px;"> 
*Przykład 2: Po zastosowaniu warstwy granicznej siatki MES*

<img alt="" src=images/FEMMeshBoundaryLayer_Example3.png.png  style="width:300px;"> 
*Przykład 3: Prosty przykład rezultatu w drzewie modelu*



## Uwagi



## Powiązane





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM MeshBoundaryLayer/pl
