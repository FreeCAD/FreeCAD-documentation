---
 GuiCommand:
   Name: FEM ConstraintTemperature
   Name/ru: FEM ConstraintTemperature
   MenuLocation: Model , Thermal Constraints , Constraint temperature
   Workbenches: FEM_Workbench/ru
   Shortcut: 
   SeeAlso: FEM_tutorial/ru
---

# FEM ConstraintTemperature/ru


</div>



## Описание


<div class="mw-translate-fuzzy">

Создаёт ограничения для МКЭ по температурным границам.


</div>



## Применение

1.  There are several ways to invoke the command:
    -   Press the **<img src="images/FEM_ConstraintTemperature.svg" width=16px> [Temperature boundary condition](FEM_ConstraintTemperature.md)** button.
    -   Select the **Model → Thermal boundary conditions and loads → <img src="images/FEM_ConstraintTemperature.svg" width=16px> Temperature boundary condition** option from the menu.
2.  In the [3D view](3D_view.md) select the objects the boundary condition should be applied to, which can be a vertices (corners), edges, or faces.
3.  Enter a temperature to apply to the objects.

### Option

By default, this feature defines a temperature boundary condition. By using the option **Concentrated heat flux**, one can specify a heat flux value (in mW) in each node belonging to the selected geometrical entity.



## Примечания


<div class="mw-translate-fuzzy">

1.  Ограничение температуры использует карту \*BOUNDARY в CalculiX. Подробнее об ограничение температуры можно узнать по адрессу <http://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node163.html>


</div>





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintTemperature/ru
