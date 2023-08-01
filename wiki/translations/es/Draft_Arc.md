---
- GuiCommand:
   Name:Draft Arc
   Name/es:Draft Arc
   MenuLocation:Croquis → Arco
   Workbenches:[Croquis](Draft_Workbench/es.md), [Arquitectura](Arch_Workbench/es.md)
   Shortcut:A R
   SeeAlso:[Circunferencia](Draft_Circle/es.md)
---

# Draft Arc/es


</div>


<div class="mw-translate-fuzzy">

## Descripción

La herramienta arco crea un arco en el [plano de trabajo](Draft_SelectPlane/es.md) actual introduciendo cuatro puntos, el centro, el radio, el primer punto y el último punto, o seleccionando tangencias, o cualquier combinación de ellas. Toma el [espesor de línea y color](Draft_Linestyle/es.md) previamente definidos en la pestaña de tareas. Esta herramienta funciona del mismo modo que la herramienta [circunferencia](Draft_Circle/es.md), pero añade los ángulos inicial y final.


</div>

The <img alt="" src=images/Draft_Arc.svg  style="width:24px;"> **Draft Arc** command creates a circular arc in the current [working plane](Draft_SelectPlane.md) from a center, a radius, a start angle and an aperture angle. The radius and the angles can be defined by picking points.

A Draft Arc is in fact a [Draft Circle](Draft_Circle.md) with a **First Angle** that is not the same as its **Last Angle**.

<img alt="" src=images/Draft_Arc_example.jpg  style="width:400px;">


<div class="mw-translate-fuzzy">

<img alt="" src=images/Draft_Arc_example.jpg  style="width:400px;">


</div>

## Usage

See also: [Draft Tray](Draft_Tray.md), [Draft Snap](Draft_Snap.md) and [Draft Constrain](Draft_Constrain.md).


<div class="mw-translate-fuzzy">

## Utilización

1.  Presiona el botón **<img src="images/Draft_Arc.png" width=16px> [Arco](Draft_Arc/es.md)
**, o presiona las teclas **A** y **R**
2.  Indica un primer punto en la vista 3D, o escribe unas coordenadas
3.  Indica un segundo punto en la vista 3D, o introduce el valor del radio
4.  Indica un tercer punto en la vista 3D, o introduce un ángulo de inicio
5.  Indica un cuarto punto en la vista 3D, o introduce un ángulo final


</div>

## Options

The single character keyboard shortcuts available in the task panel can be changed. See [Draft Preferences](Draft_Preferences.md). The shortcuts mentioned here are the default shortcuts.


<div class="mw-translate-fuzzy">

## Opciones

-   El principal uso de la herramienta arco es designando 4 puntos: el centro, un punto de la circunferencia, definiendo el radio, un tercer punto definiendo el ángulo de inicio del arco, y un cuarto punto definiendo su final.
-   Presionando **ALT**, puedes seleccionar una tangente en lugar de designar un punto, para definir la circunferencia base del arco. Puedes por tanto construir diversos tipos de circunferencias seleccionando una, dos o tres tangencias.
-   La dirección del arco depende del movimiento que hagas con el ratón. Si empiezas a moverlo en sentido de las agujas del reloj después de indicar el tercer punto, tu arco irá en sentido de las agujas del reloj. Para ir al contrario de las agujas del reloj, simplemente mueve el ratón sobre el tercer punto indicado, hasta que el arco se dibuje hacia el otro sentido.
-   Para introducir las coordenadas manualmente, simplemente introduce los números, presiona **ENTER** entre cada componente X, Y y Z.
-   Presiona **T** o selecciona la casilla para activar/desactivar el botón **'''Continue'''**. Si el modo continuo está activado, la herramienta arco se reiniciará después de indicar el cuarto punto, permitiendo que dibujes otro arco sin necesidad de presionar el botón de arco de nuevo.
-   Presiona **CTRL** mientras dibujas para forzar el [ajuste](Draft_Snap/es.md) de tu punto a la ubicación de ajuste más cercana, independientemente de la distancia.
-   Presiona **SHIFT** mientras dibujas para [restringir](Draft_Constrain/es.md) tu punto horizontal o verticalmente en relación con el centro.
-   Presiona **ESC** o el botón **'''Cancelar'''** para abortar la línea de comando actual.
-   El arco se puede convertir en una circunferencia después de crearse, definiendo el mismo valor para las propiedades de sus ángulos de inicio y fin.


</div>

## Notes

-   A Draft Arc can be edited with the [Draft Edit](Draft_Edit.md) command.

## Preferences

See also: [Preferences Editor](Preferences_Editor.md) and [Draft Preferences](Draft_Preferences.md).

-   To change the number of decimals used for the input of coordinates, radii and angles: **Edit → Preferences... → General → Units → Units settings → Number of decimals**.
-   If the **Edit → Preferences... → Draft → General settings → Draft tools options → Use Part Primitives when available** option is checked, the command will create a [Part Circle](Part_Circle.md) instead of a Draft Circle.

## Properties


<div class="mw-translate-fuzzy">

## Propiedades

-    **Radius**: El radio del arco

-    **First Angle**: El ángulo del primer punto del arco

-    **Last Angle**: El ángulo del último punto del arco


</div>

## Scripting


<div class="mw-translate-fuzzy">

## Archivos de guión 

La herramienta circunferencia también se puede utilizar para crear arco en [macros](macros/es.md) y desde la consola de Python utilizando la siguiente instrucción, con los argumentos adicionales dados:


</div>

To create a Draft Arc use the `make_circle` method (<small>(v0.19)</small> ) of the Draft module. This method replaces the deprecated `makeCircle` method.

Example:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

arc1 = Draft.make_circle(200, startangle=0, endangle=90)
arc2 = Draft.make_circle(500, startangle=20, endangle=160)
arc3 = Draft.make_circle(750, startangle=-30, endangle=-150)

doc.recompute()
```



---
![](images/Button_right.svg) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Arc/es
