---
- GuiCommand:
   Name:PartDesign Chamfer
   MenuLocation:Part Design → Apply a dress-up feature → Chamfer
   Workbenches:[PartDesign](PartDesign_Workbench.md)
   SeeAlso:[PartDesign Fillet](PartDesign_Fillet.md), [Part Chamfer](Part_Chamfer.md)
---


<div class="mw-translate-fuzzy">

### Tanım


</div>

This tool creates chamfers on the selected edges of an object. A new separate Chamfer entry (followed by a consecutive number if there are already existing chamfers in the document) is created in the Project tree.

## Usage

-   Select a single edge, multiple edges or a face on an object, then start the tool either by clicking the button **<img src="images/PartDesign_Chamfer.svg" width=24px> '''Chamfer'''** or using the menu **PartDesign → Apply a dress-up feature → Chamfer**. In case you selected a face all its edges are respected for chamfering.
-   In the appearing [Task panel](Task_panel.md) you can define the chamber in 3 ways:
    -   **Equal distance**: The chamfer edges are equally distanced from the body edge.
    -   **Two distances**: The distances of the chamfer edge to the body edge are specified. The distance direction can be flipped. <small>(v0.19)</small> 
    -   **Distance and angle**: One distances of the chamfer edge to the body edge is specified. The second chamfer edge is defined by the angle of the chamfer. The distance direction can be flipped. <small>(v0.19)</small> 
-   If you want to add more edges or faces click the **Add** button and select edges and/or the faces.
-   If you want to remove edges or faces
    -   either select the edge/face in the list of the dialog and press the **DEL** key. *Note*: Since there must be at least an edge for the feature, the last remaining edge or face in the list cannot be removed.
    -   or click the **Remove** button. All edges and faces being previously selected are highlighted in purple. Select the edge or the face to be removed.
-   Click **OK** to validate.
-   For a chain of edges tangential to one another, one single edge can be selected; the chamfer will propagate along the chain.
-   To edit the chamfer after the function has been validated, either double-click on the chamfer label in the Project tree, or right-click on it and select **Edit Chamfer**.

## PartDesign Chamfer vs. Part Chamfer 

**The PartDesign Chamfer is not to be confused with its [Part workbench counterpart](Part_Chamfer.md)**. Although they share the same icon, they are not the same, and are not used the same way. The main difference is that PartDesign Chamfer creates a separate Chamfer entry (followed by a sequential number if there are already existing chamfers) in the Project tree for the current body. The Part Chamfer becomes the parent of the object it was applied to.





{{PartDesign Tools navi

}} 
