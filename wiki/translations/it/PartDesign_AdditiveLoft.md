---
- GuiCommand:/it
   Name:PartDesign AdditiveLoft
   Name/it:Loft additivo
   Workbenches:[PartDesign](PartDesign_Workbench/it.md)
   MenuLocation:Part Design → Loft additivo
   Version:0.17
   SeeAlso:[Sweep additivo](PartDesign_AdditivePipe/it.md)
---

# PartDesign AdditiveLoft/it


</div>

## Descrizione

**Loft additivo** crea un solido nel corpo attivo eseguendo una transizione tra due o più schizzi (indicati anche come sezioni trasversali). Se il corpo contiene già delle funzionalità, il loft additivo viene unito a loro.

![](images/PartDesign_AddLoft_example.png )


<div class="mw-translate-fuzzy">

\'\' A sinistra le sezioni trasversali (A), (B) e (C); a destra il loft additivo che viene creato. \'\'


</div>

## Utilizzo

### Dialog-based workflow 


<div class="mw-translate-fuzzy">

1.  Premere il pulsante **<img src="images/PartDesign_AdditiveLoft.png" width=24px> '''Loft additivo'''**.
2.  Nel dialogo **Select feature**, selezionare uno schizzo da utilizzare come prima sezione trasversale e fare clic su **OK**.
    -   In alternativa, è possibile selezionare un singolo schizzo prima di premere il pulsante Loft additivo.
3.  In **Loft parameters**, premere il pulsante **Add Section**.
4.  Selezionare il successivo schizzo nella vista 3D. Ripetere per selezionare altri schizzi nell\'ordine in cui si desidera che vengano loftati.
5.  Impostare le opzioni, se necessario, e poi fare clic su **OK**.


</div>

### Selection-based workflow 


<small>(v0.19)</small> 

1.  Select several sketches. It is hereby important in what order you select them:
    -   The sketch selected at first will become the base profile object in the next step
    -   The sketches selected after the first one will become the loft sections. Also here the selection order is important: The sketch selected as second will become the first loft section, the one selected as third becomes the second section and so on. (You can change the section order any time later in the loft dialog by dragging sections in the list to the desired position.<small>(v0.19)</small> )
    -   The first or last selection can also be a face of a 3D object (<small>(v0.20)</small> )
2.  Press the **<img src=images/PartDesign_AdditiveLoft.svg style="width:24px"> [Additive loft](PartDesign_AdditiveLoft.md)** button.
3.  Set options if needed and click **OK**.

## Opzioni


<div class="mw-translate-fuzzy">

-   **Ruled surface**: effettua transizioni diritte tra le sezioni trasversali. Non si applica a un loft con due sezioni trasversali. Se non viene selezionato, le transizioni sono fluide.
-   **Closed**: effettua una transizione dall\'ultima sezione trasversale alla prima, creando un loop.
-   Premere il pulsante **Rimuovi sezione** per rimuovere uno schizzo, selezionandolo nella vista 3D.


</div>

## Proprietà


<div class="mw-translate-fuzzy">

-    {{PropertyData/it|Label}}: nome dato all\'operazione, questo nome può essere cambiato a piacere.

-    {{PropertyData/it|Sections}}: elenca le sezioni utilizzate.

-    {{PropertyData/it|Ruled}}: vedere [Opzioni](PartDesign_AdditiveLoft/it#Opzioni.md).

-    {{PropertyData/it|Closed}}: vedere [Opzioni](PartDesign_AdditiveLoft/it#Opzioni.md).

-    {{PropertyData/it|Midplane}}: non applicabile.

-    {{PropertyData/it|Reversed}}: non applicabile.

-    {{PropertyData/it|Refine}}: vero o falso. Se impostato su true, pulisce il solido dai bordi residui lasciati dalle operazioni. Per maggiori dettagli vedere [Affina forma](Part_RefineShape/it.md).


</div>

## Notes


<div class="mw-translate-fuzzy">

-   Gli schizzi devono formare profili chiusi.
-   Non è possibile eseguire il loft su un vertice.
-   Una sezione trasversale non può giacere sullo stesso piano di quella immediatamente precedente.
-   Per controllare meglio la forma del loft, è consigliabile che tutte le sezioni abbiano lo stesso numero di segmenti. Ad esempio, per un loft tra un rettangolo e un cerchio, il cerchio può essere suddiviso in 4 archi collegati.
-   Loft viene creato nell\'ordine in cui sono state aggiunte le sezioni trasversali


</div>

## Link


<div class="mw-translate-fuzzy">

-   [Dettagli tecnici di Loft di Part](Part_Loft_Technical_Details/it.md) spiega come viene creato un [Loft di Part](Part_Loft/it.md), e gran parte del suo contenuto è rilevante anche per il loft additivo di PartDesign.


</div>


<div class="mw-translate-fuzzy">





</div>


{{PartDesign Tools navi

}}

---
[documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign AdditiveLoft/it
