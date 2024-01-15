---
 GuiCommand:
   Name: Draft BezCurve
   Name/es: Borrador BezCurva
   MenuLocation: Borrador , Herramientas Bézier , Curva Bézier
   Workbenches: Draft_Workbench/es, Arch_Workbench/es
   Version: 0.14
   SeeAlso: Draft_CubicBezCurve/es, Draft_BSpline/es
---

# Draft BezCurve/es


</div>



## Descripción


<div class="mw-translate-fuzzy">

El <img alt="" src=images/Draft_BezCurve.svg  style="width:24px;"> **Borrador BezCurva** comando crea una [Curva de Bézier](https://es.wikipedia.org/wiki/Curva_de_B%C3%A9zier) a partir de varios puntos.


</div>

El comando crea una única curva de Bézier con una **Degree** que es `number_of_points - 1`. Se puede transformar en una curva Bézier a trozos reduciendo esta propiedad.

Los comandos [Borrador CubicBezCurva](Draft_CubicBezCurve/es.md) utilizan **puntos de control** para definir la posición y la curvatura de la spline. El comando [Borrador BSpline](Draft_BSpline/es.md), en cambio, especifica los **puntos exactos** por los que pasará la curva

<img alt="" src=images/Draft_BezCurve_Example.png  style="width:400px;"> 
*Curva de Bézier definida por múltiples puntos*



## Utilización

Ver también: [Bandeja Borrador](Draft_Tray/es.md), [Borrador Atrapar](Draft_Snap/es.md) y [Borrador Restricción](Draft_Constrain/es.md).


<div class="mw-translate-fuzzy">

1.  Hay varias formas de invocar el comando:
    -   Pulsar el **<img src="images/Draft_BezCurve.svg" width=16px> [Borrador BezCurve](Draft_BezCurve/es.md)**.
    -   Seleccione la opción **Borrador → Herramientas Bézier → <img src="images/Draft_BezCurve.svg" width=16px> Curva Bézier** en el menú.
2.  Se abre el panel de tareas **Curva Bézier**. Ver [Opciones](#Opciones.md) para más información.
3.  Escoge el primer punto en la [Vista 3D](3D_view/es.md), o escribe las coordenadas y pulsa el **<img src="images/Draft_AddPoint.svg" width=16px> Introducir punto** botón.
4.  Escoge puntos adicionales en la [Vista 3D](3D_view/es.md), o escribe las coordenadas y pulsa el **<img src="images/Draft_AddPoint.svg" width=16px> Introducir punto** botón.
5.  Pulse **Esc** o el botón **Cerrar** para finalizar el comando.


</div>



## Opciones


<div class="mw-translate-fuzzy">

Los atajos de teclado de un solo carácter disponibles en el panel de tareas se pueden cambiar. Ver [Preferencias de Borrador](Draft_Preferences/rs.md). Los atajos mencionados aquí son los atajos por defecto.


</div>


<div class="mw-translate-fuzzy">

-   Para introducir manualmente las coordenadas introduzca el componente X, Y y Z, y pulse **Enter** después de cada una. O puede pulsar el **<img src="images/Draft_AddPoint.svg" width=16px> Introducir punto** cuando tenga los valores deseados. Es aconsejable mover el puntero fuera de la [Vista 3D](3D_view/es.md) antes de introducir las coordenadas.
-   Pulse **R** o haga clic en la casilla **Relative** para activar el modo relativo. Si el modo relativo está activado, las coordenadas son relativas al último punto, si está disponible, sino son relativas al origen del sistema de coordenadas.
-   Pulse **G** o haga clic en la casilla **Global** para activar el modo global. Si el modo global está activado, las coordenadas son relativas al sistema de coordenadas global, sino son relativas al sistema de coordenadas del [Plano de trabajo](Draft_SelectPlane/es.md). {{Version/es|0.20}}
-   Pulse **L** o haga clic en la casilla **Relleno** para activar el modo relleno. Si el modo de relleno está activado, la curva creada tendrá **Hacer Cara** establecido en `True` y tendrá una cara rellena, siempre y cuando esté cerrada y no se auto-intersecte. Tenga en cuenta que una curva que se auto-interseca con una cara no se mostrará correctamente, para tal curva **Hacer Cara** debe ser ajustado a `False`.
-   Pulse **T** o haga clic en la casilla **Continuar** para activar el modo de continuación. Si el modo de continuar está activado, el comando se reiniciará después de usar **<img src="images/Draft_FinishLine.svg" width=16px> Terminar** o **<img src="images/Draft_CloseLine.svg" width=16px> Cerrar**, o después de crear una curva cerrada ajustándose al primer punto de la curva, permitiéndole continuar creando curvas.
-   Pulse el **<img src="images/Draft_UndoLine.svg" width=16px> Deshacer** para deshacer el último punto. El atajo de teclado **Ctrl**+**Z** actualmente no funciona.
-   Pulse **A** o el botón **<img src="images/Draft_FinishLine.svg" width=16px> Finalizar** para terminar el comando y dejar la curva abierta.
-   Pulse **O** o el botón **<img src="images/Draft_CloseLine.svg" width=16px> Cerrar** para terminar el comando y cerrar la curva. También se puede crear una curva cerrada ajustándose al primer punto de la curva.
-   Pulse **W** o el botón **<img src="images/Draft_Wipe.svg" width=16px> Limpiar** para borrar los segmentos ya colocados, pero seguir trabajando desde el último punto.
-   Pulsar **U** o el **<img src="images/Draft_SelectPlane.svg" width=16px> [Fijar PT](Draft_SelectPlane/es.md)** para ajustar el plano de trabajo actual en la orientación definida por el último punto y el anterior.
-   Pulse **S** para activar o desactivar el [Borrador Atrapar](Draft_Snap/es.md).
-   Pulse **Esc** o el botón **Cerrar** para finalizar el comando.


</div>



## Notas

-   Un Borrador de Curva de Bézier puede ser editado con el comando [Borrador Edición](Draft_Edit/es.md).
-   OpenCascade, y por tanto FreeCAD, no soporta curvas Bézier de grados superiores a 25. Esto no debería ser un problema en la práctica, ya que la mayoría de los usuarios suelen utilizar curvas Bézier de grados 3 a 5.



## Propiedades


<div class="mw-translate-fuzzy">

Ver también: [Editor de propiedades](property_editor/es.md).


</div>

Un objeto Draft BezCurva deriva de un [Pieza2DObjeto](Part_Part2DObject/es.md) y hereda todas sus propiedades. También tiene las siguientes propiedades adicionales:



### Datos


{{TitleProperty|Borrador}}

-    **Area|Area**: (read-only) specifies the area of the face of the curve. The value will be {{value|0.0}} if **Make Face** if `False` or the face cannot be created.

-    **Closed|Bool**: specifies if the curve is closed or not. If the curve is initially open this value is `False`, setting it to `True` will draw a segment to close the curve. If the curve is initially closed this value is `True`, setting it to `False` will remove the last segment and make the curve open.

-    **Continuity|IntegerList**: (read-only) specifies the continuity of the curve.

-    **Degree|Integer**: specifies the degree of the curve.

-    **Length|Length**: (read-only) specifies the total length of the curve.

-    **Make Face|Bool**: specifies if the curve makes a face or not. If it is `True` a face is created, otherwise only the perimeter is considered part of the object. This property only works if **Closed** is `True` and if the curve does not self-intersect.

-    **Points|VectorList**: specifies the control points of the curve in its local coordinate system.



### Vistas


{{TitleProperty|Borrador}}

-    **Arrow Size|Length**: specifies the size of the symbol displayed at the end of the curve.

-    **Arrow Type|Enumeration**: specifies the type of symbol displayed at the end of the curve, which can be {{value|Dot}}, {{value|Circle}}, {{value|Arrow}}, {{value|Tick}} or {{value|Tick-2}}.

-    **End Arrow|Bool**: specifies whether to show a symbol at the end of the curve, so it can be used as an annotation line.

-    **Pattern|Enumeration**: specifies the [Draft Pattern](Draft_Pattern.md) with which to fill the face of the closed curve. This property only works if **Make Face** is `True` and if **Display Mode** is {{value|Flat Lines}}.

-    **Pattern Size|Float**: specifies the size of the [Draft Pattern](Draft_Pattern.md).



## Guión

Ver también: [Documentación de la API autogenerada](https://freecad.github.io/SourceDoc/) y [Fundamentos de FreeCAD Guión](FreeCAD_Scripting_Basics/es.md).

Para crear una Borrador Línea utilice el método `make_bezcurve` ({{Version/es|0.19}}) del módulo Borrador. Este método sustituye al método obsoleto `makeBezCurve`.


```python
bezcurve = make_bezcurve(pointslist, closed=False, placement=None, face=None, support=None, degree=None)
bezcurve = make_bezcurve(Part.Wire, closed=False, placement=None, face=None, support=None, degree=None)
```

-   Crea un objeto `bezcurve` con la lista de puntos dada, `pointslist`.
    -   Cada punto de la lista está definido por su `FreeCAD.Vector`, con unidades en milímetros.
    -   Alternativamente, la entrada puede ser un `Part.Wire`, del que se extraen los puntos.
-   Si `closed` es `True`, o si el primer y el último punto son idénticos, la curva está cerrada.
-   Si `placement` es `None` la curva se crea en el origen.
-   Si `face` es `True`, y la curva es cerrada, la curva formará una cara, es decir, aparecerá rellena.

Ejemplo:


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


<div class="mw-translate-fuzzy">





</div>



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft BezCurve/es
