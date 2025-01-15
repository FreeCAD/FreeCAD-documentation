---
 GuiCommand:Container|
{{GuiCommand/pl
   Name: FEM ConstraintSectionPrint
   Name/pl: MES: Zapis wyników z przekroju
   MenuLocation:  Model , Cechy geometryczne analizy , Zapis wyników z przekroju
   Workbenches: FEM_Workbench/pl
   Version: 0.19
   SeeAlso: 
}}
{{GuiCommandFemInfo/pl
   Solvers: CalculiX
}}
---

# FEM ConstraintSectionPrint/pl



## Opis

Zapisuje wstępnie zdefiniowane zmienne wyjściowe z modelu *(siły i momenty)* do pliku danych.


{{Version/pl|1.0}}

: Może też zapisać strumień ciepła i naprężenia od siły oporu (te ostatnie wymagają wsparcia dla analiz przepływowych 3D w CalculiX, które nie zostały jeszcze zaimplementowane).



## Użycie

1.  Istnieje kilka sposobów na wywołanie tego polecenia:
    -   Naciśnij przycisk **<img src="images/FEM_ConstraintSectionPrint.svg" width=16px> '''Funkcja zapisu wyników z przekroju'''** .
    -   Wybierz opcję z menu **Model → Cechy geometryczne analizy → <img src="images/FEM_ConstraintSectionPrint.svg" width=16px> Funkcja zapisu wyników z przekroju**.

2.  Wciśnij przycisk **Dodaj** i wybierz jedną powierzchnię, dla której będą zapisywane dane wyjściowe.

3.  
    <small>(v1.0)</small> : Z listy *Zmienna*, wybierz zmienną, którą chcesz zapisać: *Section Force* (siły przekrojowe), *Heat Flux* (strumień ciepła) lub *Drag Stress* (naprężenia od siły oporu, aktualnie niewspierane).



## Uwagi

-   To narzędzie wykorzystuje słowo kluczowe \*SECTION PRINT w CalculiX.





{{FEM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintSectionPrint/pl
