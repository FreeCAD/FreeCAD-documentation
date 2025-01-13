---
 GuiCommand:
   Name: Draft Snap Perpendicular
   Name/it: Draft Aggancia Perpendicolare
   MenuLocation: Aggancio , Aggancia perpendicolare
   Workbenches: Draft_Workbench/it, BIM_Workbench/it
   SeeAlso: Draft Snap/it, Draft_Snap_Lock/it
---

# Draft Snap Perpendicular/it



## Descrizione

L\'opzione <img alt="" src=images/Draft_Snap_Perpendicular.svg  style="width:24px;"> **Draft Aggancia Perpendicolare** esegue l\'aggancio alle proiezioni perpendicolari di un punto precedente su facce ({{Version/it|0.21}}) e bordi. Le facce e gli spigoli possono appartenere ad oggetti [Draft](Draft_Workbench/it.md) o [BIM](BIM_Workbench/it.md) ma anche ad oggetti creati con altri [ambienti di lavoro](Workbenches/it.md).

Questa opzione di aggancio troverà anche punti su facce e bordi estesi.

![](images/Draft_Snap_Perpendicular_example.png ) 
*Aggancio del secondo punto di una linea al punto perpendicolare su un bordo esteso*



## Utilizzo

Per informazioni generali riguardo gli agganci vedere [Draft Aggancio](Draft_Snap/it.md).

1.  Assicurarsi che l\'aggancio sia abilitato. Vedere <img alt="" src=images/Draft_Snap_Lock.svg  style="width:16px;"> [Draft Blocca aggancio](Draft_Snap_Lock/it.md).
2.  Se **Draft Aggancia Perpendicolare** non è attivo, eseguire una delle seguenti operazioni:
    -   Premere il pulsante **<img src="images/Draft_Snap_Perpendicular.svg" width=16px> [Aggancia perpendicolare](Draft_Snap_Perpendicular/it.md)** nella barra degli strumenti di aggancio Draft.
    -   [Draft](Draft_Workbench/it.md): Tenere premuto il pulsante **<img src="images/Draft_Snap_Lock.svg" width=x16px><img src="images/Toolbar_flyout_arrow.svg" width=x16px>** nel [Draft snap widget](Draft_snap_widget/it.md) e nel menu che si apre selezionare l\'opzione **<img src="images/Draft_Snap_Perpendicular.svg" width=16px> Aggancia perpendicolare**.
    -   [BIM](BIM_Workbench/it.md): Selezionare l\'opzione **Aggancio → <img src="images/Draft_Snap_Perpendicular.svg" width=16px> Aggancia perpendicolare** dal menu o dal menu contestuale della [Vista 3D](3D_view/it.md).
3.  Scegliere un comando Draft o BIM per creare la propria geometria.
4.  Tenere presente che si può anche modificare le opzioni di aggancio mentre un comando è attivo.
5.  Scegliere un primo punto. Questa opzione di aggancio richiede un punto precedente. Il punto perpendicolare verrà determinato in relazione a questo punto.
6.  Spostare il cursore su una faccia o un bordo.
7.  La faccia o il bordo vengono evidenziati.
8.  Se viene trovato un punto perpendicolare, il punto viene contrassegnato e l\'icona <img alt="" src=images/Draft_Snap_Perpendicular.svg  style="width:16px;"> viene visualizzata vicino al cursore.
9.  Se sono presenti più punti perpendicolari: facoltativamente spostare il cursore più vicino a un altro punto perpendicolare. {{Version/it|0.21}}
10. Fare clic per confermare il punto.



## Preferenze

Vedere [Draft Aggancio](Draft_Snap/it#Preferenze.md).



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Snap Perpendicular/it
