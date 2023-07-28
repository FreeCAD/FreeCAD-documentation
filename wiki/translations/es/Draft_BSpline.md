---
- GuiCommand:/es
   Name:Draft BSpline
   Name/es:Borrador BSpline
   MenuLocation:Borrador → B-Spline 
   Workbenches:[Borrador](Draft_Workbench/es.md), [Arquitectura](Arch_Workbench/es.md)
   Shortcut:**B** **S**
   Version:0.7
   SeeAlso:[Borrador Hilo](Draft_Wire/es.md), [Borrador CúbicaBezCurva](Draft_CubicBezCurve/es.md), [Borrador BezCurva](Draft_BezCurve/es.md)
---

# Draft BSpline/es


</div>



## Descripción

El <img alt="" src=images/Draft_BSpline.svg  style="width:24px;"> comando **Borrador BSpline** crea una [curva B-spline](https://es.wikipedia.org/wiki/B-spline) a partir de varios puntos.

El comando Borrador BSpline especifica los **puntos exactos** por los que pasará la curva. Los comandos [Borrador BezCurva](Draft_BezCurve/es.md) y [Borrador CúbicaBezCurva](Draft_CubicBezCurve/es.md), por otro lado, utilizan **puntos de control** para definir la posición y la curvatura de la spline.

<img alt="" src=images/Draft_bspline_example.jpg  style="width:400px;"> 
*Spline definida por múltiples puntos*



## Utilización

Ver también: [Bandeja Borrador](Draft_Tray/es.md), [Borrador Atrapar](Draft_Snap/es.md) y [Borrador Restricción](Draft_Constrain/es.md).

1.  Hay varias formas de invocar el comando:
    -   Pulsar el **<img src="images/Draft_BSpline.svg" width=16px> [Borrador BSpline](Draft_BSpline/es.md)**.
    -   Seleccione la opción **Borrador → <img src="images/Draft_BSpline.svg" width=16px> B-spline** en el menú.
    -   Utilice el atajo de teclado: **B** y luego **S**.
2.  Se abre el panel de tareas **B-spline**. Ver [Opciones](#Opciones.md) para más información.
3.  Elige el primer punto en la [Vista 3D](3D_view/es.md), o escribe las coordenadas y pulsa el **<img src="images/Draft_AddPoint.svg" width=16px> Introducir punto** botón.
4.  Elige puntos adicionales en la [Vista 3D](3D_view/es.md), o escribe las coordenadas y pulsa el botón **<img src="images/Draft_AddPoint.svg" width=16px> Introducir punto** botón.
5.  Pulse **Esc** o el botón **Cerrar** para finalizar el comando.



## Opciones

Los atajos de teclado de un solo carácter disponibles en el panel de tareas se pueden cambiar. Ver [Preferencias de Borrador](Draft_Preferences/rs.md). Los atajos mencionados aquí son los atajos por defecto.


<div class="mw-translate-fuzzy">

-   Para introducir manualmente las coordenadas introduzca el componente X, Y y Z, y pulse **Enter** después de cada una. O puede pulsar el **<img src="images/Draft_AddPoint.svg" width=16px> Introducir punto** cuando tenga los valores deseados. Es aconsejable mover el puntero fuera de la [Vista 3D](3D_view/es.md) antes de introducir las coordenadas.
-   Pulse **R** o haga clic en la casilla **Relative** para activar el modo relativo. Si el modo relativo está activado, las coordenadas son relativas al último punto, si está disponible, sino son relativas al origen del sistema de coordenadas.
-   Pulse **G** o haga clic en la casilla **Global** para activar el modo global. Si el modo global está activado, las coordenadas son relativas al sistema de coordenadas global, sino son relativas al sistema de coordenadas del [plano de trabajo](Draft_SelectPlane/es.md). {{Version/es|0.20}}
-   Pulse **L** o haga clic en la casilla **Filled** para activar el modo relleno. Si el modo de relleno está activado, la spline creada tendrá **Make Face** establecida en `True` y tendrá una cara rellena, siempre y cuando esté cerrada y no se auto-intersecte. Tenga en cuenta que una spline que se auto-interseque con una cara no se mostrará correctamente, para tal spline **Make Face** debe establecerse en `False`.
-   Pulse **T** o haga clic en la casilla **Continue** para activar el modo de continuación. Si el modo de continuar está activado, el comando se reiniciará después de usar **<img src="images/Draft_FinishLine.svg" width=16px> Terminar** o **<img src="images/Draft_CloseLine.svg" width=16px> Cerrar**, o después de crear una spline cerrada ajustándose al primer punto de la spline, permitiéndole continuar creando splines.
-   Pulsar el **<img src="images/Draft_UndoLine.svg" width=16px> Deshacer** para deshacer el último punto. El atajo de teclado **Ctrl**+**Z** actualmente no funciona.
-   Pulse **A** o el botón **<img src="images/Draft_FinishLine.svg" width=16px> Finalizar** para terminar el comando y dejar la spline abierta.
-   Pulsar **O** o el botón **<img src="images/Draft_CloseLine.svg" width=16px> Cerrar** para terminar el comando y cerrar la spline. También se puede crear una spline cerrada ajustándose al primer punto de la spline.
-   Pulse **W** o el botón **<img src="images/Draft_Wipe.svg" width=16px> Limpiar** para borrar los segmentos de la curva ya colocados, pero seguir trabajando desde el último punto.
-   Pulsar **U** o el **<img src="images/Draft_SelectPlane.svg" width=16px> [Ajustar el plano de trabajo](Draft_SelectPlane/es.md)** para ajustar el plano de trabajo actual en la orientación definida por el último punto y el anterior.
-   Pulsar **S** para activar o desactivar el [Borrador](Draft_Snap.md).
-   Pulse **Esc** o el botón {{button|Close}} para finalizar el comando.


</div>



## Notas

-   Un Borrador BSpline puede ser editado con el comando [Borrador Edición](Draft_Edit/es.md).
-   Un Borrador BSpline puede convertirse en un [Borrador Hilo](Draft_Wire/es.md) con el comando [Borrador HiloABSpline](Draft_WireToBSpline/es.md).



## Preferencias

Ver también: [Editor de preferencias](Preferences_Editor/es.md) y [Borrador Preferencias](Draft_Preferences/es.md).

-   Para cambiar el número de decimales utilizados para la entrada de coordenadas: **Edición → Preferencias... → General → Unidades → Configuración de unidades → Número de decimales**.
-   Para cambiar el valor inicial del modo relleno: **Edición → Preferencias... → Borrador → Ajustes generales → Borrador Opciones de las herramientas → Rellenar objetos con caras siempre que sea posible**. Cambiar el modo de relleno en un panel de tareas anulará esta preferencia para la sesión actual de FreeCAD.



## Propiedades


<div class="mw-translate-fuzzy">

Ver también: [Editor de propiedades](property_editor/es.md).


</div>

Un objeto Borrador BSpline deriva de un [Pieza2DObjeto](Part_Part2DObject/es.md) y hereda todas sus propiedades. También tiene las siguientes propiedades adicionales:



### Datos


{{TitleProperty|Draft}}

-    **Area|Area**: (read-only) specifies the area of the face of the spline. The value will be {{value|0.0}} if **Make Face** if `False` or the face cannot be created.

-    **Closed|Bool**: specifies if the spline is closed or not. If the spline is initially open this value is `False`, setting it to `True` will draw a curve segment to close the spline. If the spline is initially closed this value is `True`, setting it to `False` will remove the last curve segment and make the spline open.

-    **Make Face|Bool**: specifies if the spline makes a face or not. If it is `True` a face is created, otherwise only the perimeter is considered part of the object. This property only works if **Closed** is `True` and if the spline does not self-intersect.

-    **Parameterization|Float**: affects the shape of the spline.

-    **Points|VectorList**: specifies the points of the spline in its local coordinate system.



### Vista


{{TitleProperty|Draft}}

-    **Arrow Size|Length**: specifies the size of the symbol displayed at the end of the spline.

-    **Arrow Type|Enumeration**: specifies the type of symbol displayed at the end of the spline, which can be {{value|Dot}}, {{value|Circle}}, {{value|Arrow}}, {{value|Tick}} or {{value|Tick-2}}.

-    **End Arrow|Bool**: specifies whether to show a symbol at the end of the spline, so it can be used as an annotation line.

-    **Pattern|Enumeration**: specifies the [Draft Pattern](Draft_Pattern.md) with which to fill the face of the closed spline. This property only works if **Make Face** is `True` and if **Display Mode** is {{value|Flat Lines}}.

-    **Pattern Size|Float**: specifies the size of the [Draft Pattern](Draft_Pattern.md).



## Guión

Ver también: [Documentación de la API autogenerada](https://freecad.github.io/SourceDoc/) y [Fundamentos de FreeCAD Guión](FreeCAD_Scripting_Basics/es.md).

Para crear una Borrador BSpline utilice el método `make_bspline` ({{Version/es|0.19}}) del módulo Borrador. Este método sustituye al método obsoleto `makeBSpline`.


```python
bspline = make_bspline(pointslist, closed=False, placement=None, face=None, support=None)
bspline = make_bspline(Part.Wire, closed=False, placement=None, face=None, support=None)
```

-   Crea un objeto `bspline` con la lista de puntos dada, `pointslist`.
    -   Cada punto de la lista está definido por su `FreeCAD.Vector`, con unidades en milímetros.
    -   Alternativamente, la entrada puede ser un `Part.Wire`, del que se extraen los puntos.
-   Si `closed` es `True`, o si el primer y el último punto son idénticos, la spline está cerrada.
-   Si `placement` es `None` la spline se crea en el origen.
-   Si `face` es `True`, y la spline está cerrada, la spline hará una cara, es decir, aparecerá rellena.

Ejemplo:


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


<div class="mw-translate-fuzzy">





</div>



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft BSpline/es
