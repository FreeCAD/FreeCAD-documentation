---
 GuiCommand:
   Name: Draft Circle
   Name/es: Draft Círculo
   Workbenches: Draft_Workbench/es, Arch_Workbench/es
   MenuLocation: Boceto , Circunferencia
   Shortcut: **C** **I**
   Version: 0.7
   SeeAlso: Draft_Arc/es
---

# Draft Circle/es


</div>

## Description


<div class="mw-translate-fuzzy">

#### Descripción

La herramienta Circunferencia crea una circunferencia en el [plano de trabajo](Draft_SelectPlane/es.md) actual introduciendo dos puntos, el centro y el radio, o seleccionando las tangentes o cualquier combinación de ellas. Toma el [espesor de línea y color](Draft_Linestyle/es.md) previamente establecido en la pestaña de tareas. Esta herramienta funciona del mismo modo que la herramienta [Arco](Draft_Arc/es.md), excepto que termina después de introducir el radio.


</div>

A Draft Circle can be turned into an arc by setting its **First Angle** and **Last Angle** properties to different values.

<img alt="" src=images/Draft_Circle_example.jpg  style="width:400px;">


<div class="mw-translate-fuzzy">

<img alt="" src=images/Draft_Circle_example.jpg  style="width:400px;">


</div>

## Usage

See also: [Draft Tray](Draft_Tray.md), [Draft Snap](Draft_Snap.md) and [Draft Constrain](Draft_Constrain.md).


<div class="mw-translate-fuzzy">

#### Utilización

1.  Presiona el botón **<img src="images/Draft_Circle.png" width=16px> [Circunferencia](Draft_Circle/es.md)
**, o presiona las teclas **C** y **I**
2.  Selecciona un primer punto en la vista 3D, o escribe una coordenadas
3.  Selecciona un segundo punto en la vista 3D, o introduce un valor de radio.


</div>

## Options

The single character keyboard shortcuts available in the task panel can be changed. See [Draft Preferences](Draft_Preferences.md). The shortcuts mentioned here are the default shortcuts (for version 0.22).


<div class="mw-translate-fuzzy">

## Opciones

-   El principal uso de la herramienta circunferencia es indicando dos puntos, el centro y un punto en la circunferencia, definiendo el radio.
-   Presionando **ALT**, puedes indicar una tangencia en lugar del centro o del radio. Puedes por tanto construir varios tipos de circunferencias seleccionando una, dos o tres tangencias.
-   Para introducir coordenadas manualmente, simplemente introduce los números y presiona **ENTER** entre cada componente X, Y y Z.
-   Presiona **T** o pulsa la casilla activar / desactivar el modo **'''Continuo'''**. Si está definido el modo continuo, la herramienta Circunferencia se iniciará después de indicar el segundo punto, permitiendo que dibujes otra circunferencia sin presionar el botón de circunferencia de nuevo.
-   Presiona **CTRL** mientras dibujas para forzar el [ajuste](Draft_Snap/es.md) de tu punto a la posición de ajuste más cercana, independientemente de la distancia.
-   Presiona **SHIFT** mientras dibujas para [restringir](Draft_Constrain/es.md) tu segundo punto horizontal o verticalmente en relación al primero.
-   Presiona **I** o el botón de **'''Relleno'''** para que la circunferencia se muestre como una cara después de que se cierre. Esto simplemente establece Vista -\> Propiedad de la circunferencia a \"Líneas planas\" o \"Alámbricas\", sde modo que se pueda cambiar fácilmente más adelante.
-   Presiona **ESC** o el botón **'''Cancelar'''** para abortar el comando línea actual.
-   La circunferencia se puede convertir en un arco después de crearse, estableciendo las propiedades del primer ángulo y último ángulo a valores diferentes.


</div>

## Notes

-   A Draft Circle can be edited with the [Draft Edit](Draft_Edit.md) command.

## Preferences

See also: [Preferences Editor](Preferences_Editor.md) and [Draft Preferences](Draft_Preferences.md).

-   If the **Edit → Preferences... → Draft → General → Create Part primitives if possible** option is checked, the command will create a [Part Circle](Part_Circle.md) instead of a Draft Circle.

## Properties

See also: [Property editor](Property_editor.md).

A Draft Circle object is derived from a [Part Part2DObject](Part_Part2DObject.md) and inherits all its properties. It also has the following additional properties:

### Data


{{TitleProperty|Draft}}

-    **Area|Area**: (read-only) specifies the area of the face of the circle. The value will be {{value|0.0}} if **Make Face** if `False` or the face cannot be created.

-    **First Angle|Angle**: specifies the start angle of the circle, normally {{value|0&#176;}}.

-    **Last Angle|Angle**: specifies the end angle of the circle, normally {{value|0&#176;}}.

-    **Make Face|Bool**: specifies if the circle makes a face or not. If it is `True` a face is created, otherwise only the perimeter is considered part of the object. This property only works if the **First Angle** and **Last Angle** have the same value. Note that {{value|0&#176;}} and {{value|360&#176;}} are not considered the same.

-    **Radius|Length**: specifies the radius of the circle.

### View


{{TitleProperty|Draft}}

-    **Pattern|Enumeration**: specifies the [Draft Pattern](Draft_Pattern.md) with which to fill the face of the circle. This property only works if **Make Face** is `True` and if **Display Mode** is {{value|Flat Lines}}.

-    **Pattern Size|Float**: specifies the size of the [Draft Pattern](Draft_Pattern.md).

## Scripting


<div class="mw-translate-fuzzy">

## Archivos de guión 

La herramienta Circunferencia se puede utilizar en [macros](macros/es.md) y desde la consola utilizando la siguiente función:


</div>

To create a Draft Circle use the `make_circle` method (<small>(v0.19)</small> ) of the Draft module. This method replaces the deprecated `makeCircle` method.


```python
circle = make_circle(radius, placement=None, face=None, startangle=None, endangle=None, support=None)
circle = make_circle(Part.Edge, placement=None, face=None, startangle=None, endangle=None, support=None)
```


<div class="mw-translate-fuzzy">

-   Crea un objeto circunferencia con el valor de radio dado.
-   Si se indica una ubicación, se utiliza. Si el modo de cara es falso, la circunferencia se mostrará como una estructura alámbrica, en otro caso como una cara.
-   Si se indican un ángulo de inicio Y un ángulo final (en grados), se utilizarán y el objeto se mostrará como un arco.
-   Devuelve el objeto recién creado.


</div>

Ejemplo: 
```python
import FreeCAD as App
import Draft

doc = App.newDocument()

circle1 = Draft.make_circle(200)

zaxis = App.Vector(0, 0, 1)
p2 = App.Vector(1000, 1000, 0)
place2 = App.Placement(p2, App.Rotation(zaxis, 0))
circle2 = Draft.make_circle(500, placement=place2)

p3 = App.Vector(-1000, -1000, 0)
place3 = App.Placement(p3, App.Rotation(zaxis, 0))
circle3 = Draft.make_circle(750, placement=place3)

doc.recompute()
```



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Circle/es
