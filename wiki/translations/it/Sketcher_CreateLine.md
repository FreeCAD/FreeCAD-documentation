---
 GuiCommand:
   Name: Sketcher CreateLine
   Name/it: Sketcher Crea linea
   MenuLocation: Schizzo , Geometrie Sketcher , Crea linea
   Workbenches: Sketcher Workbench/it
   Shortcut: **G** **L**
   SeeAlso: Sketcher_CreatePolyline/it
---

# Sketcher CreateLine/it



## Descrizione

Lo strumento <img alt="" src=images/Sketcher_CreateLine.svg  style="width:24px;"> [Sketcher Crea linea](Sketcher_CreateLine/it.md) crea una linea. {{Version/it|1.0}}: Se [On-View-Parameters](Sketcher_Preferences/it#Generale.md) sono abilitati, lo strumento ha tre modalità.

![](images/Sketcher_LineExample1.png‎ )



## Utilizzo

Vedere anche: [Aiuti per il disegno](Sketcher_Workbench/it#Drawing_aids.md).

Pos-OVP = [On-View-Parameters](Sketcher_Preferences/it#Generale.md) Posizionali. {{Version/it|1.0}}
Dim-OVP = On-View-Parameters Dimensionali. {{Version/it|1.0}}

1.  Esistono diversi modi per richiamare lo strumento:
    -   Premere il pulsante **<img src="images/Sketcher_CreateLine.svg" width=16px> [Crea linea](Sketcher_CreateLine/it.md)**.
    -   Selezionare l\'opzione **Schizzo → Geometrie Sketcher → <img src="images/Sketcher_CreateLine.svg" width=16px> Crea linea** dal menu.
    -   Usare la scorciatoia da tastiera: **G** quindi **L**.
2.  Il cursore si trasforma in una croce con l\'icona della modalità strumento corrente.
3.  Se [On-View-Parameters](Sketcher_Preferences/it#Generale.md) sono abilitati, la sezione **Line parametri** ({{Version/it|1.0}}) viene aggiunta nella parte superiore della finestra [Dialogo Sketcher](Sketcher_Dialog/it.md).
4.  Facoltativamente, premere il tasto **M** o selezionare dall\'elenco a discesa nella sezione dei parametri per modificare la modalità dello strumento:
    -   <img alt="" src=images/Sketcher_CreateLineAngleLength.svg  style="width:16px;"> **Punto, lunghezza, angolo**: {{Version/it|1.0}}
        1.  Scegliere il punto iniziale della linea. Oppure con Pos-OVP: inserire le sue coordinate X e/o Y.
        2.  Scegliere il punto finale della linea. Oppure con Dim-OVP: inserisci la lunghezza e/o l\'angolo della linea. L\'angolo è relativo all\'asse X dello schizzo.
    -   <img alt="" src=images/Sketcher_CreateLineLengthWidth.svg  style="width:16px;"> **Punto, larghezza, altezza**: {{Version/it|1.0}}
        1.  Scegliere il punto iniziale della linea. Oppure con Pos-OVP: inserire le sue coordinate X e/o Y.
        2.  Scegliere il punto finale della linea. Oppure con Dim-OVP: inserisci la sua distanza X e/o Y dal punto iniziale.
    -   <img alt="" src=images/Sketcher_CreateLine.svg  style="width:16px;"> **2 punti**:
        1.  Scegliere il punto iniziale della linea. Oppure con Pos-OVP: inserire le sue coordinate X e/o Y.
        2.  Scegliere il punto finale della linea. Oppure con Pos-OVP: inserire le sue coordinate X e/o Y.
5.  La linea viene creata e vengono aggiunti i vincoli basati su Pos-OVP e Dim-OVP applicabili.
6.  Se lo strumento viene eseguito in [modalità continua](Sketcher_Workbench/it#Continue_modes.md):
    1.  Facoltativamente, continuare a creare linee.
    2.  Per terminare, fare clic con il pulsante destro del mouse o premere **Esc** oppure avviare un altro strumento di creazione di geometrie o vincoli.





{{Sketcher Tools navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CreateLine/it
