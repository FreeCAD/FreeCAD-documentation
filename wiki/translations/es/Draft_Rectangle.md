---
- GuiCommand:/es
   Name:Draft Rectangle
   Name/es:Draft Rectangle
   MenuLocation:Croquis →  Rectángulo
   Workbenches:[Croquis](Draft_Workbench/es.md), [Arquitectura](Arch_Workbench/es.md)
   Shortcut:**R** **E**
   Version:0.7
   SeeAlso:[Cubo](Part_Box/es.md)
---


</div>

## Description


<div class="mw-translate-fuzzy">

## Descripción

Esta herramienta dibuja un Rectángulo indicando dos puntos de su diagonal.

La herramienta rectángulo crea un rectángulo indicando dos puntos de su diagonal. Toma el [espesor de línea y color](Draft_Linestyle/es.md) previamente definidos en la Barra de herramientas de la bandeja de tiro. Opcionalmente, puede agregar un chaflán de 45 grados o un filete circular a cada esquina del rectángulo, y puede dividir el rectángulo en una serie de filas y / o columnas de igual tamaño.


</div>

The corners of a Draft Rectangle can be filleted (rounded) or chamfered by changing its **Fillet Radius** or **Chamfer Size** respectively. It is also possible to subdivide a Draft Rectangle by changing its **Columns** and/or **Rows** property.

<img alt="" src=images/Draft_Rectangle_example.jpg  style="width:400px;">


<div class="mw-translate-fuzzy">

<img alt="" src=images/Draft_Rectangle_example.jpg  style="width:400px;">


</div>

## Usage

See also: [Draft Tray](Draft_Tray.md), [Draft Snap](Draft_Snap.md) and [Draft Constrain](Draft_Constrain.md).


<div class="mw-translate-fuzzy">

## Utilización

1.  Presiona el botón **<img src="images/Draft_Rectangle.png" width=16px> [rectángulo](Draft_Rectangle/es.md)
**, o presiona las teclas **R** y **E**
2.  Designa un primer punto de la diagonal en la vista 3D, o escribe unas [coordenadas](Draft_Coordinates/es.md)
3.  Designa el punto apuesto de la diagonal en la vista 3D, o escribe unas [coordenadas](Draft_Coordinates/es.md). El rectángulo también será una cara, incluso aunque se muestre como en modo alámbrico.


</div>

## Options

The single character keyboard shortcuts available in the task panel can be changed. See [Draft Preferences](Draft_Preferences.md). The shortcuts mentioned here are the default shortcuts.


<div class="mw-translate-fuzzy">

## Opciones

-   Presiona **X**, **Y** o **Z** después de un punto para restringir el siguiente punto respecto al eje dado.
-   Para introducir coordenadas manualmente, simplemente introduce los números, presiona **ENTER** entre cada componente X, Y y Z.
-   Presiona **R** o selecciona la casilla para activar/desactivar el botón **'''Relativas'''**. Si el modo relativas está activado, las coordenadas del siguiente punto son relativas al punto anterior. Si no, son absolutas, desde el origen de coordenadas (0,0,0).
-   Presiona **T** o selecciona la casilla para activar/desactivar el botón **'''Continuo'''**. Si el modo continuo está activado, la herramienta rectángulo se reiniciará después de terminar, permitiendo que dibujes otro sin necesidad de presionar el botón de rectángulo de nuevo.
-   Presiona **CTRL** mientras dibujas para forzar el [ajuste](Draft_Snap/es.md) de tu punto a la posición de ajuste más cercana, independientemente de la distancia.
-   Presiona **SHIFT** mientras dibujas para [restringir](Draft_Constrain/es.md) tu siguiente punto horizontal o verticalmente en relación al anterior.
-   Presiona **I** o el botón **'''Relleno'''** para que el rectángulo se muestre como una cara después de que se ha cerrado. Esto simplemente establece la Vista\--\>Propiedad del rectángulo como \"líneas planas\" o \"alámbrico\", de modo que se puede cambiar después de forma sencilla.
-   Presiona **ESC** o el botón **'''Cancelar'''** para abortar la línea de comando actual.
-   Los rectángulos, cuando están en modo \"Líneas planas\", pueden mostrar un patrón de sombreado, al establecer su propiedad \"patrón\".


</div>

## Notes

-   A Draft Rectangle can be edited with the [Draft Edit](Draft_Edit.md) command.

## Preferences

See also: [Preferences Editor](Preferences_Editor.md) and [Draft Preferences](Draft_Preferences.md).

-   To change the number of decimals used for the input of coordinates: **Edit → Preferences... → General → Units → Units settings → Number of decimals**.
-   To change the initial value of filled mode: **Edit → Preferences... → Draft → General settings → Draft tools options → Fill objects with faces whenever possible**. Changing the filled mode in a task panel will override this preference for the current FreeCAD session.
-   If the **Edit → Preferences... → Draft → General settings → Draft tools options → Use Part Primitives when available** option is checked, the command will create a [Part Plane](Part_Plane.md) instead of a Draft Rectangle.


<div class="mw-translate-fuzzy">

## Propiedades

-    **Length**: Especifica la longitud del rectángulo

-    **Width**: Especifica el ancho del rectángulo

-    **Fillet Radius**: Especifica el radio de curvatura a dar a las esquinas del rectángulo

-    {{PropertyData | Fillet Radius}}: especifica el radio del filete de 90 grados en cada esquina del rectángulo

 

-    {{PropertyData | Rows}}: divide el rectángulo (horizontalmente) en filas de igual tamaño. Todo el rectángulo es 1 fila, por defecto

 

-    {{PropertyData | Columns}}: divide el rectángulo (verticalmente) en columnas de igual tamaño. Todo el rectángulo es 1 columna, por defecto.

-    {{PropertyData | Make Face}}: llena el rectángulo con una cara

-    **Texture Image**: Permite indicar la ruta de una imagen a ser mapeada sobre el rectángulo. Depende de ti dar al rectángulo la misma proporción que a la imagen si quieres evitar distorsiones. Dejándolo en blanco se eliminará la imagen.

-    {{PropertyView | Pattern}}: especifica un patrón de sombreado para rellenar el cable.

  +

-    {{PropertyView | Pattern Size}}: especifica el tamaño del patrón de sombreado


</div>

See also: [Property editor](Property_editor.md).

A Draft Rectangle object is derived from a [Part Part2DObject](Part_Part2DObject.md) and inherits all its properties. It also has the following additional properties:

### Data


{{TitleProperty|Draft}}

-    **Area|Area**: (read-only) specifies the area of the face of the rectangle. The value will be {{value|0.0}} if **Make Face** if `False`.

-    **Chamfer Size|Length**: specifies the length of the chamfers at the corners of the rectangle.

-    **Columns|Integer**: specifies the number of equal-sized columns in which the rectangle is divided.

-    **Fillet Radius|Length**: specifies the radius of the fillets at the corners of the rectangle.

-    **Height|Distance**: specifies the height of the rectangle.

-    **Length|Distance**: specifies the length of the rectangle.

-    **Make Face|Bool**: specifies if the rectangle makes a face or not. If it is `True` a face is created, otherwise only the perimeter is considered part of the object.

-    **Rows|Integer**: specifies the number of equal-sized rows in which the rectangle is divided.

### View


{{TitleProperty|Draft}}

-    **Pattern|Enumeration**: specifies the [Draft Pattern](Draft_Pattern.md) with which to fill the face of the rectangle. This property only works if **Make Face** is `True` and if **Display Mode** is {{value|Flat Lines}}.

-    **Pattern Size|Float**: specifies the size of the [Draft Pattern](Draft_Pattern.md).

-    **Texture Image|File**: specifies the path of the image file to be mapped onto the face of the rectangle. Blanking this property will remove the image. The rectangle should have the same proportions as the image to avoid distortions.

## Scripting


<div class="mw-translate-fuzzy">

## Archivos de guión 

La herramienta rectángulo puede utilizarse en [macros](macros/es.md) y desde la consola de [Python](Python.md) utilizando la siguiente función:


</div>

To create a Draft Rectangle use the `make_rectangle` method (<small>(v0.19)</small> ) of the Draft module. This method replaces the deprecated `makeRectangle` method.


```python
rectangle = make_rectangle(length, height, placement=None, face=None, support=None)
```


<div class="mw-translate-fuzzy">

-   Crea un objeto rectángulo Rectangle con longitud length en dirección X y altura height en dirección Y.
-   Si se indica una ubicación, se utiliza.
-   Si facemode es False, el rectángulo se mostrará en modo alámbrico, en otro caso como una cara.
-   Se utilizarán el espesor de línea y color actuales de Boceto.
-   Devuelve el objeto recién creado.


</div>

Ejemplo: 
```python
import FreeCAD as App
import Draft

doc = App.newDocument()

rectangle1 = Draft.make_rectangle(4000, 1000)
rectangle2 = Draft.make_rectangle(1000, 4000)

zaxis = App.Vector(0, 0, 1)
p3 = App.Vector(1000, 1000, 0)
place3 = App.Placement(p3, App.Rotation(zaxis, 45))

rectangle3 = Draft.make_rectangle(3500, 250, placement=place3)

doc.recompute()
```





 
