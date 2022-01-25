---
- GuiCommand:/de
   Name:Draft Polygon
   Name/de:Entwurf Polygon
   MenuLocation:Entwurf → Polygon
   Workbenches:[Entwurf](Draft_Workbench/de.md), [Arch](Arch_Workbench/de.md)
   Shortcut:**P** **G**
   Version:0.7
   SeeAlso:[Entwurf Kreis](Draft_Circle/de.md), [Entwurf Muster](Draft_Pattern/de.md)
---

# Draft Polygon/de


</div>

## Beschreibung


<div class="mw-translate-fuzzy">

Das Polygonwerkzeug erstellt ein regelmäßiges Polygon, das in einen Umfang eingeschrieben ist, indem es zwei Punkte auswählt, den Mittelpunkt und den Radius. Es wird das [Draft Linestyle/de](Draft_Linestyle/de.md) verwendet, das auf dem [Draft Tray/de](Draft_Tray/de.md) eingestellt ist.


</div>


<div class="mw-translate-fuzzy">

Das Polygon wird in einem Kreis mit dem angegebenen Radius einbeschrieben; es kann nach der Erstellung durch Ändern seiner Zeichenmoduseigenschaften auf umschrieben umgeschaltet werden.


</div>

<img alt="" src=images/Draft_polygon_example.jpg  style="width:400px;">


<div class="mw-translate-fuzzy">



*Regelmäßiges Polygon, das durch den Mittelpunkt und den Radius definiert ist*


</div>

## Anwendung

See also: [Draft Tray](Draft_Tray.md), [Draft Snap](Draft_Snap.md) and [Draft Constrain](Draft_Constrain.md).


<div class="mw-translate-fuzzy">

1.  Drücke die Taste **<img src="images/Draft_Polygon.png" width=16px> [[Draft Polygon]]** oder drücke **P** dann **G** Tasten.
2.  Passe die gewünschte Anzahl von Seiten im Optionsdialog an.
3.  Klicke auf einen ersten Punkt in der 3D-Ansicht, oder gib eine Koordinate und drücke die **<img src="images/Draft_AddPoint.svg" width=16px> add point** Taste.
4.  Klicke auf einen anderen Punkt in der 3D-Ansicht oder gib einen Radiuswert ein, um den Polygonradius zu definieren.


</div>

## Options

The single character keyboard shortcuts available in the task panel can be changed. See [Draft Preferences](Draft_Preferences.md). The shortcuts mentioned here are the default shortcuts.

-   To manually enter the coordinates for the center enter the X, Y and Z component, and press **Enter** after each. Or you can press the **<img src="images/Draft_AddPoint.svg" width=16px> Enter point** button when you have the desired values. It is advisable to move the pointer out of the [3D view](3D_view.md) before entering coordinates.
-   The **Relative** checkbox, displayed in FreeCAD version 0.19 and earlier, has no purpose for this command.
-   Press **G** or click the **Global** checkbox to toggle global mode. If global mode is on, coordinates are relative to the global coordinate system, else they are relative to the [working plane](Draft_SelectPlane.md) coordinate system. <small>(v0.20)</small> 
-   Press **L** or click the **Filled** checkbox to toggle filled mode. If filled mode is on, the created polygon will have **Make Face** set to `True` and will have a filled face.
-   Press **T** or click the **Continue** checkbox to toggle continue mode. If continue mode is on, the command will restart after finishing, allowing you to continue creating polygons.
-   Press **S** to switch [Draft snapping](Draft_Snap.md) on or off.
-   Press **Esc** or the **Close** button to abort the command.

## Notes


<div class="mw-translate-fuzzy">

Das Polygon kann durch Doppelklick auf das Element in der Baumansicht oder durch Drücken der Taste **<img src="images/Draft_Edit.svg" width=16px> [[Draft Edit/de]]** bearbeitet werden. Dann kannst Du die Mittel- und Radiuspunkte auf eine neue Position verschieben.


</div>

## Preferences

See also: [Preferences Editor](Preferences_Editor.md) and [Draft Preferences](Draft_Preferences.md).

-   To change the number of decimals used for the input of coordinates and radii: **Edit → Preferences... → General → Units → Units settings → Number of decimals**.
-   To change the initial value of filled mode: **Edit → Preferences... → Draft → General settings → Draft tools options → Fill objects with faces whenever possible**. Changing the filled mode in a task panel will override this preference for the current FreeCAD session.
-   If the **Edit → Preferences... → Draft → General settings → Draft tools options → Use Part Primitives when available** option is checked, the command will create a [Part RegularPolygon](Part_RegularPolygon.md) instead of a Draft Polygon.

## Eigenschaften

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


<div class="mw-translate-fuzzy">

## Skripten


**Siehe auch:**

[Draft API](Draft_API/de.md) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).


</div>

To create a Draft Polygon use the `make_polygon` method (<small>(v0.19)</small> ) of the Draft module. This method replaces the deprecated `makePolygon` method.


```python
polygon = make_polygon(nfaces, radius=1, inscribed=True, placement=None, face=None, support=None)
```

-   Creates a `polygon` object with the given number of faces (`nfaces`), and based on a circle of `radius` in millimeters.
-   If `inscribed` is `True`, the polygon is inscribed in the circle, otherwise it will be circumscribed.
-   If `placement` is `None` the polygon is created at the origin and one of its vertices will lie on the X axis.
-   If `face` is `True`, the polygon will make a face, that is, it will appear filled.

Beispiel: 
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


<div class="mw-translate-fuzzy">





</div>



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Polygon/de
