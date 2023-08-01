---
- GuiCommand:
   Name: Draft BezCurve
   Name/ro: Draft BezCurve
   MenuLocation: Draft - BezCurve
   Workbenches: [Draft](Draft_Workbench/ro.md), [Arch](Arch_Workbench/ro.md)
   Shortcut: B Z
---

# Draft BezCurve/ro


</div>



## Descriere


<div class="mw-translate-fuzzy">

Instrumentul BezCurve creează o [Bezier Curve](http://en.wikipedia.org/wiki/Bezier_curve) (sau o curbă Bezier în bucăți) din mai multe puncte din planul curent [ work plane](Draft_SelectPlane.md). Este nevoie de [linewidth and color](Draft_Linestyle.md) setată anterior pe fila Activități.


</div>


<div class="mw-translate-fuzzy">

Obiectul este creat ca o singură curbă Bezier de grad (număr_de\_ puncte - 1). Aceasta poate fi modificată la o curbă Bezier în parte, de un anumit grad după crearea folosind [ editor proprietăți](Property.md). Bezier Curves poate fi editat folosind {{KEY | <img src="images/_Draft_Edit.png_" width= 16px> Editare proiect}}.


</div>

The Draft BezCurve and the [Draft CubicBezCurve](Draft_CubicBezCurve.md) commands use **control points** to define the position and curvature of the spline. The [Draft BSpline](Draft_BSpline.md) command, on the other hand, specifies the **exact points** through which the curve will pass.

<img alt="" src=images/Draft_BezCurve_Example.png  style="width:400px;"> 
*Bézier curve defined by multiple points*




<div class="mw-translate-fuzzy">

<img alt="" src=images/Draft_BezCurve_Example.png  style="width:400px;">

## Cum se folosește 


</div>

See also: [Draft Tray](Draft_Tray.md), [Draft Snap](Draft_Snap.md) and [Draft Constrain](Draft_Constrain.md).

1.  There are several ways to invoke the command:
    -   Press the **<img src="images/Draft_BezCurve.svg" width=16px> [Draft BezCurve](Draft_BezCurve.md)** button.
    -   Select the **Drafting → Bézier tools → <img src="images/Draft_BezCurve.svg" width=16px> Bézier curve** option from the menu.
    -   Use the keyboard shortcut: **B** then **Z**. <small>(v0.20)</small> 
2.  The **Bézier curve** task panel opens. See [Options](#Options.md) for more information.
3.  Pick the first point in the [3D view](3D_view.md), or type coordinates and press the **<img src="images/Draft_AddPoint.svg" width=16px> Enter point** button.
4.  Pick additional points in the [3D view](3D_view.md), or type coordinates and press the **<img src="images/Draft_AddPoint.svg" width=16px> Enter point** button.
5.  Press **Esc** or the **Close** button to finish the command.




<div class="mw-translate-fuzzy">

## Cum se foloseşte 

1.  Apăsați butonul **<img src="images/Draft_BezCurve.png" width=16px> [[Draft BezCurve]]
** , sau apăsați {{KEY | W}} apoi tastele **I**
2.  Faceți clic pe un prim punct din vizualizarea 3D sau tastați un coordinate
3.  Faceți clic pe un punct suplimentar în vizualizarea 3D sau tastați un coordinate
4.  Apăsați **F** sau **C** sau faceți dublu clic pe ultimul punct sau faceți clic pe primul punct pentru a termina sau a închide filamentul/polilinia. Dacă filamentul este închis, acesta va fi, de asemenea, o fațetă, chiar dacă acesta apare ca o rețea wireframe.


</div>

The single character keyboard shortcuts available in the task panel can be changed. See [Draft Preferences](Draft_Preferences.md). The shortcuts mentioned here are the default shortcuts.


<div class="mw-translate-fuzzy">

-   Apăsați tasta **F** sau butonul **<img src="images/Draft_FinishLine.png" width=12px> '''Finish'''** pentru a finaliza funcția B spline, lăsând-o deschisă
-   Press **C** or the **<img src="images/Draft_CloseLine.png" width=12px> '''Close'''** button or click on the first point to finish the spline, but making it closed by adding a last segment between the last point and the first one.
-   Press **X**, **Y** or **Z** after a point to constrain the next point on the given axis.
-   To enter coordinates manually, simply enter the numbers, then press **ENTER** between each X, Y and Z component.
-   Press **R** or click the checkbox to check/uncheck the **'''Relative'''** button. If relative mode is on, the coordinates of the next point are relative to the last one. If not, they are absolute, taken from the (0,0,0) origin point.
-   Press **T** or click the checkbox to check/uncheck the **'''Continue'''** button. If continue mode is on, the BezCurve tool will restart after you finish or close it, allowing you to draw another one without pressing the BezCurve button again.
-   Press **CTRL** while drawing to force [snapping](Draft_Snap.md) your point to the nearest snap location, independently of the distance.
-   Press **SHIFT** while drawing to [constrain](Draft_Constrain.md) your next point horizontally or vertically in relation to the last one.
-   Press **W** or press the **<img src="images/Draft_Wipe.png" width=12px> '''Wipe'''** button to remove the existing segments and start the spline from the last point.
-   Press **CTRL**+**Z** or press the **<img src="images/Draft_UndoLine.png" width=12px> '''Undo'''** button to undo the last point.
-   Apăsați tasta **ESC** sau butonul **'''Cancel'''** penru a abandona comanda BezCurve .


</div>

## Notes


<div class="mw-translate-fuzzy">

## Limitări

-   Acest instrument nu este disponibil înainte de versiunea FreeCAD 0.14
-   Proprietatea puncte nu apare încă în lista de proprietăți.
-   OpenCascade nu suportă Bezier Curve cu grad\> 25. Aceasta nu ar trebui să fie o problemă în practică.


</div>

## Preferences

See also: [Preferences Editor](Preferences_Editor.md) and [Draft Preferences](Draft_Preferences.md).

-   To change the number of decimals used for the input of coordinates: **Edit → Preferences... → General → Units → Units settings → Number of decimals**.
-   To change the initial value of filled mode: **Edit → Preferences... → Draft → General settings → Draft tools options → Fill objects with faces whenever possible**. Changing the filled mode in a task panel will override this preference for the current FreeCAD session.



## Proprietăți

See also: [Property editor](Property_editor.md).

A Draft BezCurve object is derived from a [Part Part2DObject](Part_Part2DObject.md) and inherits all its properties. It also has the following additional properties:

### Data


{{TitleProperty|Draft}}

-    **Area|Area**: (read-only) specifies the area of the face of the curve. The value will be {{value|0.0}} if **Make Face** if `False` or the face cannot be created.

-    **Closed|Bool**: specifies if the curve is closed or not. If the curve is initially open this value is `False`, setting it to `True` will draw a segment to close the curve. If the curve is initially closed this value is `True`, setting it to `False` will remove the last segment and make the curve open.

-    **Continuity|IntegerList**: (read-only) specifies the continuity of the curve.

-    **Degree|Integer**: specifies the degree of the curve.

-    **Length|Length**: (read-only) specifies the total length of the curve.

-    **Make Face|Bool**: specifies if the curve makes a face or not. If it is `True` a face is created, otherwise only the perimeter is considered part of the object. This property only works if **Closed** is `True` and if the curve does not self-intersect.

-    **Points|VectorList**: specifies the control points of the curve in its local coordinate system.

### View


{{TitleProperty|Draft}}

-    **Arrow Size|Length**: specifies the size of the symbol displayed at the end of the curve.

-    **Arrow Type|Enumeration**: specifies the type of symbol displayed at the end of the curve, which can be {{value|Dot}}, {{value|Circle}}, {{value|Arrow}}, {{value|Tick}} or {{value|Tick-2}}.

-    **End Arrow|Bool**: specifies whether to show a symbol at the end of the curve, so it can be used as an annotation line.

-    **Pattern|Enumeration**: specifies the [Draft Pattern](Draft_Pattern.md) with which to fill the face of the closed curve. This property only works if **Make Face** is `True` and if **Display Mode** is {{value|Flat Lines}}.

-    **Pattern Size|Float**: specifies the size of the [Draft Pattern](Draft_Pattern.md).

## Scripting


<div class="mw-translate-fuzzy">

## Scrip-Programare 


</div>


<div class="mw-translate-fuzzy">

Instrumentul BezCurve poate fi folosit în [macros](macros.md) și din consola Python utilizând următoarea funcție:


</div>


```python
bezcurve = make_bezcurve(pointslist, closed=False, placement=None, face=None, support=None, degree=None)
bezcurve = make_bezcurve(Part.Wire, closed=False, placement=None, face=None, support=None, degree=None)
```


<div class="mw-translate-fuzzy">

-   Creați un obiect tip curbă Bezier din lista dată a vectorilor. În loc de o listă de puncte, puteți trece și o secțiune parțială.


</div>

Example:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

p1 = App.Vector(0, 0, 0)
p2 = App.Vector(1000, 1000, 0)
p3 = App.Vector(2000, 0, 0)
p4 = App.Vector(1500, -2000, 0)

bezcurve1 = Draft.make_bezcurve([p1, p2, p3, p4], closed=True)
bezcurve2 = Draft.make_bezcurve([p4, 1.3*p2, p1, 4.1*p3], closed=True)
bezcurve3 = Draft.make_bezcurve([1.7*p3, 1.5*p4, 2.1*p2, p1], closed=True)

doc.recompute()
```



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft BezCurve/ro
