---
- GuiCommand:/tr
   Name:Draft Edit
   Name/tr:Düzenle
   MenuLocation:Taslak → Düzenle
   Workbenches:[Taslak](Draft_Workbench/tr.md), [Yapı](Arch_Workbench/tr.md)
   Shortcut:**D** **E**
   SeeAlso:[Std Edit](Std_Edit.md)
---

# Draft Edit/tr


</div>

## Tanım


<div class="mw-translate-fuzzy">

Düzenleme aracı, seçili nesnenin [Tel](Draft_Wire/tr.md) köşeleri, [Dikdörtgen](Draft_Rectangle/tr.md) uzunluğu ve genişliği veya [Çember](Draft_Circle/tr.md) yarıçapı gibi belirli özelliklerini grafiksel olarak düzenlemenizi sağlar.


</div>

![](images/Draft_Edit_example.png ) 
*4 objects in Draft Edit mode: a Draft Wire (red), a Draft Arc (black), a Draft BSpline (green) and a Draft BezCurve (magenta)*

## Usage

See also: [Draft Snap](Draft_Snap.md) and [Draft Constrain](Draft_Constrain.md).

1.  Optionally select one or more objects. Note that although multiple objects can be in Draft Edit mode, objects can only be edited one at a time.
2.  There are several ways to invoke the command:
    -   If you have not yet selected an object: double-click an object in the [Tree view](Tree_view.md). This only work for supported Draft objects.
    -   Press the **<img src="images/Draft_Edit.svg" width=16px> [Draft Edit](Draft_Edit.md)** button.
    -   Select the **Modification → <img src="images/Draft_Edit.svg" width=16px> Edit** option from the menu.
    -   Use the keyboard shortcut: **D** then **E**.
3.  If you have not yet selected an object: select an object in the [3D view](3D_view.md).
4.  The selected objects are marked with temporary nodes, and the [Main task panel](#Main_task_panel.md) opens. See [Options](#Options.md) for more information.
5.  Optionally use a node or edge context menu. These context menus are only available for some Draft objects. See [Supported objects](#Supported_objects.md) for more information.
    -   Do one of the following:
        -   On all operating systems: hold down **E** and click the node or edge. To use **E** you may have to click in the [3D view](3D_view.md) once to ensure that it has the focus.
        -   On Windows: hold down **Alt** and click the node or edge.
        -   On Linux: hold down **Shift**+**Alt**, **Ctrl**+**Alt** or **Alt**, and click the node or edge.
        -   On macOS: hold down **Option** and click the node or edge.
    -   Select an option from the context menu.
    -   If the selected option requires point input:
        -   The [Node task panel](#Node_task_panel.md) opens. See [Options](#Options.md) for more information.
        -   Pick a point in the [3D view](3D_view.md), or type coordinates and press the **<img src="images/Draft_AddPoint.svg" width=16px> Enter point** button.
6.  Optionally move a node:
    -   Click the node in the [3D view](3D_view.md).
    -   The [Node task panel](#Node_task_panel.md) opens. See [Options](#Options.md) for more information.
    -   Pick a point in the [3D view](3D_view.md), or type coordinates and press the **<img src="images/Draft_AddPoint.svg" width=16px> Enter point** button.
    -   The result depends on the object and the selected node.
7.  Press **Esc** or the **Close** button (the button at the top of the task panel, without the image) to finish the command.

## Seçenekler

The single character keyboard shortcuts mentioned here can be changed. See [Draft Preferences](Draft_Preferences.md).

### Main task panel 

-   Press **O** or the **<img src="images/Draft_CloseLine.svg" width=16px> Close** button to finish the command. If a single [Draft Wire](Draft_Wire.md), [Draft BSpline](Draft_BSpline.md), [Draft CubicBezCurve](Draft_CubicBezCurve.md) or [Draft BezCurve](Draft_BezCurve.md) has been selected the object is closed.
-   Press **Esc** or the **Close** button to finish the command.

### Node task panel 


<div class="mw-translate-fuzzy">

-   Verilen eksendeki bir sonraki noktayı sınırlamak için bir noktadan sonra **X**, **Y** veya **Z** tuşlarına basın.
-   Koordinatları manuel olarak girmek için sayıları girin, ardından her bir X, Y ve Z bileşeni arasında **Enter** tuşuna basın. Noktayı yerleştirmek istediğiniz değerleri aldığınızda **<img src="images/_Draft_AddPoint.svg_" width= 16px> [ Nokta ekle](Draft_AddPoint/tr.md)** düğmesine basabilirsiniz.
-   [ snapping](Draft_Snap/tr.md) noktanızı mesafeden bağımsız olarak, en yakın çeki konumuna yönlendirmek için çizim yaparken **Ctrl** tuşunu basılı tutun.
-   Bir sonraki noktanızı yatay veya dikey olarak son noktaya göre [ constrain](Draft_Constrain/tr.md) çizerken {{KEY | Shift}} tuşunu basılı tutun.
-   Düzenlemeyi bitirmek için {{KEY | Esc}} veya {{button|Kapat}} düğmesine veya **<img src="images/_Draft_Edit.svg_" width= 16px> [Düzenle](Draft_Edit/tr.md)** düğmesine basınız. .


</div>

## Supported objects 

### <img alt="" src=images/Draft_Line.svg  style="width:24px;"> _ 

-   If the start or end node of an open wire is moved so that they coincide, the wire is closed.
-   Node context menu: {{Value|delete point}}. At least two points must remain.
-   Edge context menu: {{Value|add point}}, {{Value|reverse wire}} (<small>(v0.20)</small> ).

### <img alt="" src=images/Draft_Arc.svg  style="width:24px;"> _ 

-   Center node context menu: {{Value|move arc}}.
-   Start node context menu: {{Value|set first angle}}.
-   End node context menu: {{Value|set last angle}}.
-   Mid node context menu: {{Value|set radius}}.
-   Edge context menu: {{Value|invert arc}}. Currently this does not work.

### <img alt="" src=images/Draft_Circle.svg  style="width:24px;"> [Draft Circle](Draft_Circle.md) 

-   No context menus for this object.

### <img alt="" src=images/Draft_Ellipse.svg  style="width:24px;"> [Draft Ellipse](Draft_Ellipse.md) 

-   No context menus for this object.

### <img alt="" src=images/Draft_Rectangle.svg  style="width:24px;"> [Draft Rectangle](Draft_Rectangle.md) 

-   No context menus for this object.

### <img alt="" src=images/Draft_Polygon.svg  style="width:24px;"> [Draft Polygon](Draft_Polygon.md) 

-   No context menus for this object.

### <img alt="" src=images/Draft_BSpline.svg  style="width:24px;"> [Draft BSpline](Draft_BSpline.md) 

-   If the start or end node of an open spline is moved so that they coincide, the spline is closed.
-   Node context menu: {{Value|delete point}}. At least two points must remain for an open spline. For a closed spline the minimum number of points is three.
-   Edge context menu: {{Value|add point}}.

### <img alt="" src=images/Draft_CubicBezCurve.svg  style="width:24px;"> _ 

-   If the start or end node of an open curve is moved so that they coincide, the curve is closed.
-   Node context menu: {{Value|make sharp}}, {{Value|make tangent}}, {{Value|make symmetric}} and {{Value|delete point}}.
-   Edge context menu: {{Value|add point}}.

### <img alt="" src=images/Draft_Dimension.svg  style="width:24px;"> [Draft Dimension](Draft_Dimension.md) 

-   Angular dimensions cannot be edited.
-   The start and end nodes of parametric dimensions cannot be moved.
-   No context menus for this object.

### <img alt="" src=images/Arch_Wall.svg  style="width:24px;"> [Arch Wall](Arch_Wall.md) 

-   A single node to control the height of the wall is displayed above the **Placement** of the wall.
-   No context menus for this object.

### <img alt="" src=images/Arch_Structure.svg  style="width:24px;"> [Arch Structure](Arch_Structure.md) 

-   No context menus for this object.

### <img alt="" src=images/Arch_Window.svg  style="width:24px;"> [Arch Window](Arch_Window.md) 

-   No context menus for this object.

### <img alt="" src=images/Arch_Space.svg  style="width:24px;"> [Arch Space](Arch_Space.md) 

-   No context menus for this object.

### <img alt="" src=images/Arch_Panel_Cut.svg  style="width:24px;"> [Arch Panel Cut](Arch_Panel_Cut.md) 

-   No context menus for this object.

### <img alt="" src=images/Arch_Panel_Sheet.svg  style="width:24px;"> [Arch Panel Sheet](Arch_Panel_Sheet.md) 

-   No context menus for this object.

### <img alt="" src=images/Part_Box.svg  style="width:24px;"> [Part Box](Part_Box.md) 

-   No context menus for this object.

### <img alt="" src=images/Part_Cylinder.svg  style="width:24px;"> [Part Cylinder](Part_Cylinder.md) 

-   No context menus for this object.

### <img alt="" src=images/Part_Sphere.svg  style="width:24px;"> [Part Sphere](Part_Sphere.md) 

-   No context menus for this object.

### <img alt="" src=images/Part_Cone.svg  style="width:24px;"> [Part Cone](Part_Cone.md) 

-   No context menus for this object.

### <img alt="" src=images/Part_Line.svg  style="width:24px;"> [Part Line](Part_Line.md) 

-   No context menus for this object.

### <img alt="" src=images/Sketcher_NewSketch.svg  style="width:24px;"> [Sketcher Sketch](Sketcher_NewSketch.md) 

-   Only sketches that contain a single unconstrained line can be edited. Currently this does not work properly.
-   No context menus for this object.

## Preferences

See also: [Preferences Editor](Preferences_Editor.md) and [Draft Preferences](Draft_Preferences.md).

-   The color of the temporary nodes is the same as the color of the snap symbols. This color can be changed in the preferences: **Edit → Preferences... → Draft → Visual settings → Visual Settings → Color**. Note that this color is not used for the temporary nodes displayed for [Draft BezCurves](Draft_BezCurve.md). These nodes use the **Line Color** of the curve instead.

## Scripting


<div class="mw-translate-fuzzy">

## Betik


**Ayrıca bkz.:**

[Taslak API](Draft_API/tr.md) ve [FreeCAD Betik esasları](FreeCAD_Scripting_Basics/tr.md).


</div>


<div class="mw-translate-fuzzy">

Düzenleme aracı için uygun bir programlama arayüzü yoktur. Her nesne, niteliklerini doğrudan değiştirerek değiştirilir.


</div>


<div class="mw-translate-fuzzy">


{{Draft Tools navi/tr}}


{{Userdocnavi/tr}}


</div>

---
[documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Edit/tr
