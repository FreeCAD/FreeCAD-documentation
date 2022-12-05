---
- GuiCommand:/it
   Name:TechDraw 2LineCenterLine
   Name/it:Linea centrale a 2 linee
   MenuLocation:TechDraw → Aggiungi linee → Linea centrale a 2 linee
   Workbenches:[TechDraw](TechDraw_Workbench/it.md)
   SeeAlso:[Linea a centro faccia](TechDraw_FaceCenterLine/it.md), [Linea centrale a 2 punti](TechDraw_2PointCenterLine/it.md)
   Version:0.19
---

# TechDraw 2LineCenterLine/it


</div>

## Descrizione

Lo strumento Linea centrale a 2 linee aggiunge una linea centrale tra due bordi.

<img alt="" src=images/CL2LinesSample.png  style="width:350px;">



*Linea centrale allineata tra 2 bordi*

## Utilizzo


<div class="mw-translate-fuzzy">

1.  Selezionare 2 bordi in una vista. Non è necessario che i bordi siano paralleli.
2.  Premere il pulsante **<img src="images/TechDraw_2LineCenterLine.svg" width=16px> Linea centrale a 2 linee**.
3.  Si apre una finestra di dialogo in cui è possibile specificare gli attributi della nuova linea centrale.
4.  Viene aggiunta una linea centrale tra i 2 bordi selezionati.Se la riga generata sembra strana, potrebbe essere necessario utilizzare l\'opzione [**Flip Ends**](#Flip_Ends.md).


</div>

Per eliminare una linea centrale, selezionarla e utilizzare il pulsante della barra degli strumenti **<img src="images/TechDraw_CosmeticEraser.svg" width=16px> [Rimuovi oggetto cosmetico](TechDraw_CosmeticEraser/it.md)**.

## Modificare le linee centrali 

Per modificare qualsiasi linea centrale si può usare qualsiasi pulsante di comando delle linee centrali (**<img src="images/TechDraw_FaceCenterLine.svg" width=16px> [Linea a centro faccia](TechDraw_FaceCenterLine/it.md)**, **<img src="images/TechDraw_2LineCenterLine.svg" width=16px> Linea centrale a 2 linee**, **<img src="images/TechDraw_2PointCenterLine.svg" width=16px> [Linea centrale a 2 punti](TechDraw_2PointCenterLine/it.md)**).

1.  Selezionare una linea centrale.
2.  Premere qualsiasi pulsante di comando di linea centrale.
3.  Si apre una finestra di dialogo in cui è possibile modificare gli attributi della linea centrale.
4.  Premere **OK** per vedere applicate le modifiche.

## Proprietà


<div class="mw-translate-fuzzy">

Le linee centrali cosmetiche non hanno proprietà proprie, in quanto non sono Document Objects. Esse hanno degli attributi che possono essere modificati.


</div>


<div class="mw-translate-fuzzy">

1.  Modus (pulsanti di opzione):
    -   **Verticale**: Forza una linea centrale verticale
    -   **Orizzontale**: Forza una linea centrale orizzontale
    -   **Allineata**: La linea centrale a 2 linee segue la direzione generale dei bordi
2.  **Scostamento orizzontale**: Sposta la linea centrale a sinistra o a destra della sua posizione normale
3.  **Scostamento verticale**: Sposta la linea centrale verso l\'alto o verso il basso dalla sua posizione normale
4.  **Ruota**: Ruota la linea centrale attorno al suo centro (in gradi, + antiorario, - orario)
5.  **Estesa per**: Aumenta la linea centrale di questo importo
6.  **Colore**: Colore della linea centrale
7.  **Spessore**: Spessore della linea centrale
8.  **Stile**: <img alt="" src=images/Continuous-line.svg  style="width:20px;"> continua, <img alt="" src=images/Dash-line.svg  style="width:20px;"> a tratti, <img alt="" src=images/Dot-line.svg  style="width:20px;"> punti, <img alt="" src=images/DashDot-line.svg  style="width:20px;"> tratto e punto, <img alt="" src=images/DashDotDot-line.svg  style="width:20px;"> tratto e due punti
9.  **Capovolgi**: Capovolge i punti finali per la creazione come descritto di seguito


</div>

## Capovilgi


<div class="mw-translate-fuzzy">

<img alt="Schizzo di come viene costruita la linea centrale" src=images/TD-CenterLineFlip.png  style="width:350px;"> La linea centrale tra 2 linee viene disegnata tra i punti medi (m0 e m1) delle linee che collegano i punti finali delle linee selezionate (p0 e p1), vedere lo schizzo. A seconda dell\'ordine dei punti ci sono 2 possibilità per disegnare le linee di collegamento. L\'opzione **Capovolgi** inverte il modo in cui vengono disegnate le linee di collegamento.


</div>

## Script


<div class="mw-translate-fuzzy">


**Vedere anche:**

[TechDraw API](TechDraw_API/it.md) e [Nozioni di base sugli script di FreeCAD](FreeCAD_Scripting_Basics/it.md).


</div>


<div class="mw-translate-fuzzy">

In questo momento la Linea centrale non è accessibile dalle [macro](macros/it.md) o dalla console [Python](Python/it.md).


</div>


<div class="mw-translate-fuzzy">





</div>


{{TechDraw Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw 2LineCenterLine/it
