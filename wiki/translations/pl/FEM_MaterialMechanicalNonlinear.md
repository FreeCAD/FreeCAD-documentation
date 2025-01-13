---
 GuiCommand:Container|
{{GuiCommand/pl
   Name: FEM MaterialMechanicalNonlinear
   Name/pl: Nieliniowy materiał mechaniczny
   MenuLocation: Model , Materiały , Nieliniowy materiał mechaniczny
   Workbenches: FEM_Workbench/pl
   SeeAlso: FEM_tutorial/pl
}}
{{GuiCommandFemInfo/pl
   Solvers: CalculiX
}}
---

# FEM MaterialMechanicalNonlinear/pl



## Opis

Tworzy nieliniowy materiał mechaniczny. Obecnie dostępna jest tylko plastyczność z prostym wzmocnieniem (izotropowym). {{Version/pl|1.0}}: Dostępne jest też wzmocnienie kinematyczne.



## Użycie

1.  Aby utworzyć nowy obiekt MaterialMechanicalNonlinear, skorzystaj z jednego z następujących podejść:
    -   Dodaj najpierw **<img src="images/FEM_MaterialSolid.svg" width=16px> [Materiał dla bryły](FEM_MaterialSolid/pl.md)** i zaznacz go.
    -   Wciśnij przycisk **<img src="images/FEM_MaterialMechanicalNonlinear.svg" width=16px> '''Nieliniowy materiał mechaniczny'''** lub wybierz opcję **Model → Materiały → <img src="images/FEM_MaterialMechanicalNonlinear.svg" width=16px> Nieliniowy materiał mechaniczny‏‎** z menu.
2.  Aby edytować istniejący obiekt MaterialMechanicalNonlinear:
    -   Zaznacz go w [widoku drzewa](Tree_view/pl.md).
    -   Wybierz model materiału *(wzmocnienie izotropowe (proste) lub {{Version/pl|1.0}}: wzmocnienie kinematyczne)*.
    -   Zdefiniuj punkty z krzywej naprężenie \[MPa\] - odkształcenie plastyczne. Pierwszy punkt musi mieć zerowe odkształcenia plastyczne. Wciśnij przycisk **...** obok właściwości **Yield Points** aby wprowadzić punkty za pomocą wygodnej listy. Składnia jest opisana w sekcji [Uwagi](#Uwagi.md).



## Uwagi

-   We FreeCAD 0.19 i starszych wersjach, można wprowadzić tylko 3 punkty z krzywej naprężenie - odkształcenie plastyczne. Od wersji 0.20 lista punktów może być dowolnie długa.
-   Składnia powinna być następująca:

:   
    
```python
    stress_1, 0
    stress_2, plastic_strain_2
    ...
    
```
    





:   Z kropką jako separatorem dziesiętnym, ponieważ korzysta z niej CalculiX.





:   Przykładowo, aby zdefiniować model biliniowy ze wzmocnieniem dla stali S275:





:   
    
```python
    275, 0
    490, 0.2
    
```
    





:   Lub, aby zdefiniować idealną plastyczność bez wzmocnienia dla tego materiału:





:   
    
```python
    275, 0
    
```
    





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM MaterialMechanicalNonlinear/pl
