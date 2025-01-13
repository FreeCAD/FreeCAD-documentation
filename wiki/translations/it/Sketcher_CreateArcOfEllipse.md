---
 GuiCommand:
   Name: Sketcher CreateArcOfEllipse
   Name/it: Sketcher Crea arco di ellisse
   MenuLocation: Schizzo , Geometrie Sketcher , Crea arco di ellisse
   Workbenches: Sketcher Workbench/it
   Shortcut: **G** **E** **A**
   Version: 0.15
   SeeAlso: Sketcher_CreateEllipseByCenter/it
---

# Sketcher CreateArcOfEllipse/it



## Descrizione

Lo strumento <img alt="" src=images/Sketcher_CreateArcOfEllipse.svg  style="width:24px;"> [Sketcher Crea arco di ellisse](Sketcher_CreateArcOfEllipse/it.md) crea un arco di ellisse.

![](images/Sketcher_CreateArcOfEllipse_Example.png ) 
*Arco di ellisse (bianco) con geometria interna (giallo scuro)*



## Utilizzo

Vedere anche: [Aiuti per il disegno](Sketcher_Workbench/it#Drawing_aids.md).

1.  Esistono diversi modi per richiamare lo strumento:
    -   Premere il pulsante **<img src="images/Sketcher_CreateArcOfEllipse.svg" width=16px> [Arco di ellisse per centro, raggio, punti finali](Sketcher_CreateArcOfEllipse/it.md)**.
    -   Selezionare l\'opzione **Sketcher → Geometrie Sketcher → <img src="images/Sketcher_CreateArcOfEllipse.svg" width=16px> Crea arco di ellisse** dal menu.
    -   Usare la scorciatoia da tastiera: **G** quindi **E**, quindi **A**.
2.  Il cursore si trasforma in una croce con l\'icona dello strumento.
3.  Scegliere il centro dell\'arco.
4.  Scegliere un punto finale di uno degli assi dell\'arco, questo definisce anche uno dei suoi raggi.
5.  Scegliere il punto iniziale dell\'arco, questo definisce anche l\'altro raggio dell\'arco.
6.  Selezionare il punto finale dell\'arco.
7.  Viene creato l\'arco di ellisse, incluso un insieme di geometrie interne (asse maggiore, asse minore e due fuochi).
8.  Se lo strumento viene eseguito in [modalità continua](Sketcher_Workbench/it#Continue_modes.md):
    1.  Facoltativamente continuare a creare archi.
    2.  Per terminare, fare clic con il pulsante destro del mouse o premere **Esc** oppure avviare un altro strumento di creazione di geometrie o vincoli.



## Note

-   Gli elementi della geometria interna possono essere cancellati. Possono essere ricreati in qualsiasi momento con [Sketcher Mostra/nascondi la geometria interna](Sketcher_RestoreInternalAlignmentGeometry/it.md).
-   Una volta creati, gli assi maggiore e minore di un arco di ellisse sono rigorosi e non possono essere scambiati ridimensionando. Questa è una conseguenza della parametrizzazione del risolutore e dello stesso rigido comportamento di [OpenCASCADE](OpenCASCADE/it.md). Un arco di ellisse deve essere ruotato per scambiare i suoi assi.





{{Sketcher Tools navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CreateArcOfEllipse/it
