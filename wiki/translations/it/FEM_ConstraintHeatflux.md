---
- GuiCommand:/it
   Name:FEM_ConstraintHeatflux
   Name/it:Scambio termico
   MenuLocation:Modello → Vincoli termici → Vincolo scambio termico
   Workbenches:[FEM](FEM_Workbench/it.md)
   Shortcut:
   SeeAlso:[Tutorial FEM](FEM_tutorial/it.md)
---

# FEM ConstraintHeatflux/it


</div>

## Descrizione


<div class="mw-translate-fuzzy">

Questo vincolo specifica lo scambio termico (film heat transfer) di una superficie a temperatura *T* e con un coefficiente di scambio termico *h* e una temperatura ambiente *T~0~*. Il flusso di calore convettivo *q* è in grado di soddisfare: ***q = h(T -T~0~)***


</div>

## Utilizzo


<div class="mw-translate-fuzzy">

1.  Cliccare su <img alt="" src=images/FEM_ConstraintHeatflux.png  style="width:32px;"> o scgliere **Modello** → **Vincoli termici** → **<img src="images/FEM_ConstraintHeatflux.png" width=32px> Vincolo Scambio termico** dal menu principale.
2.  Selezionare nella vista 3D la superficie a cui il vincolo deve essere applicato.
3.  Inserire la temperatura della superficie desiderata, il coefficiente del materiale e la temperatura ambiente.


</div>

## Note


<div class="mw-translate-fuzzy">

1.  Il vincolo utilizza la \*FILM card in CalculiX. Il vincolo scambio termico è spiegato in <http://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node203.html>


</div>


<div class="mw-translate-fuzzy">





</div>


{{FEM Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintHeatflux/it
