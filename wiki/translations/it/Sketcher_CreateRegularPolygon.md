---
 GuiCommand:
   Name: Sketcher CreateRegularPolygon
   Name/it: Sketcher Crea poligono regolare
   MenuLocation: Schizzo , Geometrie Sketcher , Crea poligono regolare
   Workbenches: Sketcher_Workbench/it
   Shortcut: **G** **P** **R**
---

# Sketcher CreateRegularPolygon/it



## Descrizione

Lo strumento <img alt="" src=images/Sketcher_CreateRegularPolygon.svg  style="width:24px;"> [Sketcher Crea poligono regolare](Sketcher_CreateRegularPolygon/it.md) crea un poligono regolare.



## Utilizzo

Vedere anche: [Aiuti per il disegno](Sketcher_Workbench/it#Drawing_aids.md).

Pos-OVP = [On-View-Parameters](Sketcher_Preferences/it#Generale.md) Posizionali. {{Version/it|1.0}}
Dim-OVP = On-View-Parameters Dimensionali. {{Version/it|1.0}}

1.  Esistono diversi modi per richiamare lo strumento:
    -   Premere il pulsante **<img src="images/Sketcher_CreateRegularPolygon.svg" width=16px> [Poligono regolare](Sketcher_CreateRegularPolygon/it.md)**.
    -   Selezionare l\'opzione **Schizzo → Geometrie Sketcher → <img src="images/Sketcher_CreateRegularPolygon.svg" width=16px> Crea poligono regolare** dal menu.
    -   Usare la scorciatoia da tastiera: **G** quindi **P**, quindi **R**.
2.  Inserire il **Numero di lati** nella finestra di dialogo che si apre.
3.  Il cursore si trasforma in una croce con l\'icona dello strumento.
4.  La sezione **Parametri poligono** ({{Version/it|1.0}}) è stata aggiunta nella parte superiore della finestra [Dialogo Sketcher](Sketcher_Dialog/it.md).
5.  Facoltativamente, modificare il numero di **Lati** (questo può essere fatto anche dopo aver selezionato il centro):
    -   Inserire un numero maggiore di due.
    -   Premere il tasto **U** per aumentare il numero.
    -   Premere il tasto **J** per diminuire il numero.
6.  Scegliere il centro del poligono. Oppure con Pos-OVP: inserire le sue coordinate X e/o Y.
7.  Scegliere il primo punto del poligono, questo definisce anche il raggio del cerchio circoscritto. Oppure con Dim-OVP: inserire il raggio del cerchio e/o l\'angolo del primo punto. L\'angolo è relativo all\'asse X dello schizzo. Non viene creato alcun vincolo per questo angolo.
8.  Viene creato il poligono, incluso un cerchio di geometria di costruzione circoscritta, e vengono aggiunti i vincoli basati su Pos-OVP e Dim-OVP applicabili.
9.  Se lo strumento viene eseguito in [modalità continua](Sketcher_Workbench#Continue_modes/it.md):
    1.  Facoltativamente, continuare a creare poligoni.
    2.  Per terminare, fare clic con il pulsante destro del mouse o premere **Esc** oppure avviare un altro strumento di creazione di geometrie o vincoli.



## Note

-   Il cerchio della geometria di costruzione non è visibile all\'esterno dello schizzo. Non può essere eliminato senza interrompere la geometria del poligono.





{{Sketcher Tools navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CreateRegularPolygon/it
