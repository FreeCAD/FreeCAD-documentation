---
- GuiCommand:/es
   Name:PartDesign Chamfer
   Name/es:DiseñoPieza Chaflán
   Workbenches:[DiseñoPieza](PartDesign_Workbench/es.md)
   MenuLocation:DiseñoPieza → Chaflán
   SeeAlso:[Redondeo](PartDesign_Fillet/es.md), [Pieza Chaflán](Part_Chamfer/es.md)
---

# PartDesign Chamfer/es


</div>

## Descripción

Esta herramienta crea chaflanes en los bordes seleccionados de un objeto. Se crea una nueva entrada separada de chaflanes (seguida de un número consecutivo si ya existen chaflanes en el documento) en el árbol del proyecto.

## Utilización

-   Select a single edge, multiple edges or a face on an object, then start the tool either by clicking the button **<img src="images/PartDesign_Chamfer.svg" width=24px> '''Chamfer'''** or using the menu **PartDesign → Apply a dress-up feature → Chamfer**. In case you selected a face or a 3D object (<small>(v0.20)</small> ) all its edges are respected for chamfering.
-   In the appearing [Task panel](Task_panel.md) you can define the chamfer in 3 ways:
    -   
        **Equal distance**
        
        : The chamfer edges are equally distanced from the body edge.

    -   
        **Two distances**
        
        : The distances of the chamfer edge to the body edge are specified. The distance direction can be flipped. <small>(v0.19)</small> 

    -   
        **Distance and angle**
        
        : One distances of the chamfer edge to the body edge is specified. The second chamfer edge is defined by the angle of the chamfer. The distance direction can be flipped. <small>(v0.19)</small> 
-   If you want to add more edges or faces click the **Add** button and select edges and/or the faces.
-   After clicking the **Add** button you can add all edges of the object by right-clicking and selecting **Add all edges** from the context menu. <small>(v0.20)</small> 
-   If you want to remove edges or faces
    -   either select the edge/face in the list of the dialog and press the **DEL** key. *Note*: Since there must be at least one edge for the feature, the last remaining edge or face in the list cannot be removed.
    -   or click the **Remove** button. All edges and faces being previously selected are highlighted in purple. Select the edge or the face to be removed.
-   Click **OK** to validate.
-   For a chain of edges tangential to one another, one single edge can be selected; the chamfer will propagate along the chain.
-   To edit the chamfer after the function has been validated, either double-click on the chamfer label in the Project tree, or right-click on it and select **Edit Chamfer**.

## Notes


<div class="mw-translate-fuzzy">

## DiseñoPieza Chaflán VS. Pieza Chaflán 

\"El DiseñoPiezas chaflán no debe confundirse con su [Ambiente de trabajo piezas contraparte](Part_Chamfer/de.md)\". Aunque comparten el mismo icono, no son lo mismo, y no se usan de la misma manera. La principal diferencia es que DiseñoPiezas Chaflán crea una entrada de chaflán separada (seguida de un número secuencial si ya existen chaflanes) en el árbol de proyecto para el cuerpo actual. El Piezas chaflán se convierte en el padre del objeto al que se aplicó.


</div>


<div class="mw-translate-fuzzy">





</div>


{{PartDesign Tools navi

}}

---
[documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Chamfer/es
