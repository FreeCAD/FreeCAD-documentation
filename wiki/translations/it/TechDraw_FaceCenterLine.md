---
 GuiCommand:
   Name: TechDraw FaceCenterLine
   Name/it: TechDraw Linea centrale alla faccia
   MenuLocation: TechDraw , Aggiungi linee , Linea centrale alla faccia
   Version: 0.19
   Workbenches: TechDraw_Workbench/it
   SeeAlso: TechDraw_2LineCenterLine/it, TechDraw_2PointCenterLine/it
---

# TechDraw FaceCenterLine/it



## Descrizione

Lo strumento **TechDraw Linea centrale alla faccia** aggiunge una linea centrale alle facce selezionate.

<img alt="" src=images/TechDraw_FaceCenterLine_Sample.png  style="width:400px;"> 
*Linea centrale aggiunta alla faccia*



## Creazione

1.  Selezionare una o più facce in una Vista.
2.  Esistono diversi modi per richiamare lo strumento:
    -   Premere il pulsante **<img src="images/TechDraw_FaceCenterLine.svg" width=16px> [Aggiungi Linea centrale alle facce](TechDraw_FaceCenterLine/it.md)**.
    -   Selezionare l\'opzione **TechDraw → Aggiungi linee → <img src="images/TechDraw_FaceCenterLine.svg" width=16px> Aggiungi Linea centrale alle facce** dal menu.
3.  Si apre un pannello delle azioni. Vedere [Opzioni](#Opzioni.md) per ulteriori informazioni.
4.  Premere il pulsante **OK** per confermare.
5.  Una linea centrale viene aggiunta al punto medio del riquadro di delimitazione delle facce selezionate.



## Modifica

Uno qualsiasi degli strumenti della linea centrale (<img alt="" src=images/TechDraw_FaceCenterLine.svg  style="width:16px;"> TechDraw Linea centrale faccia, <img alt="" src=images/TechDraw_2LineCenterLine.svg  style="width:16px;"> [TechDraw Linea centrale a 2 linee](TechDraw_2LineCenterLine/it.md) e <img alt="" src=images/TechDraw_2PointCenterLine.svg  style="width:16px;"> [TechDraw Linea centrale a 2 punti](TechDraw_2PointCenterLine/it.md)) può essere utilizzato per modificare qualsiasi linea centrale.

1.  Selezionare una linea centrale.
2.  Invocare uno strumento della linea centrale.
3.  Si apre un pannello delle azioni. Vedere [Opzioni](#Opzioni.md) per ulteriori informazioni.
4.  Premere il pulsante **OK** per confermare.



## Opzioni

-   **Orientamento**:
    -   **Verticale**: Forza la linea centrale in verticale. Ignorato per Linea centrale tra 2 linee.
    -   **Orizzontale**: forza la linea centrale in orizzontale. Ignorato per Linea centrale tra 2 linee.
    -   **Allineato**: non disponibile per Line centrale alla faccia. Forza la linea centrale a seguire la direzione generale dei bordi selezionati per Line a centrale a 2 linee. Ignorato per Linea centrale a 2 punti.
-   **Scostamento orizzontale**: sposta la linea centrale a sinistra o a destra rispetto alla sua posizione normale.
-   **Scostamento verticale**: sposta la linea centrale verso l\'alto o verso il basso rispetto alla sua posizione normale.
-   **Ruota**: Ruota la linea centrale attorno al suo punto medio (gradi + in senso antiorario, - in senso orario).
-   **Estesa per**: Allunga la linea centrale di questo valore.
-   **Colore**: il colore della linea centrale.
-   **Spessore**: La larghezza della linea centrale.
-   **Stile**: lo stile della linea centrale. Le opzioni sono:
    -   <img alt="" src=images/Continuous-line.svg  style="width:20px;"> 
**Continua**
    -   <img alt="" src=images/Dash-line.svg  style="width:20px;"> 
**Tratteggiata**
    -   <img alt="" src=images/Dot-line.svg  style="width:20px;"> 
**Punto**
    -   <img alt="" src=images/DashDot-line.svg  style="width:20px;"> 
**TrattoPunto**
    -   <img alt="" src=images/DashDotDot-line.svg  style="width:20px;"> 
**TrattoPuntoPunto**



## Note

-   Per eliminare una linea centrale selezionarla e premere **Delete**. {{Version/it|1.0}}
-   Linea centrale alla faccia sostituirà eventualmente due proprietà View:
    -   
        **HorizCenterLine**
        
        : mostra una linea centrale orizzontale attraverso la Vista.

    -   
        **VertCenterLine**
        
        : mostra una linea centrale verticale attraverso la Vista.



## Proprietà

Le Linee centrali non hanno proprietà proprie, poiché non sono oggetti documento.





{{TechDraw Tools navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw FaceCenterLine/it
