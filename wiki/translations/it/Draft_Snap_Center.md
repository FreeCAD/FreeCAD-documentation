---
 GuiCommand:
   Name: Draft Snap Center
   Name/it: Aggancia Centro
   Workbenches: Draft_Workbench/it, Arch_Workbench/it
   SeeAlso: Draft Snap/it, Draft_Snap_Lock/it
---

# Draft Snap Center/it



## Descrizione

L\'opzione <img alt="" src=images/Draft_Snap_Center.svg  style="width:24px;"> **Draft Aggancia Centro** esegue l\'aggancio al punto centrale delle facce e dei bordi circolari e al punto **Placement** di [Draft Piani di Lavoro Proxy](Draft_WorkingPlaneProxy/it.md) e [Arch Parti di Edificio](Arch_BuildingPart/it.md). Le facce e gli spigoli possono appartenere ad oggetti [Draft](Draft_Workbench/it.md) o [Arch](Arch_Workbench/it.md) ma anche ad oggetti creati con altri [ambienti di lavoro](Workbenches/it.md).

![](images/Draft_Snap_Center_example_arc.png ) 
*Aggancio del secondo punto di una linea al centro di un bordo circolare*

![](images/Draft_Snap_Center_example_buildingpart.png ) 
*Aggancio del secondo punto di una linea al punto di Posizionamento di un Arch Parte di Edificio*



## Utilizzo

Per informazioni generali riguardo gli agganci vedere [Draft Aggancio](Draft_Snap/it.md).

1.  Assicurarsi che l\'aggancio sia abilitato. Vedere <img alt="" src=images/Draft_Snap_Lock.svg  style="width:16px;"> [Draft Blocca aggancio](Draft_Snap_Lock.md).
2.  Se **Draft Aggancia Centro** non è attivo, eseguire una delle seguenti operazioni:
    -   Premere il pulsante **<img src="images/Draft_Snap_Center.svg" width=16px>** nella barra degli strumenti di aggancio Draft.
    -   Tenere premuto il pulsante **<img src="images/Draft_Snap_Lock.svg" width=x16px><img src="images/Toolbar_flyout_arrow.svg" width=x16px>** nel [Draft snap widget](Draft_snap_widget/it.md) e nel menu che si apre selezionare l\'opzione **<img src="images/Draft_Snap_Center.svg" width=16px> Aggancia Centro**.
3.  Scegliere un comando [Draft](Draft_Workbench/it.md) o [Arch](Arch_Workbench/it.md) per creare la propria geometria.
4.  Tenere presente che si può anche modificare le opzioni di aggancio mentre un comando è attivo.
5.  Effettuare una delle seguenti operazioni:
    -   Per selezionare il punto centrale di una faccia o di un bordo circolare:
        -   Spostare il cursore sulla faccia o sul bordo.
        -   La faccia o il bordo vengono evidenziati.
    -   Per selezionare il punto **Placement** di un [Draft Piano di Lavoro Proxy](Draft_WorkingPlaneProxy/it.md):
        -   Spostare il cursore su qualsiasi elemento del piano di lavoro proxy.
        -   Il piano di lavoro proxy non è evidenziato.
    -   Per selezionare il punto **Placement** di un [Arch Parte di Edificio](Arch_BuildingPart/it.md):
        -   Spostare il cursore su uno dei bordi del simbolo dell\'asse piccolo della Parte di Edificio, o sul testo accanto ad esso che visualizza la **Label** della Parte di Edificio e il suo livello.
        -   Vengono evidenziati solo i bordi del simbolo dell\'asse. Il testo non è evidenziato.
6.  Se viene trovato un punto, il punto viene contrassegnato e l\'icona <img alt="" src=images/Draft_Snap_Center.svg  style="width:16px;"> viene visualizzata vicino al cursore.
7.  Fare clic per confermare il punto.



## Preferenze

Vedere [Draft Aggancio](Draft_Snap/it#Preferenze.md).



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Snap Center/it
