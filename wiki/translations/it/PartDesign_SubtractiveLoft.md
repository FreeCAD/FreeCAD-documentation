# PartDesign SubtractiveLoft/it
---
- GuiCommand   */it   Name   *PartDesign SubtractiveLoft   Name/it   *Loft sottrattivo   Workbenches   *[MenuLocation   *Part Design → Loft sottrattivo   Version   *0.17   SeeAlso   *[[PartDesign AdditiveLoft/it|Loft additivo](PartDesign_Workbench/it___PartDesign]].md), [Sweep sottrattivo](PartDesign_SubtractivePipe/it.md)---


</div>

## Descrizione

**Loft sottrattivo** crea un solido sottrattivo nel corpo attivo eseguendo una transizione tra due o più schizzi (indicati anche come sezioni trasversali). La sua forma viene quindi sottratta dal solido esistente.

## Utilizzo

### Dialog-based workflow 

1.  Press the **[<img src=images/PartDesign_SubtractiveLoft.svg style="width   *24px"> [Subtractive loft](PartDesign_SubtractiveLoft.md)** button.
2.  In the **Select feature** dialog, select a sketch to be used as base profile object and click **OK**.
    -   Alternatively, either a single sketch or the face of a 3D object (<small>(v0.20)</small> ) can be selected prior to pressing the subtractive loft button.
3.  In the **Loft parameters**, press the **Add Section** button.
4.  Select the next sketch in the [3D view](3D_view.md). Repeat to select more sketches in the order you want them to be lofted through. (You can change the section order any time later in the loft dialog by dragging sections in the list to the desired position.<small>(v0.19)</small> )
5.  Set options if needed and click **OK**.

### Selection-based workflow 


<small>(v0.19)</small> 

1.  Select several sketches. It is hereby important in what order you select them   *
    -   The sketch selected at first will become the base profile object in the next step
    -   The sketches selected after the first one will become the loft sections. Also here the selection order is important   * The sketch selected as second will become the first loft section, the one selected as third becomes the second section and so on. (You can change the section order any time later in the loft dialog by dragging sections in the list to the desired position.<small>(v0.19)</small> )
    -   The first or last selection can also be a face of a 3D object (<small>(v0.20)</small> )
2.  Press the **[<img src=images/PartDesign_SubtractiveLoft.svg style="width   *24px"> [Subtractive loft](PartDesign_SubtractiveLoft.md)** button.
3.  Set options if needed and click **OK**.

## Opzioni


<div class="mw-translate-fuzzy">

-   **Ruled surface**   * effettua transizioni diritte tra le sezioni trasversali. Non si applica a un loft con due sezioni trasversali. Se non viene selezionato, le transizioni sono fluide.
-   **Closed**   * effettua una transizione dall\'ultima sezione trasversale alla prima, creando un loop.
-   Premere il pulsante **Rimuovi sezione** per rimuovere uno schizzo, selezionandolo nella vista 3D.


</div>

## Proprietà


<div class="mw-translate-fuzzy">

-    {{PropertyData/it|Label}}   * nome dato all\'operazione, questo nome può essere cambiato a piacere.

-    {{PropertyData/it|Sections}}   * elenca le sezioni utilizzate.

-    {{PropertyData/it|Ruled}}   * vedere [Opzioni](#Opzioni.md).

-    {{PropertyData/it|Closed}}   * vedere [Opzioni](#Opzioni.md).

-    {{PropertyData/it|Midplane}}   * N/A

-    {{PropertyData/it|Reversed}}   * N/A

-    {{PropertyData/it|Refine}}   * vero o falso. Se impostato su true, pulisce il solido dai bordi residui lasciati dalle operazioni. Per maggiori dettagli vedere [Affina forma](Part_RefineShape/it.md).


</div>

## Notes


<div class="mw-translate-fuzzy">

-   Gli schizzi devono formare profili chiusi.
-   Non è possibile eseguire il loft su un vertice.
-   Una sezione trasversale non può giacere sullo stesso piano di quella immediatamente precedente.
-   Per controllare meglio la forma del loft, è consigliabile che tutte le sezioni abbiano lo stesso numero di segmenti. Ad esempio, per un loft tra un rettangolo e un cerchio, il cerchio può essere suddiviso in 4 archi collegati.


</div>

## Link


<div class="mw-translate-fuzzy">

-   [Dettagli tecnici di Loft di Part](Part_Loft_Technical_Details/it.md) spiega come viene creato un [Loft di Part](Part_Loft/it.md), e gran parte del suo contenuto è rilevante anche per il loft sottrattivo di PartDesign.


</div>


<div class="mw-translate-fuzzy">





</div>


{{PartDesign Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign SubtractiveLoft/it
