---
 GuiCommand:
   Name: Draft Wire
   Name/es: Draft Wire
   MenuLocation: Croquis -> Polilínea
   Workbenches: Draft_Workbench/es, Arch_Workbench/es
   Shortcut: **P** **L**
   Version: 0.7
   SeeAlso: Draft Line/es, Draft BSpline/es
---

# Draft Wire/es


</div>

## Description


<div class="mw-translate-fuzzy">

#### Descripción

La herramienta Contorno crea polilíneas (secuencias de líneas formadas por varios segmentos) en el [plano de trabajo](Draft_SelectPlane/es.md) actual. Toma el [Espesor de línea y color](Draft_Linestyle/es.md) previamente definidos en la pestaña de tareas. La herramienta Contorno se comporta como la herramienta [Línea](Draft_Line/es.md), con la excepción de que no termina tras indicar dos puntos.


</div>

The corners of a Draft Wire can be filleted (rounded) or chamfered by changing its **Fillet Radius** or **Chamfer Size** respectively. It is also possible to subdivide the edges of a Draft Wire by changing its **Subdivisions** property.

<img alt="" src=images/Draft_Polyline_example.jpg  style="width:400px;">


<div class="mw-translate-fuzzy">

<img alt="" src=images/Draft_Polyline_example.jpg  style="width:400px;">


</div>

## Create

### Usage

See also: [Draft Tray](Draft_Tray.md), [Draft Snap](Draft_Snap.md) and [Draft Constrain](Draft_Constrain.md).


<div class="mw-translate-fuzzy">

#### Utilización

1.  Presiona el botón **<img src="images/Draft_Wire.png" width=16px> [Contorno](Draft_Wire/es.md)
**, o presiona las teclas **W** y **I**
2.  Selecciona un primer punto en la vista 3D, o escribe unas coordenadas
3.  Selecciona puntos adicionales en la vista 3D, o escribe coordenadas
4.  Presiona **F** o **C**, o haz doble clic en el último punto, o selecciona el primer punto para terminar o cerrar el contorno. Si el contorno es cerrado, también será una cara, aunque su apariencia sea alámbrica.


</div>

### Options

The single character keyboard shortcuts available in the task panel can be changed. See [Draft Preferences](Draft_Preferences.md). The shortcuts mentioned here are the default shortcuts (for version 1.0).


<div class="mw-translate-fuzzy">

## Opciones

-   Si se seleccionan [ Draft Lineas](Draft_Line/es.md) conectadas al presionar el botón **Draft Wire**, se convertirán en un Wire y el comando terminara. {{Version | 0.17}}
-   Presiona **F** o el botón **<img src="images/Draft_FinishLine.png" width=12px> '''Terminar'''** para finalizar el contorno, dejándolo abierto
-   Presiona **C** o el botón **<img src="images/Draft_CloseLine.png" width=12px> '''Cerrar'''** o selecciona el primer punto para finalizar el contorno, pero haciendo que se cierre añadiendo un último segmento entre el último punto y el primero.
-   Presiona **X**, **Y** o **Z** después de un punto para restringir el siguiente punto con respecto al eje dado.
-   Para introducir coordenadas manualmente, simplemente introduce los números, presiona **ENTER** entre cada componente X, Y y Z.
-   Presiona **R** o selecciona la casilla para activar / desactivar el modo **'''Relativo'''**. Si está activado el modo relativo, las coordenadas del siguiente punto son relativas al anterior. En caso contrario, son absolutas, desde el origen de coordenadas (0,0,0).
-   Presiona **T** o selecciona la casilla para activar / desactivar el modo **'''Continuo'''**. Si está activado el modo continuo, la herramienta Contorno se iniciará después de que termines o cierres el contorno actual, permitiendo que dibujes otro contorno sin necesidad de pulsar el botón de Contorno otra vez.
-   Presiona **CTRL** mientras dibujas para forzar el [ajuste](Draft_Snap/es.md) del punto a la ubicación de ajuste más cercana, independientemente de la distancia.
-   Presiona **SHIFT** mientras dibujas para [restringir](Draft_Constrain/es.md) tu siguiente punto horizontal o verticalmente en relación al último punto indicado.
-   Presiona **W** o el botón **<img src="images/Draft_Wipe.png" width=12px> '''Contorno'''** para eliminar el segmento existente y comenzar el contorno desde el último punto.
-   Presiona **CTRL**+**Z** o el botón **<img src="images/Draft_UndoLine.png" width=12px> '''Deshacer'''** para deshacer el último punto.
-   Presiona **I** o el botón **'''Relleno'''** para que el Wire se muestre como una cara si esta cerrada.
-   Presiona **ESC** o el botón **'''Cancelar'''** para abortar el comando Línea actual.
-   Los Wires cerrados, cuando están en el modo de visualización \"Líneas planas\", pueden mostrar un patrón de sombreado, configurando a continuación la propiedad \"Patrón\".


</div>

## Join

### Usage 

1.  The end points of the [Draft Lines](Draft_Line.md) and/or Draft Wires to be joined must be exactly coincident. If required first adjust points to ensure that this is the case.
2.  Select two or more [Draft Lines](Draft_Line.md) and/or Draft Wires.
3.  There are several ways to invoke the command:
    -   Press the **<img src="images/Draft_Wire.svg" width=16px> [Draft Wire](Draft_Wire.md)** button.
    -   Select the **Drafting → <img src="images/Draft_Wire.svg" width=16px> Polyline** option from the menu.
    -   Use the keyboard shortcut: **P** then **L**.

## Notes

-   A Draft Wire can be edited with the [Draft Edit](Draft_Edit.md) command.
-   A Draft Wire can be converted to a [Draft BSpline](Draft_BSpline.md) with the [Draft WireToBSpline](Draft_WireToBSpline.md) command.
-   [Draft Lines](Draft_Line.md) and Draft Wires can also be joined with the [Draft Join](Draft_Join.md) command or the [Draft Upgrade](Draft_Upgrade.md) command.

## Properties

See also: [Property editor](Property_editor.md).

A Draft Wire object is derived from a [Part Part2DObject](Part_Part2DObject.md) and inherits all its properties. It also has the following additional properties:

### Data


{{TitleProperty|Draft}}

-    **Area|Area**: (read-only) specifies the area of the face of the wire. The value will be {{value|0.0}} if **Make Face** is `False` or the face cannot be created.

-    **Base|Link**
    

-    **Chamfer Size|Length**: specifies the length of the chamfers at the corners of the wire.

-    **Closed|Bool**: specifies if the wire is closed or not. If the wire is initially open this value is `False`, setting it to `True` will draw a line segment to close the wire. If the wire is initially closed this value is `True`, setting it to `False` will remove the last line segment and make the wire open.

-    **End|VectorDistance**: specifies the end point of the wire.

-    **Fillet Radius|Length**: specifies the radius of the fillets at the corners of the wire.

-    **Length|Length**: (read-only) specifies the total length of the wire.

-    **Make Face|Bool**: specifies if the wire makes a face or not. If it is `True` a face is created, otherwise only the edges are considered part of the object. This property only works if **Closed** is `True` and if the wire does not self-intersect.

-    **Points|VectorList**: specifies the points of the wire in its local coordinate system.

-    **Start|VectorDistance**: specifies the start point of the wire.

-    **Subdivisions|Integer**: specifies the number of subdivisions for each edge of the wire. If it is {{value|1}} each edge will be divided into {{value|2}} equal segments. Subdivisions are applied before chamfers and fillets.

-    **Tool|Link**
    

### View


{{TitleProperty|Draft}}

-    **Arrow Size|Length**: specifies the size of the symbol displayed at the end of the wire.

-    **Arrow Type|Enumeration**: specifies the type of symbol displayed at the end of the wire, which can be {{value|Dot}}, {{value|Circle}}, {{value|Arrow}}, {{value|Tick}} or {{value|Tick-2}}.

-    **End Arrow|Bool**: specifies whether to show a symbol at the end of the wire, so it can be used as an annotation line.

-    **Pattern|Enumeration**: specifies the [Draft Pattern](Draft_Pattern.md) with which to fill the face of the closed wire. This property only works if **Make Face** is `True` and if **Display Mode** is {{value|Flat Lines}}.

-    **Pattern Size|Float**: specifies the size of the [Draft Pattern](Draft_Pattern.md).




<div class="mw-translate-fuzzy">

## Programación

La herramienta Contorno se puede utilizar en [macros](macros/es.md) y desde la consola de [Python](Python.md) utilizando la siguiente función:


</div>

See also: [Autogenerated API documentation](https://freecad.github.io/SourceDoc/) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

To create a Draft Wire use the `make_wire` method (<small>(v0.19)</small> ) of the Draft module. This method replaces the deprecated `makeWire` method.


```python
wire = make_wire(pointslist, closed=False, placement=None, face=None, support=None)
wire = make_wire(Part.Wire, closed=False, placement=None, face=None, support=None)
```


<div class="mw-translate-fuzzy">

-   Crea un objeto Contorno a partir de la lista de vectores dada o a partir del contorno dado.
    -   Si cerrado es True o si el primer y último puntos son idénticos, el contorno es cerrado.
    -   Si el modo de cara es True (y el contorno está cerrado), el contorno se mostrará relleno.
-   Se utilizaran el espesor de línea y color actuales.
-   Devuelve el objeto recién creado.


</div>

Ejemplo:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

p1 = App.Vector(0, 0, 0)
p2 = App.Vector(1000, 1000, 0)
p3 = App.Vector(2000, 0, 0)

wire1 = Draft.make_wire([p1, p2, p3], closed=True)
wire2 = Draft.make_wire([p1, 2*p3, 1.3*p2], closed=True)
wire3 = Draft.make_wire([1.3*p3, p1, -1.7*p2], closed=True)

doc.recompute()
```



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Wire/es
