---
 GuiCommand:
   Name: SketcherCreateCircle
   Name/it: Sketcher Crea cerchio dal centro
   MenuLocation: Schizzo , Geometrie Sketcher , Crea cerchio dal centro
   Workbenches: Sketcher_Workbench/it
   Shortcut: **G** **C**
   SeeAlso: Sketcher_CreateArc/it
---

# Sketcher CreateCircle/it



## Descrizione

Lo strumento <img alt="" src=images/Sketcher_CreateCircle.svg  style="width:24px;"> [Sketcher Crea cerchio](Sketcher_CreateCircle/it.md) crea un cerchio in base al suo centro e un punto lungo la circonferenza. {{Version/it|1.0}}: o facoltativamente da tre punti lungo la circonferenza.

![](images/Sketcher_CircleExample1.png‎ )



## Utilizzo

Vedere anche: [Aiuti per il disegno](Sketcher_Workbench/it#Drawing_aids.md).

Pos-OVP = [On-View-Parameters](Sketcher_Preferences/it#Generale.md) Posizionali. {{Version/it|1.0}}
Dim-OVP = On-View-Parameters Dimensionali. {{Version/it|1.0}}

1.  Esistono diversi modi per richiamare lo strumento:
    -   Premere il pulsante **<img src="images/Sketcher_CreateCircle.svg" width=16px> [Crea cerchio dal centro](Sketcher_CreateCircle/it.md)**.
    -   Selezionare l\'opzione **Schizzo → Geometrie Sketcher → <img src="images/Sketcher_CreateCircle.svg" width=16px> Crea cerchio dal centro** dal menu.
    -   Fare clic con il pulsante destro del mouse nella [Vista 3D](3D_view/it.md) e selezionare l\'opzione **<img src="images/Sketcher_CreateCircle.svg" width=16px> Crea cerchio dal centro** dal menu contestuale.
    -   Usare la scorciatoia da tastiera: **G** quindi **C**.
2.  Il cursore si trasforma in una croce con l\'icona della modalità strumento corrente.
3.  La sezione **Parametri cerchio** ({{Version/it|1.0}}) è stata aggiunta nella parte superiore della finestra [Dialogo Sketcher](Sketcher_Dialog/it.md).
4.  Facoltativamente, premere il tasto **M** o selezionare dall\'elenco a discesa nella sezione dei parametri per modificare la modalità dello strumento:
    -   <img alt="" src=images/Sketcher_CreateCircle.svg  style="width:16px;"> **Centro**:
        1.  Scegliere il centro del cerchio. Oppure con Pos-OVP: inserire le sue coordinate X e/o Y.
        2.  Scegliere un punto per definire il raggio del cerchio. Oppure con Dim-OVP: inserire questo raggio.
    -   <img alt="" src=images/Sketcher_Create3PointCircle.svg  style="width:16px;"> **3 punti**: {{Version/it|1.0}}
        1.  Scegliere tre punti per definire il cerchio. Oppure con Pos-OVP: inserire le loro coordinate X e/o Y. Per questi punti non viene creato alcun vincolo.
5.  Il cerchio viene creato e vengono aggiunti i vincoli basati su Pos-OVP e Dim-OVP applicabili.
6.  Se lo strumento viene eseguito in [modalità continua](Sketcher_Workbench/it#Continue_modes.md):
    1.  Facoltativamente, continuare a creare cerchi.
    2.  Per terminare, fare clic con il pulsante destro del mouse o premere **Esc**, oppure avviare un altro strumento di creazione di geometrie o vincoli.



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CreateCircle/it
