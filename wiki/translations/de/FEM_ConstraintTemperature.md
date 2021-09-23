---
- GuiCommand:/de
   Name:FEM ConstraintTemperature
   Name/de:FEM BeschränkungTemperatur
   MenuLocation:Modell → Thermische Beschränkungen → Temperaturbeschränkung 
   Workbenches:[FEM](FEM_Workbench/de.md)
   Shortcut:
   SeeAlso:[FEM Tutorium](FEM_tutorial/de.md)
---

# FEM ConstraintTemperature/de


</div>

## Beschreibung

Creates a FEM constraint for a temperature boundary condition.

## Anwendung

1.  There are several ways to invoke the command:
    -   Press the **<img src="images/FEM_ConstraintTemperature.svg" width=16px> [FEM ConstraintTemperature](FEM_ConstraintTemperature.md)** button.
    -   Select the **Model → Thermal Constraints → <img src="images/FEM_ConstraintTemperature.svg" width=16px> Constraint temperature** option from the menu.
2.  In the [3D view](3D_view.md) select the objects the constraint should be applied to, which can be a vertices (corners), edges, or faces.
3.  Enter a temperature to apply to the objects.

## Hinweise

1.  The temperature constraint uses the \*BOUNDARY card in CalculiX. the temperature constraint is explained at <http://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node163.html>


<div class="mw-translate-fuzzy">





</div>


{{FEM Tools navi

}}

---
[documentation index](../README.md) > FEM ConstraintTemperature/de
