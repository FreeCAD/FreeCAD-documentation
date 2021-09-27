# <img alt="El icono del Ambiente de trabajo Borrador" src=images/Workbench_Draft.svg  style="width:64px;"> Draft Workbench/es


{{TOCright}}

## Introducción

El <img alt="" src=images/Workbench_Draft.svg  style="width:32px;"> **Ambiente de trabajo Borrador** se centra principalmente en la creación y modificación de objetos 2D en FreeCAD. Pero no está restringido al plano XY del sistema global de coordenadas. Sus objetos pueden tener cualquier orientación y posición en el espacio 3D, y algunos objetos de Borrador pueden ser planos o no planos.

Los objetos Borrador se pueden utilizarse para elaboración general, similar a lo que se puede hacer con Inkscape o AutoCAD. Pero también pueden ser la base para la creación de objetos 3D en otros bancos de trabajo. Un [Borrador Hilo](Draft_Wire/es.md) puede definir la trayectoria de un [Arquitectura Muro](Arch_Wall/es.md), un [Borrador Polígono](Draft_Polygon/es.md) puede ser extruido con [Pieza Extrudir](Part_Extrude/es.md), etc. Muchas de las [Borrador herramientas de modificación](#Modificación.md) pueden aplicarse a objetos 2D y 3D creados con otros ambientes de trabajo también. Puedes, por ejemplo, [mover](Draft_Move/es.md) un [Croquis](Sketcher_Workbench/es.md) o crear un [Borrador OrthoArreglo](Draft_OrthoArray/es.md) a partir de un objeto [Pieza](Part_Workbench/es.md).

The Draft Workbench also provides tools to define a [working plane](Draft_SelectPlane.md), a [grid](Draft_Snap_Grid.md), and a [snapping system](Draft_Snap.md) to precisely control the position of geometry.

Si tu objetivo principal es la producción de dibujos 2D complejos y archivos [DXF](DXF/es.md), y no necesitas el modelado 3D, FreeCAD puede no ser la elección correcta para ti. Es posible que desee considerar un programa de software dedicado para el dibujo técnico en su lugar, como [LibreCAD](https://es.wikipedia.org/wiki/LibreCAD) o [QCad](https://es.wikipedia.org/wiki/QCad).

![](images/Draft_Workbench_Example.png ) *The image shows the [grid](Draft_Snap_Grid.md) aligned with the XY plane.<br>
On the left, in white, several planar objects.<br>
On the right a non-planar [Draft Wire](Draft_Wire.md) used as the Path Object of a [Draft PathArray](Draft_PathArray.md).*

## Drafting

-   <img alt="" src=images/Draft_Line.svg  style="width:32px;"> [Line](Draft_Line.md): creates a straight line.

-   <img alt="" src=images/Draft_Wire.svg  style="width:32px;"> [Polyline](Draft_Wire.md): creates a polyline, a sequence of several connected line segments.

-   <img alt="" src=images/Draft_Fillet.svg  style="width:32px;"> _. <small>(v0.19)</small> 

-   <img alt="" src=images/Draft_Arc.svg  style="width:32px;"> Arc tools

:\* <img alt="" src=images/Draft_Arc.svg  style="width:32px;"> [Arc](Draft_Arc.md): creates a circular arc from a center, a radius, a start angle and an aperture angle.

:\* <img alt="" src=images/Draft_Arc_3Points.svg  style="width:32px;"> [Arc by 3 points](Draft_Arc_3Points.md): creates a circular arc from three points that define its circumference. <small>(v0.19)</small> 

-   <img alt="" src=images/Draft_Circle.svg  style="width:32px;"> [Circle](Draft_Circle.md): creates a circle from a center and a radius.

-   <img alt="" src=images/Draft_Ellipse.svg  style="width:32px;"> [Ellipse](Draft_Ellipse.md): creates an ellipse from two points defining a rectangle in which the ellipse will fit.

-   <img alt="" src=images/Draft_Rectangle.svg  style="width:32px;"> [Rectangle](Draft_Rectangle.md): creates a rectangle from two points.

-   <img alt="" src=images/Draft_Polygon.svg  style="width:32px;"> [Polygon](Draft_Polygon.md): creates a regular polygon from a center and a radius.

-   <img alt="" src=images/Draft_BSpline.svg  style="width:32px;"> [B-spline](Draft_BSpline.md): creates a B-spline curve from several points.

-   <img alt="" src=images/Draft_CubicBezCurve.svg  style="width:32px;"> Bézier tools

:\* <img alt="" src=images/Draft_CubicBezCurve.svg  style="width:32px;"> [Cubic Bézier curve](Draft_CubicBezCurve.md): creates a Bézier curve of the third degree. <small>(v0.19)</small> 

:\* <img alt="" src=images/Draft_BezCurve.svg  style="width:32px;"> [Bézier curve](Draft_BezCurve.md): creates a Bézier curve from several points.

-   <img alt="" src=images/Draft_Point.svg  style="width:32px;"> [Point](Draft_Point.md): creates a simple point.

-   <img alt="" src=images/Draft_Facebinder.svg  style="width:32px;"> [Facebinder](Draft_Facebinder.md): creates a surface object from selected faces.

-   <img alt="" src=images/Draft_ShapeString.svg  style="width:32px;"> [ShapeString](Draft_ShapeString.md): creates a compound shape that represents a text string.

## Annotation

-   <img alt="" src=images/Draft_Text.svg  style="width:32px;"> [Text](Draft_Text.md): creates a multi-line text at a given point.

-   <img alt="" src=images/Draft_Dimension.svg  style="width:32px;"> [Dimension](Draft_Dimension.md): creates a linear dimension, a radial dimension or an angular dimension.

-   <img alt="" src=images/Draft_Label.svg  style="width:32px;"> [Label](Draft_Label.md): creates a multi-line text with a 2-segment leader line and an arrow.

-   <img alt="" src=images/Draft_AnnotationStyleEditor.svg  style="width:32px;"> [Annotation styles\...](Draft_AnnotationStyleEditor.md): allows you to define styles that affect the visual properties of annotation-like objects. <small>(v0.19)</small> 

## Modificación

-   <img alt="" src=images/Draft_Move.svg  style="width:32px;"> [Move](Draft_Move.md): moves or copies selected objects from one point to another.

-   <img alt="" src=images/Draft_Rotate.svg  style="width:32px;"> [Rotate](Draft_Rotate.md): rotates or copies selected objects around a center point by a given angle.

-   <img alt="" src=images/Draft_Scale.svg  style="width:32px;"> [Scale](Draft_Scale.md): scales or copies selected objects around a base point.

-   <img alt="" src=images/Draft_Mirror.svg  style="width:32px;"> [Mirror](Draft_Mirror.md): creates mirrored copies from selected objects.

-   <img alt="" src=images/Draft_Offset.svg  style="width:32px;"> [Offset](Draft_Offset.md): offsets each segment of a selected object over a given distance, or creates an offset copy of the selected object.

-   <img alt="" src=images/Draft_Trimex.svg  style="width:32px;"> [Trimex](Draft_Trimex.md): trims or extends a selected object.

-   <img alt="" src=images/Draft_Stretch.svg  style="width:32px;"> [Stretch](Draft_Stretch.md): stretches objects by moving selected points.

-   <img alt="" src=images/Draft_Clone.svg  style="width:32px;"> [Clone](Draft_Clone.md): creates linked copies, clones, of selected objects.

-   <img alt="" src=images/Draft_OrthoArray.svg  style="width:32px;"> Array tools

:\* <img alt="" src=images/Draft_OrthoArray.svg  style="width:32px;"> _ array. <small>(v0.19)</small> 

:\* <img alt="" src=images/Draft_PolarArray.svg  style="width:32px;"> _ array. <small>(v0.19)</small> 

:\* <img alt="" src=images/Draft_CircularArray.svg  style="width:32px;"> _ array. <small>(v0.19)</small> 

:\* <img alt="" src=images/Draft_PathArray.svg  style="width:32px;"> [Path array](Draft_PathArray.md): creates an array from a selected object by placing copies along a path.

:\* <img alt="" src=images/Draft_PathLinkArray.svg  style="width:32px;"> _ array instead of a regular array. <small>(v0.19)</small> 

:\* <img alt="" src=images/Draft_PointArray.svg  style="width:32px;"> [Point Array](Draft_PointArray.md): creates an array from a selected object by placing copies at the points from a point compound.

:\* <img alt="" src=images/Draft_PointLinkArray.svg  style="width:32px;"> _ array instead of a regular array. <small>(v0.19)</small> 

-   <img alt="" src=images/Draft_Edit.svg  style="width:32px;"> [Edit](Draft_Edit.md): puts selected objects in Draft Edit mode. In this mode the properties of objects can be edited graphically.

-   <img alt="" src=images/Draft_SubelementHighlight.svg  style="width:32px;"> [Subelement highlight](Draft_SubelementHighlight.md): temporarily highlights selected objects, or the base objects of selected objects.

-   <img alt="" src=images/Draft_Join.svg  style="width:32px;"> _ and [Draft Wires](Draft_Wire.md) into a single wire.

-   <img alt="" src=images/Draft_Split.svg  style="width:32px;"> _ or [Draft Wire](Draft_Wire.md) at a specified point or edge.

-   <img alt="" src=images/Draft_Upgrade.svg  style="width:32px;"> [Upgrade](Draft_Upgrade.md): upgrades selected objects.

-   <img alt="" src=images/Draft_Downgrade.svg  style="width:32px;"> [Downgrade](Draft_Downgrade.md): downgrades selected objects.

-   <img alt="" src=images/Draft_WireToBSpline.svg  style="width:32px;"> _ to [Draft BSplines](Draft_BSpline.md) and vice versa.

-   <img alt="" src=images/Draft_Draft2Sketch.svg  style="width:32px;"> _ objects to [Sketcher Sketches](Sketcher_NewSketch.md) and vice versa.

-   <img alt="" src=images/Draft_Slope.svg  style="width:32px;"> _ or [Draft Wires](Draft_Wire.md) by increasing, or decreasing, the Z coordinate of all points after the first one.

-   <img alt="" src=images/Draft_FlipDimension.svg  style="width:32px;"> _ 180° around the dimension line.

-   <img alt="" src=images/Draft_Shape2DView.svg  style="width:32px;"> [Shape 2D view](Draft_Shape2DView.md): creates 2D projections from selected objects.

## Borrador Bandeja 

La [Borrador Bandeja](Draft_Tray/es.md) Barra herramienta aparece cuando se inicia el ambiente de trabajo, y permite seleccionar el plano de trabajo, junto con algunas propiedades visuales como el color de la línea, el color de la forma, el ancho de la línea, el tamaño del texto y el grupo automático.

![](images/Draft_tray_default.png )


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Draft_SelectPlane.svg  style="width:32px;"> [Plano Trabajo](Draft_SelectPlane/es.md): establece un plano de trabajo desde una vista estándar o una cara seleccionada.
-   <img alt="" src=images/Draft_SetStyle.svg  style="width:32px;"> [Establece estilo](Draft_SetStyle/es.md): establece el estilo por defecto para los nuevos objetos, y opcionalmente aplica el estilo a los objetos y grupos seleccionados.
-   <img alt="" src=images/Draft_ToggleConstructionMode.svg  style="width:32px;"> [Modo de construcción](Draft_ToggleConstructionMode/es.md): activa o desactiva el modo de construcción Borrador.
-   <img alt="" src=images/Draft_AutoGroup.svg  style="width:32px;"> _, <img alt="" src=images/Draft_Layer.svg  style="width:32px;"> _. {{Version/es|0.17}}


</div>

-   ![](images/Draft_tray_button_style.png ) [Set style](Draft_SetStyle.md): sets the default style for new objects. Also available in the menu: **Draft → Utilities → <img src="images/Draft_SetStyle.svg" width=16px> Set style**. <small>(v0.19)</small> 

-   ![](images/Draft_tray_button_construction.png ) [Toggle construction mode](Draft_ToggleConstructionMode.md): switches Draft construction mode on or off. Also available in the menu: **Draft → Utilities → <img src="images/Draft_ToggleConstructionMode.svg" width=16px> Toggle construction mode**.

-   !_ or, optionally, the active [Std Group](Std_Group.md) or group-like [Arch](Arch_Workbench.md) object.

## Borrador Widget escala de anotacion 

With the [Draft annotation scale widget](Draft_annotation_scale_widget.md) the Draft annotation scale can be specified. <small>(v0.19)</small> 

![](images/Draft_annotation_scale_widget_button.png )

## Borrador Widget Atrapar 

The [Draft snap widget](Draft_snap_widget.md) can be used as an alternative for the [Draft Snap toolbar](#Draft_Snap_toolbar.md). <small>(v0.19)</small> 

![](images/Draft_snap_widget_button.png )

## Borrador Barra de herramientas Atrapar 

La barra de herramientas [Borrador Atrapar](Draft_Snap/es.md) permite seleccionar el modo de ajuste actual. Su botón se mantiene pulsado cuando un modo está activo.

-   <img alt="" src=images/Draft_Snap_Lock.svg  style="width:32px;"> [Snap Lock](Draft_Snap_Lock.md): enables or disables snapping globally.

-   <img alt="" src=images/Draft_Snap_Endpoint.svg  style="width:32px;"> [Snap Endpoint](Draft_Snap_Endpoint.md): snaps to the endpoints of edges.

-   <img alt="" src=images/Draft_Snap_Midpoint.svg  style="width:32px;"> [Snap Midpoint](Draft_Snap_Midpoint.md): snaps to the midpoint of straight and circular edges.

-   <img alt="" src=images/Draft_Snap_Center.svg  style="width:32px;"> _ and [Arch BuildingParts](Arch_BuildingPart.md).

-   <img alt="" src=images/Draft_Snap_Angle.svg  style="width:32px;"> [Snap Angle](Draft_Snap_Angle.md): snaps to the special cardinal points on circular edges, at multiples of 30° and 45°.

-   <img alt="" src=images/Draft_Snap_Intersection.svg  style="width:32px;"> [Snap Intersection](Draft_Snap_Intersection.md): snaps to the intersection of two edges.

-   <img alt="" src=images/Draft_Snap_Perpendicular.svg  style="width:32px;"> [Snap Perpendicular](Draft_Snap_Perpendicular.md): snaps to the perpendicular point on edges.

-   <img alt="" src=images/Draft_Snap_Extension.svg  style="width:32px;"> [Snap Extension](Draft_Snap_Extension.md): snaps to an imaginary line that extends beyond the endpoints of straight edges.

-   <img alt="" src=images/Draft_Snap_Parallel.svg  style="width:32px;"> [Snap Parallel](Draft_Snap_Parallel.md): snaps to an imaginary line parallel to straight edges.

-   <img alt="" src=images/Draft_Snap_Special.svg  style="width:32px;"> [Snap Special](Draft_Snap_Special.md): snaps to special points defined by the object.

-   <img alt="" src=images/Draft_Snap_Near.svg  style="width:32px;"> [Snap Near](Draft_Snap_Near.md): snaps to the nearest point on faces or edges.

-   <img alt="" src=images/Draft_Snap_Ortho.svg  style="width:32px;"> [Snap Ortho](Draft_Snap_Ortho.md): snaps to imaginary lines that cross the previous point at 0°, 45°, 90° and 135°.

-   <img alt="" src=images/Draft_Snap_Grid.svg  style="width:32px;"> [Snap Grid](Draft_Snap_Grid.md): snaps to the intersections of grid lines.

-   <img alt="" src=images/Draft_Snap_WorkingPlane.svg  style="width:32px;"> _.

-   <img alt="" src=images/Draft_Snap_Dimensions.svg  style="width:32px;"> [Snap Dimensions](Draft_Snap_Dimensions.md): shows temporary X and Y dimensions.

-   <img alt="" src=images/Draft_ToggleGrid.svg  style="width:32px;"> [Toggle Grid](Draft_ToggleGrid.md): switches the grid on or off.

## Borrador Herramientas de utilidad 

-   <img alt="" src=images/Draft_Layer.svg  style="width:32px;"> _. <small>(v0.19)</small> 

-   <img alt="" src=images/Draft_WorkingPlaneProxy.svg  style="width:32px;"> _.

-   <img alt="" src=images/Draft_ToggleDisplayMode.svg  style="width:32px;"> [Toggle normal/wireframe display](Draft_ToggleDisplayMode.md): switches the **Display Mode** property of selected objects between {{Value|Flat Lines}} and {{Value|Wireframe}}.

-   <img alt="" src=images/Draft_AddToGroup.svg  style="width:32px;"> _. It can also ungroup objects.

-   <img alt="" src=images/Draft_SelectGroup.svg  style="width:32px;"> _, [Std Groups](Std_Group.md) or group-like [Arch](Arch_Workbench.md) objects.

-   <img alt="" src=images/Draft_AddConstruction.svg  style="width:32px;"> _.

## Herramientas adicionales 

Herramientas adicionales disponibles desde el menú **Bosquejo → Utilidades**, o a través del menú contextual del botón derecho, dependiendo de los objeto seleccionados.

-   <img alt="" src=images/Draft_Heal.svg  style="width:32px;"> [Heal](Draft_Heal.md): heals problematic Draft objects found in very old files.

-   <img alt="" src=images/Draft_ToggleContinueMode.svg  style="width:32px;"> [Toggle continue mode](Draft_ToggleContinueMode.md): switches continue mode on or off.

-   <img alt="" src=images/Draft_ApplyStyle.svg  style="width:32px;"> [Apply current style](Draft_ApplyStyle.md): applies the current style settings to selected objects.

-   <img alt="" src=images/Draft_ShowSnapBar.svg  style="width:32px;"> _.

## Características adicionales 


<div class="mw-translate-fuzzy">

-   [Coordinates](Draft_Coordinates/es.md): introducir coordenadas en lugar de hacer clic en la vista 3D para definir un nuevo punto.
-   [Restricción](Draft_Constrain/es.md): limitar el puntero a movimientos horizontales o verticales en relación con un punto previo.
-   [Ajuste](Draft_Snap/es.md): colocar nuevos puntos en lugares especiales de los objetos existentes o en la cuadrícula.
-   [Modo de copia](Draft_Copying/es.md): Todas las herramientas de modificación pueden modificar los objetos seleccionados o crear una copia modificada de los mismos. Si se mantiene pulsada la tecla **Alt** mientras se modifica el objeto, por ejemplo, moviéndolo o rotándolo, se crea una copia cuando se suelta la tecla.
-   [Modo de construcción](Draft_ToggleConstructionMode/es.md): Permite crear geometrías separadas del resto, simplemente activándolas y desactivándolas.
-   [Plano de trabajo](Draft_SelectPlane/es.md): permite seleccionar una superficie sobre la que construir las formas.


</div>

## Menú contextual de vista de árbol 

The following additional options are available in the [Tree view](Tree_view.md) context menu:

### Opciones de selección 

If there is a selection the context menu contains one additional sub-menu:

-    **Utilities**: a subset of the tools available in the main Draft Utilities menu.

### Opciones Hilos 

For a [Draft Wire](Draft_Wire.md), [Draft BSpline](Draft_BSpline.md), [Draft CubicBezCurve](Draft_CubicBezCurve.md) and [Draft BezCurve](Draft_BezCurve.md) this additional option is available:

-   <img alt="" src=images/Draft_Edit.svg  style="width:32px;"> Flatten this wire: flattens the wire based on its internal geometry. This option currently does not work properly.

### Opciones contenedor capas 

For a [Draft LayerContainer](Draft_Layer.md) these additional options are available:

-   <img alt="" src=images/Draft_Layer.svg  style="width:32px;"> Merge layer duplicates: this option currently does not work.

-   <img alt="" src=images/Draft_NewLayer.svg  style="width:32px;"> [Add new layer](Draft_Layer.md): adds a new layer to the current document.

### Opciones capa 

For a [Draft Layer](Draft_Layer.md) these additional options are available:

-   <img alt="" src=images/button_right.svg  style="width:32px;"> [Activate this layer](Draft_AutoGroup.md): activates the selected layer.

-   <img alt="" src=images/Draft_SelectGroup.svg  style="width:32px;"> [Select layer contents](Draft_SelectGroup.md): selects the objects inside the selected layer.

### Plano trabajo opciones proxy 

For a [Draft WorkingPlaneProxy](Draft_WorkingPlaneProxy.md) these additional options are available:

-   <img alt="" src=images/Draft_SelectPlane.svg  style="width:32px;"> _ camera settings.

-   <img alt="" src=images/Draft_SelectPlane.svg  style="width:32px;"> [Write objects state](Draft_WorkingPlaneProxy#Context_menu.md): updates the **Visibility Map** property of the working plane proxy with the current visibility state of objects in the document.

## 3D vista menú contextual 

The following additional options are available in the [3D view](3D_view.md) context menu:

### Opciones no-selección 

If there is no selection the context menu contains one additional sub-menu:

-    **Utilities**: a subset of the tools available in the main Draft Utilities menu.

### Opciones de selección 

If there is a selection the context menu contains two additional sub-menus:

-    **Draft**: tools for [drawing objects](#Drafting.md) and [modifying objects](#Modification.md).

-    **Utilities**: a subset of the tools available in the main Draft Utilities menu.

## Herramientas obsoletas 

Estas herramientas se eliminaron de la interfaz en la v0.19 porque ya no tenían ninguna utilidad.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Draft_VisGroup.svg  style="width:32px;"> _. {{Obsoleto/es|0.19}}
-   <img alt="" src=images/Draft_FinishLine.svg  style="width:32px;"> \[\[Draft\_FinishLine/es\|

Finalización línea\]\]: termina el dibujo del [Borrador Alambre](Draft_Wire/es.md) o [Borrador BSpline](Draft_BSpline/es.md) actual, sin cerrarlo. {{Obsoleto/es|0.19}}{{Obsolete/es|0.19}}

-   <img alt="" src=images/Draft_CloseLine.svg  style="width:32px;"> _ o [Borrador BSpline](Draft_BSpline/es.md) actual, y lo cierra. {{Obsoleto/es|0.19}}
-   <img alt="" src=images/Draft_UndoLine.svg  style="width:32px;"> _. {{Obsoleto/es|0.19}}


</div>

-   <img alt="" src=images/Draft_Drawing.svg  style="width:32px;"> _ page. {{Obsolete|0.17}}

These [3D view](3D_view.md) context menu options are still available when the [Draft Wire](Draft_Wire.md), [Draft BSpline](Draft_BSpline.md), [Draft CubicBezCurve](Draft_CubicBezCurve.md) or [Draft BezCurve](Draft_BezCurve.md) command is active but will be removed in the near future:

-   <img alt="" src=images/Draft_UndoLine.svg  style="width:32px;"> [Undo last segment](Draft_Wire#Options.md): use the {{button|<img src="images/Draft_UndoLine.svg" width=16px> Undo}} button in the task panel of the command instead. {{Obsolete|0.20}}

-   <img alt="" src=images/Draft_FinishLine.svg  style="width:32px;"> [Finish line](Draft_Wire#Options.md): use the **<img src="images/Draft_FinishLine.svg" width=16px> Finish** button in the task panel of the command instead. {{Obsolete|0.20}}

-   <img alt="" src=images/Draft_CloseLine.svg  style="width:32px;"> [Close line](Draft_Wire#Options.md): use the **<img src="images/Draft_CloseLine.svg" width=16px> Close** button in the task panel of the command instead. {{Obsolete|0.20}}

## Preferencias


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Preferences-draft.svg  style="width:32px;"> [Preferencias](Draft_Preferences/es.md): preferencias generales para el plano de trabajo y las herramientas de dibujo.
-   <img alt="" src=images/Preferences-import-export.svg  style="width:32px;"> [Preferencias de importación y exportación](Import_Export_Preferences/es.md): preferencias disponibles para importar desde y exportar a diferentes formatos de archivo.


</div>

-   <img alt="" src=images/Preferences-import-export.svg  style="width:32px;"> [Import Export Preferences](Import_Export_Preferences.md): preferences available for importing from and exporting to different file formats.

## Formatos de archivo 


<div class="mw-translate-fuzzy">

Son funciones para abrir, importar o exportar otros formatos de archivo. Abrir abrirá un nuevo documento con el contenido del archivo, mientras que importar añadirá el contenido del archivo al documento actual. Exportar guardará los objetos seleccionados en un archivo. Si no se selecciona nada, se exportarán todos los objetos. Tenga en cuenta que el propósito del Módulo Borrador es trabajar con objetos 2D, por lo que esas rutinas de importación se centran sólo en objetos 2D, y aunque los formatos DXF y OCA también soportan definiciones de objetos en el espacio 3D (los objetos no son necesariamente planos), no importarán objetos volumétricos como mallas, superficies 3D, etc., sino líneas, círculos, textos o formas planas. Los formatos de archivo actualmente soportados son: El módulo Borrador proporciona a FreeCAD importadores y exportadores para los siguientes formatos de archivo:


</div>


<div class="mw-translate-fuzzy">

-   _.
-   _ está instalada. Ver también [FreeCAD y DWG Importación](FreeCAD_y_DWG_Import/es.md).
-   [SVG (como geometría)](Draft_SVG/es.md): importa y exporta archivos [Scalable Vector Graphics](http://en.wikipedia.org/wiki/Scalable_Vector_Graphics) creados con aplicaciones de dibujo vectoriales
-   [Open Cad format .OCA](Draft_OCA/es.md): importa y exporta archivos OCA/GCAD, un potencialmente nuevo [formato de archivo abierto para CAD](http://groups.google.com/group/open_cad_format)
-   [Ala Data Format .DAT](Draft_DAT/es.md): importa archivos DAT describiendo [Ala perfiles](http://www.ae.illinois.edu/m-selig/ads/coord_database.html)


</div>

## Pruebas unitarias 


<div class="mw-translate-fuzzy">


**Véase también:**

[Ambiente de trabajo Prueba](Test_Workbench/es.md).


</div>


<div class="mw-translate-fuzzy">

Para ejecutar las pruebas unitarias del banco de trabajo, ejecute lo siguiente desde el terminal del sistema operativo.


</div>


```python
freecad -t TestDraft
```

## Guionización


<div class="mw-translate-fuzzy">

Las herramientas de Bosquejo pueden utilizarse en [macros](macros/es.md) y desde la [Python](Python/es.md) consola utilizando la [Bosquejo API](Draft_API/es.md).


</div>

El ambiente de trabajo incluye un módulo para crear muestras de todos los objetos en un nuevo documento. {{Version/es|0.19}}


<div class="mw-translate-fuzzy">

Utilícelo para comprobar que todos los objetos se producen correctamente.


</div>


```python
import drafttests.draft_test_objects as dto
doc = dto.create_test_file()
```


<div class="mw-translate-fuzzy">

Inspeccionar el código de este módulo es útil para entender cómo utilizar la interfaz de programación.


</div>

<img alt="" src=images/Draft_test_objects.png  style="width:500px;">


<div class="mw-translate-fuzzy">


*Test objects for the [Ambiente de trabajo Borrador](Draft_Workbench/de.md).*


</div>

## Tutoriales

-   [Borrador Tutorial](Draft_tutorial/es.md)
-   [Borrador FormaCadena Tutorial](Draft_ShapeString_tutorial/es.md)





 

_

---
[documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > Draft Workbench/es
