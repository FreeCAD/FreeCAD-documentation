---
 GuiCommand:
   Name: Draft Snap Grid
   Name/it: Draft Aggancia Griglia
   MenuLocation: Aggancio , Aggancia griglia
   Workbenches: Draft_Workbench/it, BIM_Workbench/it
   SeeAlso: Draft_Snap/it, Draft_Snap_Lock/it, Draft_ToggleGrid/it, Draft_SelectPlane/it
---

# Draft Snap Grid/it



## Descrizione

L\'opzione <img alt="" src=images/Draft_Snap_Grid.svg  style="width:24px;"> **Draft Aggancia Griglia** aggancia alle intersezioni delle linee della griglia.

![](images/Draft_Snap_Grid_example.png ) 
*Aggancio del secondo punto di una linea alla griglia*



## Utilizzo

Per informazioni generali riguardo gli agganci vedere [Draft Aggancio](Draft_Snap/it.md).

1.  Facoltativamente cambiare il [piano di lavoro e/o la griglia](Draft_SelectPlane/it.md).
2.  Assicurarsi che l\'aggancio sia abilitato. Vedere <img alt="" src=images/Draft_Snap_Lock.svg  style="width:16px;"> [Draft Blocca aggancio](Draft_Snap_Lock/it.md).
3.  Se **Aggancia alla griglia** non è attivo fare una delle seguenti cose:
    -   Premere il bottone **<img src="images/Draft_Snap_Grid.svg" width=16px> [Aggancia griglia](Draft_Snap_Grid/it.md)** nella barra di aggacio di Draft.
    -   [Draft](Draft_Workbench/it.md): Tenere premuto il bottone **<img src="images/Draft_Snap_Lock.svg" width=x16px><img src="images/Toolbar_flyout_arrow.svg" width=x16px>** nella [Draft snap widget](Draft_snap_widget/it.md) e nel menu che si apre selezionare l\'opzione **<img src="images/Draft_Snap_Grid.svg" width=16px> Aggancia griglia**.
    -   [BIM](BIM_Workbench/it.md): Selezionare l\'opzione **Aggancio → <img src="images/Draft_Snap_Grid.svg" width=16px> Aggancia griglia** dal menu o dal menu contestuale della [Vista 3D](3D_view/it.md).
4.  Scegliere un comando Draft o BIM per creare la propria geometria.
5.  Notare che si può anche cambiare le opzioni di aggancio mentre il comando è attivo.
6.  Se necessario, utilizzare [Draft Attiva/disattiva Griglia](Draft_ToggleGrid/it.md) per visualizzare la griglia. La griglia deve essere visibile affinché questa opzione di aggancio funzioni.
7.  Muovere il cursore vicino all\'intersezione di due linee della griglia.
8.  Se un\'intersezione viene trovata il punto viene selezionato e l\'icona <img alt="" src=images/Draft_Snap_Grid.svg  style="width:16px;"> è visualizzata vicino al cursore.
9.  Cliccare per confermare il punto.



## Preferenze

Vedere [Draft Aggancio](Draft_Snap/it#Preferenze.md).

-   Sono disponibili diverse preferenze della griglia: **Modifica → Preferenze... → Draft → Griglia e aggancio**.



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Snap Grid/it
