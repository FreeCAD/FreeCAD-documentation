---
- GuiCommand:
   Name: PartDesign NewSketch
   Name/it: Nuovo schizzo
   Workbenches: PartDesign Workbench/it
   MenuLocation: Part Design -> Crea schizzo
   Version: 0.17
---

# PartDesign NewSketch/it


</div>



## Descrizione


<div class="mw-translate-fuzzy">

Questo strumento crea un nuovo schizzo, crea un nuovo [Corpo](PartDesign_Body/it.md) per contenere lo schizzo se non esiste e apre automaticamente l\'ambiente [Sketcher](Sketcher_Workbench/it.md) dopo la creazione.


</div>


<div class="mw-translate-fuzzy">

Quando si creano modelli usando [PartDesign](PartDesign_Workbench/it.md), questo strumento deve essere preferito allo strumento [Nuovo schizzo](Sketcher_NewSketch/it.md) che si trova nell\'[ambiente Sketcher](Sketcher_Workbench/it.md).


</div>



## Uso


<div class="mw-translate-fuzzy">

1.  Premere il pulsante **[<img src=images/PartDesign_NewSketch.svg style="width:24px">** dalla barra degli strumenti di PartDesign.
2.  Nel pannello Azioni, viene visualizzata la finestra di dialogo **Seleziona funzione**. Selezionare uno dei piani nell\'elenco o nella vista 3D che può essere riorientata per una migliore la visibilità.
3.  Premere **OK**.
4.  L\'interfaccia passa automaticamente a Sketcher e lo schizzo può essere modificato. Quando lo schizzo è terminato e viene chiuso, l\'interfaccia viene riportata a PartDesign e la vista 3D viene ripristinata all\'orientamento della vista utilizzata prima di creare lo schizzo.
5.  In alternativa, è possibile selezionare un piano o una faccia sul corpo attivo esistente prima di creare lo schizzo, nel qual caso lo schizzo viene creato immediatamente.


</div>



## Opzioni

-   Per cambiare il modo di associazione di uno schizzo esistente, cambiare le sue proprietà**Map Mode**.

-   The *Select feature* Dialog defines the features of the new sketch

:   

    :   <img alt="" src=images/PartDesign.CreateSketch.SelectFeatureDialog.jpeg  style="width:300px;">
    :   *Select feature* dialog. These settings create a sketch on the XY plane and allow cross-references from other items of the same body

Dialog settings

-   Coordinate system box: defines the orientation of the sketch plane
-   Allow Used Features: *TBD*

:   Allow external features options

-   From other bodies of the same part: any elements used in the same body can be referenced
-   From different parts or free features: *TBD*
-   Make independent copy: all other elements will be separate copies, i.e. they will not change when the original changes.
-   Make dependent copy: the elements will be copies, but a dependency to the original elements is kept. This is basically using a [Shapebinder](PartDesign_ShapeBinder.md)
-   Create cross-reference: the linked elements will not be copies, but point to the original elements, e.g. a master sketch. Any changes are reflected to this sketch

To reference any items in the [Workbench Sketcher](Sketcher_Workbench.md) use the **<img src="images/Sketcher_External.svg" width=16px> [External Geometry](Sketcher_External.md)** and **[<img src=images/Sketcher_CarbonCopy.svg style="width:16px"> [CarbonCopy](Sketcher_CarbonCopy.md)** tools. Generally it is recommended to use other sketches as source for references rather than faces or edges, because they are less affected by the Topological Naming Issue.



## Proprietà


<div class="mw-translate-fuzzy">

-    **Map Mode**: modalità di associazione dello schizzo ad un altro oggetto, solitamente un piano o una faccia ma possono essere altri tipi di oggetti. Fare clic una volta sul campo per rendere visibile un pulsante ** ...** e premerlo per aprire la finestra di dialogo [Associazione](Part_EditAttachment/it.md). Se è impostato su Disattivato, la proprietà Posizionamento è abilitata.

-    **Placement**: controlla l\'orientamento dello schizzo nello spazio 3D; vedere [Posizionamento](Std_Placement/it.md). Disabilitato se lo schizzo è associato tramite la proprietà Map Mode.


</div>


<div class="mw-translate-fuzzy">





</div>





{{PartDesign Tools navi

}}



---
⏵ [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign NewSketch/it
