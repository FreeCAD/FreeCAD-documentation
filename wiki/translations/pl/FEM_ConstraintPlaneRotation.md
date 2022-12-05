---
- GuiCommand:/pl
   Name:FEM ConstraintPlaneRotation
   Name/pl:MES: Zdefiniuj obrót w płaszczyźnie
   MenuLocation:Model → Wiązania geometryczne → Zdefiniuj obrót w płaszczyźnie
   Workbenches:[środowisko pracy MES](FEM_Workbench/pl.md)
   SeeAlso:[Zdefiniuj odkształcenia](FEM_ConstraintTransform/pl.md)
---

# FEM ConstraintPlaneRotation/pl

## Opis

Tworzy wiązanie metodą elementów skończonych, aby węzły na powierzchni płaskiej znajdowały się w tej samej płaszczyźnie.

## Użycie

1.  Istnieje kilka sposobów na wywołanie polecenia:
    -   Naciśnij przycisk **<img src="images/FEM_ConstraintPlaneRotation.svg" width=16px> '''Zdefiniuj obrót w płaszczyźnie'''** na pasku narzędzi.
    -   Wybierz opcję z menu **Model → Wiązania geometryczne → <img src="images/FEM_ConstraintPlaneRotation.svg" width=16px> Zdefiniuj obrót w płaszczyźnie**.
2.  W oknie [widoku 3D](3D_view/pl.md) wybierz obiekt, do którego ma być zastosowane wiązanie, może to być ściana.

## Ograniczenia

1.  Wiązanie obrotu w płaszczyźnie może być zastosowane tylko do jednej ściany płaskiej.
2.  Jeśli wiązanie obrotu w płaszczyźnie zostanie zastosowane do tej samej ściany co wiązanie przemieszczenia / stałości, pierwszeństwo ma wiązanie przemieszczenia /stałości.

## Uwagi

1.  Wiązanie to wykorzystuje kartę \*MPC w programie CalculiX. Karta ta jest szczegółowo opisana na stronie <http://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node220.html>





{{FEM Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintPlaneRotation/pl
