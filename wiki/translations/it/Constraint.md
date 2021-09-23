# Constraint/it


## Introduzione


{{TOCright}}

In FreeCAD la parola \"Vincolo\" è normalmente usata per fare riferimento a una \"regola\" per disegnare forme geometriche all\'interno di uno ![ 16px](images/_Workbench_Sketcher.svg ) [Schizzo](Sketch/it.md) (classe `Sketcher::SketchObject`). Un vincolo limita la posizione di un determinato elemento geometrico in diversi modi, ad esempio può specificare se l\'elemento è orizzontale, verticale, tangente, parallelo, perpendicolare, coincidente con un punto, concentrico a un altro oggetto, ecc.

Esistono due grandi tipi di vincoli:

-   I **vincoli geometrici** definiscono le caratteristiche delle forme senza specificare le dimensioni esatte, ad esempio orizzontalità, verticalità, parallelismo, perpendicolarità e tangenza.
-   I **dati** o **vincoli dimensionali** definiscono le caratteristiche delle forme specificando le dimensioni, ad esempio il valore di una lunghezza o di un angolo.

Per un elenco di tutti i vincoli che possono essere applicati vedere le informazioni in <img alt="" src=images/Workbench_Sketcher.svg  style="width:24px;"> [Sketcher](Sketcher_Workbench/it.md). Alcuni di essi si applicano alle linee, alcuni alle curve e alcuni ai vertici. Vedi anche il [Tutorial di base per sketcher](Basic_Sketcher_Tutorial/it.md).

## Utilizzo

1.  Create a sketch either from the <img alt="" src=images/Workbench_Sketcher.svg  style="width:24px;"> [Sketcher Workbench](Sketcher_Workbench.md) or through the <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [PartDesign Workbench](PartDesign_Workbench.md).
2.  Press
    -   
        **<img src=images/Sketcher_NewSketch.svg style="width:16px"> [Sketcher NewSketch](Sketcher_NewSketch.md)**
        
        , or

    -   
        **<img src=images/PartDesign_Body.svg style="width:16px"> [PartDesign Body](PartDesign_Body.md)**
        
        followed by **<img src=images/PartDesign_NewSketch.svg style="width:16px"> [PartDesign NewSketch](PartDesign_NewSketch.md)**.
3.  Double click the created sketch to enter its edit mode.
4.  Draw a series of lines using **<img src=images/Sketcher_CreatePolyline.svg style="width:16px"> [Create polyline](Sketcher_CreatePolyline.md)**.
5.  Pick one of the lines, and use **<img src=images/Sketcher_ConstrainVertical.svg style="width:16px"> [Constrain vertical](Sketcher_ConstrainVertical.md)**.
6.  Pick one of the lines, and use **<img src=images/Sketcher_ConstrainHorizontal.svg style="width:16px"> [Constrain horizontal](Sketcher_ConstrainHorizontal.md)**.
7.  Pick the vertical line, and use **<img src=images/Sketcher_ConstrainDistanceY.svg style="width:16px"> [Constrain distance Y](Sketcher_ConstrainDistanceY.md)**; assign a distance.
8.  Pick the horizontal line, and use **<img src=images/Sketcher_ConstrainDistanceX.svg style="width:16px"> [Constrain distance X](Sketcher_ConstrainDistanceX.md)**; assign a distance.

## Note

-   Constraints are useful to create very precise profiles which can the be turned into solid extrusions by using the **<img src=images/PartDesign_Pad.svg style="width:16px"> <img src=images/Part_Extrude.svg style="width:PartDesign Pad](PartDesign_Pad.md)** or **[16px"> [Part Extrude](Part_Extrude.md)** operations.
-   Constraints are only used within [Sketches](Sketch.md); other 2D objects such as those created with the <img alt="" src=images/Workbench_Draft.svg  style="width:24px;"> [Draft Workbench](Draft_Workbench.md) do not understand about constraints; the latter are simply placed in 3D space, and their properties define their shape and position.


{{Sketcher Tools navi

}} {{Document objects navi}} 

[Category:Glossary](Category:Glossary.md)
