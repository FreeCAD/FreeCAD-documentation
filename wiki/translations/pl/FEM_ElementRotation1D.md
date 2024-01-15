---
 GuiCommand:
   Name: FEM ElementRotation1D
   Name/pl: MES: Obrót belki
   MenuLocation: Model , Geometria elementu , Obrót belki
   Workbenches: FEM_Workbench/pl
   SeeAlso: FEM_tutorial/pl
---

# FEM ElementRotation1D/pl



## Opis

**ElementRotation1D** jest używany do obrócenia przekroju poprzecznego belki wokół osi elementów belkowych.



## Użycie

1.  Jest kilka sposobów wywołania tej komendy:
    -   Wciśnij przycisk **<img src="images/FEM_ElementRotation1D.svg" width=16px> [Obrót belki](FEM_ElementRotation1D/pl.md)** button.
    -   Wybierz opcję **Model → Geometria elementu → <img src="images/FEM_ElementRotation1D.svg" width=16px> Obrót belki** z menu.
2.  Podaj kąt obrotu przekroju poprzecznego belki.



## Opcje



## Właściwości



## Ograniczenia

-   Obecnie nie są wspierane różne obroty w jednym modelu *(jeden obrót jest zadawany na wszystkie belki w modelu)*.



## Uwagi

-   Aby zwizualizować obrócony przekrój, należy ustawić `Beam Shell Result Output 3D` w [solverze CalculiX](FEM_SolverCalculixCxxtools/pl.md) na wartość {{True/pl}} i uruchomić analizę.





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ElementRotation1D/pl
