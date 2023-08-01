# FEM ConstraintForce/ro
---
- GuiCommand:   Name:FEM ConstraintForce   MenuLocation:Model → Mechanical Constraints → Constraint force   |Workbenches:[Shortcut:   SeeAlso:[[FEM_tutorial|FEM tutorial](FEM_Workbench___FEM]].md)---


</div>

## Descriere

Această comandă aplică o forță de valoare dată \[N\] la geometria țintei selectată.


<div class="mw-translate-fuzzy">

## Cum se folosește 


</div>


<div class="mw-translate-fuzzy">

1)Aplicarea unei forțe în direcția normală a unei fațete

-   -   In Atelierul FEM, click pe <img alt="Constraint Force" src=images/Fem-constraint-force.svg  style="width:24px;"> or select **Model** → **Mechanical Constraints** → **Constraint force** pentru a deschide dialogul proprietăților Force Constraint

![](images/FEMForceConstraintProperties.PNG )

-   -   If you have Mesh displayed, you need to hide it (select the mesh object and press **spacebar** or right click and select **Hide item**) and show the original model.
    -   Click on a *face* to which a force should be applied. It will appear in the list of geometrical objects.
    -   Fill in **Line load** with a force value in \[N\] (attention: *Not* in \[N/m\])

![](images/ApplyingForceToFace.PNG )

-   -   
        **Direction**
        
        : In a typical case, you\'ll click this field empty to apply a force in normal direction to the face. You can revert the direction of the force by clicking **Reverse direction**. In other cases, you need to pick a face or plane, which is in normal to the force direction (it could differ from the face, to which the force is being applied)

    -   Click pe obiectul **Close** to finish the dialog and create **[<img src=images/FEM_ConstraintForce.png style="width:24px"> ConstraintForce**


</div>

![](images/FEM_ConstraintForce_example.JPG )

## Notes

-   Defined force is applied uniformly to selected objects. For example, if you define one force constraint with 200 N applied to two faces having the same area, each face will be uniformly loaded with 100 N.





{{FEM Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintForce/ro
