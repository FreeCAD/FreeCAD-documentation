---
 GuiCommand:
   Name: Draft Snap Special
   Name/it: Draft Aggancia Speciale
   Workbenches: Draft_Workbench/it, Arch_Workbench/it
   Version: 0.17
   SeeAlso: Draft Snap/it, Draft_Snap_Lock/it
---

# Draft Snap Special/it



## Descrizione

L\'opzione <img alt="" src=images/Draft_Snap_Special.svg  style="width:24px;"> **Draft Aggancia Speciale** esegue l\'aggancio ai [punti speciali](#Supported_special_points.md) definiti dall\'oggetto. Gli oggetti supportati sono [Arch Muri](Arch_Wall/it.md), [Arch Strutture](Arch_Structure/it.md) e [Arch Arredamento](Arch_Equipment/it.md).

![](images/Draft_Snap_Special_example.png ) 
*Aggancio del secondo punto di una linea a un punto speciale di un muro ad arco, che è un vertice del suo oggetto Base*



## Utilizzo

Per informazioni generali riguardo gli agganci vedere [Draft Aggancio](Draft_Snap/it.md).

1.  Assicurarsi che l\'aggancio sia abilitato. Vedere <img alt="" src=images/Draft_Snap_Lock.svg  style="width:16px;"> [Draft Blocca aggancio](Draft_Snap_Lock.md).
2.  Se **Draft Aggancia Speciale** non è attivo, eseguire una delle seguenti operazioni:
    -   Premiere il pulsante **<img src="images/Draft_Snap_Special.svg" width=16px>** nella barra degli strumenti di aggancio di Draft.
    -   Tenere premuto il pulsante **<img src="images/Draft_Snap_Lock.svg" width=x16px><img src="images/Toolbar_flyout_arrow.svg" width=x16px>** nel [Draft snap widget](Draft_snap_widget/it.md) e nel menu che si apre selezionare l\'opzione **<img src="images/Draft_Snap_Special.svg" width=16px> Aggancia Speciale**.
3.  Scegliere un comando [Draft](Draft_Workbench/it.md) o [Arch](Arch_Workbench/it.md) per creare la propria geometria.
4.  Tenere presente che si può anche modificare le opzioni di aggancio mentre un comando è attivo.
5.  Spostare il cursore su un oggetto supportato.
6.  L\'oggetto viene evidenziato.
7.  Se viene trovato un punto speciale, il punto viene contrassegnato e l\'icona <img alt="" src=images/Draft_Snap_Special.svg  style="width:16px;"> viene visualizzata vicino al cursore.
8.  Se l\'oggetto ha più punti speciali: opzionalmente spostare il cursore più vicino a un altro punto speciale.
9.  Fare clic per confermare il punto.



## Punti speciali supportati 

-   I vertici dell\'oggetto **Base** di <img alt="" src=images/Arch_Wall.svg  style="width:16px;"> [Arch Muri](Arch_Wall/it.md).
-   Il punto **Placement** di <img alt="" src=images/Arch_Structure.svg  style="width:16px;"> [Arch Strutture](Arch_Structure/it.md).
-   I **Snap Points** di <img alt="" src=images/Arch_Equipment.svg  style="width:16px;"> [Arch Arredamento](Arch_Equipment/it.md).



## Preferenze

Vedere [Draft Aggancio](Draft_Snap/it#Preferenze.md).



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Snap Special/it
