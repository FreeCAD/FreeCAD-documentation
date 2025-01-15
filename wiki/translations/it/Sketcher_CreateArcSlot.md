---
 GuiCommand:
   Name: Sketcher CreateArcSlot
   Name/it: Sketcher Crea asola ad arco
   MenuLocation: Schizzo , Geometrie Sketcher , Crea asola ad arco
   Workbenches: Sketcher_Workbench/it
   Shortcut: **G** **S** **2**
   Version: 1.0
   SeeAlso: Sketcher_CreateSlot/it
---

# Sketcher CreateArcSlot/it



## Descrizione

Lo strumento <img alt="" src=images/Sketcher_CreateArcSlot.svg  style="width:24px;"> [Sketcher Crea asola ad arco](Sketcher_CreateArcSlot/it.md) crea un\'asola ad arco, una polilinea chiusa costituita da due archi concentrici paralleli chiusi da due semicerchi o due rette radiali.

<img alt="" src=images/Sketcher_CreateArcSlot_Example.png  style="width:300px;"> 
*Asola ad arco con estremità ad arco (a sinistra) ed estremità piatte (a destra)*



## Utilizzo

Vedere anche: [Aiuti per il disegno](Sketcher_Workbench/it#Drawing_aids.md).

Pos-OVP = [On-View-Parameters](Sketcher_Preferences/it#Generale.md) Posizionali.
Dim-OVP = On-View-Parameters Dimensionali.

1.  Esistono diversi modi per richiamare lo strumento:
    -   Premere il pulsante **<img src="images/Sketcher_CreateArcSlot.svg" width=16px> [Crea asola ad arco](Sketcher_CreateArcSlot/it.md)**.
    -   Selezionare l\'opzione **Schizzo → Geometrie Sketcher → <img src="images/Sketcher_CreateArcSlot.svg" width=16px> Crea asola ad  arco** dal menu.
    -   La scorciatoia da tastiera: **G** poi **S**, poi **2**.
2.  Il cursore si trasforma in una croce con l\'icona dello strumento.
3.  La sezione **Parametri Asola ad arco** è stata aggiunta nella parte superiore della finestra [Dialogo Sketcher](Sketcher_Dialog.md).
4.  Facoltativamente, premere il tasto **M** o selezionare dall\'elenco a discesa nella sezione dei parametri per modificare la modalità dello strumento:
    -   <img alt="" src=images/Sketcher_CreateArcSlot.svg  style="width:16px;"> **Terminazione ad arco**:
        1.  Scegliere il centro dell\'asola ad arco. Oppure con Pos-OVP: inserire le sue coordinate X e/o Y.
        2.  Scegliere il centro del primo semicerchio, questo definisce anche il raggio della linea centrale (virtuale) dell\'asola. Oppure con Dim-OVP: inserire il raggio e/o l\'angolo iniziale dell\'asola. L\'angolo è relativo all\'asse X dello schizzo. Non viene creato alcun vincolo per questo angolo.
        3.  Scegliere il centro del secondo semicerchio. Oppure con Dim-OVP: inserire l\'angolo di apertura dell\'arco della linea centrale.
        4.  Scegliere un punto per definire il raggio dei semicerchi. Oppure con Dim-OVP: inserire questo raggio.
    -   <img alt="" src=images/Sketcher_CreateRectangleSlot.svg  style="width:16px;"> **Terminazione piatta**:
        1.  Scegliere il centro dellìasola ad arco. Oppure con Pos-OVP: inserire le sue coordinate X e/o Y.
        2.  Scegliere il punto iniziale del primo arco, questo ne definisce anche il raggio. Oppure con Dim-OVP: inserire il raggio e/o l\'angolo iniziale del primo arco. L\'angolo è relativo all\'asse X dello schizzo. Non viene creato alcun vincolo per questo angolo.
        3.  Selezionare il punto finale del primo arco. Oppure con Dim-OVP: inserire l\'angolo di apertura dell\'arco.
        4.  Scegliere un punto per definire la larghezza dell\'asola. Oppure con Dim-OVP: inserire questa larghezza.
5.  Viene creata l\'asola e vengono aggiunti i vincoli basati su Pos-OVP e Dim-OVP applicabili.
6.  Se lo strumento viene eseguito in [modalità continua](Sketcher_Workbench#Continue_modes/it.md):
    1.  Facoltativamente, continuare a creare asole.
    2.  Per terminare, fare clic con il pulsante destro del mouse o premere **Esc** oppure avviare un altro strumento di creazione di geometrie o vincoli.



## Note

-   I punti selezionati per definire il raggio dei semicerchi o l\'offset degli archi interni ed esterni non devono toccare la geometria, la distanza dal cursore al centro dell\'asola in realtà controlla il valore.
-   Nella modalità **Terminazione ad arco** il primo raggio si applica ad un arco centrale virtuale, mentre si applica a uno degli archi di contorno nella modalità **Terminazione piatta**.
-   Se il valore della larghezza inserito nella modalità **Terminazione piatta** è positivo, l\'arco vincolato diventa l\'arco interno, per un valore negativo sarà l\'arco esterno.



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CreateArcSlot/it
