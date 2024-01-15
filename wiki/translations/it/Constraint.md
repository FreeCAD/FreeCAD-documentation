# Constraint/it
## Introduzione




In FreeCAD la parola \"Vincolo\" è normalmente usata per fare riferimento a una \"regola\" per disegnare forme geometriche all\'interno di uno ![ 16px](images/_Workbench_Sketcher.svg ) [Schizzo](Sketch/it.md) (classe `Sketcher::SketchObject`). Un vincolo limita la posizione di un determinato elemento geometrico in diversi modi, ad esempio può specificare se l\'elemento è orizzontale, verticale, tangente, parallelo, perpendicolare, coincidente con un punto, concentrico a un altro oggetto, ecc.

Esistono due grandi tipi di vincoli:

-   I **vincoli geometrici** definiscono le caratteristiche delle forme senza specificare le dimensioni esatte, ad esempio orizzontalità, verticalità, parallelismo, perpendicolarità e tangenza.
-   I **dati** o **vincoli dimensionali** definiscono le caratteristiche delle forme specificando le dimensioni, ad esempio il valore di una lunghezza o di un angolo.

Per un elenco di tutti i vincoli che possono essere applicati vedere le informazioni in <img alt="" src=images/Workbench_Sketcher.svg  style="width:24px;"> [Sketcher](Sketcher_Workbench/it.md). Alcuni di essi si applicano alle linee, alcuni alle curve e alcuni ai vertici. Vedi anche il [Tutorial di base per sketcher](Basic_Sketcher_Tutorial/it.md).



## Utilizzo

1.  Creare uno sketch da <img alt="" src=images/Workbench_Sketcher.svg  style="width:24px;"> [Sketcher](Sketcher_Workbench/it.md) o tramite <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [PartDesign](PartDesign_Workbench/it.md).
2.  Premere
    -   
        **[<img src=images/Sketcher_NewSketch.svg style="width:16px"> [Crea uno schizzo](Sketcher_NewSketch/it.md)**
        
        , o

    -   
        **[<img src=images/PartDesign_Body.svg style="width:16px"> [Crea un corpo](PartDesign_Body/it.md)**
        
        seguito da **[<img src=images/PartDesign_NewSketch.svg style="width:16px"> [Crea uno schizzo](PartDesign_NewSketch/it.md)**.
3.  Fare doppio clic sullo schizzo creato per accedere alla modalità di modifica.
4.  Disegnare una serie di linee usando **[<img src=images/Sketcher_CreatePolyline.svg style="width:16px"> [Polilinea](Sketcher_CreatePolyline/it.md)**.
5.  Selezionare una delle linee e cliccare **[<img src=images/Sketcher_ConstrainVertical.svg style="width:16px"> [Verticale](Sketcher_ConstrainVertical/it.md)**.
6.  Selezionare una delle linee e cliccare **[<img src=images/Sketcher_ConstrainHorizontal.svg style="width:16px"> [Orizzontale](Sketcher_ConstrainHorizontal/it.md)**.
7.  Selezionare la linea verticale e cliccare **[<img src=images/Sketcher_ConstrainDistanceY.svg style="width:16px"> [Distanza verticale](Sketcher_ConstrainDistanceY/it.md)**; assegnare una distanza.
8.  Selezionare la linea orizzontale e cliccare **[<img src=images/Sketcher_ConstrainDistanceX.svg style="width:16px"> [Distanza orizzontale](Sketcher_ConstrainDistanceX/it.md)**; assegnare una distanza.



## Note

-   I vincoli sono utili per creare profili molto precisi che possono essere trasformati in estrusioni solide utilizzando il pulsante **[<img src=images/PartDesign_Pad.svg style="width:16px"> [Estrusione di PartDesign](PartDesign_Pad/it.md)** o il pulsante **[<img src=images/Part_Extrude.svg style="width:16px"> [Estrudi di Part](Part_Extrude/it.md)**.
-   I vincoli vengono utilizzati solo all\'interno di [Sketcher](Sketch/it.md); altri oggetti 2D come quelli creati con <img alt="" src=images/Workbench_Draft.svg  style="width:24px;"> [Draft](Draft_Workbench/it.md) non comprendono i vincoli; questi ultimi vengono semplicemente collocati nello spazio 3D, e le loro proprietà ne definiscono forma e posizione.


{{Sketcher Tools navi

}} {{Document objects navi}}



---
⏵ [documentation index](../README.md) > [Glossary](Category_Glossary.md) > [Sketcher](Category_Sketcher.md) > Constraint/it
