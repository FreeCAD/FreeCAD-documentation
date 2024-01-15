---
 GuiCommand:
   Name: Draft Snap Parallel
   Name/it: Draft Aggancia Parallelo
   Workbenches: Draft_Workbench/it, Arch_Workbench/it
   SeeAlso: Draft Snap/it, Draft_Snap_Lock/it
---

# Draft Snap Parallel/it



## Descrizione

L\'opzione <img alt="" src=images/Draft_Snap_Parallel.svg  style="width:24px;"> **Draft Aggancia Parallelo** esegue l\'aggancio ad una linea immaginaria parallela ai bordi diritti. I bordi possono appartenere ad oggetti [Draft](Draft_Workbench/it.md) o [Arch](Arch_Workbench/it.md) ma anche ad oggetti creati con altri [ambienti di lavoro](Workbenches/it.md).

È possibile fare riferimento a un massimo di 2 (o 8 {{Version/it|0.20}}) bordi con questa opzione di aggancio e [Draft Aggancia Estensioni](Draft_Snap_Extension/it.md), rendendo possibile l\'aggancio alle intersezioni virtuali. Entrambe le opzioni di aggancio possono anche essere combinate con altre opzioni di aggancio.

![](images/Draft_Snap_Parallel_example.png ) 
*Aggancio del secondo punto di una linea a una linea invisibile che è parallela a un bordo*



## Utilizzo

Per informazioni generali riguardo gli agganci vedere [Draft Aggancio](Draft_Snap/it.md).

1.  Assicurarsi che l\'aggancio sia abilitato. Vedere <img alt="" src=images/Draft_Snap_Lock.svg  style="width:16px;"> [Draft Blocca aggancio](Draft_Snap_Lock/it.md).
2.  Se **Draft Aggancia Parallelo** non è attivo, eseguire una delle seguenti operazioni:
    -   Premere il pulsante **<img src="images/Draft_Snap_Parallel.svg" width=16px>** nella barra degli strumenti di aggancio Draft.
    -   Tenere premuto il pulsante **<img src="images/Draft_Snap_Lock.svg" width=x16px><img src="images/Toolbar_flyout_arrow.svg" width=x16px>** nel [Draft snap widget](Draft_snap_widget/it.md) e nel menu che si apre selezionare l\'opzione **<img src="images/Draft_Snap_Parallel.svg" width=16px> Aggancia Parallelo**.
3.  Scegliere un comando [Draft](Draft_Workbench/it.md) o [Arch](Arch_Workbench/it.md) per creare la propria geometria.
4.  Tenere presente che si può anche modificare le opzioni di aggancio mentre un comando è attivo.
5.  Scegliere un primo punto. Questa opzione di aggancio richiede un punto precedente. La linea di cattura parallela passerà attraverso questo punto.
6.  Spostare il cursore su un bordo dritto.
7.  Il bordo viene evidenziato.
8.  Se ora si sposta il ​​cursore attorno al punto precedente si noterà un effetto \"magnetico\" quando il cursore si trova sulla linea di cattura parallela.
9.  Il punto viene contrassegnato e l\'icona <img alt="" src=images/Draft_Snap_Parallel.svg  style="width:16px;"> viene visualizzata vicino al cursore.
10. Fare clic per confermare il punto.



## Preferenze

Vedere [Draft Aggancio](Draft_Snap/it#Preferenze.md).



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Snap Parallel/it
