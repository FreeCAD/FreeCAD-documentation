---
- GuiCommand   */es
   Name   *Draft Move
   Name/es   *Draft Move
   MenuLocation   *Croquis -> Mover
   Workbenches   *[Croquis](Draft_Workbench/es.md)
   Shortcut   ***M** **V**
---

# Draft Move/es


</div>

## Descripción


<div class="mw-translate-fuzzy">

La herramienta Mover mueve o copia los objetos seleccionados de un punto a otro. Si no se han seleccionado objetos, te invita a seleccionarlos.


</div>

The command can be used on 2D objects created with the [Draft Workbench](Draft_Workbench.md) or [Sketcher Workbench](Sketcher_Workbench.md), but also on many 3D objects such as those created with the [Part Workbench](Part_Workbench.md), [PartDesign Workbench](PartDesign_Workbench.md) or [Arch Workbench](Arch_Workbench.md).

<img alt="" src=images/Draft_Move_example.jpg  style="width   *400px;"> 
*Moving an object from one point to another*

## Utilización

See also   * [Draft Snap](Draft_Snap.md) and [Draft Constrain](Draft_Constrain.md).


<div class="mw-translate-fuzzy">

1.  Selecciona los objetos que deseas mover o copiar
2.  Presiona el botón **<img src="images/Draft_Move.png" width=16px> [Mover](Draft_Move/es.md)
**, o presiona las teclas **M** y **V**
3.  Designa un primer punto en la vista 3D, o tipo en coordenadas
4.  Designa otro punto en la vista 3D, o escribe unas coordenadas


</div>

## Opciones

The single character keyboard shortcuts mentioned here can be changed. See [Draft Preferences](Draft_Preferences.md).


<div class="mw-translate-fuzzy">

-   Presiona **X**, **Y** o **Z** después de un punto para restringir el siguiente punto sobre el eje indicado.
-   Para introducir coordenadas manualmente, simplemente introduce los números y presiona **ENTER** entre cada componente X, Y y Z.
-   Presiona **R** o selecciona la casilla para activar/desactivar el botón **'''Relativas'''**. Si está activado el modo relativas, las coordenadas del siguiente punto son relativas al punto anterior. En otro caso, son absolutas, tomadas desde el origen de coordenadas (0,0,0).
-   Presiona **T** o selecciona la casilla para activar/desactivar el botón **'''Continuar'''**. Si el modo continuar está activado, la herramienta mover se reiniciará después de terminar, permitiendo mover o copiar los objetos otra vez sin volver a pulsar el botón de Mover.
-   Presionando **ALT** o **C** o seleccionando el botón **'''Copy'''** se creará una copia de los objetos, en lugar de moverlos. Si mantienes la tecla **ALT** pulsada después de designar el segundo punto, serás capaz de ubicar más copias, hasta que liberes la tecla **ALT**.
-   Presiona **CTRL** mientras dibujas para forzar el [ajuste](Draft_Snap/es.md) de tu punto a la ubicación de ajuste más cercana, independientemente de la distancia.
-   Presiona **SHIFT** mientras dibujas para [restringir](Draft_Constrain/es.md) tu siguiente punto horizontal o verticalmente en relación con el último.
-   Presiona **ESC** o el botón **'''Cancelar'''** para abortar el comando actual.


</div>

## Notes

-   An Object that is [attached](Part_EditAttachment.md) cannot be moved with the Draft Move command. To move it either its **Support** object has to be moved, or its **Attachment Offset** has to be changed.

## Preferences

See also   * [Preferences Editor](Preferences_Editor.md) and [Draft Preferences](Draft_Preferences.md).

-   To change the number of decimals used for the input of coordinates, lengths and angles   * **Edit → Preferences... → General → Units → Units settings → Number of decimals**.
-   To change the initial focus of the task panel to the **Length** input box   * **Edit → Preferences... → Draft → General settings → Draft tools options → Set focus on Length instead of X coordinate**. Note that you must move the pointer in the [3D view](3D_view.md) for the change to take effect.
-   To store and reuse the same copy mode setting across commands   * **Edit → Preferences... → Draft → General settings → Draft tools options → Global copy mode**.
-   To reselect the base objects after copying objects   * **Edit → Preferences... → Draft → General settings → Draft tools options → Select base objects after copying**.

## Scripting


<div class="mw-translate-fuzzy">

## Programación


</div>


<div class="mw-translate-fuzzy">

La herramienta Mover se puede utilizar en [macros](macros/es.md) y desde la consola de Pyython utilizando la siguiente función   *


</div>


```python
moved_list = move(objectslist, vector, copy=False)
```


<div class="mw-translate-fuzzy">

-   Mueve el objeto dado o los objetos contenido en la lista indicada

en la dirección y distancia indicada por el vector dado. 

-   Si copymode es True, los objetos actuales no se moverán, sino que

en su lugar se crearán copias. 

-   Devuelve los objetos (o sus copias si copymode era True)


</div>

Ejemplo   *


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

polygon1 = Draft.make_polygon(5, radius=1000)
polygon2 = Draft.make_polygon(3, radius=500)
polygon3 = Draft.make_polygon(6, radius=220)

Draft.move(polygon1, App.Vector(500, 500, 0))
Draft.move(polygon1, App.Vector(500, 500, 0))
Draft.move(polygon2, App.Vector(1000, -1000, 0))
Draft.move(polygon3, App.Vector(-500, -500, 0))

list1 = [polygon1, polygon2, polygon3]

vector = App.Vector(-2000, -2000, 0)
list2 = Draft.move(list1, vector, copy=True)
list3 = Draft.move(list1, -2*vector, copy=True)

doc.recompute()
```



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Move/es
