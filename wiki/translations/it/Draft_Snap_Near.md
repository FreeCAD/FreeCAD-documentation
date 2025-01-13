---
 GuiCommand:
   Name: Draft Snap Near
   Name/it: Draft Aggancia Vicino
   MenuLocation: Aggancio , Aggancia vicino
   Workbenches: Draft_Workbench/it, BIM_Workbench/it
   SeeAlso: Draft Snap/it, Draft_Snap_Lock/it
---

# Draft Snap Near/it



## Descrizione

L\'opzione <img alt="" src=images/Draft_Snap_Near.svg  style="width:24px;"> **Draft Aggancia Vicino** esegue l\'aggancio al punto più vicino su facce e bordi. Le facce e gli spigoli possono appartenere ad oggetti [Draft](Draft_Workbench/it.md) o [BIM](BIM_Workbench/it.md) ma anche ad oggetti creati con altri [ambienti di lavoro](Workbenches/it.md).

![](images/Draft_Snap_Near_example.png ) 
*Aggancio del secondo punto di una linea al punto più vicino su un bordo*



## Utilizzo

Per informazioni generali riguardo gli agganci vedere [Draft Aggancio](Draft_Snap/it.md).

1.  Assicurarsi che l\'aggancio sia abilitato. Vedere <img alt="" src=images/Draft_Snap_Lock.svg  style="width:16px;"> [Draft Blocca aggancio](Draft_Snap_Lock/it.md).
2.  Se **Draft Aggancia Vicino** non è attivo, eseguire una delle seguenti operazioni:
    -   Premere il pulsante **<img src="images/Draft_Snap_Near.svg" width=16px> [Aggancia vicino](Draft_Snap_Near/it.md)** nella barra degli strumenti di aggancio di Draft.
    -   [Draft](Draft_Workbench/it.md): Tenere premuto il pulsante **<img src="images/Draft_Snap_Lock.svg" width=x16px><img src="images/Toolbar_flyout_arrow.svg" width=x16px>** nel [Draft snap widget](Draft_snap_widget/it.md) e nel menu che si apre selezionare l\'opzione **<img src="images/Draft_Snap_Near.svg" width=16px> Aggancia vicino**.
    -   [BIM](BIM_Workbench/it.md): Selezionare l\'opzione **Aggancio → <img src="images/Draft_Snap_Near.svg" width=16px> Aggancia vicino** dal menu o dal menu contestuale della [Vista 3D](3D_view/it.md).
3.  Scegliere un comando Draft o BIM per creare la propria geometria.
4.  Tenere presente che si può anche modificare le opzioni di aggancio mentre un comando è attivo.
5.  Spostare il cursore su una faccia o un bordo.
6.  La faccia o il bordo vengono evidenziati.
7.  Se viene trovato il punto più vicino, il punto viene contrassegnato.
8.  Facoltativamente, spostare il cursore lungo la faccia o il bordo per selezionare un punto diverso più vicino.
9.  Fare clic per confermare il punto.



## Note

-   Non è una buona idea avere [Draft Aggancia Vicino](Draft_Snap_Near/it.md) permanentemente attivo poiché ha la precedenza su molte altre opzioni di aggancio.



## Preferenze

Vedere [Draft Aggancio](Draft_Snap/it#Preferenze.md).



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Snap Near/it
