---
- GuiCommand:/it   Name:PartDesign Thickness   Name/it:Spessore   Workbenches:[MenuLocation:Part Design → Spessore   Version:0.17   SeeAlso:[[Part_Thickness/it|Spessore di Parte](PartDesign_Workbench/it___PartDesign]].md)---


</div>

## Descrizione

Lo strumento **Spessore** funziona su un corpo solido e lo trasforma in un oggetto cavo, con almeno una faccia aperta, e assegna a ciascuna delle sue facce rimanenti uno spessore uniforme. Su alcuni solidi permette di velocizzare significativamente il lavoro ed evita di fare estrusioni e tasche.

<img alt="" src=images/PartDesign_Thickness_example.svg  style="width:600px;"> 
*The thickness tool applied to a face (B) of a solid (A), resulting in the hollow object (C).*

## Utilizzo


<div class="mw-translate-fuzzy">

1.  Selezionare una o più facce nel corpo attivo.
2.  Premere il pulsante **<img src="images/PartDesign_Thickness.svg" width=24px> '''Spessore'''**.
3.  Definire i **Parametri dello spessore** (vedere le [Opzioni](#Options/it.md)).
4.  Per aggiungere più facce da aprire, premere su **Aggiungi faccia** e selezionare una faccia nella vista 3D.
5.  Per rimuovere una faccia selezionata in precedenza, premere su **Rimuovi faccia** e selezionare una faccia nella vista 3D o fare clic con il tasto destro sull\'etichetta della faccia nell\'elenco e selezionare *Rimuovi*.
6.  Premere **OK**.


</div>

## Opzioni

-   **Thickness**: Spessore della parete dell\'oggetto risultante. Impostare il valore desiderato.
-   **Mode**
    -   *Skin*: Selezionare questa opzione per ottenere un oggetto simile ad un vaso, senza testa ma con il fondo
    -   *Pipe*: Selezionare questa opzione per ottenere un oggetto simile ad un tubo, senza testa e senza fondo. In questo caso può essere conveniente selezionare le facce da eliminare prima di avviare lo strumento. Aiutarsi con i pulsanti delle viste predefinite o utilizzare i tasti numerici.
    -   *Recto Verso*:
-   **Join Type**
    -   *Arc*: rimuove i bordi esterni e crea un raccordo con un raggio uguale allo spessore definito.
    -   *Intersection*: quando le facce sono spostate verso l\'esterno, gli spigoli tra le facce vengono mantenuti.
-   **Make thickness inwards**: quando è selezionato, le facce sono spostate verso l\'interno.

## Limitazioni


<div class="mw-translate-fuzzy">

-   Deve essere selezionata almeno una faccia da aprire.
-   Se lo spessore va verso l\'interno, il valore deve essere inferiore alla dimensione più piccola del corpo.
-   Il comando potrebbe non riuscire con forme complesse. In questo contesto la superficie di un cono deve già essere considerata complessa.
    -   [Sweep additivi](PartDesign_AdditivePipe/it.md) o [Loft additivo](PartDesign_AdditiveLoft.md) possono funzionare meglio per creare forme complesse


</div>

## Esempio

1.  Creare un pad dallo schizzo
2.  Creare un secondo schizzo sul piano XY
3.  Creare un secondo pad dal secondo schizzo

Come nelle seguenti immagini:

![](images/Braga-primoPad.png )

![](images/Braga-secondoschizzo.png )

![](images/Braga-secondo_Pad.png )

Poi

1.  Selezionare una faccia circolare
2.  Selezionare **<img src="images/PartDesign_Thickness.svg" width=24px> Spessore
**
3.  Aggiungere le altre facce circolari alla selezione

Risultato: ![](images/Brga-spessore.png )

## Errori noti 


<div class="mw-translate-fuzzy">

-   BRep\_API: command not done
-   BRep\_Tool:: no parameter on edge
-   Silently Fails


</div>


<div class="mw-translate-fuzzy">





</div>


{{PartDesign Tools navi

}} 
