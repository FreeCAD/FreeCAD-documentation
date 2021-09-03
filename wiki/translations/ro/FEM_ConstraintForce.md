---
- GuiCommand:   Name:FEM ConstraintForce   MenuLocation:Model → Mechanical Constraints → Constraint force   |Workbenches:[Shortcut:   SeeAlso:[[FEM_tutorial|FEM tutorial](FEM_Workbench___FEM]].md)---


</div>

## Descriere

Această comandă aplică o forță de valoare dată \[N\] la geometria țintei selectată.


<div class="mw-translate-fuzzy">

## Cum se folosește {#cum_se_folosește}


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

    -   Click pe obiectul **Close** to finish the dialog and create **<img src=images/FEM_ConstraintForce.png style="width:24px"> ConstraintForce**


</div>


<div class="mw-translate-fuzzy">

2\) Applying a force in to line in selected direction

-   -   In FEM workbench, click on <img alt="Constraint Force" src=images/FEM_ConstraintForce.png  style="width:24px;"> or select **Model** → **Mechanical Constraints** → **Constraint force** to open Force Constraint properties dialog

    -   If you have Mesh displayed, you need to hide it (select the mesh object and press **spacebar** or right click and select **Hide item**) and show the original model.

    -   Click on a *line segment* to which a force should be applied. It will appear in the list of geometrical objects.

    -   Fill in **Area load** with a force value in \[N\]

    -   
        **Direction**
        
        : Acum, cu segmentul de linie selectat, probabil că forța este aplicată într-o direcție greșită. Trebuie să specificăm direcția făcând clic pe butonul **Direction** și apoi făcând clic pe o fațetă care indică direcția sa normală în direcția forței (sau direcția inversă). Din nou, puteți reveni la direcția forței făcând clic pe **Reverse direction**.

![](images/FEMforceonline.PNG )

-   -   Click pe **Close** pentru a încheia dealogul și a crea obiectul **<img src=images/FEM_ConstraintForce.png style="width:24px"> ConstraintForce**


</div>





{{FEM Tools navi

}}  
