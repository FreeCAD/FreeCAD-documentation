# <img alt="Sketcher workbench icon" src=images/Workbench_Sketcher.svg  style="width:64px;"> Sketcher Workbench/ja






## はじめに


<div class="mw-translate-fuzzy">

**スケッチャーワークベンチ**は**[パートデザインワークベンチ](PartDesign_Workbench/jp.md)**やその他のワークベンチで使用するための2次元形状を作成するために使われます。 ほとんどのCADモデルでは2次元形状が開始点となることが普通です・・まず簡単な2次元スケッチを\'押し出して\'3次元形状を作り、その形状の表面に穴を開けるための2次元スケッチを追加したり、スケッチで\'突起\'（押し出し形状）を定義したりします。 スケッチャーは[ブーリアン演算と並んで](Part_Module/jp.md)3次元形状デザイン作成の中核を成す機能なのです。


</div>


<div class="mw-translate-fuzzy">

スケッチャーワークベンチの特徴はなんといっても拘束です・・これによって2次元形状を厳密な幾何定義に従って拘束することが可能です。また拘束用ソルバーによって2次元形状の拘束範囲を計算したり、スケッチの自由度を対話的に検査したりすることが可能です。


</div>

<img alt="" src=images/FC_ConstrainedSketch.png  style="width:450px;"> 
*A fully constrained sketch*

## Basics of constraint sketching 


<div class="mw-translate-fuzzy">

## スケッチ拘束の基本

スケッチャーがどのように動作するか説明するには\"従来\"の製図方法と比較するとわかりやすいでしょう。


</div>

#### Traditional Drafting 


<div class="mw-translate-fuzzy">

#### 従来の製図

\"従来\"のCAD製図方法は過去の[製図板](http://en.wikipedia.org/wiki/Drawing_board)を用いた方法を受け継いでいます。[（2次元）正射影図](http://en.wikipedia.org/wiki/Multiview_orthographic_projection)を手書きすることで製図（いわゆる青写真）を作成します。物体は意図したサイズ、寸法に合わせて正確に描画されます。もし点(0, 0)から伸びる100mmの水平線を描きたければまずラインツールを選択し、画面をクリックするか座標(0, 0)と入力して始点を設定した後、終点をクリックするか座標を(100,0)を入力します。あるいは位置を気にせずに線を描き、後から位置を調整します。形状を描き終わったらそれらに寸法を追加します。


</div>

#### Constraint Sketching 


<div class="mw-translate-fuzzy">

#### 拘束スケッチ

**スケッチャー**の方法は全く異なります。物体を厳密に描く必要はありません。なぜなら物体は後で拘束をかけることによって定義されるからです。物体はおおまかに描けばよく、拘束をかける前であれば変更も可能です。実際の所、物体は\"流動的\"で動かしたり、伸ばしたり、回転させたり、拡大縮小させたりといったことが可能です。これによってデザイン作業がとても柔軟なものになります。


</div>

#### What are constraints? 


<div class="mw-translate-fuzzy">

#### 拘束とは何なのか？

拘束は物体の自由度を制限するために使用されます。例えばラインは拘束がない場合は4つの自由度を持ちます。つまり水平方向、垂直方向への移動と拡大縮小と回転が可能です。


</div>

水平拘束、垂直拘束、あるいは（他のラインか座標軸の一つに対する）角度拘束を適用すると回転が制限され自由度は3つに減ります。片方の短点を原点に対してロックすることでさらに2つの自由度が減ります。最後にサイズ拘束を適用すれば最後の自由度が無くなります。こうしてラインは**完全拘束**状態になります。


<div class="mw-translate-fuzzy">

複数のオブジェクトがある場合は相互に拘束が可能です。二本のラインがあった場合、点一致拘束を使用することでそれぞれの端点をつなぎ合わせることができます。また二本のラインの間の角度を設定したり、二本のラインが垂直になるよう設定することも可能です。ラインに対しては円弧や円の接線となるように拘束することもできます。


</div>


<div class="mw-translate-fuzzy">

拘束には二種類あります。幾何拘束と寸法拘束です。これらについては下の[\'ツール\'セクションで詳しく説明します](#The_tools.md)。


</div>

#### What the Sketcher is not good for 


<div class="mw-translate-fuzzy">

### スケッチャーに向かないもの

スケッチャーは2次元図面を作成するためのものではありません。ソリッド形状を作成するとスケッチは自動的に非表示になります。寸法はスケッチ編集モード時のみ表示されます。


</div>


<div class="mw-translate-fuzzy">

もし印刷用の2次元表示を作成するだけで3次元モデルが必要ないのであれば[製図ワークベンチをチェックしてください](Draft_Workbench/ja.md)（製図ワークベンチでも2次元形状が作れることを記憶に留めておいてください。今のところスケッチャーでは使用できない機能、例えばB-スプラインなどを使うこともできます）。


</div>

The tool [Draft2Sketch](Draft_Draft2Sketch.md) converts a Draft object to a Sketch object, and vice versa. Many tools that require a 2D element as input work with either type of object as an internal conversion is done automatically.

## Sketching Workflow 


<div class="mw-translate-fuzzy">

## Sketching Workflow 

スケッチは常に2次元（2D）です。 ソリッドを作成するには、囲まれた1つの領域の2Dスケッチを作成し、次にPaddedまたはRevolvedで3次元を追加して、2Dスケッチから3Dソリッドを作成します。


</div>


<div class="mw-translate-fuzzy">

スケッチが互いに交差する線分、Pointが線分上に直接ない場所、または隣接する線分の端点間にギャップがある場所では、PadまたはRevolveはソリッドを作成しません。 この規則の例外は、それがConstruction（blue）Geometryには適用されないことです。


</div>


<div class="mw-translate-fuzzy">

囲まれた領域の内側に、重ならない小さな領域を含めることができます。 3Dソリッドを作成すると、これらは無効になります。


</div>

Once a Sketch is fully constrained, the Sketch features will turn green; Construction Geometry will remain blue. It is usually \"finished\" at this point and suitable for use in creating a 3D solid. However, once the Sketch dialog is closed it may be worthwhile going to <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Part Workbench](Part_Workbench.md) and running **[<img src=images/Part_CheckGeometry.svg style="width:16px"> [Check geometry](Part_CheckGeometry.md)** to ensure there are no features in the Sketch which may cause later problems.

## Tools


<div class="mw-translate-fuzzy">

## ツール

スケッチャーワークベンチのツールはスケッチャーワークベンチをロードすると表示されるSketcherメニューに配置されています。


</div>


<small>(v0.21)</small> 

: If a sketch is in edit mode the Structure toolbar is hidden as none of its tools can then be used.

### General

#### Sketcher toolbar 

-   <img alt="" src=images/Sketcher_NewSketch.svg‎‎  style="width:32px;"> [Create sketch](Sketcher_NewSketch.md): Creates‎ a new sketch on a selected face or plane. If no face is selected while this tool is executed the user is prompted to select a plane from a pop-up window.

-   <img alt="" src=images/Sketcher_EditSketch.svg  style="width:32px;"> [Edit sketch](Sketcher_EditSketch.md): Edit the selected Sketch. This will open the [Sketcher Dialog](Sketcher_Dialog.md).

-   <img alt="" src=images/Sketcher_MapSketch.svg  style="width:32px;"> [Map sketch to face](Sketcher_MapSketch.md): Maps a sketch to the previously selected face of a solid.

-   <img alt="" src=images/Sketcher_ReorientSketch.svg  style="width:32px;"> [Reorient sketch](Sketcher_ReorientSketch.md): Allows you to attach the sketch to one of the main planes.

-   <img alt="" src=images/Sketcher_ValidateSketch.svg  style="width:32px;"> [Validate sketch](Sketcher_ValidateSketch.md): Verify the tolerance of different points and adjust them.

-   <img alt="" src=images/Sketcher_MergeSketches.svg  style="width:32px;"> [Merge sketches](Sketcher_MergeSketches.md): Merge two or more sketches.

-   <img alt="" src=images/Sketcher_MirrorSketch.svg  style="width:32px;"> [Mirror sketch](Sketcher_MirrorSketch.md): Mirror a sketch along the x-axis, the y-axis or the origin.

#### Sketcher Edit Mode toolbar 

-   <img alt="" src=images/Sketcher_LeaveSketch.svg  style="width:32px;"> [Leave sketch](Sketcher_LeaveSketch.md): Leave the Sketch editing mode.

-   <img alt="" src=images/Sketcher_ViewSketch.svg  style="width:32px;"> [View sketch](Sketcher_ViewSketch.md): Sets the model view perpendicular to the sketch plane.

-   <img alt="" src=images/Sketcher_ViewSection.svg  style="width:32px;"> [View section](Sketcher_ViewSection.md): Creates a section plane that temporarily hides any matter in front of the sketch plane.

#### Sketcher edit tools toolbar 

-   <img alt="" src=images/Sketcher_Grid.svg  style="width:32px;"> [Toggle grid](Sketcher_Grid.md): Toggles the grid in the sketch currently being edited. Settings can be changed in the related menu. <small>(v0.21)</small> 

-   <img alt="" src=images/Sketcher_Snap.svg  style="width:32px;"> [Toggle snap](Sketcher_Snap.md): Toggles snapping in all sketches. Settings can be changed in the related menu. <small>(v0.21)</small> 

-   <img alt="" src=images/Sketcher_RenderingOrder.svg  style="width:32px;"> [Configure rendering order](Sketcher_RenderingOrder.md): The rendering order of all sketches can be changed in the related menu. <small>(v0.21)</small> 

#### Other

-   <img alt="" src=images/Sketcher_StopOperation.svg  style="width:32px;"> [Stop operation](Sketcher_StopOperation.md): When in edit mode, stop the current operation, whether that is drawing, setting constraints, etc.

### Sketcher geometries 

These are tools for creating objects.

-   <img alt="" src=images/Sketcher_CreatePoint.svg  style="width:32px;"> [Point](Sketcher_CreatePoint.md): Draws a point.

-   <img alt="" src=images/Sketcher_CreateLine.svg  style="width:32px;"> [Line](Sketcher_CreateLine.md): Draws a line segment between 2 points. Lines are infinite regarding certain constraints.

-   <img alt="" src=images/Sketcher_CompCreateArc.png  style="width:48px;"> [Create arc](Sketcher_CompCreateArc.md): This is an icon menu in the Sketcher toolbar that holds the following commands:

  - <img alt="" src=images/Sketcher_CreateArc.svg  style="width:32px;"> [Arc](Sketcher_CreateArc.md): Draws an arc segment from center, radius, start angle and end angle.

  - <img alt="" src=images/Sketcher_Create3PointArc.svg  style="width:32px;"> [Arc by 3 points](Sketcher_Create3PointArc.md): Draws an arc segment from two endpoints and another point on the circumference.

-   <img alt="" src=images/Sketcher_CompCreateCircle.png  style="width:48px;"> [Create circle](Sketcher_CompCreateCircle.md): This is an icon menu in the Sketcher toolbar that holds the following commands:

  - <img alt="" src=images/Sketcher_CreateCircle.svg  style="width:32px;"> [Circle](Sketcher_CreateCircle.md): Draws a circle from center and radius.

  - <img alt="" src=images/Sketcher_Create3PointCircle.svg  style="width:32px;"> [Circle by 3 points](Sketcher_Create3PointCircle.md): Draws a circle from three points on the circumference.

-   <img alt="" src=images/Sketcher_CompCreateConic.png  style="width:48px;"> [Create conic](Sketcher_CompCreateConic.md): The sketcher provides the following conical sections. Unlike B-splines they can be used with all sorts of constraints such as [Tangent](Sketcher_ConstrainTangent.md), [Point On Object](Sketcher_ConstrainPointOnObject.md), or [Perpendicular](Sketcher_ConstrainPerpendicular.md).

  - <img alt="" src=images/Sketcher_CreateEllipseByCenter.svg  style="width:32px;"> [Ellipse by center](Sketcher_CreateEllipseByCenter.md): Draws an ellipse by center point, major radius point and minor radius point.

  - <img alt="" src=images/Sketcher_CreateEllipseBy3Points.svg  style="width:32px;"> [Ellipse by 3 points](Sketcher_CreateEllipseBy3Points.md): Draws an ellipse by major diameter (2 points) and minor radius point.

  - <img alt="" src=images/Sketcher_CreateArcOfEllipse.svg  style="width:32px;"> [Arc of ellipse](Sketcher_CreateArcOfEllipse.md): Draws an arc of ellipse by center point, major radius point, starting point and ending point.

  - <img alt="" src=images/Sketcher_CreateArcOfHyperbola.svg  style="width:32px;"> [Arc of hyperbola](Sketcher_CreateArcOfHyperbola.md): Draws an arc of hyperbola.

  - <img alt="" src=images/Sketcher_CreateArcOfParabola.svg  style="width:32px;"> [Arc of parabola](Sketcher_CreateArcOfParabola.md): Draws an arc of parabola.

-   <img alt="" src=images/Sketcher_CompCreateBSpline.png  style="width:48px;"> [Create B-spline](Sketcher_CompCreateBSpline.md): This is an icon menu in the Sketcher toolbar that holds the following commands:

  - <img alt="" src=images/Sketcher_CreateBSpline.svg  style="width:32px;"> [B-spline by control points](Sketcher_CreateBSpline.md): Draws a B-spline curve by its control points.

  - <img alt="" src=images/Sketcher_CreatePeriodicBSpline.svg  style="width:32px;"> [Periodic B-spline by control points](Sketcher_CreatePeriodicBSpline.md): Draws a periodic (closed) B-spline curve by its control points.

  - <img alt="" src=images/Sketcher_CreateBSplineByInterpolation.svg  style="width:32px;"> [B-spline by knots](Sketcher_CreateBSplineByInterpolation.md): Draws a B-spline curve by its knots. <small>(v0.21)</small> 

  - <img alt="" src=images/Sketcher_CreatePeriodicBSplineByInterpolation.svg  style="width:32px;"> [Periodic B-spline by knots](Sketcher_CreatePeriodicBSplineByInterpolation.md): Draws a periodic (closed) B-spline curve by its knots. <small>(v0.21)</small> 

-   <img alt="" src=images/Sketcher_CreatePolyline.svg  style="width:32px;"> [Polyline (multiple-point line)](Sketcher_CreatePolyline.md): Draws a line made of multiple line segments. Pressing the **M** key while drawing a Polyline toggles between the different polyline modes.

-   <img alt="" src=images/Sketcher_CompCreateRectangles.png  style="width:48px;"> [Create rectangle](Sketcher_CompCreateRectangles.md): This is an icon menu in the Sketcher toolbar that holds the following commands: <small>(v0.20)</small> 

  - <img alt="" src=images/Sketcher_CreateRectangle.svg  style="width:32px;"> [Rectangle](Sketcher_CreateRectangle.md): Draws a rectangle from 2 opposite points.

  - <img alt="" src=images/Sketcher_CreateRectangle_Center.svg  style="width:32px;"> [Centered rectangle](Sketcher_CreateRectangle_Center.md): Draws a rectangle from a central point and an edge point. <small>(v0.20)</small> 

  - <img alt="" src=images/Sketcher_CreateOblong.svg  style="width:32px;"> [Rounded rectangle](Sketcher_CreateOblong.md): Draws a rounded rectangle from 2 opposite points. <small>(v0.20)</small> 

-   <img alt="" src=images/Sketcher_CompCreateRegularPolygon.png  style="width:48px;"> [Create regular polygon](Sketcher_CompCreateRegularPolygon.md): This is an icon menu in the Sketcher toolbar that holds the following commands:

  - <img alt="" src=images/Sketcher_CreateTriangle.svg  style="width:32px;"> [Triangle](Sketcher_CreateTriangle.md): Draws a regular triangle inscribed in a construction geometry circle.

  - <img alt="" src=images/Sketcher_CreateSquare.svg  style="width:32px;"> [Square](Sketcher_CreateSquare.md): Draws a regular square inscribed in a construction geometry circle.

  - <img alt="" src=images/Sketcher_CreatePentagon.svg  style="width:32px;"> [Pentagon](Sketcher_CreatePentagon.md): Draws a regular pentagon inscribed in a construction geometry circle.

  - <img alt="" src=images/Sketcher_CreateHexagon.svg  style="width:32px;"> [Hexagon](Sketcher_CreateHexagon.md): Draws a regular hexagon inscribed in a construction geometry circle.

  - <img alt="" src=images/Sketcher_CreateHeptagon.svg  style="width:32px;"> [Heptagon](Sketcher_CreateHeptagon.md): Draws a regular heptagon inscribed in a construction geometry circle.

  - <img alt="" src=images/Sketcher_CreateOctagon.svg  style="width:32px;"> [Octagon](Sketcher_CreateOctagon.md): Draws a regular octagon inscribed in a construction geometry circle.

  - <img alt="" src=images/Sketcher_CreateRegularPolygon.svg  style="width:32px;"> [Regular polygon](Sketcher_CreateRegularPolygon.md) : Draws a regular polygon by selecting the number of sides and picking two points: the center and one corner.

-   <img alt="" src=images/Sketcher_CreateSlot.svg  style="width:32px;"> [Slot](Sketcher_CreateSlot.md): Draws an oval by selecting the center of one semicircle and an endpoint of the other semicircle.

-   <img alt="" src=images/Sketcher_CompCreateFillets.png  style="width:48px;"> [Create fillet](Sketcher_CompCreateFillets.md): This is an icon menu in the Sketcher toolbar that holds the following commands:

  - <img alt="" src=images/Sketcher_CreateFillet.svg  style="width:32px;"> [Fillet](Sketcher_CreateFillet.md): Creates a fillet between two non-parallel lines.

  - <img alt="" src=images/Sketcher_CreatePointFillet.svg  style="width:32px;"> [Corner-preserving fillet](Sketcher_CreatePointFillet.md): Creates a fillet between two non-parallel lines while preserving their (virtual) intersection.

-   <img alt="" src=images/Sketcher_Trimming.svg  style="width:32px;"> [Trim](Sketcher_Trimming.md): Trims a line, circle or arc with respect to the clicked point.

-   <img alt="" src=images/Sketcher_Extend.svg  style="width:32px;"> [Extend](Sketcher_Extend.md): Extends a line or an arc to a boundary line, arc, ellipse, arc of ellipse or a point in space.

-   <img alt="" src=images/Sketcher_Split.svg  style="width:32px;"> [Split](Sketcher_Split.md): Splits an edge into two while keeping most of the constraints. <small>(v0.20)</small> 

-   <img alt="" src=images/Sketcher_External.svg  style="width:32px;"> [External geometry](Sketcher_External.md): Creates an edge linked to external geometry.

-   <img alt="" src=images/Sketcher_CarbonCopy.svg  style="width:32px;"> [Carbon copy](Sketcher_CarbonCopy.md): Copies the geometry of another sketch.

-   <img alt="" src=images/Sketcher_ToggleConstruction.svg  style="width:32px;"> [Toggle construction geometry](Sketcher_ToggleConstruction.md): Toggles sketch geometry from/to construction mode. Construction geometry is shown in blue and is discarded outside of Sketch editing mode.

### Sketcher constraints 

Constraints are used to define lengths, set rules between sketch elements, and to lock the sketch along the vertical and horizontal axes. Some constraints require use of [Helper constraints](Sketcher_helper_constraint.md).

#### Geometric constraints 

These constraints are not associated with numeric data.

-   <img alt="" src=images/Sketcher_ConstrainCoincident.svg  style="width:32px;"> [Coincident](Sketcher_ConstrainCoincident.md): Affixes a point onto (coincident with) one or more other points. It acts as a concentric constraint if two or more circles, arcs, ellipses or arcs of ellipses are selected.

-   <img alt="" src=images/Sketcher_ConstrainPointOnObject.svg  style="width:32px;"> [Point on object](Sketcher_ConstrainPointOnObject.md): Affixes a point onto another object such as a line, arc, or axis.

-   <img alt="" src=images/Sketcher_ConstrainVertical.svg  style="width:32px;"> [Vertical](Sketcher_ConstrainVertical.md): Constrains the selected lines or polyline elements to a true vertical orientation. More than one object can be selected before applying this constraint.

-   <img alt="" src=images/Sketcher_ConstrainHorizontal.svg  style="width:32px;"> [Horizontal](Sketcher_ConstrainHorizontal.md): Constrains the selected lines or polyline elements to a true horizontal orientation. More than one object can be selected before applying this constraint.

-   <img alt="" src=images/Sketcher_ConstrainParallel.svg  style="width:32px;"> [Parallel](Sketcher_ConstrainParallel.md): Constrains two or more lines parallel to one another.

-   <img alt="" src=images/Sketcher_ConstrainPerpendicular.svg  style="width:32px;"> [Perpendicular](Sketcher_ConstrainPerpendicular.md): Constrains two lines perpendicular to one another, or constrains a line perpendicular to an arc endpoint.

-   <img alt="" src=images/Sketcher_ConstrainTangent.svg  style="width:32px;"> [Tangent](Sketcher_ConstrainTangent.md): Creates a tangent constraint between two selected entities, or a co-linear constraint between two line segments. A line segment does not have to lie directly on an arc or circle to be constrained tangent to that arc or circle.

-   <img alt="" src=images/Sketcher_ConstrainEqual.svg  style="width:32px;"> [Equal](Sketcher_ConstrainEqual.md): Constrains two selected entities equal to one another. If used on circles or arcs their radii will be set equal.

-   <img alt="" src=images/Sketcher_ConstrainSymmetric.svg  style="width:32px;"> [Symmetric](Sketcher_ConstrainSymmetric.md): Constrains two points symmetrically about a line, or constrains the first two selected points symmetrically about a third selected point.

-   <img alt="" src=images/Sketcher_ConstrainBlock.svg  style="width:32px;"> [Block](Sketcher_ConstrainBlock.md): it blocks an edge from moving, that is, it prevents its vertices from changing their current positions. It should be particularly useful to fix the position of B-Splines. See the [Block Constraint forum topic](https://forum.freecadweb.org/viewtopic.php?f=9&t=26572).

#### Dimensional constraints 

These are constraints associated with numeric data, for which you can use the [expressions](Expressions.md). The data may be taken from a [spreadsheet](Spreadsheet_Workbench.md).

-   <img alt="" src=images/Sketcher_ConstrainLock.svg  style="width:32px;"> [Lock](Sketcher_ConstrainLock.md): Constrains the selected item by setting vertical and horizontal distances relative to the origin, thereby locking the location of that item. These constraint distances can be edited later.

-   <img alt="" src=images/Sketcher_ConstrainDistanceX.svg  style="width:32px;"> [Horizontal distance](Sketcher_ConstrainDistanceX.md): Fixes the horizontal distance between two points or line endpoints. If only one item is selected, the distance is set to the origin.

-   <img alt="" src=images/Sketcher_ConstrainDistanceY.svg  style="width:32px;"> [Vertical distance](Sketcher_ConstrainDistanceY.md): Fixes the vertical distance between 2 points or line endpoints. If only one item is selected, the distance is set to the origin.

-   <img alt="" src=images/Sketcher_ConstrainDistance.svg  style="width:32px;"> [Distance](Sketcher_ConstrainDistance.md): Defines the length of a line, the perpendicular distance between a point and a line, the distance between two points, or, <small>(v0.21)</small> , the distance between the edges of two circles.

-   <img alt="" src=images/Sketcher_CompConstrainRadDia.png  style="width:48px;"> [Constrain radius or diameter](Sketcher_CompConstrainRadDia.md): This is an icon menu in the Sketcher constraints toolbar that holds the following commands:

  - <img alt="" src=images/Sketcher_ConstrainRadius.svg  style="width:32px;"> [Radius or weight](Sketcher_ConstrainRadius.md): Defines the radius of an arc or circle or the weight of a B-spline pole.

  - <img alt="" src=images/Sketcher_ConstrainDiameter.svg  style="width:32px;"> [Diameter](Sketcher_ConstrainDiameter.md): Defines the diameter of an arc or circle.

  - <img alt="" src=images/Sketcher_ConstrainRadiam.svg  style="width:32px;"> [Auto radius/diameter](Sketcher_ConstrainRadiam.md): Defines the radius of an arc, the diameter of a circle or the weight of a B-spline pole. <small>(v0.20)</small> 

-   <img alt="" src=images/Sketcher_ConstrainAngle.svg  style="width:32px;"> [Angle](Sketcher_ConstrainAngle.md): Defines the internal angle between two selected lines.

#### Special constraints 

-   <img alt="" src=images/Sketcher_ConstrainSnellsLaw.svg  style="width:32px;"> [Refraction (Snell\'s law)](Sketcher_ConstrainSnellsLaw.md): Constrains two lines to obey a refraction law to simulate the light going through an interface.

#### Constraint tools 

The following tools can be used the change the effect of constraints:

-   <img alt="" src=images/Sketcher_ToggleDrivingConstraint.svg  style="width:32px;"> [Toggle driving/reference constraint](Sketcher_ToggleDrivingConstraint.md): Toggles the toolbar or the selected constraints to/from reference mode.

-   <img alt="" src=images/Sketcher_ToggleActiveConstraint.svg  style="width:32px;"> [Activate/deactivate constraint](Sketcher_ToggleActiveConstraint.md): Enable or disable an already placed constraint.

### Sketcher tools 

-   <img alt="" src=images/Sketcher_SelectElementsWithDoFs.svg  style="width:32px;"> [Select unconstrained DoF](Sketcher_SelectElementsWithDoFs.md): Highlights in green the geometry with degrees of freedom (DOFs), i.e. not fully constrained.

-   <img alt="" src=images/Sketcher_SelectConstraints.svg  style="width:32px;"> [Select associated constraints](Sketcher_SelectConstraints.md): Selects the constraints of a sketcher element.

-   <img alt="" src=images/Sketcher_SelectElementsAssociatedWithConstraints.svg  style="width:32px;"> [Select associated geometry](Sketcher_SelectElementsAssociatedWithConstraints.md): Select sketcher elements associated with constraints.

-   <img alt="" src=images/Sketcher_SelectRedundantConstraints.svg  style="width:32px;"> [Select redundant constraints](Sketcher_SelectRedundantConstraints.md): Selects redundant constraints of a sketch.

-   <img alt="" src=images/Sketcher_SelectConflictingConstraints.svg  style="width:32px;"> [Select conflicting constraints](Sketcher_SelectConflictingConstraints.md): Selects conflicting constraints of a sketch.

-   <img alt="" src=images/Sketcher_RestoreInternalAlignmentGeometry.svg  style="width:32px;"> [Show/hide internal geometry](Sketcher_RestoreInternalAlignmentGeometry.md): Recreates missing/deletes unneeded internal geometry of a selected ellipse, arc of ellipse/hyperbola/parabola or B-spline.

-   <img alt="" src=images/Sketcher_SelectOrigin.svg  style="width:32px;"> [Select origin](Sketcher_SelectOrigin.md): Selects the origin of a sketch.

-   <img alt="" src=images/Sketcher_SelectHorizontalAxis.svg  style="width:32px;"> [Select horizontal axis](Sketcher_SelectHorizontalAxis.md): Selects the horizontal axis of a sketch.

-   <img alt="" src=images/Sketcher_SelectVerticalAxis.svg  style="width:32px;"> [Select vertical axis](Sketcher_SelectVerticalAxis.md): Selects the vertical axis of a sketch.

-   <img alt="" src=images/Sketcher_Symmetry.svg  style="width:32px;"> [Symmetry](Sketcher_Symmetry.md): Copies a sketcher element symmetrical to a chosen line.

-   <img alt="" src=images/Sketcher_Clone.svg  style="width:32px;"> [Clone](Sketcher_Clone.md): Clones a sketcher element.

-   <img alt="" src=images/Sketcher_Copy.svg  style="width:32px;"> [Copy](Sketcher_Copy.md): Copies a sketcher element.

-   <img alt="" src=images/Sketcher_Move.svg  style="width:32px;"> [Move](Sketcher_Move.md): Moves the selected geometry taking as reference the last selected point.

-   <img alt="" src=images/Sketcher_RectangularArray.svg  style="width:32px;"> [Rectangular array](Sketcher_RectangularArray.md): Creates an array of selected sketcher elements.

-   <img alt="" src=images/Sketcher_RemoveAxesAlignment.svg  style="width:32px;"> [Remove axes alignment](Sketcher_RemoveAxesAlignment.md): Remove axes alignment while trying to preserve the constraint relationship of the selection. <small>(v0.20)</small> 

-   <img alt="" src=images/Sketcher_DeleteAllGeometry.svg  style="width:32px;"> [Delete all geometry](Sketcher_DeleteAllGeometry.md): Deletes all geometry from the sketch.

-   <img alt="" src=images/Sketcher_DeleteAllConstraints.svg  style="width:32px;"> [Delete all constraints](Sketcher_DeleteAllConstraints.md): Deletes all constraints from the sketch.

### Sketcher B-spline tools 

-   <img alt="" src=images/Sketcher_BSplineDegree.svg  style="width:32px;"> [Show/hide B-spline degree](Sketcher_BSplineDegree.md): Shows or hides the display of the degree of a B-spline.

-   <img alt="" src=images/Sketcher_BSplinePolygon.svg  style="width:32px;"> [Show/hide B-spline control polygon](Sketcher_BSplinePolygon.md): Shows or hides the display of the defining polygon of a B-spline.

-   <img alt="" src=images/Sketcher_BSplineComb.svg  style="width:32px;"> [Show/hide B-spline curvature comb](Sketcher_BSplineComb.md): Shows or hides the display of the curvature comb of a B-spline.

-   <img alt="" src=images/Sketcher_BSplineKnotMultiplicity.svg  style="width:32px;"> [Show/hide B-spline knot multiplicity](Sketcher_BSplineKnotMultiplicity.md): Shows or hides the display of the knot multiplicity of a B-spline.

-   <img alt="" src=images/Sketcher_BSplinePoleWeight.svg  style="width:32px;"> [Show/hide B-spline control point weight](Sketcher_BSplinePoleWeight.md): Shows or hides the display of the weights for the control points of a B-spline.

-   <img alt="" src=images/Sketcher_BSplineApproximate.svg  style="width:32px;"> [Convert geometry to B-spline](Sketcher_BSplineApproximate.md): Converts compatible geometry, edges and curves, into a B-spline.

-   <img alt="" src=images/Sketcher_BSplineIncreaseDegree.svg  style="width:32px;"> [Increase B-spline degree](Sketcher_BSplineIncreaseDegree.md): Increases the degree (order) of a B-spline.

-   <img alt="" src=images/Sketcher_BSplineDecreaseDegree.svg  style="width:32px;"> [Decrease B-spline degree](Sketcher_BSplineDecreaseDegree.md): Decreases the degree (order) of a B-spline.

-   <img alt="" src=images/Sketcher_BSplineIncreaseKnotMultiplicity.svg  style="width:32px;"> [Increase knot multiplicity](Sketcher_BSplineIncreaseKnotMultiplicity.md): Increases the multiplicity of a B-spline knot.

-   <img alt="" src=images/Sketcher_BSplineDecreaseKnotMultiplicity.svg  style="width:32px;"> [Decrease knot multiplicity](Sketcher_BSplineDecreaseKnotMultiplicity.md): Decreases the multiplicity of a B-spline knot.

-   <img alt="" src=images/Sketcher_BSplineInsertKnot.svg  style="width:32px;"> [Insert knot](Sketcher_BSplineInsertKnot.md): Inserts a knot into an existing B-spline. <small>(v0.20)</small> 

-   <img alt="" src=images/Sketcher_JoinCurves.svg  style="width:32px;"> [Join curves](Sketcher_JoinCurves.md): Joins two curves at selected end points. <small>(v0.21)</small> 

### Sketcher virtual space 

-   <img alt="" src=images/Sketcher_SwitchVirtualSpace.svg  style="width:32px;"> [Switch virtual space](Sketcher_SwitchVirtualSpace.md): Allows you to hide all constraints of a sketch and make them visible again.

### Obsolete tools 

-   <img alt="" src=images/Sketcher_CloseShape.svg  style="width:32px;"> [Close shape](Sketcher_CloseShape.md): Creates a closed shape by applying coincident constraints to endpoints. Not available in <small>(v0.21)</small> .

-   <img alt="" src=images/Sketcher_ConnectLines.svg  style="width:32px;"> [Connect edges](Sketcher_ConnectLines.md): Connect sketcher elements by applying coincident constraints to endpoints. Not available in <small>(v0.21)</small> .

## Preferences

-   <img alt="" src=images/Workbench_Sketcher.svg  style="width:32px;"> [Preferences](Sketcher_Preferences.md): Preferences for the **Sketcher** workbench.

## Best Practices 

Every CAD user develops his own way of working over time, but there are some useful general principles to follow.

-   A series of simple sketches is easier to manage than a single complex one. For example, a first sketch can be created for the base 3D feature (either a pad or a revolve), while a second one can contain holes or cutouts (pockets). Some details can be left out, to be realized later on as 3D features. You can choose to avoid fillets in your sketch if there are too many, and add them as a 3D feature.
-   Always create a closed profile, or your sketch won\'t produce a solid, but rather a set of open faces. If you don\'t want some of the objects to be included in the solid creation, turn them to construction elements with the Construction Mode tool.
-   Use the auto constraints feature to limit the number of constraints you\'ll have to add manually.
-   As a general rule, apply geometric constraints first, then dimensional constraints, and lock your sketch last. But remember: rules are made to be broken. If you\'re having trouble manipulating your sketch, it may be useful to constrain a few objects first before completing your profile.
-   If possible, center your sketch to the origin (0,0) with the lock constraint. If your sketch is not symmetric, locate one of its points to the origin, or choose nice round numbers for the lock distances.
-   If you have the possibility to choose between the Length constraint and the Horizontal or Vertical Distance constraints, prefer the latter. Horizontal and Vertical Distance constraints are computationally cheaper.
-   In general, the best constraints to use are: Horizontal and Vertical Constraints; Horizontal and Vertical Length Constraints; Point-to-Point Tangency. If possible, limit the use of these: the general Length Constraint; Edge-to-Edge Tangency; Fix Point Onto a Line Constraint; Symmetry Constraint.
-   If in doubt about the validity of a sketch once it is complete (features turn green), close the Sketcher dialog, switch to the <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Part Workbench](Part_Workbench.md) and run **[<img src=images/Part_CheckGeometry.svg style="width:16px"> [Check geometry](Part_CheckGeometry.md)**.




<div class="mw-translate-fuzzy">

## チュートリアル


</div>

-   [Sketcher tutorial](https://forum.freecadweb.org/viewtopic.php?f=36&t=30104) by chrisb. This is a 70-page long PDF document that serves as a detailed manual for the sketcher. It explains the basics of Sketcher usage, and goes into a lot of detail about the creation of geometrical shapes, and each of the constraints.
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
⏵ [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > Sketcher Workbench/ja
