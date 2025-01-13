---
 GuiCommand:
   Name: Sketcher Split
   Name/it: Sketcher Dividi
   MenuLocation: Schizzo , Strumenti Sketcher , Dividi bordo
   Workbenches: Sketcher_Workbench/it
   Shortcut: **G** **Z**
   Version: 0.20
   SeeAlso: Sketcher_Trimming/it
---

# Sketcher Split/it



## Descrizione

Lo strumento <img alt="" src=images/Sketcher_Split.svg  style="width:24px;"> [Sketcher Dividi](Sketcher_Split/it.md) divide un bordo. Se il bordo è una curva chiusa (cioè un cerchio, un\'ellisse o una B-spline periodica) viene convertito in una curva aperta (rispettivamente un arco, un arco di ellisse o una B-spline non periodica).



## Utilizzo

Vedere anche: [Aiuti per il disegno](Sketcher_Workbench/it#Drawing_aids.md).

1.  Esistono diversi modi per richiamare lo strumento:
    -   Premere il pulsante **<img src="images/Sketcher_Split.svg" width=16px> [Dividi bordo](Sketcher_Split/it.md)**.
    -   Selezionare l\'opzione **Schizzo → Strumenti Sketcher → <img src="images/Sketcher_Split.svg" width=16px> Dividi bordo** dal menu.
    -   Usare la scorciatoia da tastiera: **G** quindi **Z**.
2.  Se c\'è una selezione precedente, viene cancellata. Lo strumento non accetta una preselezione.
3.  Il cursore si trasforma in una croce con l\'icona dello strumento.
4.  Fare clic su un bordo nel punto in cui deve essere diviso.
5.  Se il bordo originale è una linea o una curva aperta, vengono creati due nuovi bordi collegati da un [Vincolo coincidente](Sketcher_ConstrainCoincident/it.md). Per le curve chiuse viene creata una nuova curva aperta, il nuovo punto quindi non riceve un vincolo Coincidente. I vincoli applicabili esistenti vengono trasferiti ai nuovi bordi. Vedi [Note](#Note.md).
6.  Questo strumento viene sempre eseguito in modalità continua: facoltativamente mantienere la divisione dei bordi.
7.  Per terminare, fare clic in un\'area vuota nella [VIsta 3D](3D_view/it.md), fare clic con il pulsante destro del mouse o premere **Esc** oppure avviare un altro strumento di creazione di geometrie o vincoli.



## Note

-   Un vincolo [Coincidente](Sketcher_ConstrainCoincident/it.md) viene applicato ai punti centrali dei nuovi archi.
-   I vincoli [Raggio](Sketcher_ConstrainRadius/it.md) e [Diametro](Sketcher_ConstrainDiameter/it.md) vengono copiati su nuovi archi (con conseguente ridondanza).
-   I vincoli coincidenti e i vincoli [Punto sull\'oggetto](Sketcher_ConstrainPointOnObject/it.md) vengono trasferiti al nuovo bordo più vicino.
-   I vincoli [Orizzontale](Sketcher_ConstrainHorizontal/it.md) e [Verticale](Sketcher_ConstrainVertical/it.md) tra i punti vengono trasferiti al nuovo bordo più vicino.
-   I vincoli orizzontali e verticali associati alle linee vengono copiati nei nuovi segmenti di linea.
-   I vincoli [Parallelo](Sketcher_ConstrainParallel/it.md) e [Perpendicolare](Sketcher_ConstrainPerpendicular/it.md) vengono copiati su nuovi segmenti di linea, per i nuovi archi vengono copiati solo su quello più vicino.
-   I vincoli [Distanza orizzontale](Sketcher_ConstrainDistanceX/it.md), [Distanza verticale](Sketcher_ConstrainDistanceY/it.md) e [Distanza](Sketcher_ConstrainDistance/it.md) vengono trasferiti al nuovo bordo più vicino.
-   I vincoli [Angolo](Sketcher_ConstrainAngle/it.md), [Simmetrico](Sketcher_ConstrainSymmetric/it.md) e [Blocca](Sketcher_ConstrainBlock/it.md) attualmente non vengono trasferiti.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher Split/it
