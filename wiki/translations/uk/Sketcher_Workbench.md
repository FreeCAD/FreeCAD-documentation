# <img alt="Sketcher workbench icon" src=images/Workbench_Sketcher.svg  style="width   *64px;"> Sketcher Workbench/uk


{{TOCright}}

## Introduction

The FreeCAD <img alt="" src=images/Workbench_Sketcher.svg  style="width   *24px;"> [Sketcher Workbench](Sketcher_Workbench.md) is used to create 2D geometries intended for use in the <img alt="" src=images/Workbench_PartDesign.svg  style="width   *24px;"> [PartDesign Workbench](PartDesign_Workbench.md), <img alt="" src=images/Workbench_Arch.svg  style="width   *24px;"> [Arch Workbench](Arch_Workbench.md), and other workbenches. Generally, a 2D drawing is considered the starting point for most CAD models, as a 2D sketch can be \"extruded\" to create a 3D shape; further 2D sketches can be used to create other features like pockets, ridges, or extrusions on top of the previously built 3D shapes. Together with boolean operations defined in the <img alt="" src=images/Workbench_Part.svg  style="width   *24px;"> [Part Workbench](Part_Workbench.md), the Sketcher forms the basis of the [constructive solid geometry](constructive_solid_geometry.md) (CSG) method of building solids. Moreover, together with the <img alt="" src=images/Workbench_PartDesign.svg  style="width   *24px;"> [PartDesign Workbench](PartDesign_Workbench.md) operations, the Sketcher also forms the basis of the [feature editing](feature_editing.md) methodology of creating solids.

The Sketcher workbench features \"constraints\", allowing 2D shapes to follow precise geometrical definitions in terms of length, angles, and relationships (horizontality, verticality, perpendicularity, etc.). A constraint solver calculates the constrained-extent of 2D geometry and allows interactive exploration of degrees-of-freedom of the sketch.

<img alt="" src=images/FC_ConstrainedSketch.png  style="width   *450px;"> 
*A fully constrained sketch*

## Basics of constraint sketching 

To explain how the Sketcher works, it may be useful to compare it to the \"traditional\" way of drafting.

#### Traditional Drafting 

The traditional way of CAD drafting inherits from the old [drawing board](http   *//en.wikipedia.org/wiki/Drawing_board). [Orthogonal (2D) views](http   *//en.wikipedia.org/wiki/Multiview_orthographic_projection) are drawn manually and intended for producing technical drawings (also known as blueprints). Objects are drawn precisely to the intended size or dimension. If you want to draw an horizontal line 100mm in length starting at (0,0), you activate the line tool, either click on the screen or input the (0,0) coordinates for the first point, then make a second click or input the second point coordinates at (100,0). Or you will draw your line without regard to its position, and move it afterwards. When you\'ve finished drawing your geometries, you add dimensions to them.

#### Constraint Sketching 

The **Sketcher** moves away from this logic. Objects do not need to be drawn exactly as you intend to, because they will be defined later on by constraints. Objects can be drawn loosely, and as long as they are unconstrained, can be modified. They are in effect \"floating\" and can be moved, stretched, rotated, scaled, and so on. This gives great flexibility in the design process.

#### What are constraints? 

Instead of dimensions, Constraints are used to limit the degrees of freedom of an object. For example, a line without constraints has 4 Degrees Of Freedom (abbreviated as \"DOF\")   * it can be moved horizontally or vertically, it can be stretched, and it can be rotated.

Applying a horizontal or vertical constraint, or an angle constraint (relative to another line or to one of the axes), will limit its capacity to rotate, thus leaving it with 3 degrees of freedom. Locking one of its points in relation to the origin will remove another 2 degrees of freedom. And applying a dimension constraint will remove the last degree of freedom. The line is then considered **fully-constrained**.

Multiple objects can be constrained between one another. Two lines can be joined through one of their points with the coincident point constraint. An angle can be set between them, or they can be set perpendicular. A line can be tangent to an arc or a circle, and so on. A complex Sketch with multiple objects will have a number of different solutions, and making it **fully-constrained** means that just one of these possible solutions has been reached based on the applied constraints.

There are two kinds of constraints   * geometric and dimensional. They are detailed in the [\'Tools\'](#Tools.md) section below.

#### What the Sketcher is not good for 

The Sketcher is not intended for producing 2D blueprints. Once sketches are used to generate a solid feature, they are automatically hidden. Constraints are only visible in Sketch edit mode.

If you only need to produce 2D views for print, and don\'t want to create 3D models, check out the [Draft workbench](Draft_Workbench.md). Unlike Sketcher elements, Draft objects don\'t use constraints; they are simple shapes defined at the moment of creation. Both Draft and Sketcher can be used for 2D geometry drawing, and 3D solid creation, although their preferred use is different; the Sketcher is normally used together with the [Part](Part_Workbench.md) and [PartDesign](PartDesign_Workbench.md) workbenches to create solids; Draft is normally used for simple planar drawings over a grid, as when drawing an architectural floor plan; in these situations Draft is mostly used together with the [Arch Workbench](Arch_Workbench.md). The tool [Draft2Sketch](Draft_Draft2Sketch.md) converts a Draft object to a Sketch object, and vice versa; many tools that require a 2D element as input work with either type of object as an internal conversion is done automatically.

## Sketching Workflow 

A Sketch is always 2-dimensional (2D). To create a solid, a 2D Sketch of a single enclosed area is created and then either Padded or Revolved to add the 3rd dimension, creating a 3D solid from the 2D Sketch.

If a Sketch has segments that cross one another, places where a Point is not directly on a segment, or places where there are gaps between endpoints of adjacent segments, Pad or Revolve won\'t create a solid. Sometimes a Sketch which contains lines which cross one another will work for a simple operation such as Pad, but later operations such as Linear Pattern will fail. It is best to avoid crossing lines. The exception to this rule is that it doesn\'t apply to Construction (blue) Geometry.

Inside the enclosed area we can have smaller non-overlapping areas. These will become voids when the 3D solid is created.

Once a Sketch is fully constrained, the Sketch features will turn green; Construction Geometry will remain blue. It is usually \"finished\" at this point and suitable for use in creating a 3D solid. However, once the Sketch dialog is closed it may be worthwhile going to <img alt="" src=images/Workbench_Part.svg  style="width   *24px;"> [Part Workbench](Part_Workbench.md) and running **[<img src=images/Part_CheckGeometry.svg style="width   *16px"> [Check geometry](Part_CheckGeometry.md)** to ensure there are no features in the Sketch which may cause later problems.

## Tools

The Sketcher Workbench tools are all located in the Sketch menu that appears when you load the Sketcher Workbench.

### General

-   <img alt="" src=images/Sketcher_NewSketch.svg‎‎  style="width   *32px;"> [Create sketch](Sketcher_NewSketch.md)   * Creates‎ a new sketch on a selected face or plane. If no face is selected while this tool is executed the user is prompted to select a plane from a pop-up window.

-   <img alt="" src=images/Sketcher_EditSketch.svg  style="width   *32px;"> [Edit sketch](Sketcher_EditSketch.md)   * Edit the selected Sketch. This will open the [Sketcher Dialog](Sketcher_Dialog.md).

-   <img alt="" src=images/Sketcher_LeaveSketch.svg  style="width   *32px;"> [Leave sketch](Sketcher_LeaveSketch.md)   * Leave the Sketch editing mode.

-   <img alt="" src=images/Sketcher_ViewSketch.svg  style="width   *32px;"> [View sketch](Sketcher_ViewSketch.md)   * Sets the model view perpendicular to the sketch plane.

-   <img alt="" src=images/Sketcher_ViewSection.svg  style="width   *32px;"> [View section](Sketcher_ViewSection.md)   * Creates a section plane that temporarily hides any matter in front of the sketch plane.

-   <img alt="" src=images/Sketcher_MapSketch.svg  style="width   *32px;"> [Map sketch to face](Sketcher_MapSketch.md)   * Maps a sketch to the previously selected face of a solid.

-   <img alt="" src=images/Sketcher_ReorientSketch.svg  style="width   *32px;"> [Reorient sketch](Sketcher_ReorientSketch.md)   * Allows you to attach the sketch to one of the main planes.

-   <img alt="" src=images/Sketcher_ValidateSketch.svg  style="width   *32px;"> [Validate sketch](Sketcher_ValidateSketch.md)   * Verify the tolerance of different points and adjust them.

-   <img alt="" src=images/Sketcher_MergeSketches.svg  style="width   *32px;"> [Merge sketches](Sketcher_MergeSketches.md)   * Merge two or more sketches.

-   <img alt="" src=images/Sketcher_MirrorSketch.svg  style="width   *32px;"> [Mirror sketch](Sketcher_MirrorSketch.md)   * Mirror a sketch along the x-axis, the y-axis or the origin.

-   <img alt="" src=images/Sketcher_StopOperation.svg  style="width   *32px;"> [Stop operation](Sketcher_StopOperation.md)   * When in edit mode, stop the current operation, whether that is drawing, setting constraints, etc.

### Sketcher geometries 

These are tools for creating objects.

-   <img alt="" src=images/Sketcher_CreatePoint.svg  style="width   *32px;"> [Point](Sketcher_CreatePoint.md)   * Draws a point.

-   <img alt="" src=images/Sketcher_CreateLine.svg  style="width   *32px;"> [Line](Sketcher_CreateLine.md)   * Draws a line segment between 2 points. Lines are infinite regarding certain constraints.

-   <img alt="" src=images/Sketcher_CompCreateArc.png  style="width   *48px;"> [Create an arc](Sketcher_CompCreateArc.md)   * This is an icon menu in the Sketcher toolbar that holds the following commands   *

   ** <img alt="" src=images/Sketcher_CreateArc.svg  style="width   *32px;"> [Arc](Sketcher_CreateArc.md)   * Draws an arc segment from center, radius, start angle and end angle.

   ** <img alt="" src=images/Sketcher_Create3PointArc.svg  style="width   *32px;"> [Arc by 3 points](Sketcher_Create3PointArc.md)   * Draws an arc segment from two endpoints and another point on the circumference.

-   <img alt="" src=images/Sketcher_CompCreateCircle.png  style="width   *48px;"> [Create a circle](Sketcher_CompCreateCircle.md)   * This is an icon menu in the Sketcher toolbar that holds the following commands   *

   ** <img alt="" src=images/Sketcher_CreateCircle.svg  style="width   *32px;"> [Circle](Sketcher_CreateCircle.md)   * Draws a circle from center and radius.

   ** <img alt="" src=images/Sketcher_Create3PointCircle.svg  style="width   *32px;"> [Circle by 3 points](Sketcher_Create3PointCircle.md)   * Draws a circle from three points on the circumference.

-   <img alt="" src=images/Sketcher_CompCreateConic.png  style="width   *48px;"> [Create a conic](Sketcher_CompCreateConic.md)   * The sketcher provides the following conical sections. Unlike B-splines they can be used with all sorts of constraints such as [Tangent](Sketcher_ConstrainTangent.md), [Point On Object](Sketcher_ConstrainPointOnObject.md), or [Perpendicular](Sketcher_ConstrainPerpendicular.md).

   ** <img alt="" src=images/Sketcher_CreateEllipseByCenter.svg  style="width   *32px;"> [Ellipse by center](Sketcher_CreateEllipseByCenter.md)   * Draws an ellipse by center point, major radius point and minor radius point.

   ** <img alt="" src=images/Sketcher_CreateEllipseBy3Points.svg  style="width   *32px;"> [Ellipse by 3 points](Sketcher_CreateEllipseBy3Points.md)   * Draws an ellipse by major diameter (2 points) and minor radius point.

   ** <img alt="" src=images/Sketcher_CreateArcOfEllipse.svg  style="width   *32px;"> [Arc of ellipse](Sketcher_CreateArcOfEllipse.md)   * Draws an arc of ellipse by center point, major radius point, starting point and ending point.

   ** <img alt="" src=images/Sketcher_CreateArcOfHyperbola.svg  style="width   *32px;"> [Arc of hyperbola](Sketcher_CreateArcOfHyperbola.md)   * Draws an arc of hyperbola.

   ** <img alt="" src=images/Sketcher_CreateArcOfParabola.svg  style="width   *32px;"> [Arc of parabola](Sketcher_CreateArcOfParabola.md)   * Draws an arc of parabola.

-   <img alt="" src=images/Sketcher_CompCreateBSpline.png  style="width   *48px;"> [Create a B-spline](Sketcher_CompCreateBSpline.md)   * This is an icon menu in the Sketcher toolbar that holds the following commands   *

   ** <img alt="" src=images/Sketcher_CreateBSpline.svg  style="width   *32px;"> [B-spline](Sketcher_CreateBSpline.md)   * Draws a B-spline curve by its control points.

   ** <img alt="" src=images/Sketcher_CreatePeriodicBSpline.svg  style="width   *32px;"> [Periodic B-spline](Sketcher_CreatePeriodicBSpline.md)   * Draws a periodic (closed) B-spline curve by its control points.

-   <img alt="" src=images/Sketcher_CreatePolyline.svg  style="width   *32px;"> [Polyline (multiple-point line)](Sketcher_CreatePolyline.md)   * Draws a line made of multiple line segments. Pressing the **M** key while drawing a Polyline toggles between the different polyline modes.

-   <img alt="" src=images/Sketcher_CompCreateRectangles.png  style="width   *48px;"> [Create a rectangle](Sketcher_CompCreateRectangles.md)   * This is an icon menu in the Sketcher toolbar that holds the following commands   * <small>(v0.20)</small> 

   ** <img alt="" src=images/Sketcher_CreateRectangle.svg  style="width   *32px;"> [Rectangle](Sketcher_CreateRectangle.md)   * Draws a rectangle from 2 opposite points.

   ** <img alt="" src=images/Sketcher_CreateRectangle_Center.svg  style="width   *32px;"> [Centered rectangle](Sketcher_CreateRectangle_Center.md)   * Draws a rectangle from a central point and an edge point. <small>(v0.20)</small> 

   ** <img alt="" src=images/Sketcher_CreateOblong.svg  style="width   *32px;"> [Rounded rectangle](Sketcher_CreateOblong.md)   * Draws a rounded rectangle from 2 opposite points. <small>(v0.20)</small> 

-   <img alt="" src=images/Sketcher_CompCreateRegularPolygon.png  style="width   *48px;"> [Create a regular polygon](Sketcher_CompCreateRegularPolygon.md)   * This is an icon menu in the Sketcher toolbar that holds the following commands   *

   ** <img alt="" src=images/Sketcher_CreateTriangle.svg  style="width   *32px;"> [Triangle](Sketcher_CreateTriangle.md)   * Draws a regular triangle inscribed in a construction geometry circle.

   ** <img alt="" src=images/Sketcher_CreateSquare.svg  style="width   *32px;"> [Square](Sketcher_CreateSquare.md)   * Draws a regular square inscribed in a construction geometry circle.

   ** <img alt="" src=images/Sketcher_CreatePentagon.svg  style="width   *32px;"> [Pentagon](Sketcher_CreatePentagon.md)   * Draws a regular pentagon inscribed in a construction geometry circle.

   ** <img alt="" src=images/Sketcher_CreateHexagon.svg  style="width   *32px;"> [Hexagon](Sketcher_CreateHexagon.md)   * Draws a regular hexagon inscribed in a construction geometry circle.

   ** <img alt="" src=images/Sketcher_CreateHeptagon.svg  style="width   *32px;"> [Heptagon](Sketcher_CreateHeptagon.md)   * Draws a regular heptagon inscribed in a construction geometry circle.

   ** <img alt="" src=images/Sketcher_CreateOctagon.svg  style="width   *32px;"> [Octagon](Sketcher_CreateOctagon.md)   * Draws a regular octagon inscribed in a construction geometry circle.

   ** <img alt="" src=images/Sketcher_CreateRegularPolygon.svg  style="width   *32px;"> [Regular polygon](Sketcher_CreateRegularPolygon.md)    * Draws a regular polygon by selecting the number of sides and picking two points   * the center and one corner.

-   <img alt="" src=images/Sketcher_CreateSlot.svg  style="width   *32px;"> [Slot](Sketcher_CreateSlot.md)   * Draws an oval by selecting the center of one semicircle and an endpoint of the other semicircle.

-   <img alt="" src=images/Sketcher_CompCreateFillets.png  style="width   *48px;"> [Create a fillet](Sketcher_CompCreateFillets.md)   * This is an icon menu in the Sketcher toolbar that holds the following commands   *

   ** <img alt="" src=images/Sketcher_CreateFillet.svg  style="width   *32px;"> [Fillet](Sketcher_CreateFillet.md)   * Creates a fillet between two non-parallel lines.

   ** <img alt="" src=images/Sketcher_CreatePointFillet.svg  style="width   *32px;"> [Corner-preserving fillet](Sketcher_CreatePointFillet.md)   * Creates a fillet between two non-parallel lines while preserving their (virtual) intersection.

-   <img alt="" src=images/Sketcher_Trimming.svg  style="width   *32px;"> [Trim](Sketcher_Trimming.md)   * Trims a line, circle or arc with respect to the clicked point.

-   <img alt="" src=images/Sketcher_Extend.svg  style="width   *32px;"> [Extend](Sketcher_Extend.md)   * Extends a line or an arc to a boundary line, arc, ellipse, arc of ellipse or a point in space.

-   <img alt="" src=images/Sketcher_Split.svg  style="width   *32px;"> [Split](Sketcher_Split.md)   * Splits a line or an arc into two, converts a circle into an arc while keeping most of the constraints. <small>(v0.20)</small> 

-   <img alt="" src=images/Sketcher_External.svg  style="width   *32px;"> [External geometry](Sketcher_External.md)   * Creates an edge linked to external geometry.

-   <img alt="" src=images/Sketcher_CarbonCopy.svg  style="width   *32px;"> [Carbon copy](Sketcher_CarbonCopy.md)   * Copies the geometry of another sketch.

-   <img alt="" src=images/Sketcher_ToggleConstruction.svg  style="width   *32px;"> [Toggle construction geometry](Sketcher_ToggleConstruction.md)   * Toggles sketch geometry from/to construction mode. Construction geometry is shown in blue and is discarded outside of Sketch editing mode.

### Sketcher constraints 

Constraints are used to define lengths, set rules between sketch elements, and to lock the sketch along the vertical and horizontal axes. Some constraints require use of [Helper constraints](Sketcher_helper_constraint.md).

#### Geometric constraints 

These constraints are not associated with numeric data.

-   <img alt="" src=images/Sketcher_ConstrainCoincident.svg  style="width   *32px;"> [Coincident](Sketcher_ConstrainCoincident.md)   * Affixes a point onto (coincident with) one or more other points. It acts as a concentric constraint if two or more circles, arcs, ellipses or arcs of ellipses are selected.

-   <img alt="" src=images/Sketcher_ConstrainPointOnObject.svg  style="width   *32px;"> [Point on object](Sketcher_ConstrainPointOnObject.md)   * Affixes a point onto another object such as a line, arc, or axis.

-   <img alt="" src=images/Sketcher_ConstrainVertical.svg  style="width   *32px;"> [Vertical](Sketcher_ConstrainVertical.md)   * Constrains the selected lines or polyline elements to a true vertical orientation. More than one object can be selected before applying this constraint.

-   <img alt="" src=images/Sketcher_ConstrainHorizontal.svg  style="width   *32px;"> [Horizontal](Sketcher_ConstrainHorizontal.md)   * Constrains the selected lines or polyline elements to a true horizontal orientation. More than one object can be selected before applying this constraint.

-   <img alt="" src=images/Sketcher_ConstrainParallel.svg  style="width   *32px;"> [Parallel](Sketcher_ConstrainParallel.md)   * Constrains two or more lines parallel to one another.

-   <img alt="" src=images/Sketcher_ConstrainPerpendicular.svg  style="width   *32px;"> [Perpendicular](Sketcher_ConstrainPerpendicular.md)   * Constrains two lines perpendicular to one another, or constrains a line perpendicular to an arc endpoint.

-   <img alt="" src=images/Sketcher_ConstrainTangent.svg  style="width   *32px;"> [Tangent](Sketcher_ConstrainTangent.md)   * Creates a tangent constraint between two selected entities, or a co-linear constraint between two line segments. A line segment does not have to lie directly on an arc or circle to be constrained tangent to that arc or circle.

-   <img alt="" src=images/Sketcher_ConstrainEqual.svg  style="width   *32px;"> [Equal](Sketcher_ConstrainEqual.md)   * Constrains two selected entities equal to one another. If used on circles or arcs their radii will be set equal.

-   <img alt="" src=images/Sketcher_ConstrainSymmetric.svg  style="width   *32px;"> [Symmetric](Sketcher_ConstrainSymmetric.md)   * Constrains two points symmetrically about a line, or constrains the first two selected points symmetrically about a third selected point.

-   <img alt="" src=images/Sketcher_ConstrainBlock.svg  style="width   *32px;"> [Block](Sketcher_ConstrainBlock.md)   * it blocks an edge from moving, that is, it prevents its vertices from changing their current positions. It should be particularly useful to fix the position of B-Splines. See the [Block Constraint forum topic](https   *//forum.freecadweb.org/viewtopic.php?f=9&t=26572).

#### Dimensional constraints 

These are constraints associated with numeric data, for which you can use the [expressions](Expressions.md). The data may be taken from a [spreadsheet](Spreadsheet_Workbench.md).

-   <img alt="" src=images/Sketcher_ConstrainLock.svg  style="width   *32px;"> [Lock](Sketcher_ConstrainLock.md)   * Constrains the selected item by setting vertical and horizontal distances relative to the origin, thereby locking the location of that item. These constraint distances can be edited later.

-   <img alt="" src=images/Sketcher_ConstrainDistanceX.svg  style="width   *32px;"> [Horizontal distance](Sketcher_ConstrainDistanceX.md)   * Fixes the horizontal distance between two points or line endpoints. If only one item is selected, the distance is set to the origin.

-   <img alt="" src=images/Sketcher_ConstrainDistanceY.svg  style="width   *32px;"> [Vertical distance](Sketcher_ConstrainDistanceY.md)   * Fixes the vertical distance between 2 points or line endpoints. If only one item is selected, the distance is set to the origin.

-   <img alt="" src=images/Sketcher_ConstrainDistance.svg  style="width   *32px;"> [Distance](Sketcher_ConstrainDistance.md)   * Defines the distance of a selected line by constraining its length, or defines the distance between two points by constraining the distance between them.

-   <img alt="" src=images/Sketcher_CompConstrainRadDia.png  style="width   *48px;"> [Arc or circle](Sketcher_CompConstrainRadDia.md)   * This is an icon menu in the Sketcher constraints toolbar that holds the following commands   *

   ** <img alt="" src=images/Sketcher_ConstrainRadius.svg  style="width   *32px;"> [Radius](Sketcher_ConstrainRadius.md)   * Defines the radius of a selected arc or circle by constraining the radius.

   ** <img alt="" src=images/Sketcher_ConstrainDiameter.svg  style="width   *32px;"> [Diameter](Sketcher_ConstrainDiameter.md)   * Defines the diameter of a selected arc or circle by constraining the diameter.

   ** <img alt="" src=images/Sketcher_ConstrainRadiam.svg  style="width   *32px;"> [Radiam](Sketcher_ConstrainRadiam.md)   * Automatically defines radius/diameter of a selected arc or circle (weight for a B-spline pole, diameter for a complete circle, radius for an arc). <small>(v0.20)</small> 

-   <img alt="" src=images/Sketcher_ConstrainAngle.svg  style="width   *32px;"> [Angle](Sketcher_ConstrainAngle.md)   * Defines the internal angle between two selected lines.

#### Special constraints 

-   <img alt="" src=images/Sketcher_ConstrainSnellsLaw.svg  style="width   *32px;"> [Snell\'s law](Sketcher_ConstrainSnellsLaw.md)   * Constrains two lines to obey a refraction law to simulate the light going through an interface.

-   <img alt="" src=images/Sketcher_ConstrainInternalAlignment.svg  style="width   *32px;"> [Internal alignment](Sketcher_ConstrainInternalAlignment.md)   * Aligns selected elements to selected shape (e.g. a line to become major axis of an ellipse).

#### Constraint tools 

The following tools can be used the change the effect of constraints   *

-   <img alt="" src=images/Sketcher_ToggleDrivingConstraint.svg  style="width   *32px;"> [Toggle driving/reference constraint](Sketcher_ToggleDrivingConstraint.md)   * Toggles the toolbar or the selected constraints to/from reference mode.

-   <img alt="" src=images/Sketcher_ToggleActiveConstraint.svg  style="width   *32px;"> [Activate/deactivate constraint](Sketcher_ToggleActiveConstraint.md)   * Enable or disable an already placed constraint. <small>(v0.19)</small> 

### Sketcher tools 

-   <img alt="" src=images/Sketcher_SelectElementsWithDoFs.svg  style="width   *32px;"> [Select unconstrained DoF](Sketcher_SelectElementsWithDoFs.md)   * Highlights in green the geometry with degrees of freedom (DOFs), i.e. not fully constrained.

-   <img alt="" src=images/Sketcher_CloseShape.svg  style="width   *32px;"> [Close shape](Sketcher_CloseShape.md)   * Creates a closed shape by applying coincident constraints to endpoints. This tool is obsolete, it will not be available in future releases (<small>(v1.0)</small> ).

-   <img alt="" src=images/Sketcher_ConnectLines.svg  style="width   *32px;"> [Connect edges](Sketcher_ConnectLines.md)   * Connect sketcher elements by applying coincident constraints to endpoints. This tool is obsolete, it will not be available in future releases (<small>(v1.0)</small> ).

-   <img alt="" src=images/Sketcher_SelectConstraints.svg  style="width   *32px;"> [Select associated constraints](Sketcher_SelectConstraints.md)   * Selects the constraints of a sketcher element.

-   <img alt="" src=images/Sketcher_SelectElementsAssociatedWithConstraints.svg  style="width   *32px;"> [Select associated geometry](Sketcher_SelectElementsAssociatedWithConstraints.md)   * Select sketcher elements associated with constraints.

-   <img alt="" src=images/Sketcher_SelectRedundantConstraints.svg  style="width   *32px;"> [Select redundant constraints](Sketcher_SelectRedundantConstraints.md)   * Selects redundant constraints of a sketch.

-   <img alt="" src=images/Sketcher_SelectConflictingConstraints.svg  style="width   *32px;"> [Select conflicting constraints](Sketcher_SelectConflictingConstraints.md)   * Selects conflicting constraints of a sketch.

-   <img alt="" src=images/Sketcher_RestoreInternalAlignmentGeometry.svg  style="width   *32px;"> [Show/hide internal geometry](Sketcher_RestoreInternalAlignmentGeometry.md)   * Recreates missing/deletes unneeded internal geometry of a selected ellipse, arc of ellipse/hyperbola/parabola or B-spline.

-   <img alt="" src=images/Sketcher_SelectOrigin.svg  style="width   *32px;"> [Select origin](Sketcher_SelectOrigin.md)   * Selects the origin of a sketch.

-   <img alt="" src=images/Sketcher_SelectVerticalAxis.svg  style="width   *32px;"> [Select vertical axis](Sketcher_SelectVerticalAxis.md)   * Selects the vertical axis of a sketch.

-   <img alt="" src=images/Sketcher_SelectHorizontalAxis.svg  style="width   *32px;"> [Select horizontal axis](Sketcher_SelectHorizontalAxis.md)   * Selects the horizontal axis of a sketch.

-   <img alt="" src=images/Sketcher_Symmetry.svg  style="width   *32px;"> [Symmetry](Sketcher_Symmetry.md)   * Copies a sketcher element symmetrical to a chosen line.

-   <img alt="" src=images/Sketcher_Clone.svg  style="width   *32px;"> [Clone](Sketcher_Clone.md)   * Clones a sketcher element.

-   <img alt="" src=images/Sketcher_Copy.svg  style="width   *32px;"> [Copy](Sketcher_Copy.md)   * Copies a sketcher element.

-   <img alt="" src=images/Sketcher_Move.svg  style="width   *32px;"> [Move](Sketcher_Move.md)   * Moves the selected geometry taking as reference the last selected point.

-   <img alt="" src=images/Sketcher_RectangularArray.svg  style="width   *32px;"> [Rectangular array](Sketcher_RectangularArray.md)   * Creates an array of selected sketcher elements.

-   <img alt="" src=images/Sketcher_RemoveAxesAlignment.svg  style="width   *32px;"> [Remove axes alignment](Sketcher_RemoveAxesAlignment.md)   * Remove axes alignment while trying to preserve the constraint relationship of the selection. <small>(v0.20)</small> 

-   <img alt="" src=images/Sketcher_DeleteAllGeometry.svg  style="width   *32px;"> [Delete all geometry](Sketcher_DeleteAllGeometry.md)   * Deletes all geometry from the sketch.

-   <img alt="" src=images/Sketcher_DeleteAllConstraints.svg  style="width   *32px;"> [Delete all constraints](Sketcher_DeleteAllConstraints.md)   * Deletes all constraints from the sketch.

### Sketcher B-spline tools 

-   <img alt="" src=images/Sketcher_BSplineDegree.svg  style="width   *32px;"> [Show/hide B-spline degree](Sketcher_BSplineDegree.md)

-   <img alt="" src=images/Sketcher_BSplinePolygon.svg  style="width   *32px;"> [Show/hide B-spline control polygon](Sketcher_BSplinePolygon.md)

-   <img alt="" src=images/Sketcher_BSplineComb.svg  style="width   *32px;"> [Show/hide B-spline curvature comb](Sketcher_BSplineComb.md)

-   <img alt="" src=images/Sketcher_BSplineKnotMultiplicity.svg  style="width   *32px;"> [Show/hide B-spline knot multiplicity](Sketcher_BSplineKnotMultiplicity.md)

-   <img alt="" src=images/Sketcher_BSplinePoleWeight.svg  style="width   *32px;"> [Show/hide B-spline control point weight](Sketcher_BSplinePoleWeight.md), <small>(v0.19)</small> 

-   <img alt="" src=images/Sketcher_BSplineApproximate.svg  style="width   *32px;"> [Convert geometry to B-spline](Sketcher_BSplineApproximate.md)

-   <img alt="" src=images/Sketcher_BSplineIncreaseDegree.svg  style="width   *32px;"> [Increase B-spline degree](Sketcher_BSplineIncreaseDegree.md)

-   <img alt="" src=images/Sketcher_BSplineDecreaseDegree.svg  style="width   *32px;"> [Decrease B-spline degree](Sketcher_BSplineDecreaseDegree.md), <small>(v0.19)</small> 

-   <img alt="" src=images/Sketcher_BSplineIncreaseKnotMultiplicity.svg  style="width   *32px;"> [Increase knot multiplicity](Sketcher_BSplineIncreaseKnotMultiplicity.md)

-   <img alt="" src=images/Sketcher_BSplineDecreaseKnotMultiplicity.svg  style="width   *32px;"> [Decrease knot multiplicity](Sketcher_BSplineDecreaseKnotMultiplicity.md)

-   <img alt="" src=images/Sketcher_BSplineInsertKnot.svg  style="width   *32px;"> [Insert knot](Sketcher_BSplineInsertKnot.md), <small>(v0.20)</small> 

### Sketcher virtual space 

-   <img alt="" src=images/Sketcher_SwitchVirtualSpace.svg  style="width   *32px;"> [Switch virtual space](Sketcher_SwitchVirtualSpace.md)   * Allows you to hide all constraints of a sketch and make them visible again.

## Preferences

-   <img alt="" src=images/Preferences-general.svg  style="width   *32px;"> [Preferences](Sketcher_Preferences.md)   * Preferences for the **Sketcher** workbench.

## Best Practices 

Every CAD user develops his own way of working over time, but there are some useful general principles to follow.

-   A series of simple sketches is easier to manage than a single complex one. For example, a first sketch can be created for the base 3D feature (either a pad or a revolve), while a second one can contain holes or cutouts (pockets). Some details can be left out, to be realized later on as 3D features. You can choose to avoid fillets in your sketch if there are too many, and add them as a 3D feature.
-   Always create a closed profile, or your sketch won\'t produce a solid, but rather a set of open faces. If you don\'t want some of the objects to be included in the solid creation, turn them to construction elements with the Construction Mode tool.
-   Use the auto constraints feature to limit the number of constraints you\'ll have to add manually.
-   As a general rule, apply geometric constraints first, then dimensional constraints, and lock your sketch last. But remember   * rules are made to be broken. If you\'re having trouble manipulating your sketch, it may be useful to constrain a few objects first before completing your profile.
-   If possible, center your sketch to the origin (0,0) with the lock constraint. If your sketch is not symmetric, locate one of its points to the origin, or choose nice round numbers for the lock distances.
-   If you have the possibility to choose between the Length constraint and the Horizontal or Vertical Distance constraints, prefer the latter. Horizontal and Vertical Distance constraints are computationally cheaper.
-   In general, the best constraints to use are   * Horizontal and Vertical Constraints; Horizontal and Vertical Length Constraints; Point-to-Point Tangency. If possible, limit the use of these   * the general Length Constraint; Edge-to-Edge Tangency; Fix Point Onto a Line Constraint; Symmetry Constraint.
-   If in doubt about the validity of a sketch once it is complete (features turn green), close the Sketcher dialog, switch to the <img alt="" src=images/Workbench_Part.svg  style="width   *24px;"> [Part Workbench](Part_Workbench.md) and run **[<img src=images/Part_CheckGeometry.svg style="width   *16px"> [Check geometry](Part_CheckGeometry.md)**.

## Tutorials

-   [Sketcher tutorial](https   *//forum.freecadweb.org/viewtopic.php?f=36&t=30104) by chrisb. This is a 70-page long PDF document that serves as a detailed manual for the sketcher. It explains the basics of Sketcher usage, and goes into a lot of detail about the creation of geometrical shapes, and each of the constraints.
-   [Basic Sketcher Tutorial](Basic_Sketcher_Tutorial.md) for beginners
-   [Sketcher Micro Tutorial - Constraint Practices](Sketcher_Micro_Tutorial_-_Constraint_Practices.md)
-   [Sketcher requirement for a sketch](Sketcher_requirement_for_a_sketch.md) Minimum requirement for a sketch and Complete determination of a sketch

## Scripting

The [Sketcher scripting](Sketcher_scripting.md) page contains examples on how to create constraints from Python scripts.





{{Sketcher_Tools_navi

}} 

[Category   *Workbenches](Category_Workbenches.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > Sketcher Workbench/uk
