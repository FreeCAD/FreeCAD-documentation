# Part Defeaturing/it
---
- GuiCommand:   Name:Part Defeaturing   Name/it:Elimina funzione   MenuLocation:Part - Elimina funzione   Workbenches:[[Part_Workbench/it   Part]]|Version:0.18---


</div>

## Descrizione

Lo strumento **Elimina funzione** è destinato alla rimozione di funzioni selezionate dal modello. In questo contesto, le funzioni sono intese come fori, sporgenze, spazi vuoti, smussi, raccordi ecc., che si trovano sul modello.

Lo strumento elimina funzioni può essere molto utile in diversi contesti:


<div class="mw-translate-fuzzy">

-   Per modificare un solido importato in cui non è disponibile una cronologia delle operazioni;
-   Correggere i difetti nel modello, ad es. riempire gli spazi vuoti, i fori, ecc.
-   Semplificare il modello per l\'analisi numerica, la visualizzazione su dispositivi mobili, ecc;


</div>

Le funzioni rimosse sono riempite dall\'estensione delle facce adiacenti, quindi non dovrebbero apparire parti inaspettate nel risultato. Notare che il risultato è una nuova forma che non è collegata all\'originale; quindi non è parametrica.


<div class="mw-translate-fuzzy">

Per essere disponibile, questo strumento richiede che FreeCAD sia basato su Open Cascade 7.3.0 o successivo. Se non è disponibile nella propria versione di FreeCAD, si può vedere il componente aggiuntivo [Defeaturing Workbench](Defeaturing_Workbench/it.md), che propone delle funzionalità simili anche con versioni precedenti di OCC o FreeCAD.


</div>

![](images/Part_Defeaturing_example.png )

## Utilizzo


<div class="mw-translate-fuzzy">

1.  Selezionare la faccia o le facce che si vuole rimuovere dal modello.
2.  Premere il pulsante **[<img src=images/Part_Defeaturing.svg style="width:24px"> '''Elimina funzione'''**.
3.  Viene creato un nuovo oggetto con l\'etichetta \"Defeatured\" nell\'albero del modello e l\'oggetto originale è nascosto alla vista.


</div>

## Link


<div class="mw-translate-fuzzy">

-   [3D Model Defeaturing](https://dev.opencascade.org/index.php?q=node/1211), l\'annuncio ufficiale sul portale di sviluppo collaborativo di Open Cascade.
-   [Freecad 0.18 Defeaturing](https://peertube.mastodon.host/videos/watch/c6bc5abd-2eb7-48c7-af67-c4d8e6783872), una dimostrazione video (in tedesco) su un modello complesso su PeerTube; anche senza capire la lingua, è abbastanza facile da seguire.
-   <img alt="" src=images/Defeaturing_workbench_icon.svg  style="width:24px;"> [Ambiente Defeaturing](Defeaturing_Workbench/it.md)


</div>


<div class="mw-translate-fuzzy">





</div>



---
![](images/Button_right.svg) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Defeaturing/it
