---
- GuiCommand:
   Name: Draft Line
   Name/es: Borrador Linea
   MenuLocation: Borrador - Línea
   Workbenches: [Borrador](Draft_Workbench/es.md), [Arquitectura](Arch_Workbench/es.md)
   Shortcut: **L** **I**
   Version: 0.7
   SeeAlso: [Borrador Hilo](Draft_Wire/es.md), [Borrador Punto](Draft_Point/es.md)
---

# Draft Line/es


</div>

## Descripción


<div class="mw-translate-fuzzy">

La herramienta Línea crea una línea recta definida por dos puntos. Utiliza el [Estilo de Línea de Borrador](Draft_Linestyle/es.md) establecido en la [Bandeja de Borrador](Draft_Tray/es.md). La herramienta Línea se comporta exactamente como la herramienta [Borrador Hilo](Draft_Wire/es.md), excepto que se detiene después de dos puntos.


</div>

A Draft Line is in fact a [Draft Wire](Draft_Wire.md) with only two points.

<img alt="" src=images/Draft_Line_example.jpg  style="width:400px;">


<div class="mw-translate-fuzzy">



*Línea creada por dos puntos*


</div>

## Utilización

See also: [Draft Tray](Draft_Tray.md), [Draft Snap](Draft_Snap.md) and [Draft Constrain](Draft_Constrain.md).


<div class="mw-translate-fuzzy">

1.  Pulse el **<img src="images/Draft_Line.svg" width=16px> [Línea de Borrador](Draft_Line/es.md)**, o utilice el botón **Borrador** → **<img src="images/Draft_Line.svg" width=16px> [Línea](Draft_Line/es.md)** del menú superior, o utiliza el atajo de teclado: **L** y luego **I**.
2.  Haga clic en un primer punto en la vista 3D, o escriba una coordenada y pulse el **<img src="images/Draft_AddPoint.svg" width=16px> añadir punto**.
3.  Haz clic en un segundo punto en la vista 3D, o escribe una coordenada y pulsa el **<img src="images/Draft_AddPoint.svg" width=16px> añadir punto**.


</div>

## Options

The single character keyboard shortcuts available in the task panel can be changed. See [Draft Preferences](Draft_Preferences.md). The shortcuts mentioned here are the default shortcuts.


<div class="mw-translate-fuzzy">

## Opciones

-   Pulse **X**, **Y** o **Z** después del primer punto para restringir el segundo punto en el eje dado.
-   Para introducir las coordenadas manualmente, simplemente introduzca los números y luego pulse **Enter** entre cada componente X, Y y Z.
    -   También puede definir las coordenadas polares del punto dando un valor a \"Longitud\" y \"Ángulo\". Haga clic en la casilla de verificación junto a \"Ángulo\" para restringir el puntero al ángulo especificado.
    -   Puede pulsar el **<img src="images/Draft_AddPoint.svg" width=16px> añadir un punto** cuando tenga los valores deseados para insertar el punto.
-   Pulse **R** o haga clic en la casilla para activar el modo *relativo*. Si el modo relativo está activado, las coordenadas del segundo punto son relativas al primero; si no, son absolutas, tomadas desde el origen (0,0,0).
-   Pulse **T** o haga clic en la casilla para activar el modo *continuar*. Si el modo de continuar está activado, la herramienta Línea se reiniciará después de dar el segundo punto, lo que le permitirá dibujar otro segmento de línea sin tener que volver a pulsar el botón de la herramienta.
-   Mantén pulsado **Ctrl** mientras dibujas para forzar [snapping](Draft_Snap.md) tu punto a la ubicación de snap más cercana, independientemente de la distancia.
-   Mantén pulsado **Shift** mientras dibujas para [restringir](Draft_Constrain/es.md) tu segundo punto horizontal o verticalmente en relación con el primero.
-   Pulse **Ctrl**+**Z** o pulse el **<img src="images/Draft_UndoLine.svg" width=12px> Deshacer** para deshacer el último punto.
-   Pulse **Esc** o el botón **Close** para abortar el comando actual.


</div>

## Notes


<div class="mw-translate-fuzzy">

La línea puede editarse haciendo doble clic en el elemento en la vista de árbol, o pulsando el **<img src="images/Draft_Edit.svg" width=16px> [Borrador de edición](Draft_Edit/es.md)**. A continuación, puede mover los puntos a una nueva posición.


</div>

## Preferences

See also: [Preferences Editor](Preferences_Editor.md) and [Draft Preferences](Draft_Preferences.md).

-   To change the number of decimals used for the input of coordinates, lengths and angles: **Edit → Preferences... → General → Units → Units settings → Number of decimals**.
-   To change the initial focus of the task panel to the **Length** input box: **Edit → Preferences... → Draft → General settings → Draft tools options → Set focus on Length instead of X coordinate**. Note that you must move the pointer in the [3D view](3D_view.md) for the change to take effect.
-   If the **Edit → Preferences... → Draft → General settings → Draft tools options → Use Part Primitives when available** option is checked, the command will create a [Part Line](Part_Line.md) instead of a Draft Line.

## Properties


<div class="mw-translate-fuzzy">

## Propiedades

Un objeto Línea comparte todas las propiedades de un **<img src="images/Draft_Wire.svg" width=16px> [Borrador Hilo](Draft_Wire/es.md)**, sin embargo, sólo algunas de estas propiedades son aplicables a la Línea.


</div>

## Scripting


<div class="mw-translate-fuzzy">

## Guión


**Ver también:**

[Borrador API](Draft_API/es.md) y [Fundamentos de Guión FreeCAD](FreeCAD_Scripting_Basics/es.md).


</div>

To create a Draft Line use the `make_line` method (<small>(v0.19)</small> ) of the Draft module. This method replaces the deprecated `makeLine` method.


```python
line = make_line(p1, p2)
line = make_line(LineSegment)
line = make_line(Shape)
```

-   Crea un objeto `Line` entre los puntos `p1` y `p2`, cada uno definido por su `FreeCAD.Vector`, con unidades en milímetros.
-   Crea un objeto `Line` a partir de un `Part.LineSegment`.
-   Crea un objeto `Line` desde el primer vértice hasta el último del `Shape` dado.

Ejemplo:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

p1 = App.Vector(0, 0, 0)
p2 = App.Vector(1000, 500, 0)
p3 = App.Vector(-250, -500, 0)
p4 = App.Vector(500, 1000, 0)

line1 = Draft.make_line(p1, p2)
line2 = Draft.make_line(p3, p4)

doc.recompute()
```


<div class="mw-translate-fuzzy">





</div>



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Line/es
