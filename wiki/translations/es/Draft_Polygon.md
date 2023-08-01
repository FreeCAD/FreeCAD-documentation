---
- GuiCommand:
   Name:Draft Polygon
   Name/es:Draft Polygon
   MenuLocation:Croquis - Polígono
   Workbenches:[Croquis](Draft_Workbench/es.md), [Arquitectura](Arch_Workbench/es.md)
   Shortcut:**P** **G**
---

# Draft Polygon/es


</div>

## Description


<div class="mw-translate-fuzzy">

## Descripción

La herramienta polígono crea un polígono regular designando dos puntos, el centro y un segundo punto definiendo un radio. Toma el [espesor de línea y color](Draft_Linestyle/es.md) previamente establecidos en la pestaña de tareas.


</div>

A Draft Polygon can be switched from inscribed to circumscribed by changing its **Draw Mode** property. The corners of a Draft Polygon can be filleted (rounded) or chamfered by changing its **Fillet Radius** or **Chamfer Size** respectively.

<img alt="" src=images/Draft_polygon_example.jpg  style="width:400px;">


<div class="mw-translate-fuzzy">

<img alt="" src=images/Draft_polygon_example.jpg  style="width:400px;">


</div>

## Usage

See also: [Draft Tray](Draft_Tray.md), [Draft Snap](Draft_Snap.md) and [Draft Constrain](Draft_Constrain.md).


<div class="mw-translate-fuzzy">

El punto puede indicarse con el ratón en una vista 3D o introduciendo coordenadas desde el teclado.

## Utilización

1.  Presiona el botón **<img src="images/Draft_Polygon.png" width=16px> [Polígono](Draft_Polygon/es.md)
**, o presiona las teclas **P** y **G**
2.  Designa un primer punto en la vista 3D, o escribe unas coordenadas para indicar el centro
3.  Ajusta el número deseado de dados en el letrero de diálogo de opciones,
4.  Designa otro punto en la vista 3D, o escribe un valor de radio para definir el radio del polígono. El polígono será también una cara, aunque se muestre en modo alámbrico.


</div>

## Options

The single character keyboard shortcuts available in the task panel can be changed. See [Draft Preferences](Draft_Preferences.md). The shortcuts mentioned here are the default shortcuts.


<div class="mw-translate-fuzzy">

## Opciones

-   Paras introducir coordenadas manualmente, simplemente introduce los números y presiona **ENTER** entre cada componente X, Y y Z.
-   Presiona **T** o selecciona la casilla para activar/desactivar el botón **'''Continuar'''**. Si el modo continuar está activado, la herramienta polígono se reiniciará después de terminar permitiendo que dibujes otro sin presionar el botón de polígono de nuevo.
-   Presiona **CTRL** mientras dibujas para forzar el [ajuste](Draft_Snap/es.md) de tu punto a la ubicación de ajuste más cercana, independientemente de la distancia.
-   Presiona **SHIFT** mientras dibujas para [restringir](Draft_Constrain/es.md) tu siguiente punto horizontal o verticalmente en relación al último punto indicado.
-   Presiona **I** o el botón **'''Relleno'''** para que el polígono se muestre como una cara. Esto simplemente establece las propiedades de vista del rectángulo como \"líneas planas\" o \"alámbricas\", de modo que se pueda cambiar después de forma sencilla.
-   Presiona **ESC** o el botón **'''Cancelar'''** para abortar el comando actual.
-   Los polígonos, cuando se encuentran en el modo de visualización \"Líneas planas\", pueden mostrar un patrón de sombreado, estableciendo su propiedad \"Patrón\" a continuación.


</div>

## Notes

-   A Draft Polygon can be edited with the [Draft Edit](Draft_Edit.md) command.

## Preferences

See also: [Preferences Editor](Preferences_Editor.md) and [Draft Preferences](Draft_Preferences.md).

-   To change the number of decimals used for the input of coordinates and radii: **Edit → Preferences... → General → Units → Units settings → Number of decimals**.
-   To change the initial value of filled mode: **Edit → Preferences... → Draft → General settings → Draft tools options → Fill objects with faces whenever possible**. Changing the filled mode in a task panel will override this preference for the current FreeCAD session.
-   If the **Edit → Preferences... → Draft → General settings → Draft tools options → Use Part Primitives when available** option is checked, the command will create a [Part RegularPolygon](Part_RegularPolygon.md) instead of a Draft Polygon.


<div class="mw-translate-fuzzy">

## Propiedades

-    **Radius**: El radio de la circunferencia de definición

-    **Draw Mode**: Especifica si el polígono es inscrito o circunscrito a la circunferencia

-    {{PropertyData | Chaflán tamaño}}: Especifica el tamaño de las esquinas achaflanadas

-    **Faces Number**: El número de lados del polígono

-    **Fillet Radius**: Especifica el radio de curvatura a dar a los vértices del rectángulo

-    {{PropertyData | Make Face}}: llena el polígono con una cara

 \* {{PropertyView | Pattern}}: especifica un patrón de sombreado para rellenar el cable con  \* {{PropertyView | Pattern Size}}: especifica el tamaño del patrón de sombreado


</div>

See also: [Property editor](Property_editor.md).

A Draft Polygon object is derived from a [Part Part2DObject](Part_Part2DObject.md) and inherits all its properties. It also has the following additional properties:

### Data


{{TitleProperty|Draft}}

-    **Area|Area**: (read-only) specifies the area of the face of the polygon. The value will be {{value|0.0}} if **Make Face** if `False`.

-    **Chamfer Size|Length**: specifies the length of the chamfers at the corners of the polygon.

-    **Draw Mode|Enumeration**: specifies if the polygon is {{value|inscribed}} in a circle or {{value|circumscribed}} around a circle.

-    **Faces Number|Integer**: specifies the number of sides of the polygon.

-    **Fillet Radius|Length**: specifies the radius of the fillets at the corners of the polygon.

-    **Make Face|Bool**: specifies if the polygon makes a face or not. If it is `True` a face is created, otherwise only the perimeter is considered part of the object.

-    **Radius|Length**: specifies the radius of the circle that defines the polygon.

### View


{{TitleProperty|Draft}}

-    **Pattern|Enumeration**: specifies the [Draft Pattern](Draft_Pattern.md) with which to fill the face of the polygon. This property only works if **Make Face** is `True` and if **Display Mode** is {{value|Flat Lines}}.

-    **Pattern Size|Float**: specifies the size of the [Draft Pattern](Draft_Pattern.md).

## Scripting


<div class="mw-translate-fuzzy">

## Archivos de guión 

La herramienta polígono puede utilizarse en [macros](macros/es.md) y desde la consola de Python utilizando la siguiente función:


</div>

To create a Draft Polygon use the `make_polygon` method (<small>(v0.19)</small> ) of the Draft module. This method replaces the deprecated `makePolygon` method.


```python
polygon = make_polygon(nfaces, radius=1, inscribed=True, placement=None, face=None, support=None)
```


<div class="mw-translate-fuzzy">

-   Crea un objeto polígono con el número de caras y el radio dados.
-   Siinscribed es False, el polígono es circunscrito a la circunferencia con el radio dado, en otro caso es inscrito.
-   Si face es True, la forma resultante se muestra como una cara, en otro caso como una estructura alámbrica.
-   Devuelve el objeto recién creado.


</div>

Ejemplo: 
```python
import FreeCAD as App
import Draft

doc = App.newDocument()

polygon1 = Draft.make_polygon(4, radius=500)
polygon2 = Draft.make_polygon(5, radius=750)

zaxis = App.Vector(0, 0, 1)
p3 = App.Vector(1000, 1000, 0)
place3 = App.Placement(p3, App.Rotation(zaxis, 90))

Polygon3 = Draft.make_polygon(6, radius=1450, placement=place3)

doc.recompute()
```



---
![](images/Button_right.svg) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Polygon/es
