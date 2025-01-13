---
 GuiCommand:
   Name: Draft Snap Midpoint
   Name/it: Draft Aggancia Punto medio
   MenuLocation: Aggancio , Aggancia punto medio
   Workbenches: Draft_Workbench/it, BIM_Workbench/it
   SeeAlso: Draft Snap/it, Draft_Snap_Lock/it
---

# Draft Snap Midpoint/it



## Descrizione

L\'opzione <img alt="" src=images/Draft_Snap_Midpoint.svg  style="width:24px;"> **Draft Aggancia Punto Medio** esegue l\'aggancio al punto medio dei bordi. I bordi possono appartenere ad oggetti [Draft](Draft_Workbench/it.md) o [BIM](BIM_Workbench/it.md) ma anche ad oggetti creati con altri [ambienti di lavoro](Workbenches/it.md).

![](images/Draft_Snap_Midpoint_example.png ) 
*Aggancio del secondo punto di una linea al punto medio di un bordo*



## Utilizzo

Per informazioni generali riguardo gli agganci vedere [Draft Aggancio](Draft_Snap/it.md).

1.  Assicurarsi che l\'aggancio sia abilitato. Vedere <img alt="" src=images/Draft_Snap_Lock.svg  style="width:16px;"> [Draft Blocca aggancio](Draft_Snap_Lock.md).
2.  Se **Draft Aggancia Punto Medio** non è attivo, eseguire una delle seguenti operazioni:
    -   Premere il pulsante **<img src="images/Draft_Snap_Midpoint.svg" width=16px> [Aggancia punto medio](Draft_Snap_Midpoint/it.md)** nella barra degli strumenti di aggancio Draft.
    -   [Draft](Draft_Workbench/it.md): Tenere premuto il pulsante **<img src="images/Draft_Snap_Lock.svg" width=x16px><img src="images/Toolbar_flyout_arrow.svg" width=x16px>** nel [Draft snap widget](Draft_snap_widget/it.md) e nel menu che si apre selezionare l\'opzione **<img src="images/Draft_Snap_Midpoint.svg" width=16px> Aggancia punto medio**.
    -   [BIM](BIM_Workbench/it.md): Selezionare l\'opzione **Aggancio → <img src="images/Draft_Snap_Midpoint.svg" width=16px> Aggancia punto medio** dal menu o dal menu contestuale della [Vista 3D](3D_view/it.md).
3.  Scegliere un comando Draft o BIM per creare la propria geometria.
4.  Tenere presente che si può anche modificare le opzioni di aggancio mentre un comando è attivo.
5.  Spostare il cursore su un bordo.
6.  Il bordo viene evidenziato.
7.  Se viene trovato un punto medio, il punto viene contrassegnato e l\'icona <img alt="" src=images/Draft_Snap_Midpoint.svg  style="width:16px;"> viene visualizzata vicino al cursore.
8.  Fare clic per confermare il punto.



## Preferenze

Vedere [Draft Aggancio](Draft_Snap/it#Preferenze.md).



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Snap Midpoint/it
