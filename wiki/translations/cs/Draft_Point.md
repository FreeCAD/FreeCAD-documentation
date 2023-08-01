# Draft Point/cs
---
- GuiCommand:   Name:Draft Point   Name/cs:Kreslení Bod   Workbenches:[Architektura](Draft_Workbench/cs___Kreslení]],_[[Arch_Workbench/cs.md)|MenuLocation:Kreslení -> Bod   Shortcut:P T---


</div>



## Popis


<div class="mw-translate-fuzzy">

Nástroj Bod vytváří jednoduchý bod v aktuální [pracovní rovině](Draft_SelectPlane/cs.md), užitečný jako referenční bod pro umisťování dalších objektů. Přebírá [barvu](Draft_Linestyle/cs.md) předem nastavenou v záložce Úkoly.


</div>

<img alt="" src=images/Draft_point_example.jpg  style="width:400px;">




<div class="mw-translate-fuzzy">

## Použití


</div>

See also: [Draft Tray](Draft_Tray.md), [Draft Snap](Draft_Snap.md) and [Draft Constrain](Draft_Constrain.md).


<div class="mw-translate-fuzzy">

1.  Stiskněte tlačítko **<img src="images/Draft_Point.png" width=16px> [Kreslení Bod](Draft_Point/cs.md)
** nebo klávesy **P** potom **T**
2.  Klikněte na bod ve 3D pohledu nebo zadejte souřadnice


</div>



## Volby

The single character keyboard shortcuts available in the task panel can be changed. See [Draft Preferences](Draft_Preferences.md). The shortcuts mentioned here are the default shortcuts.


<div class="mw-translate-fuzzy">

-   Chcete-li zadat souřadnice ručně jednoduše zadejte číslo a potom stiskněte **ENTER** mezi každou z komponent X, Y a Z.
-   Stisknutím tlačítka **ESC** nebo **'''Zrušit'''** zrušíte právě probíhající příkaz.


</div>

## Notes

-   Use <img alt="" src=images/Draft_Snap_Near.svg  style="width:16px;"> [Draft Snap Near](Draft_Snap_Near.md) ({{VersionMinus|0.20}}) or <img alt="" src=images/Draft_Snap_Endpoint.svg  style="width:16px;"> [Draft Snap Endpoint](Draft_Snap_Endpoint.md) (<small>(v0.21)</small> ) to snap to Draft points.

## Preferences

See also: [Preferences Editor](Preferences_Editor.md) and [Draft Preferences](Draft_Preferences.md).

-   To change the number of decimals used for the input of coordinates: **Edit → Preferences... → General → Units → Units settings → Number of decimals**.



## Vlastnosti

See also: [Property editor](Property_editor.md).

A Draft Point object is derived from a [Part Feature](Part_Feature.md) object and inherits all its properties. It also has the following additional properties:

### Data


{{TitleProperty|Draft}}


<div class="mw-translate-fuzzy">

-    **X**: X souřadnice bodu

-    **Y**: Y souřadnice bodu

-    **Z**: Z souřadnice bodu


</div>

### View


{{TitleProperty|Draft}}

-    **Pattern|Enumeration**: not used.

-    **Pattern Size|Float**: not used.

## Scripting


<div class="mw-translate-fuzzy">

## Skriptování


</div>


<div class="mw-translate-fuzzy">

Nástroj Bod může být využit v [makrech](macros.md) a z konzoly Pythonu použitím následující funkce:


</div>


```python
point = make_point(X=0, Y=0, Z=0, color=None, name="Point", point_size=5)
point = make_point(point, Y=0, Z=0, color=None, name="Point", point_size=5)
```


<div class="mw-translate-fuzzy">

-   Vytvoří bod na zadaných souřadnicích. Není-li zadána žádná ze souřadnic X, Y, Z, bude bod vytvořen na souřadnicích (0,0,0). Vrací nově vytvořený objekt.


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

Příklad:

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
![](images/Button_right.svg) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Point/cs
