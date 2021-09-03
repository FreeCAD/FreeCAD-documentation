


 

<img alt="Draft workbench icon" src=images/Workbench_Draft.svg  style="width:128px;">


{{TOCright}}

## Introduction

製図ワークベンチを使うと現在のドキュメントにシンプルな2Dオブジェクトを手軽に描くことができます。また描いた後でそれらを変更するためのツールもいくつか用意されています。ツールの一部は製図ワークベンチで作成したものだけでなく他のFreeCADオブジェクト全てに対して使用することができます。また完璧に動作するスナップシステムやオブジェクトと設定を管理するためのいくつかのユーティリティも提供されています。

The created 2D objects can be used for general drafting in a way similar as is done with Inkscape or Autocad. These 2D shapes can also be used as the base components of 3D objects created with other workbenches, for example, the <img alt="" src=images/Workbench_Part.svg  style="width:32px;"> [Part](Part_Workbench.md) and <img alt="" src=images/Workbench_Arch.svg  style="width:32px;"> [Arch Workbenches](Arch_Workbench.md). Conversion of Draft objects to <img alt="" src=images/Workbench_Sketcher.svg  style="width:32px;"> [Sketches](Sketcher_Workbench.md) is also possible, which means that the shapes can also be used with the <img alt="" src=images/Workbench_PartDesign.svg  style="width:32px;"> [PartDesign Workbench](PartDesign_Workbench.md) for the creation of solid bodies.

FreeCAD is primarily a 3D modelling application, and thus its 2D tools aren\'t as advanced as in other drawing programs. If your primary goal is the production of complex 2D drawings and [DXF](DXF.md) files, and you don\'t need 3D modelling, you may wish to consider a dedicated software program for technical drafting such as [LibreCAD](https://en.wikipedia.org/wiki/LibreCAD), [QCad](https://en.wikipedia.org/wiki/QCad), or others.

<img alt="Draft Workbench Example" src=images/Draft_Workbench_Example.png  style="width:400px;">

### 作図オブジェクト

オブジェクトを作成するためのツールです。

-   <img alt="" src=images/Draft_Line.png  style="width:32px;"> [2点線分](Draft_Line.md): 2点からなる線分を描きます
-   <img alt="" src=images/Draft_Wire.png  style="width:32px;"> [ワイヤー（複数の点からなる線分）](Draft_Wire.md): 複数点の線分で作られる線を描きます
-   <img alt="" src=images/Draft_Circle.png  style="width:32px;"> [円](Draft_Circle.md): 中心と半径から円を描きます
-   <img alt="" src=images/Draft_Arc.png  style="width:32px;"> [円弧](Draft_Arc.md): 中心、半径、開始角度と終了角度から円弧を描きます
-   <img alt="" src=images/Draft_Ellipse.png  style="width:32px;"> [Ellipse](Draft_Ellipse.md): Draws an ellipse from two corner points
-   <img alt="" src=images/Draft_Polygon.png  style="width:32px;"> [多角形](Draft_Polygon.md): 中心、半径、辺数から正多角形を描く
-   <img alt="" src=images/Draft_Rectangle.png  style="width:32px;"> [四角形](Draft_Rectangle.md): ２つの対点から四角形を描きます
-   <img alt="" src=images/Draft_Text.png  style="width:32px;"> [テキスト](Draft_Text.md): 複数行のテキストの注釈を描きます
-   <img alt="" src=images/Draft_Dimension.png  style="width:32px;"> [寸法](Draft_Dimension.md): 寸法の注釈を描きます
-   <img alt="" src=images/Draft_BSpline.png  style="width:32px;"> [B-スプライン](Draft_BSpline.md): 点列からB-スプラインを描きます
-   <img alt="" src=images/Draft_Point.png  style="width:32px;"> [点](Draft_Point.md): 点オブジェクトを挿入します
-   <img alt="" src=images/Draft_ShapeString.png  style="width:32px;"> [ShapeString](Draft_ShapeString.md): The ShapeString tool inserts a compound shape representing a text string at a given point in the current document
-   <img alt="" src=images/Draft_Facebinder.png  style="width:32px;"> [Facebinder](Draft_Facebinder.md): Creates a new object from selected faces on existing objects
-   <img alt="" src=images/Draft_BezCurve.png  style="width:32px;"> [Bezier Curve](Draft_BezCurve.md): Draws a Bezier curve from a series of points
-   <img alt="" src=images/Draft_Label.png  style="width:32px;"> [Label](Draft_Label.md): Places a label with an arrow pointing to a selected element <small>(v0.17)</small> 

## Annotation objects 

-   <img alt="" src=images/Draft_Text.svg  style="width:32px;"> [Text](Draft_Text.md): draws a multi-line text annotation.
-   <img alt="" src=images/Draft_Dimension.svg  style="width:32px;"> [Dimension](Draft_Dimension.md): draws a dimension annotation.
-   <img alt="" src=images/Draft_Label.svg  style="width:32px;"> [Label](Draft_Label.md): places a label with an arrow pointing to a selected element.
-   <img alt="" src=images/Draft_AnnotationStyleEditor.svg  style="width:32px;"> [Annotation style editor](Draft_AnnotationStyleEditor.md): opens an editor to change the annotation style of these objects. <small>(v0.19)</small> 

### オブジェクトの変更

既存のオブジェクトを変更するためのツールです。これらのツールは選択したオブジェクトに対して動作します。もしオブジェクトを選択していない場合にはオブジェクトを選択するように促します。

Many operation tools (move, rotate, array, etc.) also work on solid objects ([Part](Part_Workbench.md), [PartDesign](PartDesign_Workbench.md), [Arch](Arch_Workbench.md), etc.).

-   <img alt="" src=images/Draft_Move.png  style="width:32px;"> [移動](Draft_Move.md): オブジェクト（複数可）をある位置から別の位置へ移動します
-   <img alt="" src=images/Draft_Rotate.png  style="width:32px;"> [回転](Draft_Rotate.md): 開始角から終了角へのオブジェクト（複数可）を回転します
-   <img alt="" src=images/Draft_Offset.png  style="width:32px;"> [オフセット](Draft_Offset.md): オブジェクトの線分を一定の距離だけ移動します
-   <img alt="" src=images/Draft_Trimex.png  style="width:32px;"> [トリム/延長](Draft_Trimex.md): オブジェクトをトリムまたは延長します
-   <img alt="" src=images/Draft_Upgrade.png  style="width:32px;"> [アップグレード](Draft_Upgrade.md): オブジェクトを結合し、1階層上のオブジェクトにします
-   <img alt="" src=images/Draft_Downgrade.png  style="width:32px;"> [ダウングレード](Draft_Downgrade.md): オブジェクトを解体し、1階層下のオブジェクトにします
-   <img alt="" src=images/Draft_Scale.png  style="width:32px;"> [スケール](Draft_Scale.md): 選択したオブジェクト（複数可）を基点を中心にスケールします
-   <img alt="" src=images/Draft_Edit.png  style="width:32px;"> [編集](Draft_Edit.md): 選択したオブジェクトを編集します
-   <img alt="" src=images/Draft_WireToBSpline.png  style="width:32px;"> [ワイヤーからB-スプラインへ](Draft_WireToBSpline.md): ワイヤーからB-スプラインへの変換、またその逆変換を行います
-   <img alt="" src=images/Draft_AddPoint.png  style="width:32px;"> [点の追加](Draft_AddPoint.md): ワイヤーまたはB-スプラインへ点を追加します
-   <img alt="" src=images/Draft_DelPoint.png  style="width:32px;"> [点の削除](Draft_DelPoint.md): ワイヤーまたはB-スプラインから点を削除します
-   <img alt="" src=images/Draft_Shape2DView.png  style="width:32px;"> [2Dビュー成形](Draft_Shape2DView.md): 別の3Dオブジェクトの平面化2Dビューであるような2Dオブジェクトを作成します
-   <img alt="" src=images/Draft_Draft2Sketch.png  style="width:32px;"> [ドラフトからスケッチへ](Draft_Draft2Sketch.md): ラフトオブジェクトを[Sketcher Workbenchスケッチに変換します](Sketcher_Workbench.md)。
-   <img alt="" src=images/Draft_Array.png  style="width:32px;"> [配列](Draft_Array.md): 選択されたオブジェクトを円形または矩形に並べた配列を作成します
-   <img alt="" src=images/Draft_PathArray.png  style="width:32px;"> [Path Array](Draft_PathArray.md): Creates an array of objects by placing the copies along a path
-   <img alt="" src=images/Draft_PointArray.svg  style="width:32px;"> [Point Array](Draft_PointArray.md): Creates an array of objects by placing the copies at certain points <small>(v0.18)</small> 
-   <img alt="" src=images/Draft_Clone.png  style="width:32px;"> [複製](Draft_Clone.md): 選択されたオブジェクトを複製します
-   <img alt="" src=images/Draft_PutOnSheet.png  style="width:32px;"> [Drawing](Draft_Drawing.md): Writes selected objects to a [Drawing Workbench](Drawing_Workbench.md) page
-   <img alt="" src=images/Draft_Mirror.png  style="width:32px;"> [Mirror](Draft_Mirror.md): Mirrors the selected objects
-   <img alt="" src=images/Draft_Stretch.png  style="width:32px;"> [Stretch](Draft_Stretch.md): Stretches the selected objects {{Version/jp|0.17}}

-   <img alt="" src=images/Draft_Clone.svg  style="width:32px;"> [Clone](Draft_Clone.md): clones the selected objects.
-   <img alt="" src=images/Draft_Array.svg  style="width:32px;"> Array tools.
    -   <img alt="" src=images/Draft_OrthoArray.svg  style="width:32px;"> [Ortho Array](Draft_OrthoArray.md): creates an orthogonal array from the selected object. It can also create [App Link](App_Link.md) copies. <small>(v0.19)</small> 
    -   <img alt="" src=images/Draft_PolarArray.svg  style="width:32px;"> [Polar Array](Draft_PolarArray.md): creates an array in a polar pattern, that is, sweeping an angle. It can also create [App Link](App_Link.md) copies. <small>(v0.19)</small> 
    -   <img alt="" src=images/Draft_CircularArray.svg  style="width:32px;"> [Circular Array](Draft_CircularArray.md): creates an array in a circular pattern, that is, starting from a center and moving outwards radially. It can also create [App Link](App_Link.md) copies. <small>(v0.19)</small> 
    -   <img alt="" src=images/Draft_PathArray.svg  style="width:32px;"> [Path Array](Draft_PathArray.md): creates an array of objects by placing the copies along a path.
    -   <img alt="" src=images/Draft_PathLinkArray.svg  style="width:32px;"> [Path LinkArray](Draft_PathLinkArray.md): like <img alt="" src=images/Draft_PathArray.svg  style="width:32px;"> [Path Array](Draft_PathArray.md), but creates [App Links](App_Link.md) instead of regular copies. <small>(v0.19)</small> 
    -   <img alt="" src=images/Draft_PointArray.svg  style="width:32px;"> [Point Array](Draft_PointArray.md): creates an array of objects by placing the copies at certain points.
    -   <img alt="" src=images/Draft_PointLinkArray.svg  style="width:32px;"> [Point LinkArray](Draft_PointLinkArray.md): like <img alt="" src=images/Draft_PointArray.svg  style="width:32px;"> [Point Array](Draft_PointArray.md), but creates [App Links](App_Link.md) instead of regular copies. <small>(v0.19)</small> 

-   <img alt="" src=images/Draft_Edit.svg  style="width:32px;"> [Edit](Draft_Edit.md): edits a selected object.
-   <img alt="" src=images/Draft_SubelementHighlight.svg  style="width:32px;"> [Subelement highlight](Draft_SubelementHighlight.md): enters an edit mode that allows editing different objects. <small>(v0.19)</small> 

-   <img alt="" src=images/Draft_Join.svg  style="width:32px;"> [Join](Draft_Join.md): joins lines together into a single wire.
-   <img alt="" src=images/Draft_Split.svg  style="width:32px;"> [Split](Draft_Split.md): splits a wire into two at a point.
-   <img alt="" src=images/Draft_Upgrade.svg  style="width:32px;"> [Upgrade](Draft_Upgrade.md): upgrades objects into a higher-level object.
-   <img alt="" src=images/Draft_Downgrade.svg  style="width:32px;"> [Downgrade](Draft_Downgrade.md): downgrades objects into lower-level objects.

-   <img alt="" src=images/Draft_WireToBSpline.svg  style="width:32px;"> [Wire to BSpline](Draft_WireToBSpline.md): converts a wire to a B-Spline and vice-versa.
-   <img alt="" src=images/Draft_Draft2Sketch.svg  style="width:32px;"> [Draft to Sketch](Draft_Draft2Sketch.md): converts a Draft object to a [Sketcher Workbench](Sketcher_Workbench.md) Sketch and vice-versa.
-   <img alt="" src=images/Draft_Slope.svg  style="width:32px;"> [Slope](Draft_Slope.md): changes the elevation slope of the currently selected [Draft Line](Draft_Line.md) or [Draft Wire](Draft_Wire.md).
-   <img alt="" src=images/Draft_FlipDimension.svg  style="width:32px;"> [Flip Dimension](Draft_FlipDimension.md): flips the orientation of the text of a [Draft Dimension](Draft_Dimension.md).

-   <img alt="" src=images/Draft_Shape2DView.svg  style="width:32px;"> [Shape 2D View](Draft_Shape2DView.md): creates a 2D object which is a flattened 2D view of a 3D object.

## Draft Tray 

The [Draft Tray](Draft_Tray.md) allows selecting the working plane, defining style settings, toggling construction mode, and specifying the active layer or group.

![](images/Draft_tray_default.png )

Its tools are also available in the **Draft → Utilities** menu:

-   <img alt="" src=images/Draft_SelectPlane.svg  style="width:32px;"> [Select Plane](Draft_SelectPlane.md): selects the current Draft working plane.

-   <img alt="" src=images/Draft_SetStyle.svg  style="width:32px;"> [Set style](Draft_SetStyle.md): sets the default style for new objects. <small>(v0.19)</small> 

-   <img alt="" src=images/Draft_ToggleConstructionMode.svg  style="width:32px;"> [Toggle construction mode](Draft_ToggleConstructionMode.md): switches Draft construction mode on or off.

-   <img alt="" src=images/Draft_AutoGroup.svg  style="width:32px;"> [AutoGroup](Draft_AutoGroup.md): changes the active [Draft Layer](Draft_Layer.md) or, optionally, the active [Std Group](Std_Group.md) or group-like [Arch](Arch_Workbench.md) object.

## Draft annotation scale widget 

With the [Draft annotation scale widget](Draft_annotation_scale_widget.md) the Draft annotation scale can be specified. <small>(v0.19)</small> 

![](images/Draft_annotation_scale_widget_button.png )

## Draft snap widget 

The [Draft snap widget](Draft_snap_widget.md) can be used as an alternative for the [Draft Snap toolbar](#Draft_snap_toolbar.md). <small>(v0.19)</small> 

![](images/Draft_snap_widget_button.png )

## Draft Snap toolbar 

The Draft Snap toolbar allows selecting the active snap options. The buttons belonging to active options stay depressed. For general information about snapping see: [Draft Snap](Draft_Snap.md).

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

### ユーティリティーツール

-   <img alt="" src=images/Draft_Layer.svg  style="width:32px;"> [Layer](Draft_Layer.md): creates a Layer in the current document, to which objects can be added to control object visibility and color. It replaces Draft VisGroup. <small>(v0.19)</small> 
-   <img alt="" src=images/Draft_WorkingPlaneProxy.svg  style="width:32px;"> [Working Plane Proxy](Draft_WorkingPlaneProxy.md): create a proxy object to store the current [Working Plane](Draft_SelectPlane.md) position.
-   <img alt="" src=images/Draft_ToggleDisplayMode.svg  style="width:32px;"> [Toggle display mode](Draft_ToggleDisplayMode.md): switches the display mode of selected objects between \"Flat Lines\" and \"Wireframe\".
-   <img alt="" src=images/Draft_AddToGroup.svg  style="width:32px;"> [Add to group](Draft_AddToGroup.md): quickly adds selected objects to an existing [Std Group](Std_Group.md).
-   <img alt="" src=images/Draft_SelectGroup.svg  style="width:32px;"> [Select group contents](Draft_SelectGroup.md): selects the contents of a selected [Std Group](Std_Group.md) or [Draft Layer](Draft_Layer.md).
-   <img alt="" src=images/Draft_AddConstruction.svg  style="width:32px;"> [Add to Construction group](Draft_AddConstruction.md): add selected objects to the Construction group.
-   <img alt="" src=images/Draft_Heal.svg  style="width:32px;"> [Heal](Draft_Heal.md): heals problematic Draft objects found in very old files.

## Additional tools 

右クリックのコンテキストメニューから利用可能な追加ツールです。選択されているオブジェクトに依存して変わります。

-   <img alt="" src=images/Draft_SelectPlane.png  style="width:32px;"> [作業平面の設定](Draft_SelectPlane/jp.md): 標準ビューまたは選択された面から作業平面を設定します
-   <img alt="" src=images/Draft_FinishLine.png  style="width:32px;"> [ラインを終了](Draft_FinishLine/jp.md): ワイヤー、B-スプラインの描画をラインが閉じないで終了します
-   <img alt="" src=images/Draft_CloseLine.png  style="width:32px;"> [ラインを閉じる](Draft_CloseLine/jp.md): ワイヤー、B-スプラインの描画をラインを閉じて終了します
-   <img alt="" src=images/Draft_UndoLine.png  style="width:32px;"> [ラインをアンドゥ](Draft_UndoLine/jp.md): ラインの最後の区間をアンドゥします
-   <img alt="" src=images/Draft_ToggleConstructionMode.png  style="width:32px;"> [作成モードの切り替え](Draft_ToggleConstructionMode/jp.md): ドラフト作成モードのオン/オフを切り替えます
-   <img alt="" src=images/Draft_ToggleContinueMode.png  style="width:32px;"> [継続モードの切り替え](Draft_ToggleContinueMode/jp.md): ドラフト継続モードのオン/オフを切り替えます
-   <img alt="" src=images/Draft_ApplyStyle.png  style="width:32px;"> [スタイルを適用](Draft_Apply/jp.md): 選択されたオブジェクトに現在のスタイルと色を適用します
-   <img alt="" src=images/Draft_ToggleDisplayMode.png  style="width:32px;"> [表示モードの切り替え](Draft_ToggleDisplayMode/jp.md): 選択されたオブジェクトの表示モードを\"フラットライン\"または\"ワイヤーフレーム\"に切り替えます
-   <img alt="" src=images/Draft_AddToGroup.png  style="width:32px;"> [グループに追加](Draft_AddToGroup/jp.md): ただちに選択されたオブジェクトを既存のグループに追加します
-   <img alt="" src=images/Draft_SelectGroup.png  style="width:32px;"> [グループの中身を選択](Draft_SelectGroup/jp.md): 選択されたグループの中身を選択します
-   <img alt="" src=images/Draft_ToggleSnap.png  style="width:32px;"> [スナップの切り替え](Draft_ToggleSnap/jp.md): [オブジェクトのスナップのオン](Draft_Snap/jp.md)/オフを切り替えます
-   <img alt="" src=images/Draft_ToggleGrid.png  style="width:32px;"> [グリッドの切り替え](Draft_ToggleGrid/jp.md): グリッドのオン/オフを切り替えます
-   <img alt="" src=images/Draft_ShowSnapBar.png  style="width:32px;"> [スナップバーを表示](Draft_ShowSnapBar/jp.md): [スナップツールバーの表示](Draft_Snap/jp.md)/非表示を切り替えます
-   <img alt="" src=images/Draft_Heal.png  style="width:32px;"> [Heal](Draft_Heal.md): Heals problematic Draft objects found in very old files
-   <img alt="" src=images/Draft_FlipDimension.png  style="width:32px;"> [Flip Dimension](Draft_FlipDimension.md): Flips the orientation of the text of a [dimension](Draft_Dimension.md)
-   <img alt="" src=images/Draft_VisGroup.png  style="width:32px;"> [VisGroup](Draft_VisGroup.md): Creates a VisGroup in the current document
-   <img alt="" src=images/Draft_Slope.png  style="width:32px;"> [Slope](Draft_Slope.md): Changes the slope of selected Lines or Wires {{Version/jp|0.17}}
-   <img alt="" src=images/Draft_AutoGroup.png  style="width:32px;"> [AutoGroup](Draft_AutoGroup.md): Automatically place new objects in a given group {{Version/jp|0.17}}
-   <img alt="" src=images/Draft_SetWorkingPlaneProxy.png  style="width:32px;"> [Set Working Plane Proxy](Draft_SetWorkingPlaneProxy.md): Add a proxy object in the document to store a [Working Plane](Draft_SelectPlane.md) position {{Version/jp|0.17}}
-   <img alt="" src=images/Draft_ToggleConstructionMode.png  style="width:32px;"> [Add to Construction group](Draft_AddConstruction.md): Add selected objects to the Construction group <small>(v0.17)</small> 

### 追加機能

-   [スナッピング](Draft_Snap/jp.md): 既存オブジェクトの特定位置に新しい点を配置できます
-   [拘束](Draft_Constrain/jp.md): 既存の点に対して相対的な水平位置、垂直位置を指定して新しい点を配置できます
-   [座標入力での作業](Draft_Coordinates/jp.md): 画面クリックの代わりに手動で座標を入力できます
-   [Working plane](Draft_SelectPlane.md): Allows you to define a plane in the 3D space, where next operations will take place

## Tree view context menu 

The following additional options are available in the [Tree view](Tree_view.md) context menu:

### Selection options 

If there is a selection the context menu contains one additional sub-menu:

-    **Utilities**: a subset of the tools available in the main Draft Utilities menu.

### Wire options 

For a [Draft Wire](Draft_Wire.md), [Draft BSpline](Draft_BSpline.md), [Draft CubicBezCurve](Draft_CubicBezCurve.md) and [Draft BezCurve](Draft_BezCurve.md) this additional option is available:

-   <img alt="" src=images/Draft_Edit.svg  style="width:32px;"> Flatten this wire: flattens the wire based on its internal geometry. This option currently does not work properly.

### Layer container options 

For a [Draft LayerContainer](Draft_Layer.md) these additional options are available:

-   <img alt="" src=images/Draft_Layer.svg  style="width:32px;"> Merge layer duplicates: this option currently does not work.

-   <img alt="" src=images/Draft_NewLayer.svg  style="width:32px;"> [Add new layer](Draft_Layer.md): adds a new layer to the current document.

### Layer options 

For a [Draft Layer](Draft_Layer.md) these additional options are available:

-   <img alt="" src=images/button_right.svg  style="width:32px;"> [Activate this layer](Draft_AutoGroup.md): makes the selected layer the active layer.

-   <img alt="" src=images/Draft_SelectGroup.svg  style="width:32px;"> [Select layer contents](Draft_SelectGroup.md): selects the objects inside the selected layer.

### Working plane proxy options 

For a [Draft WorkingPlaneProxy](Draft_WorkingPlaneProxy.md) these additional options are available:

-   <img alt="" src=images/Draft_SelectPlane.svg  style="width:32px;"> [Write camera position](Draft_WorkingPlaneProxy#Tree_view_context_menu.md): updates the camera settings stored in the working plane proxy.

-   <img alt="" src=images/Draft_SelectPlane.svg  style="width:32px;"> [Write objects state](Draft_WorkingPlaneProxy#Tree_view_context_menu.md): updates the visibility state of objects stored in the working plane proxy.

## 3D view context menu 

The following additional options are available in the [3D view](3D_view.md) context menu:

### No-selection options 

If there is no selection the context menu contains one additional sub-menu:

-    **Utilities**: a subset of the tools available in the main Draft Utilities menu.

### Selection options 

If there is a selection the context menu contains two additional sub-menus:

-    **Draft**: tools for [drawing objects](#Drawing_objects.md) and [modifying objects](#Modifying_objects.md).

-    **Utilities**: a subset of the tools available in the main Draft Utilities menu.

## Obsolete tools 

These commands are obsolete but still available:

-   <img alt="" src=images/Draft_Array.svg  style="width:32px;"> [Array](Draft_Array.md): creates a polar or rectangular array from selected objects. {{Obsolete|0.19}}

-   <img alt="" src=images/Draft_Drawing.svg  style="width:32px;"> [Drawing](Draft_Drawing.md): writes selected objects to a [Drawing Workbench](Drawing_Workbench.md) page. {{Obsolete|0.17}}

These [3D view](3D_view.md) context menu options are still available when the [Draft Wire](Draft_Wire.md), [Draft BSpline](Draft_BSpline.md), [Draft CubicBezCurve](Draft_CubicBezCurve.md) or [Draft BezCurve](Draft_BezCurve.md) command is active but will be removed in the near future:

-   <img alt="" src=images/Draft_UndoLine.svg  style="width:32px;"> [Undo last segment](Draft_Wire#Options.md): use the {{button|<img src="images/Draft_UndoLine.svg" width=16px> Undo}} button in the task panel of the command instead. {{Obsolete|0.20}}

-   <img alt="" src=images/Draft_FinishLine.svg  style="width:32px;"> [Finish line](Draft_Wire#Options.md): use the **<img src="images/Draft_FinishLine.svg" width=16px> Finish** button in the task panel of the command instead. {{Obsolete|0.20}}

-   <img alt="" src=images/Draft_CloseLine.svg  style="width:32px;"> [Close line](Draft_Wire#Options.md): use the **<img src="images/Draft_CloseLine.svg" width=16px> Close** button in the task panel of the command instead. {{Obsolete|0.20}}

### 環境設定

-   製図モジュールには専用の[環境設定ドラフトワークベンチで利用可能な設定](Draft_Preferences.md)。

### ファイル形式

製図モジュールによってFreeCADは以下のファイル形式をインポート、エクスポートできるようになっています。

-   [Autodesk .DXF](Draft_DXF.md): 2D-CADアプリケーションを使って作成された[Drawing Exchange Format](http://en.wikipedia.org/wiki/AutoCAD_DXF)ファイルのインポートとエクスポート
-   [SVG（形状）](Draft_SVG.md): ベクター描画アプリケーションを使って作成された[Scalable Vector Graphics](http://en.wikipedia.org/wiki/Scalable_Vector_Graphics)ファイルのインポートとエクスポート
-   [Open Cad format .OCA](Draft_OCA.md): OCA/GCADファイルのインポートとエクスポート。将来的な可能性を秘めた新しい [オープンなCADファイル形式](http://groups.google.com/group/open_cad_format)です
-   [Airfoil Data Format .DAT](Draft_DAT.md): [翼型断面](http://www.ae.illinois.edu/m-selig/ads/coord_database.html)の記述に使用されるDATファイルのインポート
-   [Autodesk .DWG](Draft_DXF.md): Import and exports DWG files via the DXF importer, when the [ODA Converter](Extra_python_modules#ODA_Converter_(previously_Teigha_Converter).md) utility is installed.
-   [FreeCAD and DWG Import](FreeCAD_and_DWG_Import.md): Import and exports DWG files
-   [FreeCAD and DXF Import](FreeCAD_and_DXF_Import.md): Import and exports DXF files

### Install importers 

-   [FreeCAD and DWG Import](FreeCAD_and_DWG_Import.md): Imports and exports DWG files
-   [FreeCAD and DXF Import](FreeCAD_and_DXF_Import.md): Imports and exports DXF files

## Unit tests 


**See also:**

[Test Workbench](Test_Workbench.md).

To run the unit tests of the workbench execute the following from the operating system terminal. 
```python
freecad -t TestDraft
```

### スクリプト処理

製図モジュール機能には完全な[製図用APIがあり](Draft_API/jp.md)、スクリプトやマクロからその機能を使用することができます

The workbench includes a module to create samples of all objects in a new document. <small>(v0.19)</small> 

Use this to test that all objects are produced correctly. 
```python
import drafttests.draft_test_objects as dto
doc = dto.create_test_file()
```

Inspecting the code of this module is useful to understand how to use the programming interface. 
```python
$INSTALLDIR/Mod/Draft/drafttests/draft_test_objects.py
```

Where `$INSTALLDIR` is the toplevel directory where the software was installed; for example, in Linux it may be `/usr/share/freecad`.

<img alt="" src=images/Draft_test_objects.png  style="width:500px;"> 
*Test objects for the [Draft Workbench](Draft_Workbench.md).*

## Tutorials

-   [Draft tutorial](Draft_tutorial.md)
-   [Draft ShapeString tutorial](Draft_ShapeString_tutorial.md)





 

[Category:Workbenches{{\#translation:}}](Category:Workbenches.md)
