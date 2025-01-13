---
 GuiCommand:
   Name: Sketcher CreateSlot
   Name/it: Sketcher Crea asola
   MenuLocation: Schizzo , Geometrie Sketcher , Crea asola
   Workbenches: Sketcher_Workbench/it
   Shortcut: **G** **S**
   SeeAlso: Sketcher_CreateArcSlot/it
---

# Sketcher CreateSlot/it



## Descrizione

Lo strumento <img alt="" src=images/Sketcher_CreateSlot.svg  style="width:24px;"> [Sketcher Crea asola](Sketcher_CreateSlot/it.md) crea un\'asola, una polilinea chiusa composta da due semicerchi collegati da due linee rette parallele.

![](images/SketcherCreateSlotExample.png‎ )



## Utilizzo

Vedere anche: [Aiuti per il disegno](Sketcher_Workbench/it#Drawing_aids.md).

Pos-OVP = [On-View-Parameters](Sketcher_Preferences/it#Generale.md) Posizionali. {{Version/it|1.0}}
Dim-OVP = On-View-Parameters Dimensionali. {{Version/it|1.0}}

1.  Esistono diversi modi per richiamare lo strumento:
    -   Premere il pulsante **<img src="images/Sketcher_CreateSlot.svg" width=16px> [Crea asola](Sketcher_CreateSlot/it.md)**.
    -   Selezionare l\'opzione **Schizzo → Geometrie Sketcher → <img src="images/Sketcher_CreateSlot.svg" width=16px> Crea asola** dal menu.
    -   La scorciatoia da tastiera: **G** quindi **S**.
2.  Il cursore si trasforma in una croce con l\'icona dello strumento.
3.  Scegliere il centro del primo semicerchio. Oppure con Pos-OVP: inserire le sue coordinate X e/o Y.
4.  Scegliere il centro del secondo semicerchio. Oppure con Dim-OVP: inserire la distanza tra i centri e/o l\'angolo dell\'asola. L\'angolo è relativo all\'asse X dello schizzo.
5.  Scegliere un punto per definire il raggio dell\'asola. Oppure con Dim-OVP: inserire questo raggio.
6.  Viene creata l\'asola e vengono aggiunti i vincoli basati su Pos-OVP e Dim-OVP applicabili.
7.  Se lo strumento viene eseguito in [modalità continua](Sketcher_Workbench#Continue_modes/it.md):
    1.  Facoltativamente, continuare a creare asole.
    2.  Per terminare, fare clic con il pulsante destro del mouse o premere **Esc** oppure avviare un altro strumento di creazione di geometrie o vincoli.



## Note

-    {{VersionMinus/it|0.21}}({{Version/it|0.20}}): Tenendo premuto **Ctrl** quando si seleziona il secondo centro vincolerà l\'asola ad essere disegnata orizzontalmente o verticalmente.

-    {{Version/it|1.0}}: [Aggancio angolare](Sketcher_Snap/it.md) può essere utilizzato per controllare l\'angolo dell\'asola.

-    {{Version/it|0.20}}: un\'asola può anche essere vincolata orizzontalmente o verticalmente se l\'opzione [Vincoli automatici](Sketcher_Workbench/it#Auto_constraints.md) è abilitata.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CreateSlot/it
