---
- GuiCommand:
   Name:FEM_ConstraintPlaneRotation
   Name/it:Vincolo piano di rotazione
   MenuLocation:Modello - Vincoli meccanici - Vincolo piano di rotazione
   Workbenches:[FEM](FEM_Workbench/it.md)
   Shortcut:
   SeeAlso:[FEM tutorial](FEM_tutorial/it.md)
---

# FEM ConstraintPlaneRotation/it


</div>

## Descrizione

Crea un vincolo FEM per mantenere i nodi in una superficie planare nello stesso piano.

## Utilizzo


<div class="mw-translate-fuzzy">

1.  Cliccare su <img alt="" src=images/FEM_ConstraintPlaneRotation.png  style="width:32px;"> o scegliere **Modello** → **Vincoli meccanici** → **<img src="images/FEM_ConstraintPlaneRotation.png" width=32px> Vincolo piano di rotazione** dal menu principale.
2.  Selezionare nella vista 3D l\'oggetto a cui deve essere applicato il vincolo, che deve essere una faccia.


</div>

## Limitazioni


<div class="mw-translate-fuzzy">

1.  Il vincolo piano di rotazione può essere applicato solo ad una singola faccia planare.
2.  Quando un vincolo piano di rotazione viene applicato alla stessa faccia che ha un vincolo di dislocamento o fissaggio, il vincolo di dislocamento o fissaggio prevale.


</div>

## Note


<div class="mw-translate-fuzzy">

1.  Il vincolo utilizza la \*MPC card in CalculiX. La card è spiegata in dettaglio <http://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node220.html>


</div>


<div class="mw-translate-fuzzy">





</div>


{{FEM Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintPlaneRotation/it
