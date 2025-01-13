---
 GuiCommand:
   Name: Part Defeaturing
   Name/it: Part Elimina funzioni
   MenuLocation: Parte , Elimina funzioni
   Workbenches: Part_Workbench/it
   Version: 0.18
   SeeAlso: Defeaturing_Workbench/it, Macro_Parametric_Defeaturing
---

# Part Defeaturing/it



## Descrizione

Lo strumento **Elimina funzione** è destinato alla rimozione di funzioni selezionate dal modello. In questo contesto, le funzioni sono intese come fori, sporgenze, spazi vuoti, smussi, raccordi ecc., che si trovano sul modello.

Lo strumento elimina funzioni può essere molto utile in diversi contesti:

-   Per modificare un solido importato in cui non è disponibile una cronologia delle operazioni.
-   Correggere i difetti nel modello, ad es. riempire gli spazi vuoti, i fori, ecc.
-   Semplificare il modello per l\'analisi numerica, la visualizzazione su dispositivi mobili, ecc.

Le funzioni rimosse sono riempite dall\'estensione delle facce adiacenti, quindi non dovrebbero apparire parti inaspettate nel risultato. Notare che il risultato è una nuova forma che non è collegata all\'originale; quindi non è parametrica.

Per essere disponibile, questo strumento richiede che FreeCAD sia basato su Open Cascade 7.3.0 o successivo. Se non è disponibile nella propria versione di FreeCAD, si può usare il componente aggiuntivo [Ambiente Defeaturing](Defeaturing_Workbench/it.md), che propone delle funzionalità simili anche con versioni precedenti di OCC o FreeCAD.

![](images/Part_Defeaturing_example.png )



## Utilizzo

1.  Selezionare la faccia o le facce che si vuole rimuovere dal modello.
2.  Premere il pulsante **<img src="images/Part_Defeaturing.svg" width=16px> [Elimina funzioni](Part_Defeaturing/it.md)**.
3.  Viene creato un nuovo oggetto etichettato *Defeatured* nel modello [vista ad albero](Tree_view/it.md) e l\'oggetto originale viene nascosto alla vista.



## Link

-   [3D Model Defeaturing](https://dev.opencascade.org/index.php?q=node/1211), l\'annuncio ufficiale sul portale di sviluppo collaborativo di Open Cascade.





{{Part_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Defeaturing/it
