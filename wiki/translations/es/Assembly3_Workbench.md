

<img alt="Assembly3 workbench icon" src=images/Assembly3_workbench_icon.svg  style="width:128px;">


{{TOCright}}

## Introducción

<img alt="" src=images/Assembly3_workbench_icon.svg  style="width:24px;"> [Assembly3](Assembly3_Workbench/es.md) es un [Ambiente de trabajo externo](External_workbenches/es.md) que se utiliza para realizar el ensamblaje de diferentes cuerpos contenidos en un único archivo o en múltiples documentos. El ambiente de trabajo se basa en varios cambios en las funciones principales realizados para la versión de FreeCAD 0.19 (por ejemplo, [Enlace Aplicación](App_Link/es.md)), por lo que el ambiente de trabajo Assembly3 no puede utilizarse con versiones anteriores.

Las principales características del Assembly3 Ambiente de trabajo son

-   **Solver dinámico/interactivo**. Esto significa que puede mover las piezas con el ratón mientras el solucionador restringe el movimiento. Esto permite, por ejemplo, conectar una rueda a un eje y girar la rueda interactivamente con el ratón.
-   **Enlaces**\'. Esto significa que puede utilizar una sola pieza, por ejemplo, un tornillo, varias veces en un conjunto (en diferentes lugares) sin duplicar la geometría.
-   **Enlaces externos**. Es posible tener un documento freecad que sólo contenga un ensamblaje y no piezas. Todas las piezas podrían estar en archivos individuales. Los archivos pueden estar incluso en una biblioteca o en cualquier otro lugar del sistema de archivos. El único requisito es que el archivo debe ser cargado cuando se hace el enlace. Una vez realizado el enlace, el archivo debe estar abierto para realizar las actualizaciones de los enlaces que implican al archivo. Assembly3 resuelve esto abriendo los archivos en segundo plano según sea necesario.
-   **Montajes jerárquicos**. Como en la vida real, un ensamblaje mecánico puede estar formado por subensamblajes. Estos pueden consistir en sub-ensamblajes de nuevo y así sucesivamente.
-   **Congelación de conjuntos**. Como la CPU sólo puede manejar un número determinado de restricciones concurrentes en tiempo real, congelar un ensamblaje permite utilizar restricciones incluso para ensamblajes grandes. Al congelar los conjuntos terminados o las restricciones que no deben permanecer dinámicas (por ejemplo, las piezas soldadas, atornilladas o pegadas), éstas se excluyen de los cálculos de actualización y el solucionador de Assembly3 las considera geometría fija.

    :   Tenga en cuenta que otros enfoques ofrecen una solución diferente a este problema, por ejemplo, el <img alt="" src=images/Assembly4_workbench_icon.svg  style="width:24px;"> [Ambiente de trabajo de Assembly4](Assembly4_Workbench.md).

[inicio](#top.md)

### Barras de herramientas 

A partir de 2020, el ambiente de trabajo Assembly3 cuenta con las siguientes barras de herramientas.

#### Barra de herramientas principal 

:   <img alt="" src=images/Assembly3_ToolbarMain.png  style="width:700px;">


<div class="mw-collapsible mw-collapsed">

La **Barra Herramienta principal** contiene herramientas que cubren las funciones más utilizadas del ambiente de trabajo. La información sobre las herramientas le dará los atajos de teclado.


<div class="mw-collapsible-content toccolours">

:\* <img alt="" src=images/Assembly_New_Assembly.svg‎‎  style="width:32px;"> [Create assembly](Assembly3_CreateAssembly.md): Add an assembly folder

:\* <img alt="" src=images/Assembly_New_Group.svg‎‎  style="width:32px;"> [Group objects](Assembly3_GroupObjects.md): Group objects

:\* <img alt="" src=images/Assembly_New_Element.svg‎‎  style="width:32px;"> [Create element](Assembly3_CreateElement.md): Create element.

:\* Import from STEP. This has two settings

:\*\* <img alt="" src=images/Assembly_Import.svg‎‎  style="width:32px;"> [Import from STEP](Assembly3_ImportFromSTEP.md): Import STEP files

:\*\* <img alt="" src=images/Assembly_ImportMulti.svg‎‎  style="width:32px;"> [Import as multi-document](Assembly3_ImportMultiDocument.md): Import assemblies from STEP into separate documents

:\* <img alt="" src=images/Assembly3_workbench_icon.svg‎‎  style="width:32px;"> [Resolve constraints](Assembly3_ResolveConstraints.md): Resolve constraints

:\* <img alt="" src=images/Assembly_QuickSolve.svg‎‎  style="width:32px;"> [Quick solve](Assembly3_QuickSolve.md): Quick resolve constraints

:\* <img alt="" src=images/Assembly_Move.svg‎‎  style="width:32px;"> [Move part](Assembly3_MovePart.md): Move parts in 3D, this is specific to Assembly3

:\* <img alt="" src=images/Assembly_AxialMove.svg‎‎  style="width:32px;"> [Axial move](Assembly3_AxialMove.md): Axial move parts in 3D, this is the classical tool available elsewhere in FreeCAD

:\* <img alt="" src=images/Assembly_QuickMove.svg‎‎  style="width:32px;"> [Quick move](Assembly3_QuickMove.md): This will attach the part selected in the tree to the mouse cursor. It will change the position of the part when you click.

:\*: Often added parts are stacked upon each other in the origin. Use this function to grab a part you can not see.

:\* <img alt="" src=images/Assembly_LockMover.svg‎‎  style="width:32px;"> [Lock mover](Assembly3_LockMover.md): Lock mover for fixed part. Toggle Button. When this is un-selected you can move the parts that have a \"Locked\" constraint.

:\* <img alt="" src=images/Assembly_TogglePartVisibility.svg‎‎  style="width:32px;"> [Toggle part visibility](Assembly3_TogglePartVisibility.md): This toggles the visiblity of the selected part on/off.

:\*: Note that this differs from using space. Using space with selected items from a sub-assembly in the 3D view often does not behave as expected. Use this function in those cases (or shortcut A-Space)

:\* <img alt="" src=images/Assembly_Trace.svg‎‎  style="width:32px;"> [Trace part move](Assembly3_TracePartMove.md): Trace part move (TBD)

:\* <img alt="" src=images/Assembly_AutoRecompute.svg‎‎  style="width:32px;"> [Auto recompute](Assembly3_AutoRecompute.md): Auto recompute. Usually enabled.

:\*: May be un-selected when repairing constraints or fixing parts where the solver gives a *\"do not converge\"* message (e.g. by turning the part 180deg)

:\* <img alt="" src=images/Assembly_SmartRecompute.svg‎‎  style="width:32px;"> [Smart recompute](Assembly3_SmartRecompute.md): Smart recompute. Usually enabled.

:\* <img alt="" src=images/Assembly_AutoFixElement.svg‎‎  style="width:32px;"> [Auto fix element](Assembly3_AutoFixElement.md): Element Auto Fixing. Experimental feature in 0.19\_pre

:\* Element Style. This has two settings

:\*\* <img alt="" src=images/Assembly_AutoElementVis.svg‎‎  style="width:32px;"> [Auto element visibility](Assembly3_AutoElementVisibility.md): Auto element visibility

:\*\* <img alt="" src=images/Assembly_ShowElementCS.svg‎‎  style="width:32px;"> [Show element coordinate system](Assembly3_ShowElementCS.md): Show element coordinate system

:\* Workplane and origin. Adds a workplane, placement or origin. A part must be selected. This has five settings

:\*\* <img alt="" src=images/Assembly_Add_Workplane.svg‎‎  style="width:32px;"> [Add workplane](Assembly3_AddXYWorkplane.md): Add XY workplane

:\*\* <img alt="" src=images/Assembly_Add_WorkplaneXZ.svg‎‎  style="width:32px;"> [Add XZ workplane](Assembly3_AddXZWorkplane.md): Add XZ workplane

:\*\* <img alt="" src=images/Assembly_Add_WorkplaneZY.svg‎‎  style="width:32px;"> [Add ZY workplane](Assembly3_AddZYWorkplane.md): Add YZ workplane

:\*\* <img alt="" src=images/Assembly_Add_Placement.svg‎‎  style="width:32px;"> [Add placement](Assembly3_AddPlacement.md): Add placement

:\*\* <img alt="" src=images/Assembly_Add_Origin.svg‎‎  style="width:32px;"> [Add Origin](Assembly3_AddOrigin.md): Add Origin

:\* <img alt="" src=images/Assembly_TreeItemUp.svg‎‎  style="width:32px;"> [Move item up](Assembly3_MoveItemUp.md): Move selected tree item up

:\* <img alt="" src=images/Assembly_TreeItemDown.svg‎‎  style="width:32px;"> [Move item down](Assembly3_MoveItemDown.md): Move selected tree item down

:\*: Allows to sort Parts, Elements or Constraints in the tree. Element roll over (top to bottom and vice versa). Only works for a single selection.

:\* <img alt="" src=images/Assembly_ConstraintMultiply.svg‎‎  style="width:32px;"> [Multiply constraint](Assembly3_MultiplyConstraint.md): Multiply Constraint. This can be selected if multiple parts and suitable Elements are present.

:\*: It is used e.g. to assign multiple fasteners of the same type into multiple holes with one constraint.


</div>


</div>


<div class="mw-translate-fuzzy">

#### Barra de herramientas de restricciones principales 

:   <img alt="" src=images/Assembly3_ToolbarConstraints_1.jpg  style="width:700px;">


</div>


:   <img alt="" src=images/Assembly_ConstraintLock.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintAlignment.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintCoincidence.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintAttachment.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintAxial.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintSameOrientation.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintMultiParallel.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintAngle.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintPerpendicular.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintPointCoincident.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintPointInPlane.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintPointOnLine.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintPointOnCircle.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintPointsDistance.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintPointPlaneDistance.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintPointLineDistance.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintSymmetric.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintMore.svg‎‎  style="width:28px;">


<div class="mw-collapsible mw-collapsed">


:   Some tools are actually a menu for more tools.


<div class="mw-collapsible-content toccolours">

:\* <img alt="" src=images/Assembly_ConstraintLock.svg‎‎  style="width:32px;"> [Locked](Assembly3_ConstraintLock.md): Add a \"Locked\" constraint to fix one or more parts.

:\*: You must select a geometry element of the part.

:\*: If you fix a vertex or an edge the part is still free to rotate around the vertex or edge.

:\*: Fixing a face will completely lock the part.

:\* <img alt="" src=images/Assembly_ConstraintAlignment.svg‎‎  style="width:32px;"> [Plane Alignment](Assembly3_ConstraintAlignment.md): Add a \"Plane alignment\" constraint to align planar faces of two or more parts.

:\*: The faces become coplanar or parallel with an optional distance.

:\* <img alt="" src=images/Assembly_ConstraintCoincidence.svg‎‎  style="width:32px;"> [Plane Coincidence](Assembly3_ConstraintCoincidence.md): Add a \"Plane coincidence\" constraint to coincide planar faces of two or more parts.

:\*: The faces are coincided at their centers with an optional distance.

:\* <img alt="" src=images/Assembly_ConstraintAttachment.svg‎‎  style="width:32px;"> [Attachment](Assembly3_ConstraintAttachment.md): Add an \"Attachment\" constraint to attach two parts by the selected geometry elements.

:\*: This constraint completely fixes the parts relative to each other.

:\* <img alt="" src=images/Assembly_ConstraintAxial.svg‎‎  style="width:32px;"> [Axial Alignment](Assembly3_ConstraintAxial.md): Add an \"Axial alignment\" constraint to align edges/faces of two or more parts.

:\*: The constraint accepts

:\*:: linear edges, which become collinear,

:\*:: planar faces, which are aligned using their surface normal axis,

:\*:: and cylindrical face, which are aligned using the axial direction.

:\*: Different types of geometry elements can be mixed.

:\* <img alt="" src=images/Assembly_ConstraintSameOrientation.svg‎‎  style="width:32px;"> [Same orientation](Assembly3_ConstraintSameOrientation.md): Add a \"Same orientation\" constraint to align faces of two or more parts.

:\*: The planes are aligned to have the same orientation (i.e. rotation)

:\* <img alt="" src=images/Assembly_ConstraintMultiParallel.svg‎‎  style="width:32px;"> [Multi parallel](Assembly3_ConstraintMultiParallel.md): Add a \"Multi parallel\" constraint to make planar faces or linear edges of two or more parts parallel.

:\* <img alt="" src=images/Assembly_ConstraintAngle.svg‎‎  style="width:32px;"> [Angle](Assembly3_ConstraintAngle.md): Add an \"Angle\" constraint to set the angle of planar faces or linear edges of two parts.

:\* <img alt="" src=images/Assembly_ConstraintPerpendicular.svg‎‎  style="width:32px;"> [Perpendicular](Assembly3_ConstraintPerpendicular.md): Add a \"Perpendicular\" constraint to make planar faces or linear edges of two parts perpendicular.

:\* <img alt="" src=images/Assembly_ConstraintPointCoincident.svg‎‎  style="width:32px;"> [Points coincident](Assembly3_ConstraintPointsCoincident.md): Add a \"Point coincident\" constraint to coincide two points in 2D or 3D.

:\* <img alt="" src=images/Assembly_ConstraintPointInPlane.svg‎‎  style="width:32px;"> [Point on plane](Assembly3_ConstraintPointInPlane.md): Add a \"Point on plane\" to constrain one or more point onto a plane.

:\* <img alt="" src=images/Assembly_ConstraintPointOnLine.svg‎‎  style="width:32px;"> [Point on line](Assembly3_ConstraintPointOnLine.md): Add a \"Point on line\" to constrain a point onto a line in 2D or 3D.

:\* <img alt="" src=images/Assembly_ConstraintPointOnCircle.svg‎‎  style="width:32px;"> [Point on circle](Assembly3_ConstraintPointOnCircle.md): Add a \"Point on circle\" to constrain one or more points on to a clyndrical surface defined by a cricle.

:\*: Note that you must select a point (any geometry element can define a point), and then select the circle (or clyndrical surface),

:\*: after which you can add more points to your selection if you want.

:\* <img alt="" src=images/Assembly_ConstraintPointsDistance.svg‎‎  style="width:32px;"> [Points distance](Assembly3_ConstraintPointsDistance.md): Add a \"Points distance\" to constrain the distance of two or more points.

:\* <img alt="" src=images/Assembly_ConstraintPointPlaneDistance.svg‎‎  style="width:32px;"> [Point plane distance](Assembly3_ConstraintPointPlaneDistance.md): Add a \"Point plane distance\" to constrain the distance between one or more points and a plane.

:\* <img alt="" src=images/Assembly_ConstraintPointLineDistance.svg‎‎  style="width:32px;"> [Point line distance](Assembly3_ConstraintPointLineDistance.md): Add a \"Point line distance\" to constrain the distance between a point and a linear edge in 2D or 3D.

:\* <img alt="" src=images/Assembly_ConstraintSymmetric.svg‎‎  style="width:32px;"> [Symmetric](Assembly3_ConstraintSymmetric.md): Add a \"Symmetric\" constraint to make geometry elements of two parts symmetric about a plane.

:\*: The supported elements are linear edge and planar face.

:\* <img alt="" src=images/Assembly_ConstraintMore.svg‎‎  style="width:32px;"> [More](Assembly3_ConstraintMore.md): Toggle toolbars for more constraints

:\*: Not really a constraint but a toggle switch to show/hide the **Additional Constraints Toolbars**.


</div>


</div>


<div class="mw-translate-fuzzy">

#### Barras Herramienta de restricciones adicionales 

:   <img alt="" src=images/Assembly3_ToolbarConstraints_2.jpg  style="width:700px;">


</div>


:   <img alt="" src=images/Assembly_ConstraintPointDistance.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintEqualAngle.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintPointsSymmetric.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintGeneral.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintGeneral.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintSymmetricLine.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintPointsHorizontal.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintPointsVertical.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintLineHorizontal.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintLineVertical.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintArcLineTangent.svg‎‎  style="width:28px;"> (Assembly3 Constraints2)





:   <img alt="" src=images/Assembly_ConstraintSketchPlane.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintLineLength.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintEqualLength.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintLengthRatio.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintLengthDifference.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintLengthEqualPointLineDistance.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintEqualLineArcLength.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintMidPoint.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintDiameter.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintEqualRadius.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintPointsProjectDistance.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintEqualPointLineDistance.svg‎‎  style="width:28px;"> <img alt="" src=images/Assembly_ConstraintColinear.svg‎‎  style="width:28px;"> (Assembly3 Sketch Constraints)


<div class="mw-collapsible mw-collapsed">


:   You can enable these by selecting the **<img src="images/Assembly_ConstraintMore.svg‎‎" width=16px> [More](Assembly3_ConstraintMore.md)** button on the Main Constraints toolbar.


<div class="mw-collapsible-content toccolours">

:\* <img alt="" src=images/Assembly_ConstraintPointDistance.svg‎‎  style="width:32px;"> [Point distance](Assembly3_ConstraintPointDistance.md): Add a \"Point distance\" to constrain the distance of two points in 2D or 3D.

:\* <img alt="" src=images/Assembly_ConstraintEqualAngle.svg‎‎  style="width:32px;"> [Equal angle](Assembly3_ConstraintEqualAngle.md): Add an \"Equal angle\" to equate the angles between two lines or normals.

:\* <img alt="" src=images/Assembly_ConstraintPointsSymmetric.svg‎‎  style="width:32px;"> [Points symmetric](Assembly3_ConstraintPointsSymmetric.md): Add a \"Points symmetric\" constraint to make two points symmetric about a plane.

:\* <img alt="" src=images/Assembly_ConstraintGeneral.svg‎‎  style="width:32px;"> () [Symmetric horizontal](Assembly3_ConstraintSymmetricHorizontal.md): Symmetric horizontal

:\* <img alt="" src=images/Assembly_ConstraintGeneral.svg‎‎  style="width:32px;"> () [Symmetric vertical](Assembly3_ConstraintSymmetricVertical.md): Symmetric vertical

:\* <img alt="" src=images/Assembly_ConstraintSymmetricLine.svg‎‎  style="width:32px;"> [Symmetric line](Assembly3_ConstraintSymmetricLine.md): Add a \"Symmetric line\" constraint to make two points symmetric about a line.

:\* <img alt="" src=images/Assembly_ConstraintPointsHorizontal.svg‎‎  style="width:32px;"> [Points horizontal](Assembly3_ConstraintPointsHorizontal.md): Add a \"Points horizontal\" constraint to make two points horizontal with each other when projected onto a plane.

:\* <img alt="" src=images/Assembly_ConstraintPointsVertical.svg‎‎  style="width:32px;"> [Points vertical](Assembly3_ConstraintPointsVertical.md): Add a \"Points vertical\" constraint to make two points vertical with each other when projected onto a plane.

:\* <img alt="" src=images/Assembly_ConstraintLineHorizontal.svg‎‎  style="width:32px;"> [Line horizontal](Assembly3_ConstraintLineHorizontal.md):Add a \"Line horizontal\" constraint to make a line segment horizontal when projected onto a plane.

:\* <img alt="" src=images/Assembly_ConstraintLineVertical.svg‎‎  style="width:32px;"> [Line vertical](Assembly3_ConstraintLineVertical.md): Add a \"Line vertical\" constraint to make a line segment vertical when projected onto a plane.

:\* <img alt="" src=images/Assembly_ConstraintArcLineTangent.svg‎‎  style="width:32px;"> [Arc line tangent](Assembly3_ConstraintArcLineTangent.md): Add an \"Arc line tangent\" constraint to make a line tangent to an arc at the start or end point of the arc.

:\* <img alt="" src=images/Assembly_ConstraintSketchPlane.svg‎‎  style="width:32px;"> [Sketch plane](Assembly3_ConstraintSketchPlane.md): Add a \"Sketch plane\" to define the work plane of any draft element inside or following this constraint.

:\*: Add an empty \"Sketch plane\" to undefine the previous work plane.

:\* <img alt="" src=images/Assembly_ConstraintLineLength.svg‎‎  style="width:32px;"> [Line length](Assembly3_ConstraintLineLength.md): Add a \"Line length\" constrain the length of a non-subdivided Draft.Wire.

:\* <img alt="" src=images/Assembly_ConstraintEqualLength.svg‎‎  style="width:32px;"> [Equal length](Assembly3_ConstraintEqualLength.md): Add an \"Equal length\" constraint to make two lines of the same length.

:\* <img alt="" src=images/Assembly_ConstraintLengthRatio.svg‎‎  style="width:32px;"> [Length ratio](Assembly3_ConstraintLengthRatio.md): Add a \"Length ratio\" to constrain the length ratio of two lines.

:\* <img alt="" src=images/Assembly_ConstraintLengthDifference.svg‎‎  style="width:32px;"> [Length difference](Assembly3_ConstraintLengthDifference.md): Add a \"Length difference\" to constrain the length difference of two lines.

:\* <img alt="" src=images/Assembly_ConstraintLengthEqualPointLineDistance.svg‎‎  style="width:32px;"> [Length Equal Point Line Distance](Assembly3_ConstraintLengthEqualPointLineDistance.md): Add a \"Length Equal Point Line Distance\" to constrain the distance

:\*: between a point and a line to be the same as the length of a another line.

:\* <img alt="" src=images/Assembly_ConstraintGeneral.svg‎‎  style="width:32px;"> ( <img alt="" src=images/Assembly_ConstraintEqualLineArcLength.svg‎‎  style="width:32px;"> )[Equal Line Arc Length](Assembly3_ConstraintEqualLineArcLength.md): Add an \"Equal Line Arc Length\" constraint to make a line of the same length as an arc.

:\* <img alt="" src=images/Assembly_ConstraintMidPoint.svg‎‎  style="width:32px;"> [Mid point](Assembly3_ConstraintMidPoint.md): Add a \"Mid point\" to constrain a point to the middle point of a line.

:\* <img alt="" src=images/Assembly_ConstraintDiameter.svg‎‎  style="width:32px;"> [Diameter](Assembly3_ConstraintDiameter.md): Add a \"Diameter\" to constrain the diameter of a circle/arc.

:\* <img alt="" src=images/Assembly_ConstraintEqualRadius.svg‎‎  style="width:32px;"> [Equal radius](Assembly3_ConstraintEqualRadius.md): Add an \"Equal radius\" constraint to make two circles/arcs of the same radius.

:\* <img alt="" src=images/Assembly_ConstraintPointsProjectDistance.svg‎‎  style="width:32px;"> [Points project distance](Assembly3_ConstraintPointsProjectDistance.md): Add a \"Points project distance\" to constrain the distance of two points projected on a line.

:\* <img alt="" src=images/Assembly_ConstraintEqualPointLineDistance.svg‎‎  style="width:32px;"> [Equal point line distance](Assembly3_ConstraintEqualPointLineDistance.md): Add an \"Equal point line distance\" to constrain the distance

:\*: between a point and a line to be the same as the distance between another point and line.

:\* <img alt="" src=images/Assembly_ConstraintColinear.svg‎‎  style="width:32px;"> [Colinear](Assembly3_ConstraintColinear.md): Add a \"Colinear\" constraint to make two lines collinear.


</div>


</div>


:   The **Constraints Toolbars** will be the main interface used when assembling parts.
:   They are greyed out by default but are activated once at least one face, line or point of a part is selected.
:   Generally you select the Elements that should be joined and then select the constraint type.
:   The different colored frames mark different characteristics of the constraints:

    :   whether 2D/3D of if more than 2 Elements can be added.
:   A detailed description can be found in the Github wiki.


<div class="mw-translate-fuzzy">

#### Barra Herramienta de navegación 

:   <img alt="" src=images/Assembly3_ToolbarNavigation.jpg  style="width:100px;">


</div>


<div class="mw-collapsible mw-collapsed">


:   Theses functions are useful when working with an assembly with a hierarchy of linked external files


<div class="mw-collapsible-content toccolours">

:\* <img alt="" src=images/Assembly_GotoRelation.svg‎‎  style="width:32px;"> [Go to relation](Assembly3_GoToRelation.md): Reveals the Relations group (hidden by default) and selects a relation object.

:\* <img alt="" src=images/Std_LinkSelectLinked.svg  style="width:32px;"> [Select linked object](Std_LinkSelectLinked.md): Selects the linked object and switches to its document. <small>(v0.19)</small> 

:\* <img alt="" src=images/Std_LinkSelectLinkedFinal.svg  style="width:32px;"> [Select linked final](Std_LinkSelectLinkedFinal.md): Selects the deepest linked object and switches to its document. <small>(v0.19)</small> 


</div>


</div>


<div class="mw-translate-fuzzy">

#### Barra Herramienta de medición 

:   <img alt="" src=images/Assembly3_ToolbarMeasurement.jpg  style="width:150px;">


</div>


:   <img alt="" src=images/Assembly_MeasurePointDistance.svg‎‎  style="width:28px;"> <img alt="" src=images/_Assembly_MeasurePointLineDistance.svg‎‎  style="width:28px;"> <img alt="" src=images/_Assembly_MeasurePointPlaneDistance.svg‎‎  style="width:28px;"> <img alt="" src=images/_Assembly_MeasureAngle.svg‎‎  style="width:28px;">


<div class="mw-collapsible mw-collapsed">


:   The **Measurement toolbar** adds functions to measure the distance or the angle between two objects


<div class="mw-collapsible-content toccolours">

:\* <img alt="" src=images/Assembly_MeasurePointDistance.svg‎‎  style="width:32px;"> [Measure points](Assembly3_MeasurePoints.md): Add a \"Measure points\" to measure the distance of two points in 2D or 3D.

:\* <img alt="" src=images/Assembly_MeasurePointLineDistance.svg‎‎  style="width:32px;"> [Measure point to line](Assembly3_MeasurePointLine.md): Add a \"Measure point to line\" to measure the distance between a point and a linear edge in 2D or 3D.

:\* <img alt="" src=images/Assembly_MeasurePointPlaneDistance.svg‎‎  style="width:32px;"> [Measure point to plane](Assembly3_MeasurePointPlane.md): Add a \"Measure point to plane\" to measure the distance between a point and a plane.

:\* <img alt="" src=images/Assembly_MeasureAngle.svg‎‎  style="width:32px;"> [Measure angle](Assembly3_MeasureAngle.md): Add a \"Measure angle\" to measure the angle of planar faces or linear edges of two parts.

:   There is no function to measure a radius or diameter.
:   The measurement tools survive part changes, e.g. the distance between edges of a cube when the cube is re-sized.
:   As the constraints the calculations are done in real time and updated upon any change. Behind the scenes, the function is very similar to the [constraints](#Constraints.md). The distance or angle is calculated between [Elements](#Elements.md) in the same way as for [constraints](#Constraints.md). The display in the tree works in the same way.


</div>


</div>

As usual you can modify the tool bars and add or remove single tools. Be sure to check the menu Assembly3 for functions that may not be present in the tool bars.

[top](#top.md)

### Restricciones

El diseñador utiliza las restricciones para conseguir el resultado deseado en la relación de dos partes. El arte consiste en la selección de las restricciones adecuadas que mejor se adaptan a cada problema. Cada GL (grado de libertad) eliminado debería, en teoría, ser eliminado sólo una vez entre dos objetos, pero en la práctica, con muchas herramientas CAD, las restricciones seleccionadas causan combinaciones de exceso de restricciones, a menudo compensadas por complejos algoritmos, a veces no. Assembly3 utiliza algoritmos para detectar y compensar el exceso de restricciones, pero es evidente que aún no están muy maduros. Así que en la práctica, para Assembly3 las restricciones evitan problemas al ser conscientes de cuántos grados de libertad (GL) se han utilizado y cuáles quedan por bloquear mediante restricciones. Ninguna pieza debería tener una conexión por restricciones que utilice más de 6GL.

:   Note: If the solver meets a combination that can not be solved, it will give an error. It is very difficult for the solver to find out what caused the problem, so typically from this error given it will not be clear *where* the problem is. In larger assemblies this can lead to complex problem searches. Unfortunately there is no easy way to avoid this. However, it helps to be fully aware how the system works (.e.g see [Elements](#Elements.md) below), use clear names for all components involved and only ever add additional constraints when the solver solves the current assembly. Very helpful to track down a problem is the \"ContexMenu/Deactivate\" function of each Constraint.

Assembly3 Constraints define restrictions in the position or orientation between two [Elements](#Elements.md). Some constraints even work with more than two [Elements](#Elements.md). An [Elements](#Elements.md) can be a face, a line or edge or a point of a part. Generally constraints are defined by selecting the desired [Elements](#Elements.md) and then select the constraint from the Constraints [toolbar](#Toolbars.md).

-   Fixes 6 DOF, leaves 0 DOF:
    -   **Lock**: The lock constraint fixes all DOFs for a face. It should be used for one base part in each assembly. You may also want to enable the \"MoveLock\" function (in the tool bar) so that the part can not be moved accidentially. Normally it does not matter which face/line/point you use to fix a part. Also note that the lock is only valid for the direct assembly, i.e. in case of a sub-assembly the parent assembly would still require a locked part on its own.
    -   **Attachment**: Makes both elements coordinate systems equal for all axes. This is computation wise the most inexpensive function and should be used where ever possible. Note that you could use the element properties to compensate for offsets and angles if the two [elements](#Elements.md) are not perfectly aligned.
-   Fixes 5 DOF, leaves 1 DOF:
    -   **Plane Coincident**: fixes Tx,Ty,Tz, Rx,Ry. Only Rz is free. There remains the rotation around the normal passing through the ''center of the plane''.
-   Fixes 4 DOF, leaves 2 DOF:
    -   **Axial Alignment**: fixes Tx,Ty, Rx,Ry. Only Tz, Rz are free. There remains the rotation around the axis of the shape and the translation along this same axis. Two *PointOnLine* constraints (if the two points are different) give the same result. The \''Colinear\'' constraint too.
    -   **PointOnLine**: This eliminates the translation and rotation along the normals to the reference line. Only the translation and rotation along the line axis is allowed.
-   Fixes 3 DOF, leaves 3 DOF:
    -   **Same Orientation**: fixes Rx,Rz,Rz. All T\'s remain free.
    -   **Points Coincident**: fixes Tx,Ty,Tz. All R\'s remain free.
    -   **PointOnPoint** constraint eliminates the 3 translations.
    -   **Plane Alignment**: fixes Tz, Rx,Ry. In plane motion and Rz. This eliminates the translation along the normal to the reference plane and the two rotations around the axes of this plane.
-   Fixes 2 DOF, leaves 4 DOF:
    -   **Multi Parallel**: fixes Rx,Ry. all T\'s and Rz remain. This eliminates the two rotations around the axes of the reference plane.
-   Fixes 1 DOF, leaves 5 DOF:
    -   **Points in Plane**: Fixes Tz. This eliminates the translation along the normal to the reference plane.
    -   **Points Distance**: fixes the distance between the Element origins.

        :   This gives you more freedom than *Points in Plane*

Other

-   **Points on Circle**: fixes Tz and partially Tx,Ty. Freezes the point translation (or several points) on a circle or disk area. You must pick the circle second. This leaves all rotations free and gives limited translation in the circle reference plane.

*: Note: In the following list Tx,Ty,Tz and Rx,Ry,Rz are used to describe translations and rotations about the reference coordinate systems of the involved Element\'s. This is not always exact or fully defined, e.g. when a line is involved it is not defined if it runs in X, Y or any angle in betweeen. The system is used for bevity and easy comparison in favour of a correct but more complex definition. So Z is generally the normal direction of any faces involved. Please feel free to modify this with a better approach with improved readability.*

[top](#top.md)

### Elements

Elements is a specific term used in the Assembly3 workbench and it is important to understand Elements for understanding how Assembly3 should be used.

It is helpul to think of an Element as a general word for a \'selectable item\' of a part, i.e. a face, an edge, a circle or a corner or other point. The items you select to constrain them, are those Elements. In the tree an Assembly folder has three sub-folders. Beside \'Parts\' and \'Constraints\' there is a folder named \'Elements\', which is emtpy as long as there are no constraints added. When adding a constraint the constraint itself gets two (or more) leafs, these are the selected \'Elements\'. Also these get added in the \'Elements\' folder which is just a list of all Elements used in the assembly. Its a good idea to change their names (with F2 key), especially in bigger assemblies.

Lets look at an example

:   Create a new file and add from the Part workbench a cube and a cylinder. We will stack the cylinder onto the tube. First we fix the base part, in out case the cube. Select the bottom face of the cube and select the \"Locked\" constraints (first icon in the Constraints [toolbar](#Toolbars.md)). Select the top face of the cylinder and the top face of the cube. Then select the \"Plane Coincident\" constraint. Now the cylinder is moved into the cube and in the tree a new leaf with two childe nodes was added under \'Constraints\'. Additionally the same two child nodes were added under \'Elements\'. If you cylinder is inside the cube instread of on top of the cube, lets correct that first: select the child node under \'Constraints\' that shows the cylinder face and with a right click in the context menu select \'Flip Part\'. Now the cylinder is stacked onto the box.

The key think to understand is that the constraint operates on links to Elements in the list in the \'Elements\' tree folder. This allows to keep the constraint structure intact while changing the parts. This is very difficult to see without an example.

Lets get back to the example above

:   Note: make sure you added the \"Lock\" constraint to the cube or this will look confusing
:   In the CAD window select another face of the cube. Now we only work in the tree view. Go with your mouse in the tree where the cube should be selected. Drag&Drop the cube to the \'Elements\' folder. Drop it on the \'Elements\' name, not anywhere else in the folder - why we see later. You should see that another Element is added to the \'ELements\' list. Now select in the \'Constraints\' folder the child node of the cube face in out \"Plane Coincident\" constraint and delete it. The Constraint will show an exclamation mark since its missing one Element. Note that by deleting the Element in the Constraint we did *not* delete it in the list. That is because in the constraint was only a link to the Element in the list. Now take the newly added Element in the \'Elements\' list and drag&drop it onto the \"Plane Coincident\" constraint. Now the cylider moves to the other face we selected. We might need to select \'context menu/flip part\' again if the cylinder is again inside the cube.

The example showed that without removing the constraint we can change the Elements that are used for the constraint. The same way we can move the cylinder to a totally different part. After playing around with this example a bit more, you will note some additional things as

-   If you rename an Element in the list, the name will be changed in all Constraints.
-   you can use one Element in the list in several constraints.
-   You can use the Property Window of an Element to add **Offsets**. In the example this could move the cylinder around on the cube face.
-   you can use the \"Show Element Coordinate System\" button in the main toolbar to see what \'ContextMenu/Flip Part\' and \'ContextMenu/Flip Element\' are doing. Be sure to look what happens in the Property Window.
-   you can add a constraint in a totally different order: First add some Elements to the \'Elements List\' (naming is useful, e.g. \"Cube Top Face\" or \"Cube Front Face\"), then add a constraint without selecting anything - it will be an empty constraint. Then drag Elements from the \'Elements\' list. The result is the same than what we did in the first example. After doing that exercise the nature of how constraints work with Elements should be clear.
-   you can change an existing constraint between existing elements by just select a different item in the PropertyWindow/ConstraintType property.

[top](#top.md)

## Compatibilidad

Assembly3 was inspired by [Assembly2](Assembly2_Workbench.md), but it is not compatible with it. If you have older models made in Assembly2, you should stay with FreeCAD 0.16 and use Assembly2 there.

New models developed with Assembly3 should only be opened and edited with this workbench.

Although they may have similar tools, Assembly3 is not compatible with [A2plus](A2plus_Workbench.md) nor [Assembly4](Assembly4_Workbench.md). Models created with these workbenches should be opened only with their respective workbench.

[top](#top.md)

## Pruebas

The [Assembly3 Workbench](Assembly3_Workbench.md) is under development and is not yet available (April 2020) through the [Addon Manager](Std_AddonMgr.md), but it is expected that this will happen at some point.

You can test it in two ways:

-   A special fork of FreeCAD made by realthunder; see [FreeCAD\_assembly3 releases](https://github.com/realthunder/FreeCAD_assembly3/releases). This fork is based on a particular commit of the master branch of FreeCAD, but it also has additional features currently not present in the master branch. Due to this fork being based on a particular development snapshot, it does not have the latest features merged daily to the master branch.
-   The development [AppImage](AppImage.md); this is based on the current master branch, and includes the dependencies needed for working with Assembly3 such as the SolveSpace solver.

Since the AppImage only works for Linux, for Windows users at the moment the only option to test Assembly3 is the first option (realthunder\'s fork).

[top](#top.md)

## Instrucción

### Get Started 

There are many ways to create an assembly with Assembly3. Here is the most simple one you can do.

:   <img alt="" src=images/Assembly3_Example-GettingStarted.jpg  style="width:600px;">
:   *Final Result of the Getting Started Example. In the image the Assembly3 Worksbench is selected, so its multiple toolbars are visible. Note that the vertical \"TabBar\" left of the tree view is an AddOn Workbench that is not contained in standard FreeCAD (but can be installed with the Addon-Manager).*

-   Press **<img src="images/Std_New.svg" width=16px> [New](Std_New.md)** to create a new FreeCAD file
-   Change to <img alt="" src=images/Assembly3_workbench_icon.svg  style="width:16px;"> [Assembly3](Assembly3_Workbench.md) workbench
-   Select **<img src="images/Assembly_New_Assembly.svg‎‎" width=16px> [Create assembly](Assembly3_CreateAssembly.md)
**
-   Change to <img alt="" src=images/Workbench_Part.svg  style="width:16px;"> [Part](Part_Workbench.md) workbench and add a <img alt="" src=images/Part_Cylinder.svg  style="width:16px;"> [Cylinder](Part_Cylinder.md) and a <img alt="" src=images/Part_Box.svg  style="width:16px;"> [Cube](Part_Box.md)
-   <img alt="" src=images/Std_Save.svg  style="width:16px;"> [Save](Std_Save.md) the file with any filename you like. <img alt="" src=images/Std_CloseActiveWindow.svg  style="width:16px;"> [Close](Std_CloseActiveWindow.md) and <img alt="" src=images/Std_Open.svg  style="width:16px;"> [Open\...](Std_Open.md) the file again

The tree view should look like this (0.20.pre and Link Branch):

<img alt="" src=images/Assembly3_Example-Tree-01.png  style="width:300px;"> <img alt="" src=images/Assembly3_Example-Tree-02.png  style="width:280px;">

-   Now *Drag&Drop* with the mouse both **Cylinder** and **Cube** onto the **Parts** folder. They are moved into that folder.

    :   That is the quickest way and suitable for simple cases like this. A better way is via the use of link objects:
    :   Select **Cube** and **Cylinder** and then **<img src="images/Std_LinkMake.svg" width=16px> [Make link](Std_LinkMake.md)** either from the **Context menu** (-\> LinkActions -\> MakeLink) or the **Structure** panel.
    :   This adds two link objects. Then *Drag&Drop* the link objects to the **Parts** folder.
-   Click both top surfaces of **Cylinder** and **Cube** (keep Ctrl pressed (Cmd on a Mac))
-   Change to <img alt="" src=images/Assembly3_workbench_icon.svg  style="width:16px;"> [Assembly3](Assembly3_Workbench.md) workbench
-   Select **<img src="images/Assembly_ConstraintCoincidence.svg‎‎" width=16px> [Plane Coincidence](Assembly3_ConstraintCoincidence.md)** from the [Main constraints toolbar](#Main_Constraints_Toolbar.md).

Now the parts should be joined into each other and your tree should look like this (0.20.pre and Link Branch):

<img alt="" src=images/Assembly3_Example-Tree-03.png  style="width:300px;"> <img alt="" src=images/Assembly3_Example-Tree-04.png  style="width:280px;">

-   Right click **\_Element** (either of the two) and select **Flip Part**.

Now the **Cylinder** should be on top of the **Cube**. If the whole thing is upside down, go back and select **Flip Part** on the other element.

:   We omitted one important step that should be done in larger assemblies: Locking a base part.
:   That means to define one part that should not be moved by constraints. In this example we use the **Cube** for that:
    -   Select the lower face of the **Cube**. Only the lower face, not the whole **Cube**
    -   select the **<img src="images/Assembly_ConstraintLock.svg‎‎" width=16px> [Locked](Assembly3_ConstraintLock.md)** constraint from the [Main constraints toolbar](#Main_Constraints_Toolbar.md)

Done.

The finished assembly tree should look like (0.20.pre and Link Branch):

<img alt="" src=images/Assembly3_Example-Tree-05.png  style="width:300px;"> <img alt="" src=images/Assembly3_Example-Tree-06.png  style="width:280px;">:

If you like you can move the **Locked** constraint upwards in the tree. Use the **<img src="images/Assembly_TreeItemUp.svg‎‎" width=16px> [Move item up](Assembly3_MoveItemUp.md)** button on the [Main toolbar](#Main_Toolbar.md) for that.

**Note:** all new external files must be **saved**, **closed** and re-**opend** at least once, so that Assembly3 can find it.

:   Without doing that FreeCAD can not give a file handle to the Assembly3 Workbench and it can not find the new part.
:   When all parts are in the same file, you should **save** and re-**open** the file.

[top](#top.md)

### Add an Offset 

Assembly3 does not offer Offset with the constaints in the way the [A2plus Workbench](A2plus_Workbench.md) or other CAD tools do. Instead it offers a more general and flexible system to add offsets translations but also angles.

-   Add the offset in the properties of one [Elements](#Elements.md) of a [Constraint](#Constraint.md).

    :   you can choose which one of the two you want to use.

Example:

-   Add 2 cubes to an assembly and select their side faces.
-   select \"PlaneCoincident\". The cubes will be attached inside each other.
-   select one Element and *ContextMenu/Flip Part*. The cubes will be attached side-by-side.
-   select one Element property Offset/Position/Zz and set to 5mm. The cubes will be 5mm apart.

:\* Test with other axes or the angle/axis fields. Also verify that you get the same result when using the other Element. This is the same approach for all other constraints.

[top](#top.md)


<div class="mw-translate-fuzzy">

### Resolver un fallo de solucionador 

Esto sucede a menudo cuando las piezas están restringidas en exceso, es decir, más de 6 DOF están bloqueados.


</div>

The easiest way to find the problem is to click relevant constraints in the tree and select *ContextMenu/Disable* and re-calculate. It is helpful to know the last added constraints before the solver failed and just undo them.

Note: as Assembly3 tries to compensate for over-constraint parts behind the scenes, sometimes the problem is just triggered by a new constraint but the root cause is somewhere different. Before deleting all and starting again, remember that you can re-use Elements. If you named them you can identify the required elements and re-build the constraints without using the 3D view at all. See [Elements](#Elements.md) seciton above.

[top](#top.md)

### Replace a part or rename a filename 

When a part is removed or when a filename changes, the assembly breaks, it can not longer be solved and the solver will issue the message \"Inconsistent constraints\". The solver marks invalid Elements and Constrains with a question mark in the tree.

One way to solve this is to just delete all invalid constraints and elements, import the new part and redo everything. But there is a better way:

-   Rename a file
    1.  Use a file manager and copy the file you want renamed. Then give the new name to the copy.
    2.  Open the copy in FreeCAD. The assembly and the old file should also be open
    3.  Select the old object in the tree and click to change the propery \"Linked object\" (it does contain the old filename)
    4.  A list dialog will open containing all open parts. It shows the filenames and objects of each part. The old part and object is selected. Locate the renamed part in the tree and select the same object in the new part. Then confim the selection.
    5.  Delete the old part in the tree. Also the file can be deleted now.
    6.  Constraints and elements of te old part became invalid. Open the constraint or Elements list in the tree. Then sequentially
        -   select each element surface on the new part. An item in the tree will be highliged.
        -   Take that item and drag&drop it over the old element (either in the element list or in one of the constraints where it was used). That element should become valid.
        -   Repeat the procedure for the remaining elements. Often a single element is enough to allow Assembly3 to identify the remaining elements of the part automatically.
        -   If an element was assigned to the wrong surface by accident, just repeat with the correct surface.
    7.  Change the object name in FreeCAD, if desired

-   Replace a part with another part

    :   *which is simular enough to the original part that the original constraints still make sense, of course*

    1.  Delete the old part in the tree. Also the file can be deleted.
    2.  Constraints and elements of te old part became invalid. Open the constraint or Elements list in the tree.
        -   Select an element surface on the new part. An item in the tree will be highliged.
        -   Take that item and drag&drop it over the old element (either in the element list or in one of the constraints where it was used). That element should become valid.
        -   repeat the procedure for the remaining elements.
        -   If an element was assigned to the wrong surface by accident, just repeat with the correct surface.
    3.  Change the object name in FreeCAD, if desired

\'\'Notes
\* They are not as complicated as it may seem here. After 2-3 times they should become second nature and feel really easy to do.

-   Its not only usually ways quicker than deleting and re-doing constraints, its also safer because an element could have been used in a parent assembly. Deleting the original would destroy that link, re-assingning would keep it.
-   Also this procedure becomes really quick and easy to do if constraints and elements are named. There is no guessing where the surfaces should be dragged&dropped to because the names tell it (see [Tips & Tricks](#Tips_&_Tricks.md)).

\'\'

[top](#top.md)

### Tips & Tricks 

-   Using hierarchical assemblies helps in avoiding solver issues and keeping you model fluid. You can freeze a subassembly with one click and save CPU resources easily (use the context menu in the tree). When loading an assembly Assembly3 does not need to open external files for frozen subassemblies which keeps the tree compact.
-   Is very helpful to make it a habit to name the elements and constraints. Use the **F2** key to do this quickly in the tree. You will find the tree sorting tools in the main toolbar very useful. An assembly with fully named constraints and elements is very easy to understand for other people or for oneself when looking at an older file.

    :   Examples for constraint names for a table could be \"Align\_FrontLegs\", \"Align\_FrameBottom-LegTops\" and element names could be \"Leg1\_Top\" or \"TableTop\_Front\", \"TableTop\_Left\".
-   Please note that once external files are opened by an assembly its not possible easy to close them again without closing the assembly. Since the assembly keeps open those files in the backgound, the tab may disappear but the file remains visible in the tree. If you have several layers of subassemblies it becomes close to impossible to close single files. This behaviour may change, but until then a possible approach could be to regulary use the commands *File/Save All* and *File/Close All* to clean up the tree before working on another sub-assembly.

    :   \'\'Example: consider you have a large CNC machine with a main assembly and a subassembly for each module. Once you have the main assembly open it may open literally hundreds of files down to a single ball bearing. Before working on the subassembly of the electronics cabinet of the machine it is a good idea to save and close all files to get an empty tree. Then open just the subassembly for the electronics cabinet. This will open all file it needs but ony those.
-   Using external files makes it easier to re-use a parts or do part versioning with systems like git or subversion. The workflow in FreeCAD with Assembly feels quite the same as with files that have all parts in the same file. For exchanging files often with other parties, single files might be more convenient.
-   Multiply linked parts. If you added a link into the assembly, it will have a property value named \"Element Count\", default 0. If you set this to 3 you get 3 instances of that part. They will be added into a subfolder and can be used like fully separte parts. Use this feature to keep the data footprint of your file low, because the part is saved only once. Each instance only contain the differences.
-   Insert multiple parts, e.g. Screws, with one click. Check out the [Assembly3 Wiki](https://github.com/realthunder/FreeCAD_assembly3/wiki/Constraints-and-Solvers) on the Github site. This is not only a stunning function (even a bit magic), but really really useful.

-   Using the [TabBar Workbench](https://github.com/triplus/TabBar) speeds up working with assembly. This adds a Toolbar with one button for each workbench. You can sort the toolbar and can put it where every you want it. Many people put it vertically on the left side just beside the tree view. Of you have Assembly3, Part, PartDesign and other often used workbenches close to the top switching between them becomes extremely easy.

[inicio](#top.md)

## Enlaces

-   [App Link](App_Link.md) object that makes Assembly3 work.
-   [FreeCAD\_assembly3](https://github.com/realthunder/FreeCAD_assembly3) repository and documentation.
-   [Assembly3 preview](https://forum.freecadweb.org/viewtopic.php?f=20&t=25712), big discussion thread.
-   [Test tutorial for Assembly 3 WB](https://forum.freecadweb.org/viewtopic.php?f=36&t=29562) by jpg87.
-   [Current Assembly Status](https://forum.freecadweb.org/viewtopic.php?f=20&t=34583)
-   [External workbenches](External_workbenches.md)
-   [Old Assembly project](Assembly_project.md) development plan, to get acquainted with the history of the issue.




[Category:Addons{{\#translation:}}](Category:Addons.md) [Category:External Workbenches{{\#translation:}}](Category:External_Workbenches.md)
