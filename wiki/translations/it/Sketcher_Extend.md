---
 GuiCommand:
   Name: Sketcher Extend
   Name/it: Estendi
   MenuLocation: Schizzo , Strumenti Sketcher , Estendi bordo
   Workbenches: Sketcher Workbench/it
   Shortcut: **G** **Q**
   Version: 0.17
   SeeAlso: Sketcher_Trimming/it
---

# Sketcher Extend/it



## Descrizione

Lo strumento <img alt="" src=images/Sketcher_Extend.svg  style="width:24px;"> [Sketcher Estendi](Sketcher_Extend/it.md) estende o accorcia una linea o un arco in una posizione arbitraria o in un bordo o punto di destinazione.

<img alt="" src=images/Sketcher_Extend_example_01.png  style="width:600px;"> 
*Mostrati a sinistra (1), i due elementi dello schizzo prima dell'operazione; al centro (2), la linea viene estesa fino all'arco; a destra (3), il risultato finale.*



## Utilizzo

Vedere anche: [Aiuti per il disegno](Sketcher_Workbench/it#Drawing_aids.md).

1.  Esistono diversi modi per richiamare lo strumento:
    -   Premere il pulsante **<img src="images/Sketcher_Extend.svg" width=16px> [Estendi bordo](Sketcher_Extend/it.md)**.
    -   Selezionare l\'opzione **Schizzo → Strumenti Sketcher → <img src="images/Sketcher_Extend.svg" width=16px> Estendi bordo** dal menu.
    -   Fare clic con il pulsante destro del mouse nella [Vista 3D](3D_view/it.md) e selezionare l\'opzione **<img src="images/Sketcher_Extend.svg" width=16px> Estendi bordo** dal menu contestuale.
    -   Usare la scorciatoia da tastiera: **G** quindi **Q**.
2.  Se c\'è una selezione precedente, viene cancellata. Lo strumento non accetta una preselezione.
3.  Il cursore si trasforma in una croce con l\'icona dello strumento.
4.  Selezionare una linea o un arco.
5.  Spostare il cursore nella direzione per estendere o accorciare.
6.  Effettuare una delle seguenti operazioni:
    -   Fare clic su un punto arbitrario.
    -   Per estendere/accorciare a un altro bordo ([Vincoli automatici](Sketcher_Workbench/it#Auto_constraints.md) deve essere abilitato): posizionare il cursore sul bordo di destinazione. Quando è evidenziato e viene visualizzata l\'icona <img alt="" src=images/Sketcher_ConstrainPointOnObject.svg  style="width:16px;"> [Vincolo Punto su oggetto](Sketcher_ConstrainPointOnObject/it.md) accanto al cursore, fare clic per confermare. Viene aggiunto il vincolo.
    -   Per estendere/accorciare fino a un punto (i vincoli automatici devono essere abilitati): posizionare il cursore sul punto target. Quando è evidenziato e accanto al cursore viene visualizzata l\'icona <img alt="" src=images/Sketcher_ConstrainCoincident.svg  style="width:16px;"> [Vincolo coincidente](Sketcher_ConstrainCoincident/it.md), fare clic per confermare. Viene aggiunto il vincolo.
7.  Se lo strumento viene eseguito in [modalità continua](Sketcher_Workbench/it#Continue_modes.md):
    1.  Facoltativamente, continuare ad estendere/accorciare i bordi.
    2.  Per terminare, fare clic in un\'area vuota nella [Vista 3D](3D_view/it.md), fare clic con il pulsante destro del mouse o premere **Esc** oppure avviare un altro strumento di creazione di geometrie o vincoli.



## Note

-   Se non completamente vincolato, anche il bordo o il punto di destinazione può essere modificato.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher Extend/it
