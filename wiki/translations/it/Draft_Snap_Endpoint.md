---
 GuiCommand:
   Name: Draft Snap Endpoint
   Name/it: Draft Aggancia Punto Finale
   Workbenches: Draft_Workbench/it, Arch_Workbench/it
   SeeAlso: Draft_Snap/it, Draft_Snap_Lock/it
---

# Draft Snap Endpoint/it



## Descrizione

L\'opzione <img alt="" src=images/Draft_Snap_Endpoint.svg  style="width:24px;"> **Draft Aggancia Punto Finale** esegue l\'aggancio ai punti finali dei bordi. I bordi possono appartenere ad oggetti [Draft](Draft_Workbench/it.md) o [Arch](Arch_Workbench/it.md) ma anche ad oggetti creati con altri [ambienti di lavoro](Workbenches/it.md).

![](images/Draft_Snap_Endpoint_example.png ) 
*Aggancio del secondo punto di una linea al punto finale di un bordo*



## Utilizzo

Per informazioni generali riguardo gli agganci vedere [Draft Aggancio](Draft_Snap/it.md).

1.  Assicurarsi che l\'aggancio sia abilitato. Vedere <img alt="" src=images/Draft_Snap_Lock.svg  style="width:16px;"> [Draft Blocca aggancio](Draft_Snap_Lock/it.md).
2.  Se **Draft Aggancia Punto Finale** non è attivo, eseguire una delle seguenti operazioni:
    -   Premere il pulsante **<img src="images/Draft_Snap_Endpoint.svg" width=16px>** nella barra degli strumenti di aggancio Draft.
    -   Tenere premuto il pulsante **<img src="images/Draft_Snap_Lock.svg" width=x16px><img src="images/Toolbar_flyout_arrow.svg" width=x16px>** nel [Draft snap widget](Draft_snap_widget/it.md) e nel menu che si apre selezionare l\'opzione **<img src="images/Draft_Snap_Endpoint.svg" width=16px> Aggancia Punto Finale**.
3.  Scegliere un comando [Draft](Draft_Workbench/it.md) o [Arch](Arch_Workbench/it.md) per creare la propria geometria.
4.  Tenere presente che è possibile anche modificare le opzioni di aggancio mentre un comando è attivo.
5.  Spostare il cursore su un bordo.
6.  Il bordo viene evidenziato.
7.  Se viene trovato un punto finale, il punto viene contrassegnato e l\'icona <img alt="" src=images/Draft_Snap_Endpoint.svg  style="width:16px;"> viene visualizzata vicino al cursore.
8.  Facoltativamente, spostare il cursore più vicino all\'altro punto finale per selezionare invece quel punto.
9.  Fare clic per confermare il punto.



## Preferenze

Vedere [Draft Aggancio](Draft_Snap/it#Preferenze.md).



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Snap Endpoint/it
