---
 GuiCommand:Container|
{{GuiCommand/pl
   Name: FEM ConstraintPlaneRotation
   Name/pl: MES: Zdefiniuj obrót w płaszczyźnie
   MenuLocation: Model , Funkcje analizy geometrycznej , Zdefiniuj obrót w płaszczyźnie
   Workbenches: FEM_Workbench/pl
   SeeAlso: FEM_ConstraintTransform/pl
}}
{{GuiCommandFemInfo/pl
   Solvers: CalculiX
}}
---

# FEM ConstraintPlaneRotation/pl



## Opis

Tworzy wiązanie wielopunktowe *(MPC)* w celu utrzymania węzłów leżących na płaskiej powierzchni na tej samej płaszczyźnie.



## Użycie

1.  Istnieje kilka sposobów na wywołanie tego polecenia:
    -   Naciśnij przycisk **<img src="images/FEM_ConstraintPlaneRotation.svg" width=16px> '''Wiązanie MPC typu płaszczyzna'''** na pasku narzędzi.
    -   Wybierz opcję z menu **Model → Funkcje analizy geometrycznej → <img src="images/FEM_ConstraintPlaneRotation.svg" width=16px> Wiązanie MPC typu płaszczyzna**.
2.  W oknie [widoku 3D](3D_view/pl.md) wybierz obiekt, do którego ma być zastosowane wiązanie MPC, może to być tylko pojedyncza ściana.
3.  Wciśnij przycisk **Dodaj**.



## Ograniczenia

1.  Wiązanie wielopunktowe w płaszczyźnie może być zastosowane tylko do jednej ściany płaskiej.
2.  Jeśli wiązanie wielopunktowe w płaszczyźnie zostanie zastosowane do tej samej ściany co wiązanie przemieszczenia / stały warunek brzegowy, pierwszeństwo ma wiązanie przemieszczenia / stały warunek brzegowy.



## Uwagi

1.  Wiązanie to wykorzystuje [słowo kluczowe \*MPC w CalculiX](http://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node220.html).





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintPlaneRotation/pl
