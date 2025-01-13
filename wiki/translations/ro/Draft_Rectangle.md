---
 GuiCommand:
   Name: Draft Rectangle
   Name/ro: Dreptunghi
   Workbenches: Draft_Workbench/ro, Arch_Workbench/ro
   MenuLocation: Draft , Rectangle
   Shortcut: **R** **E**
   Version: 0.7
   SeeAlso: Part Box/ro
---

# Draft Rectangle/ro


</div>

## Description


<div class="mw-translate-fuzzy">

## Descriere

Instrumentul Dreptunghi creează un dreptunghi prin alegerea a două puncte. Este nevoie de [linewidth and color](Draft_Linestyle/ro.md) setată pe Bara de instrumente pentru bara de meniu. Puteți adăuga opțional un șanț de 45 de grade sau un filet circular la fiecare colț al dreptunghiului și puteți împărți dreptunghiul într-o serie de rânduri și/sau coloane de dimensiuni egale.


</div>

The corners of a Draft Rectangle can be filleted (rounded) or chamfered by changing its **Fillet Radius** or **Chamfer Size** respectively. It is also possible to subdivide a Draft Rectangle by changing its **Columns** and/or **Rows** property.

<img alt="" src=images/Draft_Rectangle_example.jpg  style="width:400px;">


<div class="mw-translate-fuzzy">

<img alt="" src=images/Draft_Rectangle_example.jpg  style="width:400px;">


</div>

## Usage

See also: [Draft Tray](Draft_Tray.md), [Draft Snap](Draft_Snap.md) and [Draft Constrain](Draft_Constrain.md).


<div class="mw-translate-fuzzy">

## Cum se utiliează 

1.  Press the **<img src="images/Draft_Rectangle.png" width=16px> [Draft Rectangle](Draft_Rectangle/ro.md)** button, or press **R** then **E** keys
2.  Click a first corner point on the 3D view, or type a coordinate
3.  Click another opposite point on the 3D view, or type a coordinate. The rectangle will also be a face, even if it appears as wireframe.


</div>

## Options

The single character keyboard shortcuts available in the task panel can be changed. See [Draft Preferences](Draft_Preferences.md). The shortcuts mentioned here are the default shortcuts (for version 1.0).


<div class="mw-translate-fuzzy">

## Opțiuni

-   Press **X**, **Y** or **Z** after a point to constrain the next point on the given axis.
-   To enter coordinates manually, simply enter the numbers, then press **ENTER** between each X, Y and Z component.
-   Press **R** or click the checkbox to check/uncheck the **'''Relative'''** button. If relative mode is on, the coordinates of the next point are relative to the last one. If not, they are absolute, taken from the (0,0,0) origin point.
-   Press **T** or click the checkbox to check/uncheck the **'''Continue'''** button. If continue mode is on, the Rectangle tool will restart after you finish or close it, allowing you to draw another one without pressing the Rectangle button again.
-   Press **CTRL** while drawing to force [snapping](Draft_Snap/ro.md) your point to the nearest snap location, independently of the distance.
-   Press **SHIFT** while drawing to [constrain](Draft_Constrain/ro.md) your next point horizontally or vertically in relation to the last one.
-   Press **I** or the **'''Filled'''** button to have the rectangle filled with a face after it has been closed.
-   Press **ESC** or the **'''Cancel'''** button to abort the current Line command.
-   Rectangles, when in \"Flat Lines\" display mode, can display a hatch pattern, by setting their \"Pattern\" property.


</div>

## Notes

-   A Draft Rectangle can be edited with the [Draft Edit](Draft_Edit.md) command.

## Preferences

See also: [Preferences Editor](Preferences_Editor.md) and [Draft Preferences](Draft_Preferences.md).

-   If the **Edit → Preferences... → Draft → General → Create Part primitives if possible** option is checked, the command will create a [Part Plane](Part_Plane.md) instead of a Draft Rectangle.




<div class="mw-translate-fuzzy">

## Proprietăți

-    {{PropertyData/ro|Length}}: Specifies the length of the rectangle

-    {{PropertyData/ro|Width}}: Specifies the width of the rectangle

-    {{PropertyData/ro|Chamfer Size}}: Specifies the size of chamfered corners

-    {{PropertyData/ro|Fillet Radius}}: Specifies a curvature radius to give to the corners of the rectangle

-    {{PropertyData/ro|Rows}}: Allows to give horizontal subdivisions to this rectangle

-    {{PropertyData/ro|Columns}}: Allows to give vertical subdivisions to this rectangle

-    {{PropertyData/ro|Make Face}}: Fills the rectangle with a face

-    {{PropertyView/ro|Texture Image}}: Allows to give the path to an image file to be mapped on the rectangle. It is up to you to give the rectangle the same proportion as the image if you want to avoid distortions. Blanking this property will remove the image.

-    {{PropertyView/ro|Pattern}}: Specifies a hatch pattern to fill the wire with.

-    {{PropertyView/ro|Pattern Size}}: Specifies the size of the hatch pattern


</div>

See also: [Property editor](Property_editor.md).

A Draft Rectangle object is derived from a [Part Part2DObject](Part_Part2DObject.md) and inherits all its properties. It also has the following additional properties:

### Data


{{TitleProperty|Draft}}

-    **Area|Area**: (read-only) specifies the area of the face of the rectangle. The value will be {{value|0.0}} if **Make Face** if `False`.

-    **Chamfer Size|Length**: specifies the length of the chamfers at the corners of the rectangle.

-    **Columns|Integer**: specifies the number of equal-sized columns in which the rectangle is divided.

-    **Fillet Radius|Length**: specifies the radius of the fillets at the corners of the rectangle.

-    **Height|Distance**: specifies the height of the rectangle.

-    **Length|Distance**: specifies the length of the rectangle.

-    **Make Face|Bool**: specifies if the rectangle makes a face or not. If it is `True` a face is created, otherwise only the perimeter is considered part of the object.

-    **Rows|Integer**: specifies the number of equal-sized rows in which the rectangle is divided.

### View


{{TitleProperty|Draft}}

-    **Pattern|Enumeration**: specifies the [Draft Pattern](Draft_Pattern.md) with which to fill the face of the rectangle. This property only works if **Make Face** is `True` and if **Display Mode** is {{value|Flat Lines}}.

-    **Pattern Size|Float**: specifies the size of the [Draft Pattern](Draft_Pattern.md).

-    **Texture Image|File**: specifies the path of the image file to be mapped onto the face of the rectangle. Blanking this property will remove the image. The rectangle should have the same proportions as the image to avoid distortions.

## Scripting


<div class="mw-translate-fuzzy">

## Scripturi

Instrumentul dreptunghi poate fi folosit în [macros](macros/ro.md) și din consola [Python](Python/ro.md) utilizând următoarea funcție:


</div>

To create a Draft Rectangle use the `make_rectangle` method (<small>(v0.19)</small> ) of the Draft module. This method replaces the deprecated `makeRectangle` method.


```python
rectangle = make_rectangle(length, height, placement=None, face=None, support=None)
```


<div class="mw-translate-fuzzy">

-   Creează un obiect Dreptunghi Rectangle cu lungimea length în direcția X și înălțimea height în direcția Y.
-   Dacă este dată o destinație de plasare, aceasta este utilizată.
-   Dacă face is None, dreptunghiul este afișat ca un cadru de sârmă, altfel ca o fațetă.
-   Se va folosi versiunea curentă [Draft Linestyle](Draft_Linestyle/ro.md) de linie și culoare.
-   Returnează obiectul nou creat.


</div>

Exempluː 
```python
import FreeCAD as App
import Draft

doc = App.newDocument()

rectangle1 = Draft.make_rectangle(4000, 1000)
rectangle2 = Draft.make_rectangle(1000, 4000)

zaxis = App.Vector(0, 0, 1)
p3 = App.Vector(1000, 1000, 0)
place3 = App.Placement(p3, App.Rotation(zaxis, 45))

rectangle3 = Draft.make_rectangle(3500, 250, placement=place3)

doc.recompute()
```



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Rectangle/ro
