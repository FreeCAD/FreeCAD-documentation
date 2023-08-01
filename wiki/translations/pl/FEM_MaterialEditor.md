---
- GuiCommand:
   Name: FEM MaterialEditor
   MenuLocation: Model - Materials - Material editor
   Workbenches: [FEM](FEM_Workbench.md), [Arch](Arch_Workbench.md)
   Version: 0.18
   SeeAlso: [Arch SetMaterial](Arch_SetMaterial.md), [FEM tutorial](FEM_tutorial.md)
---

# FEM MaterialEditor/pl

## Description

The **Material Editor** allows you to edit and save the information contained in a [FreeCAD material](Material.md). Currently such materials are used by the <img alt="" src=images/Workbench_FEM.svg  style="width:24px;"> [FEM](FEM_Workbench.md) and <img alt="" src=images/Workbench_Arch.svg  style="width:24px;"> [Arch](Arch_Workbench.md) workbenches.

![](images/Material_editor.png )

## Usage

The material editor can currently be accessed by either:

1.  <img alt="" src=images/Workbench_Arch.svg  style="width:24px;"> [Arch Workbench](Arch_Workbench.md):
    -   The **<img src="images/Arch_SetMaterial.svg" width=16px> [Material](Arch_SetMaterial.md)** button.
    -   The menu **Arch → Material tools → <img src="images/Arch_SetMaterial.svg" width=16px> Material** entry.
2.  <img alt="" src=images/Workbench_FEM.svg  style="width:24px;"> [FEM Workbench](FEM_Workbench.md):
    -   The **<img src="images/FEM_MaterialEditor.svg" width=16px> [Material editor](FEM_MaterialEditor.md)** button.
    -   The menu **Model → Materials → <img src="images/FEM_MaterialEditor.svg" width=16px> Material editor** entry.

## Options

-   **Browser button**: Opens the contents of the URL property in a browser

-   **Material card**: Allows to choose a preset to fill in the fields

-    **Open**: Opens a .FCMat file

-    **Save as**: Saves the contents of the editor as a new .FCMat file

-   **Preview**: Not implemented yet

-   **Properties editor**: Allows to edit the contents of the material properties

-    **Add property**: Allows to add a new custom property

-    **Delete property**: Deletes a selected property. Only custom properties can be deleted

## Notes

-   The **OK** and **Cancel** buttons have the same effect when the Material editor is not used to edit directly the material property of an existing object.





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM MaterialEditor/pl
