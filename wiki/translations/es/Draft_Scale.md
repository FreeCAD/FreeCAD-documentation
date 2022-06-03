---
- GuiCommand   */es
   Name   *Draft Scale
   Name/es   *Draft Scale
   Workbenches   *[Croquis](Draft_Workbench/es.md), [Arquitectura](Arch_Workbench/es.md)
   MenuLocation   *Croquis -> Escala
   Shortcut   ***S** **C**
   SeeAlso   *[Clonar](Draft_Clone/es.md)
---

# Draft Scale/es


</div>

## Descripción


<div class="mw-translate-fuzzy">

Esta herramienta escala los objetos seleccionados con respecto a un punto base. Si no se han seleccionado objetos, te invitará a seleccionarlos.


</div>

The command can be used on 2D objects created with the [Draft Workbench](Draft_Workbench.md) or [Sketcher Workbench](Sketcher_Workbench.md), but also on many 3D objects such as those created with the [Part Workbench](Part_Workbench.md), [PartDesign Workbench](PartDesign_Workbench.md) or [Arch Workbench](Arch_Workbench.md).

<img alt="" src=images/Draft_Scale_example.png  style="width   *400px;"> 
*Scaling an object around a base point*

## Utilización

See also   * [Draft Snap](Draft_Snap.md) and [Draft Constrain](Draft_Constrain.md).


<div class="mw-translate-fuzzy">

1.  Selecciona los objetos que quieres escalar
2.  Presiona el botón **<img src="images/Draft_Scale.png" width=16px> [Escala](Draft_Scale/es.md)
**, o presiona las teclas **S** y **C**
3.  Indica un primer punto en la vista 3D, o escribe unas coordenadas para definir el punto base del escalado. Indica otro punto en la vista 3D, o escribe unas coordenadas
4.  Otro menú con opciones de escalado se abrirá. Rellena las diferentes opciones y pulsa **OK** para aceptar


</div>

## Opciones

### First task panel 

The single character keyboard shortcuts mentioned here can be changed. See [Draft Preferences](Draft_Preferences.md).

-   To manually enter the coordinates for the base point enter the X, Y and Z component, and press **Enter** after each. Or you can press the **<img src="images/Draft_AddPoint.svg" width=16px> Enter point** button when you have the desired values. It is advisable to move the pointer out of the [3D view](3D_view.md) before entering coordinates.
-   Press **G** or click the **Global** checkbox to toggle global mode. If global mode is on, coordinates are relative to the global coordinate system, else they are relative to the [working plane](Draft_SelectPlane.md) coordinate system. <small>(v0.20)</small> 
-   The other checkboxes in this task panel, displayed in FreeCAD version 0.19 and earlier, are ignored by the command.
-   Press **S** to switch [Draft snapping](Draft_Snap.md) on or off.
-   Press the **Close** button to abort the command.

### Second task panel 


<div class="mw-translate-fuzzy">

-   Para introducir coordenadas manualmente, simplemente introduce los números, presiona **ENTER** entre cada componente X, Y y Z.
-   Las componentes X, Y, Z del segundo punto definen el factor de escala. Por ejemplo, (1,1,1) no hará nada, (2,2,2) utilizará un factor de escala scale 2x en todas las direcciones, (-1,1,1) hará una simetría en la dirección X.
-   Presionando **ALT** o **C** o pulsando el botón **'''Copiar'''** se creará una copia de los objetos, en lugar de escalar los originales. Si mantienes presionada **ALT** después de indicar el segundo punto, podrás crear más copias, hasta que liberes la tecla **ALT**.
-   Presiona **CTRL** mientras dibujas para forzar el [ajuste](Draft_Snap/es.md) de tu punto a la ubicación de ajuste más cercana, independientemente de la distancia.
-   Presionando **SHIFT** se bloqueará la relación de las coordenadas X e Y, de modo que la forma no se distorsione.
-   Presionando **ESC** o el botón **'''Cancelar'''** para abortar el comando actual.
-   El objeto resultante es una [clonación](Draft_Clone/es.md), que permite cambiar el valor de escala después de que se ha creado.


</div>

## Notes

-   The command can also scale [Image Planes](Image_CreateImagePlane.md), but not in clone mode.

## Preferences

See also   * [Preferences Editor](Preferences_Editor.md) and [Draft Preferences](Draft_Preferences.md).

-   To change the number of decimals used for the input of scale factors (<small>(v0.20)</small> ) and coordinates   * **Edit → Preferences... → General → Units → Units settings → Number of decimals**.
-   To change the number of decimals used for the input of scale factors ({{VersionMinus|0.19}})   * **Edit → Preferences... → Draft → General settings → General Draft Settings → Internal precision level**.
-   To reselect the base objects after copying objects   * **Edit → Preferences... → Draft → General settings → Draft tools options → Select base objects after copying**.

## Scripting


<div class="mw-translate-fuzzy">

## Programación


</div>


<div class="mw-translate-fuzzy">

La herramienta de Escalar se puede utilizar en [macros](macros/es.md) y desde la consola de Python utilizando la siguiente instrucción   *


</div>


```python
scaled_list = scale(objectslist, scale=Vector(1,1,1), center=Vector(0,0,0), copy=False)
```


<div class="mw-translate-fuzzy">

-   Escala los objetos contenidos en objects (que pueden ser una lista de objetos o un objeto) por los factores de escala definidos por el vector dado (en direcciones X, Y y Z) con respecto al centro dado.
-   Si legacy es True, se utiliza el modo directo (antiguo), en caso contrario se crea una copia paramétrica.
-   Si copy es True, los objetos en realidad no se mueven sino que se crean copias en su lugar.
-   Devuelve los objetos (o sus copias).


</div>

Ejemplo   *


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

pts = [App.Vector(0, 0, 0), App.Vector(500, 500, 0), App.Vector(600, 0, 0)]
wire1 = Draft.make_wire(pts, closed=True)
doc.recompute()

scale1 = App.Vector(2.3, 0.75, 0)
wire2 = Draft.scale(wire1, scale1, copy=True)
doc.recompute()

scale2 = App.Vector(-2, -1.5, 0)
wires = Draft.scale([wire1, wire2], scale2, copy=True)
doc.recompute()
```



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Scale/es
