---
- GuiCommand:
   Name: Draft Point
   Name/es: Draft Point
   MenuLocation: Boceto -> Punto
   Workbenches: Draft_Workbench/es, Arch_Workbench/es
   Shortcut: P T
---

# Draft Point/es


</div>



## Descripción


<div class="mw-translate-fuzzy">

La herramienta punto crea un punto simple en el [plano de trabajo](Draft_SelectPlane/es.md) actual, útil para servir como referencia para ubicar otros objetos después. Toma el [color](Draft_Linestyle/es.md) previamente establecido en la pestaña de tareas.


</div>

<img alt="" src=images/Draft_point_example.jpg  style="width:400px;">




<div class="mw-translate-fuzzy">

## Utilización


</div>

See also: [Draft Tray](Draft_Tray.md), [Draft Snap](Draft_Snap.md) and [Draft Constrain](Draft_Constrain.md).


<div class="mw-translate-fuzzy">

1.  Presiona el botón **<img src="images/Draft_Point.png" width=16px> [punto](Draft_Point/es.md)
**, o presiona las teclas **P** y **T**
2.  Designa un punto en la vista 3D, o escribe unas coordenadas coordenadas


</div>



## Opciones

The single character keyboard shortcuts available in the task panel can be changed. See [Draft Preferences](Draft_Preferences.md). The shortcuts mentioned here are the default shortcuts.


<div class="mw-translate-fuzzy">

-   Para introducir coordenadas manualmente, simplemente introduce los números, y presiona **ENTER** entre cada componente X, Y y Z.
-   Presiona **ESC** o el botón **'''Cancelar'''** para evitar el comando actual.


</div>

## Notes

-   Use <img alt="" src=images/Draft_Snap_Near.svg  style="width:16px;"> [Draft Snap Near](Draft_Snap_Near.md) ({{VersionMinus|0.20}}) or <img alt="" src=images/Draft_Snap_Endpoint.svg  style="width:16px;"> [Draft Snap Endpoint](Draft_Snap_Endpoint.md) (<small>(v0.21)</small> ) to snap to Draft points.

## Preferences

See also: [Preferences Editor](Preferences_Editor.md) and [Draft Preferences](Draft_Preferences.md).

-   To change the number of decimals used for the input of coordinates: **Edit → Preferences... → General → Units → Units settings → Number of decimals**.



## Propiedades

See also: [Property editor](Property_editor.md).

A Draft Point object is derived from a [Part Feature](Part_Feature.md) object and inherits all its properties. It also has the following additional properties:

### Data


{{TitleProperty|Draft}}


<div class="mw-translate-fuzzy">

-    **X**: La coordenada X del punto

-    **Y**: La coordenada Y del punto

-    **Z**: La coordenada Z del punto


</div>

### View


{{TitleProperty|Draft}}

-    **Pattern|Enumeration**: not used.

-    **Pattern Size|Float**: not used.

## Scripting


<div class="mw-translate-fuzzy">

## Archivos de guión 


</div>


<div class="mw-translate-fuzzy">

La herramienta punto se puede utilizar en [macros](macros/es.md) y desde la consola Python utilizando la siguiente función:


</div>


```python
point = make_point(X=0, Y=0, Z=0, color=None, name="Point", point_size=5)
point = make_point(point, Y=0, Z=0, color=None, name="Point", point_size=5)
```


<div class="mw-translate-fuzzy">

-   crea un punto en las coordenadas indicadas. Si no se indican las coordenadas X, Y y Z, el punto se creará en el origen de coordenadas (0,0,0). Devuelve el objeto recién creado.


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

Example:

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
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Point/es
