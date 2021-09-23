# <img alt="Ikonka FreeCAD dla Środowiska pracy Rysunek roboczy" src=images/Workbench_Draft.svg  style="width:64px;"> Draft Workbench/pl


{{TOCright}}

## Wprowadzenie

Środowisko pracy <img alt="" src=images/Workbench_Draft.svg  style="width:32px;"> **Rysunek Roboczy** skupia się przede wszystkim na tworzeniu i modyfikacji obiektów 2D w programie FreeCAD. Nie jest jednak ograniczone do płaszczyzny XY globalnego układu współrzędnych. Jego obiekty mogą mieć dowolną orientację i położenie w przestrzeni, a niektóre obiekty Rysunku Roboczego mogą być zarówno płaskie jak i przestrzenne.

Obiekty Rysunku Roboczego mogą być używane do ogólnego szkicowania, podobnie jak w programie Inkscape lub AutoCAD. Ale mogą one również stanowić podstawę do tworzenia obiektów 3D w innych środowiskach pracy. A [polilinia](Draft_Wire/pl.md) może zdefiniować ścieżkę dla [ściany](Arch_Wall/pl.md) środowiska Architektura, [wielokąt](Draft_Polygon/pl.md) środowiska Rysunek Roboczy może być wciągany za pomocą funkcji [wyciągnięcia](Part_Extrude/pl.md) środowiska Część, itd. Wiele z [narzędzi modyfikujących](#Modyfikacja.md) środowiska pracy Rysunek Roboczy może być zastosowanych do obiektów płaskich oraz przestrzennych stworzonych za pomocą innych środowisk pracy. Możesz, na przykład, [przesunąć](Draft_Move/pl.md) [szkic](Sketcher_Workbench/pl.md) lub stworzyć [szyk ortogonalny](Draft_OrthoArray/pl.md) z obiektu [Części](Part_Workbench/pl.md).

Środowisko pracy Rysunek Roboczy dostarcza również narzędzi do definiowania [płaszczyzny roboczej](Draft_SelectPlane/pl.md), [siatki](Draft_Snap_Grid/pl.md) oraz [systemu przyciągania](Draft_Snap/pl.md) do precyzyjnego sterowania położeniem geometrii.

Jeśli Twoim głównym celem jest tworzenie złożonych rysunków 2D i plików [DXF](DXF/pl.md), a nie potrzebujesz modelowania 3D, FreeCAD może nie być właściwym wyborem dla Ciebie. Możesz rozważyć zastosowanie dedykowanego programu do tworzenia projektów technicznych, takiego jak [LibreCAD](https://en.wikipedia.org/wiki/LibreCAD), [QCad](https://en.wikipedia.org/wiki/QCad), lub innego.

![](images/Draft_Workbench_Example.png ) *Obrazek przedstawia [siatkę](Draft_Grid/pl.md) wyrównaną do płaszczyzny XY.<br>
Po lewej stronie, na biało, kilka obiektów planarnych.<br>
Po prawej nieplanarny obiekt [polilinii](Draft_Wire/pl.md) użyty jako obiekt ścieżki w [wyciąganiu pop ścieżce](Draft_PathArray/pl.md).*

## Kreślenie

-   <img alt="" src=images/Draft_Line.svg  style="width:32px;"> [Line](Draft_Line.md): creates a straight line.

-   <img alt="" src=images/Draft_Wire.svg  style="width:32px;"> [Polyline](Draft_Wire.md): creates a polyline, a sequence of several connected line segments.

-   <img alt="" src=images/Draft_Fillet.svg  style="width:32px;"> [Fillet](Draft_Fillet.md): creates a fillet, a rounded corner, or a chamfer, a straight edge, between two [Draft Lines](Draft_Line.md). <small>(v0.19)</small> 

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

## Modyfikacja

-   <img alt="" src=images/Draft_Move.svg  style="width:32px;"> [Move](Draft_Move.md): moves or copies selected objects from one point to another.

-   <img alt="" src=images/Draft_Rotate.svg  style="width:32px;"> [Rotate](Draft_Rotate.md): rotates or copies selected objects around a center point by a given angle.

-   <img alt="" src=images/Draft_Scale.svg  style="width:32px;"> [Scale](Draft_Scale.md): scales or copies selected objects around a base point.

-   <img alt="" src=images/Draft_Mirror.svg  style="width:32px;"> [Mirror](Draft_Mirror.md): creates mirrored copies from selected objects.

-   <img alt="" src=images/Draft_Offset.svg  style="width:32px;"> [Offset](Draft_Offset.md): offsets each segment of a selected object over a given distance, or creates an offset copy of the selected object.

-   <img alt="" src=images/Draft_Trimex.svg  style="width:32px;"> [Trimex](Draft_Trimex.md): trims or extends a selected object.

-   <img alt="" src=images/Draft_Stretch.svg  style="width:32px;"> [Stretch](Draft_Stretch.md): stretches objects by moving selected points.

-   <img alt="" src=images/Draft_Clone.svg  style="width:32px;"> [Clone](Draft_Clone.md): creates linked copies, clones, of selected objects.

-   <img alt="" src=images/Draft_OrthoArray.svg  style="width:32px;"> Array tools

:\* <img alt="" src=images/Draft_OrthoArray.svg  style="width:32px;"> [Array](Draft_OrthoArray.md): creates an orthogonal array from a selected object. It can optionally create a [Link](App_Link.md) array. <small>(v0.19)</small> 

:\* <img alt="" src=images/Draft_PolarArray.svg  style="width:32px;"> [Polar array](Draft_PolarArray.md): creates an array from a selected object by placing copies along a circumference. It can optionally create a [Link](App_Link.md) array. <small>(v0.19)</small> 

:\* <img alt="" src=images/Draft_CircularArray.svg  style="width:32px;"> [Circular array](Draft_CircularArray.md): creates an array from a selected object by placing copies along concentric circumferences. It can optionally create a [Link](App_Link.md) array. <small>(v0.19)</small> 

:\* <img alt="" src=images/Draft_PathArray.svg  style="width:32px;"> [Path array](Draft_PathArray.md): creates an array from a selected object by placing copies along a path.

:\* <img alt="" src=images/Draft_PathLinkArray.svg  style="width:32px;"> [Path Link array](Draft_PathLinkArray.md): idem, but create a [Link](App_Link.md) array instead of a regular array. <small>(v0.19)</small> 

:\* <img alt="" src=images/Draft_PointArray.svg  style="width:32px;"> [Point Array](Draft_PointArray.md): creates an array from a selected object by placing copies at the points from a point compound.

:\* <img alt="" src=images/Draft_PointLinkArray.svg  style="width:32px;"> [Point Link array](Draft_PointLinkArray.md): idem, but create a [Link](App_Link.md) array instead of a regular array. <small>(v0.19)</small> 

-   <img alt="" src=images/Draft_Edit.svg  style="width:32px;"> [Edit](Draft_Edit.md): puts selected objects in Draft Edit mode. In this mode the properties of objects can be edited graphically.

-   <img alt="" src=images/Draft_SubelementHighlight.svg  style="width:32px;"> [Subelement highlight](Draft_SubelementHighlight.md): temporarily highlights selected objects, or the base objects of selected objects.

-   <img alt="" src=images/Draft_Join.svg  style="width:32px;"> [Join](Draft_Join.md): joins [Draft Lines](Draft_Line.md) and [Draft Wires](Draft_Wire.md) into a single wire.

-   <img alt="" src=images/Draft_Split.svg  style="width:32px;"> [Split](Draft_Split.md): splits a [Draft Line](Draft_Line.md) or [Draft Wire](Draft_Wire.md) at a specified point or edge.

-   <img alt="" src=images/Draft_Upgrade.svg  style="width:32px;"> [Upgrade](Draft_Upgrade.md): upgrades selected objects.

-   <img alt="" src=images/Draft_Downgrade.svg  style="width:32px;"> [Downgrade](Draft_Downgrade.md): downgrades selected objects.

-   <img alt="" src=images/Draft_WireToBSpline.svg  style="width:32px;"> [Wire to B-spline](Draft_WireToBSpline.md): converts [Draft Wires](Draft_Wire.md) to [Draft BSplines](Draft_BSpline.md) and vice versa.

-   <img alt="" src=images/Draft_Draft2Sketch.svg  style="width:32px;"> [Draft to Sketch](Draft_Draft2Sketch.md): converts [Draft](Draft_Workbench.md) objects to [Sketcher Sketches](Sketcher_NewSketch.md) and vice versa.

-   <img alt="" src=images/Draft_Slope.svg  style="width:32px;"> [Set slope](Draft_Slope.md): slopes selected [Draft Lines](Draft_Line.md) or [Draft Wires](Draft_Wire.md) by increasing, or decreasing, the Z coordinate of all points after the first one.

-   <img alt="" src=images/Draft_FlipDimension.svg  style="width:32px;"> [Flip dimension](Draft_FlipDimension.md): rotates the dimension text of selected [Draft Dimensions](Draft_Dimension.md) 180° around the dimension line.

-   <img alt="" src=images/Draft_Shape2DView.svg  style="width:32px;"> [Shape 2D view](Draft_Shape2DView.md): creates 2D projections from selected objects.

## Pasek narzędzi Draft: Tray 

Pasek narzędzi zasobnika środowiska [Rysunek Roboczy](Draft_Tray/pl.md) pojawia się po uruchomieniu stołu warsztatowego i umożliwia wybór płaszczyzny roboczej, wraz z niektórymi właściwościami wizualnymi, takimi jak kolor linii, kolor kształtu, szerokość linii, rozmiar tekstu oraz grupa automatyczna.

![](images/Draft_tray_default.png )

-   ![](images/Draft_tray_button_plane.png ) [Bieżąca płaszczyzna robocza](Draft_SelectPlane/pl.md): wybiera bieżącą płaszczyznę roboczą Rysunku Roboczego. Funkcja dostępna jest również w menu: **Narzędzia → <img src="images/Draft_SelectPlane.svg" width=16px> Wybierz płaszczyznę**.

-   ![](images/Draft_tray_button_style.png ) [Set style](Draft_SetStyle.md): sets the default style for new objects. Also available in the menu: **Draft → Utilities → <img src="images/Draft_SetStyle.svg" width=16px> Set style**. <small>(v0.19)</small> 

-   ![](images/Draft_tray_button_construction.png ) [Toggle construction mode](Draft_ToggleConstructionMode.md): switches Draft construction mode on or off. Also available in the menu: **Draft → Utilities → <img src="images/Draft_ToggleConstructionMode.svg" width=16px> Toggle construction mode**.

-   ![](images/Draft_tray_button_layer.png ) [AutoGroup](Draft_AutoGroup.md): changes the active [Draft Layer](Draft_Layer.md) or, optionally, the active [Std Group](Std_Group.md) or group-like [Arch](Arch_Workbench.md) object.

## Widżet skali adnotacji 

Za pomocą widżetu [skali anotacji](Draft_annotation_scale_widget/pl.md) można określić skalę adnotacji. Widżet ten znajduje się na [paseku statusu](Status_bar/pl.md).

![](images/Draft_annotation_scale_widget_button.png )

## Widżet przyciągania 

Widżet [przyciągania](Draft_snap_widget/pl.md) może być używany jako alternatywa dla [paska narzędzi przyciągania](#Pasek_narz.C4.99dzi_Rysunek_roboczy:_Przyci.C4.85gnij.md). {{Version/pl|0.19}}

![](images/Draft_snap_widget_button.png )

## Pasek narzędzi Rysunek roboczy: Przyciągnij 

Pasek narzędzi [Rysunek roboczy: Przyciągnij](Draft_Snap/pl.md) umożliwia wybranie bieżącego trybu przyciągania. Jego przycisk pozostaje wciśnięty, gdy tryb jest aktywny.

-   <img alt="" src=images/Draft_Snap_Lock.svg  style="width:32px;"> [Snap Lock](Draft_Snap_Lock.md): enables or disables snapping globally.

-   <img alt="" src=images/Draft_Snap_Endpoint.svg  style="width:32px;"> [Snap Endpoint](Draft_Snap_Endpoint.md): snaps to the endpoints of edges.

-   <img alt="" src=images/Draft_Snap_Midpoint.svg  style="width:32px;"> [Snap Midpoint](Draft_Snap_Midpoint.md): snaps to the midpoint of straight and circular edges.

-   <img alt="" src=images/Draft_Snap_Center.svg  style="width:32px;"> [Snap Center](Draft_Snap_Center.md): snaps to the center point of faces and circular edges, and to the **Placement** point of [Draft WorkingPlaneProxies](Draft_WorkingPlaneProxy.md) and [Arch BuildingParts](Arch_BuildingPart.md).

-   <img alt="" src=images/Draft_Snap_Angle.svg  style="width:32px;"> [Snap Angle](Draft_Snap_Angle.md): snaps to the special cardinal points on circular edges, at multiples of 30° and 45°.

-   <img alt="" src=images/Draft_Snap_Intersection.svg  style="width:32px;"> [Snap Intersection](Draft_Snap_Intersection.md): snaps to the intersection of two edges.

-   <img alt="" src=images/Draft_Snap_Perpendicular.svg  style="width:32px;"> [Snap Perpendicular](Draft_Snap_Perpendicular.md): snaps to the perpendicular point on edges.

-   <img alt="" src=images/Draft_Snap_Extension.svg  style="width:32px;"> [Snap Extension](Draft_Snap_Extension.md): snaps to an imaginary line that extends beyond the endpoints of straight edges.

-   <img alt="" src=images/Draft_Snap_Parallel.svg  style="width:32px;"> [Snap Parallel](Draft_Snap_Parallel.md): snaps to an imaginary line parallel to straight edges.

-   <img alt="" src=images/Draft_Snap_Special.svg  style="width:32px;"> [Snap Special](Draft_Snap_Special.md): snaps to special points defined by the object.

-   <img alt="" src=images/Draft_Snap_Near.svg  style="width:32px;"> [Snap Near](Draft_Snap_Near.md): snaps to the nearest point on faces or edges.

-   <img alt="" src=images/Draft_Snap_Ortho.svg  style="width:32px;"> [Snap Ortho](Draft_Snap_Ortho.md): snaps to imaginary lines that cross the previous point at 0°, 45°, 90° and 135°.

-   <img alt="" src=images/Draft_Snap_Grid.svg  style="width:32px;"> [Snap Grid](Draft_Snap_Grid.md): snaps to the intersections of grid lines.

-   <img alt="" src=images/Draft_Snap_WorkingPlane.svg  style="width:32px;"> [Snap WorkingPlane](Draft_Snap_WorkingPlane.md): projects the snap point onto the current [working plane](Draft_SelectPlane.md).

-   <img alt="" src=images/Draft_Snap_Dimensions.svg  style="width:32px;"> [Snap Dimensions](Draft_Snap_Dimensions.md): shows temporary X and Y dimensions.

-   <img alt="" src=images/Draft_ToggleGrid.svg  style="width:32px;"> [Toggle Grid](Draft_ToggleGrid.md): switches the grid on or off.

### Pasek narzędzi użytkowych 

-   <img alt="" src=images/Draft_Layer.svg  style="width:32px;"> [Layer](Draft_Layer.md): creates a [Draft Layer](Draft_Layer.md). <small>(v0.19)</small> 

-   <img alt="" src=images/Draft_WorkingPlaneProxy.svg  style="width:32px;"> [Create working plane proxy](Draft_WorkingPlaneProxy.md): creates a working plane proxy to save the current [Draft working plane](Draft_SelectPlane.md).

-   <img alt="" src=images/Draft_ToggleDisplayMode.svg  style="width:32px;"> [Toggle normal/wireframe display](Draft_ToggleDisplayMode.md): switches the **Display Mode** property of selected objects between {{Value|Flat Lines}} and {{Value|Wireframe}}.

-   <img alt="" src=images/Draft_AddToGroup.svg  style="width:32px;"> [Move to group\...](Draft_AddToGroup.md): moves objects to a [Std Group](Std_Group.md). It can also ungroup objects.

-   <img alt="" src=images/Draft_SelectGroup.svg  style="width:32px;"> [Select group](Draft_SelectGroup.md): selects the content of [Draft Layers](Draft_Layer.md), [Std Groups](Std_Group.md) or group-like [Arch](Arch_Workbench.md) objects.

-   <img alt="" src=images/Draft_AddConstruction.svg  style="width:32px;"> [Add to Construction group](Draft_AddConstruction.md): moves objects to the [Draft construction group](Draft_ToggleConstructionMode.md).

## Dodatkowe narzędzia 

Menu środowiska Rysunek Roboczy **Narzędzia** zawiera kilka narzędzi. Większość z nich jest dostępna również z pasków narzędziowych i została już wymieniona powyżej. W przypadku poniższych narzędzi nie jest to regułą.

-   <img alt="" src=images/Draft_Heal.svg  style="width:32px;"> [Heal](Draft_Heal.md): heals problematic Draft objects found in very old files.

-   <img alt="" src=images/Draft_ToggleContinueMode.svg  style="width:32px;"> [Toggle continue mode](Draft_ToggleContinueMode.md): switches continue mode on or off.

-   <img alt="" src=images/Draft_ApplyStyle.svg  style="width:32px;"> [Apply current style](Draft_ApplyStyle.md): applies the current style settings to selected objects.

-   <img alt="" src=images/Draft_ShowSnapBar.svg  style="width:32px;"> [Show snap toolbar](Draft_ShowSnapBar.md): shows the [Draft Snap toolbar](#Draft_Snap_toolbar.md).

## Dodatkowe właściwości 

-   [Płaszczyzna robocza](Draft_SelectPlane/pl.md): Umożliwia wybranie powierzchni w oknie [widoku 3D](3D_view.md), na której można budować swoje kształty.
-   [Przyciąganie](Draft_Snap/pl.md): Pozwala wybierać dokładne punkty geometryczne na, lub zdefiniowane przez, istniejące obiekty lub siatkę.
-   [Wiązania](Draft_Constrain/pl.md): Dla każdego kolejnego punktu można ograniczyć ruch kursora do kierunku X, Y lub Z.
-   [Tryb konstrukcji](Draft_ToggleConstructionMode/pl.md): Umieszcza nowe obiekty Rysunku Roboczego w dedykowanej grupie, ułatwiając ich ukrywanie lub usuwanie.
-   [Wzór](Draft_Pattern/pl.md): Obiekty Rysunku Roboczego z właściwością {{PropertyData/pl|Utwórz ścianę}} mogą wyświetlać wzór kreskowania zamiast jednolitego koloru ściany.

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

-   <img alt="" src=images/button_right.svg  style="width:32px;"> [Activate this layer](Draft_AutoGroup.md): activates the selected layer.

-   <img alt="" src=images/Draft_SelectGroup.svg  style="width:32px;"> [Select layer contents](Draft_SelectGroup.md): selects the objects inside the selected layer.

### Working plane proxy options 

For a [Draft WorkingPlaneProxy](Draft_WorkingPlaneProxy.md) these additional options are available:

-   <img alt="" src=images/Draft_SelectPlane.svg  style="width:32px;"> [Write camera position](Draft_WorkingPlaneProxy#Context_menu.md): updates the **View Data** property of the working plane proxy with the current [3D view](3D_view.md) camera settings.

-   <img alt="" src=images/Draft_SelectPlane.svg  style="width:32px;"> [Write objects state](Draft_WorkingPlaneProxy#Context_menu.md): updates the **Visibility Map** property of the working plane proxy with the current visibility state of objects in the document.

## 3D view context menu 

The following additional options are available in the [3D view](3D_view.md) context menu:

### No-selection options 

If there is no selection the context menu contains one additional sub-menu:

-    **Utilities**: a subset of the tools available in the main Draft Utilities menu.

### Selection options 

If there is a selection the context menu contains two additional sub-menus:

-    **Draft**: tools for [drawing objects](#Drafting.md) and [modifying objects](#Modification.md).

-    **Utilities**: a subset of the tools available in the main Draft Utilities menu.

## Narzędzia przestarzałe 

Polecenia te są przestarzałe, ale nadal dostępne.

-   <img alt="" src=images/Draft_Array.svg  style="width:32px;"> [Utwórz szyk](Draft_Array/pl.md): tworzy ortogonalną tablicę z wybranego obiektu. Utworzona tablica może zostać przekształcona w [szyk biegunowy](Draft_PolarArray/pl.md) lub [szyk kołowy](Draft_CircularArray/pl.md) poprzez zmianę jej właściwości {{PropertyData/pl|Array Type}}. {{Obsolete/pl|0.19}}

-   <img alt="" src=images/Draft_Drawing.svg  style="width:32px;"> [Projekt rysunku](Draft_Drawing/pl.md): wstawia widoki obiektów na stronie środowiska [Rysunek Roboczy](Drawing_Workbench/pl.md). {{Obsolete/pl|0.17}}

These [3D view](3D_view.md) context menu options are still available when the [Draft Wire](Draft_Wire.md), [Draft BSpline](Draft_BSpline.md), [Draft CubicBezCurve](Draft_CubicBezCurve.md) or [Draft BezCurve](Draft_BezCurve.md) command is active but will be removed in the near future:

-   <img alt="" src=images/Draft_UndoLine.svg  style="width:32px;"> [Cofnij kreślenie linii](Draft_UndoLine/pl.md): użyj przycisku {{button|<img src="images/Draft_UndoLine.svg" width=16px> Cofnij}} w panelu zadań polecenia. {{Obsolete/pl|0.20}}

-   <img alt="" src=images/Draft_FinishLine.svg  style="width:32px;"> [Zakończ linię](Draft_FinishLine/pl.md): użyj przycisku **<img src="images/Draft_FinishLine.svg" width=16px> Zakończ** w panelu zadań tego polecenia. {{Obsolete/pl|0.20}}

-   <img alt="" src=images/Draft_CloseLine.svg  style="width:32px;"> [Zamknij linię](Draft_CloseLine/pl.md): użyj przycisku **<img src="images/Draft_CloseLine.svg" width=16px> Zamknij** w panelu zadań tego polecenia. {{Obsolete/pl|0.20}}

## Ustawienia

-   <img alt="" src=images/Preferences-draft.svg  style="width:32px;"> [Ustawienia](Draft_Preferences/pl.md): ogólne ustawienia dla środowiska pracy Rysunek Roboczy.

-   <img alt="" src=images/Preferences-import-export.svg  style="width:32px;"> [Ustawienia Importu i Eksportu](Import_Export_Preferences/pl.md): Ustawienia dostępne dla importu i eksportu do różnych formatów plików.

### Formaty plików 

Środowisko pracy Rysunek Roboczy dostarcza programowi FreeCAD narzędzia do importu i eksportu dla kilku formatów plików. Są one używane przez polecenia [Import](Std_Import/pl.md) i [Eksport](Std_Export/pl.md).

-   [Autodesk .DXF](Draft_DXF/pl.md): Import i eksport plików [Drawing Exchange Format](http://en.wikipedia.org/wiki/AutoCAD_DXF) utworzonych za pomocą aplikacji 2D CAD. Zobacz również [FreeCAD i import DXF](FreeCAD_and_DXF_Import/pl.md).
-   [Autodesk .DWG](Draft_DXF/pl.md): Import i eksport plików DWG przez importer DXF, gdy jest zainstalowany [ODA Converter](Extra_python_modules#ODA_Converter_(previously_Teigha_Converter).md). Zobacz również [FreeCAD i import DWG](FreeCAD_and_DWG_Import/pl.md).
-   [Scalable Vector Graphics .SVG](Draft_SVG/pl.md): Import i eksport plików [Scalable Vector Graphics](http://en.wikipedia.org/wiki/Scalable_Vector_Graphics) utworzonych za pomocą aplikacji do rysowania wektorowego.
-   [Open Cad format .OCA](Draft_OCA/pl.md): Import i eksport plików [OCA/GCAD](http://groups.google.com/group/open_cad_format).
-   [Airfoil Data Format .DAT](Draft_DAT/pl.md): Import plików DAT opisujących profil Airfoil.

## Test jednostek 

Zobacz również: [Środowisko pracy Test](Testing/pl.md)

Aby przeprowadzić testy jednostek w środowisku pracy, należy wykonać następujące czynności z terminala systemu operacyjnego:


```python
freecad -t TestDraft
```

## Tworzenie skryptów 

Zobacz również stronę: [Dokumentacja API generowana automatycznie](https://freecad.github.io/SourceDoc/) oraz [Podstawy tworzenia skryptów FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Środowisko pracy zawiera moduł do tworzenia przykładów wszystkich obiektów w nowym dokumencie. {{Version/pl|0.19}}

Użyj tego, aby sprawdzić, czy wszystkie obiekty są prawidłowo utworzone:


```python
import drafttests.draft_test_objects as dto
doc = dto.create_test_file()
```

Sprawdzenie kodu tego modułu jest pomocne, aby zrozumieć interfejs programowania.

<img alt="" src=images/Draft_test_objects.png  style="width:500px;"> 
*Obiekty testowe dla środowiska pracy Rysunek Roboczy.*

## Poradniki

-   [Poradnik dla Środowiska pracy Draft](Draft_tutorial/pl.md)
-   [Draft ShapeString tutorial](Draft_ShapeString_tutorial.md)





 

[Category:Workbenches](Category:Workbenches.md)

---
[documentation index](../README.md) > Draft Workbench/pl
