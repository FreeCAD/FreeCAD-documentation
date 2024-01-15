---
 GuiCommand:
   Name: FEM_ConstraintTemperature
   Name/it: Vincolo temperatura
   MenuLocation: Modello , Vincoli termici , Vincolo temperatura
   Workbenches: FEM_Workbench/it
   Shortcut: 
   SeeAlso: FEM_tutorial/it
---

# FEM ConstraintTemperature/it


</div>



## Descrizione


<div class="mw-translate-fuzzy">

Crea un vincolo FEM per una condizione limite di temperatura.


</div>



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

By default, this feature defines a temperature boundary condition. By using the option **Concentrated heat flux**, one can specify a heat flux value (in mW) in each node belonging to the selected geometrical entity.



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
