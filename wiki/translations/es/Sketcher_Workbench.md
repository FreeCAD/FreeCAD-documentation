# <img alt="El icono del Ambiente de trabajo Croquizador" src=images/Workbench_Sketcher.svg  style="width:64px;"> Sketcher Workbench/es






## Introducción


<div class="mw-translate-fuzzy">

El FreeCAD <img alt="" src=images/Workbench_Sketcher.svg  style="width:24px;"> [Ambiente de trabajo Croquizador](Sketcher_Workbench/es.md) se utiliza para crear geometrías 2D destinadas a ser utilizadas en el <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [Ambiente de trabajo DiseñoPieza](PartDesign_Workbench/es.md), <img alt="" src=images/Workbench_Arch.svg  style="width:24px;"> y otros Ambiente de trabajo. Generalmente, un dibujo 2D se considera el punto de partida para la mayoría de los modelos CAD, ya que un boceto 2D puede ser \"extruido\" para crear una forma 3D; otros bocetos 2D pueden ser utilizados para crear otras características como bolsas, crestas o extrusiones sobre las formas 3D previamente construidas. Junto con las operaciones booleanas definidas en el <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Ambiente de trabajo piezas](Part_Workbench/es.md), el Croquis forma la base de la [geometría sólida constructiva](constructive_solid_geometry/es.md) (CSG) método de construcción de sólidos. Además, junto con el <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [Ambiente de trabajo DiseñoPieza](PartDesign_Workbench/es.md) operaciones, el Sketcher también forma la base de la [edición de características](feature_editing/es.md) metodología de la creación de sólidos.


</div>

Together with boolean operations defined in the <img alt="" src=images/Workbench_Part.svg  style="width:16px;"> [Part Workbench](Part_Workbench.md), the Sketcher Workbench, or \"The Sketcher\" for short, forms the basis of the [constructive solid geometry](Constructive_solid_geometry.md) (CSG) method of building solids. Together with <img alt="" src=images/Workbench_PartDesign.svg  style="width:16px;"> [PartDesign Workbench](PartDesign_Workbench.md) operations, it also forms the basis of the [feature editing](Feature_editing.md) methodology of creating solids. But many other workbenches use sketches as well.


<div class="mw-translate-fuzzy">

El ambiente de trabajo Croquizador presenta \"restricciones\", que permiten que las formas 2D sigan definiciones geométricas precisas en términos de longitud, ángulos y relaciones (horizontalidad, verticalidad, perpendicularidad, etc.). Un solucionador de restricciones calcula el alcance de las restricciones de la geometría 2D y permite la exploración interactiva de los grados de libertad del croquis.


</div>


<div class="mw-translate-fuzzy">

#### ¿Para qué no es bueno el entorno de croquizado? 

El Croquizador no está pensado para producir planos detallados en 2D. Una vez que los croquis se utilizan para generar un sólido, son automáticamente ocultados. Las cotas son sólo visibles en el modo de edición del croquis.


</div>

<img alt="" src=images/FC_ConstrainedSketch.png  style="width:450px;"> 
*Un croquis completamente restringido‎*

## Constraints


<div class="mw-translate-fuzzy">

#### ¿Qué son las restricciones? 

Las restricciones se utilizan para limitar los grados de libertad de un objeto. Por ejemplo, una línea tiene 4 [grados de libertad](#Degrees_Of_Freedom.md) (en inglés Degrees Of Freedom, generalmente abreviado como \" DOF \"): Se puede mover horizontal o verticalmente, se puede estirar, y puede girarse.


</div>

Aplicando una restricción horizontal o vertical, o una restricción angular (relativa a otra línea o a uno de los ejes), se limitará su capacidad de girar, aunque seguirá con 3 grados de libertad. Bloqueando uno de sus extremos en relación con el origen eliminará otros 2 grados de libertad. Y aplicando una restricción dimensional se eliminará el último grado de libertad. La línea se considerará que está entonces **completamente restringida**.


<div class="mw-translate-fuzzy">

Múltiples objetos pueden ser restringidos con respecto a otro. Dos líneas se pueden unir por uno de sus puntos con la restricción de coincidencia de puntos. Un ángulo se puede definir entre ellas, o se pueden establecer como perpendiculares. Una línea puede ser tangente a un arco o a una circunferencia, etc. Un Croquis complejo puede tener diferentes soluciones y **restringir completamente** significa encontrar una de esas posibles soluciones mediante el uso de restricciones.


</div>


<div class="mw-translate-fuzzy">

Existen dos tipos de restricciones: geométricas y dimensionales. Ambas son explicadas en la sección [#Las herramientas](#Las_herramientas.md) más abajo.


</div>

### Edit constraints 

When a [driving dimensional constraint](Sketcher_ToggleDrivingConstraint.md) is created, and if the **Ask for value after creating a dimensional constraint** [preference](Sketcher_Preferences#Display.md) is selected (default), a dialog opens to edit its value.

![](images/Sketcher_Edit_Constraint.png )

You can enter a numerical value or an [expression](Expressions.md), and it is possible to name the constraint to facilitate its use in other expressions. You can also check the **Reference** checkbox to switch the constrain to [reference mode](Sketcher_ToggleDrivingConstraint.md).

To edit the value of an existing dimensional constraint do one of the following:

-   Double-click the constraint value in the [3D view](3D_view.md).
-   Double-click the constraint in the [Sketcher Dialog](Sketcher_Dialog.md).
-   Right-click the constraint in the Sketcher Dialog and select the **Change value** option from the context menu.

### Reposition constraints 

Dimensional constraints can be repositioned in the 3D view by dragging. Hold down the left mouse button over the constraint value and move the mouse. The symbols of geometric constraints are positioned automatically and cannot be moved.

## Profile sketches 

To create a sketch that can be used as a profile for generating solids certain rules must be followed:

-   The sketch must contain only closed contours. Gaps between endpoints, however small, are not allowed.
-   Contours can be nested, to create voids, but should not self-intersect or intersect other contours.
-   Contours cannot share edges with other contours. Duplicate edges must be avoided.
-   T-connections, that is more than two edges sharing a common point, or a point touching an edge, are not allowed.

These rules do not apply to construction geometry (default color blue), which is not shown outside edit mode, or if the sketch is used for a different purpose. Depending on the workbench and the tool that will use the profile sketch, additional restrictions may apply.

## Drawing aids 

The Sketcher Workbench has several drawing aids and other features that can help when creating geometry and applying constraints.

### Continue modes 

There are two continue modes: **Geometry creation \"Continue Mode\"** and **Constraint creation \"Continue Mode\"**. If these are checked (default) in the [preferences](Sketcher_Preferences#Display.md), related tools will restart after finishing. To exit a continuous tool press **Esc** or the right mouse button. This must be repeated if a continuous geometry tool has already received input. You can also exit a continuous tool by starting another geometry or constraint creation tool. Note that pressing **Esc** if no tool is active will exit sketch edit mode. Uncheck the **Esc can leave sketch edit mode** [preference](Sketcher_Preferences#General.md) if you often inadvertently press **Esc** too many times.

### Auto constraints 

In sketches that have **Auto constraints** checked (default) several constraints are applied automatically. The icon of a proposed automatic constraint is shown next to the cursor when it is placed correctly. Left-Clicking will then apply that constraint. This is a per-sketch setting that can be changed in the [Sketcher Dialog](Sketcher_Dialog#Constraints.md) or by changing the **Autoconstraints** [property](Property_editor.md) of the sketch.

The following constraints are applied automatically:

-   <img alt="" src=images/Sketcher_ConstrainCoincident.svg  style="width:16px;"> [Coincident](Sketcher_ConstrainCoincident.md)

-   <img alt="" src=images/Sketcher_ConstrainPointOnObject.svg  style="width:16px;"> [Point on object](Sketcher_ConstrainPointOnObject.md)

-   <img alt="" src=images/Sketcher_ConstrainHorizontal.svg  style="width:16px;"> [Horizontal](Sketcher_ConstrainHorizontal.md)

-   <img alt="" src=images/Sketcher_ConstrainVertical.svg  style="width:16px;"> [Vertical](Sketcher_ConstrainVertical.md)

-   <img alt="" src=images/Sketcher_ConstrainTangent.svg  style="width:16px;"> [Tangent](Sketcher_ConstrainTangent.md)

-    <small>(v1.0)</small> : <img alt="" src=images/Sketcher_ConstrainSymmetric.svg  style="width:16px;"> [Symmetric](Sketcher_ConstrainSymmetric.md) (line midpoint)

### Snapping


<small>(v0.21)</small> 

It is possible to [snap](Sketcher_Snap.md) to grid lines and grid intersection, to edges of geometry and midpoints of lines and arcs, and to certain angles. Please note that snapping does not produce constraints in and of itself. For example, only if [Auto constraints](#Auto_constraints.md) is switched on will snapping to an edge produce a [Point on object constraint](Sketcher_ConstrainPointOnObject.md). But just picking a point on the edge would then have the same result.

### On-View-Parameters 


<small>(v1.0)</small> 

Depending on the selected option in the [preferences](Sketcher_Preferences#General.md) only the dimensional On-View-Parameters or both the dimensional and the positional On-View-Parameters can be enabled. Positional parameters allow the input of exact coordinates, for example the center of a circle, or the start point of a line. Dimensional parameters allow the input of exact dimensions, for example the radius of a circle, or the length and angle of a line. On-View-Parameters are not available for all tools.

![](images/Sketcher_On_view_parameters_positional.png ) 
*Determining the center point of a circle with the positional parameters enabled*

![](images/Sketcher_On_view_parameters_dimensional.png ) 
*Determining the radius of a circle with the dimensional parameters enabled*

If values are entered and confirmed by pressing **Enter** or **Tab**, related constraints are added automatically. If two parameters are displayed at the same time, for example the X and Y coordinate of a point, it is possible to enter one value and pick a point to define the other. Depending on the object additional constraints may be required to fully constrain it. Constraints resulting from On-View-Parameters take precedence over those that may result from [Auto constraints](Sketcher_Dialog#Constraints.md).

<img alt="" src=images/Sketcher_ArcExample3.png  style="width:300px;"> 
*Arc created by entering all On-View-Parameters with resulting automatically created constraints*

### Coordinate display 

If the **Show coordinates beside cursor while editing** [preference](Sketcher_Preferences#Display.md) is checked (default), the parameters of the current geometry tool (coordinates, radius, or length and angle) are displayed next to the cursor. This is deactivated while On-View-Parameters are shown.

## Selection methods 

While a sketch is in edit mode the following selection methods can be used:

### 3D view element selection 

As elsewhere in FreeCAD, an element can be selected in the [3D view](3D_view.md) with a single left mouse click. But there is no need to hold down the **Ctrl** key when selecting multiple elements. Holding down that key is possible though and has the advantage that you can miss-click without losing the selection. Edges, points and constraints can be selected in this manner.

### 3D view box selection 

Box selection in the 3D view works without using [Std BoxSelection](Std_BoxSelection.md) or [Std BoxElementSelection](Std_BoxElementSelection.md):

1.  Make sure that no tool is active.
2.  Do one of the following:
    -   Click in an empty area and drag a rectangle from left to right to select elements that lie completely inside the rectangle.
    -   Click in an empty area and drag a rectangle from right to left to also select elements that touch or cross the rectangle.

You can box-select edges and points, constraints cannot be box-selected.

### 3D view connected geometry selection 


<small>(v1.0)</small> 

Double-clicking an edge in the 3D view will select all edges directly and indirectly connected with that edge via endpoints. There is no need for the edges to be connected with [Coincident constraints](Sketcher_ConstrainCoincident.md), endpoints need only have the same coordinates.

### Sketcher Dialog selection 

Edges and points can also be selected from the Elements section of the [Sketcher Dialog](Sketcher_Dialog.md), and constraints from the Constraints section of that dialog.

## Copy, cut and paste 


<small>(v1.0)</small> 

The standard keyboard shortcuts, **Ctrl**+**C**, **Ctrl**+**X** and **Ctrl**+**V**, can be used to copy, cut and paste selected Sketcher geometry including related constraints. But these tools are also available from the **Sketch → Sketcher tools** menu. They can be used within the same sketch but also between different sketches or separate instances of FreeCAD. Since the data is copied to the clipboard in the form of Python code, it can be used in other ways too (e.g. shared on the forum).

## Tools


<div class="mw-translate-fuzzy">

## Las herramientas 

Todas las herramientas del Ambiente de Trabajo Croquiz se encuentran en el menú Boceto que aparece al cargar el Ambiente de Trabajo Croquiz.


</div>

Some tools are also available from the [3D view](3D_view.md) context menu while a sketch is in edit mode, or from the context menus of the [Sketcher Dialog](Sketcher_Dialog.md).


<small>(v0.21)</small> 

: If a sketch is in edit mode the Structure toolbar is hidden as none of its tools can then be used.

### General

#### Sketcher toolbar 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_NewSketch.svg  style="width:32px;"> [Nuevo croquis](Sketcher_NewSketch/es.md): Crea un nuevo croquis en la cara o plano seleccionado. Si no se selecciona ninguna cara mientras se ejecuta esta herramienta, se le pide al usuario que seleccione un avión en una ventana emergente.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_EditSketch.svg  style="width:32px;"> [Editar croquis](Sketcher_EditSketch/es.md): Edita el croquis seleccionado. Esto abrirá el [Diálogo de Croquis](Sketcher_Dialog/es.md).


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_MapSketch.svg‎  style="width:32px;"> [Fijar croquis a cara](Sketcher_MapSketch/es.md): Traza un boceto de la cara previamente seleccionada de un sólido.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ReorientSketch.svg  style="width:32px;">[Reorientar croquis](Sketcher_ReorientSketch/es.md): Permite adjuntar el boceto a uno de los planos principales.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ValidateSketch.svg  style="width:32px;">[Validar el boceto](Sketcher_ValidateSketch/es.md): Verificar la tolerancia de los diferentes puntos y ajustarlos.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_MergeSketch.svg‎  style="width:32px;"> [Fusionar croquis](Sketcher_MergeSketches/es.md): Fusiona dos o más croquis


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_MirrorSketch.svg‎  style="width:32px;"> [Reflejar croquis](Sketcher_MirrorSketch/es.md):

Reflejar un boceto a lo largo del eje X, el eje Y o el origen.


</div>

#### Sketcher Edit Mode toolbar 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_LeaveSketch.svg  style="width:32px;"> [Abandonar el croquis](Sketcher_LeaveSketch/es.md): Abandona el modo de edición del croquis.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ViewSketch.svg‎  style="width:32px;"> [Vista de croquis](Sketcher_ViewSketch/es.md): Establece la vista del modelo perpendicular al plano del croquis.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ViewSection.svg  style="width:32px;"> [Ver sección](Sketcher_ViewSection/es.md): Crea un plano de sección que oculta temporalmente cualquier materia delante del plano de dibujo.


</div>

#### Sketcher edit tools toolbar 

-   <img alt="" src=images/Sketcher_Grid.svg  style="width:32px;"> [Toggle grid](Sketcher_Grid.md): Toggles the grid in the sketch currently being edited. Settings can be changed in the related menu. <small>(v0.21)</small> 

-   <img alt="" src=images/Sketcher_Snap.svg  style="width:32px;"> [Toggle snap](Sketcher_Snap.md): Toggles snapping in all sketches. Settings can be changed in the related menu. <small>(v0.21)</small> 

-   <img alt="" src=images/Sketcher_RenderingOrder.svg  style="width:32px;"> [Configure rendering order](Sketcher_RenderingOrder.md): The rendering order of all sketches can be changed in the related menu. <small>(v0.21)</small> 

#### Other


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_StopOperation.svg  style="width:32px;"> [Detener la operación](Sketcher_StopOperation/es.md): cuando esté en el modo de edición, detenga la operación actual, ya sea el dibujo, la configuración de restricciones, etc.


</div>



### Geometrías de croquis 

Estas son las herramientas para la creación de objetos.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_CreatePoint.svg  style="width:32px;"> [Punto](Sketcher_CreatePoint/es.md): Dibuja un punto.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_CreatePolyline.svg  style="width:32px;"> [Polilínea (línea de múltiples puntos)](Sketcher_CreatePolyline/es.md): Dibuja una línea creada por múltiples segmentos de línea. Presionando la tecla M se puede iterar entre los diferents modos.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_Line.svg  style="width:32px;"> [Línea](Sketcher_CreateLine/es.md): Dibuja un segmento de línea entre 2 puntos. Las líneas son infinitas en lo que respecta a ciertas restricciones.


</div>

-   <img alt="" src=images/Sketcher_CreateArc.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Create arc:


<div class="mw-translate-fuzzy">

  - <img alt="" src=images/Sketcher_Arc.svg  style="width:32px;"> [Arco](Sketcher_CreateArc/es.md): Dibuja un segmento de arco dada por el centro, radio, ángulo inicial y ángulo final.


</div>


<div class="mw-translate-fuzzy">

  - <img alt="" src=images/Sketcher_Create3PointArc.svg  style="width:32px;"> [Arco a través de 3 Puntos](Sketcher_Create3PointArc/es.md): Dibuja un segmento de arco entre dos puntos y un tercer punto que se haya en la circumferencia.


</div>

  - <img alt="" src=images/Sketcher_CreateArcOfEllipse.svg  style="width:32px;"> [Arc of ellipse](Sketcher_CreateArcOfEllipse.md): Creates an arc of ellipse.

  - <img alt="" src=images/Sketcher_CreateArcOfHyperbola.svg  style="width:32px;"> [Arc of hyperbola](Sketcher_CreateArcOfHyperbola.md): Creates an arc of hyperbola.

  - <img alt="" src=images/Sketcher_CreateArcOfParabola.svg  style="width:32px;"> [Arc of parabola](Sketcher_CreateArcOfParabola.md): Creates an arc of parabola.

-   <img alt="" src=images/Sketcher_CreateCircle.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Create circle/ellipse:


<div class="mw-translate-fuzzy">

  - <img alt="" src=images/Sketcher_Circle.svg  style="width:32px;"> [Círculo](Sketcher_CreateCircle/es.md): Dibuja un círculo desde el centro y el radio.


</div>


<div class="mw-translate-fuzzy">

  - <img alt="" src=images/Sketcher_Create3PointCircle.svg  style="width:32px;"> [Círculo de 3 puntos](Sketcher_Create3PointCircle/es.md): Dibuja un círculo de tres puntos en la circunferencia.


</div>

  - <img alt="" src=images/Sketcher_CreateEllipseByCenter.svg  style="width:32px;"> [Ellipse by center](Sketcher_CreateEllipseByCenter.md): Creates an ellipse by its center, an endpoint of one of its axes, and a point along the ellipse. <small>(v1.0)</small> : Or by both endpoints of one of its axes and a point along the ellipse.

  - <img alt="" src=images/Sketcher_CreateEllipseBy3Points.svg  style="width:32px;"> [Ellipse by 3 points](Sketcher_CreateEllipseBy3Points.md): Creates an ellipse by the endpoints of one of its axes and a point along the ellipse. <small>(v1.0)</small> : This is the same tool as [Ellipse by center](Sketcher_CreateEllipseByCenter.md) but with a different initial mode.

-   <img alt="" src=images/Sketcher_CreateRectangle.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Create rectangle:


<div class="mw-translate-fuzzy">

  - <img alt="" src=images/Sketcher_CreateRectangle.svg  style="width:32px;"> [Rectángulo](Sketcher_CreateRectangle/es.md): Dibuja un rectángulo dado por 2 puntos opuestos


</div>


<div class="mw-translate-fuzzy">

  - <img alt="" src=images/Sketcher_CreateRectangle_Center.svg  style="width:32px;"> [Rectángulo Centrado](Sketcher_CreateRectangle_Center/es.md): Dibuja un rectángulo a partir de un punto central y un punto de borde. {{Version/es|0.20}}


</div>


<div class="mw-translate-fuzzy">

  - <img alt="" src=images/Sketcher_CreateOblong.svg  style="width:32px;"> [Rectángulo Redondeado](Sketcher_CreateOblong/es.md): Dibuja un rectángulo redondeado desde 2 puntos opuestos. {{Version/es|0.20}}


</div>

-   <img alt="" src=images/Sketcher_CreateHexagon.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Create regular polygon:


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_CreateTriangle.svg  style="width:32px;"> [Triángulo](Sketcher_CreateTriangle/es.md): Dibuja un triángulo regular inscrito en un círculo de geometría de construcción.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_CreateSquare.svg  style="width:32px;"> [Cuadrado](Sketcher_CreateSquare/es.md): Dibuja un cuadrado regular inscrito en una circumferencia en modo construcción.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_CreatePentagon.svg  style="width:32px;"> [Pentagon](Sketcher_CreatePentagon/es.md): Dibuja un pentágono regular inscrito en una circumferencia en modo construcción.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_CreateHexagon.svg  style="width:32px;"> [Hexagon](Sketcher_CreateHexagon/es.md): Dibuja un hexágono regular inscrito en un círculo de geometría de construcción.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_CreateHeptagon.svg  style="width:32px;"> [Heptagon](Sketcher_CreateHeptagon/es.md): Dibuja un heptágono regular inscrito en un círculo de geometría de construcción.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_CreateOctagon.svg  style="width:32px;"> [Octagon](Sketcher_CreateOctagon/es.md): Dibuja un octágono regular inscrito en un círculo de geometría de construcción.


</div>


<div class="mw-translate-fuzzy">

  - <img alt="" src=images/Sketcher_CreateRegularPolygon.svg  style="width:32px;"> [Crear polígono regular](Sketcher_CreateRegularPolygon/es.md) : Dibuja un polígono regular seleccionando el número de lados y eligiendo dos puntos: el centro y una esquina.


</div>

-   <img alt="" src=images/Sketcher_CreateSlot.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Create slot:


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_CreateSlot.svg  style="width:32px;"> [Ranura](Sketcher_CreateSlot/es.md): Dibuja un óvalo seleccionando el centro de un semicírculo y un punto final del otro semicírculo.


</div>

  - <img alt="" src=images/Sketcher_CreateArcSlot.svg  style="width:32px;"> [Arc slot](Sketcher_CreateArcSlot.md): Creates an arc slot. <small>(v1.0)</small> 

-   <img alt="" src=images/Sketcher_CreateBSpline.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Create B-spline:

  - <img alt="" src=images/Sketcher_CreateBSpline.svg  style="width:32px;"> [B-spline by control points](Sketcher_CreateBSpline.md): Creates a B-spline curve by control points. <small>(v1.0)</small> : Or by knot points.

  - <img alt="" src=images/Sketcher_CreatePeriodicBSpline.svg  style="width:32px;"> [Periodic B-spline by control points](Sketcher_CreatePeriodicBSpline.md): Creates a periodic (closed) B-spline curve by control points. <small>(v1.0)</small> : This is the same tool as [B-spline by control points](Sketcher_CreateBSpline.md) but with a different initial mode.

  - <img alt="" src=images/Sketcher_CreateBSplineByInterpolation.svg  style="width:32px;"> [B-spline by knots](Sketcher_CreateBSplineByInterpolation.md): Creates a B-spline curve by knot points. Idem.

  - <img alt="" src=images/Sketcher_CreatePeriodicBSplineByInterpolation.svg  style="width:32px;"> [Periodic B-spline by knots](Sketcher_CreatePeriodicBSplineByInterpolation.md): Creates a periodic (closed) B-spline curve by knot points. Idem.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ToggleConstruction.svg  style="width:32px;"> [Modo de construcción](Sketcher_ToggleConstruction/es.md): Cambia la geometría del boceto del modo de construcción. La geometría de la construcción se muestra en azul y se descarta fuera del modo de edición del boceto.


</div>



### Restricciones de croquis 


<div class="mw-translate-fuzzy">

Las restricciones son utilizadas para establecer reglas entre los elementos del croquis, y para bloquear el croquis a lo largo de los ejes verticales y horizontales. Algunas restricciones crean restricciones auxiliares adicionales [Restricciones auxiliares](Sketcher_helper_constraint/es.md)


</div>

-   <img alt="" src=images/Sketcher_Dimension.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Dimensional constraints:

  - <img alt="" src=images/Sketcher_Dimension.svg  style="width:32px;"> [Dimension](Sketcher_Dimension.md): Is the context-sensitive constraint tool of the Sketcher Workbench. Based on the current selection, it offers appropriate dimensional constraints, but also geometric constraints. <small>(v1.0)</small> 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ConstrainDistanceX.svg  style="width:32px;"> [Distancia Horizontal](Sketcher_ConstrainDistanceX/es.md): Fija la distancia horizontal entre dos puntos o puntos finales de líneas. Si solo se selecciona uno, la distancia se define respecto al origen.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ConstrainDistanceY.svg  style="width:32px;">[Distancia Vertical](Sketcher_ConstrainDistanceY/es.md): Fija la distancia vertical entre dos puntos o puntos finales de líneas. Si solo se selecciona uno, la distancia se define respecto al origen.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ConstrainDistance.svg  style="width:32px;"> [Distancia](Sketcher_ConstrainDistance/es.md): Define la distancia de una línea seleccionada limitando su longitud, o define la distancia entre dos puntos limitando la distancia entre ellos.


</div>

  - <img alt="" src=images/Sketcher_ConstrainRadiam.svg  style="width:32px;"> [Auto radius/diameter](Sketcher_ConstrainRadiam.md): Fixes the radius of arcs and B-spline weight circles, and the diameter of circles.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ConstrainRadius.svg  style="width:32px;"> [Radio](Sketcher_ConstrainRadius/es.md): Define el radio de un arco o círculo seleccionado restringiendo el radio.
-   <img alt="" src=images/Sketcher_ConstrainDiameter.svg  style="width:32px;"> [Diámetro](Sketcher_ConstrainDiameter/es.md): Define el diámetro de un arco o círculo seleccionado restringiendo el diámetro.
-   <img alt="" src=images/Sketcher_ConstrainRadiam.svg  style="width:32px;"> [Radiam](Sketcher_ConstrainRadiam/es.md): Define automáticamente el radio/diámetro de un arco o círculo seleccionado (peso para un polo B-spline, diámetro para un círculo completo, radio para un arco) {{Version/es|0.20}}
-   <img alt="" src=images/Sketcher_ConstrainAngle.svg  style="width:32px;"> [Ángulo](Sketcher_ConstrainAngle/es.md): Define el ángulo interno entre dos líneas seleccionadas.


</div>

  - <img alt="" src=images/Sketcher_ConstrainDiameter.svg  style="width:32px;"> [Diameter](Sketcher_ConstrainDiameter.md): Fixes the diameter of circles and arcs.

  - <img alt="" src=images/Sketcher_ConstrainAngle.svg  style="width:32px;"> [Angle](Sketcher_ConstrainAngle.md): Fixes the angle between two edges, the angle of a line with the horizontal axis of the sketch, or the aperture angle of a circular arc.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ConstrainLock.svg  style="width:32px;"> [Bloquear](Sketcher_ConstrainLock/es.md): Restringe el artículo seleccionado estableciendo distancias verticales y horizontales relativas al origen, bloqueando así la ubicación de ese artículo. Estas distancias de restricción pueden ser editadas más tarde.


</div>

-   <img alt="" src=images/Sketcher_ConstrainCoincidentUnified.svg  style="width:32px;"> [Coincident (unified)](Sketcher_ConstrainCoincidentUnified.md): Creates a coincident constraint between points, fixes points on edges or axes, or creates a concentric constraint. It combines the [Coincident](Sketcher_ConstrainCoincident.md) and [Point on object](Sketcher_ConstrainPointOnObject.md) tools. <small>(v1.0)</small> 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ConstrainCoincident.svg  style="width:32px;"> [Coincidente](Sketcher_ConstrainCoincident/es.md): Pone un punto en (coincidente con) uno o más puntos.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ConstrainPointOnObject.svg  style="width:32px;"> [Punto sobre objeto](Sketcher_ConstrainPointOnObject/es.md): Pone un punto sobre otro objeto como una línea, un arco o un eje.


</div>

-   <img alt="" src=images/Sketcher_ConstrainHorVer.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;">Horizontal/vertical constraints:

  - <img alt="" src=images/Sketcher_ConstrainHorVer.svg  style="width:32px;"> [Horizontal/vertical](Sketcher_ConstrainHorVer.md): Constrains lines or pairs of points to be horizontal or vertical, whichever is closest to the current alignment. It combines the [Horizontal](Sketcher_ConstrainHorizontal.md) and [Vertical](Sketcher_ConstrainVertical.md) tools. <small>(v1.0)</small> 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ConstrainHorizontal.svg  style="width:32px;"> [Horizontal](Sketcher_ConstrainHorizontal/es.md): Limita las líneas o elementos de polilínea seleccionados a una verdadera orientación horizontal. Se puede seleccionar más de un objeto antes de aplicar esta restricción.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ConstrainVertical.svg  style="width:32px;">[Vertical](Sketcher_ConstrainVertical/es.md): Limita las líneas o elementos de polilínea seleccionados a una verdadera orientación vertical. Se puede seleccionar más de un objeto antes de aplicar esta restricción.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ConstrainParallel.svg  style="width:32px;">[Paralelo](Sketcher_ConstrainParallel/es.md): Restringir dos o más líneas paralelas entre sí.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ConstrainPerpendicular.svg  style="width:32px;"> [Perpendicular](Sketcher_ConstrainPerpendicular/es.md): Restringe dos líneas perpendiculares entre sí, o restringe una línea perpendicular a un punto final de un arco.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ConstrainTangent.svg  style="width:32px;"> [Tangente](Sketcher_ConstrainTangent/es.md): Crea una restricción tangente entre dos entidades seleccionadas, o una restricción co-lineal entre dos segmentos de línea. Un segmento de línea no tiene que estar situado directamente en un arco o círculo para ser restringido tangencialmente a ese arco o círculo.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ConstrainEqual.svg  style="width:32px;"> [Iguales](Sketcher_ConstrainEqual/es.md): Limita a dos entidades seleccionadas iguales entre sí. Si se usan en círculos o arcos, sus radios serán iguales.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ConstrainSymmetric.svg  style="width:32px;"> [Simétrico](Sketcher_ConstrainSymmetric/es.md): Restringe dos puntos simétricamente sobre una línea, o restringe los dos primeros puntos seleccionados simétricamente sobre un tercer punto seleccionado.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ConstrainBlock.svg  style="width:32px;"> [Bloqueo](Sketcher_ConstrainBlock/es.md): bloquea el movimiento de un borde, es decir, impide que sus vértices cambien su posición actual. Debería ser particularmente útil para fijar la posición de las Líneas B. Ver el [Tema de foro Bloqueo de restricción](https://forum.freecadweb.org/viewtopic.php?f=9&t=26572).


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ConstrainSnellsLaw.svg  style="width:32px;"> [Ley de Snell](Sketcher_ConstrainSnellsLaw/es.md): restringe dos líneas para obedecer una ley de refracción para simular la luz que pasa a través de una interfaz.


</div>

-   <img alt="" src=images/Sketcher_ToggleDrivingConstraint.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Toggle constraints:


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ToggleDrivingConstraint.svg  style="width:32px;"> [Cambiar la conducción/restricción de referencia](Sketcher_ToggleDrivingConstraint/es.md): Conmuta la barra de herramientas o las restricciones seleccionadas a/desde el modo de referencia.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ToggleActiveConstraint.svg  style="width:32px;"> [Activar/Desactivar restricción](Sketcher_ToggleActiveConstraint/es.md): Activar o desactivar una restricción ya colocada. {{Version/es|0.19}}


</div>



### Herriamentas de croquis 

-   <img alt="" src=images/Sketcher_CreateFillet.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Create fillet/chamfer:


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_CreateFillet.svg  style="width:32px;"> [Redondeo](Sketcher_CreateFillet/es.md): Hace un redondeo entre dos líneas unidas en un punto. Selecciona ambas líneas o haz clic en el punto de la esquina, y luego activa la herramienta.


</div>

  - <img alt="" src=images/Sketcher_CreateChamfer.svg  style="width:32px;"> [Chamfer](Sketcher_CreateChamfer.md): creates a chamfer between two non-parallel edges. This is the same tool as [Fillet](Sketcher_CreateFillet.md) but with a different initial mode. <small>(v1.0)</small> 

-   <img alt="" src=images/Sketcher_Trimming.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Edit edge:


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_Trimming.svg  style="width:32px;"> [Recortar](Sketcher_Trimming/es.md): Recorta una línea, círculo o arco con respecto al punto designado.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_Split.svg  style="width:32px;"> [Dividir](Sketcher_Split/es.md): Divide una línea o un arco en dos, convierte un círculo en un arco manteniendo la mayoría de las restricciones. {{Version/es|0.20}}


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_Extend.svg  style="width:32px;"> [Extender](Sketcher_Extend/es.md): Extiende una línea o un arco a una línea límite, arco, elipse, arco de elipse o un punto en el espacio.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_External.svg  style="width:32px;"> [Geometría externa](Sketcher_External/es.md): Crea una arista enlazada a geometría externa.


</div>

-   <img alt="" src=images/Sketcher_Projection.svg  style="width:32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> External geometry:

  - <img alt="" src=images/Sketcher_Projection.svg  style="width:32px;"> [Create external projection geometry](Sketcher_Projection.md): Creates the projection edges of external geometry. <small>(v1.1)</small> 

  - <img alt="" src=images/Sketcher_Intersection.svg  style="width:32px;"> [Create external intersection geometry](Sketcher_Intersection.md): Creates the intersection edges of external geometry with the sketch plane. <small>(v1.1)</small> 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_CarbonCopy.svg  style="width:32px;"> [CarbonoCopia](Sketcher_CarbonCopy/es.md): Copia la geometría de otro boceto.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_SelectOrigin.svg  style="width:32px;"> [Seleccionar el origen](Sketcher_SelectOrigin/es.md): Selecciona el origen del croquis


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_SelectHorizontalAxis.svg  style="width:32px;"> [Seleccionar el eje horizontal](Sketcher_SelectHorizontalAxis/es.md): Selecciona el eje horizontal del croquis


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_SelectVerticalAxis.svg  style="width:32px;"> [Seleccionar el eje vertical](Sketcher_SelectVerticalAxis/es.md): Selecciona el eje vertical del croquis


</div>

-   <img alt="" src=images/Sketcher_Translate.svg  style="width:32px;"> [Array transform](Sketcher_Translate.md): Moves or optionally creates copies of selected elements. <small>(v1.0)</small> 

-   <img alt="" src=images/Sketcher_Rotate.svg  style="width:32px;"> [Polar transform](Sketcher_Rotate.md): Rotates or optionally creates rotated copies of selected elements. <small>(v1.0)</small> 

-   <img alt="" src=images/Sketcher_Scale.svg  style="width:32px;"> [Scale transform](Sketcher_Scale.md): Scales or optionally creates scaled copies of selected elements. <small>(v1.0)</small> 

-   <img alt="" src=images/Sketcher_Offset.svg  style="width:32px;"> [Offset geometry](Sketcher_Offset.md): Creates equidistant edges around selected edges. <small>(v1.0)</small> 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_Symmetry.svg  style="width:32px;"> [Symmetría](Sketcher_Symmetry/es.md): Copia un elemento del croquis manteniéndolo simétrico a una línea seleccionada


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_RemoveAxesAlignment.svg  style="width:32px;"> [Eliminar la alineación de los ejes](Sketcher_RemoveAxesAlignment/es.md): Elimina la alineación de los ejes intentando conservar la relación de restricción de la selección {{Version/es|0.20}}


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_DeleteAllGeometry.svg  style="width:32px;"> [Eliminar toda la geometría](Sketcher_DeleteAllGeometry/es.md): Elimina toda la geometría del boceto.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_DeleteAllConstraints.svg  style="width:32px;"> [Eliminar todas las restricciones](Sketcher_DeleteAllConstraints/es.md): Elimina todas las restricciones del boceto.


</div>

-   <img alt="" src=images/Edit-copy.svg  style="width:32px;"> Copy in Sketcher: See [Copy, cut and paste](#Copy,_cut_and_paste.md).

-   <img alt="" src=images/Edit-cut.svg  style="width:32px;"> Cut in Sketcher: See [Copy, cut and paste](#Copy,_cut_and_paste.md).

-   <img alt="" src=images/Edit-paste.svg  style="width:32px;"> Paste in Sketcher: See [Copy, cut and paste](#Copy,_cut_and_paste.md).



### Herramientas B-spline de Croquizador 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_BSplineApproximate.svg  style="width:32px;"> [Convertir la geometría en B-spline](Sketcher_BSplineApproximate/es.md)


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_BSplineIncreaseDegree.svg  style="width:32px;"> [Aumentar el grado de B-spline](Sketcher_BSplineIncreaseDegree/es.md)


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_BSplineDecreaseDegree.svg  style="width:32px;"> [Disminuir el grado de la B-spline](Sketcher_BSplineDecreaseDegree/es.md), <small>(v0.19)</small> 


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_BSplineIncreaseKnotMultiplicity.svg  style="width:32px;"> [Aumentar la multiplicidad de nudos](Sketcher_BSplineIncreaseKnotMultiplicity/es.md)


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_BSplineDecreaseKnotMultiplicity.svg  style="width:32px;"> [Disminuir la multiplicidad de nudos](Sketcher_BSplineDecreaseKnotMultiplicity/es.md)


</div>

-   <img alt="" src=images/Sketcher_BSplineInsertKnot.svg  style="width:32px;"> [Insert knot](Sketcher_BSplineInsertKnot.md): Inserts a knot into a B-spline or increases the multiplicity of an existing knot.

-   <img alt="" src=images/Sketcher_JoinCurves.svg  style="width:32px;"> [Join curves](Sketcher_JoinCurves.md): Creates a B-spline by joining two existing B-splines or other edges. <small>(v0.21)</small> 

### Sketcher visual 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_SelectElementsWithDoFs.svg  style="width:32px;"> [Selecciona los DOF del solucionador](Sketcher_SelectElementsWithDoFs/es.md): Resalta en verde la geometría con grados de libertad (DOFs), es decir, no totalmente restringida.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_SelectConstraints.svg  style="width:32px;"> [Seleccione Restricciones](Sketcher_SelectConstraints/es.md): Selecciona las restricciones de un elemento de dibujo


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_SelectElementsAssociatedWithConstraints.svg  style="width:32px;"> [Seleccionar elementos asociados con restricciones](Sketcher_SelectElementsAssociatedWithConstraints/es.md): Seleccionar los elementos de bosquejo asociados a las restricciones


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_SelectRedundantConstraints.svg  style="width:32px;"> [Seleccionar restricciones redundantes](Sketcher_SelectRedundantConstraints/es.md): Selecciona las restricciones redundantes del croquis


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_SelectConflictingConstraints.svg  style="width:32px;"> [Seleccionar restricciones conflictivas](Sketcher_SelectConflictingConstraints/es.md): Selecciona las restricciones conflictivas del croquis


</div>

-   <img alt="" src=images/Sketcher_ArcOverlay.svg  style="width:32px;"> [Show/hide circular helper for arcs](Sketcher_ArcOverlay.md): Shows or hides the circular helpers (underlying virtual circles) for arcs in all sketches. <small>(v1.0)</small> 

-   <img alt="" src=images/Sketcher_BSplinePolygon.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Show/hide B-spline information layer:


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_BSplineDegree.svg  style="width:32px;"> [Mostrar/ocultar el grado de B-spline](Sketcher_BSplineDegree/es.md)


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_BSplinePolygon.svg  style="width:32px;"> [Mostrar/ocultar el polígono de control de la B-spline](Sketcher_BSplinePolygon/es.md)


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_BSplineComb.svg  style="width:32px;"> [Mostrar/ocultar peine de curvatura B-spline](Sketcher_BSplineComb/es.md)


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_BSplineKnotMultiplicity.svg  style="width:32px;"> [Mostrar/ocultar multiplicidad de nudos B-spline](Sketcher_BSplineKnotMultiplicity/de.md)


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_BSplinePoleWeight.svg  style="width:32px;"> [Mostrar/ocultar el peso del punto de control de la B-spline](Sketcher_BSplinePoleWeight/es.md), <small>(v0.19)</small> 


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_RestoreInternalAlignmentGeometry.svg  style="width:32px;"> [Mostrar/Ocultar geometría interna](Sketcher_RestoreInternalAlignmentGeometry/es.md): Recrea la geometría interna que falta/elimina la innecesaria de una elipse, arco de elipse/hiperbola/parábola o B-spline seleccionados.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_SwitchVirtualSpace.svg  style="width:32px;"> [Cambiar el espacio virtual](Sketcher_SwitchVirtualSpace/es.md): Permite ocultar todas las restricciones de un boceto y hacerlas visibles de nuevo.


</div>

### Obsolete tools 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_Clone.svg  style="width:32px;"> [Clonar](Sketcher_Clone/es.md): Clona un elemento del croquis


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_CloseShape.svg  style="width:32px;"> [Forma cercana](Sketcher_CloseShape/es.md): Crea una forma cerrada aplicando restricciones coincidentes a los puntos finales


</div>

-   <img alt="" src=images/Sketcher_CreatePointFillet.svg  style="width:32px;"> [Corner-preserving fillet](Sketcher_CreatePointFillet.md): Creates a fillet between two non-parallel lines while preserving their corner point. Not available in <small>(v1.0)</small> .


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ConnectLines.svg  style="width:32px;"> [Conecta los bordes](Sketcher_ConnectLines/es.md): Conectar los elementos del esbozo aplicando restricciones coincidentes a los puntos finales


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_Copy.svg  style="width:32px;"> [Copiar](Sketcher_Copy/es.md): Copia un elemento del croquis


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_Move.svg  style="width:32px;"> [Muévete](Sketcher_Move/es.md): Mueve la geometría seleccionada tomando como referencia el último punto seleccionado.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_RectangularArray.svg  style="width:32px;"> [ordenación rectangular](Sketcher_RectangularArray/es.md): Crea un conjunto de elementos seleccionados de croquis


</div>




<div class="mw-translate-fuzzy">

### Preferencias


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Preferences-general.svg  style="width:32px;"> [Preferencias](Sketcher_Preferences/es.md): Preferencias para el ambiente de trabajo *Croquis*.


</div>

## Best practices 


<div class="mw-translate-fuzzy">

## Buenas practicas 

Cada usuario de CAD desarrolla su propia forma de trabajar a lo largo del tiempo, pero hay algunos principios generales útiles a seguir.


</div>


<div class="mw-translate-fuzzy">

-   Una serie de croquis simples es más sencilla de manejar que un croquis complejo. Por ejemplo, un primer croquis se puede crear para la operación base 3D (ya sea un saliente o una revolución), mientras una segunda puede contener taladros o cajeras. Algunos detalles se pueden dejar fuera, para realizar luego como operaciones 3D. Puedes elegir evitar los redondeos en tu croquis si son muchos, y añadirlos como una operación 3D.

-   Crea siempre un perfil cerrado, o tu croquis no producirá un sólido, sino un conjunto de caras abiertas. Si no quieres que alguno de los objetos sea incluido en la creación del sólido, cámbialos a elementos de construcción con la herramienta de Modo de Contrucción.

-   Utiliza las restricciones automáticas para limitar el número de restricciones que tendrás que añadir manualmente.

-   Como regla general, aplica las restricciones geométricas primero, luego las restricciones dimensionales, y bloquea tu croquis al final. Pero recuerda: Las reglas se hacen para romperlas. Si tienes problemas manipulando tu croquis, puede ser útil restringir algunos objetos antes de completar el perfil.

-   Si es posible, centra tu croquis en el origen (0,0) con la restricción de bloqueo. Si tu croquis no es simétrico, ubica uno de sus puntos en el origen, o selecciona un buen número para las distancias de bloqueo. En la v0.12, las restricciones externas (restringiendo el croquis con respecto a geometría 3D como aristas u otros croquis) no están implementada. Esto significa q2ue para ubicar las siguientes geometrías de croquis a tu primer croquis, necesitaras definir distancias relativas a tu primer croquis manualmente. Una restricción de bloqueo de (25,75) desde el origen es más fácil de recordar que (23.47,73.02).

-   Si tienes la posibilidad de seleccionar entre la Restricción Distancia y las restricciones de Distancia Vertical o Distancia Horizontal, es mejor que utilices las últimas pues se comportan mejor a nivel de consumo de memoria.

-   En general, las mejores restricciones a utilizar son: Restricciones horizontales/verticales; Restricciones de distancia horizontal o vertical y tangencia en puntos finales. De ser posible, conviene limitar el uso de: Restricciones de Distancia; tangencia entre aristas; Punto en Objeto y simetría.

-   Si tiene dudas sobre la validez de un boceto una vez completado (las características se vuelven verdes), cierre el cuadro de diálogo Sketcher, cambie al <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Ambiente de trabajos piezas](Part_Workbench/es.md) y ejecuta **[<img src=images/Part_CheckGeometry.svg style="width:16px"> [Comprobar geometría](Part_CheckGeometry/es.md)**.


</div>



## Tutoriales


<div class="mw-translate-fuzzy">

-   [Tutorial de croquis](https://forum.freecadweb.org/viewtopic.php?f=36&t=30104) por Chrisb. Este es un documento PDF de 70 páginas que sirve como un manual detallado para el croquis. Explica los fundamentos del uso del croquis, y entra en muchos detalles sobre la creación de formas geométricas, y cada una de las restricciones.
-   [Tutorial básico de dibujo](Basic_Sketcher_Tutorial/es.md) para principiantes
-   [Coquis Micro Tutorial - Prácticas de Restricción](Sketcher_Micro_Tutorial_-_Constraint_Practices/es.md)
-   [Requisito por un boceto](Sketcher_requirement_for_a_sketch/es.md) Requisito mínimo de un boceto y determinación completa de un boceto


</div>



## Guión

La página [Croquizador Guión](Sketcher_scripting/es.md) contiene ejemplos sobre cómo crear restricciones a partir de scripts de Python.

## Examples

For some ideas of what can be achieved with Sketcher tools, have a look at: [Sketcher examples](Sketcher_Examples.md).

<img alt="" src=images/Sketcher_ExampleHinge-01.gif  style="width:80px;"> <img alt="" src=images/Sketcher_ExampleHinge-15.png  style="width:90px;">





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > [Sketcher](Category_Sketcher.md) > Sketcher Workbench/es
