---
 GuiCommand:
   Name: FEM MeshDisplayInfo
   Name: MES: Wyświetl informacje o siatce MES
   MenuLocation: Menu podręczne na obiekcie siatki , Wyświetl informacje o siatce MES
   Workbenches: FEM_Workbench/pl
   SeeAlso: FEM_tutorial/pl
---

# FEM MeshDisplayInfo/pl



## Opis

Wyświetla podstawowe statystyki istniejącej siatki - liczbę węzłów i elementów każdego typu. Dokładniej, całkowite liczby następujących cech są podawane:

-   Węzły,
-   Krawędzie,
-   Ściany,
-   Wielokąty,
-   Objętości,
-   Wielościany,

\* Krawędzie liniowe,

-   Ściany liniowe,
-   Objętości liniowe,

\* Krawędzie kwadratowe,

-   Ściany kwadratowe,
-   Trójkąty kwadratowe,
-   Czworoboki kwadratowe,
-   Objętości kwadratowe,
-   Prostopadłościany kwadratowe,
-   Czworościany kwadratowe,
-   Pięcościany kwadratowe,
-   Piramidki kwadratowe.



## Użycie

1.  Najpierw utwórz siatkę MES *(używając jednej z dostępnych technik)*.
2.  Zaznacz siatkę w [widoku drzewa](Tree_view/pl.md).
3.  Kliknij na niej prawym przyciskiem myszy i wybierz opcję **<img src="images/FEM_MeshDisplayInfo.svg" width=16px> [Wyświetl informacje o siatce MES](FEM_MeshDisplayInfo/pl.md)**.
4.  Aby zamknąć okno FEM Mesh Info, wciśnij przycisk **OK**.



## Skrypty


{{code|code=
# setup some model with a fem mesh to print information from
from femexamples.ccx_cantilever_faceload import setup
setup()
# print the fem mesh information
print(App.ActiveDocument.Mesh.FemMesh)
}}

da następujący wynikː


{{code|code=
>>> print(App.ActiveDocument.Mesh.FemMesh)
========================== Dump contents of mesh ==========================


1) Total number of nodes:       228
2) Total number of edges:       0
3) Total number of faces:       0
4) Total number of polygons:    0
5) Total number of volumes:     79
6) Total number of polyhedrons: 0

7) Total number of linear edges:    0
8) Total number of linear faces:    0
9) Total number of linear volumes:  0

10) Total number of quadratic edges:    0
11) Total number of quadratic faces:    0
12) Total number of quadratic volumes:  79
12.1) Number of quadratic hexahedrons:  0
12.2) Number of quadratic tetrahedrons: 79
12.3) Number of quadratic prisms:       0
12.4) Number of quadratic pyramids:     0

===========================================================================
}}





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM MeshDisplayInfo/pl
