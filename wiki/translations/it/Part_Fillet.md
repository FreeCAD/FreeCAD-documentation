---
 GuiCommand:
   Name: Part_Fillet
   Name/it: Part Raccorda
   MenuLocation: Parte , Raccorda...
   Workbenches: Part_Workbench/it
   SeeAlso: Part Chamfer/it
---

# Part Fillet/it



## Descrizione

**Part Raccorda** crea raccordi (arrotondamenti) sui bordi selezionati di una forma. Una finestra di dialogo permette di scegliere su quale forma e su quali bordi lavorare.



## Utilizzo

-   Richiamare lo strumento dalla barra degli strumenti Part o dal menu **Parte → Raccorda...**. È possibile selezionare la forma prima di richiamare lo strumento.

1.  Se la forma non è stata selezionata in precedenza, selezionarla nel menù a discesa Forma della [Scheda Azioni](Task_panel/it.md).
2.  Selezionare il tipo di raccordo, a raggio costante (di default), oppure a raggio variabile.
3.  Selezionare gli spigoli da raccordare, nella [Vista 3D](3D_view/it.md), oppure nella [Scheda Azioni](Task_panel/it.md).
4.  Stabilire il valore del raggio.
5.  Confermare con il pulsante **OK**.

![](images/Dialog-fillet.png )



## Part Raccorda VS. PartDesign Raccorda 

Vi è un altro strumento di raccordo in <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [PartDesign](PartDesign_Workbench/it.md). Si prega di notare che il loro funzionamento è molto diverso. Per le differenze vedere la pagina <img alt="" src=images/PartDesign_Fillet.svg  style="width:24px;"> [PartDesign Raccorda](PartDesign_Fillet/it.md).



## Note sull\'applicazione di Part Raccorda 

Il raccordo potrebbe non fare nulla se il risultato tocca o attraversa il bordo adiacente successivo. Quindi, se non si ottiene il risultato atteso, provare con un valore di **Raggio** inferiore. Lo stesso vale per <img alt="" src=images/Part_Chamfer.svg  style="width:24px;"> [Part Smussa](Part_Chamfer/it.md).

Lo strumento Raccordo a volte fallisce quando si tenta di raccordare oggetti complessi. Una causa comune di questo può essere dovuta al fatto che la forma che viene raccordata non è geometricamente corretta. Questo può essere il risultato di linee, piani, ecc. in esubero che non vengono rimossi dopo le precedenti operazioni utilizzate per costruire la forma (ad esempio Taglia, Intersezione o Fusione). Per minimizzare i problemi si può:

-   dove è possibile lasciare questa operazione per ultima, fino a quando la parte non è completamente generata. Questo riduce al minimo l\'interazione dei raccordi con le successive operazioni booleane;
-   Usare **Parte → Controlla la geometria** per verificare la presenza di eventuali errori nella geometria della forma e correggerli;
-   Usare **Parte → Crea una copia →  Affina forma** per rimuovere eventuali artefatti introdotti da precedenti operazioni booleane prima dei raccordi (e in alcuni casi tra operazioni di raccordi in sequenza);
-   Considerare di usare **Modifica → Preferenze → PartDesign** per abilitare il controllo e l\'affinazione automatica del modello dopo le operazioni booleane e le operazioni basate su schizzi (se queste opzioni sono attive, le prestazioni possono risentirne).

Lo strumento per il raccordo è soggetto al problema della [denominazione topologica](Topological_naming_problem/it.md) quando viene apportata una modifica ad una fase di modellazione precedente nella catena che influenza il numero di facce o vertici. Ciò può causare risultati imprevedibili. Finchè questo problema non verrà risolto, si consiglia di applicare le operazioni di raccordo e di smusso negli ultimi passi di modellazione della catena.





{{Part_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Fillet/it
