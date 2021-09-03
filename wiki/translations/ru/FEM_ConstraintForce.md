---
- GuiCommand:/ru   Name:FEM ConstraintForce   Name/ru:FEM ConstraintForce   MenuLocation:FEM → Constraint force   |Workbenches:[Shortcut:   SeeAlso:[[FEM_tutorial/ru|FEM tutorial](FEM_Workbench/ru___FEM]].md)---


</div>

## Description

This command applies a force of given value \[N\] to selected target geometry.

## Usage

1\) Applying a force in normal direction to a face

-   -   In FEM workbench, click on <img alt="Constraint Force" src=images/FEM_ConstraintForce.svg  style="width:24px;"> or select **Model** → **Mechanical Constraints** → **Constraint force** to open Force Constraint properties dialog

![](images/FEMForceConstraintProperties.PNG )

-   -   If you have Mesh displayed, you need to hide it (select the mesh object and press **spacebar** or right click and select **Hide item**) and show the original model.
    -   Click on a *face* to which a force should be applied. It will appear in the list of geometrical objects.
    -   Fill in **Line load** with a force value in \[N\] (attention: *Not* in \[N/m\])

![](images/ApplyingForceToFace.PNG )

-   -   
        **Direction**
        
        : In a typical case, you\'ll click this field empty to apply a force in normal direction to the face. You can revert the direction of the force by clicking **Reverse direction**. In other cases, you need to pick a face or plane, which is in normal to the force direction (it could differ from the face, to which the force is being applied)

    -   Click **Close** to finish the dialog and create **<img src=images/FEM_ConstraintForce.svg style="width:24px"> ConstraintForce** object

2\) Applying a force in to line in selected direction

-   -   In FEM workbench, click on <img alt="Constraint Force" src=images/FEM_ConstraintForce.svg  style="width:24px;"> or select **Model** → **Mechanical Constraints** → **Constraint force** to open Force Constraint properties dialog

    -   If you have Mesh displayed, you need to hide it (select the mesh object and press **spacebar** or right click and select **Hide item**) and show the original model.

    -   Click on a *line segment* to which a force should be applied. It will appear in the list of geometrical objects.

    -   Fill in **Area load** with a force value in \[N\]

    -   
        **Direction**
        
        : Now, with line segment selected, it si likely that the force is applied in a wrong direction. We need to specify the direction by clicking the button **Direction** and then clicking a face pointing with its normal to the direction of the force (or reversed direction). Again, you can revert the direction of the force by clicking **Reverse direction**.

![](images/FEMforceonline.PNG )

-   -   Click **Close** to finish the dialog and create **<img src=images/FEM_ConstraintForce.svg style="width:24px"> ConstraintForce** object





{{FEM Tools navi

}}  
