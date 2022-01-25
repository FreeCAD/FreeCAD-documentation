---
- GuiCommand:/es
   Name:Sketcher ConstrainEqual
   Name/es:Croquizador RestringirIgual
   Workbenches:[Croquizador](Sketcher_Workbench/es.md)
   MenuLocation:Croquis → Croquizador Restricciones → Restringir igual
   Shortcut:E
   SeeAlso:[Restringir radius](Sketcher_ConstrainRadius/es.md)
---

# Sketcher ConstrainEqual/es


</div>

## Descripción


<div class="mw-translate-fuzzy">

La restricción Igual fuerza que dos o más segmentos de línea en una línea, polilínea o rectángulo tengan la misma longitud. Si se aplica sobre arcos o circunferencias el radio se restringe para que sea igual. No puede aplicarse sobre geometría que no sea del mismo tipo (por ejemplo segmentos de línea y arcos).


</div>


<div class="mw-translate-fuzzy">

## Funcionamiento

El croquis de ejemplo de abajo contiene una serie de primitivas de croquis ( línea, polilínea, rectángulo, arco y circunferencia).

<img alt="" src=images/EqualConstraint1.png  style="width:256px;">

Selecciona dos o más segmentos de línea (por ejemplo la línea y un lado del rectángulo).

<img alt="" src=images/EqualConstraint2.png  style="width:256px;">

Pulsa sobre el icono de la Restricción Igual <img alt="" src=images/Constraint_EqualLength.png  style="width:16px;"> en la barra de herramientas del Croquizador (tanto en el entorno del Croquizador como en el de Diseño de Piezas) o selecciona el elemento Restricción Igual en el submenú de las restricciones del entorno del Croquizador o en el entorno de Diseño de Piezas, dependiendo del entorno que esté seleccionado (Croquizador o Diseño de Piezas) para aplicar la restricción a los elementos seleccionados.

<img alt="" src=images/EqualConstraint3.png  style="width:256px;">

Ahora selecciona el arco y la circunferencia en el croquis.

<img alt="" src=images/EqualConstraint4.png  style="width:256px;">

y aplica la Restricción Igual <img alt="" src=images/Constraint_EqualLength.png  style="width:16px;"> tal como hiciste antes.

<img alt="" src=images/EqualConstraint5.png  style="width:256px;">

Ahora selecciona el segmento de línea, todos los segmentos de la polilínea y uno de los lados del rectángulo que no están restringidos

<img alt="" src=images/EqualConstraint6.png  style="width:256px;">

y aplica la Restricción Igual <img alt="" src=images/Constraint_EqualLength.png  style="width:16px;"> tal como hiciste antes.

<img alt="" src=images/EqualConstraint7.png  style="width:256px;">

Selecciona el segmento de línea y el arco

<img alt="" src=images/EqualConstraint8.png  style="width:256px;">

y aplica la Restricción Igual <img alt="" src=images/Constraint_EqualLength.png  style="width:16px;"> tal como hiciste antes. Un letrero de mensaje indica que los elementos restringidos deben ser del mismo tipo geométrico (líneas de curvatura cero o líneas de curvatura distinta de cero).

<img alt="" src=images/EqualConstraint9.png  style="width:256px;">


</div>

The example sketch below contains a number of sketch primitives (line, poly-line, rectangle, arc and circle).

![](images/EqualConstraint1.png )

Select two or more line segments (e.g. line and one side of the rectangle).

![](images/EqualConstraint2.png )

Click on **[<img src=images/Sketcher_ConstrainEqual.svg style="width:16px"> [Constrain equal](Sketcher_ConstrainEqual.md)** in the Sketcher toolbar (in either the Sketcher or Part Design workbenches) or select the Constrain Equal menu item from the Sketcher constraints sub menu item in either the Sketch or Part Design menu item depending upon which workbench is selected (Sketcher or Part Design) to apply the constraint to the selected items.

![](images/EqualConstraint3.png )

Now select the arc and the circle in the sketch.

![](images/EqualConstraint4.png )

and apply **[<img src=images/Sketcher_ConstrainEqual.svg style="width:16px"> [Constrain equal](Sketcher_ConstrainEqual.md)** as before.

![](images/EqualConstraint5.png )

Now select the line segment, all segments of the poly-line and one of the remaining unconstrained sides of the rectangle

![](images/EqualConstraint6.png )

and apply **[<img src=images/Sketcher_ConstrainEqual.svg style="width:16px"> [Constrain equal](Sketcher_ConstrainEqual.md)** as before.

![](images/EqualConstraint7.png )

Select the line segment and the arc

![](images/EqualConstraint8.png )

and apply **[<img src=images/Sketcher_ConstrainEqual.svg style="width:16px"> [Constrain equal](Sketcher_ConstrainEqual.md)** as before. A pop-up message indicates that the constrained items have to be of the same geometrical type (lines of zero curvature or lines of non-zero curvature).

![](images/EqualConstraint9.png )

## Scripting


```pythonSketch.addConstraint(Sketcher.Constraint('Equal', Edge1, Edge2))```

The [Sketcher scripting](Sketcher_scripting.md) page explains the values which can be used for `Edge1` and `Edge2` and contains further examples on how to create constraints from Python scripts.





{{Sketcher Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainEqual/es
