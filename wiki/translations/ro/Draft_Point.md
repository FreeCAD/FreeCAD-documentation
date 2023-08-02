---
- GuiCommand:
   Name: Draft Point
   Name/ro: Draft Punctul
   Workbenches: Draft_Workbench/ro, Arch_Workbench/ro
   MenuLocation: Draft -> Point
   Shortcut: P T
---

# Draft Point/ro


</div>



## Descriere


<div class="mw-translate-fuzzy">

Instrumentul Punct creează un punct simplu în planul curent [work plane](Draft_SelectPlane/ro.md), util pentru a servi ca referință pentru plasarea mai multor obiecte mai târziu. Este nevoie de [color](Draft_Linestyle/ro.md) setat anterior pe fila Activități.


</div>

<img alt="" src=images/Draft_point_example.jpg  style="width:400px;">




<div class="mw-translate-fuzzy">

## Cum se folosește 


</div>

See also: [Draft Tray](Draft_Tray.md), [Draft Snap](Draft_Snap.md) and [Draft Constrain](Draft_Constrain.md).


<div class="mw-translate-fuzzy">

1.  Apăsați butonul **<img src="images/Draft_Point.png" width=16px> [Draft Point](Draft_Point/ro.md)
**, sau apăsați tasta **P** apoi apăsați tasta **T**
2.  Click un punct în vizualizarea 3D, sau tastați coordinate


</div>



## Opţiuni

The single character keyboard shortcuts available in the task panel can be changed. See [Draft Preferences](Draft_Preferences.md). The shortcuts mentioned here are the default shortcuts.


<div class="mw-translate-fuzzy">

-   Petru a introduce coordonatele manual, pur și simplu introduceți numerele, apoi apăsați tasta **ENTER** între fiecare componentă pe X, Y și Z .
-   Apăsați tasta **ESC** sau butonul **'''Cancel'''** pentru a abandona linia de comandă curentă.


</div>

## Notes

-   Use <img alt="" src=images/Draft_Snap_Near.svg  style="width:16px;"> [Draft Snap Near](Draft_Snap_Near.md) ({{VersionMinus|0.20}}) or <img alt="" src=images/Draft_Snap_Endpoint.svg  style="width:16px;"> [Draft Snap Endpoint](Draft_Snap_Endpoint.md) (<small>(v0.21)</small> ) to snap to Draft points.

## Preferences

See also: [Preferences Editor](Preferences_Editor.md) and [Draft Preferences](Draft_Preferences.md).

-   To change the number of decimals used for the input of coordinates: **Edit → Preferences... → General → Units → Units settings → Number of decimals**.



## Proprietăți

See also: [Property editor](Property_editor.md).

A Draft Point object is derived from a [Part Feature](Part_Feature.md) object and inherits all its properties. It also has the following additional properties:

### Data


{{TitleProperty|Draft}}


<div class="mw-translate-fuzzy">

-    {{PropertyData/ro|X}}: Coordonatele X ale punctului

-    {{PropertyData/ro|Y}}: Coordonatele Y ale punctului

-    {{PropertyData/ro|Z}}: Coordonatele Z ale punctului


</div>

### View


{{TitleProperty|Draft}}

-    **Pattern|Enumeration**: not used.

-    **Pattern Size|Float**: not used.

## Scripting


<div class="mw-translate-fuzzy">

## Scrip-Programare 


</div>


<div class="mw-translate-fuzzy">

Instrumentul Point poate fi utilizat în [macros](macros/ro.md) și de la consola Python folosind următoarea funcție:


</div>


```python
point = make_point(X=0, Y=0, Z=0, color=None, name="Point", point_size=5)
point = make_point(point, Y=0, Z=0, color=None, name="Point", point_size=5)
```


<div class="mw-translate-fuzzy">

-   creează un punct la coordonatele date. Dacă nu sunt date coordonate X, Y și Z, punctul este creat la (0,0,0). Returnează obiectul nou creat. \"


</div>

Example:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

point1 = Draft.make_point(1600, 1400, 0)

p2 = App.Vector(-3200, 1800, 0)
point2 = Draft.make_point(p2, color=(0.5, 0.3, 0.6), point_size=10)

doc.recompute()
```

Exempluː

This code creates `N` random points within a square of side `2L`. It makes a loop creating `N` points, that may appear anywhere from `-L` to `+L` on both X and Y. It also chooses a random color and size for each point. Change `N` to change the number of points, and change `L` to change the area covered by the points.


```python
import random
import FreeCAD as App
import Draft

doc = App.newDocument()

L = 1000
centered = App.Placement(App.Vector(-L, -L, 0), App.Rotation())
rectangle = Draft.make_rectangle(2*L, 2*L, placement=centered)

N = 10
for i in range(N):
    x = 2*L*random.random() - L
    y = 2*L*random.random() - L
    z = 0
    r = random.random()
    g = random.random()
    b = random.random()
    size = 15*random.random() + 5
    Draft.make_point(x, y, z, color=(r, g, b), point_size=size)

doc.recompute()
```



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Point/ro
