---
- GuiCommand:/it   Name:PartDesign_Pocket   Name/it:Tasca   MenuLocation:PartDesign → Tasca   Workbenches:[PartDesign](PartDesign_Workbench/it.md)---


</div>

## Descrizione

Lo strumento **Tasca** scava un solido estrudendo uno schizzo, o una faccia di un solido, in un percorso rettilineo e sottraendolo dal solido.

![](images/PartDesign_Pocket_example.svg ) \'\'A sinistra lo schizzo del profilo (A) è mappato sulla faccia superiore del solido di base (B); a destra il risultato della tasca. \'\'

## Utilizzo

1.  Selezionare lo schizzo da usare per lo scavo.

    :   Lo schizzo selezionato deve essere mappato su una faccia planare di un solido esistente o su un oggetto Part Design, altrimenti si riceve un messaggio di errore. {{VersionMinus/it|0.16}}
2.  Premere il pulsante **<img src="images/PartDesign_Pocket.svg" width=16px> '''Pocket'''**.
3.  Impostare i parametri Pocket (vedere successiva sezione).
4.  Cliccare OK.

### Opzioni

![](images/Pocket_options_it.png )


<div class="mw-translate-fuzzy">

Quando si crea una cavità, la finestra di dialogo **Parametri Tasca** offre quattro diversi modi per specificare la lunghezza (profondità) di estrusione dello scavo:

#### Quota

Inserire un valore numerico per la profondità della tasca. La direzione di default per l\'estrusione è verso l\'interno del supporto. Le estrusioni si realizzano [normali](http://en.wikipedia.org/wiki/Surface_normal) al piano di definizione dello schizzo.

Le quote negative non sono possibili. Al suo posto usare invece l\'opzione **Invertita**.

#### Fino al primo 

La tasca viene prodotta fino alla prima faccia del supporto nella direzione di estrusione. In altre parole, viene asportato tutto il materiale fino a raggiungere uno spazio vuoto.

#### Attraverso tutto 

La tasca scava attraverso tutto il materiale nella direzione di estrusione. Quando si attiva l\'opzione **Simmetrico al piano** lo scavo viene prodotto attraverso tutto il materiale in entrambe le direzioni.

#### Fino alla faccia 

La tasca si estrude fino a una faccia del supporto che può essere scelta facendo clic su di essa.

### Due dimensioni 

Questo permette di inserire una seconda lunghezza per estendere la tasca nella direzione opposta (nel supporto). Anche questa può essere cambiata spuntando l\'opzione **Invertita**. {{VersionPlus/it|0.17}}


</div>

### Up to face 

The pocket will extrude up to a face in the support that can be chosen by clicking on it.

### Two dimensions 

This allows to enter a second length in which the pocket should extend in the opposite direction (into the support). Again can be changed by ticking the **Reversed** option. <small>(v0.17)</small> 

### Limitazioni

-   Quando è possibile utilizzare il tipo **Quota** oppure **Attraverso tutto** perché gli altri tipi a volte danno problemi quando essi vengono utilizzati per essere replicati in schiere.
-   Inoltre, la funzione tasca ha le stesse [limitazioni](PartDesign_Pad#Limitations.md) della funzione Pad.

### Link utili 

Un [esempio](http://forum.freecadweb.org/viewtopic.php?f=3&t=3733&start=10) di applicazione pratica nel forum.


<div class="mw-translate-fuzzy">





</div>


{{PartDesign Tools navi

}} 
