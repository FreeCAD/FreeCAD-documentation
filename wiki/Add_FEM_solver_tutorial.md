# Add FEM solver tutorial



 


{{TutorialInfo
|Topic= Add FEM Solver
|Level= 
|Time= 
|Author=[M42kus](User:M42kus.md)
|FCVersion=
|Files=
}}

## Introduction

In this tutorial we will take the **Mystran** solver as an example to show how to add a solver to FreeCAD. Please make sure you have read and understood [Extend FEM Module](Extend_FEM_Module.md) before reading this tutorial. The detail of adding the Mystran Solver to FreeCAD master: <https://github.com/FreeCAD/FreeCAD/compare/a03eb6b9625ba>\...dfc01ec949525

The task can be split into seven parts:

-   **Mesh exporter**. Write out Mesh or Case file from FreeCAD to the solver.
-   **Results importer**. Read the solver\'s result file back to FreeCAD.
-   **Solver object**. Needs changes in solver settings, unit tests, ObjectsFem modules as well.
-   **Task and writer module**. Here is where the main solver input writing happens.
-   **Gui tool to create a solver**.
-   **Gui preference tab to set the solver binary path**.
-   **A solver input writing unit test**. Best to take the ccx cantilever. This is available for all mesh element types.



[Category:FEM](Category:FEM.md)
