---
 GuiCommand:
   Name: Draft Snap Extension
   Name/it: Draft Aggancia Estensione
   Workbenches: Draft_Workbench/it, Arch_Workbench/it
   SeeAlso: Draft Snap/it, Draft_Snap_Lock/it
---

# Draft Snap Extension/it



## Descrizione

L\'opzione <img alt="" src=images/Draft_Snap_Extension.svg  style="width:24px;"> **Draft Aggancia Estensione** esegue l\'aggancio ad una linea immaginaria che si estende oltre i punti finali dei bordi diritti. I bordi possono appartenere ad oggetti [Draft](Draft_Workbench/it.md) o [Arch](Arch_Workbench/it.md) ma anche ad oggetti creati con altri [ambienti di lavoro](Workbenches/it.md).

È possibile fare riferimento a un massimo di 2 (o 8 {{Version/it|0.20}}) bordi con questa opzione di aggancio e [Draft Aggancia Parallelo](Draft_Snap_Parallel/it.md), rendendo possibile l\'aggancio alle intersezioni virtuali. Entrambe le opzioni di aggancio possono anche essere combinate con altre opzioni di aggancio.

![](images/Draft_Snap_Extension_example.png ) 
*Aggancio del secondo punto di una linea all'estensione di un bordo*



## Utilizzo


{{Userdocnavi/it}}

1.  Assicurarsi che l\'aggancio sia abilitato. Vedere <img alt="" src=images/Draft_Snap_Lock.svg  style="width:16px;"> [Draft Blocca aggancio](Draft_Snap_Lock/it.md).
2.  Se **Draft Aggancia Estensione** non è attivo, eseguire una delle seguenti operazioni:
    -   Premere il pulsante **<img src="images/Draft_Snap_Extension.svg" width=16px>** nella barra degli strumenti di aggancio Draft.
    -   Tenere premuto il pulsante **<img src="images/Draft_Snap_Lock.svg" width=x16px><img src="images/Toolbar_flyout_arrow.svg" width=x16px>** nel [Draft snap widget](Draft_snap_widget/it.md) e nel menu che si apre selezionare l\'opzione **<img src="images/Draft_Snap_Extension.svg" width=16px> Aggancia Estensione**.
3.  Scegliere un comando [Draft](Draft_Workbench/it.md) o [Arch](Arch_Workbench/it.md) per creare la propria geometria.
4.  Tenere presente che si può anche modificare le opzioni di aggancio mentre un comando è attivo.
5.  Spostare il cursore su un bordo dritto.
6.  Il bordo viene evidenziato.
7.  Se ora si sposta il ​​cursore oltre gli estremi del bordo, si vedrà apparire una linea tratteggiata quando il cursore si trova sul bordo esteso.
8.  Il punto viene contrassegnato e l\'icona <img alt="" src=images/Draft_Snap_Extension.svg  style="width:16px;"> viene visualizzata vicino al cursore.
9.  Fare clic per confermare il punto.



## Preferenze

Vedere [Draft Aggancio](Draft_Snap/it#Preferenze.md).



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Snap Extension/it
