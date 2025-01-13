---
 GuiCommand:
   Name: Sketcher ConstrainLock
   Name/es: Sketcher ConstrainLock
   Workbenches: Sketcher Workbench/es, PartDesign Workbench/es
   MenuLocation: Croquizador , Restricciones del Croquizador  , Bloquear
   SeeAlso: Sketcher_ConstrainBlock/es
---

# Sketcher ConstrainLock/es


</div>




<div class="mw-translate-fuzzy">

\"Crea una restricción de bloqueo sobre el elemento seleccionado\"

## Descripción

Esta restricción trata de restringir completamente cualquier elemento seleccionado.


</div>

The <img alt="" src=images/Sketcher_ConstrainLock.svg  style="width:24px;"> [Sketcher ConstrainLock](Sketcher_ConstrainLock.md) tool applies [Horizontal distance](Sketcher_ConstrainDistanceX.md) and [Vertical distance](Sketcher_ConstrainDistanceY.md) constraints to points. If a single point is selected the constraints reference the origin of the sketch. If two or more points are selected the constraints reference the last point in the selection.




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

See also: [Drawing aids](Sketcher_Workbench#Drawing_aids.md).

### [Continue mode](Sketcher_Workbench#Continue_modes.md) 

1.  Make sure there is no selection.
2.  There are several ways to invoke the tool:
    -   
        <small>(v1.0)</small> 
        
        : If the **Dimensioning constraints** [preference](Sketcher_Preferences#General.md) is set to {{Value|Single tool}} (default): press the down arrow to the right of the **<img src="images/Sketcher_Dimension.svg" width=|x16px><img src="images/Toolbar_flyout_arrow.svg" width=x16px>** button and select the **<img src="images/Sketcher_ConstrainLock.svg" width=16px> Constrain lock** option from the dropdown.

    -   If this preference has a different value (and in {{VersionMinus|0.21}}): press the **<img src="images/Sketcher_ConstrainLock.svg" width=16px> [Constrain lock](Sketcher_ConstrainLock.md)** button.

    -   Select the **Sketch → Sketcher constraints → <img src="images/Sketcher_ConstrainLock.svg" width=16px> Constrain lock** option from the menu.

    -   
        <small>(v1.0)</small> 
        
        : Right-click in the [3D view](3D_view.md) and select the **Dimension → <img src="images/Sketcher_ConstrainLock.svg" width=16px> Constrain lock** option from the context menu.

    -   Use the keyboard shortcut: **K** then **L**.
3.  The cursor changes to a cross with the tool icon.
4.  Select a single point.
5.  Two constraints are added.
6.  Optionally keep creating constraints.
7.  To finish, right-click or press **Esc**, or start another geometry or constraint creation tool.

### Run-once mode 

1.  Select one or more points.
2.  Invoke the tool as explained above.
3.  Depending on the selection two or more constraints are added.

## Notes

-   There is no automatic prompt to edit the constraint values. If required values can be [edited manually](Sketcher_Workbench#Edit_constraints.md).





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainLock/es
