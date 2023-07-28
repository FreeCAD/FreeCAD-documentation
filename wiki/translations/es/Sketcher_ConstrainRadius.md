---
- GuiCommand:/es
   Name:Constraint Radius
   Name/es:Constraint Radius
   Workbenches:[Croquizador](Sketcher_Workbench/es.md), [Diseño de Piezas](PartDesign_Workbench/es.md)
   MenuLocation:Croquizador → Restricciones del Croquizador → Radio
   SeeAlso:[Distancia](Sketcher_ConstrainDistance/es.md), [Horizontal](Sketcher_ConstrainHorizontal/es.md), [Vertical](Sketcher_ConstrainVertical/es.md)
---

# Sketcher ConstrainRadius/es


</div>



## Descripción


<div class="mw-translate-fuzzy">

Esta restricción restringe el valor del radio de una circunferencia o un arco a un valor específico. Sólo se puede restringir un arco o una circunferencia de cada vez.


</div>

![](images/Sketcher_ConstrainRadius_example.png )



## Utilización

Selecciona un arco o una circunferencia en el croquis pulsando encima (se volverá de color verde oscuro).

<img alt="" src=images/ConstrainRadius2.png  style="width:256px;">

Aplica la restricción pulsando el icono de la Restricción de Radio <img alt="" src=images/Constraint_Radius.png  style="width:16px;"> en la barra de herramientas del Croquizador o selecciona la Restricción de Radio en el submenú de Restricciones del módulo del Croquizador (o Diseño de Piezas dependiendo de que entorno esté seleccionado).

<img alt="" src=images/ConstrainRadius3.png  style="width:256px;">

El radio se restringe a su valor actual al aplicar la restricción.

Para cambiar el valor de la restricción haz doble clic sobre ella en la vista 3D o en la pestaña de Tareas. Esto abrirá una ventana en la que se puede modificar el valor asignado.

<img alt="" src=images/ConstrainRadius4.png  style="width:256px;">

Introduce el valor deseado para el radio y pulsa OK para establecer el valor a la restricción.

<img alt="" src=images/ConstrainRadius5.png  style="width:256px;">

El valor de la restricción se establecerá al valor indicado en la ventana. 

**Note:** the constraint tool can also be started with no prior selection. By default the command will be in continue mode to create new constraints; press the right mouse button or **Esc** once to quit the command.

## Scripting


```pythonSketch.addConstraint(Sketcher.Constraint('Radius', ArcOrCircle, App.Units.Quantity('123.0 mm')))```

The [Sketcher scripting](Sketcher_scripting.md) page explains the values which can be used for `ArcOrCircle`, and contains further examples on how to create constraints from Python scripts.





{{Sketcher_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainRadius/es
