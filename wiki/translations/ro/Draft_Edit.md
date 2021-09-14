---
- GuiCommand:   Name:Draft Edit   Workbenches:[Arch](Draft_Workbench___Draft]],_[[Arch_Workbench.md)|MenuLocation:Draft → Edit---


</div>

## Descriere


<div class="mw-translate-fuzzy">

Acest instrument vă permite să editați în mod grafic anumite proprietăți ale obiectului selectat, cum ar fi vârfurile unui filament, lungimea și lățimea unui dreptunghi sau raza unui cerc. El nu face decât să intre în modul de editare al obiectului, astfel încât alte moduri de a intra în modul de editare (cum ar fi dublul clic pe obiect în vizualizarea Arbore) dau același rezultat.


</div>

![](images/Draft_Edit_example.png ) *4 objects in Draft Edit mode: a Draft Wire (red), a Draft Arc (black), a Draft BSpline (green) and a Draft BezCurve (magenta)*

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
7.  Press **Esc** or the **Close** button to finish the command.

## Opţiuni

The single character keyboard shortcuts mentioned here can be changed. See [Draft Preferences](Draft_Preferences.md).

### Main task panel 

-   Press **O** or the **<img src="images/Draft_CloseLine.svg" width=16px> Close** button to finish the command. If a single [Draft Wire](Draft_Wire.md) has been selected the wire is closed.
-   Press **Esc** or the **Close** button to finish the command.

### Node task panel 


<div class="mw-translate-fuzzy">

-   Instrumentul Editare funcționează numai pe un obiect selectat la un moment dat.
-   Instrumentul Editare funcționează numai pe filamente Draft, dreptunghiuri, cercuri și arce de cerc. Alte tipuri de obiecte trebuie mai întâi să fie convertite în obiecte Draft.
-   Faceți clic pe un vertex de editare pentru a o muta, faceți clic din nou pentru a o elibera.
-   Apăsați {{KEY | X}}, {{KEY | Y}} sau {{KEY | Z}} după un punct pentru a restrânge următorul punct de pe axa dată.
-   Pentru a introduce manual coordonatele, pur și simplu introduceți numerele, apoi apăsați {{KEY | ENTER}} între fiecare componentă X, Y și Z.
-   Apăsați {{KEY | CTRL}} în timp ce desenați pentru a forța [ snapping](Draft_Snap.md) punctul dvs. către cea mai apropiată locație, independent de distanța.
-   Apăsați pe {{KEY | SHIFT}} în timp ce desenați [ constrain](Draft_Constrain.md) următorul punct pe orizontală sau pe verticală în raport cu ultima.
-   Apăsați tasta {{KEY | ESC}} sau butonul {{KEY | '''Anulare'''}} sau **<img src="images/Draft_Edit.png" width=16px> [[Draft Edit]]** pentru a termina editarea.
-   Apasarea tastei **<img src="images/Draft_AddPoint.png" width=12px> [Add point](Draft_AddPoint.md)** vă permite să adăugați puncte în Filamente și curbe BSplines făcând clic pe segmente
-   Apasarea tastei **<img src="images/Draft_DelPoint.png" width=12px> [Del point](Draft_DelPoint.md)** va permite sa îndepărtați punctele de pe Wire si BSplines facand click pe punctele pe care le eliminati


</div>

## Supported objects 

### <img alt="" src=images/Draft_Line.svg  style="width:24px;"> [Draft Line](Draft_Line.md) and <img alt="" src=images/Draft_Wire.svg  style="width:24px;"> [Draft Wire](Draft_Wire.md) 

-   If the start or end node of an open wire is moved so that they coincide, the wire is closed.
-   Node context menu: {{Value|delete point}}. At least two points must remain.
-   Edge context menu: {{Value|add point}}, {{Value|reverse wire}} (<small>(v0.20)</small> ).

### <img alt="" src=images/Draft_Arc.svg  style="width:24px;"> [Draft Arc](Draft_Arc.md) and <img alt="" src=images/Draft_Arc_3Points.svg  style="width:24px;"> [Draft Arc 3Points](Draft_Arc_3Points.md) 

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

### <img alt="" src=images/Draft_CubicBezCurve.svg  style="width:24px;"> [Draft CubicBezCurve](Draft_CubicBezCurve.md) and <img alt="" src=images/Draft_BezCurve.svg  style="width:24px;"> [Draft BezCurve](Draft_BezCurve.md) 

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

## Scrip-Programare 


</div>


<div class="mw-translate-fuzzy">

Nu e disponibil. Fiecare obiect de mai sus poate fi modificat prin schimbarea proprietăților sale direct.


</div>





 
