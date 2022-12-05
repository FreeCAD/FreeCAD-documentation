---
- GuiCommand:/pl
   Name:Mesh FillInteractiveHole
   Name/pl:Siatka: Interaktywne wypełnienie otworów
   MenuLocation:Meshes → Zamknij otwór
   Workbenches:[Siatka](Mesh_Workbench/pl.md)
   SeeAlso:[Wypełnienie otworów](Mesh_FillupHoles/pl.md), [Dodaj trójkąt](Mesh_AddFacet/pl.md)
---

# Mesh FillInteractiveHole/pl

## Opis

Polecenie **Zamknij otwór** wypełnia wybrane otwory w obiektach siatkowych.

## Użycie

1.  Istnieje kilka sposobów na wywołanie polecenia:
    -   Naciśnij przycisk **<img src="images/Mesh_FillInteractiveHole.svg" width=16px> [Zamknij otwór](Mesh_FillInteractiveHole/pl.md)**.
    -   Wybierz z menu opcję **Siatki → <img src="images/Mesh_FillInteractiveHole.svg" width=16px> Zamknij otwór**.
2.  Kursor zmienia wygląd na ikonę trójkąta.
3.  Wybierz ścianę, która ma wspólną krawędź z otworem, który chcesz zamknąć.
4.  Otwór zostanie zamknięty.
5.  Opcjonalnie powtórz to, aby zamknąć kolejne otwory.
6.  W razie potrzeby możesz użyć [Cofnij](Std_Undo/pl.md) aby cofnąć ostatnie działanie polecenia.
7.  Wybierz opcję **Opuść tryb wypełnienie otworu** z menu kontekstowego okna [widoku 3D](3D_view/pl.md), aby zakończyć polecenie.

## Uwagi

-   Jeśli krawędzie otworu nie leżą w tej samej płaszczyźnie, wynik polecenia może zależeć od wybranej ściany.





{{Mesh Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Mesh](Mesh_Workbench.md) > Mesh FillInteractiveHole/pl
