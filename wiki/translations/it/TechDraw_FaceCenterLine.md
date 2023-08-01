---
- GuiCommand:
   Name:TechDraw FaceCenterLine
   Name/it:Linea a centro faccia
   MenuLocation:TechDraw - Aggiungi linee - Linea a centro faccia
   Workbenches:[TechDraw](TechDraw_Workbench/it.md)
   SeeAlso:[Vertice cosmetico](TechDraw_CosmeticVertex/it.md), [Linea centrale a 2 linee](TechDraw_2LineCenterLine/it.md), [Linea centrale a 2 punti](TechDraw_2PointCenterLine/it.md), [Rimuovi oggetto cosmetico](TechDraw_CosmeticEraser/it.md)
   Version:0.19
---

# TechDraw FaceCenterLine/it


</div>



## Descrizione


<div class="mw-translate-fuzzy">

Lo strumento Linea a centro faccia aggiunge una linea centrale alle facce selezionate


</div>

<img alt="" src=images/TechDraw_FaceCenterLine_Sample.png  style="width:400px;">


<div class="mw-translate-fuzzy">



*Linea centrale aggiunta alla faccia*


</div>

## Usage create 


<div class="mw-translate-fuzzy">

1.  Selezionare una o più facce in una vista.
2.  Premere il pulsante **<img src="images/TechDraw_FaceCenterLine.svg" width=16px> Linea a centro faccia
**
3.  Si apre una finestra di dialogo in cui è possibile specificare gli attributi della nuova linea centrale.
4.  Viene aggiunta una linea centrale nel punto medio del riquadro di delimitazione delle facce selezionate.


</div>

## Usage edit 


<div class="mw-translate-fuzzy">

Per modificare qualsiasi linea centrale si può usare qualsiasi pulsante di comando delle linee centrali (**<img src="images/TechDraw_FaceCenterLine.svg" width=16px> Linea a centro faccia**, **<img src="images/TechDraw_2LineCenterLine.svg" width=16px> [Linea a centro linee](TechDraw_2LineCenterLine/it.md)**, **<img src="images/TechDraw_2PointCenterLine.svg" width=16px> [Linea a centro punti](TechDraw_2PointCenterLine/it.md)**).


</div>


<div class="mw-translate-fuzzy">

1.  Selezionare una linea centrale.
2.  Premere qualsiasi pulsante di comando di linea centrale.
3.  Si apre una finestra di dialogo in cui è possibile modificare gli attributi della linea centrale.
4.  Premere **OK** per vedere le modifiche applicate.


</div>




<div class="mw-translate-fuzzy">

## Proprietà


</div>


<div class="mw-translate-fuzzy">

1.  Mode (pulsanti di opzione):
    -   **Vertical**: Forza una linea centrale verticale
    -   **Horizontal**: Forza una linea centrale orizzontale
    -   ***Aligned**: Questa opzione non è possibile per la linea centrale delle facce*
2.  **Shift Horiz**: Sposta la linea centrale a sinistra o a destra della sua posizione normale
3.  **Shift Vert**: Sposta la linea centrale verso l\'alto o verso il basso dalla sua posizione normale
4.  **Rotate**: Ruota la linea centrale attorno al suo centro (in gradi, + Antiorario, - orario)
5.  **Extend**: Allunga la linea centrale di questo importo
6.  **Color**: Colore della linea centrale
7.  **Weight**: Spessore della linea centrale
8.  **Style**: <img alt="" src=images/Continuous-line.svg  style="width:20px;"> Continua, <img alt="" src=images/Dash-line.svg  style="width:20px;"> A tratti, <img alt="" src=images/Dot-line.svg  style="width:20px;"> Punti, <img alt="" src=images/DashDot-line.svg  style="width:20px;"> Tratto e punto, <img alt="" src=images/DashDotDot-line.svg  style="width:20px;"> Tratto e due punti


</div>



## Note


<div class="mw-translate-fuzzy">

-   FaceCenterLine sostituisce eventualmente due proprietà vista:
    -   
        **HorizCenterLine**
        
        : Mostra una linea centrale orizzontale attraverso la vista.

    -   
        **VertCenterLine**
        
        : Mostra una linea centrale verticale attraverso la vista.


</div>

## Properties

Centerlines have no properties of their own, as they are not document objects.


<div class="mw-translate-fuzzy">





</div>


{{TechDraw Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw FaceCenterLine/it
