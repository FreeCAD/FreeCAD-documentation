


 

<img alt="El icono del Ambiente de trabajo Borrador" src=images/Workbench_Draft.svg  style="width:128px;">


{{TOCright}}

## Introducción

El <img alt="" src=images/Workbench_Draft.svg  style="width:32px;"> [Ambiente de trabajo borrador](Draft_Module/es.md) permite dibujar objetos 2D simples, y ofrecer diversas herramientas para poderlas modificar después. También proporciona herramientas para definir un plano de trabajo, una cuadrícula y un sistema de enganche para controlar con precisión la posición de su geometría.

Los objetos 2D creados pueden utilizarse para el dibujo general de forma similar a como se hace con Inkscape o Autocad. Estas formas 2D también pueden utilizarse como componentes base de objetos 3D creados con otros Ambientes de trabajo, por ejemplo, el <img alt="" src=images/Workbench_Part.svg  style="width:32px;"> [Pieza](Part_Workbench/es.md) y <img alt="" src=images/Workbench_Arch.svg  style="width:32px;"> [Ambiente de trabajo Arquitectura](Arch_Workbench/es.md). Conversión de objetos de Borrador a <img alt="" src=images/Workbench_Sketcher.svg  style="width:32px;"> [Bocetos](Sketcher_Workbench/es.md) también es posible, lo que significa que las formas también se pueden utilizar con el <img alt="" src=images/Workbench_PartDesign.svg  style="width:32px;"> [Ambiente de trabajo Diseño Piezas](PartDesign_Workbench/es.md) para la creación de cuerpos sólidos.

FreeCAD es principalmente una aplicación de modelado 3D, y por lo tanto sus herramientas 2D no son tan avanzadas como en otros programas de dibujo. Si tu objetivo principal es la producción de dibujos 2D complejos y archivos [DXF](DXF/es.md), y no necesitas el modelado 3D, puedes considerar un programa dedicado al dibujo técnico como [LibreCAD](https://en.wikipedia.org/wiki/LibreCAD), [QCad](https://en.wikipedia.org/wiki/QCad), u otros.

<img alt="Draft Workbench Example" src=images/Draft_Workbench_Example.png  style="width:400px;">

## Dibujando objetos 

Estas son las herramientas para crear objetos.

-   <img alt="" src=images/Draft_Line.svg  style="width:32px;"> [Línea](Draft_Line/es.md): Dibuja un segmento de línea entre dos puntos
-   <img alt="" src=images/Draft_Wire.svg  style="width:32px;"> [Polilínea](Draft_Wire/es.md): Dibuja una línea formada por múltiples segmentos de línea (polilínea).
-   <img alt="" src=images/Draft_Fillet.svg  style="width:32px;"> [Redondeado](Draft_Fillet/es.md): dibuja un filete (esquina redondeada) o un chaflán (línea recta) entre dos [Líneas](Draft_Line/es.md) simples. {{Version/es|0.19}}
-   <img alt="" src=images/Draft_Arc.svg  style="width:32px;"> [Arco](Draft_Arc/es.md): Dibuja un segmento de arco a partir del centro, radio, ángulo inicio y ángulo final.
-   <img alt="" src=images/Draft_Arc_3Points.svg  style="width:32px;"> [Arco 3Puntos](Draft_Arc_3Points/es.md): dibuja un segmento de arco circular a partir de tres puntos que se encuentran en la circunferencia. {{Version/es|0.19}}
-   <img alt="" src=images/Draft_Circle.svg  style="width:32px;"> [Círculo](Draft_Circle/es.md): Dibuja una círculo a partir de su centro y radio
-   <img alt="" src=images/Draft_Ellipse.svg  style="width:32px;"> [Elipse](Draft_Ellipse/es.md): Dibuja una elipse a partir de dos puntos de esquina
-   <img alt="" src=images/Draft_Rectangle.svg  style="width:32px;"> [Rectángulo](Draft_Rectangle/es.md): dibuja un rectángulo a partir de dos puntos de esquina.
-   <img alt="" src=images/Draft_Polygon.svg  style="width:32px;"> [Polígono](Draft_Polygon/es.md): dibuja un polígono regular a partir del centro, el radio y el número de lados.
-   <img alt="" src=images/Draft_BSpline.svg  style="width:32px;"> [BSpline](Draft_BSpline/es.md): Dibuja una B-Spline a partir de una serie de puntos

-   <img alt="" src=images/Draft_CubicBezCurve.svg  style="width:32px;"> [Curva cúbica de Bézier](Draft_CubicBezCurve/es.md): dibuja una curva de Bézier de tercer grado arrastrando dos puntos. {{Version/es|0.19}}
-   <img alt="" src=images/Draft_BezCurve.svg  style="width:32px;"> [Curva de Bézier](Draft_BezCurve/es.md): dibuja una curva de Bézier a partir de una serie de puntos.
-   <img alt="" src=images/Draft_Point.svg  style="width:32px;"> [Punto](Draft_Point/es.md): inserta un objeto de punto.
-   <img alt="" src=images/Draft_Facebinder.svg  style="width:32px;"> [LadoLazo](Draft_Facebinder/es.md): crea un nuevo objeto a partir de las caras seleccionadas en los objetos existentes.
-   <img alt="" src=images/Draft_ShapeString.svg  style="width:32px;"> [CadenaForma](Draft_ShapeString/es.md): inserta una forma compuesta que representa una cadena de texto en un punto determinado.

## Objetos de anotación 

-   <img alt="" src=images/Draft_Text.svg  style="width:32px;"> [Texto](Draft_Text/es.md): dibuja una anotación de texto de varias líneas.
-   <img alt="" src=images/Draft_Dimension.svg  style="width:32px;"> [Dimensión](Draft_Dimension/es.md): dibuja una anotación de dimensión.

-   <img alt="" src=images/Draft_Label.svg  style="width:32px;"> [Etiqueta](Draft_Label/es.md): coloca una etiqueta con una flecha que apunta a un elemento seleccionado. {{Version/es|0.17}}
-   <img alt="" src=images/Draft_AnnotationStyleEditor.svg  style="width:32px;"> [Editor de estilo anotación](Draft_AnnotationStyleEditor/es.md): abre un editor para cambiar el estilo de anotación de estos objetos. {{Version/es|0.19}}

## Modificando objetos 

Estas son las herramientas para la edición de los objetos existentes. Trabajan sobre los objetos seleccionados, pero si no hay ningún objeto seleccionado, permiten seleccionar uno.

Muchas herramientas de operación (mover, rotar, matriz, etc.) también funcionan en objetos sólidos ([Pieza](Part_Workbench/es.md), [DiseñoPiezas](PartDesign_Workbench/es.md), [Arquitectura](Arch_Workbench/es.md), etc.).

-   <img alt="" src=images/Draft_Move.svg  style="width:32px;"> [Desplazar](Draft_Move/es.md): Desplaza objeto(s) desde una ubicación a otra
-   <img alt="" src=images/Draft_Rotate.svg  style="width:32px;"> [Girar](Draft_Rotate/es.md): Gira objeto(s) desde un ángulo de inicio a un ángulo final
-   <img alt="" src=images/Draft_Scale.svg  style="width:32px;"> [Escala](Draft_Scale/es.md): escala los objetos seleccionados alrededor de un punto base.
-   <img alt="" src=images/Draft_Mirror.svg  style="width:32px;"> [Reflejar](Draft_Mirror/es.md): refleja los objetos seleccionados.
-   <img alt="" src=images/Draft_Offset.svg  style="width:32px;"> [Desplazamiento](Draft_Offset/es.md): desplaza segmentos de un objeto una determinada distancia.
-   <img alt="" src=images/Draft_Trimex.svg  style="width:32px;"> [Recortar/Extender (Trimex)](Draft_Trimex/es.md): recorta o extiende un objeto.
-   <img alt="" src=images/Draft_Stretch.svg  style="width:32px;"> [Estirar](Draft_Stretch/es.md): estira los objetos seleccionados. {{Version/es|0.17}}

-   <img alt="" src=images/Draft_Clone.svg  style="width:32px;"> [Clon](Draft_Clone/es.md): clona los objetos seleccionados.
-   <img alt="" src=images/Draft_Array.svg  style="width:32px;"> Herramientas de los arreglos
    -   <img alt="" src=images/Draft_OrthoArray.svg  style="width:32px;"> [Arreglo ortogonal](Draft_OrthoArray/es.md): crea un arreglo ortogonal a partir del objeto seleccionado. También puede crear copias de [Enlace a la aplicación](App_Link/es.md). {{Version/es|0.19}}
    -   <img alt="" src=images/Draft_PolarArray.svg  style="width:32px;">[Arreglo polar](Draft_PolarArray/es.md): crea un arreglo en un patrón polar, es decir, barriendo un ángulo. También puede crear copias de [Enlace de aplicación](App_Link/es.md). {{Version/es|0.19}}
    -   <img alt="" src=images/Draft_CircularArray.svg  style="width:32px;"> [Arreglo circular](Draft_CircularArray/es.md): crea un arreglo en forma circular, es decir, partiendo de un centro y moviéndose radialmente hacia afuera. También puede crear copias de [Enlace de aplicación](App_Link/es.md). {{Version/es|0.19}}
    -   <img alt="" src=images/Draft_PathArray.svg  style="width:32px;"> [Arreglo Ruta](Draft_PathArray/es.md): crea una arreglo de objetos colocando las copias a lo largo de una ruta.
    -   <img alt="" src=images/Draft_PointArray.svg  style="width:32px;"> [Arreglo de puntos](Draft_PointArray/es.md): crea una arreglo de objetos colocando las copias en determinados puntos. {{Version/es|0.18}}
    -   <img alt="" src=images/Draft_PointLinkArray.svg  style="width:32px;"> [Arreglo de enlaces puntos](Draft_PointLinkArray/es.md): como <img alt="" src=images/Draft_PointArray.svg  style="width:32px;"> [Arreglo de puntos](Draft_PointArray/es.md), pero crea [Enlaces de aplicación](App_Link/es.md) en lugar de copias normales. {{Version/es|0.19}}

-   <img alt="" src=images/Draft_Edit.svg  style="width:32px;"> [Editar](Draft_Edit/es.md): edita un objeto seleccionado.
-   <img alt="" src=images/Draft_SubelementHighlight.svg  style="width:32px;"> [Resaltar subelemento](Draft_SubelementHighlight/es.md): entra en un modo de edición que permite editar diferentes objetos. {{Version/es|0.19}}

-   <img alt="" src=images/Draft_Join.svg  style="width:32px;"> [Unir](Draft_Join/es.md): une las líneas en un solo hilo. {{Version/es|0.18}}
-   <img alt="" src=images/Draft_Split.svg  style="width:32px;"> [Dividir](Draft_Split/es.md): divide un cable en dos en un punto. {{Version/es|0.18}}
-   <img alt="" src=images/Draft_Upgrade.svg  style="width:32px;"> [Elevar](Draft_Upgrade/es.md): eleva objetos en un objeto de nivel superior.
-   <img alt="" src=images/Draft_Downgrade.svg  style="width:32px;"> [Rebajarl](Draft_Downgrade/es.md): rebaja objetos a un nivel inferior.

-   <img alt="" src=images/Draft_WireToBSpline.svg  style="width:32px;"> [Alambre a BSpline](Draft_WireToBSpline/es.md): convierte un alambre en una B-Spline y viceversa.
-   <img alt="" src=images/Draft_Draft2Sketch.svg  style="width:32px;"> [Borrador a Sketch](Draft_Draft2Sketch/es.md): convierte un objeto Borrador en un [Ambiente de trabajo Croquizador](Sketcher_Workbench/es.md) boceto y viceversa.
-   <img alt="" src=images/Draft_Slope.svg  style="width:32px;"> [Slope](Draft_Slope/es.md): cambia la pendiente de elevación de la [Borrador Linea](Draft_Line/es.md) o [Borrador Alambre](Draft_Wire/es.md) actualmente seleccionada. {{Version/es|0.17}}
-   <img alt="" src=images/Draft_FlipDimension.svg  style="width:32px;"> [Deslizar Dimensión](Draft_FlipDimension/es.md): invierte la orientación del texto de un [Borrador Dimensión](Draft_Dimension/es.md).

-   <img alt="" src=images/Draft_Shape2DView.svg  style="width:32px;"> [Forma Vista 2D](Draft_Shape2DView/es.md): crea un objeto 2D que es una vista 2D aplanada de un objeto 3D.

## Borrador Bandeja 

La [Borrador Bandeja](Draft_Tray/es.md) Barra herramienta aparece cuando se inicia el ambiente de trabajo, y permite seleccionar el plano de trabajo, junto con algunas propiedades visuales como el color de la línea, el color de la forma, el ancho de la línea, el tamaño del texto y el grupo automático.

![](images/Draft_tray_default.png )

Its tools are also available in the **Draft → Utilities** menu:

-   <img alt="" src=images/Draft_SelectPlane.svg  style="width:32px;"> [Plano Trabajo](Draft_SelectPlane/es.md): establece un plano de trabajo desde una vista estándar o una cara seleccionada.
-   <img alt="" src=images/Draft_SetStyle.svg  style="width:32px;"> [Establece estilo](Draft_SetStyle/es.md): establece el estilo por defecto para los nuevos objetos, y opcionalmente aplica el estilo a los objetos y grupos seleccionados.
-   <img alt="" src=images/Draft_ToggleConstructionMode.svg  style="width:32px;"> [Modo de construcción](Draft_ToggleConstructionMode/es.md): activa o desactiva el modo de construcción Borrador.
-   <img alt="" src=images/Draft_AutoGroup.svg  style="width:32px;"> [AutoGrupo](Draft_AutoGroup/es.md): coloca automáticamente los nuevos objetos en un determinado <img alt="" src=images/Std_Group.svg  style="width:32px;"> [Grupo Std](Std_Group/es.md), <img alt="" src=images/Draft_Layer.svg  style="width:32px;"> [Capa de Borrador](Draft_Layer/es.md), o uno de los objetos tipo grupo del [Am iente de Trabajo Arquitectura](Arch_Workbench/es.md), como <img alt="" src=images/Arch_BuildingPart.svg  style="width:32px;"> [Arquitectura EdificarPieza](Arch_BuildingPart/es.md). {{Version/es|0.17}}

-   <img alt="" src=images/Draft_SetStyle.svg  style="width:32px;"> [Set style](Draft_SetStyle.md): sets the default style for new objects. <small>(v0.19)</small> 

-   <img alt="" src=images/Draft_ToggleConstructionMode.svg  style="width:32px;"> [Toggle construction mode](Draft_ToggleConstructionMode.md): switches Draft construction mode on or off.

-   <img alt="" src=images/Draft_AutoGroup.svg  style="width:32px;"> [AutoGroup](Draft_AutoGroup.md): changes the active [Draft Layer](Draft_Layer.md) or, optionally, the active [Std Group](Std_Group.md) or group-like [Arch](Arch_Workbench.md) object.

## Borrador Widget escala de anotacion 

With the [Draft annotation scale widget](Draft_annotation_scale_widget.md) the Draft annotation scale can be specified. <small>(v0.19)</small> 

![](images/Draft_annotation_scale_widget_button.png )

## Borrador Widget Atrapar 

The [Draft snap widget](Draft_snap_widget.md) can be used as an alternative for the [Draft Snap toolbar](#Draft_snap_toolbar.md). <small>(v0.19)</small> 

![](images/Draft_snap_widget_button.png )

## Borrador Barra de herramientas Atrapar 

La barra de herramientas [Borrador Atrapar](Draft_Snap/es.md) permite seleccionar el modo de ajuste actual. Su botón se mantiene pulsado cuando un modo está activo.

-   <img alt="" src=images/Draft_Snap_Lock.svg  style="width:32px;"> [Toggle snap](Draft_Snap_Lock.md): toggles [object snapping](Draft_Snap.md) globally on or off.
-   <img alt="" src=images/Draft_Snap_Endpoint.svg  style="width:32px;"> [Endpoint](Draft_Snap_Endpoint.md): snaps to the endpoints of line, arc and spline segments.
-   <img alt="" src=images/Draft_Snap_Midpoint.svg  style="width:32px;"> [Midpoint](Draft_Snap_Midpoint.md): snaps to the middle point of line and arc segments.
-   <img alt="" src=images/Draft_Snap_Center.svg  style="width:32px;"> [Center](Draft_Snap_Center.md): snaps to the center point of circles, arcs and faces, [WP proxies](Draft_WorkingPlaneProxy.md) and [Building parts](Arch_BuildingPart.md)
-   <img alt="" src=images/Draft_Snap_Angle.svg  style="width:32px;"> [Angle](Draft_Snap_Angle.md): snaps to the special cardinal points of circles and arcs, at 45° and 90°.
-   <img alt="" src=images/Draft_Snap_Intersection.svg  style="width:32px;"> [Intersection](Draft_Snap_Intersection.md): snaps to the intersection of two line or arc segments. Hover the mouse over the two desired objects to activate their intersection snaps.
-   <img alt="" src=images/Draft_Snap_Perpendicular.svg  style="width:32px;"> [Perpendicular](Draft_Snap_Perpendicular.md): on line and arc segments, snaps perpendicularly to the latest point.
-   <img alt="" src=images/Draft_Snap_Extension.svg  style="width:32px;"> [Extension](Draft_Snap_Extension.md): snaps on an imaginary line that extends beyond the endpoints of line segments. Hover the mouse over the desired object to activate its extension snap.
-   <img alt="" src=images/Draft_Snap_Parallel.svg  style="width:32px;"> [Parallel](Draft_Snap_Parallel.md): snaps on an imaginary line parallel to a line segment. Hover the mouse over the desired object to activate its parallel snap.
-   <img alt="" src=images/Draft_Snap_Special.svg  style="width:32px;"> [Special](Draft_Snap_Special.md): snaps on special points defined by the object.
-   <img alt="" src=images/Draft_Snap_Near.svg  style="width:32px;"> [Near](Draft_Snap_Near.md): snaps to the closest point or edge on the nearest object.
-   <img alt="" src=images/Draft_Snap_Ortho.svg  style="width:32px;"> [Ortho](Draft_Snap_Ortho.md): snaps on imaginary lines that cross the last point, and extend at 0°, 45° and 90°.
-   <img alt="" src=images/Draft_Snap_Grid.svg  style="width:32px;"> [Grid](Draft_Snap_Grid.md): snaps to the intersections of the grid lines, if the grid is visible.
-   <img alt="" src=images/Draft_Snap_WorkingPlane.svg  style="width:32px;"> [Working plane](Draft_Snap_WorkingPlane.md): always places the snapped point on the current [working plane](Draft_SelectPlane.md), even if you snap to a point outside that working plane.
-   <img alt="" src=images/Draft_Snap_Dimensions.svg  style="width:32px;"> [Dimensions](Draft_Snap_Dimensions.md): shows temporary X and Y dimensions while snapping.
-   <img alt="" src=images/Draft_ToggleGrid.svg  style="width:32px;"> [Toggle grid](Draft_ToggleGrid.md): toggles the visibility of the grid on or off.

## Borrador Herramientas de utilidad 

-   <img alt="" src=images/Draft_Layer.svg  style="width:32px;"> [Layer](Draft_Layer.md): creates a Layer in the current document, to which objects can be added to control object visibility and color. It replaces Draft VisGroup. <small>(v0.19)</small> 
-   <img alt="" src=images/Draft_WorkingPlaneProxy.svg  style="width:32px;"> [Working Plane Proxy](Draft_WorkingPlaneProxy.md): create a proxy object to store the current [Working Plane](Draft_SelectPlane.md) position.
-   <img alt="" src=images/Draft_ToggleDisplayMode.svg  style="width:32px;"> [Toggle display mode](Draft_ToggleDisplayMode.md): switches the display mode of selected objects between \"Flat Lines\" and \"Wireframe\".
-   <img alt="" src=images/Draft_AddToGroup.svg  style="width:32px;"> [Add to group](Draft_AddToGroup.md): quickly adds selected objects to an existing [Std Group](Std_Group.md).
-   <img alt="" src=images/Draft_SelectGroup.svg  style="width:32px;"> [Select group contents](Draft_SelectGroup.md): selects the contents of a selected [Std Group](Std_Group.md) or [Draft Layer](Draft_Layer.md).
-   <img alt="" src=images/Draft_AddConstruction.svg  style="width:32px;"> [Add to Construction group](Draft_AddConstruction.md): add selected objects to the Construction group.
-   <img alt="" src=images/Draft_Heal.svg  style="width:32px;"> [Heal](Draft_Heal.md): heals problematic Draft objects found in very old files.

## Herramientas adicionales 

Herramientas adicionales disponibles desde el menú **Bosquejo → Utilidades**, o a través del menú contextual del botón derecho, dependiendo de los objeto seleccionados.

-   <img alt="" src=images/Draft_ToggleContinueMode.svg  style="width:32px;"> [Activar el modo de continuación](Draft_ToggleContinueMode/es.md): activa o desactiva el modo de continuación del borrador.
-   <img alt="" src=images/Draft_ShowSnapBar.svg  style="width:32px;"> [Mostrar barra de ajuste](Draft_ShowSnapBar/es.md): muestra u oculta la barra de herramientas de [Ajuste de borrador](Draft_Snap/es.md).

## Características adicionales 

-   [Coordinates](Draft_Coordinates/es.md): introducir coordenadas en lugar de hacer clic en la vista 3D para definir un nuevo punto.
-   [Restricción](Draft_Constrain/es.md): limitar el puntero a movimientos horizontales o verticales en relación con un punto previo.
-   [Ajuste](Draft_Snap/es.md): colocar nuevos puntos en lugares especiales de los objetos existentes o en la cuadrícula.
-   [Modo de copia](Draft_Copying/es.md): Todas las herramientas de modificación pueden modificar los objetos seleccionados o crear una copia modificada de los mismos. Si se mantiene pulsada la tecla **Alt** mientras se modifica el objeto, por ejemplo, moviéndolo o rotándolo, se crea una copia cuando se suelta la tecla.
-   [Modo de construcción](Draft_ToggleConstructionMode/es.md): Permite crear geometrías separadas del resto, simplemente activándolas y desactivándolas.
-   [Plano de trabajo](Draft_SelectPlane/es.md): permite seleccionar una superficie sobre la que construir las formas.

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

-   <img alt="" src=images/button_right.svg  style="width:32px;"> [Activate this layer](Draft_AutoGroup.md): makes the selected layer the active layer.

-   <img alt="" src=images/Draft_SelectGroup.svg  style="width:32px;"> [Select layer contents](Draft_SelectGroup.md): selects the objects inside the selected layer.

### Plano trabajo opciones proxy 

For a [Draft WorkingPlaneProxy](Draft_WorkingPlaneProxy.md) these additional options are available:

-   <img alt="" src=images/Draft_SelectPlane.svg  style="width:32px;"> [Write camera position](Draft_WorkingPlaneProxy#Tree_view_context_menu.md): updates the camera settings stored in the working plane proxy.

-   <img alt="" src=images/Draft_SelectPlane.svg  style="width:32px;"> [Write objects state](Draft_WorkingPlaneProxy#Tree_view_context_menu.md): updates the visibility state of objects stored in the working plane proxy.

## 3D vista menú contextual 

The following additional options are available in the [3D view](3D_view.md) context menu:

### Opciones no-selección 

If there is no selection the context menu contains one additional sub-menu:

-    **Utilities**: a subset of the tools available in the main Draft Utilities menu.

### Opciones de selección 

If there is a selection the context menu contains two additional sub-menus:

-    **Draft**: tools for [drawing objects](#Drawing_objects.md) and [modifying objects](#Modifying_objects.md).

-    **Utilities**: a subset of the tools available in the main Draft Utilities menu.

## Herramientas obsoletas 

Estas herramientas se eliminaron de la interfaz en la v0.19 porque ya no tenían ninguna utilidad.

-   <img alt="" src=images/Draft_VisGroup.svg  style="width:32px;"> [VisGrupo](Draft_VisGroup/es.md): crea un VisGrupo en el documento actual. Esto fue reemplazado por <img alt="" src=images/Draft_Layer.svg  style="width:32px;"> [Capa](Draft_Layer/es.md). {{Obsoleto/es|0.19}}
-   <img alt="" src=images/Draft_FinishLine.svg  style="width:32px;"> \[\[Draft\_FinishLine/es\|

Finalización línea\]\]: termina el dibujo del [Borrador Alambre](Draft_Wire/es.md) o [Borrador BSpline](Draft_BSpline/es.md) actual, sin cerrarlo. {{Obsoleto/es|0.19}}{{Obsolete/es|0.19}}

-   <img alt="" src=images/Draft_CloseLine.svg  style="width:32px;"> [Cerrar línea](Draft_CloseLine.md): finaliza el dibujo del [Borrador Alambre](Draft_Wire/es.md) o [Borrador BSpline](Draft_BSpline/es.md) actual, y lo cierra. {{Obsoleto/es|0.19}}
-   <img alt="" src=images/Draft_UndoLine.svg  style="width:32px;"> [Deshacer línea](Draft_UndoLine/es.md): deshace el último segmento de un [Borrador Alambre](Draft_Wire/es.md). {{Obsoleto/es|0.19}}

-   <img alt="" src=images/Draft_Drawing.svg  style="width:32px;"> [Drawing](Draft_Drawing.md): writes selected objects to a [Drawing Workbench](Drawing_Workbench.md) page. {{Obsolete|0.17}}

These [3D view](3D_view.md) context menu options are still available when the [Draft Wire](Draft_Wire.md), [Draft BSpline](Draft_BSpline.md), [Draft CubicBezCurve](Draft_CubicBezCurve.md) or [Draft BezCurve](Draft_BezCurve.md) command is active but will be removed in the near future:

-   <img alt="" src=images/Draft_UndoLine.svg  style="width:32px;"> [Undo last segment](Draft_Wire#Options.md): use the {{button|<img src="images/Draft_UndoLine.svg" width=16px> Undo}} button in the task panel of the command instead. {{Obsolete|0.20}}

-   <img alt="" src=images/Draft_FinishLine.svg  style="width:32px;"> [Finish line](Draft_Wire#Options.md): use the **<img src="images/Draft_FinishLine.svg" width=16px> Finish** button in the task panel of the command instead. {{Obsolete|0.20}}

-   <img alt="" src=images/Draft_CloseLine.svg  style="width:32px;"> [Close line](Draft_Wire#Options.md): use the **<img src="images/Draft_CloseLine.svg" width=16px> Close** button in the task panel of the command instead. {{Obsolete|0.20}}

## Preferencias

-   <img alt="" src=images/Preferences-draft.svg  style="width:32px;"> [Preferencias](Draft_Preferences/es.md): preferencias generales para el plano de trabajo y las herramientas de dibujo.
-   <img alt="" src=images/Preferences-import-export.svg  style="width:32px;"> [Preferencias de importación y exportación](Import_Export_Preferences/es.md): preferencias disponibles para importar desde y exportar a diferentes formatos de archivo.

## Formatos de archivo 

Son funciones para abrir, importar o exportar otros formatos de archivo. Abrir abrirá un nuevo documento con el contenido del archivo, mientras que importar añadirá el contenido del archivo al documento actual. Exportar guardará los objetos seleccionados en un archivo. Si no se selecciona nada, se exportarán todos los objetos. Tenga en cuenta que el propósito del Módulo Borrador es trabajar con objetos 2D, por lo que esas rutinas de importación se centran sólo en objetos 2D, y aunque los formatos DXF y OCA también soportan definiciones de objetos en el espacio 3D (los objetos no son necesariamente planos), no importarán objetos volumétricos como mallas, superficies 3D, etc., sino líneas, círculos, textos o formas planas. Los formatos de archivo actualmente soportados son: El módulo Borrador proporciona a FreeCAD importadores y exportadores para los siguientes formatos de archivo:

-   [Autodesk .DXF](Draft_DXF/es.md): importa y exporta archivos [Drawing Exchange Format](http://en.wikipedia.org/wiki/AutoCAD_DXF) creados con otras aplicaciones de CAD 2D. Ver también [FreeCAD y DXF Importación](FreeCAD_and_DXF_Import/es.md).
-   [Autodesk .DWG](Draft_DXF/es.md): importa y exporta archivos DWG a través del importador DXF, cuando la utilidad [ODA Converter](Extra_python_modules#ODA_Converter_(antes_Teigha_Converter).md) está instalada. Ver también [FreeCAD y DWG Importación](FreeCAD_y_DWG_Import/es.md).
-   [SVG (como geometría)](Draft_SVG/es.md): importa y exporta archivos [Scalable Vector Graphics](http://en.wikipedia.org/wiki/Scalable_Vector_Graphics) creados con aplicaciones de dibujo vectoriales
-   [Open Cad format .OCA](Draft_OCA/es.md): importa y exporta archivos OCA/GCAD, un potencialmente nuevo [formato de archivo abierto para CAD](http://groups.google.com/group/open_cad_format)
-   [Ala Data Format .DAT](Draft_DAT/es.md): importa archivos DAT describiendo [Ala perfiles](http://www.ae.illinois.edu/m-selig/ads/coord_database.html)

### Instalar importadores 

-   [FreeCAD y DWG Importación](FreeCAD_and_DWG_Import/es.md): Importación y exportación de archivos DWG
-   [FreeCAD y DXF Importación](FreeCAD_and_DXF_Import/es.md): Importación y exportación de archivos DXF

## Pruebas unitarias 


**Véase también:**

[Ambiente de trabajo Prueba](Test_Workbench/es.md).

Para ejecutar las pruebas unitarias del banco de trabajo, ejecute lo siguiente desde el terminal del sistema operativo. 
```python
freecad -t TestDraft
```

## Guión

Las herramientas de Bosquejo pueden utilizarse en [macros](macros/es.md) y desde la [Python](Python/es.md) consola utilizando la [Bosquejo API](Draft_API/es.md).

El ambiente de trabajo incluye un módulo para crear muestras de todos los objetos en un nuevo documento. {{Version/es|0.19}}

Utilícelo para comprobar que todos los objetos se producen correctamente. 
```python
import drafttests.draft_test_objects as dto
doc = dto.create_test_file()
```

Inspeccionar el código de este módulo es útil para entender cómo utilizar la interfaz de programación. 
```python
$INSTALLDIR/Mod/Draft/drafttests/draft_test_objects.py
```

Donde `$INSTALLDIR` es el directorio de nivel superior donde se instaló el software; por ejemplo, en Linux puede ser `/usr/share/freecad`.

<img alt="" src=images/Draft_test_objects.png  style="width:500px;"> 
*Test objects for the [Ambiente de trabajo Borrador](Draft_Workbench/de.md).*

## Tutoriales

-   [Borrador del tutorial](Draft_tutorial/es.md)
-   [Borrador del tutorial Anticuado](Draft_tutorial_Outdated/es.md)
-   [Tutorial de la forma de las cuerdas del borrador](Draft_ShapeString_tutorial/es.md)





 

[Category:Workbenches{{\#translation:}}](Category:Workbenches.md)
