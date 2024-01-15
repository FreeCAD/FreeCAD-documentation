---
 GuiCommand:
   Name: FEM MaterialFluid
   Name/pl: Materiał dla płynu
   MenuLocation: Model , Materiały , Materiał dla płynu
   Workbenches: FEM_Workbench/pl
   SeeAlso: FEM_tutorial/pl
---

# FEM MaterialFluid/pl



## Opis

Tworzy materiał dla płynu.

![](images/FEMMaterialFluidProperties.png ) 
*Okno dialogowe materiału MES.*



## Użycie

1.  Aby utworzyć nowy obiekt MaterialFluid, skorzystaj z jednego z następujących podejść:
    -   Wciśnij przycisk **<img src="images/FEM_MaterialFluid.svg" width=16px> '''Materiał dla płynu'''**.
    -   Wybierz opcję **Model → Materiały → <img src="images/FEM_MaterialFluid.svg" width=16px> Materiał dla płynu‏‎** z menu.
2.  Aby edytować istniejący obiekt MaterialFluid:
    -   Dwukrotnie kliknij na nim w [widoku drzewa](Tree_view/pl.md).
3.  Zostanie otwarte okno dialogowe materiału MES.
4.  Wybierz typ płynu. Do analiz CFD *(Computational Fluid Dynamics)* najczęściej wykorzystywane są materiały **Air** i **Water**.
5.  Jeśli definiujesz materiał płynu dla całego modelu, nie wybieraj żadnych obiektów geometrycznych *(zostaw pustą listę odniesień)*. Materiał płynu zostanie automatycznie przypisany do całego modelu. W innym wypadku, przypisz materiały płynu do wybranych części ręcznie, poprzez wybieranie ich do poszczególnych definicji materiału, ale nie zostawiaj żadnej części modelu bez definicji materiału płynu.
6.  Możesz dostosować właściwości płynu, takie jak gęstość, lepkość kinematyczna, przewodność cieplna itd. Kilka najczęściej spotykanych płynów jest już na liście i nie wymaga edycji.
7.  Jeśli wprowadzisz modyfikacje, możesz zapisać zmieniony materiał.
8.  Wciśnij przycisk **Zamknij** aby zamknąć okno dialogowe.





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM MaterialFluid/pl
