---
 GuiCommand:
   Name: Constraint Radius
   Name/es: Constraint Radius
   Workbenches: Sketcher Workbench/es, PartDesign Workbench/es
   MenuLocation: Croquizador , Restricciones del Croquizador , Radio
   SeeAlso: Sketcher_ConstrainDistance/es, Sketcher_ConstrainHorizontal/es, Sketcher_ConstrainVertical/es
---

# Sketcher ConstrainRadius/es


</div>



## Descripción


<div class="mw-translate-fuzzy">

Esta restricción restringe el valor del radio de una circunferencia o un arco a un valor específico. Sólo se puede restringir un arco o una circunferencia de cada vez.


</div>

![](images/Sketcher_ConstrainRadius_example.png )



## Utilización

See also: [Drawing aids](Sketcher_Workbench#Drawing_aids.md).

### [Continue mode](Sketcher_Workbench#Continue_modes.md) 


<div class="mw-translate-fuzzy">

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


</div>

### Run-once mode 

See [Sketcher ConstrainRadiam](Sketcher_ConstrainRadiam#Run-once_mode.md).

## Scripting


```pythonSketch.addConstraint(Sketcher.Constraint('Radius', ArcOrCircle, App.Units.Quantity('123.0 mm')))```

The [Sketcher scripting](Sketcher_scripting.md) page explains the values which can be used for `ArcOrCircle`, and contains further examples on how to create constraints from Python scripts.



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainRadius/es
