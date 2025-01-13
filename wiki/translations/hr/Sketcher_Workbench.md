# <img alt="Sketcher workbench icon" src=images/Workbench_Sketcher.svg  style="width:64px;"> Sketcher Workbench/hr






## Predstavljanje

With the <img alt="" src=images/Workbench_Sketcher.svg  style="width:24px;"> [Sketcher Workbench](Sketcher_Workbench.md) 2D sketches intended for use in other workbenches can be created. 2D sketches are the starting point for many CAD models. They typically define the profiles and paths for operations to create 3D shapes. A model may depend on several sketches for its final shape.

Together with boolean operations defined in the <img alt="" src=images/Workbench_Part.svg  style="width:16px;"> [Part Workbench](Part_Workbench.md), the Sketcher Workbench, or \"The Sketcher\" for short, forms the basis of the [constructive solid geometry](Constructive_solid_geometry.md) (CSG) method of building solids. Together with <img alt="" src=images/Workbench_PartDesign.svg  style="width:16px;"> [PartDesign Workbench](PartDesign_Workbench.md) operations, it also forms the basis of the [feature editing](Feature_editing.md) methodology of creating solids. But many other workbenches use sketches as well.

The Sketcher workbench features [constraints](#Constraints.md), allowing 2D shapes to follow precise geometrical definitions in terms of length, angles, and relationships (horizontality, verticality, perpendicularity, etc.). A constraint solver calculates the constrained-extent of 2D geometry and allows interactive exploration of the degrees-of-freedom of the sketch.

The Sketcher is not intended for producing 2D blueprints. Once sketches are used to generate a solid feature, they are automatically hidden and Constraints are only visible in Sketch edit mode. If you only need to produce 2D views for print, and don\'t want to create 3D models, check out the [Draft workbench](Draft_Workbench.md).

<img alt="" src=images/FC_ConstrainedSketch.png  style="width:450px;"> 
*A fully constrained sketch*

## Constraints

Constraints are used to limit the degrees of freedom of an object. For example, a line without constraints has 4 degrees of freedom (abbreviated as \"DoF\"): it can be moved horizontally or vertically, it can be stretched, and it can be rotated.

Applying a horizontal or vertical constraint, or an angle constraint (relative to another line or to one of the axes), will limit its capacity to rotate, thus leaving it with 3 degrees of freedom. Locking one of its points in relation to the origin will remove another 2 degrees of freedom. And applying a dimension constraint will remove the last degree of freedom. The line is then considered **fully-constrained**.

Objects can be constrained in relation to one another. Two lines can be joined through one of their points with the coincident point constraint. An angle can be set between them, or they can be set perpendicular. A line can be tangent to an arc or a circle, and so on. A complex Sketch with multiple objects may have a number of different solutions, and making it **fully-constrained** can mean that just one of these possible solutions has been reached based on the applied constraints.

There are two kinds of constraints: geometric and dimensional. They are detailed in the [Tools](#Tools.md) section below.

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

The Sketcher Workbench tools are located in the Sketch menu and/or several toolbars. <small>(v0.21)</small> : Almost all Sketcher toolbars are only displayed while a sketch is in edit mode. The only exception is the [Sketcher toolbar](#Sketcher_toolbar.md) which is only displayed if no sketch is in edit mode.

Some tools are also available from the [3D view](3D_view.md) context menu while a sketch is in edit mode, or from the context menus of the [Sketcher Dialog](Sketcher_Dialog.md).


<small>(v0.21)</small> 

: If a sketch is in edit mode the Structure toolbar is hidden as none of its tools can then be used.

### General

#### Sketcher toolbar 

-   <img alt="" src=images/Sketcher_NewSketch.svg‎‎  style="width:32px;"> [Create sketch](Sketcher_NewSketch.md): Creates a new sketch and opens the [Sketcher Dialog](Sketcher_Dialog.md) to edit it.

-   <img alt="" src=images/Sketcher_EditSketch.svg  style="width:32px;"> [Edit sketch](Sketcher_EditSketch.md): Opens the Sketcher Dialog to edit an existing sketch.

-   <img alt="" src=images/Sketcher_MapSketch.svg  style="width:32px;"> [Attach sketch](Sketcher_MapSketch.md): Attaches a sketch to selected geometry.

-   <img alt="" src=images/Sketcher_ReorientSketch.svg  style="width:32px;"> [Reorient sketch](Sketcher_ReorientSketch.md): Places a sketch on one of the main planes with an optional offset. It can also be used to detach a sketch.

-   <img alt="" src=images/Sketcher_ValidateSketch.svg  style="width:32px;"> [Validate sketch](Sketcher_ValidateSketch.md): Can analyze and repair a sketch that is no longer editable or has invalid constraints, or add missing coincident constraints.

-   <img alt="" src=images/Sketcher_MergeSketches.svg  style="width:32px;"> [Merge sketches](Sketcher_MergeSketches.md): Merges two or more sketches.

-   <img alt="" src=images/Sketcher_MirrorSketch.svg  style="width:32px;"> [Mirror sketch](Sketcher_MirrorSketch.md): Mirrors sketches across their X axis, Y axis, or origin.

#### Sketcher Edit Mode toolbar 

-   <img alt="" src=images/Sketcher_LeaveSketch.svg  style="width:32px;"> [Leave sketch](Sketcher_LeaveSketch.md): Finishes sketch edit mode and closes the [Sketcher Dialog](Sketcher_Dialog.md).

-   <img alt="" src=images/Sketcher_ViewSketch.svg  style="width:32px;"> [View sketch](Sketcher_ViewSketch.md): Aligns the [3D view](3D_view.md) with the sketch.

-   <img alt="" src=images/Sketcher_ViewSection.svg  style="width:32px;"> [View section](Sketcher_ViewSection.md): Toggles a temporary section plane that hides any objects and parts of objects in front of the sketch plane.

#### Sketcher edit tools toolbar 

-   <img alt="" src=images/Sketcher_Grid.svg  style="width:32px;"> [Toggle grid](Sketcher_Grid.md): Toggles the grid in the sketch currently being edited. Settings can be changed in the related menu. <small>(v0.21)</small> 

-   <img alt="" src=images/Sketcher_Snap.svg  style="width:32px;"> [Toggle snap](Sketcher_Snap.md): Toggles snapping in all sketches. Settings can be changed in the related menu. <small>(v0.21)</small> 

-   <img alt="" src=images/Sketcher_RenderingOrder.svg  style="width:32px;"> [Configure rendering order](Sketcher_RenderingOrder.md): The rendering order of all sketches can be changed in the related menu. <small>(v0.21)</small> 

#### Other

-   <img alt="" src=images/Sketcher_StopOperation.svg  style="width:32px;"> [Stop operation](Sketcher_StopOperation.md): Stops any currently running geometry or constraint creation tool.



### Geometrije skice 

These are tools for creating objects.

-   <img alt="" src=images/Sketcher_CreatePoint.svg  style="width:32px;"> [Point](Sketcher_CreatePoint.md): Creates a point.

-   <img alt="" src=images/Sketcher_CreatePolyline.svg  style="width:32px;"> [Polyline](Sketcher_CreatePolyline.md): Creates a series of line and arc segments connected by their endpoints. The tool has several modes.

-   <img alt="" src=images/Sketcher_CreateLine.svg  style="width:32px;"> [Line](Sketcher_CreateLine.md): Creates a line. <small>(v1.0)</small> : The tool has three modes.

-   <img alt="" src=images/Sketcher_CreateArc.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Create arc:

  - <img alt="" src=images/Sketcher_CreateArc.svg  style="width:32px;"> [Arc by center](Sketcher_CreateArc.md): Creates an arc by its center and its endpoints. <small>(v1.0)</small> : Or by its endpoints and a point along the arc.

  - <img alt="" src=images/Sketcher_Create3PointArc.svg  style="width:32px;"> [Arc by 3 points](Sketcher_Create3PointArc.md): Creates an arc by its endpoints and a point along the arc. <small>(v1.0)</small> : This is the same tool as [Arc by center](Sketcher_CreateArc.md) but with a different initial mode.

  - <img alt="" src=images/Sketcher_CreateArcOfEllipse.svg  style="width:32px;"> [Arc of ellipse](Sketcher_CreateArcOfEllipse.md): Creates an arc of ellipse.

  - <img alt="" src=images/Sketcher_CreateArcOfHyperbola.svg  style="width:32px;"> [Arc of hyperbola](Sketcher_CreateArcOfHyperbola.md): Creates an arc of hyperbola.

  - <img alt="" src=images/Sketcher_CreateArcOfParabola.svg  style="width:32px;"> [Arc of parabola](Sketcher_CreateArcOfParabola.md): Creates an arc of parabola.

-   <img alt="" src=images/Sketcher_CreateCircle.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Create circle/ellipse:

  - <img alt="" src=images/Sketcher_CreateCircle.svg  style="width:32px;"> [Circle by center](Sketcher_CreateCircle.md): Creates a circle by its center and a point along the circle. <small>(v1.0)</small> : Or by three points along the circle.

  - <img alt="" src=images/Sketcher_Create3PointCircle.svg  style="width:32px;"> [Circle by 3 points](Sketcher_Create3PointCircle.md): Creates a circle by three points along the circle. <small>(v1.0)</small> : This is the same tool as [Circle by center](Sketcher_CreateCircle.md) but with a different initial mode.

  - <img alt="" src=images/Sketcher_CreateEllipseByCenter.svg  style="width:32px;"> [Ellipse by center](Sketcher_CreateEllipseByCenter.md): Creates an ellipse by its center, an endpoint of one of its axes, and a point along the ellipse. <small>(v1.0)</small> : Or by both endpoints of one of its axes and a point along the ellipse.

  - <img alt="" src=images/Sketcher_CreateEllipseBy3Points.svg  style="width:32px;"> [Ellipse by 3 points](Sketcher_CreateEllipseBy3Points.md): Creates an ellipse by the endpoints of one of its axes and a point along the ellipse. <small>(v1.0)</small> : This is the same tool as [Ellipse by center](Sketcher_CreateEllipseByCenter.md) but with a different initial mode.

-   <img alt="" src=images/Sketcher_CreateRectangle.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Create rectangle:

  - <img alt="" src=images/Sketcher_CreateRectangle.svg  style="width:32px;"> [Rectangle](Sketcher_CreateRectangle.md): Creates a rectangle. <small>(v1.0)</small> : The tool has four modes. Rounded corners and creating an offset copy are optional features.

  - <img alt="" src=images/Sketcher_CreateRectangle_Center.svg  style="width:32px;"> [Centered rectangle](Sketcher_CreateRectangle_Center.md): Creates a centered rectangle. <small>(v1.0)</small> : This is the same tool as [Rectangle](Sketcher_CreateRectangle.md) but with a different initial mode.

  - <img alt="" src=images/Sketcher_CreateOblong.svg  style="width:32px;"> [Rounded rectangle](Sketcher_CreateOblong.md): Creates a rounded rectangle. Idem.

-   <img alt="" src=images/Sketcher_CreateHexagon.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Create regular polygon:

  - <img alt="" src=images/Sketcher_CreateTriangle.svg  style="width:32px;"> [Triangle](Sketcher_CreateTriangle.md): creates an equilateral triangle. <small>(v1.0)</small> : This is the same tool as [Regular polygon](Sketcher_CreateRegularPolygon.md) but with the number of sides preset to a specif value.

  - <img alt="" src=images/Sketcher_CreateSquare.svg  style="width:32px;"> [Square](Sketcher_CreateSquare.md): Creates a square. Idem.

  - <img alt="" src=images/Sketcher_CreatePentagon.svg  style="width:32px;"> [Pentagon](Sketcher_CreatePentagon.md): Creates a pentagon. Idem.

  - <img alt="" src=images/Sketcher_CreateHexagon.svg  style="width:32px;"> [Hexagon](Sketcher_CreateHexagon.md): Creates a hexagon. Idem.

  - <img alt="" src=images/Sketcher_CreateHeptagon.svg  style="width:32px;"> [Heptagon](Sketcher_CreateHeptagon.md): Creates a heptagon. Idem.

  - <img alt="" src=images/Sketcher_CreateOctagon.svg  style="width:32px;"> [Octagon](Sketcher_CreateOctagon.md): Creates an octagon. Idem.

  - <img alt="" src=images/Sketcher_CreateRegularPolygon.svg  style="width:32px;"> [Regular polygon](Sketcher_CreateRegularPolygon.md): Creates a regular polygon. The number of sides can be specified.

-   <img alt="" src=images/Sketcher_CreateSlot.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Create slot:

  - <img alt="" src=images/Sketcher_CreateSlot.svg  style="width:32px;"> [Slot](Sketcher_CreateSlot.md): Creates a slot.

  - <img alt="" src=images/Sketcher_CreateArcSlot.svg  style="width:32px;"> [Arc slot](Sketcher_CreateArcSlot.md): Creates an arc slot. <small>(v1.0)</small> 

-   <img alt="" src=images/Sketcher_CreateBSpline.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Create B-spline:

  - <img alt="" src=images/Sketcher_CreateBSpline.svg  style="width:32px;"> [B-spline by control points](Sketcher_CreateBSpline.md): Creates a B-spline curve by control points. <small>(v1.0)</small> : Or by knot points.

  - <img alt="" src=images/Sketcher_CreatePeriodicBSpline.svg  style="width:32px;"> [Periodic B-spline by control points](Sketcher_CreatePeriodicBSpline.md): Creates a periodic (closed) B-spline curve by control points. <small>(v1.0)</small> : This is the same tool as [B-spline by control points](Sketcher_CreateBSpline.md) but with a different initial mode.

  - <img alt="" src=images/Sketcher_CreateBSplineByInterpolation.svg  style="width:32px;"> [B-spline by knots](Sketcher_CreateBSplineByInterpolation.md): Creates a B-spline curve by knot points. Idem.

  - <img alt="" src=images/Sketcher_CreatePeriodicBSplineByInterpolation.svg  style="width:32px;"> [Periodic B-spline by knots](Sketcher_CreatePeriodicBSplineByInterpolation.md): Creates a periodic (closed) B-spline curve by knot points. Idem.

-   <img alt="" src=images/Sketcher_ToggleConstruction.svg  style="width:32px;"> [Toggle construction geometry](Sketcher_ToggleConstruction.md): Either toggles the geometry creation tools to/from construction mode, or toggles selected geometry to/from construction geometry.



### Ograničenja skice 

These are tools for creating [constraints](#Constraints.md). Some constraints require the use of [Helper constraints](Sketcher_helper_constraint.md).

-   <img alt="" src=images/Sketcher_Dimension.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Dimensional constraints:

  - <img alt="" src=images/Sketcher_Dimension.svg  style="width:32px;"> [Dimension](Sketcher_Dimension.md): Is the context-sensitive constraint tool of the Sketcher Workbench. Based on the current selection, it offers appropriate dimensional constraints, but also geometric constraints. <small>(v1.0)</small> 

  - <img alt="" src=images/Sketcher_ConstrainDistanceX.svg  style="width:32px;"> [Horizontal distance](Sketcher_ConstrainDistanceX.md): Fixes the horizontal distance between two points or the endpoints of a line. If a single point is pre-selected, the distance is relative to the origin of the sketch.

  - <img alt="" src=images/Sketcher_ConstrainDistanceY.svg  style="width:32px;"> [Vertical distance](Sketcher_ConstrainDistanceY.md): Fixes the vertical distance between two points or the endpoints of a line. If a single point is pre-selected, the distance is relative to the origin of the sketch.

  - <img alt="" src=images/Sketcher_ConstrainDistance.svg  style="width:32px;"> [Distance](Sketcher_ConstrainDistance.md): Fixes the length of a line, the distance between two points, the perpendicular distance between a point and a line; or, <small>(v0.21)</small> , the distance between the edges of two circles or arcs, or between the edge of a circle or arc and a line; or, <small>(v1.0)</small> , the length of an arc.

  - <img alt="" src=images/Sketcher_ConstrainRadiam.svg  style="width:32px;"> [Auto radius/diameter](Sketcher_ConstrainRadiam.md): Fixes the radius of arcs and B-spline weight circles, and the diameter of circles.

  - <img alt="" src=images/Sketcher_ConstrainRadius.svg  style="width:32px;"> [Radius](Sketcher_ConstrainRadius.md): Fixes the radius of circles, arcs and B-spline weight circles.

  - <img alt="" src=images/Sketcher_ConstrainDiameter.svg  style="width:32px;"> [Diameter](Sketcher_ConstrainDiameter.md): Fixes the diameter of circles and arcs.

  - <img alt="" src=images/Sketcher_ConstrainAngle.svg  style="width:32px;"> [Angle](Sketcher_ConstrainAngle.md): Fixes the angle between two edges, the angle of a line with the horizontal axis of the sketch, or the aperture angle of a circular arc.

  - <img alt="" src=images/Sketcher_ConstrainLock.svg  style="width:32px;"> [Lock](Sketcher_ConstrainLock.md): Applies [Horizontal distance](Sketcher_ConstrainDistanceX.md) and [Vertical distance](Sketcher_ConstrainDistanceY.md) constraints to points. If a single point is selected the constraints reference the origin of the sketch. If two or more points are selected the constraints reference the last point in the selection.

-   <img alt="" src=images/Sketcher_ConstrainCoincidentUnified.svg  style="width:32px;"> [Coincident (unified)](Sketcher_ConstrainCoincidentUnified.md): Creates a coincident constraint between points, fixes points on edges or axes, or creates a concentric constraint. It combines the [Coincident](Sketcher_ConstrainCoincident.md) and [Point on object](Sketcher_ConstrainPointOnObject.md) tools. <small>(v1.0)</small> 

-   <img alt="" src=images/Sketcher_ConstrainCoincident.svg  style="width:32px;"> [Coincident](Sketcher_ConstrainCoincident.md): Creates a coincident constraint between points, or a concentric constraint.

-   <img alt="" src=images/Sketcher_ConstrainPointOnObject.svg  style="width:32px;"> [Point on object](Sketcher_ConstrainPointOnObject.md): Fixes points on edges or axes.

-   <img alt="" src=images/Sketcher_ConstrainHorVer.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;">Horizontal/vertical constraints:

  - <img alt="" src=images/Sketcher_ConstrainHorVer.svg  style="width:32px;"> [Horizontal/vertical](Sketcher_ConstrainHorVer.md): Constrains lines or pairs of points to be horizontal or vertical, whichever is closest to the current alignment. It combines the [Horizontal](Sketcher_ConstrainHorizontal.md) and [Vertical](Sketcher_ConstrainVertical.md) tools. <small>(v1.0)</small> 

  - <img alt="" src=images/Sketcher_ConstrainHorizontal.svg  style="width:32px;"> [Horizontal](Sketcher_ConstrainHorizontal.md): Constrains lines or pairs of points to be horizontal.

  - <img alt="" src=images/Sketcher_ConstrainVertical.svg  style="width:32px;"> [Vertical](Sketcher_ConstrainVertical.md): Constrains lines or pairs of points to be vertical.

-   <img alt="" src=images/Sketcher_ConstrainParallel.svg  style="width:32px;"> [Parallel](Sketcher_ConstrainParallel.md): Constrains lines to be parallel.

-   <img alt="" src=images/Sketcher_ConstrainPerpendicular.svg  style="width:32px;"> [Perpendicular](Sketcher_ConstrainPerpendicular.md): Constrains two lines to be perpendicular, or two edges, or an edge and an axis, to be perpendicular at their intersection. The constraint can also connect two edges, forcing them to be perpendicular at the joint.

-   <img alt="" src=images/Sketcher_ConstrainTangent.svg  style="width:32px;"> [Tangent or collinear](Sketcher_ConstrainTangent.md): Constrains two edges, or an edge and an axis, to be tangent. The constraint can also connect two edges, forcing them to be tangent at the joint. If two lines are selected they are made collinear.

-   <img alt="" src=images/Sketcher_ConstrainEqual.svg  style="width:32px;"> [Equal](Sketcher_ConstrainEqual.md): Constrains edges to have an equal length (lines) or curvature (other edges except B-splines).

-   <img alt="" src=images/Sketcher_ConstrainSymmetric.svg  style="width:32px;"> [Symmetric](Sketcher_ConstrainSymmetric.md): Constrains two points to be symmetrical around a line or axis, or around a third point.

-   <img alt="" src=images/Sketcher_ConstrainBlock.svg  style="width:32px;"> [Block](Sketcher_ConstrainBlock.md): Blocks edges in place with a single constraint. It is mainly intended for B-splines.

-   <img alt="" src=images/Sketcher_ConstrainSnellsLaw.svg  style="width:32px;"> [Refraction (Snell\'s law)](Sketcher_ConstrainSnellsLaw.md): Constrains two lines to follow the law of refraction of light as it penetrates through an interface.

-   <img alt="" src=images/Sketcher_ToggleDrivingConstraint.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Toggle constraints:

  - <img alt="" src=images/Sketcher_ToggleDrivingConstraint.svg  style="width:32px;"> [Toggle driving/reference constraint](Sketcher_ToggleDrivingConstraint.md): Toggles the dimensional constraint creation tools between driving and reference mode, or toggles selected dimensional constraints between those modes.

  - <img alt="" src=images/Sketcher_ToggleActiveConstraint.svg  style="width:32px;"> [Activate/deactivate constraint](Sketcher_ToggleActiveConstraint.md): Activates or deactivates selected constraints.

### Sketcher tools 

-   <img alt="" src=images/Sketcher_CreateFillet.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Create fillet/chamfer:

  - <img alt="" src=images/Sketcher_CreateFillet.svg  style="width:32px;"> [Fillet](Sketcher_CreateFillet.md): Creates a fillet between two non-parallel edges. <small>(v1.0)</small> : The tool can also create a chamfer.

  - <img alt="" src=images/Sketcher_CreateChamfer.svg  style="width:32px;"> [Chamfer](Sketcher_CreateChamfer.md): creates a chamfer between two non-parallel edges. This is the same tool as [Fillet](Sketcher_CreateFillet.md) but with a different initial mode. <small>(v1.0)</small> 

-   <img alt="" src=images/Sketcher_Trimming.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Edit edge:

  - <img alt="" src=images/Sketcher_Trimming.svg  style="width:32px;"> [Trim](Sketcher_Trimming.md): Trims an edge at the nearest intersections with other edges.

  - <img alt="" src=images/Sketcher_Split.svg  style="width:32px;"> [Split](Sketcher_Split.md): Splits an edge while transferring most constraints.

  - <img alt="" src=images/Sketcher_Extend.svg  style="width:32px;"> [Extend](Sketcher_Extend.md): Extends or shortens a line or an arc to an arbitrary location, or to a target edge or point.

-   <img alt="" src=images/Sketcher_External.svg  style="width:32px;"> [External geometry](Sketcher_External.md): Projects edges and/or vertices belonging to objects outside the sketch onto the sketch plane. {{VersionMinus|1.0}}

-   <img alt="" src=images/Sketcher_Projection.svg  style="width:32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> External geometry:

  - <img alt="" src=images/Sketcher_Projection.svg  style="width:32px;"> [Create external projection geometry](Sketcher_Projection.md): Creates the projection edges of external geometry. <small>(v1.1)</small> 

  - <img alt="" src=images/Sketcher_Intersection.svg  style="width:32px;"> [Create external intersection geometry](Sketcher_Intersection.md): Creates the intersection edges of external geometry with the sketch plane. <small>(v1.1)</small> 

-   <img alt="" src=images/Sketcher_CarbonCopy.svg  style="width:32px;"> [Carbon copy](Sketcher_CarbonCopy.md): Copies all geometry and constraints from another sketch into the active sketch.

-   <img alt="" src=images/Sketcher_SelectOrigin.svg  style="width:32px;"> [Select origin](Sketcher_SelectOrigin.md): Selects the origin of the sketch.

-   <img alt="" src=images/Sketcher_SelectHorizontalAxis.svg  style="width:32px;"> [Select horizontal axis](Sketcher_SelectHorizontalAxis.md): Selects the horizontal axis of the sketch.

-   <img alt="" src=images/Sketcher_SelectVerticalAxis.svg  style="width:32px;"> [Select vertical axis](Sketcher_SelectVerticalAxis.md): Selects the vertical axis of the sketch.

-   <img alt="" src=images/Sketcher_Translate.svg  style="width:32px;"> [Array transform](Sketcher_Translate.md): Moves or optionally creates copies of selected elements. <small>(v1.0)</small> 

-   <img alt="" src=images/Sketcher_Rotate.svg  style="width:32px;"> [Polar transform](Sketcher_Rotate.md): Rotates or optionally creates rotated copies of selected elements. <small>(v1.0)</small> 

-   <img alt="" src=images/Sketcher_Scale.svg  style="width:32px;"> [Scale transform](Sketcher_Scale.md): Scales or optionally creates scaled copies of selected elements. <small>(v1.0)</small> 

-   <img alt="" src=images/Sketcher_Offset.svg  style="width:32px;"> [Offset geometry](Sketcher_Offset.md): Creates equidistant edges around selected edges. <small>(v1.0)</small> 

-   <img alt="" src=images/Sketcher_Symmetry.svg  style="width:32px;"> [Symmetry](Sketcher_Symmetry.md): Creates mirrored copies of selected elements.

-   <img alt="" src=images/Sketcher_RemoveAxesAlignment.svg  style="width:32px;"> [Remove axes alignment](Sketcher_RemoveAxesAlignment.md): Removes the axes alignment of selected edges by replacing [Horizontal](Sketcher_ConstrainHorizontal.md) and [Vertical](Sketcher_ConstrainVertical.md) constraints with [Parallel](Sketcher_ConstrainParallel.md) and [Perpendicular](Sketcher_ConstrainPerpendicular.md) constraints.

-   <img alt="" src=images/Sketcher_DeleteAllGeometry.svg  style="width:32px;"> [Delete all geometry](Sketcher_DeleteAllGeometry.md): Deletes all geometry and all constraints from the sketch.

-   <img alt="" src=images/Sketcher_DeleteAllConstraints.svg  style="width:32px;"> [Delete all constraints](Sketcher_DeleteAllConstraints.md): Deletes all constraints from the sketch.

-   <img alt="" src=images/Edit-copy.svg  style="width:32px;"> Copy in Sketcher: See [Copy, cut and paste](#Copy,_cut_and_paste.md).

-   <img alt="" src=images/Edit-cut.svg  style="width:32px;"> Cut in Sketcher: See [Copy, cut and paste](#Copy,_cut_and_paste.md).

-   <img alt="" src=images/Edit-paste.svg  style="width:32px;"> Paste in Sketcher: See [Copy, cut and paste](#Copy,_cut_and_paste.md).

### Sketcher B-spline tools 

-   <img alt="" src=images/Sketcher_BSplineConvertToNURBS.svg  style="width:32px;"> [Convert geometry to B-spline](Sketcher_BSplineConvertToNURBS.md): Converts edges to B-splines.

-   <img alt="" src=images/Sketcher_BSplineIncreaseDegree.svg  style="width:32px;"> [Increase B-spline degree](Sketcher_BSplineIncreaseDegree.md): Increases the degree (order) of B-splines.

-   <img alt="" src=images/Sketcher_BSplineDecreaseDegree.svg  style="width:32px;"> [Decrease B-spline degree](Sketcher_BSplineDecreaseDegree.md): Decreases the degree (order) of B-splines.

-   <img alt="" src=images/Sketcher_BSplineIncreaseKnotMultiplicity.svg  style="width:32px;"> [Increase knot multiplicity](Sketcher_BSplineIncreaseKnotMultiplicity.md): Increases the multiplicity of a B-spline knot.

-   <img alt="" src=images/Sketcher_BSplineDecreaseKnotMultiplicity.svg  style="width:32px;"> [Decrease knot multiplicity](Sketcher_BSplineDecreaseKnotMultiplicity.md): Decreases the multiplicity of a B-spline knot.

-   <img alt="" src=images/Sketcher_BSplineInsertKnot.svg  style="width:32px;"> [Insert knot](Sketcher_BSplineInsertKnot.md): Inserts a knot into a B-spline or increases the multiplicity of an existing knot.

-   <img alt="" src=images/Sketcher_JoinCurves.svg  style="width:32px;"> [Join curves](Sketcher_JoinCurves.md): Creates a B-spline by joining two existing B-splines or other edges. <small>(v0.21)</small> 

### Sketcher visual 

-   <img alt="" src=images/Sketcher_SelectElementsWithDoFs.svg  style="width:32px;"> [Select unconstrained DoF](Sketcher_SelectElementsWithDoFs.md): Selects the not fully constrained elements in the sketch.

-   <img alt="" src=images/Sketcher_SelectConstraints.svg  style="width:32px;"> [Select associated constraints](Sketcher_SelectConstraints.md): Selects the constraints associated with sketch elements.

-   <img alt="" src=images/Sketcher_SelectElementsAssociatedWithConstraints.svg  style="width:32px;"> [Select associated geometry](Sketcher_SelectElementsAssociatedWithConstraints.md): Selects the sketch elements associated with constraints.

-   <img alt="" src=images/Sketcher_SelectRedundantConstraints.svg  style="width:32px;"> [Select redundant constraints](Sketcher_SelectRedundantConstraints.md): Selects the redundant constraints in the sketch.

-   <img alt="" src=images/Sketcher_SelectConflictingConstraints.svg  style="width:32px;"> [Select conflicting constraints](Sketcher_SelectConflictingConstraints.md): Selects the conflicting constraints in the sketch.

-   <img alt="" src=images/Sketcher_ArcOverlay.svg  style="width:32px;"> [Show/hide circular helper for arcs](Sketcher_ArcOverlay.md): Shows or hides the circular helpers (underlying virtual circles) for arcs in all sketches. <small>(v1.0)</small> 

-   <img alt="" src=images/Sketcher_BSplinePolygon.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Show/hide B-spline information layer:

  - <img alt="" src=images/Sketcher_BSplineDegree.svg  style="width:32px;"> [Show/hide B-spline degree](Sketcher_BSplineDegree.md): Shows or hides the B-spline degree in all sketches.

  - <img alt="" src=images/Sketcher_BSplinePolygon.svg  style="width:32px;"> [Show/hide B-spline control polygon](Sketcher_BSplinePolygon.md): Shows or hides the B-spline control polygon in all sketches.

  - <img alt="" src=images/Sketcher_BSplineComb.svg  style="width:32px;"> [Show/hide B-spline curvature comb](Sketcher_BSplineComb.md): Shows or hides the B-spline curvature comb in all sketches.

  - <img alt="" src=images/Sketcher_BSplineKnotMultiplicity.svg  style="width:32px;"> [Show/hide B-spline knot multiplicity](Sketcher_BSplineKnotMultiplicity.md): Shows or hides the B-spline knot multiplicity in all sketches.

  - <img alt="" src=images/Sketcher_BSplinePoleWeight.svg  style="width:32px;"> [Show/hide B-spline control point weight](Sketcher_BSplinePoleWeight.md): Shows or hides the B-spline control point weight in all sketches.

-   <img alt="" src=images/Sketcher_RestoreInternalAlignmentGeometry.svg  style="width:32px;"> [Show/hide internal geometry](Sketcher_RestoreInternalAlignmentGeometry.md): Deletes the internal geometry of elements, or recreates missing internal geometry.

-   <img alt="" src=images/Sketcher_SwitchVirtualSpace.svg  style="width:32px;"> [Switch virtual space](Sketcher_SwitchVirtualSpace.md): (un)hides constraints or switches the visible virtual space.

### Obsolete tools 

-   <img alt="" src=images/Sketcher_Clone.svg  style="width:32px;"> [Clone](Sketcher_Clone.md): Clones a Sketcher element. Not available in <small>(v1.0)</small> .

-   <img alt="" src=images/Sketcher_CloseShape.svg  style="width:32px;"> [Close shape](Sketcher_CloseShape.md): Creates a closed shape by applying coincident constraints to endpoints. Not available in <small>(v0.21)</small> .

-   <img alt="" src=images/Sketcher_CreatePointFillet.svg  style="width:32px;"> [Corner-preserving fillet](Sketcher_CreatePointFillet.md): Creates a fillet between two non-parallel lines while preserving their corner point. Not available in <small>(v1.0)</small> .

-   <img alt="" src=images/Sketcher_ConnectLines.svg  style="width:32px;"> [Connect edges](Sketcher_ConnectLines.md): Connect Sketcher elements by applying coincident constraints to endpoints. Not available in <small>(v0.21)</small> .

-   <img alt="" src=images/Sketcher_Copy.svg  style="width:32px;"> [Copy](Sketcher_Copy.md): Copies a Sketcher element. Not available in <small>(v1.0)</small> .

-   <img alt="" src=images/Sketcher_Move.svg  style="width:32px;"> [Move](Sketcher_Move.md): Moves the selected geometry taking as reference the last selected point. Not available in <small>(v1.0)</small> .

-   <img alt="" src=images/Sketcher_RectangularArray.svg  style="width:32px;"> [Rectangular array](Sketcher_RectangularArray.md): Creates an array of selected Sketcher elements. Not available in <small>(v1.0)</small> .




<div class="mw-translate-fuzzy">

### Postavke


</div>

-   <img alt="" src=images/Workbench_Sketcher.svg  style="width:32px;"> [Preferences](Sketcher_Preferences.md): Preferences for the Sketcher Workbench.

## Best practices 

Every CAD user develops their own way of working over time, but there are some useful general principles to follow.

-   A series of simple sketches is easier to manage than a single complex one. For example, a first sketch can be created for the base 3D feature (either a pad or a revolve), while a second one can contain holes or cutouts (pockets). Some details can be left out, to be realized later on as 3D features. You can choose to avoid fillets in your sketch if there are too many, and add them as a 3D feature.
-   Always create a closed profile, or your sketch won\'t produce a solid, but rather a set of open faces. If you don\'t want some of the objects to be included in the solid creation, turn them to construction elements with the Construction Mode tool.
-   Use the Auto constraints feature to limit the number of constraints you\'ll have to add manually.
-   As a general rule, apply geometric constraints first, then dimensional constraints, and lock your sketch last. But remember: rules are made to be broken. If you\'re having trouble manipulating your sketch, it may be useful to constrain a few objects first before completing your profile.
-   If possible, center your sketch at the origin (0,0) with the Lock constraint. If your sketch is not symmetric, locate one of its points at the origin, or choose nice round numbers for the lock distances.
-   If you have the possibility to choose between the Length constraint and the Horizontal or Vertical distance constraints, prefer the latter. Horizontal and Vertical distance constraints are computationally cheaper.
-   In general, the best constraints to use are: Horizontal and Vertical constraints; Horizontal and Vertical length constraints; point-to-point Tangency. If possible, limit the use of these: the general Length constraint; edge-to-edge Tangency; Point on object constraint; Symmetric constraint.
-   If in doubt about the validity of a sketch once it is complete (features turn green), close the Sketcher dialog and use <img alt="" src=images/Sketcher_ValidateSketch.svg  style="width:24px;"> [Validate sketch](Sketcher_ValidateSketch.md).

## Tutorials

-   [Sketcher Lecture](https://forum.freecadweb.org/viewtopic.php?f=36&t=30104) by chrisb. This is a more than 80 page PDF document that serves as a detailed manual for the Sketcher. It explains the basics of Sketcher usage, and goes into a lot of detail about the creation of geometrical shapes, and each of the constraints.
-   [Basic Sketcher Tutorial](Basic_Sketcher_Tutorial.md) for beginners
-   [Sketcher Micro Tutorial - Constraint Practices](Sketcher_Micro_Tutorial_-_Constraint_Practices.md)
-   [Sketcher requirement for a sketch](Sketcher_requirement_for_a_sketch.md) Minimum requirement for a sketch and Complete determination of a sketch

## Scripting

The [Sketcher scripting](Sketcher_scripting.md) page contains examples on how to create constraints from Python scripts.

## Examples

For some ideas of what can be achieved with Sketcher tools, have a look at: [Sketcher examples](Sketcher_Examples.md).

<img alt="" src=images/Sketcher_ExampleHinge-01.gif  style="width:80px;"> <img alt="" src=images/Sketcher_ExampleHinge-15.png  style="width:90px;">


<div class="mw-translate-fuzzy">





</div>


{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > Sketcher Workbench/hr
