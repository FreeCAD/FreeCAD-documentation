# <img alt="Ícone da bancada de trabalho de draft" src=images/Workbench_Draft.svg  style="width:64px;"> Draft Workbench/pt-br


{{TOCright}}

## Introdução


<div class="mw-translate-fuzzy">

A <img alt="" src=images/Workbench_Draft.svg  style="width:32px;"> [bancada de trabalho Draft](Draft_Workbench/pt-br.md) permite desenhar objetos 2D simples, e oferece várias ferramentas para modificá-los posteriormente. Ele também fornece ferramentas para definir um plano de trabalho, uma grade e um sistema de disparo para controlar com precisão a posição de sua geometria.


</div>


<div class="mw-translate-fuzzy">

Os objetos 2D criados podem ser usados para esboço geral de uma forma semelhante à do Inkscape ou do Autocad. Estas formas 2D também podem ser usadas como componentes base de objetos 3D criados com outras bancadas de trabalho, por exemplo, a <img alt="" src=images/Workbench_Part.svg  style="width:32px;"> [bancada de trabalho Part](Part_Workbench/pt-br.md) e [Arch](Arch_Workbench/pt-br.md). A conversão de objetos de Draft para <img alt="" src=images/Workbench_Sketcher.svg  style="width:32px;"> [Sketches](Sketcher_Workbench/pt-br.md) também é possível, o que significa que as formas também podem ser usadas com a <img alt="" src=images/Workbench_PartDesign.svg  style="width:32px;"> [bancada de trabalho PartDesign](PartDesign_Workbench/pt-br.md) para a criação de corpos sólidos.


</div>

The Draft Workbench also provides tools to define a [working plane](Draft_SelectPlane.md), a [grid](Draft_Snap_Grid.md), and a [snapping system](Draft_Snap.md) to precisely control the position of geometry.


<div class="mw-translate-fuzzy">

O FreeCAD é principalmente uma aplicação de modelagem 3D, e assim suas ferramentas 2D não são tão avançadas como em outros programas de desenho. Se seu objetivo principal é a produção de desenhos 2D complexos e arquivos [DXF](DXF/pt-br.md), e você não precisa de modelagem 3D, talvez você queira considerar um programa de software dedicado ao desenho técnico, como o [LibreCAD](https://en.wikipedia.org/wiki/LibreCAD), [QCad](https://en.wikipedia.org/wiki/QCad), ou outros.


</div>

![](images/Draft_Workbench_Example.png ) 
*The image shows the [grid](Draft_Snap_Grid.md) aligned with the XY plane.<br>
On the left, in white, several planar objects.<br>
On the right a non-planar [Draft Wire](Draft_Wire.md) used as the Path Object of a [Draft PathArray](Draft_PathArray.md).*

## Drafting

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

-   <img alt="" src=images/Draft_Hatch.svg  style="width:32px;"> [Hatch](Draft_Hatch.md): creates hatches on the planar faces of a selected object. <small>(v0.20)</small> 

## Annotation

-   <img alt="" src=images/Draft_Text.svg  style="width:32px;"> [Text](Draft_Text.md): creates a multi-line text at a given point.

-   <img alt="" src=images/Draft_Dimension.svg  style="width:32px;"> [Dimension](Draft_Dimension.md): creates a linear dimension, a radial dimension or an angular dimension.

-   <img alt="" src=images/Draft_Label.svg  style="width:32px;"> [Label](Draft_Label.md): creates a multi-line text with a 2-segment leader line and an arrow.

-   <img alt="" src=images/Draft_AnnotationStyleEditor.svg  style="width:32px;"> [Annotation styles\...](Draft_AnnotationStyleEditor.md): allows you to define styles that affect the visual properties of annotation-like objects. <small>(v0.19)</small> 

## Modification

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

## Barra de ferramentas da bandeja de rascunho 

A barra de ferramentas [Bandeja de rascunho](Draft_Tray/pt-br.md) aparece quando a bancada de trabalho é iniciada, e permite selecionar o plano de trabalho, com algumas propriedades visuais como a cor da linha, cor da forma, largura da linha, tamanho do texto e grupo automático.

![](images/Draft_tray_default.png )


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Draft_SelectPlane.svg  style="width:32px;"> [Plano de trabalho](Draft_SelectPlane/pt-br.md): define um plano de trabalho a partir de uma vista padrão ou de uma face selecionada.
-   <img alt="" src=images/Draft_SetStyle.svg  style="width:32px;"> [Estilo de conjunto](Draft_SetStyle/pt-br.md): define o estilo padrão para novos objetos, e opcionalmente aplica o estilo a objetos e grupos selecionados.
-   <img alt="" src=images/Draft_ToggleConstructionMode.svg  style="width:32px;">[Modo de construção](Draft_ToggleConstructionMode/pt-br.md): ativa ou desativa o modo de construção de rascunho.
-   <img alt="" src=images/Draft_AutoGroup.svg  style="width:32px;"> [Grupo automático](Draft_AutoGroup/pt-br.md): colocar automaticamente novos objetos em um determinado <img alt="" src=images/Std_Group.svg  style="width:32px;">[Grupo padrão](Std_Group/pt-br.md), <img alt="" src=images/Draft_Layer.svg  style="width:32px;">[Camada](Draft_Layer/pt-br.md), ou um dos objetos de grupo do [Bancada de trabalho Arch](Arch_Workbench/pt-br.md), como <img alt="" src=images/Arch_BuildingPart.svg  style="width:32px;">. [Parte de um edifício](Arch_BuildingPart/pt-br.md). <small>(v0.17)</small> 


</div>

-   ![](images/Draft_tray_button_style.png ) [Set style](Draft_SetStyle.md): sets the default style for new objects. Also available in the menu: **Draft → Utilities → <img src="images/Draft_SetStyle.svg" width=16px> Set style**. <small>(v0.19)</small> 

-   ![](images/Draft_tray_button_construction.png ) [Toggle construction mode](Draft_ToggleConstructionMode.md): switches Draft construction mode on or off. Also available in the menu: **Draft → Utilities → <img src="images/Draft_ToggleConstructionMode.svg" width=16px> Toggle construction mode**.

-   ![](images/Draft_tray_button_layer.png ) [AutoGroup](Draft_AutoGroup.md): changes the active [Draft Layer](Draft_Layer.md) or, optionally, the active [Std Group](Std_Group.md) or group-like [Arch](Arch_Workbench.md) object.

## Draft annotation scale widget 

Com o [Widget de escala de anotação](Draft_annotation_scale_widget/pt-br.md) a escala de anotação Draft pode ser especificada. O widget está localizado na [Barra de status](Status_bar/pt-br.md).

![](images/Draft_annotation_scale_widget_button.png )

## Draft snap widget 


<div class="mw-translate-fuzzy">

O [Widget de ancoragem](Draft_snap_widget/pt-br.md) pode ser usado como uma alternativa para a [Barra de ferramentas Rascunho de pressão](#Barra_de_ferramentas_Rascunho_de_pressão.md). O widget está localizado na [Barra de status](Status_bar/pt-br.md).


</div>

![](images/Draft_snap_widget_button.png )

## Barra de ferramentas Rascunho de pressão 

A barra de ferramentas [Captura](Draft_Snap/pt-br.md) permite selecionar o modo de precisão atual. Seu botão se mantém pressionado quando um modo está ativo.

-   <img alt="" src=images/Draft_Snap_Lock.svg  style="width:32px;"> [Snap Lock](Draft_Snap_Lock.md): enables or disables snapping globally.

-   <img alt="" src=images/Draft_Snap_Endpoint.svg  style="width:32px;"> [Snap Endpoint](Draft_Snap_Endpoint.md): snaps to the endpoints of edges.

-   <img alt="" src=images/Draft_Snap_Midpoint.svg  style="width:32px;"> [Snap Midpoint](Draft_Snap_Midpoint.md): snaps to the midpoint of edges.

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

## Draft utility tools toolbar 

-   <img alt="" src=images/Draft_Layer.svg  style="width:32px;"> [Layer](Draft_Layer.md): creates a [Draft Layer](Draft_Layer.md). <small>(v0.19)</small> 

-   <img alt="" src=images/Draft_AddNamedGroup.svg  style="width:32px;"> [Add a new named group](Draft_AddNamedGroup.md): creates a named [Std Group](Std_Group.md) and moves selected objects to that group. <small>(v0.20)</small> 

-   <img alt="" src=images/Draft_AddToGroup.svg  style="width:32px;"> [Move to group\...](Draft_AddToGroup.md): moves objects to a [Std Group](Std_Group.md). It can also ungroup objects.

-   <img alt="" src=images/Draft_SelectGroup.svg  style="width:32px;"> [Select group](Draft_SelectGroup.md): selects the contents of [Std Groups](Std_Group.md) or group-like [Arch](Arch_Workbench.md) objects.

-   <img alt="" src=images/Draft_AddConstruction.svg  style="width:32px;"> [Add to Construction group](Draft_AddConstruction.md): moves objects to the [Draft construction group](Draft_ToggleConstructionMode.md).

-   <img alt="" src=images/Draft_ToggleDisplayMode.svg  style="width:32px;"> [Toggle normal/wireframe display](Draft_ToggleDisplayMode.md): switches the **Display Mode** property of selected objects between {{Value|Flat Lines}} and {{Value|Wireframe}}.

-   <img alt="" src=images/Draft_WorkingPlaneProxy.svg  style="width:32px;"> [Create working plane proxy](Draft_WorkingPlaneProxy.md): creates a working plane proxy to save the current [Draft working plane](Draft_SelectPlane.md).

## Ferramentas adicionais 

The **Draft → Utilities** menu contains several tools. Most of them can also be accessed from toolbars or the [Draft Tray](Draft_Tray.md) and have already been mentioned above. For the following tools this is not the case:

-   <img alt="" src=images/Draft_ApplyStyle.svg  style="width:32px;"> [Apply current style](Draft_ApplyStyle.md): applies the current style settings to selected objects.

-   <img alt="" src=images/Draft_Heal.svg  style="width:32px;"> [Heal](Draft_Heal.md): heals problematic Draft objects found in very old files.

-   <img alt="" src=images/Draft_ToggleContinueMode.svg  style="width:32px;"> [Toggle continue mode](Draft_ToggleContinueMode.md): switches continue mode on or off.

-   <img alt="" src=images/Draft_ShowSnapBar.svg  style="width:32px;"> [Show snap toolbar](Draft_ShowSnapBar.md): shows the [Draft Snap toolbar](#Draft_Snap_toolbar.md).

## Características adicionais 


<div class="mw-translate-fuzzy">

-   [Restrições](Draft_Constrain/pt-br.md): limitar o ponteiro a movimentos horizontais ou verticais em relação a um ponto anterior.
-   [Captura](Draft_Snap/pt-br.md): colocar novos pontos em lugares especiais sobre objetos existentes ou sobre a grade.
-   [Modo de construção](Draft_ToggleConstructionMode/pt-br.md): Permite criar geometrias separadas das demais, simplesmente ligando e desligando-as.
-   [Plano de trabalho](Draft_SelectPlane/pt-br.md): permite selecionar uma superfície sobre a qual você pode construir suas formas.


</div>

## Tree view context menu 

The following additional options are available in the [Tree view](Tree_view.md) context menu:

### Default options 

If there is an active document the context menu contains one additional sub-menu:

-    **Utilities**: a subset of the tools available in the main Draft Utilities menu.

### Wire options 

For a [Draft Wire](Draft_Wire.md), [Draft BSpline](Draft_BSpline.md), [Draft CubicBezCurve](Draft_CubicBezCurve.md) and [Draft BezCurve](Draft_BezCurve.md) this additional option is available:

-   <img alt="" src=images/Draft_Edit.svg  style="width:32px;"> Flatten this wire: flattens the wire based on its internal geometry. This option currently does not work properly.

### Layer container options 

For a [Draft LayerContainer](Draft_Layer.md) these additional options are available:

-   <img alt="" src=images/Draft_Layer.svg  style="width:32px;"> [Merge layer duplicates](Draft_Layer#Layer_container_options.md): merges all layers with the same base label. This does not work in FreeCAD version 0.19.

-   <img alt="" src=images/Draft_NewLayer.svg  style="width:32px;"> [Add new layer](Draft_Layer#Layer_container_options.md): adds a new layer to the current document.

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

### Default options 

If there is an active document the context menu contains one additional sub-menu:

-    **Utilities**: a subset of the tools available in the main Draft Utilities menu.

## Ferramentas obsoletas 

Estes comandos são obsoletos, mas ainda estão disponíveis.

-   <img alt="" src=images/Draft_Array.svg  style="width:32px;"> [Array](Draft_Array.md): creates an orthogonal array from a selected object. The created array can be turned into a [polar array](Draft_PolarArray.md) or a [circular array](Draft_CircularArray.md) by changing its **Array Type** property. {{Obsolete|0.19}}

-   <img alt="" src=images/Draft_Drawing.svg  style="width:32px;"> [Drawing](Draft_Drawing.md): inserts views of selected objects into a [drawing](Drawing_Workbench.md) page. {{Obsolete|0.17}}

## Preferências


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Preferences-draft.svg  style="width:32px;"> [Preferências](Draft_Preferences/pt-br.md): preferências gerais para o plano de trabalho e para as ferramentas de desenho.
-   <img alt="" src=images/Preferences-import-export.svg  style="width:32px;"> [Preferências de exportação de importação](Import_Export_Preferences/pt-br.md): preferências disponíveis para importação e exportação de e para diferentes formatos de arquivo.


</div>

-   <img alt="" src=images/Preferences-import-export.svg  style="width:32px;"> [Import Export Preferences](Import_Export_Preferences.md): preferences available for importing from and exporting to different file formats.

## Formatos de arquivo 

The Draft Workbench provides FreeCAD with importers and exporters for several file formats. These are used by the [Std Import](Std_Import.md) and [Std Export](Std_Export.md) commands.


<div class="mw-translate-fuzzy">

-   [Autodesk .DXF](Draft_DXF/pt-br.md): importação e exportação [Drawing Exchange Format](http://en.wikipedia.org/wiki/AutoCAD_DXF) arquivos criados com aplicações CAD 2D. Veja também [FreeCAD e DXF Import](FreeCAD_and_DXF_Import/pt-br.md).
-   Autodesk .DWG: importa e exporta arquivos DWG através do importador DXF, quando o utilitário [ODA Converter](Extra_python_modules#ODA_Converter_(anteriormente_Teigha_Converter).md) é instalado. Veja também [FreeCAD e DWG Import](FreeCAD_and_DWG_Import/pt-br.md).
-   [SVG](Draft_SVG/pt-br.md): importação e exportação [Scalable Vector Graphics](http://en.wikipedia.org/wiki/Scalable_Vector_Graphics) arquivos criados com aplicações de desenho vetorial.
-   [Open Cad format .OCA](Draft_OCA/pt-br.md): importa e exporta arquivos OCA/GCAD, um formato de arquivo CAD potencialmente novo [abrir arquivo CAD](http://groups.google.com/group/open_cad_format).
-   [Airfoil Data Format .DAT](Draft_DAT/pt-br.md): importa arquivos DAT descrevendo [Airfoil profiles](http://www.ae.illinois.edu/m-selig/ads/coord_database.html).


</div>

## Testes unitários 


<div class="mw-translate-fuzzy">


**Veja também:**

[Bancada de trabalho Testing framework](Testing/pt-br.md).


</div>


<div class="mw-translate-fuzzy">

Para executar os testes unitários da bancada de trabalho, executar o seguinte a partir do terminal do sistema operacional.


</div>


```python
freecad -t TestDraft
```

## Scripting


<div class="mw-translate-fuzzy">

As ferramentas Draft podem ser usadas em [macros](macros/pt-br.md) e do console [Python](Python/pt-br.md) usando o [Draft API](Draft_API/pt-br.md).


</div>

A bancada de trabalho inclui um módulo para criar amostras de todos os objetos em um novo documento. <small>(v0.19)</small> 


<div class="mw-translate-fuzzy">

Use isto para testar se todos os objetos são produzidos corretamente.


</div>


```python
import drafttests.draft_test_objects as dto
doc = dto.create_test_file()
```


<div class="mw-translate-fuzzy">

A inspeção do código deste módulo é útil para entender como utilizar a interface de programação.


</div>

## Tutorials

-   [Draft tutorial](Draft_tutorial.md)
-   [Draft ShapeString tutorial](Draft_ShapeString_tutorial.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > [Draft](Category_Draft.md) > Draft Workbench/pt-br
