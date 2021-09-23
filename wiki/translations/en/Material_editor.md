---
- GuiCommand:
   Name:Material editor
   Icon:Arch_Material_Group.svg
   MenuLocation:Model → Material → Material editor
   Workbenches:[FEM](FEM_Workbench.md), [Arch](Arch_Workbench.md)
   Version:0.18
   SeeAlso:[Material](Material.md), [Arch SetMaterial](Arch_SetMaterial.md), [FEM tutorial](FEM_tutorial.md)
---

# Material editor/en

## Description

The Material Editor allows you to edit and save the information contained in a [FreeCAD material](Material.md). Currently such materials are used by the **<img src="images/Workbench_FEM.svg" width=24px> [FEM](FEM_Workbench.md)** and **<img src="images/Workbench_Arch.svg" width=24px> [Arch](Arch_Workbench.md)** workbenches.

![](images/Material_editor.jpg )

## Usage

The material editor can currently be accessed by either:

1.  <img alt="" src=images/Workbench_Arch.svg  style="width:24px;"> [Arch Workbench](Arch_Workbench.md)
    -   The <img alt="" src=images/Arch_SetMaterial.svg  style="width:16px;"> [Set Material](Arch_SetMaterial.md) button of the [New material](Arch_SetMaterial.md) creation panel of the [Arch Workbench](Arch_Workbench.md)
    -   The menu **Arch → Set material...** entry
2.  <img alt="" src=images/Workbench_FEM.svg  style="width:24px;"> [FEM Workbench](FEM_Workbench.md)
    -   The <img alt="" src=images/Arch_Material_Group.svg  style="width:16px;"> [Material editor](Material_editor.md) icon
    -   The menu **Models → Material → Material editor** entry
3.  Via python (see [Scripting](#Scripting.md) section below)

## Options

-   **Browser button**: Opens the contents of the URL property in a browser

-   **Material card**: Allows to choose a preset to fill in the fields

-    **Open**: Opens a .FCMat file

-    **Save as**: Saves the contents of the editor as a new .FCMat file

-   **Preview**: Not implemented yet

-   **Properties editor**: Allows to edit the contents of the material properties

-    **Add property**: Allows to add a new custom property

-    **Delete property**: Deletes a selected property. Only custom properties can be deleted

Note:

-   The **OK** and **Cancel** buttons have the same effect when the Material editor is not used to edit directly the material property of an existing object.

## Scripting


```python
import MaterialEditor
MaterialEditor.openEditor()
```





{{FEM Tools navi

}}

---
[documentation index](../README.md) > [Material](Material_Workbench.md) > Material editor/en
