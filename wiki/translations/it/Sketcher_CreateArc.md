---
 GuiCommand:
   Name: Sketcher CreateArc
   Name/it: Sketcher Crea arco dal centro
   MenuLocation: Sketch , Geometrie , Crea arco da centro
   Workbenches: Sketcher_Workbench/it
   Shortcut: **G** **A**
   SeeAlso: Sketcher_CreateCircle/it
---

# Sketcher CreateArc/it



## Descrizione

Lo strumento <img alt="" src=images/Sketcher_CreateArc.svg  style="width:24px;"> [Sketcher Crea arco dal centro](Sketcher_CreateArc/it.md) crea un arco tramite il suo centro e i suoi punti finali. {{Version/it|1.0}}: o facoltativamente dai suoi punti finali e da un punto lungo l\'arco.

<img alt="" src=images/Sketcher_ArcExample3.png  style="width:400px;"> 
*Arco creato in modalità Centro con vincoli applicati automaticamente definiti inserendo tutti i parametri On-View*



## Utilizzo

Vedere anche: [Aiuti per il disegno](Sketcher_Workbench/it#Drawing_aids.md).

Pos-OVP = [On-View-Parameters](Sketcher_Preferences/it#Generale.md) Posizionali. {{Version/it|1.0}}
Dim-OVP = On-View-Parameters Dimensionali. {{Version/it|1.0}}

1.  Esistono diversi modi per richiamare lo strumento:
    -   Premere il pulsante **<img src="images/Sketcher_CreateArc.svg" width=16px> [Crea arco dal centro](Sketcher_CreateArc/it.md)**.
    -   Selezionare l\'opzione **Sketcher → Geometrie Sketcher → <img src="images/Sketcher_CreateArc.svg" width=16px> Crea arco dal centro** dal menu.
    -   Fare clic con il pulsante destro del mouse nella [Vista 3D](3D_view/it.md) e selezionare l\'opzione **<img src="images/Sketcher_CreateArc.svg" width=16px> Crea arco dal centro** dal menu contestuale.
    -   Usare la scorciatoia da tastiera: **G** quindi **A**.
2.  Il cursore si trasforma in una croce con l\'icona della modalità strumento corrente.
3.  La sezione **Parametri dell\'arco** ({{Version/it|1.0}}) è stata aggiunta nella parte superiore della finestra [Dialogo Sketcher](Sketcher_Dialog/it.md).
4.  Facoltativamente, premere il tasto **M** o selezionare dall\'elenco a discesa nella sezione dei parametri per modificare la modalità dello strumento:
    -   <img alt="" src=images/Sketcher_CreateArc.svg  style="width:16px;"> **Centro**:
        1.  Scegliere il centro dell\'arco. Oppure con Pos-OVP: inserire le sue coordinate X e/o Y.
        2.  Scegliere il punto iniziale dell\'arco, questo definisce anche il raggio. Oppure con Dim-OVP: inserire il raggio e/o l\'angolo iniziale dell\'arco. L\'angolo è relativo all\'asse X dello schizzo. Non viene creato alcun vincolo per questo angolo.
        3.  Selezionare il punto finale dell\'arco. Oppure con Dim-OVP: inserire l\'angolo di apertura dell\'arco.
    -   <img alt="" src=images/Sketcher_Create3PointArc.svg  style="width:16px;"> **3 punti del bordo**: {{Version/it|1.0}}
        1.  Selezionare i punti iniziale e finale dell\'arco. Oppure con Pos-OVP: inserire le loro coordinate X e/o Y.
        2.  Scegliere un altro punto per definire il raggio. Oppure con Pos-OVP: inserire le sue coordinate X e/o Y. Nessun vincolo viene creato per questo punto.
5.  L\'arco viene creato e vengono aggiunti i vincoli basati su Pos-OVP e Dim-OVP applicabili.
6.  Se lo strumento viene eseguito in [modalità continua](Sketcher_Workbench/it#Continue_modes.md):
    1.  Facoltativamente continuare a creare archi.
    2.  Per terminare, fare clic con il pulsante destro del mouse o premere **Esc** oppure avviare un altro strumento di creazione di geometrie o vincoli.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CreateArc/it
