---
- GuiCommand:/it
   Name:Part Union
   Name/it:Unione
   Icon:Part Fuse.svg
   MenuLocation:Parte → Operazione booleana → Unione
   Workbenches:[Parte](Part_Workbench/it.md)
   SeeAlso:[Sottrazione](Part_Cut/it.md), [Intersezione](Part_Common/it.md), [Operazione booleana](Part_Boolean.md)
---

# Part Fuse/it


</div>

## Descrizione

Il comando <img alt="" src=images/Part_Fuse.svg  style="width:24px;"> [Unione](Part_Union/it.md) fonde gli oggetti Parte selezionati in uno solo. Questa operazione è completamente parametrica e le componenti possono essere modificate e il risultato ricalcolato.

**Nota:** Questo comando è una forma automatizzata di <img alt="" src=images/Part_Booleans.svg  style="width:24px;"> [operazione booleana](Part_Boolean/it.md).

## Utilizzo

1.  Selezionare una o due forme.
2.  Invocare il comando Unione in uno di questi modi:
    -   Premere il pulsante **<img src="images/Part_Fuse.svg" width=16px> Unione** della barra degli strumenti di Parte
    -   Usare **Part → Booleana → Unione** nel menu principale

## Input supportati 


<div class="mw-translate-fuzzy">

Gli oggetti in ingresso devono essere delle forme [OpenCascade](OpenCascade/it.md). Ad esempio: cose fatte con gli ambienti Parte, PartDesign o Sketcher. Non mesh (a meno che essi non siano stati convertiti in Forme). Per gli oggetti mesh ci sono strumenti booleani specifici nell\'ambiente Mesh.


</div>

-   Solido + Solido: il risultato è un solido che occupa tutto il volume coperto dagli oggetti in ingresso

-   Shell + Shell, Shell + Face, Face + Face: il risultato è un guscio. Le facce che si intersecano sono divise. I gusci possono essere non-manifold. Dopo la fusione, le facce possono essere unite [Affinando](Part_RefineShape/it.md) il risultato.

-   Wire + Wire, Edge + Wire, Edge + Edge: il risultato è un wire (polilinea). I bordi (edge) sono divisi dove si intersecano.

I composti sono supportati a condizione che le forme confezionate in un composto non si tocchino o si intersechino. Se lo fanno, la Fusione probabilmente fallisce, o produce un risultato errato.

## Options


<div class="mw-translate-fuzzy">

## Opzioni

Gli elementi possono essere aggiunti e rimossi dalla fusione, trascinandoli dentro o fuori dalla funzione fusione nella vista ad albero, con il mouse. È necessario un ricalcolo manuale (premere il tasto **F5** o fare clic sull\'icona <img alt="" src=images/Std_Refresh.svg  style="width:24px;"> [Aggiorna/Ricalcola](Std_Refresh/it.md)) per vedere i risultati.


</div>

### Pulire la forma 

Il risultato della fusione di più oggetti può contenere linee superflue che derivano dalle forme originali, per ripulirlo, si può:

-   utilizzare il comando Parte → [Affinare una forma](Part_RefineShape/it.md)
-   utilizzare il comando <img alt="" src=images/OpenSCAD_RefineShapeFeature.png  style="width:32px;"> [Affina Forma](OpenSCAD_RefineShapeFeature/it.md) di [OpenScad](OpenSCAD_Workbench/it.md),

oppure per ottenere subito una forma pulita e non dover ricorrere a questo comando, attivare la voce **Affina automaticamente il modello\...** nelle [preferenze](Preferences_Editor/it.md)


<div class="mw-translate-fuzzy">





</div>



---
![](images/Button_right.svg) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Fuse/it
