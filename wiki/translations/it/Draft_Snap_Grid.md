---
 GuiCommand:
   Name: Draft Snap Grid
   Name/it: Griglia
   Workbenches: Draft_Workbench/it, Arch_Workbench/it
   SeeAlso: Draft_Snap/it, Draft_Snap_Lock/it, Draft_ToggleGrid/it, Draft_SelectPlane/it
---

# Draft Snap Grid/it

## Descrizione

L\'opzione <img alt="" src=images/Draft_Snap_Grid.svg  style="width:24px;"> **Aggancia alla Griglia** aggancia all\'intersezione delle linee della griglia. La griglia può essere usata solo se la preferenza **Usa griglia** è selezionata. Vedere [Preferenze](#Preferenze.md).

![](images/Draft_Snap_Grid_example.png ) 
*Aggancio del secondo punto di una linea alla griglia*

## Utilizzo

Per informazioni generali riguardo gli agganci vedere [Draft Snap](Draft_Snap/it.md).

1.  Facoltativamente cambiare il [piano di lavoro e/o la griglia](Draft_SelectPlane/it.md).
2.  Assicurarsi che l\'aggancio sia abilitato. Vedere <img alt="" src=images/Draft_Snap_Lock.svg  style="width:16px;"> [Draft: Attiva/Disattiva aggancio](Draft_Snap_Lock/it.md).
3.  Se **Aggancia alla griglia** non è attivo fare una delle seguenti cose:
    -   Premere il bottone **<img src="images/Draft_Snap_Grid.svg" width=16px>** nella Draft Snap toolbar.
    -   Tenere premuto il bottone **<img src="images/Draft_Snap_Lock.svg" width=x16px><img src="images/Toolbar_flyout_arrow.svg" width=x16px>** nella [Draft snap widget](Draft_snap_widget/it.md) e nel menu che si apre selezionare l\'opzione **<img src="images/Draft_Snap_Grid.svg" width=16px> Aggancia alla griglia**.
4.  Scegliere un comando [Draft](Draft_Workbench.md) o [Arch](Arch_Workbench.md) per creare la propria geometria.
5.  Nota che puoi anche cambiare le opzioni di aggancio mentre il comando è attivo.
6.  La griglia ora è visibile se non lo era di già.
7.  Muovi il cursore vicino all\'intersezione di due linee della griglia.
8.  Se una intersezione viene trovata il punto viene selezionato e l\'icona <img alt="" src=images/Draft_Snap_Grid.svg  style="width:16px;"> è visualizzata vicino al cursore.
9.  Cliccare per confermare il punto.

## Preferenze

Vedere [Draft Snap](Draft_Snap/it#Preferenze.md).

-   Per usare la griglia selezionare: **Edit → Preferences... → Draft → Grid and snapping → Grid → Use grid**. Dopo aver cambiato questa preferenza bisogna riavviare FreeCAD.
-   Alcune ulteriori preferenze sono disponibili: **Edit → Preferences... → Draft → Grid and snapping → Grid**.



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Snap Grid/it
