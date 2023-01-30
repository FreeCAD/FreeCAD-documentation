---
- GuiCommand:
   Name:FEM ResultsPurge
   MenuLocation:Results → Purge results
   Workbenches:[FEM](FEM_Workbench.md)
   Shortcut:**R** **P**
   SeeAlso:[FEM tutorial](FEM_tutorial.md)
---

# FEM ResultsPurge

## Description

**FEM ResultsPurge** deletes all [result objects](FEM_ResultShow.md) and all result meshes from the active analysis container in the [Tree view](Tree_view.md).

If you only want to delete a result object and keep the result mesh, create a copy of the result mesh, then select select the Result object in the tree view and delete it by pressing **Del**. This way the created copy of the mesh will remain. (Using FEM ResultsPurge would also delete the copy.)

## Usage

Either press the **<img src="images/FEM_ResultsPurge.svg" width=16px> '''Purge results'''** button or use the menu **Results → <img src="images/FEM_ResultsPurge.svg" width=16px> Purge results** (shortcut **R** then **P**).




 {{FEM Tools navi}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ResultsPurge
