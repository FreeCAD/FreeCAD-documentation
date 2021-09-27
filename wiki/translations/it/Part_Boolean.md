# Part Boolean/it
---
- GuiCommand:/it   Name:Part_Boolean   Name/it:Booleana   MenuLocation:Parte → Booleana...   Workbenches:[SeeAlso:[[Part Union/it|Unione ](Part_Workbench/it____Parte]].md), [ Intersezione](Part_Common/it_.md), [ Sottrazione](Part_Cut/it_.md) e [Sezione](Part_Section/it.md)---


</div>

## Descrizione

**Operazione boolena** è uno strumento booleano generico tutto-in-uno. Consente di specificare gli oggetti e le operazioni da eseguire tramite un\'unica finestra di dialogo.


<div class="mw-translate-fuzzy">

Per operazioni booleane più veloci, usare <img alt="" src=images/Part_Fuse.svg  style="width:16px;"> _, <img alt="" src=images/Part_Cut.svg  style="width:16px;"> _.


</div>

![](images/PartBooleansDialog.png )


*Finestra di dialogo per selezionare gli oggetti ed eseguire operazioni booleane con essi.*

## Utilizzo


<div class="mw-translate-fuzzy">

Vedere i singoli comandi:

-    **<img src="images/Part_Fuse.svg" width=16px> [Unione](Part_Union/it.md)
**
    

-    **<img src="images/Part_Cut.svg" width=16px> [Taglio](Part_Cut/it.md)
**
    

-    **<img src="images/Part_Common.svg" width=16px> [Intersezione](Part_Common/it.md)
**
    

-    **<img src="images/Part_Section.svg" width=16px> [Sezione](Part_Section/it.md)
**
    


</div>


<div class="mw-translate-fuzzy">

Vedere anche **Part → [Affina forma](Part_RefineShape/it.md)**


</div>

## Problemi di complanarità 

Le operazioni booleane sono eseguite dal kernel di geometria interno, [OpenCASCADE Technology](OpenCASCADE/it.md) (OCCT). Questa libreria a volte ha problemi a produrre risultati booleani quando gli oggetti di input condividono un bordo o una faccia. Per essere sicuri che l\'operazione booleana abbia successo, la raccomandazione è che le forme si intersechino tra loro; ciò significa che nella maggior parte dei casi, una forma dovrebbe sporgere o essere di dimensioni maggiori rispetto all\'altra forma.


<div class="mw-translate-fuzzy">

In caso di complanarità, anche se la prima operazione booleana riesce, le successive operazioni booleane potrebbero non riuscire. In questo caso, il problema potrebbe non essere nell\'ultima operazione eseguita, ma in quelle precedenti, ovvero nelle operazioni nidificate come indicato nella <img src=images/Part_CheckGeometry.svg style="width:vista ad albero](tree_view/it.md). Per risolvere questi problemi, si consiglia di utilizzare lo strumento **[16px"> [Controlla la geometria](Part_CheckGeometry/it.md)** per ispezionare tutti gli oggetti alla ricerca di problemi.


</div>

<img alt="" src=images/Part_Boolean_cut_coplanar_1.png  style="width:500px;">

<img alt="" src=images/Part_Boolean_cut_coplanar_2.png  style="width:500px;">


*A sinistra: forme che condividono una faccia, un taglio booleano può produrre risultati errati. A destra: forme che si intersecano chiaramente tra loro, il taglio booleano avrà successo nella maggior parte dei casi.*

<img alt="" src=images/Part_Boolean_fusion_coplanar_1.png  style="width:500px;">

<img alt="" src=images/Part_Boolean_fusion_coplanar_2.png  style="width:500px;">


*A sinistra: forme che condividono una faccia, un'unione booleana può produrre risultati errati. A destra: forme che si intersecano chiaramente tra loro, l'unione booleana avrà successo nella maggior parte dei casi.*


<div class="mw-translate-fuzzy">





</div>

---
[documentation index](../README.md) > [Part](Part_Workbench.md) > Part Boolean/it
