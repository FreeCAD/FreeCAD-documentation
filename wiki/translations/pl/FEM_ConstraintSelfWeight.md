---
 GuiCommand:
   Name: FEM ConstraintSelfWeight
|Name/pɬMES Obciążenie grawitacją
   MenuLocation: Model , Warunki brzegowe i obciążenia mechaniczne , Obciążenie grawitacją
   Workbenches: FEM_Workbench/pl
   SeeAlso: FEM_tutorial/pl
---

# FEM ConstraintSelfWeight/pl



## Opis

Definiuje przyspieszenie grawitacyjne o wartości 9,81 m/s² działające na cały model w wybranym kierunku.



## Użycie

1.  Jest kilka sposobów wywołania tej komendy:
    -   Wciśnij przycisk **<img src="images/FEM_ConstraintSelfWeight.svg" width=16px> [Obciążenie grawitacją](FEM_ConstraintSelfWeight/pl.md)** button.
    -   Wybierz opcję **Model → Warunki brzegowe i obciążenia mechaniczne → <img src="images/FEM_ConstraintSelfWeight.svg" width=16px> Obciążenie grawitacją** z menu.
2.  Możesz zmodyfikować kierunek obciążenia grawitacyjnego poprzez zmianę jego współrzędnych wektorowych w oknie właściwości nowo utworzonego obiektu ConstraintSelfWeight.



## Skrypty

Nowy obiekt:


```python
import ObjectsFem
ObjectsFem.makeConstraintSelfWeight(name)
```

Dodaj obiekt do analizy o nazwie Analysis:


```python
App.ActiveDocument.Analysis.Member = App.ActiveDocument.Analysis.Member + [(object)]
```

Przykładː


```python
import ObjectsFem
selfweight_obj = ObjectsFem.makeConstraintSelfWeight("MySelfWeightObject")
App.ActiveDocument.Analysis.Member = App.ActiveDocument.Analysis.Member + [selfweight_obj]
```

## Solver CalculiX 



### Ograniczenia

-   Aby zmienić wartość przyspieszenia grawitacyjnego, musisz edytować plik .inp.
-   Obciążenie grawitacją jest nakładane na zbiór elementów Eall, w którego skład wchodzą wszystkie elementy siatki modelu.



### Edycja pliku .inp CalculiXa 

Wartość przyspieszenia można ręcznie zmienić po wygenerowaniu pliku .inp.

Przykład linii w pliku .inpː


```python
*DLOAD
Eall,GRAV,9810,0.0,0.0,-1.0
```

gdzie 9810 to wartość przyspieszenia grawitacyjnego w \[mm/s\^2\], zaś 0,0,-1 to wektor kierunku. Wartość można ustawić jako wielokrotność standardowego przyspieszenia grawitacyjnego, aby symulować obciążenie np. 4 g.

## Solver Z88 

-   To obciążenie nie jest obecnie zaimplementowane w solverze Z88.





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintSelfWeight/pl
