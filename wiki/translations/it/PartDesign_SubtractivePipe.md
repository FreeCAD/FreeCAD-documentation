# PartDesign SubtractivePipe/it
---
- GuiCommand:   Name:PartDesign SubtractivePipe   Name/it:Sweep sottrattivo   Workbenches:[MenuLocation:Part Design → Sweep sottrattivo   Shortcut:None   Version:0.17   SeeAlso:[[PartDesign AdditivePipe/it|Sweep additivo](PartDesign_Workbench/it___PartDesign]].md), [Loft sottrattivo](PartDesign_SubtractiveLoft/it.md)---


</div>

## Descrizione


<div class="mw-translate-fuzzy">

**Sweep sottrattivo** crea un solido sottrattivo nel corpo attivo spazzando uno o più schizzi (detti anche sezioni trasversali) lungo un percorso aperto o chiuso. La sua forma viene quindi sottratta dal solido esistente. Sweep sottrattivo viene spesso utilizzato in combinazione con [Elica](Part_Helix/it.md) di Part e [Lega forme](PartDesign_ShapeBinder/it.md) di PartDesign per creare una filettatura; vedere il [Tutorial Filettatura](Thread_for_Screw_Tutorial/it.md) per i dettagli.


</div>

## Utilizzo


<div class="mw-translate-fuzzy">

1.  Premere il pulsante **<img src="images/PartDesign_SubtractivePipe.png" width=24px> '''Sweep sottrattivo'''**.
2.  Nel dialogo **Selezione della funzione**, selezionare uno schizzo da utilizzare come prima sezione trasversale e poi fare clic **OK**.
    -   In alternativa, è possibile selezionare un singolo schizzo prima di premere il pulsante Sweep sottrattivo.
3.  In **Parametri di sweep** sotto **Profilo**, premere il pulsante **Oggetto**.
4.  Selezionare nella vista 3D lo schizzo da utilizzare come percorso:
    -   In alternativa, è possibile selezionare i bordi del corpo premendo **Aggiungi bordo** e selezionando i bordi nella vista 3D.
5.  Per utilizzare più di una sezione trasversale, sotto **Trasformazione della sezione** impostare la Modalità di trasformazione in *Multisezione*; premere **Aggiungi sezione** quindi selezionare uno schizzo nella vista 3D. Ripetere l\'operazione per ogni sezione trasversale aggiuntiva.
6.  Impostare le opzioni, se necessario, e poi fare clic su **OK**.


</div>

## Opzioni

**Section Transformation**:

-   Select **Constant** to use a single profile
-   Select **Multisection** to use multiple profiles

**Section Orientation**:

-   Standard
    -   This keeps the cross section shape perpendicular to the path. This is the default setting.
-   Fixed
    -   Orientation set by first profile and constant throughout. This deactivates the alignment to the path normal vector. That means that the cross-section shape will not rotate with the path. Sweep along a circle to see the effect.
-   Frenet
    -   Create minimum possible twisting of profile. For more info, see [Frenet-Serret Formulas](https://en.wikipedia.org/wiki/Frenet%E2%80%93Serret_formulas)
-   Auxiliary
    -   Specify secondary path to guide pipe.
    -   For each point **P** along the sweep path, there will be a corresponding point **Q** on the auxiliary path.
    -   As the profile is swept, it will be transformed such that the **PQ** line is the normal of the sweep path.
    -   If **Curvelinear equivalence** is set, then the **Q** points are scaled proportionally along the sweep path, regardless of is length.
-   Binormal
    -   Specify binormal vector in X, Y and Z

**Corner Transition**

-   Transformed
-   Right
-   Rounded

## Proprietà


<div class="mw-translate-fuzzy">

-    {{PropertyData/it|Label}}: nome dato all\'operazione, questo nome può essere cambiato a piacere.

-    {{PropertyData/it|Refine}}: vero o falso. Se impostato su true, pulisce il solido dai bordi residui lasciati dalle funzioni. Per maggiori dettagli vedere [Affina forma](Part_RefineShape/it.md).

-    {{PropertyData/it|Sections}}: elenca le sezioni utilizzate.

-    {{PropertyData/it|Spine Tangent}}: vero o falso (predefinito). True estende il percorso per includere i bordi tangenti.

-    {{PropertyData/it|Auxiliary Spine Tangent}}: vero o falso (predefinito). Vero estende il percorso ausiliario per includere i bordi tangenti.

-    {{PropertyData/it|Auxiliary Curvelinear}}: vero o falso (predefinito). True calcola la normale tra i punti equidistanti su entrambe le dorsali.

-    {{PropertyData/it|Mode}}: modalità di profilo. Vedere [Opzioni](#Opzioni.md).

-    {{PropertyData/it|Binormal}}: vettore binomiale per la corrispondente modalità di orientamento.

-    {{PropertyData/it|Transition}}: modalità di transizione. Le opzioni sono *Trasformato*, *Angolo retto* o *Angolo arrotondato*.

-    {{PropertyData/it|Transformation}}: *Costante* usa una singola sezione trasversale. *Multisezione* utilizza due o più sezioni trasversali. *Lineare*, *S-shape* e *Interpolazione* al momento non sono funzionanti.


</div>

## Notes


<div class="mw-translate-fuzzy">

-   Gli schizzi devono formare profili chiusi.
-   Non è possibile utilizzare un vertice come sezione trasversale.
-   Una sezione trasversale non può giacere sullo stesso piano di quella immediatamente precedente.
-   Per controllare meglio la forma dello sweep, è consigliabile che tutte le sezioni abbiano lo stesso numero di segmenti. Ad esempio, per uno sweep tra un rettangolo e un cerchio, il cerchio può essere suddiviso in 4 archi collegati.


</div>


<div class="mw-translate-fuzzy">





</div>


{{PartDesign Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign SubtractivePipe/it
