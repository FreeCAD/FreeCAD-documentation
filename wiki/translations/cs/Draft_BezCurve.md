---
- GuiCommand   *
   Name   *Draft BezCurve
   Workbenches   *[Draft](Draft_Workbench/cs.md), [Arch](Arch_Workbench/cs.md)
   MenuLocation   *Draft -> BezCurve
   Shortcut   *B Z
---

# Draft BezCurve/cs


</div>

## Popis


<div class="mw-translate-fuzzy">

Nástroj Bezierova křivka vytváří [Bezierovu křivku](http   *//en.wikipedia.org/wiki/Bezier_curve) (nebo Bezierovu křivku po částech) z několika bodů v aktuální [pracovní rovině](Draft_SelectPlane/cs.md). Přebírá [tloušťku čáry a barvu](Draft_Linestyle/cs.md) předem nastavenou v záložce Nástroje.


</div>

The command creates a single Bézier curve with a **Degree** that is `number_of_points - 1`. It can be transformed into a piecewise Bézier curve by reducing this property.

The Draft BezCurve and the [Draft CubicBezCurve](Draft_CubicBezCurve.md) commands use **control points** to define the position and curvature of the spline. The [Draft BSpline](Draft_BSpline.md) command, on the other hand, specifies the **exact points** through which the curve will pass.

<img alt="" src=images/Draft_BezCurve_Example.png  style="width   *400px;"> 
*Bézier curve defined by multiple points*


<div class="mw-translate-fuzzy">

<img alt="" src=images/Draft_BezCurve_Example.png  style="width   *400px;">


</div>

See also   * [Draft Tray](Draft_Tray.md), [Draft Snap](Draft_Snap.md) and [Draft Constrain](Draft_Constrain.md).

1.  There are several ways to invoke the command   *
    -   Press the **<img src="images/Draft_BezCurve.svg" width=16px> [Draft BezCurve](Draft_BezCurve.md)** button.
    -   Select the **Drafting → Bézier tools → <img src="images/Draft_BezCurve.svg" width=16px> Bézier curve** option from the menu.
    -   Use the keyboard shortcut   * **B** then **Z**. <small>(v0.20)</small> 
2.  The **Bézier curve** task panel opens. See [Options](#Options.md) for more information.
3.  Pick the first point in the [3D view](3D_view.md), or type coordinates and press the **<img src="images/Draft_AddPoint.svg" width=16px> Enter point** button.
4.  Pick additional points in the [3D view](3D_view.md), or type coordinates and press the **<img src="images/Draft_AddPoint.svg" width=16px> Enter point** button.
5.  Press **Esc** or the **Close** button to finish the command.


<div class="mw-translate-fuzzy">

## Použití

1.  Stiskněte tlačítko **<img src="images/Draft_BezCurve.png" width=16px> [Bezierova křivka](Draft_BezCurve.md)
** nebo klávesy **B** potom **Z**
2.  Klikněte na první bod ve 3D pohledu nebo zadejte jeho souřadnice
3.  Klikněte na další bod ve 3D pohledu nebo zadejte jeho souřadnice
4.  Stiskněte klávesu **F** nebo **C** nebo dvojklikněte na poslední bod pro ukončení nebo na počáteční bod pro uzavření křivky.

## Volby


</div>

The single character keyboard shortcuts available in the task panel can be changed. See [Draft Preferences](Draft_Preferences.md). The shortcuts mentioned here are the default shortcuts.


<div class="mw-translate-fuzzy">

-   Stiskněte tlačítko **F** nebo **<img src="images/Draft_FinishLine.png" width=12px> '''Dokončit'''** pro ukončení křivky bez uzavření
-   Stiskněte tlačítko **C** nebo **<img src="images/Draft_CloseLine.png" width=12px> '''Uzavřít'''** nebo klikněte na první bod pro dokončení křivky s tím, že bude uzavřena a eventuálně bude přdán poslední segment do počátečního bodu.
-   Stiskněte tlačítko **X**, **Y** nebo **Z** po vybrání bodu a pak bude další výběr proveden v dané ose.
-   Pro ruční zadání souřadnic jednoduše vložte číslo a stiskněte **ENTER** mezi každou z komponent X, Y a Z.
-   Stiskněte tlačítko **R** nebo zaklikněte/odklikněte políčko **'''Relativně'''**. Je-li zapnut relativní mód souřadnice následujícího bodu bodou relativní k předchozímu bodu, jinak budou absolutní k počátku (0,0,0).
-   Stiskněte tlačítko **T** nebo zaklikněte/odklikněte políčko **'''Pokračovat'''**. Je-li zapnut pokračovací mód, bude nástroj Bezierova křivka po ukončení nebo uzavření křivky restartován a můžete hned kreslit další bez klikání na tlačítko pro Bezierovu křivku.
-   Stiskněte při kreslení tlačítko **CTRL** chcete-li [přichytit](Draft_Snap.md) Váš bod k nejbližšímu uchopovacímu místu, nezávisle na tom jak je daleko.
-   Stiskněte při kreslení tlačítko **SHIFT** pro nastavení [vazby](Draft_Constrain.md) dalšího bodu svisle nebo vodorovně v relaci k poslednímu bodu.
-   Stiskněte klávesu **W** nebo tlačítko **<img src="images/Draft_Wipe.png" width=12px> '''Smazat'''** pro smazání existujících segmentů a spuštění křivky od posledního bodu.
-   Stiskněte klávesy **CTRL**+**Z** nebo tlačítko **<img src="images/Draft_UndoLine.png" width=12px> '''Undo'''** pro vrácení k předchozímu bodu.
-   Stiskněte klávesu **ESC** nebo tlačítko **'''Zrušit'''** k ukončení aktuálního příkazu pro Bezierovu křivku.


</div>

## Notes


<div class="mw-translate-fuzzy">

## Omezení

-   Tento nástroj je dostupný až od verze FreeCADu 0.14
-   Vlastnost Body se zatím nezaobrazuje v seznamu vlastností.
-   OpenCascade nepodporuje Bezierovy křivky se stupněm \< 25. V praxi by to neměl být problém.


</div>

## Preferences

See also   * [Preferences Editor](Preferences_Editor.md) and [Draft Preferences](Draft_Preferences.md).

-   To change the number of decimals used for the input of coordinates   * **Edit → Preferences... → General → Units → Units settings → Number of decimals**.
-   To change the initial value of filled mode   * **Edit → Preferences... → Draft → General settings → Draft tools options → Fill objects with faces whenever possible**. Changing the filled mode in a task panel will override this preference for the current FreeCAD session.

## Vlastnosti

See also   * [Property editor](Property_editor.md).

A Draft BezCurve object is derived from a [Part Part2DObject](Part_Part2DObject.md) and inherits all its properties. It also has the following additional properties   *

### Data


{{TitleProperty|Draft}}

-    **Area|Area**   * (read-only) specifies the area of the face of the curve. The value will be {{value|0.0}} if **Make Face** if `False` or the face cannot be created.

-    **Closed|Bool**   * specifies if the curve is closed or not. If the curve is initially open this value is `False`, setting it to `True` will draw a segment to close the curve. If the curve is initially closed this value is `True`, setting it to `False` will remove the last segment and make the curve open.

-    **Continuity|IntegerList**   * (read-only) specifies the continuity of the curve.

-    **Degree|Integer**   * specifies the degree of the curve.

-    **Length|Length**   * (read-only) specifies the total length of the curve.

-    **Make Face|Bool**   * specifies if the curve makes a face or not. If it is `True` a face is created, otherwise only the perimeter is considered part of the object. This property only works if **Closed** is `True` and if the curve does not self-intersect.

-    **Points|VectorList**   * specifies the control points of the curve in its local coordinate system.

### View


{{TitleProperty|Draft}}

-    **Arrow Size|Length**   * specifies the size of the symbol displayed at the end of the curve.

-    **Arrow Type|Enumeration**   * specifies the type of symbol displayed at the end of the curve, which can be {{value|Dot}}, {{value|Circle}}, {{value|Arrow}}, {{value|Tick}} or {{value|Tick-2}}.

-    **End Arrow|Bool**   * specifies whether to show a symbol at the end of the curve, so it can be used as an annotation line.

-    **Pattern|Enumeration**   * specifies the [Draft Pattern](Draft_Pattern.md) with which to fill the face of the closed curve. This property only works if **Make Face** is `True` and if **Display Mode** is {{value|Flat Lines}}.

-    **Pattern Size|Float**   * specifies the size of the [Draft Pattern](Draft_Pattern.md).

## Scripting


<div class="mw-translate-fuzzy">

## Skriptování


</div>


<div class="mw-translate-fuzzy">

Nástroj Bezierova křivka může být využit v [makrech](macros.md) a z konzoly Pythonu použitím následující funkce   *


</div>


```python
bezcurve = make_bezcurve(pointslist, closed=False, placement=None, face=None, support=None, degree=None)
bezcurve = make_bezcurve(Part.Wire, closed=False, placement=None, face=None, support=None, degree=None)
```


<div class="mw-translate-fuzzy">

-   Vytvoří objekt Bezierovy křivky podle zadaného seznamu vektorů. Místo seznamu bodů můžete také vložit díl Drát.


</div>

Example   *


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
![](images/Right_arrow.png) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft BezCurve/cs
