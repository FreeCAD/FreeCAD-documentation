---
- GuiCommand:
   Name: FEM MeshClear
   Name/pl: MES: Wyczyść dane siatki
   MenuLocation: Menu podręczne na obiekcie siatki -> Wyczyść dane siatki MES
   Workbenches: FEM_Workbench/pl
   SeeAlso: FEM_tutorial/pl
---

# FEM MeshClear/pl

## Opis

Umożliwia użytkownikowi ponowną inicjalizację siatki z obiektu siatki FreeCAD MES. Siatka nadal istnieje, ale nie ma żadnych wierzchołków, krawędzi, powierzchni ani elementów. Informacje o siatce, parametry Netgen / Gmsh, regiony siatki, grupy siatki i warstwa brzegowa siatki pozostają w Drzewie modelu, co oznacza, że siatkę można odtworzyć później. Głównym zastosowaniem tej funkcji jest rozjaśnienie pliku FreeCAD w celu zwiększenia wydajności podczas korzystania z programu FreeCAD, zaoszczędzenia miejsca na dysku lub umożliwienia łatwego przenoszenia plików bez utraty danych o siatkach.

## Użycie

1.  Kliknij prawym przyciskiem myszy na Obiekt siatki MES <img alt="" src=images/FEM_MeshNetgenFromShape.svg  style="width:16px;"> [Netgen](FEM_MeshNetgenFromShape/pl.md) lub <img alt="" src=images/FEM_MeshGmshFromShape.svg  style="width:16px;"> [Gmsh](FEM_MeshGmshFromShape/pl.md) w oknie [widoku drzewa](Tree_view/pl.md).
2.  Wybierz opcję **<img src="images/FEM_MeshClear.svg" width=16px> Wyczyść dane siatki MES** z menu podręcznego .

## Uwagi

Obiekty w drzewie modelu są zachowane, ponieważ reprezentują dane siatki, ale siatka jest teraz usuwana z pliku FreeCAD.





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM MeshClear/pl
