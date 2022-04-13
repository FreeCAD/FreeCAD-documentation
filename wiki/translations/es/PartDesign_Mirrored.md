---
- GuiCommand:/es
   Name:PartDesign Mirrored
   Name/es:PartDesign Simetría
   MenuLocation:PartDesign → Apply a pattern → Simetría
   Workbenches:[PartDesign](PartDesign_Workbench/es.md)
---

# PartDesign Mirrored/es


</div>

## Descripción


<div class="mw-translate-fuzzy">

La herramienta **Simetría** realiza una operación de simetría o espejo sobre un plano. A partir de la versión v0.17, se pueden hacer simetrías de múltiples operaciones.


</div>

![](images/PartDesign_Mirrored_example.svg )



*Arriba: Una operación de vaciado fue creada desde un boceto que contenía un círculo (A). Dicho vaciado fue usado posteriormente para crear una operación de Simetría. El eje vertical del boceto (B) se usó como eje de simetría. El resultado se muestra a la derecha. (C) *

## Uso


<div class="mw-translate-fuzzy">

Para crear una simetría:

1.  Seleccionar la forma o formas que se desea hacer simétricas. {{Version/es|0.19}}
2.  Pulsar el botón **[<img src=images/PartDesign_Mirrored.svg style="width:24px"> '''Crear una operación simétrica'''** .
3.  Si se va a realizar la operación con varias formas, el orden de las mismas puede ser importante, ver un ejemplo de imagen en [PartDesign PolarPattern](PartDesign_PolarPattern#Usage.md). {{Version/es|0.19}} Se puede cambiar el orden arrastrando la forma deseada en la lista e inmediatamente se puede apreciar el resultado como vista previa.
4.  Definir el **Plano** de simetría. Ver [Opciones](#Options/es.md).
5.  Presionar **OK** para confirmar.


</div>


<div class="mw-translate-fuzzy">

Para añadir o borrar operaciones de una simetría existente:

1.  Pulsar el botón **Añadir una operación** para añadir una operación a la simetría, la cual debe ser visible en la [vista 3D](3D_view/es.md):
    1.  Ir al árbol de dependencias de la pestaña Modelo;
    2.  Seleccionar en el árbol la operación que se tiene que añadir y presionar la **barra espaciadora** para hacerla visible en la [vista 3D](3D_view/es.md);
    3.  Volver al panel de tareas;
    4.  Seleccionar la operación en la vista 3D; será añadida a la lista.
    5.  Repetir si se desea añadir más operaciones.
2.  Pulsar el botón **Eliminar operación** para quitar una operación de la lista, o pinchar con botón derecho del ratón sobre la operación en la lista y seleccionar *Eliminar*.


</div>

## Opciones


<div class="mw-translate-fuzzy">

![Parámetros de Simetría en la versión v0.16 y anteriores.](images/mirrored_parameters.png ) ![Parámetros de Simetría en la versión v0.17 y posteriores.](images/Mirrored_parameters_v017.png )


</div>

### Plano

Mientras se crea una operación de simetría, la ventana de diálogo de parámetros de simetría **Mirrored parameters** ofrece diferentes maneras de especificar un plano o línea de simetría.

#### Eje horizontal del boceto 

Usa el eje horizontal del boceto como eje de simetría.

#### Eje vertical del boceto 

Usa el eje vertical del boceto como eje de simetría.

#### Seleccione referencia\... 

Permite al usuario seleccionar un plano (como puede ser una cara o un objeto) para usarlo como plano de simetría.

#### Eje del boceto personalizado 

Si el boceto que define la simetría a realizar contiene también una línea o líneas de construcción, la lista desplegable contendrá un eje de boceto personalizado por cada línea de construcción. La primera línea de construcción se llamará \'Línea de construcción 1\'. La imagen inferior es un ejemplo, con el boceto en modo edición, que muestra una línea de construcción contenida en el boceto y es usada como eje de Simetría.

![](images/PartDesign_Mirrored_axis_fromconstructionlines.jpg )

#### Base plano (XY/XZ/YZ) 

Seleccionar uno de los planos estándar de Origen del Body (cuerpo) (XY, XZ or YZ).

### Previsualización

La simetría resultante puede ser vista de forma predeterminada en tiempo real antes de aceptar pulsando el botón **OK** habiendo marcado la casilla \"Actualizar vista\" . 

## Limitaciones


<div class="mw-translate-fuzzy">

-   No se puede realizar una operación de simetría con un sólido completo. Para ello, ver [Part Mirror](Part_Mirror/es.md) .


</div>





{{PartDesign Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Mirrored/es
