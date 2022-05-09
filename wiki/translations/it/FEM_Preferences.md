# FEM Preferences/it
{{TOCright}}


<div class="mw-translate-fuzzy">

Le finestre delle preferenze di [FEM ](FEM_Workbench/it.md) si trovano nell\'[Editor delle Preferenze](Preferences_Editor/it.md), **Modifica → Preferenze → Fem**.


</div>


<div class="mw-translate-fuzzy">

Sono disponibili cinque schede, una per la configurazione generale dell\'ambiente.


</div>

The current supported external solvers are   *

-   <img alt="" src=images/FEM_SolverCalculixCxxtools.svg  style="width   *32px;"> [CalculiX](FEM_SolverCalculixCxxtools.md)
-   <img alt="" src=images/FEM_SolverElmer.svg  style="width   *32px;"> [Elmer](FEM_SolverElmer.md)
-   <img alt="" src=images/FEM_SolverMystran.svg  style="width   *32px;"> [Mystran](FEM_SolverMystran.md) <small>(v0.20)</small> 
-   <img alt="" src=images/FEM_SolverZ88.svg  style="width   *32px;"> [Z88](FEM_SolverZ88.md)

## Generale

On the *General* tab you can specify the following   *

![](images/Preference_Fem_Tab_01.png )

## Gmsh

On the *Gmsh* tab you can specify the following   *

+++
| Name                                               | Description                                                                                                           |
+====================================================+=======================================================================================================================+
|                                     | If checked, FreeCAD will look for the binary of [Gmsh](FEM_MeshGmshFromShape.md) in known (usual) directories |
| **Search in known binary directories** |                                                                                                                       |
|                                                 |                                                                                                                       |
+++
|                                     | The path to the the binary of [Gmsh](FEM_MeshGmshFromShape.md)                                                |
| **Gmsh binary path**                   |                                                                                                                       |
|                                                 |                                                                                                                       |
+++

![](images/Preference_Fem_Tab_03.png )

## CalculiX

On the *CalculiX* tab you can specify the following   *

![](images/Preference_Fem_Tab_02.png )

## Elmer

On the *Elmer* tab you can specify the following   *

+++
| Name                                                            | Description                                                                                                                                     |
+=================================================================+=================================================================================================================================================+
|                                                  | If checked, FreeCAD will look for the binary of the grid writer utility of the [Elmer](FEM_SolverElmer.md) in known (usual) directories |
| **ElmerGrid   * Search in known binary directories**   |                                                                                                                                                 |
|                                                              |                                                                                                                                                 |
+++
|                                                  | The path to the the binary of the grid writer utility of the [Elmer](FEM_SolverElmer.md)                                                |
| **ElmerGrid binary path**                           |                                                                                                                                                 |
|                                                              |                                                                                                                                                 |
+++
|                                                  | If checked, FreeCAD will look for the solver binary of [Elmer](FEM_SolverElmer.md) in known (usual) directories                         |
| **ElmerSolver   * Search in known binary directories** |                                                                                                                                                 |
|                                                              |                                                                                                                                                 |
+++
|                                                  | The path to the the solver binary of [Elmer](FEM_SolverElmer.md)                                                                        |
| **ElmerSolver binary path**                         |                                                                                                                                                 |
|                                                              |                                                                                                                                                 |
+++

![](images/Preference_Fem_Tab_05.png )

## Mystran

On the *Mystran* tab you can specify the following   *

+++
| Name                                               | Description                                                                                                              |
+====================================================+==========================================================================================================================+
|                                     | If checked, FreeCAD will look for the binary of the [Mystran](FEM_SolverMystran.md) in known (usual) directories |
| **Search in known binary directories** |                                                                                                                          |
|                                                 |                                                                                                                          |
+++
|                                     | The path to the the binary of the [Mystran](FEM_SolverMystran.md)                                                |
| **Mystran binary path**                |                                                                                                                          |
|                                                 |                                                                                                                          |
+++

![](images/Preference_Fem_Tab_Mystran.png )

## Z88

On the *Z88* tab you can specify the following   *

+++
| Name                                               | Description                                                                                                                                                                                                               |
+====================================================+===========================================================================================================================================================================================================================+
|                                     | If checked, FreeCAD will look for the binary named *z88r* of the [Z88 solver](FEM_SolverZ88.md) in known (usual) directories                                                                                      |
| **Search in known binary directories** |                                                                                                                                                                                                                           |
|                                                 |                                                                                                                                                                                                                           |
+++
|                                     | The path to the the binary named *z88r* of the [Z88 solver](FEM_SolverZ88.md)                                                                                                                                     |
| **z88r binary path**                   |                                                                                                                                                                                                                           |
|                                                 |                                                                                                                                                                                                                           |
+++
|                                     | The solver method used by the [Z88 solver](FEM_SolverZ88.md) for new simulations.                                                                                                                                 |
| **Solver method**                      |                                                                                                                                                                                                                           |
|                                                 |                                                                                                                                                                                                                           |
+++
|                                     | This is relevant when the solver method *Simple Cholesky* is used. After starting the solver, it might tell you that you need to increase the *MAXGS* value. In this case increase the max places and re-run the solver.  |
| **Max places in stiffness matrix**     |                                                                                                                                                                                                                           |
|                                                 |                                                                                                                                                                                                                           |
+++
|                                     | This is relevant when one of the iterative solver methods is used. After starting the solver, it might tell you that you need to increase the *MAXKOI* value. In this case increase the max places and re-run the solver. |
| **Max places in coincidence vector**   |                                                                                                                                                                                                                           |
|                                                 |                                                                                                                                                                                                                           |
+++

![](images/Preference_Fem_Tab_04.png )

## Material

On the *Material* tab you can specify the following   *

+++
| Name                                                                                          | Description                                                                                                                                                                                           |
+===============================================================================================+=======================================================================================================================================================================================================+
|                                                                                | The cards built-in to FreeCAD will be listed as available.                                                                                                                                            |
| **Use built-in materials**                                                        |                                                                                                                                                                                                       |
|                                                                                            |                                                                                                                                                                                                       |
+++
| \\AppData\\Roaming\\FreeCAD\\Material* |
| **Use materials from Materials directory in user's FreeCAD preference directory** |                                                                                                                                                                                                       |
|                                                                                            |                                                                                                                                                                                                       |
+++
|                                                                                | Also material cards also from the specified directory will be listed as available.                                                                                                                    |
| **Use materials from user defined directory**                                     |                                                                                                                                                                                                       |
|                                                                                            |                                                                                                                                                                                                       |
+++
|                                                                                | Duplicate cards will be deleted from the displayed material card list.                                                                                                                                |
| **Delete card duplicates**                                                        |                                                                                                                                                                                                       |
|                                                                                            |                                                                                                                                                                                                       |
+++
|                                                                                | Material cards will appear sorted by their resources (locations). If unchecked, they will be sorted by their name.                                                                                    |
| **Sort by resources**                                                             |                                                                                                                                                                                                       |
|                                                                                            |                                                                                                                                                                                                       |
+++

![](images/Preference_Fem_Tab_Material.png )


{{FEM Tools navi

}} 

[Category   *Preferences](Category_Preferences.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Preferences](Category_Preferences.md) > [FEM](Category_FEM.md) > FEM Preferences/it
