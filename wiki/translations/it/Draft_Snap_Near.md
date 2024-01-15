---
 GuiCommand:
   Name: Draft Snap Near
   Name/it: Aggancia Vicino
   Workbenches: Draft_Workbench/it, Arch_Workbench/it
   SeeAlso: Draft Snap/it, Draft_Snap_Lock/it
---

# Draft Snap Near/it



## Descrizione

L\'opzione <img alt="" src=images/Draft_Snap_Near.svg  style="width:24px;"> **Draft Aggancia Vicino** esegue l\'aggancio al punto più vicino su facce e bordi. Le facce e gli spigoli possono appartenere ad oggetti [Draft](Draft_Workbench/it.md) o [Arch](Arch_Workbench/it.md) ma anche ad oggetti creati con altri [ambienti di lavoro](Workbenches/it.md).

![](images/Draft_Snap_Near_example.png ) 
*Aggancio del secondo punto di una linea al punto più vicino su un bordo*



## Utilizzo

Per informazioni generali riguardo gli agganci vedere [Draft Aggancio](Draft_Snap/it.md).

1.  Assicurarsi che l\'aggancio sia abilitato. Vedere <img alt="" src=images/Draft_Snap_Lock.svg  style="width:16px;"> [Draft Blocca aggancio](Draft_Snap_Lock/it.md).
2.  Se **Draft Aggancia Vicino** non è attivo, eseguire una delle seguenti operazioni:
    -   Premere il pulsante **<img src="images/Draft_Snap_Near.svg" width=16px>** nella barra degli strumenti di aggancio di Draft.
    -   Tenere premuto il pulsante **<img src="images/Draft_Snap_Lock.svg" width=x16px><img src="images/Toolbar_flyout_arrow.svg" width=x16px>** nel [Draft snap widget](Draft_snap_widget/it.md) e nel menu che si apre selezionare l\'opzione **<img src="images/Draft_Snap_Near.svg" width=16px> Aggancia Vicino**.
3.  Scegliere un comando [Draft](Draft_Workbench/it.md) o [Arch](Arch_Workbench/it.md) per creare la propria geometria.
4.  Tenere presente che si può anche modificare le opzioni di aggancio mentre un comando è attivo.
5.  Spostare il cursore su una faccia o un bordo.
6.  La faccia o il bordo vengono evidenziati.
7.  Se viene trovato il punto più vicino, il punto viene contrassegnato.
8.  Facoltativamente, spostare il cursore lungo la faccia o il bordo per selezionare un punto diverso più vicino.
9.  Fare clic per confermare il punto.



## Note

-   Non è una buona idea avere [Draft Aggancia Vicino](Draft_Snap_Near/it.md) permanentemente attivo poiché ha la precedenza su molte altre opzioni di aggancio.
-   In {{VersionMinus/it|0.20}} quando si esegue l\'aggancio alle curve, [Draft Aggancia Vicino](Draft_Snap_Near/it.md) si aggancia alla loro rappresentazione segmentata nella [Vista 3D](3D_view/it.md), il che risulta un\'imprecisione. Per ottenere un punto esatto sulla curva, traccia una [Draft Linea](Draft_Line/it.md) attraverso la curva e poi taglia la linea con [Draft Taglia/Estendi](Draft_Trimex/it.md) utilizzando la curva come strumento di taglio.



## Preferenze

Vedere [Draft Aggancio](Draft_Snap/it#Preferenze.md).



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Snap Near/it
