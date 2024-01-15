---
 GuiCommand:
   Name: FEM ElementGeometry1D
   Name/pl: MES: Przekrój poprzeczny belki
   MenuLocation: Model , Geometria elementu , Przekrój poprzeczny belki
   Workbenches: FEM_Workbench/pl
   Shortcut: **C** **B**
   SeeAlso: FEM_tutorial/pl
---

# FEM ElementGeometry1D/pl



## Opis

**ElementGeometry1D** jest używane do definiowania przekrojów poprzecznych elementów belkowych. Obecnie dostępne są następujące typy przekrojówː prostokątny, kołowy, rurowy.



## Użycie

1.  Jest kilka sposobów wywołania tej komend:
    -   Wciśnij przycisk **<img src="images/FEM_ElementGeometry1D.svg" width=16px> [Przekrój poprzeczny belki](FEM_ElementGeometry1D/pl.md)**.
    -   Wybierz opcję **Model → Geometria elementu → <img src="images/FEM_ElementGeometry1D.svg" width=16px> Przekrój poprzeczny belki** z menu.
2.  Wybierz typ przekroju i podaj wymagane wymiary:
    -   Prostokątny: szerokość i wysokość,
    -   Kołowy: średnica,
    -   Rurowy: średnica i grubość.
3.  Opcjonalnie, wciśnij przycisk **Dodaj** w panelu zadań i wybierz krawędź, do której chcesz przypisać przekrój. Jeśli żadna krawędź nie została wybrana, wszystkie pozostałe krawędzie *(bez przypisanych innych obiektów **Przekrój poprzeczny belki**)* będą automatycznie użyte.



## Opcje



## Właściwości



## Ograniczenia



## Uwagi

-   Do wyświetlania wyników z solvera CalculiX na siatce zwizualizowanej dla danego przekroju, należy ustawić właściwość `Beam Shell Result Output 3D` w [solverze CalculiX](FEM_SolverCalculixCxxtools/pl.md) na wartość {{True/pl}}.



## Skrypty





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ElementGeometry1D/pl
