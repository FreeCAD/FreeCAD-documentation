---
 GuiCommand:Container|
{{GuiCommand/pl
   Name: FEM ElementRotation1D
   Name/pl: MES: Obrót belki
   MenuLocation: Model , Geometria elementu , Obrót belki
   Workbenches: FEM_Workbench/pl
   SeeAlso: FEM_tutorial/pl
}}
{{GuiCommandFemInfo/pl
   Solvers: CalculiX
}}
---

# FEM ElementRotation1D/pl



## Opis

**ElementRotation1D** jest używany do obrócenia przekroju poprzecznego belki wokół osi elementów belkowych.



## Użycie

1.  Jest kilka sposobów wywołania tej komendy:
    -   Wciśnij przycisk **<img src="images/FEM_ElementRotation1D.svg" width=16px> [Obrót belki](FEM_ElementRotation1D/pl.md)** button.
    -   Wybierz opcję **Model → Geometria elementu → <img src="images/FEM_ElementRotation1D.svg" width=16px> Obrót belki** z menu.
2.  Podaj kąt obrotu przekroju poprzecznego belki.



## Właściwości


**Rotation**

: określa kąt obrotu.



## Ograniczenia

-   Obecnie nie są wspierane różne obroty w jednym modelu *(jeden obrót jest zadawany na wszystkie belki w modelu)*.



## Uwagi

-   Aby zwizualizować obrócony przekrój, należy ustawić `Beam Shell Result Output 3D` w [solverze CalculiX](FEM_SolverCalculixCxxtools/pl.md) na wartość {{True/pl}} i uruchomić analizę.
-   To narzędzie korzysta ze [słowa kluczowego \*BEAM SECTION w CalculiX](https://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node162.html).





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ElementRotation1D/pl
