---
- GuiCommand:
   Name: FEM_ConstraintTemperature
   Name/it: Vincolo temperatura
   MenuLocation: Modello -> Vincoli termici -> Vincolo temperatura
   Workbenches: FEM_Workbench/it
   Shortcut: 
   SeeAlso: FEM_tutorial/it
---

# FEM ConstraintTemperature/it


</div>

## Descrizione

Crea un vincolo FEM per una condizione limite di temperatura.

## Utilizzo


<div class="mw-translate-fuzzy">

1.  Cliccare su <img alt="" src=images/FEM_ConstraintTemperature.png  style="width:32px;"> o scegliere **Modello** → **Vincoli termici** → **<img src="images/FEM_ConstraintTemperature.png" width=32px> Vincolo temperatura** dal menu principale.
2.  Selezionare nella vista 3D gli oggetti a cui deve essere applicato il vincolo, che possono essere:
    1.  vertici (angoli)
    2.  bordi
    3.  facce
3.  Inserire una temperatura da applicare agli oggetti.


</div>

### Option

By default the constraint defines a temperature. By using the option **Concentrated heat Flux** a heat flux trough the area of the face (Watt per face area) can be specified.

## Note


<div class="mw-translate-fuzzy">

1.  Il vincolo di temperatura utilizza la \*BOUNDARY card in CalculiX. Il vincolo di temperatura è spiegato in <http://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node163.html>


</div>


<div class="mw-translate-fuzzy">





</div>


{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintTemperature/it
