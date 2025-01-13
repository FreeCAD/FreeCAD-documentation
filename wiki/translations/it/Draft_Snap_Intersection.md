---
 GuiCommand:
   Name: Draft Snap Intersection
   Name/it: Draft Aggancia Intersezione
   MenuLocation: Aggancio , Aggancia intersezione
   Workbenches: Draft_Workbench/it, BIM_Workbench/it
   SeeAlso: Draft Snap/it, Draft_Snap_Lock/it
---

# Draft Snap Intersection/it



## Descrizione

L\'opzione <img alt="" src=images/Draft_Snap_Intersection.svg  style="width:24px;"> **Draft Aggancia Intersezione** esegue l\'aggancio all\'intersezione di due bordi. I bordi possono appartenere ad oggetti [Draft](Draft_Workbench/it.md) o [BIM](BIM_Workbench/it.md) ma anche ad oggetti creati con altri [ambienti di lavoro](Workbenches/it.md).

Questa opzione di aggancio troverà anche le intersezioni apparenti dei bordi (estesi) rettilinei se anche <img alt="" src=images/Draft_Snap_WorkingPlane.svg  style="width:16px;"> [Draft Aggancia Piano di lavoro](Draft_Snap_WorkingPlane/it.md) è attivo.

![](images/Draft_Snap_Intersection_example.png ) 
*Aggancio del secondo punto di una linea all'intersezione di due bordi*



## Utilizzo

Per informazioni generali riguardo gli agganci vedere [Draft Aggancio](Draft_Snap/it.md).

1.  Assicurarsi che l\'aggancio sia abilitato. Vedere <img alt="" src=images/Draft_Snap_Lock.svg  style="width:16px;"> [Draft Blocca aggancio](Draft_Snap_Lock/it.md).
2.  Se **Draft Aggancia Intersezione** non è attivo, eseguire una delle seguenti operazioni:
    -   Premere il pulsante **<img src="images/Draft_Snap_Intersection.svg" width=16px> [Aggancia intersezione](Draft_Snap_Intersection/it.md)** nella barra degli strumenti di aggancio Draft.
    -   [Draft](Draft_Workbench/it.md): Tenere premuto il pulsante **<img src="images/Draft_Snap_Lock.svg" width=x16px><img src="images/Toolbar_flyout_arrow.svg" width=x16px>** nel [Draft snap widget](Draft_snap_widget/it.md) e nel menu che si apre selezionare l\'opzione **<img src="images/Draft_Snap_Intersection.svg" width=16px> Aggancia intersezione**.
    -   [BIM](BIM_Workbench/it.md): Selezionare l\'opzione **Aggancio → <img src="images/Draft_Snap_Intersection.svg" width=16px> Aggancia intersezione** dal menu o dal menu contestuale della [Vista 3D](3D_view/it.md).
3.  Scegliere un comando Draft o BIM per creare la propria geometria.
4.  Tenere presente che si può anche modificare le opzioni di aggancio mentre un comando è attivo.
5.  Spostare il cursore su uno dei bordi che si intersecano.
6.  Il bordo viene evidenziato.
7.  Spostare il cursore sull\'altro bordo.
8.  Il bordo viene evidenziato.
9.  Se viene trovata un\'intersezione, il punto viene contrassegnato e l\'icona <img alt="" src=images/Draft_Snap_Intersection.svg  style="width:16px;"> viene visualizzata vicino al cursore.
10. Se i bordi hanno più intersezioni: opzionalmente spostare il cursore più vicino a un\'altra intersezione.
11. Fare clic per confermare il punto.



## Preferenze

Vedere [Draft Aggancio](Draft_Snap/it#Preferenze.md).



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Snap Intersection/it
