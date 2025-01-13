---
 GuiCommand:
   Name: Draft Snap Angle
   Name/it: Draft Aggancia Angolo
   MenuLocation: Aggancio , Aggancia Angolo
   Workbenches: Draft_Workbench/it, BIM_Workbench/it
   SeeAlso: Draft Snap/it, Draft_Snap_Lock/it
---

# Draft Snap Angle/it



## Descrizione

L\'opzione <img alt="" src=images/Draft_Snap_Angle.svg  style="width:24px;"> **Draft Aggancia Angolo** esegue l\'aggancio ai punti cardinali speciali sui bordi circolari, a multipli di 30° e 45°. I bordi possono appartenere ad oggetti [Draft](Draft_Workbench/it.md) o [BIM](BIM_Workbench/it.md) ma anche ad oggetti creati con altri [ambienti di lavoro](Workbenches/it.md).

![](images/Draft_Snap_Angle_example.png ) 
*Aggancio del secondo punto di una linea al punto -30° su un bordo circolare. I piccoli cerchi magenta indicano tutti i punti cardinali speciali disponibili.*

 {{Userdocnavi/it}}

Per informazioni generali riguardo gli agganci vedere [Draft Aggancio](Draft_Snap/it.md).

1.  Assicurarsi che l\'aggancio sia abilitato. Vedere <img alt="" src=images/Draft_Snap_Lock.svg  style="width:16px;"> [Draft Blocca aggancio](Draft_Snap_Lock/it.md).
2.  Se **Draft Aggancia Angolo** non è attivo, eseguire una delle seguenti operazioni:
    -   Premere il pulsante **<img src="images/Draft_Snap_Angle.svg" width=16px> [Aggancia angolo](Draft_Snap_Angle/it.md)** nella barra degli strumenti di aggancio Draft.
    -   [Draft](Draft_Workbench/it.md): Tenere premuto il pulsante **<img src="images/Draft_Snap_Lock.svg" width=x16px><img src="images/Toolbar_flyout_arrow.svg" width=x16px>** nel [Draft snap widget](Draft_snap_widget/it.md) e nel menu che si apre selezionare l\'opzione **<img src="images/Draft_Snap_Angle.svg" width=16px> Aggancia angolo**.
    -   [BIM](BIM_Workbench/it.md): Selezionare l\'opzione **Aggancio → <img src="images/Draft_Snap_Angle.svg" width=16px> Aggancia angolo** dal menu, o dal menu contestuale della [Vista 3D](3D_view/it.md).
3.  Scegliere un comando Draft o BIM per creare la propria geometria.
4.  Tenere presente che si può anche modificare le opzioni di aggancio mentre un comando è attivo.
5.  Spostare il cursore su un bordo circolare.
6.  Il bordo viene evidenziato.
7.  Se viene trovato un punto cardinale, il punto viene contrassegnato e l\'icona <img alt="" src=images/Draft_Snap_Angle.svg  style="width:16px;"> viene visualizzata vicino al cursore.
8.  Facoltativamente, spostare il cursore più vicino a un altro punto cardinale per selezionare invece quel punto.
9.  Fare clic per confermare il punto.



## Preferenze

Vedere [Draft Aggancio](Draft_Snap/it#Preferenze.md).



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Snap Angle/it
