# CAM Postprocessor Customization/es
}









## Introducción


<div class="mw-translate-fuzzy">

FreeCAD utiliza como representación interna para las trayectorias generadas, los llamados G-codes. Pueden describir cosas como: la velocidad y el avance, la parada del motor, etc\... Pero lo más importante son los movimientos que describen. Estos movimientos son bastante simples: Pueden ser líneas rectas o arcos circulares. Curvas más sofisticadas como las B-splines ya son aproximadas por el <img alt="" src=images/Workbench_Path.svg  style="width:24px;"> de FreeCAD. [Ambiente de trabajo Trayectoria](Path_Workbench/es.md).


</div>



## Lo que el postprocesador puede hacer por ti 


<div class="mw-translate-fuzzy">

Muchas fresadoras utilizan también G-codes para controlar el proceso de fresado. Pueden parecerse casi a los códigos internos, pero puede haber algunas diferencias:

-   la máquina puede tener una secuencia especial de arranque
-   puede tener una secuencia de parada especial
-   los arcos pueden definirse con un centro relativo o absoluto
-   puede requerir números de línea en un formato determinado
-   puede utilizar los llamados ciclos enlatados para subprocesos predefinidos como el taladrado
-   Puede que prefiera la salida de su G-code en unidades métricas o imperiales.
-   Podría ser útil realizar un conjunto de movimientos antes de llamar a un cambio de herramienta para facilitar la acción al operario
-   Puede que desee incluir comentarios para facilitar la lectura o suprimirlos para que el programa sea pequeño.
-   Puede que desee incluir una cabecera personalizada para identificar o documentar el programa para futuras referencias.
-   \...


</div>

Además, existen otros lenguajes para controlar un fresadora, como HPGL, DXF u otros.

El postprocesador es un programa que traduce los códigos internos en un archivo completo, que puede ser cargado en su máquina.



## Preparación para escribir su propio postprocesador 

Puede empezar con un modelo muy sencillo que muestre cómo su máquina lee las líneas rectas y los arcos. Prepárelo con cualquier programa adecuado para su máquina.

Un archivo para estas trayectorias que comienzan en (0,0,0) y van hacia Y sería útil. Asegúrese de que es la propia herramienta la que se mueve a lo largo de esta trayectoria, es decir, no debe aplicarse ninguna compensación del radio de la herramienta.

![](images/Path_PostProcessorSketch.png )

La trayectoria en FreeCAD tendría este aspecto. Tenga en cuenta la pequeña flecha azul, que indica la dirección de inicio. Para un primer intento puede proporcionar sólo un nivel en el plano XY.

![](images/Path_PostProcessorModel.png )


<div class="mw-translate-fuzzy">

A continuación, puede echar un vistazo al archivo y compararlo con la salida de los postprocesadores existentes como **linux_cnc_post.py** o **grbl_post.py** y tratar de adaptarlos usted mismo o subir el suyo al foro Path <https://forum.freecadweb.org/viewforum.php?f=15> para obtener ayuda.


</div>



## Convención de denominación 


<div class="mw-translate-fuzzy">

Para un formato de archivo **<filename>** el postprocesador debe obtener el nombre **<filename>_post.py**. Tenga en cuenta que **_post.py** tiene que estar en minúsculas.


</div>

The new name should be reflected at the head of the parser arguments list in the **<filename>_post.py** file, e.g.:


{{Code|lang=text|code=
parser = argparse.ArgumentParser(prog="grbl", add_help=False)
}}


<div class="mw-translate-fuzzy">

Si estás probando, colócalo en tu directorio de macros. Si funciona bien, por favor, considera proporcionarla para que otros se beneficien (publícala en el FreeCAD Path foro) para que pueda ser incluida en la distribución de FreeCAD en el futuro.


</div>



## Otros postprocesadores existentes 


<div class="mw-translate-fuzzy">

Para comparar puedes mirar los postprocesadores que vienen con tu instalación de FreeCAD. Se encuentran bajo el directorio Mod en Path/PathScripts/post. Los postprocesadores <img alt="" src=images/linuxcnc.png  style="width:64px;"> [linuxcnc](http://linuxcnc.org/) y <img alt="" src=images/grbl.png  style="width:64px;"> [grbl](https://github.com/grbl/grbl) son muy utilizados. El estudio de su código puede ser útil.

-   En Linux la ruta es /usr/share/freecad/Mod/Path/PathScripts/post


</div>




<div class="mw-translate-fuzzy">

## Programación de tu propio postprocesador 

Este post discute algunos aspectos internos de los postprocesadores linuxcnc. La misma estructura se utiliza en otros postprocesadores también.


</div>

This post discusses some internals from the linuxcnc postprocessors. The same strucure is used in other postprocessors as well.


<div class="mw-translate-fuzzy">

Mirando linux_cnc_post.py, verás la función de exportación (a partir de 0.19.20514 está en la línea 156)


</div>


```python
def export(objectslist, filename, argstring):
    # pylint: disable=global-statement
    ...
    gcode = ""
    ...
    ...
```


<div class="mw-translate-fuzzy">

Recoge paso a paso en la variable \"gcode\" los G-codes procesados y maneja la exportación general de los objetos post-procesables (operaciones, herramientas, trabajos, etc). La exportación maneja las cosas de alto nivel como los comentarios y el refrigerante, pero cualquier objeto que tenga múltiples comandos de ruta (cambios de herramientas y operaciones) se delega a la función de análisis (a partir de la versión 0.19.20514 está en la línea 288).


</div>


```python
def parse(pathobj):
    ...
    out = ""
    lastcommand = None
    ...
    ...
```


<div class="mw-translate-fuzzy">

De forma similar a la función \"export\", recoge los G-codes en la variable \"out\". En la variable \"command\" se almacenan los comandos vistos en la función \"inspect G-code\" del ambiente de trabajo ruta y se pueden investigar para su posterior procesamiento.


</div>


```python
        for c in pathobj.Path.Commands:

            command = c.Name
```

Reconoce los diferentes códigos G, M, F, S y otros G-codes. Recordando el último comando en la variable \"lastcommand\" puede suprimir las repeticiones posteriores de los comandos modales.

Tanto el parse como el export se limitan a formatear cadenas y concatenarlas en lo que será la salida final.

Verá que ambas funciones también llaman a la función \"linenumber()\". Si el usuario quiere números de línea, la función linenumber devuelve la cadena para pegar en el lugar apropiado, de lo contrario devuelve una cadena vacía para que no se añada nada.



## Relacionados


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_PostProcess.svg  style="width:24px;"> [Trayectoria ProcesoPuesto](Path_Post/es.md)


</div>





{{CAM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [CAM](CAM_Workbench.md) > CAM Postprocessor Customization/es
