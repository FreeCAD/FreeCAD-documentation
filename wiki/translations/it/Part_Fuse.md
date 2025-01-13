---
 GuiCommand:
   Name: Part Fuse
   Name: Part Unione
   MenuLocation: Parte , Operazione booleana , Unione
   Workbenches: Part_Workbench/it
   SeeAlso: Part_Boolean/it, Part_Cut/it, Part_Common/it
---

# Part Fuse/it



## Descrizione

Il comando <img alt="" src=images/Part_Fuse.svg  style="width:24px;"> [Unione](Part_Union/it.md) fonde gli oggetti Parte selezionati in uno solo. Questa operazione è completamente parametrica e le componenti possono essere modificate e il risultato ricalcolato.

**Nota:** Questo comando è una forma automatizzata di <img alt="" src=images/Part_Booleans.svg  style="width:24px;"> [Operazione booleana](Part_Boolean/it.md).



## Utilizzo

1.  Selezionare una o due forme.
2.  Invocare il comando Unione in uno di questi modi:
    -   Premere il pulsante **<img src="images/Part_Fuse.svg" width=16px> Unione** della barra degli strumenti di Part
    -   Usare **Parte → Operazioni booleane → Unisci** nel menu principale



## Input supportati 

Gli oggetti di input devono essere forme [OpenCASCADE](OpenCASCADE/it.md). Esempi: materiale realizzato con gli ambienti Part, PartDesign e Sketcher. Non mesh (a meno che non siano state convertite in forme): per le mesh, ci sono strumenti booleani specifici nell\'ambiente MeshDesign.

-   Solido + Solido: il risultato è un solido che occupa tutto il volume coperto dagli oggetti in ingresso

-   Shell + Shell, Shell + Face, Face + Face: il risultato è un guscio. Le facce che si intersecano sono divise. I gusci possono essere non-manifold. Dopo la fusione, le facce possono essere unite [Affinando](Part_RefineShape/it.md) il risultato.

-   Wire + Wire, Edge + Wire, Edge + Edge: il risultato è un wire (polilinea). I bordi (edge) sono divisi dove si intersecano.

I composti sono supportati a condizione che le forme confezionate in un composto non si tocchino o si intersechino. Se lo fanno, la Fusione probabilmente fallisce, o produce un risultato errato.



## Opzioni

Gli elementi possono essere aggiunti e rimossi da una fusione, trascinandoli dentro o fuori dalla funzione di fusione nella vista ad albero con il mouse. Per trascinare gli elementi fuori da una fusione bisogna rilasciarli sul nodo del documento (il nome del file) del proprio modello. Per visualizzare i risultati è necessario un ricalcolo manuale (premere il tasto **F5** o fare clic sull\'icona <img alt="" src=images/Std_Refresh.svg  style="width:24px;"> [Aggiorna](Std_Refresh/it.md)).





{{Part_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Fuse/it
