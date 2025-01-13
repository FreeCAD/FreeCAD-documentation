---
 GuiCommand:
   Name: FEM ResultsPurge
   Name/ru: FEM ResultsPurge
   MenuLocation: Results , Purge results
   Workbenches: FEM_Workbench/ru
   Shortcut: **S** **S**
   SeeAlso: FEM_tutorial/ru
---

# FEM ResultsPurge/ru


</div>



## Описание

**FEM ResultsPurge** deletes all [result objects](FEM_ResultShow.md) and all result meshes from the active analysis container in the [Tree view](Tree_view.md).


<small>(v1.1)</small> 

: Deletes all output objects from all solvers (CalculiX results objects, pipelines, filters and text reports).

If you only want to delete a result object and keep the result mesh, create a copy of the result mesh, then select the Result object in the tree view and delete it by pressing **Del**. This way the created copy of the mesh will remain. (Using FEM ResultsPurge would also delete the copy.)



## Применение

There are several ways to invoke the command:

-   Press the **<img src="images/FEM_ResultsPurge.svg" width=16px> [Purge results](FEM_ResultsPurge.md)** button.
-   Select the **Results → <img src="images/FEM_ResultsPurge.svg" width=16px> Purge results** option from the menu.
-   Use the keyboard shortcut: **R** then **P**.


<div class="mw-translate-fuzzy">





</div>


{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ResultsPurge/ru
