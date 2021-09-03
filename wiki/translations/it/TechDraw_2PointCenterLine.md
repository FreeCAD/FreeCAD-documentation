---
- GuiCommand:/it
   Name:TechDraw 2PointCenterLine
   Name/it:Linea centrale a 2 punti
   MenuLocation:TechDraw → Aggiungi linee → Linea centrale a 2 punti
   Workbenches:[TechDraw](TechDraw_Workbench/it.md)
   SeeAlso:[Linea centro faccia](TechDraw_FaceCenterLine/it.md), [Linea centro linee](TechDraw_2LineCenterLine/it.md)
   Version:0.19
---


</div>

## Descrizione

Lo strumento Linea centrale a 2 punti aggiunge una linea centrale tra due vertici (punti).

<img alt="" src=images/CL2PointsSample.png  style="width:200px;">


*Linea centrale tra 2 punti*

## Utilizzo

1.  Selezionare 2 vertici in una vista.
2.  Premere il pulsante **<img src="images/TechDraw_2PointCenterLine.svg" width=16px> Linea centrale a 2 punti**.
3.  Si apre una finestra di dialogo in cui è possibile specificare gli attributi della nuova linea centrale.
4.  Viene aggiunta una linea centrale tra i 2 punti selezionati.

Per eliminare una linea centrale, selezionarla e utilizzare il pulsante della barra degli strumenti **<img src="images/TechDraw_CosmeticEraser.svg" width=16px> [Rimuovi oggetto cosmetico](TechDraw_CosmeticEraser/it.md)**.

## Modificare le linee centrali {#modificare_le_linee_centrali}

Per modificare qualsiasi linea centrale si può usare qualsiasi pulsante di comando delle linee centrali (**<img src="images/TechDraw_FaceCenterLine.svg" width=16px> [Linea centro faccia](TechDraw_FaceCenterLine/it.md)**, **<img src="images/TechDraw_2LineCenterLine.svg" width=16px> [Linea centrale a 2 linee](TechDraw_2LineCenterLine/it.md)**, **<img src="images/TechDraw_2PointCenterLine.svg" width=16px> [Linea centrale a 2 punti](TechDraw_2PointCenterLine/it.md)**).

1.  Selezionare una linea centrale.
2.  Premere qualsiasi pulsante di comando di linea centrale.
3.  Si apre una finestra di dialogo in cui è possibile modificare gli attributi della linea centrale.
4.  Premere **OK** per vedere le modifiche applicate.

## Proprietà


<div class="mw-translate-fuzzy">

Le linee centrali cosmetiche non hanno proprietà proprie, in quanto non sono Document objects. Hanno attributi che possono essere modificati nella finestra di dialogo di modifica della linea centrale.


</div>

1.  Mode (pulsanti di opzione):
    -   Vertical: forza la linea centrale verticale
    -   Horizontal: forza la linea centrale orizzontale
    -   Aligned: segue la direzione generale del bordo per la linea centrale tra due bordi
2.  Shift Horiz: sposta la linea centrale a sinistra o a destra rispetto alla sua posizione normale
3.  Shift Vert: sposta la linea centrale in alto o in basso rispetto alla sua posizione normale
4.  Rotate: ruota la linea centrale attorno al suo centro (gradi, +CCW, -CW)
5.  Extend: estende la linea centrale di questa quantità
6.  Color: colore della linea centrale
7.  Weight: spessore della linea centrale
8.  Style: <img alt="" src=images/Continuous-line.svg  style="width:20px;"> Continuous, <img alt="" src=images/Dash-line.svg  style="width:20px;"> Dash, <img alt="" src=images/Dot-line.svg  style="width:20px;"> Dot, <img alt="" src=images/DashDot-line.svg  style="width:20px;"> DashDot, <img alt="" src=images/DashDotDot-line.svg  style="width:20px;"> DashDotDot

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
