---
- GuiCommand:/es
   Name:PartDesign LinearPattern
   Name/es:DiseñoPieza PatrónLineal
   MenuLocation:DiseñoPieza  →  Aplicar un patrón → PatrónLineal
   Workbenches:[DiseñoPieza](PartDesign_Workbench/es.md)
---

## Descripción

La herramienta **<img src=images/PartDesign_LinearPattern.svg style="width:24px"> '''PatrónLineal'''** crea copias de una operación a una misma distancia en dirección lineal. A partir de la v0.17 la herramienta de patrón lineal puede repetir múltiples operaciones. {{VersionPlus/es|0.17}}

![](images/PartDesign_LinearPattern_example.svg )

\'\'Arriba: Una forma extruida con forma de L (B) construida encima de una base extruida (A, también referida como *soporte*) es usada para crear un patrón lineal. El resultado (C) se muestra a la derecha.\'\'

## Uso

Para crear un patrón de repetición:

1.  Seleccionar la operación (u operaciones {{Version/es|0.19}}) que se han de repetir.
2.  Presionar el botón **<img src=images/PartDesign_LinearPattern.svg style="width:24px"> '''PatrónLineal'''** .
3.  Definir la **Dirección**. Ver [Opciones](#Options/es.md).
4.  Definir la **Longitud** (distancia) entre la que será la última copia y la figura original.
5.  Introducir el número de **Apariciones** o copias deseadas.
6.  Si hay varias operaciones en el patrón, su orden puede ser importante, ver por ejemplo la imagen de [PolarPattern feature](PartDesign_PolarPattern#Usage.md). {{Version/es|0.19}} Se puede cambiar el orden arrastrando la forma deseada en la lista e inmediatamente se puede apreciar el resultado como vista previa.
7.  Aceptar con **OK**.

Para añadir o borrar operaciones de un patrón existente:

1.  Pulsar el botón **Añadir una operación** para añadir una operación a repetir, la cual debe ser visible en la [vista 3D](3D_view/es.md).
    1.  Ir al árbol de dependencias de la pestaña Modelo.
    2.  Seleccionar en el árbol la operación que se tiene que añadir y presionar la **barra espaciadora** para hacerla visible en la [vista 3D](3D_view/es.md).
    3.  Volver al panel de tareas.
    4.  Seleccionar la operación en la vista 3D; será añadida a la lista.
    5.  Repetir para añadir más operaciones.
2.  Pulsar el botón **Eliminar operación** para quitar una operación de la lista, o pinchar con botón derecho del ratón sobre la operación en la lista y seleccionar *Eliminar*.

## Opciones

![Parámetros de PatrónLineal en la versión v0.16 y anteriores.](images/Linearpattern_parameters.png ) ![Parámetros de PatrónLineal en la versión v0.17 y posteriores.](images/Linearpattern_parameters_v017.png )

### Dirección

Mientras se crea una operación de repetición lineal, la ventana de diálogo de parámetros de repetición **Parámetros del PatrónLineal** ofrece diferentes maneras de especificar la dirección del patrón.

#### Eje horizontal del croquis {#eje_horizontal_del_croquis}

Usa el eje horizontal del boceto como dirección.

#### Eje vertical del croquis {#eje_vertical_del_croquis}

Usa el eje vertical del boceto como dirección.

#### Eje normal del croquis {#eje_normal_del_croquis}


{{VersionPlus/es|0.17}}

Usa el eje normal del croquis como dirección.

#### Seleccione referencia\... {#seleccione_referencia...}

Permite al usuario seleccionar una Línea de referencia o una arista de un objeto, o una línea de un boceto para usarla como dirección.

#### Eje del croquis personalizado {#eje_del_croquis_personalizado}

Si el boceto que define la operación a copiar contiene también una línea o líneas de construcción, la lista desplegable contendrá un eje de boceto personalizado por cada línea de construcción. La primera línea de construcción se llamará \'Línea de construcción 1\'.

#### Eje base (X/Y/Z) {#eje_base_xyz}


{{Version/es|0.17 o posteriores}}

Seleccionar uno de los ejes estándar de Origen del Body (cuerpo) (X, Y o Z) como dirección.


<div class="mw-translate-fuzzy">

## Limitaciones

-   Las formas del Patrón no deben superponerse unas con tras, excepto en el caso especial de que haya sólo dos repeticiones (el original más una copia)
-   Cualquier repetición que no se apoye sobre el soporte original será excluida. Con esto se asegura que una operación de PartDesign siempre sea de un único y conectado sólido.
-   Los patrones de repetición de PartDesign patterns ano están aún tan optimizados como sus equivalentes de Draft, por lo que para un número mayor de casos, debería considerar usar mejor la herramienta [Draft array](Draft_Array/es.md) , combinada con una operación booleana de Part. Esto puede incluir mayores cambios saliendo de PartDesign, lo que significa que no se tendría que simplemente continuar con operaciones posteriores en PartDesign en el mismo Body. Un ejemplo es mostrado en [Forum topic](https://forum.freecadweb.org/viewtopic.php?f=3&t=55192)
-   Para más limitaciones, [PartDesign Simetría](PartDesign_Mirrored/es.md)


</div>





{{PartDesign Tools navi

}} 
