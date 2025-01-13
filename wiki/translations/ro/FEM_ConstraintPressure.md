# FEM ConstraintPressure/ro
---
 GuiCommand:   Name: FEM ConstraintPressure   Name/ro: FEM ConstraintPressure   MenuLocation: Model , Mechanical Constraints , Constraint pressure   ---


</div>



## Descriere


<div class="mw-translate-fuzzy">

Aplică o constrângere de presiune pe o fațetă.


</div>




<div class="mw-translate-fuzzy">

## Cum se folosește 


</div>


<div class="mw-translate-fuzzy">

1.  Click pe <img alt="" src=images/FEM_ConstraintPressure.png  style="width:32px;"> sau alegeți **Model** → **Mechanical Constraints** → **<img src="images/FEM_ConstraintPressure.png" width=32px> Constraint pressure** din mediul de sus.
2.  Click on ** Add reference** și selectați fațeta în vedere 3D
3.  Editați fereastra corespunzătoare pentru a specifica presiunea în MPa
4.  Bifați caseta pentru a inversa direcția, dacă este necesar.


</div>



## Note


<div class="mw-translate-fuzzy">

Distribuția presiunii este întotdeauna uniformă și întotdeauna perpendiculară pe față.


</div>

-    {{VersionMinus|0.21}}: Pressure load can be applied to shells but only when [Gmsh](FEM_MeshGmshFromShape.md) is used for meshing and group meshing is set to true. It is hardcoded as true so the user doesn\'t have to worry about that. However, due to a bug, pressure load may require remeshing to work on shells.

-   This feature uses the [\*DLOAD card in CalculiX](https://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node190.html).





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintPressure/ro
