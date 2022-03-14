---
- GuiCommand:/it
   Name:Sketcher Extend
   Name/it:Estendi bordo
   Icon:Sketcher Extend.svg
   MenuLocation:Sketch → Geometrie → Estendi bordo
   Workbenches:[Sketcher](Sketcher_Workbench/it.md)
   SeeAlso:[Rifila](Sketcher_Trimming/it.md)
   Version:0.17
---

# Sketcher Extend/it


</div>

## Descrizione


<div class="mw-translate-fuzzy">

Lo strumento **Estendi bordo** estende un bordo fino ad una posizione arbitraria nello schizzo o fino ad un altro bordo.


</div>

<img alt="" src=images/Sketcher_Extend_example_01.png  style="width:600px;">


<div class="mw-translate-fuzzy">

*A sinistra (1) sono indicati i due elementi dello schizzo prima dell\'operazione; nel mezzo (2) la linea viene estesa all\'arco; a destra (3) il risultato finale.*


</div>

## Utilizzo


<div class="mw-translate-fuzzy">

1.  Premere il pulsante <img alt="" src=images/Sketcher_Extend.svg  style="width:24px;"> **Estendi bordo**.
2.  Selezionare una linea o un arco.
3.  Nella vista 3D, spostare il puntatore del mouse verso la direzione da estendere.
4.  Fare clic su una posizione arbitraria nello spazio, oppure
5.  Per estendere fino ad un altro bordo, posizionare il puntatore del mouse sul bordo; quando è evidenziato e vicino al puntatore del mouse appare l\'icona del vincolo <img alt="" src=images/Sketcher_ConstrainPointOnObject.png  style="width:24px;"> [Punto su oggetto](Sketcher_ConstrainPointOnObject/it.md), cliccare per confermare. Viene aggiunto un vincolo punto su oggetto.
6.  Per estendere a un punto nello schizzo, posizionare il puntatore del mouse sul punto; quando è evidenziato e vicino al puntatore del mouse appare l\'icona del vincolo <img alt="" src=images/Sketcher_ConstrainCoincident.png  style="width:24px;"> [Coincidente](Sketcher_ConstrainCoincident/it.md), cliccare per confermare. Viene aggiunto un vincolo coincidente.


</div>

## Notes

-   Only arcs and lines can be extended at this time.
-   The target edge or point object may be modified as well if it is not fully constrained.


<div class="mw-translate-fuzzy">





</div>


{{Sketcher Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher Extend/it
