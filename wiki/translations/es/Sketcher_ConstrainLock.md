---
- GuiCommand:
   Name: Sketcher ConstrainLock
   Name/es: Sketcher ConstrainLock
   Workbenches: [Croquizador](Sketcher_Workbench/es.md), [Diseño de Piezas](PartDesign_Workbench/es.md)
   MenuLocation: Croquizador - Restricciones del Croquizador  - Bloquear
   SeeAlso: [Croquizador RestringirBloque](Sketcher_ConstrainBlock/es.md)
---

# Sketcher ConstrainLock/es


</div>


<div class="mw-translate-fuzzy">

\"Crea una restricción de bloqueo sobre el elemento seleccionado\"

## Descripción

Esta restricción trata de restringir completamente cualquier elemento seleccionado.


</div>

**Constraint Lock** applies **[<img src=images/Sketcher_ConstrainDistanceX.svg style="width:16px"> [Horizontal distance](Sketcher_ConstrainDistanceX.md)** and **[<img src=images/Sketcher_ConstrainDistanceY.svg style="width:16px"> [Vertical distance](Sketcher_ConstrainDistanceY.md)** constraints to selected vertices (points) in the sketch. If a single vertex is selected, the horizontal and vertical distance constraints will refer to the sketch origin point. If two or more points are selected, horizontal and vertical distance constraints will be added for each pair of points. There is no automatic prompt to edit the constraints\' values, they must be edited manually.


<div class="mw-translate-fuzzy">

Debido a que FreeCAD aún está en desarrollo - esta herramienta presenta un comportamiento extraño cuando se intenta \'bloquear\' cualquier cosa que no sea un punto. Por ejemplo (para V0.12 R4802), cuando se bloquea una circunferencia por su contorno y no por su punto central, aparece una restricción horizontal y una vertical en el letrero de diálogo pero no en la ventana gráfica.

## Funcionamiento

1.  En primer lugar es necesario resaltar una entidad que quieras restringir. Por las razones mencionadas anteriormente es preferible sólo destacar un punto.
    <img alt="" src=images/LockConstraint1.png  style="width:256px;">
2.  El destacado de un elemento de dibujo se logra moviendo el ratón sobre el elemento y pulsando el botón izquierdo del ratón. Un elemento destacado cambiará su color a verde.
    <img alt="" src=images/LockConstraint2.png  style="width:256px;">
3.  Una vez que un elemento está destacado, pulsar con el botón izquierdo del ratón en la restricción de bloquear sirve para bloquear el elemento destacado en su ubicación. Esto normalmente se manifiesta como dos restricciones: Una distancia horizontal desde el origen de coordenadas del dibujo, y una restricción vertical desde el origen del sistema de coordenadas. Estas se establecen por defecto para las coordenadas actuales del punto.
    <img alt="" src=images/LockConstraint3.png  style="width:256px;">
4.  Las restricciones Vertical y Horizontal que forman el bloqueo se pueden editar haciendo doble clic en la restricción apropiada para ser editada ya sea en el dibujo o en la pestaña de restricciones del panel. Esto abrirá un letrero de diálogo para editar la restricción. Pulsar en la componente horizontal de la restricción produce:
    <img alt="" src=images/LockConstraint4.png  style="width:256px;">.
5.  Introduce el valor deseado en el letrero de diálogo y pulsa OK.
    <img alt="" src=images/LockConstraint5.png  style="width:256px;">
6.  El nuevo valor de la restricción se aplica al dibujo.
    <img alt="" src=images/LockConstraint6.png  style="width:256px;">
7.  La restricción vertical se puede editar de forma similar para restringir el punto a la ubicación deseada.
    <img alt="" src=images/LockConstraint7.png  style="width:256px;">


</div>

1.  Select one or more vertices (points) in the sketch.
2.  Press the **[<img src=images/Sketcher_ConstrainLock.svg style="width:16px"> [Constrain lock](Sketcher_ConstrainLock.md)** button.
3.  To edit the constraints values, double-click on a constraint value in the 3D view, or double-click on the constraint or right-click and select **Edit value** in the Constraint list in the Tasks tab.

**Note:** the constraint tool can also be started with no prior selection, but it will then only work on a single vertex, and reference the constraints to the sketch origin point. By default the command will be in continue mode to create new constraints; press the right mouse button or **ESC** once to quit the command.

## Scripting

The <img alt="" src=images/Sketcher_ConstrainLock.svg  style="width:24px;"> [Lock](Sketcher_ConstrainLock.md) constraint is a GUI command which creates a <img alt="" src=images/Sketcher_ConstrainDistanceX.svg  style="width:24px;"> [Horizontal distance](Sketcher_ConstrainDistanceX.md) and a <img alt="" src=images/Sketcher_ConstrainDistanceY.svg  style="width:24px;"> [Vertical distance](Sketcher_ConstrainDistanceY.md) constraint, it is not a constraint of its own. See the [Sketcher scripting](Sketcher_scripting.md) page for details and examples on how to create these constraints from Python scripts.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainLock/es
