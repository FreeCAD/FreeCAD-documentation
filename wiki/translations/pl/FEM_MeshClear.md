---
 GuiCommand:
   Name: FEM MeshClear
   Name/pl: MES: Wyczyść dane siatki
   MenuLocation: Menu podręczne na obiekcie siatki , Wyczyść dane siatki MES
   Workbenches: FEM_Workbench/pl
   SeeAlso: FEM_tutorial/pl
---

# FEM MeshClear/pl



## Opis

Umożliwia użytkownikowi ponowną inicjalizację siatki z obiektu siatki MES FreeCAD. Siatka nadal istnieje, ale nie ma żadnych wierzchołków, krawędzi, powierzchni ani elementów. Informacje o siatce, parametry Netgen / Gmsh, obszary siatki, grupy siatki i warstwa graniczna siatki pozostają w drzewie modelu, co oznacza, że siatkę można odtworzyć później. Głównym zastosowaniem tej funkcji jest zmniejszenie rozmiaru pliku FreeCAD w celu zwiększenia wydajności podczas pracy w programie, zaoszczędzenia miejsca na dysku lub umożliwienia łatwego przenoszenia plików bez utraty danych o siatkach.



## Użycie

1.  Kliknij prawym przyciskiem myszy na obiekcie siatki MES <img alt="" src=images/FEM_MeshNetgenFromShape.svg  style="width:16px;"> [Netgen](FEM_MeshNetgenFromShape/pl.md) lub <img alt="" src=images/FEM_MeshGmshFromShape.svg  style="width:16px;"> [Gmsh](FEM_MeshGmshFromShape/pl.md) w [widoku drzewa](Tree_view/pl.md).
2.  Wybierz opcję **<img src="images/FEM_MeshClear.svg" width=16px> Wyczyść dane siatki MES** z menu podręcznego .



## Uwagi

Obiekty w drzewie modelu są zachowane, ponieważ reprezentują dane siatki, ale siatka jest usunięta z pliku FreeCAD.





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM MeshClear/pl
