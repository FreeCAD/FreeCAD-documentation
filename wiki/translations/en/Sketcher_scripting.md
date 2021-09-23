# Sketcher scripting/en
{{TOCright}}

## Creating a constraint using Python 

A geometric constraint <img alt="" src=images/Sketcher_ConstrainCoincident.svg  style="width:24px;"> <img alt="" src=images/Sketcher_ConstrainPointOnObject.svg  style="width:24px;"> <img alt="" src=images/Sketcher_ConstrainVertical.svg  style="width:24px;"> <img alt="" src=images/Sketcher_ConstrainHorizontal.svg  style="width:24px;"> <img alt="" src=images/Sketcher_ConstrainParallel.svg  style="width:24px;"> <img alt="" src=images/Sketcher_ConstrainPerpendicular.svg  style="width:24px;"> <img alt="" src=images/Sketcher_ConstrainTangent.svg  style="width:24px;"> <img alt="" src=images/Sketcher_ConstrainEqual.svg  style="width:24px;"> <img alt="" src=images/Sketcher_ConstrainSymmetric.svg  style="width:24px;"> <img alt="" src=images/Sketcher_ConstrainBlock.svg  style="width:24px;"> and the special <img alt="" src=images/Sketcher_ConstrainInternalAlignment.svg  style="width:24px;"> [InternalAlignment](Sketcher_ConstrainInternalAlignment.md) constraints can be created from macros and from the python console by using the following command:


```pythonSketch.addConstraint(Sketcher.Constraint(ConstraintType, EdgeOrPartOfEdge…)) 
```

A dimensional constraint <img alt="" src=images/Sketcher_ConstrainLock.svg  style="width:24px;"> <img alt="" src=images/Sketcher_ConstrainDistanceX.svg  style="width:24px;"> <img alt="" src=images/Sketcher_ConstrainDistanceY.svg  style="width:24px;"> <img alt="" src=images/Sketcher_ConstrainDistance.svg  style="width:24px;"> <img alt="" src=images/Sketcher_ConstrainRadius.svg  style="width:24px;"> <img alt="" src=images/Sketcher_ConstrainDiameter.svg  style="width:24px;"> <img alt="" src=images/Sketcher_ConstrainAngle.svg  style="width:24px;"> and the special constraint <img alt="" src=images/Sketcher_ConstrainSnellsLaw.svg  style="width:24px;"> [Snell\'s law](Sketcher_ConstrainSnellsLaw.md) can be created from macros and from the python console by using the following command:


```pythonSketch.addConstraint(Sketcher.Constraint(DimensionalConstraintType, EdgeOrPartOfEdge…, App.Units.Quantity('float_value unit'))) 
```


:   e.g.


```pythonSketch.addConstraint(Sketcher.Constraint(DimensionalConstraintType, EdgeOrPartOfEdge…, App.Units.Quantity('123.0 mm'))) 
```

The first argument `ConstraintType` is described below in [Constraint types](#Constraint_types.md).

A constraint can take up to six arguments which are edges or indicate which sub-part of an edge is used by the constraint. See the documentation of individual constraints for details on what combinations of edges and sub-parts of edges can be passed as arguments. The main issue with this function is to identify correctly the line number and the vertex number of the lines you want to process. The sections below describe how to [identify the numbering of a line](#Identifying_the_numbering_of_a_line.md)) and how to [Identify the numbering of the sub-parts of a line](#Identifying_the_numbering_of_the_sub-parts_of_a_line.md)).

## Constraint types 

For geometric constraints, the first argument is one of the following. See the corresponding feature page for the possible combinations of arguments allowed for each constraint.

+----------------------------+--------------------------------------------------------------------------------------------+---------------------------------------------------------------+
| Code                       | Icon                                                                                       | Feature                                                       |
+============================+============================================================================================+===============================================================+
|             | <img alt="" src=images/Sketcher_ConstrainCoincident.svg  style="width:24px;">       | [Coincident](Sketcher_ConstrainCoincident.md)         |
| `'Coincident'`    |                                                                                            |                                                               |
|                         |                                                                                            |                                                               |
+----------------------------+--------------------------------------------------------------------------------------------+---------------------------------------------------------------+
|             | <img alt="" src=images/Sketcher_ConstrainPointOnObject.svg  style="width:24px;"> | [Point On Object](Sketcher_ConstrainPointOnObject.md) |
| `'PointOnObject'` |                                                                                            |                                                               |
|                         |                                                                                            |                                                               |
+----------------------------+--------------------------------------------------------------------------------------------+---------------------------------------------------------------+
|             | <img alt="" src=images/Sketcher_ConstrainVertical.svg  style="width:24px;">           | [Vertical](Sketcher_ConstrainVertical.md)             |
| `'Vertical'`      |                                                                                            |                                                               |
|                         |                                                                                            |                                                               |
+----------------------------+--------------------------------------------------------------------------------------------+---------------------------------------------------------------+
|             | <img alt="" src=images/Sketcher_ConstrainHorizontal.svg  style="width:24px;">       | [Horizontal](Sketcher_ConstrainHorizontal.md)         |
| `'Horizontal'`    |                                                                                            |                                                               |
|                         |                                                                                            |                                                               |
+----------------------------+--------------------------------------------------------------------------------------------+---------------------------------------------------------------+
|             | <img alt="" src=images/Sketcher_ConstrainParallel.svg  style="width:24px;">           | [Parallel](Sketcher_ConstrainParallel.md)             |
| `'Parallel'`      |                                                                                            |                                                               |
|                         |                                                                                            |                                                               |
+----------------------------+--------------------------------------------------------------------------------------------+---------------------------------------------------------------+
|             | <img alt="" src=images/Sketcher_ConstrainPerpendicular.svg  style="width:24px;"> | [Perpendicular](Sketcher_ConstrainPerpendicular.md)   |
| `'Perpendicular'` |                                                                                            |                                                               |
|                         |                                                                                            |                                                               |
+----------------------------+--------------------------------------------------------------------------------------------+---------------------------------------------------------------+
|             | <img alt="" src=images/Sketcher_ConstrainTangent.svg  style="width:24px;">             | [Tangent](Sketcher_ConstrainTangent.md)               |
| `'Tangent'`       |                                                                                            |                                                               |
|                         |                                                                                            |                                                               |
+----------------------------+--------------------------------------------------------------------------------------------+---------------------------------------------------------------+
|             | <img alt="" src=images/Sketcher_ConstrainEqual.svg  style="width:24px;">                 | [Equal](Sketcher_ConstrainEqual.md)                   |
| `'Equal'`         |                                                                                            |                                                               |
|                         |                                                                                            |                                                               |
+----------------------------+--------------------------------------------------------------------------------------------+---------------------------------------------------------------+
|             | <img alt="" src=images/Sketcher_ConstrainSymmetric.svg  style="width:24px;">         | [Symmetric](Sketcher_ConstrainSymmetric.md)           |
| `'Symmetric'`     |                                                                                            |                                                               |
|                         |                                                                                            |                                                               |
+----------------------------+--------------------------------------------------------------------------------------------+---------------------------------------------------------------+
|             | <img alt="" src=images/Sketcher_ConstrainBlock.svg  style="width:24px;">                 | [Block](Sketcher_ConstrainBlock.md)                   |
| `'Block'`         |                                                                                            |                                                               |
|                         |                                                                                            |                                                               |
+----------------------------+--------------------------------------------------------------------------------------------+---------------------------------------------------------------+

The <img alt="" src=images/Sketcher_ConstrainInternalAlignment.svg  style="width:24px;"> [InternalAlignment](Sketcher_ConstrainInternalAlignment.md) constraints behave like geometric constraints for the purposes of scripting. Again, see the corresponding feature page for the possible combinations of arguments allowed for each constraint.

+-----------------------------------------------------+----------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+
| Code                                                | Icon                                                                                               | Feature                                                             |
+=====================================================+====================================================================================================+=====================================================================+
|                                      | <img alt="" src=images/Sketcher_ConstrainInternalAlignment.svg  style="width:24px;"> | [InternalAlignment](Sketcher_ConstrainInternalAlignment.md) |
| `'InternalAlignment:EllipseMajorDiameter'` |                                                                                                    |                                                                     |
|                                                  |                                                                                                    |                                                                     |
+-----------------------------------------------------+----------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+
|                                      | <img alt="" src=images/Sketcher_ConstrainInternalAlignment.svg  style="width:24px;"> | [InternalAlignment](Sketcher_ConstrainInternalAlignment.md) |
| `'InternalAlignment:EllipseMinorDiameter'` |                                                                                                    |                                                                     |
|                                                  |                                                                                                    |                                                                     |
+-----------------------------------------------------+----------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+
|                                      | <img alt="" src=images/Sketcher_ConstrainInternalAlignment.svg  style="width:24px;"> | [InternalAlignment](Sketcher_ConstrainInternalAlignment.md) |
| `'InternalAlignment:EllipseFocus1'`        |                                                                                                    |                                                                     |
|                                                  |                                                                                                    |                                                                     |
+-----------------------------------------------------+----------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+
|                                      | <img alt="" src=images/Sketcher_ConstrainInternalAlignment.svg  style="width:24px;"> | [InternalAlignment](Sketcher_ConstrainInternalAlignment.md) |
| `'InternalAlignment:EllipseFocus2'`        |                                                                                                    |                                                                     |
|                                                  |                                                                                                    |                                                                     |
+-----------------------------------------------------+----------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+

For dimensional constraints, the first argument is one of the following. See the corresponding feature page for the possible combinations of arguments allowed for each constraint.

+----------------------------+------------------------------------------------------------------------------------+---------------------------------------------------------------+
| Code                       | Icon                                                                               | Feature                                                       |
+============================+====================================================================================+===============================================================+
|             | <img alt="" src=images/Sketcher_ConstrainDistanceX.svg  style="width:24px;"> | [Horizontal distance](Sketcher_ConstrainDistanceX.md) |
| `'DistanceX'`     |                                                                                    |                                                               |
|                         |                                                                                    |                                                               |
+----------------------------+------------------------------------------------------------------------------------+---------------------------------------------------------------+
|             | <img alt="" src=images/Sketcher_ConstrainDistanceY.svg  style="width:24px;"> | [Vertical distance](Sketcher_ConstrainDistanceY.md)   |
| `'DistanceY'`     |                                                                                    |                                                               |
|                         |                                                                                    |                                                               |
+----------------------------+------------------------------------------------------------------------------------+---------------------------------------------------------------+
|             | <img alt="" src=images/Sketcher_ConstrainDistance.svg  style="width:24px;">   | [Distance](Sketcher_ConstrainDistance.md)             |
| `'Distance'`      |                                                                                    |                                                               |
|                         |                                                                                    |                                                               |
+----------------------------+------------------------------------------------------------------------------------+---------------------------------------------------------------+
|             | <img alt="" src=images/Sketcher_ConstrainRadius.svg  style="width:24px;">       | [Radius](Sketcher_ConstrainRadius.md)                 |
| `'Radius'`        |                                                                                    |                                                               |
|                         |                                                                                    |                                                               |
+----------------------------+------------------------------------------------------------------------------------+---------------------------------------------------------------+
|             | <img alt="" src=images/Sketcher_ConstrainDiameter.svg  style="width:24px;">   | [Diameter](Sketcher_ConstrainDiameter.md)             |
| `'Diameter'`      |                                                                                    |                                                               |
|                         |                                                                                    |                                                               |
+----------------------------+------------------------------------------------------------------------------------+---------------------------------------------------------------+
|             | <img alt="" src=images/Sketcher_ConstrainAngle.svg  style="width:24px;">         | [Angle](Sketcher_ConstrainAngle.md)                   |
| `'Angle'`         |                                                                                    |                                                               |
|                         |                                                                                    |                                                               |
+----------------------------+------------------------------------------------------------------------------------+---------------------------------------------------------------+
|             | <img alt="" src=images/Sketcher_ConstrainAngle.svg  style="width:24px;">         | [Angle](Sketcher_ConstrainAngle.md)                   |
| `'AngleViaPoint'` |                                                                                    |                                                               |
|                         |                                                                                    |                                                               |
+----------------------------+------------------------------------------------------------------------------------+---------------------------------------------------------------+

The <img alt="" src=images/Sketcher_ConstrainSnellsLaw.svg  style="width:24px;"> [Snell\'s law](Sketcher_ConstrainSnellsLaw.md) constraints behave like dimensional contraints for the purposes of scripting. Again, see the corresponding feature page for the possible combinations of arguments allowed for each constraint.

+------------------------+------------------------------------------------------------------------------------+--------------------------------------------------------+
| Code                   | Icon                                                                               | Feature                                                |
+========================+====================================================================================+========================================================+
|         | <img alt="" src=images/Sketcher_ConstrainSnellsLaw.svg  style="width:24px;"> | [Snell\'s law](Sketcher_ConstrainSnellsLaw.md) |
| `'SnellsLaw'` |                                                                                    |                                                        |
|                     |                                                                                    |                                                        |
+------------------------+------------------------------------------------------------------------------------+--------------------------------------------------------+

The <img alt="" src=images/Sketcher_ConstrainLock.svg  style="width:24px;"> [Lock](Sketcher_ConstrainLock.md) constraint is a GUI command which creates a <img alt="" src=images/Sketcher_ConstrainDistanceX.svg  style="width:24px;"> [Horizontal distance](Sketcher_ConstrainDistanceX.md) and a <img alt="" src=images/Sketcher_ConstrainDistanceY.svg  style="width:24px;"> [Vertical distance](Sketcher_ConstrainDistanceY.md) constraint, it is not a constraint of its own.

## Identifying the numbering of a line 

I have drawn three lines as shown in the following figure.

<img alt="" src=images/PartDesignConstraintPointOnPointScriptingFigure1.jpg  style="width:600px;">

By moving the cursor of the mouse above the line you can see the line number at the bottom left of the FreeCAD windows, see next figure.

<img alt="" src=images/PartDesignConstraintPointOnPointScriptingFigure2.jpg  style="width:600px;">

Unfortunately the numbering displayed on the FreeCAD windows start from 1 whereas the numbering of the line used to script start from 0: this means that you have to subtract one each time you want to refer to a line.

Positive numbers indicate sketch edges (straight lines, circles, conics, B-splines, and so on). The following values can be used to denote elements that are not sketch edges:

-    `-1`denotes the horizontal x axis

-    `-2`denotes the vertical y axis

-    `-n`denotes the external geometry element number `n-3` (e.g. the external geometry element with index 0 in the flattened list `App.ActiveDocument.Sketch.ExternalGeometry` would be denoted by -3, the following element in the flattened list would be -4 and so on).

## Identifying the numbering of the sub-parts of a line 

When qualifying which part of a line is affected by a constraint, the following values can be used:

-    `0`to indicate that the constraint affects the entire edge.

-    `1`to indicate that the constraint affects the starting point of the edge (a full circle has no starting point).

-    `2`to indicate that the constraint affects the end point of the edge.

-    `3`to indicate that the constraint affects the center point of the edge. For <img alt="" src=images/Sketcher_CompCreateCircle.png  style="width:24px;">[Circles](Sketcher_CompCreateCircle.md) and <img alt="" src=images/Sketcher_CompCreateConic.png  style="width:24px;">[Conics](Sketcher_CompCreateConic.md) (ellipses), this is the center of the circle or center (intersection of major and minor axes) of the ellipse. For straight <img alt="" src=images/Sketcher_CreateLine.svg  style="width:24px;">[Lines](Sketcher_CreateLine.md), `3` cannot be used to indicate the center point.

-    `n`to indicate that the constraint affects the n-th pole of a <img alt="" src=images/Sketcher_CompCreateBSpline.png  style="width:24px;">[B-Spline](Sketcher_CompCreateBSpline.md).

The vertices indicated by 1 and 2 are numbered according to their order of creation. To find out the order of their creation (If you have a lot of lines, you cannot remember which vertex you have created first), you just have to move the cursor of your mouse above the two vertices of one line, see following figure.

<img alt="" src=images/PartDesignConstraintPointOnPointScriptingFigure3.jpg  style="width:600px;">

If you read e.g. 4 and 5, it means that the vertex with the lower number (4 in this example) will be referenced by using the number 1 (first in the script command and the vertex with the higher number (5 in this example) will be referenced by using the number 2 in the script command.

## Example

Let us take the previous example of the three lines. The subsequent figure indicates the numbering of each line and their vertices according to the convention for scripting.

<img alt="" src=images/PartDesignConstraintPointOnPointScriptingFigure3Bis.jpg  style="width:600px;"> 
*<b>blue text:</b> numbering of line, <b>black text:</b> numbering of vertices*

The command `Sketch.addConstraint(Sketcher.Constraint('Coincident',1,2,2,1))` yields following result:

<img alt="" src=images/PartDesignConstraintPointOnPointScriptingFigure4.jpg  style="width:600px;">

The command `Sketch.addConstraint(Sketcher.Constraint('Coincident',0,2,2,2))` yields following result:

<img alt="" src=images/PartDesignConstraintPointOnPointScriptingFigure5.jpg  style="width:600px;">


{{Sketcher Tools navi

}}

---
[documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher scripting/en
