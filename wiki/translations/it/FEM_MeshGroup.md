# FEM MeshGroup/it
---
- GuiCommand:   Name: FEM_MeshGroup   Name/it: FEM MeshGroup   MenuLocation:  Mesh - FEM Mesh group   |Workbenches: [Shortcut:    SeeAlso: [[FEM_tutorial/it|Tutorial FEM](FEM_Workbench/it___FEM]].md)---

## Descrizione


<div class="mw-translate-fuzzy">

Da fare


</div>

FEM MeshGroup therefore enables FreeCAD to be used with external solvers (or viewers such as ParaView) when they are not yet implemented with their own case-writing routine within FreeCAD.

## Utilizzo

1.  To enable the function a mesh must be first provided <img alt="" src=images/FEM_MeshGmshFromShape.svg  style="width:24px;"> [FEM mesh from shape by Gmsh](FEM_MeshGmshFromShape.md)
2.  Then select the Mesh object in the [Tree view](Tree_view.md) and either
    -   Press the <img alt="" src=images/FEM_MeshGroup.svg  style="width:24px;"> button in the FEM toolbar
    -   Select the **Mesh → <img src="images/FEM_MeshGroup.svg" width=24px> FEM mesh group** option from the drop-down menu.
3.  Select whether the group is named or labeled
    -   If **Name** is selected, the name of the MeshGroup is used when exporting the mesh.
    -   If **Label** is selected, the specified label name will be used when exporting the mesh.
4.  Click the **OK** button.
5.  Close the task.

    :   Result: You now should see a new `FEMMeshGroup` object under the `FEMMeshGMSH` object in your active analysis container.
6.  Double-click on the `FEMMeshGMSH` parent object in your Model Tree and press **Apply** to force a mesh recalculation / relabeling.
7.  Close the task.

## Notes

-   After the mesh has been created you can change the label property using the [property editor](Property_editor.md).
-   After you changed a property, you must reopen the Gmsh dialog again and click the **Apply** button. (You can leave the dialog open while changing properties.)
-   You can create as many different mesh groups as needed.





{{FEM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > FEM MeshGroup/it
