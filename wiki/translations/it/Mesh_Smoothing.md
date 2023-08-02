---
- GuiCommand:
   Name: Mesh_Smoothing
   Name/it: Mesh Smoothing
   MenuLocation: Mesh -> Leviga...
   Workbenches: Mesh_Workbench/it
---

# Mesh Smoothing/it

## Descrizione

Il comando **Leviga** smussa gli oggetti mesh cambiando la posizione dei loro vertici.

![](images/Meshes_Smooth.jpg ) 
*Il pannello delle azioni Leviga dopo aver scelto l'opzione Solo selezione*

## Utilizzo

1.  If you plan to smooth only certain areas, note that the command uses the color red to mark the faces selected for this option. To see them properly:
    -   The **Display Mode** of the mesh objects ideally should be {{Value|Flat lines}}, but should at least show faces. If necessary use the [Std DrawStyle](Std_DrawStyle.md) command to override this property.
    -   The **Shape Color** of the mesh objects should not be red.
2.  Select one or more mesh objects.
3.  There are several ways to invoke the command:
    -   Press the **<img src="images/Mesh_Smoothing.svg" width=16px> [Mesh Smoothing](Mesh_Smoothing.md)** button.
    -   Select the **Meshes → <img src="images/Mesh_Smoothing.svg" width=16px> Smooth...** option from the menu.
4.  The **Smoothing** task panel opens.
5.  If you only want to smooth selected areas: choose the **Only selection** option:
    -   The **Selection** panel is added to the task panel.
    -   Specify the region options:
        -   
            **Respect only visible triangles**
            

        -   
            **Respect only triangles with normals facing screen**
            
    -   Press the **Add** button and while holding down the left mouse button draw a region, a closed spline, in the [3D view](3D_view.md). Faces that match the region options and (partially) fall inside the region will be selected.
    -   Optionally press the **Clear** button to clear the selection.
6.  Select the smoothing **Method**:
    -   
        **Taubin**
        

    -   
        **Laplace**
        
7.  Specify the **Parameters**:
    -   
        **Iterations**
        
        : the higher this number the smoother the final result. The value also has an impact on the total processing time of the command. Avoid high values if the mesh objects have many points.

    -   
        **λ**
        
        : the value must be in the {{Value|0}} - {{Value|1}} range.

    -   
        **μ**
        
        : the value must be in the {{Value|0}} - {{Value|1}} range.
8.  Press the **OK** button to finish the command.





{{Mesh Tools navi

}}



---
⏵ [documentation index](../README.md) > [Mesh](Mesh_Workbench.md) > Mesh Smoothing/it
