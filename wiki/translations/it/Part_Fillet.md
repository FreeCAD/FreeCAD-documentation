# Part Fillet/it
---
- GuiCommand   */it   Name   *Part_Fillet   Name/it   *Raccorda   MenuLocation   *Parte → Raccorda...   Workbenches   *[SeeAlso   *[[Part Chamfer/it|Smussa](Part_Workbench/it___Parte]].md)---


</div>

## Descrizione


<div class="mw-translate-fuzzy">

Questo strumento raccorda (arrotonda) i bordi selezionati di un oggetto. Una finestra di dialogo consente di scegliere gli oggetti e i bordi su cui lavorare.


</div>

## Utilizzo


<div class="mw-translate-fuzzy">

1.  Avviare lo strumento raccorda dell\'ambiente Parte. Gli oggetti possono essere selezionati in precedenza.
2.  Se la forma non è stata selezionata in precedenza, è possibile selezionarla nel menu della scheda Azioni.
3.  Selezionare il tipo di raccordo, a raggio costante (di default), oppure a raggio variabile.
4.  Selezionare gli spigoli da raccordare, nella vista 3D, oppure nel pannello delle Azioni.
5.  Stabilire il valore del raggio, poi
6.  Confermare con il pulsante **OK**.


</div>

![](images/Dialog-fillet_it.png )


<div class="mw-translate-fuzzy">

## Differenze tra il raccordo di Parte e il raccordo di PartDesign 

Vi è un altro strumento di raccordo in PartDesign. Si prega di notare che il loro funzionamento è molto diverso. Per le differenze vedere la pagina [Raccordo di PartDesign](PartDesign_Fillet/it.md).


</div>


<div class="mw-translate-fuzzy">

## Note sulla applicazione del Raccordo di Parte 

Il raccordo potrebbe non fare nulla se il risultato tocca o attraversa il bordo adiacente successivo. Quindi, se non si ottiene il risultato atteso, provare con un valore inferiore. Lo stesso vale per lo [Smusso](Part_Chamfer/it.md) di Part.


</div>


<div class="mw-translate-fuzzy">

Lo strumento Raccordo a volte fallisce quando si tenta di raccordare oggetti complessi. Una causa comune di questo può essere dovuta al fatto che la forma che viene raccordata non è geometricamente corretta. Questo può essere il risultato di linee, piani, ecc. in esubero che non vengono rimossi dopo le precedenti operazioni utilizzate per costruire la forma (ad esempio Taglia, Intersezione o Fusione). Per minimizzare i problemi si può   *

-   dove è possibile lasciare questa operazione per ultima, fino a quando la parte non è completamente generata. Questo riduce al minimo l\'interazione dei raccordi con le successive operazioni booleane;
-   Usare **Part → Controlla la geometria** per verificare la presenza di eventuali errori nella geometria della forma e correggerli;
-   Usare **Part → Affina forma** per rimuovere eventuali artefatti introdotti da precedenti operazioni booleane prima dei raccordi (e in alcuni casi tra operazioni di raccordi in sequenza);
-   Considerare di usare **Modifica → Preferenze → PartDesign** per abilitare il controllo e l\'affinazione automatica del modello dopo le operazioni booleane e le operazioni basate su schizzi (se queste opzioni sono attive, le prestazioni possono risentirne).


</div>


<div class="mw-translate-fuzzy">

Notare inoltre che la funzione Raccordo è soggetta al problema della [denominazione topologica](Topological_naming_problem/it.md) quando viene apportata una qualsiasi modifica a una fase di modellazione precedente nella catena che influenza il numero di sfaccettature o vertici. Ciò può causare risultati imprevedibili. Fino a quando ciò non viene risolto (possibilmente con V0.19), si consiglia di applicare le operazioni di raccordo e di [smusso](Part_Fillet/it.md) negli ultimi passi della catena.


</div>


<div class="mw-translate-fuzzy">





</div>



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Fillet/it
