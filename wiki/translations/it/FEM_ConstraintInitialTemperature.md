---
- GuiCommand:
   Name:FEM_ConstraintInitialTemperature
   Name/it:Temperatura iniziale
   MenuLocation:Modello - Vincoli termici - Vincolo temperatura iniziale
   Workbenches:[FEM](FEM_Workbench/it.md)
   Shortcut:
   SeeAlso:[Tutorial FEM](FEM_tutorial/it.md)
---

# FEM ConstraintInitialTemperature/it


</div>

## Descrizione

Crea un vincolo temperatura iniziale per l\'analisi termomeccanica.

## Utilizzo


<div class="mw-translate-fuzzy">

1.  Cliccare su <img alt="" src=images/FEM_ConstraintInitialTemperature.png  style="width:32px;"> o scegliere **Modello** → **Vincoli termici** → **<img src="images/FEM_ConstraintInitialTemperature.png" width=32px> Vincolo temperatura iniziale** dal menu principale.
2.  Inserire un valore iniziale della temperatura per l\'analisi.


</div>

## Limitazioni


<div class="mw-translate-fuzzy">

Il vincolo applica la temperatura iniziale a tutti i nodi nel modello FEA


</div>

## Note


<div class="mw-translate-fuzzy">

1.  Il vincolo usa la \*\*INITIAL CONDITIONS card in CalculiX. Il vincolo temperatura iniziale è spiegato in <http://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node215.html>


</div>


<div class="mw-translate-fuzzy">





</div>


{{FEM Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintInitialTemperature/it
