---
 GuiCommand:
   Name: Sketcher CreateFillet
   Name/it: Sketcher Crea raccordo
   MenuLocation: Schizzo , Strumenti Sketcher , Crea raccordo
   Workbenches: Sketcher_Workbench/it
   Shortcut: **G** **F** **F**
   SeeAlso: 
---

# Sketcher CreateFillet/it



## Descrizione

Lo strumento <img alt="" src=images/Sketcher_CreateFillet.svg  style="width:24px;"> [Sketcher Crea raccordo](Sketcher_CreateFillet/it.md) crea un raccordo tra due bordi non paralleli. {{Version/it|1.0}}: Lo strumento può anche creare uno smusso.


{{Version/it|1.0}}

: Se due bordi dritti collegati da un [vincolo coincidente](Sketcher_ConstrainCoincident/it.md) vengono raccordati o smussati, il punto d\'angolo può essere opzionalmente conservato. Lo strumento aggiunge quindi un [oggetto Punto](Sketcher_CreatePoint/it.md) che ha un [vincolo Punto su oggetto](Sketcher_ConstrainPointOnObject/it.md) con entrambi i bordi. I vincoli collegati al punto d\'angolo vengono trasferiti al nuovo oggetto punto.

![](images/SketcherCreateFilletExample.png‎ )



## Utilizzo

Vedere anche: [Aiuti per il disegno](Sketcher_Workbench/it#Drawing_aids.md).

1.  Esistono diversi modi per richiamare lo strumento:
    -   Premere il pulsante **<img src="images/Sketcher_CreateFillet.svg" width=16px> [Crea raccordo](Sketcher_CreateFillet/it.md)**.
    -   Selezionare l\'opzione **Sketcher → Strumenti Sketcher → <img src="images/Sketcher_CreateFillet.svg" width=16px> Crea raccordo** dal menu.
    -   Fare clic con il pulsante destro del mouse nella [Vista 3D](3D_view/it.md) e selezionare l\'opzione **<img src="images/Sketcher_CreateFillet.svg" width=16px> Crea raccordo** dal menu contestuale.
    -   Usare la scorciatoia da tastiera: **G** quindi **F**, quindi **F**.
2.  Se è presente una selezione precedente, questa viene cancellata. Lo strumento non accetta una preselezione.
3.  Il cursore si trasforma in una croce con l\'icona della modalità strumento corrente.
4.  La sezione **Parametri raccordo/smusso** ({{Version/it|1.0}}) è aggiunta nella parte superiore della finestra [Dialogo Sketcher](Sketcher_Dialog/it.md).
5.  Facoltativamente, premere il tasto **U** o deselezionare la casella di controllo **Mantieni angolo** per disabilitare tale opzione. {{Version/it|1.0}}
6.  Facoltativamente, premere il tasto **M** o selezionare dall\'elenco a discesa nella sezione parametri per modificare la modalità strumento:
    -   <img alt="" src=images/Sketcher_CreateFillet.svg  style="width:16px;"> 
**Raccordo**
    -   <img alt="" src=images/Sketcher_CreateChamfer.svg  style="width:16px;"> 
**Smusso**
7.  Eseguire una delle seguenti operazioni:
    -   Selezionare un punto con un [vincolo coincidente](Sketcher_ConstrainCoincident/it.md) che collega due bordi dritti non paralleli.
    -   Selezionare due bordi non paralleli. Entrambi i bordi possono essere una [linea](Sketcher_CreateLine/it.md), un [arco](Sketcher_CreateArc/it.md), un [arco di ellisse](Sketcher_CreateArcOfEllipse/it.md), un [arco di iperbole](Sketcher_CreateArcOfHyperbola/it.md) o un [arco di parabola](Sketcher_CreateArcOfParabola/it.md). Le [B-spline](Sketcher_Workbench/it#Sketcher_CompCreateBSpline.md) non sono attualmente supportate.
8.  Viene creato il raccordo o lo smusso, incluso un oggetto punto in caso di angolo conservato. Per uno smusso viene creato anche un arco di geometria di costruzione.
9.  Questo strumento funziona sempre in modalità continua: facoltativamente, continuare a selezionare punti e/o bordi.
10. Per terminare, fare clic con il pulsante destro del mouse o premere **Esc**, oppure avviare un altro strumento di creazione di geometrie o vincoli.



## Note

-   L\'arco della geometria di costruzione di uno smusso non è visibile all\'esterno dello schizzo. Non può essere eliminato senza interrompere la geometria dello smusso.
-   Alcune curve ([coniche](Sketcher_Workbench/it#Sketcher_CompCreateConic.md)) potrebbero dover essere [rifilate](Sketcher_Trimming/it.md) prima di poter essere raccordate.
-   Il raggio del raccordo dipende dal metodo di selezione. Se viene selezionato un [vincolo coincidente](Sketcher_ConstrainCoincident/it.md) che collega due bordi dritti, il raggio del raccordo viene derivato dalla lunghezza del bordo più corto. Se vengono selezionati due bordi, il raggio è la distanza dal primo punto cliccato all\'intersezione (estesa) dei bordi.



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CreateFillet/it
