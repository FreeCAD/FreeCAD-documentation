---
- GuiCommand:/es
   Name:Sketcher AlterConstruction
   Name/es:Alternar geometría de construcción
   Icon:Sketcher_AlterConstruction.svg
   Workbenches:[Croquizador](Sketcher_Workbench/es.md)
   MenuLocation:Sketch → Geometrías de croquis → Alternar geometría de construcción
---

# Sketcher ToggleConstruction/es


</div>

## Descripción

Esta herramienta conmuta el modo de construcción de la geometría del Croquizador. Se puede utilizar sobre cualquier tipo de geometría: Línea, arco o circunferencia.

La geometría de Construcción es una importante herramienta del Croquizador. Cuando se utiliza un croquis para una operación 3D, la geometría de Construcción es ignorada.


<div class="mw-translate-fuzzy">

En el modo de edición del croquis, la geometría de construcción se muestra en color azul, y no se puede volver verde cuando un croquis está completamente definido. Una vez que salgas del modo de croquis, la geometría de Construcción se ocultará en la pantalla.


</div>


<div class="mw-translate-fuzzy">

Las líneas de Construcción se pueden utilizar como ejes de rotación para la operación de [Revolución](PartDesign_Revolution/es.md).


</div>

<img alt="" src=images/Sketcher_ConstructionMode_fr_01.png  style="width:480px;">


<div class="mw-translate-fuzzy">

## Utilización


</div>


<div class="mw-translate-fuzzy">

-   Selecciona una o más geometrías del croquis en la vista 3D, pulsa en la herramienta o selecciónala a través del menú.


</div>

## Ejemplo

Use Construction mode on some sketch elements,

<img alt="" src=images/Sketcher_ConstructionMode_fr_01.png  style="width:450px;">

and once you **[<img src=images/Sketcher_LeaveSketch.svg style="width:16px"> [leave the sketcher editing mode](Sketcher_LeaveSketch.md)**, geometry that was turned into construction have become invisible in the [3D view](3D_view.md) (but are still present in the Sketcher editing mode).

<img alt="" src=images/Sketcher_ConstructionMode_fr_02.png  style="width:450px;">

## Notes

-    **[<img src=images/Sketcher_CreatePoint.svg style="width:16px"> [Create Point](Sketcher_CreatePoint.md)**will always create points in construction mode regardless of the toolbar toggle state, select the desired points in the [3D view](3D_view.md) after creation and click **[<img src=images/Sketcher_ToggleConstruction.svg style="width:16px"> [Toggle construction](Sketcher_ToggleConstruction.md)** to change them to normal geometry. <small>(v0.19)</small> 


<div class="mw-translate-fuzzy">


</div>


{{Sketcher Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ToggleConstruction/es
