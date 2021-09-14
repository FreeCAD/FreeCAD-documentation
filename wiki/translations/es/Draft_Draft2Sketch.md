---
- GuiCommand:/es
   Name:Draft_Draft2Sketch
   Name/es:Boceto a Croquis
   MenuLocation:Modificación → Borador a Croquis
   Workbenches:[Boceto](Draft_Workbench/es.md), [Arquitectura](Arch_Workbench/es.md)
---


</div>

## Descripción

El <img alt="" src=images/Draft_Draft2Sketch.svg  style="width:24px;"> comando **Borrador BorradorACroquis** convierte los objetos de Borrador en [Croquizador Croquis](Sketcher_NewSketch/es.md) y viceversa.

![](images/Draft_Draft2Sketch_example.png ) *Convertir objetos de borrador en Croquizador Croquis*

## Utilización

1.  Opcionalmente selecciona uno o más objetos de Borrador o [Croquizador Croquis](Sketcher_NewSketch/es.md).
2.  Hay varias formas de invocar el comando:
    -   Pulsar el **<img src="images/Draft_Draft2Sketch.svg" width=16px> [Borrador BorradorACroquis](Draft_Draft2Sketch/es.md)**.
    -   Seleccione la opción **Modificación → <img src="images/Draft_Draft2Sketch.svg" width=16px> Borrador a Croquis** en el menú.
3.  Si aún no ha seleccionado un objeto: seleccione un objeto en la [Vista 3D](3D_view/es.md).
4.  Se crea un nuevo objeto.

## Notas

-   Objetos que no son de borrador que son totalmente planas también se pueden convertir.
-   El comando sólo puede manejar objetos formados por **líneas rectas, arcos circulares, arcos elípticos, B-Splines y curvas de Bézier**.
-   [Borrador BezCurvas](Draft_BezCurve/es.md) será aproximado por [Croquizador BSplines](Sketcher_CreateBSpline/es.md).
-   El [Ambiente de trabajo KicadStepUp](KicadStepUp_Workbench/es.md) externo contiene un comando para convertir un [Borrador BSpline](Draft_BSpline/es.md) en una serie de [Coquizador Arcos](Sketcher_CreateArc/es.md). Para más información vea el tema del foro [BSplines to Shape2DView and Sketcher](https://forum.freecadweb.org/viewtopic.php?f=9&t=25082).
-   [Este otro tema del foro](https://forum.freecadweb.org/viewtopic.php?f=3&t=58781#p505207) contiene una macro para dicha conversión.

## Guión

Ver también: [Documentación de la API autogenerada](https://freecad.github.io/SourceDoc/) y [Fundamentos de FreeCAD Guión](FreeCAD_Scripting_Basics/es.md).

Para convertir objetos en un croquis utilice el método `make_sketch` ({{Version/es|0.19}}) del módulo Borrador. Este método sustituye al método obsoleto `makeSketch`.


```python
sketch = make_sketch(objects_list, autoconstraints=False, addTo=None, delete=False, name="Sketch", radiusPrecision=-1, tol=1e-3)
```

-    `objects_list`contiene los objetos a convertir. Puede ser un solo objeto o una lista de objetos. Se admiten objetos `Draft`, objetos `Part::Feature` y objetos `Part.Shape`.

-   Si `autoconstraints` es `True` se añaden restricciones coincidentes a los nodos que pertenecen al mismo objeto fuente.

-    `addTo`es el objeto de coquis existente al que se añade la geometría. Si no se proporciona, se crea un nuevo croquis.

-   Si `delete` es `True` se eliminan los objetos fuente.

-    `name`es el nombre del nuevo croquis.

-    `radiusPrecision`indica cómo deben manejarse las restricciones de radio:

    -   Utilice `-1` para desactivar las restricciones de radio.
    -   Utilice `0` para añadir restricciones de radio individuales.
    -   Utilice un número positivo para redondear los radios según esta precisión, y para añadir restricciones iguales entre curvas con radios iguales.

-    `tol`es la tolerancia utilizada para comprobar si las formas son planas y coplanares. Utilice `-1` para un análisis estricto.

-    `sketch`se devuelve con el objeto de croquis.

Para convertir un coquis en objetos Borrador utiliza el método `draftify` del módulo Borrador.


```python
draftify(objectslist, makeblock=False, delete=True)
```

-    `objectslist`contiene los objetos a convertir. Puede ser un solo objeto o una lista de objetos.

-   Si `makeblock` es `True` los objetos convertidos se agrupan en un `Part::Part2DObject`.

-   Si `delete` es `True` se borran los objetos de origen.

Ejemplo:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

rectangle = Draft.make_rectangle(2000, 1000)
circle = Draft.make_circle(500)
doc.recompute()

sketch_from_draft = Draft.make_sketch([rectangle, circle], autoconstraints=True, delete=False, radiusPrecision=0)
doc.recompute()

draft_from_sketch = Draft.draftify(sketch_from_draft, delete=False)
doc.recompute()
```


<div class="mw-translate-fuzzy">





</div>


 
