# FEM ConstraintTemperature/ro
---
- GuiCommand:   Name:FEM ConstraintTemperature   MenuLocation:Model - Thermal Constraints - Constraint temperature   |Workbenches:[Shortcut:   SeeAlso:[[FEM_tutorial|FEM tutorial](FEM_Workbench___FEM]].md)---


</div>

## Descriere

Crée une contrainte FEM pour une condition de limite de température.


<div class="mw-translate-fuzzy">

## Utilizare


</div>


<div class="mw-translate-fuzzy">

1.  Click pe <img alt="" src=images/FEM_ConstraintTemperature.png  style="width:32px;"> or choose **Model** → **Thermal Constraints** → **<img src="images/FEM_ConstraintTemperature.png" width=32px> Constraint temperature** din meniul principal.
2.  Selectați în vizualizarea 3D obiectul(e) la care trebuie aplicată constrângerea, care poate fi
    1.  vertices (corners)
    2.  edges
    3.  faces
3.  Introduceți o temperatură pentru a fi aplicată obiectului.


</div>

### Option

By default the constraint defines a temperature. By using the option **Concentrated heat Flux** a heat flux trough the area of the face (Watt per face area) can be specified.

## Notă


<div class="mw-translate-fuzzy">

1.  Constrângerea utilizează \*BOUNDARY card in CalculiX. constrângerea de temperatură este explicat la <http://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node163.html>


</div>





{{FEM Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintTemperature/ro
