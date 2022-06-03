---
- GuiCommand   */ro
   Name   *Draft BSpline
   Name/ro   *Funcții BSpline
   Workbenches   *[Draft](Draft_Workbench/ro.md), [Arch](Arch_Workbench/ro.md)
   MenuLocation   *Draft → BSpline
   Shortcut   ***B** **S**
   SeeAlso   *[Draft Wire](Draft_Wire/ro.md)
---

# Draft BSpline/ro


</div>

## Description


<div class="mw-translate-fuzzy">

## Descriere

Instrumentul BSpline creează o curbă [B-Spline](http   *//en.wikipedia.org/wiki/B-spline) din mai multe puncte din actualul [work plane](Draft_SelectPlane/ro.md). Este nevoie de [linewidth and color](Draft_Linestyle/ro.md) setată anterior pe fila Activități. Instrumentul BSpline se comportă exact ca instrumentul [Draft Wire](Draft_Wire/ro.md).


</div>

The Draft BSpline command specifies the **exact points** through which the curve will pass. The [Draft BezCurve](Draft_BezCurve.md) and the [Draft CubicBezCurve](Draft_CubicBezCurve.md) commands, on the other hand, use **control points** to define the position and curvature of the spline.

<img alt="" src=images/Draft_bspline_example.jpg  style="width   *400px;">


<div class="mw-translate-fuzzy">

<img alt="" src=images/Draft_bspline_example.jpg  style="width   *400px;">


</div>

## Usage

See also   * [Draft Tray](Draft_Tray.md), [Draft Snap](Draft_Snap.md) and [Draft Constrain](Draft_Constrain.md).


<div class="mw-translate-fuzzy">

## Cum se folosește 

1.  Apăsați butonul **<img src="images/Draft_BSpline.png" width=16px> [Draft BSpline](Draft_BSpline/ro.md)
**, sau apăsați tastele **B** apoi **S**
2.  Click pe primul punct în vizualizarea 3D, sau tastați coordinate
3.  Click ăe punctele adiționale în vizualizarea 3D, sau tastați coordinate
4.  Apăsați tastele **F** sau **C** sau faceți dublu clic pe ultimul punct sau faceți clic pe primul punct pentru a termina sau închide curba spline. Dacă curba B spline este închisă, ea va fi de asemenea o fațetă, chiar dacă ea apare ca un cadru de tip wireframe.


</div>

## Options

The single character keyboard shortcuts available in the task panel can be changed. See [Draft Preferences](Draft_Preferences.md). The shortcuts mentioned here are the default shortcuts.


<div class="mw-translate-fuzzy">

## Opțiuni

-   Apăsați **F** or the **<img src="images/Draft_FinishLine.png" width=12px> '''Finish'''** button to finish the spline, leaving it open
-   Apăsați butonul **C** or the **<img src="images/Draft_CloseLine.png" width=12px> '''Close'''** sau click pe primul punct pentru a finaliza curba Spline, dar care o închid prin adăugarea unui ultim segment între ultimul punct și primul punct.
-   Apăsați tasta **X**, **Y** sau **Z** după un punct pentru a constrânge următorul punct de pe axa dată.
-   Pentru a introduce manual coordonatele, pur și simplu introduceți numerele, apoi apăsați **ENTER** între fiecare componentă X, Y și Z.
-   Apăsați tasta **R** sau click pe checkbox pentru a bifa/debifa butonul **'''Relative'''**.Dacă modul relativ este activ, coordonatele punctului următor sunt relativ la ultima. Dacă nu, ele sunt absolute, luate din punctul de origine (0,0,0).
-   Apăsați tasta **T** sau click pe checkbox pentru a bifa/debifa butonul **'''Continue'''**. Dacă modul continuare este activat, instrumentul BSpline se va reporni după finalizarea sau închiderea acestuia, permițându-vă să desenați altul fără să apăsați din nou butonul BSpline.
-   Apăsați tasta **CTRL** în timp ce desenați pentru a forța punctul [snapping](Draft_Snap/ro.md) punctul dvs. către cea mai apropiată locație, independent de distanța.
-   Apăsați tasta **SHIFT** în timp ce desenați [constrain](Draft_Constrain/ro.md) punct dvs următor orizontal sau vertical în relație cu ultimul .
-   Apăsați tasta **W** sau apăsați butonul **<img src="images/Draft_Wipe.png" width=12px> '''Wipe'''** pentru a șterge segmentele existente și să demarați funcția Spline de la ultimul punct.
-   Apăsați combinația de taste **CTRL**+**Z** sau apăsțai butonul **<img src="images/Draft_UndoLine.png" width=12px> '''Undo'''** de undo a ultimului punct.
-   Apăsați tasta **I** sau apăsați butonul **'''Filled'''** pentru a avea funcția spline umplută cu o fațetă după ce a fost închisă.
-   Apăsați tasta **ESC** sau tasta **'''Cancel'''** pentru a întrerupe comanda curentă BSpline.
-   Planele BS, atunci când sunt în modul de afișare \"Flat Lines\", pot afișa un model de hașurare, prin setarea proprietății \"Pattern\" de mai jos.


</div>

## Notes

-   A Draft BSpline can be edited with the [Draft Edit](Draft_Edit.md) command.
-   A Draft BSpline can be converted to a [Draft Wire](Draft_Wire.md) with the [Draft WireToBSpline](Draft_WireToBSpline.md) command.

## Preferences

See also   * [Preferences Editor](Preferences_Editor.md) and [Draft Preferences](Draft_Preferences.md).

-   To change the number of decimals used for the input of coordinates   * **Edit → Preferences... → General → Units → Units settings → Number of decimals**.
-   To change the initial value of filled mode   * **Edit → Preferences... → Draft → General settings → Draft tools options → Fill objects with faces whenever possible**. Changing the filled mode in a task panel will override this preference for the current FreeCAD session.


<div class="mw-translate-fuzzy">

## Proprietăți

-    {{PropertyData/ro|Closed}}   * Specifică dacă curba spline este închisă sau nu

-    {{PropertyData/ro|Make Face}}   * Umple curba spline cu o fațetă

-    {{PropertyView/ro|End Arrow}}   * Afișează un simbol tp săgeată la ultimul punct al curbei spline, astfel încât este folosit ca linie lider de adnotare

-    {{PropertyView/ro|Pattern}}   * Specificați modelul hașurii cu care se va umple filamentul

-    {{PropertyView/ro|Pattern Size}}   * Specificați mărimea modelului de hașurare


</div>

See also   * [Property editor](Property_editor.md).

A Draft BSpline object is derived from a [Part Part2DObject](Part_Part2DObject.md) and inherits all its properties. It also has the following additional properties   *

### Data


{{TitleProperty|Draft}}

-    **Area|Area**   * (read-only) specifies the area of the face of the spline. The value will be {{value|0.0}} if **Make Face** if `False` or the face cannot be created.

-    **Closed|Bool**   * specifies if the spline is closed or not. If the spline is initially open this value is `False`, setting it to `True` will draw a curve segment to close the spline. If the spline is initially closed this value is `True`, setting it to `False` will remove the last curve segment and make the spline open.

-    **Make Face|Bool**   * specifies if the spline makes a face or not. If it is `True` a face is created, otherwise only the perimeter is considered part of the object. This property only works if **Closed** is `True` and if the spline does not self-intersect.

-    **Parameterization|Float**   * affects the shape of the spline.

-    **Points|VectorList**   * specifies the points of the spline in its local coordinate system.

### View


{{TitleProperty|Draft}}

-    **Arrow Size|Length**   * specifies the size of the symbol displayed at the end of the spline.

-    **Arrow Type|Enumeration**   * specifies the type of symbol displayed at the end of the spline, which can be {{value|Dot}}, {{value|Circle}}, {{value|Arrow}}, {{value|Tick}} or {{value|Tick-2}}.

-    **End Arrow|Bool**   * specifies whether to show a symbol at the end of the spline, so it can be used as an annotation line.

-    **Pattern|Enumeration**   * specifies the [Draft Pattern](Draft_Pattern.md) with which to fill the face of the closed spline. This property only works if **Make Face** is `True` and if **Display Mode** is {{value|Flat Lines}}.

-    **Pattern Size|Float**   * specifies the size of the [Draft Pattern](Draft_Pattern.md).

## Scripting


<div class="mw-translate-fuzzy">

## Script-Programre 

Unealta BSpline poate fi folosită în [macro-uri](macros/ro.md) şi de la consola Python cu ajutorul funcţiei următoare   *


</div>

To create a Draft BSpline use the `make_bspline` method (<small>(v0.19)</small> ) of the Draft module. This method replaces the deprecated `makeBSpline` method.


```python
bspline = make_bspline(pointslist, closed=False, placement=None, face=None, support=None)
bspline = make_bspline(Part.Wire, closed=False, placement=None, face=None, support=None)
```


<div class="mw-translate-fuzzy">

-   Creează un obiect B-Spline din lista de vectori dați.
-   Dacă închis este True sau primul și ultimul pucnt sunt identice, filamentul este îchis.
-   Dacă face este True (și curba BSpline este închisă), Curba B spline va apărea ca fiind umplută.
-   În loc de o listă de puncte, puteți să mergeți și la conturul din Part Wire.
-   Returnează obiectul noi creat.


</div>


<div class="mw-translate-fuzzy">

Exempluː


</div>


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

p1 = App.Vector(0, 0, 0)
p2 = App.Vector(1000, 1000, 0)
p3 = App.Vector(2000, 0, 0)

spline1 = Draft.make_bspline([p1, p2, p3], closed=False)
spline2 = Draft.make_bspline([p1, 2*p3, 1.3*p2], closed=False)
spline3 = Draft.make_bspline([1.3*p3, p1, -1.7*p2], closed=False)

doc.recompute()
```



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft BSpline/ro
