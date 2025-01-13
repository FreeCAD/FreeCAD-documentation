---
 GuiCommand:
   Name: Sketcher Trimming
   Name/it: Sketcher Rifila
   MenuLocation: Schizzo , Strumenti Sketcher , Rifila bordo
   Workbenches: Sketcher_Workbench/it
   Shortcut: **G** **T**
   Version: 0.12
   SeeAlso: Sketcher_Split/it, Sketcher_Extend/it
---

# Sketcher Trimming/it



## Descrizione

Lo strumento <img alt="" src=images/Sketcher_Trimming.svg  style="width:24px;"> [Sketcher Rifila](Sketcher_Trimming/it.md) ritaglia un bordo alle intersezioni più vicine con altri bordi. Se il bordo selezionato non interseca altri bordi verrà eliminato.



## Utilizzo

Vedere anche: [Aiuti per il disegno](Sketcher_Workbench/it#Drawing_aids.md).

1.  Esistono diversi modi per richiamare lo strumento:
    -   Premere il pulsante **<img src="images/Sketcher_Trimming.svg" width=16px> [Rifila bordo](Sketcher_Trimming/it.md)**.
    -   Selezionare l\'opzione **Sketcher → Strumenti Sketcher → <img src="images/Sketcher_Trimming.svg" width=16px> Rifila bordo** dal menu.
    -   Fare clic con il pulsante destro del mouse nella [Vista 3D](3D_view/it.md) e selezionare l\'opzione **<img src="images/Sketcher_Trimming.svg" width=16px> Rifila bordo** dal menu contestuale.
    -   Usa la scorciatoia da tastiera: **G** quindi **T**.
2.  Se c\'è una selezione precedente, viene cancellata. Lo strumento non accetta una preselezione.
3.  Il cursore si trasforma in una croce con l\'icona dello strumento.
4.  Esistono due modalità:
    -   Rifilare con un solo clic:
        1.  Spostare il cursore su una porzione del bordo da tagliare.
        2.  Il bordo viene evidenziato e i punti di ritaglio vengono contrassegnati con cerchi temporanei.
        3.  Fare clic per confermare.
        4.  Il bordo viene tagliato nei punti contrassegnati.
    -   Rifilare tenendo premuto e trascinato: {{Version/it|1.0}}
        1.  Tenere premuto il pulsante sinistro del mouse.
        2.  Spostare il cursore sulle porzioni di bordi da tagliare.
        3.  Il taglio avviene immediatamente.
        4.  Rilasciare il pulsante sinistro del mouse.
5.  Se una porzione viene ritagliata, i vincoli applicabili esistenti vengono trasferiti al nuovo bordo risultante. [Vincoli punto sull\'oggetto](Sketcher_ConstrainPointOnObject/it.md) vengono aggiunti tra i punti finali del bordo tagliato e i bordi taglianti.
6.  Questo strumento viene sempre eseguito in modalità continua: facoltativamente continuare a tagliare i bordi.
7.  Per terminare, fare clic in un\'area vuota nella [3D View](3D_view/it.md), fare clic con il pulsante destro del mouse o premere **Esc** oppure avviare un altro strumento di creazione di geometrie o vincoli.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher Trimming/it
