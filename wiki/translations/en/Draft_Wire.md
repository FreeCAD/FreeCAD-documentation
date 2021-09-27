---
- GuiCommand:
   Name:Draft Wire
   MenuLocation:Drafting → Polyline
   Workbenches:[Draft](Draft_Workbench.md), [Arch](Arch_Workbench.md)
   Shortcut:**P** **L**
   Version:0.7
   SeeAlso:[Draft Line](Draft_Line.md), [Draft BSpline](Draft_BSpline.md)
---

# Draft Wire/en

## Description

The <img alt="" src=images/Draft_Wire.svg  style="width:24px;"> **Draft Wire** command [creates](#Create.md) a polyline, a sequence of several connected line segments. The command can also be used to [join](#Join.md) [Draft Lines](Draft_Line.md) and Draft Wires.

<img alt="" src=images/Draft_Polyline_example.jpg  style="width:400px;"> 
*Wire defined by multiple points*

## Create

### Usage

See also: [Draft Tray](Draft_Tray.md), [Draft Snap](Draft_Snap.md) and [Draft Constrain](Draft_Constrain.md).

1.  There are several ways to invoke the command:
    -   Press the **<img src="images/Draft_Wire.svg" width=16px> [Draft Wire](Draft_Wire.md)** button.
    -   Select the **Drafting → <img src="images/Draft_Wire.svg" width=16px> Polyline** option from the menu.
    -   Use the keyboard shortcut: **P** then **L**.
2.  The **Polyline** task panel opens. See [Options](#Options.md) for more information.
3.  Pick the first point in the [3D view](3D_view.md), or type coordinates and press the **<img src="images/Draft_AddPoint.svg" width=16px> Enter point** button.
4.  Pick additional points in the [3D view](3D_view.md), or type coordinates and press the **<img src="images/Draft_AddPoint.svg" width=16px> Enter point** button.
5.  Press **Esc** or the **Close** button to finish the command.

### Options

The single character keyboard shortcuts available in the task panel can be changed. See [Draft Preferences](Draft_Preferences.md). The shortcuts mentioned here are the default shortcuts.

-   To manually enter coordinates enter the X, Y and Z component, and press **Enter** after each. Or you can press the **<img src="images/Draft_AddPoint.svg" width=16px> Enter point** button when you have the desired values. It is advisable to move the pointer out of the [3D view](3D_view.md) before entering coordinates.
-   Press **R** or click the **Relative** checkbox to toggle relative mode. If relative mode is on, coordinates are relative to the last point, if available, else they are relative to the coordinate system origin.
-   Press **G** or click the **Global** checkbox to toggle global mode. If global mode is on, coordinates are relative to the global coordinate system, else they are relative to the [working plane](Draft_SelectPlane.md) coordinate system. <small>(v0.20)</small> 
-   Press **L** or click the **Filled** checkbox to toggle filled mode. If filled mode is on, the created wire will have **Make Face** set to `True` and will have a filled face, provided it is closed and does not self-intersect. Note that a self-intersecting wire with a face will not display properly, for such a wire **Make Face** must be set to `False`.
-   Press **T** or click the **Continue** checkbox to toggle continue mode. If continue mode is on, the command will restart after using **<img src="images/Draft_FinishLine.svg" width=16px> Finish** or **<img src="images/Draft_CloseLine.svg" width=16px> Close**, or after creating a closed wire by snapping to the first point of the wire, allowing you to continue creating wires.
-   Press the {{button|<img src="images/Draft_UndoLine.svg" width=16px> Undo}} button to undo the last point. The **Ctrl**+**Z** keyboard shortcut currently does not work as expected.
-   Press **A** or the **<img src="images/Draft_FinishLine.svg" width=16px> Finish** button to finish the command and leave the wire open.
-   Press **O** or the **<img src="images/Draft_CloseLine.svg" width=16px> Close** button to finish the command and close the wire. A closed wire can also be created by snapping to the first point of the wire.
-   Press **W** or the **<img src="images/Draft_Wipe.svg" width=16px> Wipe** button to delete the segments already placed, but keep working from the last point.
-   Press **U** or the **<img src="images/Draft_SelectPlane.svg" width=16px> [Set WP](Draft_SelectPlane.md)** button to adjust the current working plane in the orientation of the last segment.
-   Press **S** to switch [Draft snapping](Draft_Snap.md) on or off.
-   Press **Esc** or the {{button|Close}} button to finish the command.

## Join

### Usage 

1.  The end points of the [Draft Lines](Draft_Line.md) and/or Draft Wires to be joined must be exactly coincident. If required first adjust points to ensure that this is the case.
2.  Select two or more [Draft Lines](Draft_Line.md) and/or Draft Wires.
3.  There are several ways to invoke the command:
    -   Press the **<img src="images/Draft_Wire.svg" width=16px> [Draft Wire](Draft_Wire.md)** button.
    -   Select the **Drafting → <img src="images/Draft_Wire.svg" width=16px> Polyline** option from the menu.
    -   Use the keyboard shortcut: **P** then **L**.

## Notes

-   A Draft Wire can be edited with the [Draft Edit](Draft_Edit.md) command.
-   A Draft Wire can be converted to a [Draft BSpline](Draft_BSpline.md) with the [Draft WireToBSpline](Draft_WireToBSpline.md) command.
-   [Draft Lines](Draft_Line.md) and Draft Wires can also be joined with the [Draft Join](Draft_Join.md) command or the [Draft Upgrade](Draft_Upgrade.md) command.

## Preferences

See also: [Preferences Editor](Preferences_Editor.md) and [Draft Preferences](Draft_Preferences.md).

-   To change the number of decimals used for the input of coordinates: **Edit → Preferences... → General → Units → Units settings → Number of decimals**.
-   To change the initial value of filled mode: **Edit → Preferences... → Draft → General settings → Draft tools options → Fill objects with faces whenever possible**. Changing the filled mode in a task panel will override this preference for the current FreeCAD session.

## Properties

See also: [Property editor](Property_editor.md).

A Draft Wire object is derived from a [Part Part2DObject](Part_Part2DObject.md) and inherits all its properties. It also has the following additional properties:

### Data


{{TitleProperty|Draft}}

-    **Area|Area**: (read-only) specifies the area of the face of the wire. The value will be {{value|0.0}} if **Make Face** if `False` or the face cannot be created.

-    **Base|Link**
    

-    **Chamfer Size|Length**: specifies the length of the chamfers at the corners of the wire.

-    **Closed|Bool**: specifies if the wire is closed or not. If the wire is initially open this value is `False`, setting it to `True` will draw a line segment to close the wire. If the wire is initially closed this value is `True`, setting it to `False` will remove the last line segment and make the wire open.

-    **End|VectorDistance**: specifies the end point of the wire.

-    **Fillet Radius|Length**: specifies the radius of the fillets at the corners of the wire.

-    **Length|Length**: (read-only) specifies the total length of the wire.

-    **Make Face|Bool**: specifies if the wire makes a face or not. If it is `True` a face is created, otherwise only the edges are considered part of the object. This property only works if **Closed** is `True` and if the wire does not self-intersect.

-    **Points|VectorList**: specifies the points of the wire in its local coordinate system.

-    **Start|VectorDistance**: specifies the start point of the wire.

-    **Subdivisions|Integer**: specifies the number of subdivisions for each edge of the wire. If it is {{value|1}} each edge will be divided into {{value|2}} equal segments. Subdivisions are applied before chamfers and fillets.

-    **Tool|Link**
    

### View


{{TitleProperty|Draft}}

-    **Arrow Size|Length**: specifies the size of the symbol displayed at the end of the wire.

-    **Arrow Type|Enumeration**: specifies the type of symbol displayed at the end of the wire, which can be {{value|Dot}}, {{value|Circle}}, {{value|Arrow}}, {{value|Tick}} or {{value|Tick-2}}.

-    **End Arrow|Bool**: specifies whether to show a symbol at the end of the wire, so it can be used as an annotation line.

-    **Pattern|Enumeration**: specifies the [Draft Pattern](Draft_Pattern.md) with which to fill the face of the closed wire. This property only works if **Make Face** is `True` and if **Display Mode** is {{value|Flat Lines}}.

-    **Pattern Size|Float**: specifies the size of the [Draft Pattern](Draft_Pattern.md).

## Scripting

See also: _.

To create a Draft Wire use the `make_wire` method (<small>(v0.19)</small> ) of the Draft module. This method replaces the deprecated `makeWire` method.


```python
wire = make_wire(pointslist, closed=False, placement=None, face=None, support=None)
wire = make_wire(Part.Wire, closed=False, placement=None, face=None, support=None)
```

-   Creates a `Wire` object with the given list of points, `pointslist`.
    -   Each point in the list is defined by its `FreeCAD.Vector`, with units in millimeters.
    -   Alternatively, the input can be a `Part.Wire`, from which points are extracted.
-   If `closed` is `True`, or if the first and last points are identical, the wire is closed.
-   If `placement` is `None` the shape is created at the origin.
-   If `face` is `True`, and the wire is closed, the wire will make a face, that is, it will appear filled.

Example:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

p1 = App.Vector(0, 0, 0)
p2 = App.Vector(1000, 1000, 0)
p3 = App.Vector(2000, 0, 0)

wire1 = Draft.make_wire([p1, p2, p3], closed=True)
wire2 = Draft.make_wire([p1, 2*p3, 1.3*p2], closed=True)
wire3 = Draft.make_wire([1.3*p3, p1, -1.7*p2], closed=True)

doc.recompute()
```

---
[documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Wire/en
