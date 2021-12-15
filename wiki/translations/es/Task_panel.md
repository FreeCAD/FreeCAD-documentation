# Task panel/es
{{TOCright}}

## Introducción


<div class="mw-translate-fuzzy">

El [panel de tareas](task_panel/es.md) aparece en la pestaña **Tareas** de la [vista combinada](combo_view/es.md), uno de los paneles importantes de la [interfaz](interface/es.md). Es un espacio personalizable que puede contener cualquier tipo de widget gráfico como sub-ventanas plegables, tablas, campos de entrada, casillas de verificación, casillas de selección, cajas de texto, botones, etiquetas, imágenes y otros elementos, dependiendo del [Ambiente de trabajo](Workbenches/de.md) actualmente activo, y de la herramienta actualmente activa.


</div>

<img alt="" src=images/FreeCAD_Combo_view_Task_panel.png  style="width:" height="550px;">


<div class="mw-translate-fuzzy">



*El panel de tareas que muestra varios comandos cuando el [Ambiente de Trabajo DiseñoPieza](PartDesign_Workbench/es.md) está activo, y se selecciona un [Boceto](Sketch/es.md).*


</div>

## Trabajando con el panel de tareas 

Un panel de tareas normalmente se abre cuando se activa una herramienta que requiere la entrada del usuario, ya sea presionando un botón de la barra de herramientas o haciendo doble clic en un objeto. Si la herramienta no necesita la entrada del usuario, producirá su resultado o terminará, pero no mostrará un panel de tareas.

La entrada del usuario puede ser cualquier cosa como texto, coordenadas de puntos 3D, elementos de una lista, caras de una forma, u opciones para modificar la forma en que opera la herramienta.

![](images/FreeCAD_Combo_view_Task_panel_Sketcher.png )



*Panel de tareas que se abre cuando se edita un [Boceto](Sketch/es.md). Se presentan varios tipos de información como mensajes del solucionador, opciones de cuadrícula, restricciones y elementos geométricos.*


<div class="mw-translate-fuzzy">

Hay muchos comandos que requieren la selección de formas u objetos presentes en el documento; para tales casos el panel de tareas esperará a que el usuario seleccione los objetos apropiados de la [ vista de árbol](tree_view/es.md) o la [ vista 3D](3D_view/es.md). Cuando un panel de tareas está abierto, es posible cambiar a la pestaña **Modelo** para mostrar la [ vista de árbol](tree_view/es.md) para elegir un objeto; una vez hecho esto, es posible volver a la pestaña **Tareas** para proceder con el comando. El panel de tareas suele cerrarse pulsando un botón **OK** o un botón **Cerrar**, o pulsando la tecla **Esc** del teclado para abortar el comando.


</div>

![](images/FreeCAD_Combo_view_Task_panel_ArchComponent.png )


<div class="mw-translate-fuzzy">



*Panel de tareas que se abre cuando se edita un [Arch Componente](Arch_Component/es.md). El panel espera a que el usuario seleccione los objetos que pueden ser añadidos o sustraídos del componente.*


</div>

Nota: Por favor note que al cambiar de la pestaña **Tareas** a la pestaña **Modelo** no se termina el comando activo; la tarea seguirá ejecutándose en segundo plano. El usuario es responsable de terminar o abortar correctamente el comando activo antes de iniciar una tarea diferente; dejar una tarea en ejecución puede producir errores al intentar lanzar otras herramientas.

## Notes

-   Users migrating from other CAD solutions that use the **ESC** key as part of their workflow may get different results in FreeCAD. When **ESC** is pressed in FC if the task panel is in focus will auto-exit the task panel. To disable this functionality, please see [Escape Key](Fine-tuning#Escape_Key.md).

## Guión


**Por favor, reformula y actualiza esta sección**

Ver [Hilo del foro](https://forum.freecadweb.org/viewtopic.php?f=10&t=44170&p=376759#p376759) Llamada que un widget de Diálogo de Tareas puede usar para cerrar la Vista de Tareas. Puede cerrarse con \"this-\>close()\", pero eso sólo cierra la parte inferior de la vista, no la vista en sí misma.

Usando python: 
```python
Gui.Control.closeDialog()
```

Usando c++: 
```python
Gui::Control().closeDialog();
```


{{Interface navi

}}

---
[documentation index](../README.md) > Task panel/es
