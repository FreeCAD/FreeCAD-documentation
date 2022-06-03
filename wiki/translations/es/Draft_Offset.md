---
- GuiCommand   */es
   Name   *Draft Offset
   Name/es   *Draft Offset
   MenuLocation   *Croquis → Equidistancia
   Workbenches   *[Croquis](Draft_Workbench/es.md), [Arquitectura](Arch_Workbench/es.md)
   Shortcut   ***O** **S**
   SeeAlso   *[Part 2D Offset](Part_Offset2D/es.md)
---

# Draft Offset/es


</div>

## Descripción


<div class="mw-translate-fuzzy">

La herramienta Equidistancia crea una equidistacia de los objetos seleccionados a una distancia dada sobre el [plano de trabajo](Draft_SelectPlane/es.md) actual. Si no se han seleccionado objetos, te invitará a seleccionar uno. Simplemente te pregunta por un punto, dando la distancia de la equidistancia de los objetos seleccionados.


</div>

<img alt="" src=images/Draft_Offset_example.jpg  style="width   *400px;"> 
*Offsetting a Draft Wire*


<div class="mw-translate-fuzzy">

## Utilización


</div>

See also   * [Draft Snap](Draft_Snap.md) and [Draft Constrain](Draft_Constrain.md).


<div class="mw-translate-fuzzy">

1.  Selecciona los objetos a los que quieras crear una equidistancia
2.  Presiona el botón **<img src="images/Draft_Offset.png" width=16px> [Equidistancia](Draft_Offset/es.md)
**, o presiona las teclas **O** y **S**
3.  Designa un punto en la vista 3D, o escribe una distancia


</div>

## Opciones

The single character keyboard shortcuts and the modifier keys mentioned here can be changed. See [Draft Preferences](Draft_Preferences.md).


<div class="mw-translate-fuzzy">

-   Presiona **T** o selecciona la casilla para activar/desactivar el botón **'''Continuar'''**. Si el modo continuar está activado, la herramienta equidistancia se reiniciará al terminar permitiendo hacer otra equidistancia o copiar objetos de nuevo sin necesidad de volver a presionar el botón de equidistancia.
-   Presionando **ALT** o **C** o seleccionando el botón **'''Copiar'''** se creará una copia de los objetos, en lugar de moverlos. Si mantienes presionada la tecla **ALT** después de seleccionar el segundo punto, podrás hacer más copias, hasta que liberes la tecla **ALT**.
-   Presiona **CTRL** mientras dibujas para forzar el [ajuste](Draft_Snap/es.md) de tu punto a la posición de ajuste más cercana, independientemente de la distancia.
-   Presionando **SHIFT** se [restringirá](Draft_Constrain/es.md) al segmento actual en lugar de seleccionar el más cercano.
-   Presiona **ESC** o el botón **'''Cancelar'''** para abortar el comando actual.


</div>

## Notes

-   To create an offset version of a [Draft BSpline](Draft_BSpline.md) its points are offset individually, and from the new points a new spline is calculated. This new spline is not parallel to the original spline. For an exact parallel offset of a [Draft BSpline](Draft_BSpline.md) the [Part Offset2D](Part_Offset2D.md) command should be used.
-   The Draft Offset command cannot handle [Draft BezCurves](Draft_BezCurve.md). Use the [Part Offset2D](Part_Offset2D.md) command instead.

## Preferences

See also   * [Preferences Editor](Preferences_Editor.md) and [Draft Preferences](Draft_Preferences.md).

-   To change the number of decimals used for the input of the distance   * **Edit → Preferences... → General → Units → Units settings → Number of decimals**.

## Scripting


<div class="mw-translate-fuzzy">

## Programación


</div>


<div class="mw-translate-fuzzy">

La herramienta Equidistancia se puede utilizar en [macros](macros/es.md) y desde la consola de Python utilizando la siguiente función   *


</div>


```python
offset_obj = offset(obj, delta, copy=False, bind=False, sym=False, occ=False)
```


<div class="mw-translate-fuzzy">

-   Crea una equidistancia del contorno dado aplicando el vector indicado a su primer vértice.
-   Si copymode es True, se crea otro objeto, en otro caso es el mismo objeto el que se equidistancia. Si bind es True, y el contorno dado está abierto, el original y el contorno equidistante estarán enlazados por sus puntos finales, creando una cara.
-   Si sym es True, la equidistancia se crea hacia ambos lados, siendo el ancho total la longitud del vector dado.
-   Devuelve el objeto equidistante (o su copia si copymode es True).


</div>

Ejemplo   *


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

p1 = App.Vector(0, 0, 0)
p2 = App.Vector(1500, 2000, 0)
p3 = App.Vector(4000, 0, 0)

wire = Draft.make_wire([p1, p2, p3])
doc.recompute()

vector = App.Vector(-200, 150, 0)
offset1 = Draft.offset(wire, vector, copy=True, bind=True, sym=True)
offset2 = Draft.offset(wire, 3*vector, copy=True)
offset3 = Draft.offset(wire, 6*vector, copy=True)
offset4 = Draft.offset(wire, 9*vector, copy=True)
offset5 = Draft.offset(wire, 1.5*vector, copy=True, occ=True)

doc.recompute()
```



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Offset/es
