---
 GuiCommand:
   Name: Draft SelectPlane
   Name/es: Borrador SeleccionarPlano
   MenuLocation: Borrador -> Seleccionar Plano
   Workbenches: Draft_Workbench/es, Arch_Workbench/es
   Shortcut: **W** **P**
   SeeAlso: Draft_WorkingPlaneProxy/es, Draft_ToggleGrid/es
---

# Draft SelectPlane/es


</div>



## Descripción


<div class="mw-translate-fuzzy">

El <img alt="" src=images/Workbench_Draft.svg  style="width:24px;"> [Ambiente de Trabajo Borrador](Draft_Workbench/es.md) cuenta con un sistema de planos de trabajo. Un plano en la [Vista 3D](3D_view/es.md) indica dónde se construirá una forma de Borrador. Hay varios métodos para definir el plano de trabajo:

-   A partir de una cara seleccionada
-   De tres vértices seleccionados.
-   A partir de la vista actual
-   A partir de una vista predefinida: Planta, alzado o perfil
-   Ninguno, en cuyo caso el plano de trabajo se adapta automáticamente a la vista actual cuando se inicia un comando, o a una cara si comienzas dibujando sobre una cara existente.


</div>


<small>(v1.0)</small> 

: For each 3D view a separate working plane is stored.

The ![](images/Draft_tray_button_plane.png ) button in the [Draft Tray](Draft_Tray.md) changes depending on the current working plane. <small>(v1.0)</small> : If the working plane is not set to **Auto** an asterisk (*****) is appended to the button label if the origin of the working plane does not match the global origin.

<img alt="" src=images/WorkingPlane_example.png  style="width:400px;">


<div class="mw-translate-fuzzy">



*Se pueden establecer diferentes planos de trabajo en los que dibujar las formas*


</div>

## Usage with pre-selection 


<div class="mw-translate-fuzzy">

1.  Selecciona una cara de un objeto existente en la [vista 3D](3D_view/es.md), o mantén pulsado **Ctrl** y selecciona tres vértices de cualquier objeto. {{Version/es|0.17}}
2.  Pulse el **<img src="images/Draft_SelectPlane.svg" width=16px> [SeleccionarPlano](Draft_SelectPlane/es.md)**, o haz clic con el botón derecho y selecciona **Utilidades → <img src="images/Draft_SelectPlane.svg" width=16px> [SeleccionarPlano](Draft_SelectPlane/es.md)**.


</div>

## Usage with post-selection 

1.  Invoke the command as explained above.
2.  The **Working plane setup** task panel opens. See [Options](#Options.md) for more information.
3.  Do one of the following:
    -   Select a single object. See the [previous paragraph](#Usage_with_pre-selection.md).
    -   Select one or more subelements. See the [previous paragraph](#Usage_with_pre-selection.md).
4.  Click anywhere in the [3D view](3D_view.md) to confirm the selection and finish the command.
5.  The working plane and the button in the [Draft Tray](Draft_Tray.md) are updated.

## Usage with presets 


<div class="mw-translate-fuzzy">

1.  Pulse el **<img src="images/Draft_SelectPlane.svg" width=16px> [SeleccinarPlano](Draft_SelectPlane/es.md)
**, o utilice **Borrador** → **Utilidades** → **<img src="images/Draft_SelectPlane.svg" width=16px> [SeleccinarPlano](Draft_SelectPlane/es.md)** del menú superior, o el atajo de teclado **W** y luego **P**
2.  Seleccione el desplazamiento, el espaciado de la cuadrícula y las líneas principales
3.  Seleccione uno de los preajustes: **<img src="images/View-top.svg" width=16px> XY (superior)**, **<img src="images/View-front.svg" width=16px> XZ (frontal)**, **<img src="images/View-right.svg" width=16px> YZ (lateral)**, **<img src="images/View-isometric.svg" width=16px> View**, o **<img src="images/View-axonometric.svg" width=16px> Auto**.


</div>



## Opciones


<div class="mw-translate-fuzzy">

-   Pulse el **<img src="images/View-top.svg" width=16px> XY (top)** para establecer el plano de trabajo en el plano XY. Para dibujar fácilmente en este plano, debes establecer la vista en la parte superior o inferior (la normal está en la dirección Z positiva o negativa). Pulsa **2** o **5** para cambiar rápidamente a estas vistas.
-   Pulse el **<img src="images/View-front.svg" width=16px> XZ (frontal)** para establecer el plano de trabajo en el plano XZ. Para dibujar fácilmente en este plano, debes fijar la vista en la parte delantera o trasera (la normal está en la dirección Y negativa o positiva). Pulsa **1** o **4** para cambiar rápidamente a estas vistas.
-   Pulse el **<img src="images/View-right.svg" width=16px> YZ (lateral)** para establecer el plano de trabajo en el plano YZ. Para dibujar fácilmente en este plano, debes fijar la vista en el lado izquierdo o derecho (la normal está en la dirección X positiva o negativa). Pulsa **3** o **6** para cambiar rápidamente a estas vistas.
-   Pulse el botón **<img src="images/View-isometric.svg" width=16px> Vista** para establecer el plano de trabajo en la vista 3D actual, perpendicular al eje de la cámara y pasando por el origen (0,0,0).
-   Pulse el botón **<img src="images/View-axonometric.svg" width=16px> Auto** para desajustar cualquier plano de trabajo actual, y establecer automáticamente un plano de trabajo cuando se utiliza una herramienta. Cuando se selecciona una herramienta de dibujo, la rejilla se actualiza automáticamente a la vista actual; entonces, si la vista se gira, y se selecciona otra herramienta, la rejilla se redibuja en la nueva vista. Esto equivale a pulsar **<img src="images/View-isometric.svg" width=16px> Vista** automáticamente antes de usar una herramienta.
-   Establecer el valor de \"Desplazamiento\" para fijar el plano de trabajo a una determinada distancia perpendicular del plano seleccionado.
-   Establezca el valor de \"Espaciado de la rejilla\" para definir el espacio entre cada línea de la rejilla.
-   Ajuste el valor \"Grid size\" para definir la extensión total del plano de la cuadrícula.
-   Ajuste el valor \"Línea principal cada\" para dibujar una línea ligeramente más gruesa en la cuadrícula en el valor establecido. Por ejemplo, si el espaciado de la cuadrícula es de 0,5 m, y hay una línea principal cada 20 líneas, habrá una línea ligeramente más gruesa cada 10 m.
-   Haga clic en la casilla \"Centrar el plano en la vista\" para dibujar el plano y la cuadrícula más cerca de la vista de la cámara en la vista 3D.
-   Pulse **Esc** o el botón **Close** para abortar el comando actual.
-   La rejilla muestra un borde adicional con el espacio de la línea principal indicado en la esquina inferior izquierda <small>(v0.19)</small> . Esto se puede desactivar a través de Edición-\>Preferencias-\>Borrador-\>Rejilla y ajuste-\>Mostrar borde de la rejilla


</div>

## Notes

-   It can be useful to align the [3D view](3D_view.md) with the selected Draft working plane. For example after switching the working plane to Front you may want to switch to the [Front view](Std_ViewFront.md) as well.
-   The grid can be toggled with the [Draft ToggleGrid](Draft_ToggleGrid.md) command.
-   By double-clicking [Draft WorkingPlaneProxies](Draft_WorkingPlaneProxy.md) in the [Tree view](Tree_view.md) you can quickly switch between working planes.

## Preferences

See also: [Preferences Editor](Preferences_Editor.md) and [Draft Preferences](Draft_Preferences.md).

-   The grid settings in the task panel as well as several other grid settings are available as preferences: **Edit → Preferences... → Draft → Grid and snapping**.
-   The Snapping radius can also be changed on-the-fly (see [Draft Snap](Draft_Snap#Preferences.md)) or by changing: **Tools → Edit parameters... → BaseApp → Preferences → Mod → Draft → snapRange**.

## Scripting


<div class="mw-translate-fuzzy">

## Guión


{{emphasis|Ver también:}}

[Fundamentos de Guión FreeCAD](FreeCAD_Scripting_Basics/es.md). Véase la [WorkingPlane API](http://www.freecadweb.org/api/DraftWorkingPlane.html).


</div>


<small>(v1.0)</small> 

The WorkingPlane module offers two classes to create working plane objects: the `PlaneBase` class and the `PlaneGui` class. The second class inherits from the first. Objects of the `PlaneGui` class interact with the GUI (the [Draft Tray](Draft_Tray.md) button), the [3D view](3D_view.md) and the [grid](Draft_Snap_Grid.md). `PlaneBase` objects do not.

Use the `get_working_plane()` method of the WorkingPlane module to get an instance of the `PlaneGui` class linked to the current 3D view. The method either returns the existing working plane linked to the view or creates a new working plane if required.


```python
import FreeCAD as App
import WorkingPlane

wp = WorkingPlane.get_working_plane()

origin = App.Vector(0, 0, 0)
normal = App.Vector(1, 1, 1).normalize()
offset = 17
wp.align_to_point_and_axis(origin, normal, offset)

point = App.Vector(10, 15, 2)
projection = wp.project_point(point)
print(projection)
```

The `PlaneBase` class can be used to create working planes independent of the GUI:


```python
import WorkingPlane

wp = WorkingPlane.PlaneBase()
```


<div class="mw-translate-fuzzy">





</div>



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft SelectPlane/es
