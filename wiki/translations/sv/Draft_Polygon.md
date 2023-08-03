# Draft Polygon/sv
---
 GuiCommand:   Name: Draft_Polygon   Workbenches: Draft_Workbench/sv   Skiss|MenuLocation: Draft -> Polygon---


</div>

## Description


<div class="mw-translate-fuzzy">

#### Beskrivning

Detta verktyg frågar användaren efter en centrumpunkt och en radie. Du kan sedan specificera antalet sidor, och en regelbunden polygon kommer att skapas inuti den givna radiens cirkel. Antalet sidor och om polygonen är inskriven eller omskriven cirkeln kan ändras när som helst i objektets egenskaper. Den nyss skapade polygonen kommer att ha nuvarande linkefärg och -tjocklek.

Punkterna kan markeras med musen i 3D vyn eller genom att mata in koordinater med tangentbordet.


</div>

A Draft Polygon can be switched from inscribed to circumscribed by changing its **Draw Mode** property. The corners of a Draft Polygon can be filleted (rounded) or chamfered by changing its **Fillet Radius** or **Chamfer Size** respectively.

<img alt="" src=images/Draft_polygon_example.jpg  style="width:400px;">


<div class="mw-translate-fuzzy">

<img alt="" src=images/Draft_polygon_example.jpg  style="width:400px;">


</div>

## Usage

See also: [Draft Tray](Draft_Tray.md), [Draft Snap](Draft_Snap.md) and [Draft Constrain](Draft_Constrain.md).


<div class="mw-translate-fuzzy">

#### Bruk

-   Markera en punkt på ett tomt område i 3D vyn, eller på ett existerande objekt.
-   Om du håller ned **CTRL** så kommer din punkt att [snäppa](Draft_Snap/sv.md) till tillgängliga snäpp platser.
-   Om du håller ned**SKIFT** så kommer din punkt att [begränsas](Draft_Constrain/sv.md) i relation till den sista punkten.
-   Skriv in siffror för att mata in en koordinat manuellt
-   Om du trycker ned **ESC** så kommer operationen att avbrytas.
-   Polygonen kan visas som en yta eller som en trådmodell, genom att ändra dess visningsläge.


</div>

## Options

The single character keyboard shortcuts available in the task panel can be changed. See [Draft Preferences](Draft_Preferences.md). The shortcuts mentioned here are the default shortcuts.

-   To manually enter the coordinates for the center enter the X, Y and Z component, and press **Enter** after each. Or you can press the **<img src="images/Draft_AddPoint.svg" width=16px> Enter point** button when you have the desired values. It is advisable to move the pointer out of the [3D view](3D_view.md) before entering coordinates.
-   Press **G** or click the **Global** checkbox to toggle global mode. If global mode is on, coordinates are relative to the global coordinate system, else they are relative to the [working plane](Draft_SelectPlane.md) coordinate system. <small>(v0.20)</small> 
-   Press **L** or click the **Filled** checkbox to toggle filled mode. If filled mode is on, the created polygon will have **Make Face** set to `True` and will have a filled face.
-   Press **T** or click the **Continue** checkbox to toggle continue mode. If continue mode is on, the command will restart after finishing, allowing you to continue creating polygons.
-   Press **S** to switch [Draft snapping](Draft_Snap.md) on or off.
-   Press **Esc** or the **Close** button to abort the command.

## Notes

-   A Draft Polygon can be edited with the [Draft Edit](Draft_Edit.md) command.

## Preferences

See also: [Preferences Editor](Preferences_Editor.md) and [Draft Preferences](Draft_Preferences.md).

-   To change the number of decimals used for the input of coordinates and radii: **Edit → Preferences... → General → Units → Units settings → Number of decimals**.
-   To change the initial value of filled mode: **Edit → Preferences... → Draft → General settings → Draft tools options → Fill objects with faces whenever possible**. Changing the filled mode in a task panel will override this preference for the current FreeCAD session.
-   If the **Edit → Preferences... → Draft → General settings → Draft tools options → Use Part Primitives when available** option is checked, the command will create a [Part RegularPolygon](Part_RegularPolygon.md) instead of a Draft Polygon.

## Properties

See also: [Property editor](Property_editor.md).

A Draft Polygon object is derived from a [Part Part2DObject](Part_Part2DObject.md) and inherits all its properties. It also has the following additional properties:

### Data


{{TitleProperty|Draft}}

-    **Area|Area**: (read-only) specifies the area of the face of the polygon. The value will be {{value|0.0}} if **Make Face** if `False`.

-    **Chamfer Size|Length**: specifies the length of the chamfers at the corners of the polygon.

-    **Draw Mode|Enumeration**: specifies if the polygon is {{value|inscribed}} in a circle or {{value|circumscribed}} around a circle.

-    **Faces Number|Integer**: specifies the number of sides of the polygon.

-    **Fillet Radius|Length**: specifies the radius of the fillets at the corners of the polygon.

-    **Make Face|Bool**: specifies if the polygon makes a face or not. If it is `True` a face is created, otherwise only the perimeter is considered part of the object.

-    **Radius|Length**: specifies the radius of the circle that defines the polygon.

### View


{{TitleProperty|Draft}}

-    **Pattern|Enumeration**: specifies the [Draft Pattern](Draft_Pattern.md) with which to fill the face of the polygon. This property only works if **Make Face** is `True` and if **Display Mode** is {{value|Flat Lines}}.

-    **Pattern Size|Float**: specifies the size of the [Draft Pattern](Draft_Pattern.md).

## Scripting

See also: [Autogenerated API documentation](https://freecad.github.io/SourceDoc/) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

To create a Draft Polygon use the `make_polygon` method (<small>(v0.19)</small> ) of the Draft module. This method replaces the deprecated `makePolygon` method.


```python
polygon = make_polygon(nfaces, radius=1, inscribed=True, placement=None, face=None, support=None)
```

-   Creates a `polygon` object with the given number of faces (`nfaces`), and based on a circle of `radius` in millimeters.
-   If `inscribed` is `True`, the polygon is inscribed in the circle, otherwise it will be circumscribed.
-   If `placement` is `None` the polygon is created at the origin and one of its vertices will lie on the X axis.
-   If `face` is `True`, the polygon will make a face, that is, it will appear filled.

Example: 
```python
import FreeCAD as App
import Draft

doc = App.newDocument()

polygon1 = Draft.make_polygon(4, radius=500)
polygon2 = Draft.make_polygon(5, radius=750)

zaxis = App.Vector(0, 0, 1)
p3 = App.Vector(1000, 1000, 0)
place3 = App.Placement(p3, App.Rotation(zaxis, 90))

Polygon3 = Draft.make_polygon(6, radius=1450, placement=place3)

doc.recompute()
```



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Polygon/sv
