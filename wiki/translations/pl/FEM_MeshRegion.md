---
 GuiCommand:
   Name: FEM MeshRegion
   Name/pl: MES Ulepsz ...
   MenuLocation: Siatka , MES Ulepsz
   Workbenches: FEM_Workbench/pl
   SeeAlso: FEM_tutorial/pl
---

# FEM MeshRegion/pl



## Opis

Umożliwia utworzenie zlokalizowanego zestawu parametrów tworzenia siatki poprzez wskazanie obiektów *(wierzchołek, krawędź, ściana)* i przypisanie do nich parametrów. Jest to szczególnie przydatne do zagęszczania siatek w obszarach zainteresowania lub obszarach gdzie solver generuje silne gradienty zmiennych. Przykładowo, można skorzystać z tego narzędzia do zagęszczenia siatki w miejscach koncentracji naprężeń *(ostre krawędzie, otwory, karby itd.)* w analizie mechanicznej lub w przewężeniach w analizach przepływów.

Lokalne zagęszczanie siatki ma tę zaletę, że umożliwia dokładne obliczenia tam, gdzie są potrzebne, pozostawiając rzadszą globalną siatkę, co znacząco skraca czas obliczeń przy zachowaniu dokładności wyników.



## Użycie

1.  Aby skorzystać z tego narzędzia należy najpierw utworzyć siatkę <img alt="" src=images/FEM_MeshGmshFromShape.svg  style="width:32px;"> [Siatka MES z kształtu przy pomocy generatora Gmsh](FEM_MeshGmshFromShape.md).
    -   Zaznacz obiekt siatki w drzewie modelu i wciśnij przycisk **<img src="images/FEM_MeshRegion.svg" width=32px> '''Ulepsz ...'''**.
    -   Zaznacz obiekt siatki w drzewie modelu i wybierz opcję **Siatka → <img src="images/FEM_MeshRegion.svg" width=32px> Ulepsz ...** z menu.
2.  Edytuj maksymalny rozmiar elementu dla obszaru.
3.  Wciśnij przycisk **OK**.
4.  Zamknij okno dialogowe.

    :   Rezultat: Powinieneś teraz widzieć nowy obiekt `FEMMeshRegion` pod obiektem `FEMMeshGMSH` *(zobacz przykład #3 poniżej)* w aktywnym kontenerze analizy.
5.  Dwukrotnie kliknij na obiekcie `FEMMeshGMSH` w drzewie modelu i wciśnij przycisk **Zastosuj** aby wymusić ponowne przeliczenie siatki.
6.  Zamknij okno dialogowe.

Po utworzeniu siatki można edytować jej właściwości przy pomocy [edytora właściwości](Property_editor/pl.md). Po zmianie właściwości należy ponownie otworzyć okno dialogowe Gmsh i wcisnąć przycisk **Zastosuj** *(można zostawić okno dialogowe otwarte podczas zmieniana właściwości)*.

Możesz utworzyć tyle różnych obszarów siatki, ile potrzeba.



## Przykłady wizualne 

<img alt="" src=images/FEMMeshRegion_Example1.png style="width:300px;"> 
*Przykład 1: Początkowa rzadka siatka Gmsh.*

<img alt="" src=images/FEMMeshRegion_Example2.png  style="width:300px;"> 
*Przykład 2: Po zastosowaniu zagęszczenia siatki przy pomoc dwóch obszarów siatki, większy otwór jest zagęszczony do maksymalnego rozmiaru elementu 3 mm, zaś mniejszy do rozmiaru 1 mm.*

<img alt="" src=images/FEMMeshRegion_Example3.png  style="width:300px;"> 
*Przykład 3: Prosty przykład rezultatu w drzewie modelu.*



## Uwagi

Kolejność, w której obszary są pokazywane w [widoku drzewa](Tree_view/pl.md) może wpłynąć na uzyskaną siatkę. Więcej informacji można znaleźć [w tym wątku na forum](https://forum.freecadweb.org/viewtopic.php?f=18&t=41955).



## Powiązane

-   \"Mesh Regions for a Better Analysis\" - poradnik wideo autorstwa ([Joko Engineering](https://www.youtube.com/watch?v=X5RVe2SDPvw))





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM MeshRegion/pl
