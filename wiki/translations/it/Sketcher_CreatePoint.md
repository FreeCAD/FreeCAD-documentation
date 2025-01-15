---
 GuiCommand:
   Name: Sketcher CreatePoint
   Name/it: Sketcher Crea punto
   MenuLocation: Schizzo , Geometrie Sketcher , Crea punto
   Workbenches: Sketcher_Workbench/it
   Shortcut: **G** **Y**
---

# Sketcher CreatePoint/it



## Descrizione

Lo strumento <img alt="" src=images/Sketcher_CreatePoint.svg  style="width:24px;"> [Sketcher Crea punto](Sketcher_CreatePoint/it.md) crea un punto.



## Utilizzo

Vedere anche: [Aiuti per il disegno](Sketcher_Workbench/it#Drawing_aids.md).

Pos-OVP = [On-View-Parameters](Sketcher_Preferences/it#Generale.md) Posizionali . {{Version/it|1.0}}

1.  Esistono diversi modi per richiamare lo strumento:
    -   Premere il pulsante **<img src="images/Sketcher_CreatePoint.svg" width=16px> [Crea punto](Sketcher_CreatePoint/it.md)**.
    -   Selezionare l\'opzione **Schizzo → Geometrie Sketcher → <img src="images/Sketcher_CreatePoint.svg" width=16px> Crea punto** dal menu.
    -   Fare clic con il pulsante destro del mouse nella [Vista 3D](3D_view/it.md) e selezionare l\'opzione **<img src="images/Sketcher_CreatePoint.svg" width=16px> Crea punto** dal menu contestuale.
    -   Usare la scorciatoia da tastiera: **G** quindi **Y**.
2.  Il cursore si trasforma in una croce con l\'icona dello strumento.
3.  Scegliere un punto. Oppure con Pos-OVP: inserire le sue coordinate X e/o Y.
4.  Il punto viene creato e vengono aggiunti i vincoli basati su Pos-OVP applicabili.
5.  Se lo strumento viene eseguito in [modalità continua](Sketcher_Workbench/it#Continue_modes.md):
    1.  Facoltativamente, continuare a creare punti.
    2.  Per terminare, fare clic con il pulsante destro del mouse o premere **Esc** oppure avviare un altro strumento di creazione di geometrie o vincoli.



## Note

-    {{VersionMinus/it|0.21}}: I punti vengono sempre creati come geometria di costruzione. Facoltativamente, modificarli in geometria normale con [Sketcher Geometria di costruzione](Sketcher_ToggleConstruction/it.md) per renderli visibili al di fuori della modalità di modifica dello schizzo.



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CreatePoint/it
