---
- GuiCommand:/es
   Name:Sketcher ConstrainParallel
   Name/es:Croquizador RestringirParallel
   Workbenches:[Croquizador](Sketcher_Workbench/es.md)
   MenuLocation:Croquis → Restricciones del Croquizador → Restringir Paralela
   Shortcut:**Shift** + **P**
   SeeAlso:[Croquizador Restriccion Vertical](Sketcher_ConstrainVertical/es.md), [Croquizador Restriccion Horizontal](Sketcher_ConstrainHorizontal/es.md)
---

# Sketcher ConstrainParallel/es


</div>

## Descripción

La Restricción Paralela fuerza que dos líneas rectas o aristas sean paralelas entre sí.

## Operación

El croquis contiene dos líneas de orientación aleatoria.

<img alt="" src=images/ConstrainParallel1.png  style="width:500px;">



*Seleccione ambas líneas haciendo clic sucesivamente en cada una de ellas.*

<img alt="" src=images/ConstrainParallel2.png  style="width:500px;">


<div class="mw-translate-fuzzy">

Aplica la Restricción Paralela seleccionando el icono <img alt="" src=images/Constraint_Parallel.png  style="width:16px;"> de la barra de herramientas de restricciones o seleccionando la Restricción Paralela del submenú de restricciones del entorno del Croquizador (con el entorno del Croquizador seleccionado) o del entorno de Diseño de Piezas (con el entorno de Diseño de Piezas seleccionado).


</div>

<img alt="" src=images/ConstrainParallel3.png  style="width:500px;">


<div class="mw-translate-fuzzy">

Las líneas seleccionadas se forzará a que sean paralelas entre sí. Cambiando la orientación de una línea se cambiará la orientación de la otra.


</div>

## Scripting


```pythonSketch.addConstraint(Sketcher.Constraint('Parallel', Line1, Line2))```

The [Sketcher scripting](Sketcher_scripting.md) page explains the values which can be used for `Line1` and `Line2` and contains further examples on how to create constraints from Python scripts.


<div class="mw-translate-fuzzy">





</div>


{{Sketcher Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainParallel/es
