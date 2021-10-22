---
- GuiCommand:/es
   Name:PartDesign Pad
   Name/es:DiseñoPieza Pastilla
   MenuLocation:DiseñoPieza → Crear una característica aditiva → Pastilla
   Workbenches:[DiseñoPiezas](PartDesign_Workbench/es.md)
   SeeAlso:[DiseñoPiezas Cajera](PartDesign_Pocket/es.md)
---

# PartDesign Pad/es

## Descripción

La **<img src="images/PartDesign_Pad.svg" width=16px> [DiseñoPieza Pastilla](PartDesign_Pad/es.md)** herramienta extrae un boceto en un sólido en una dirección normal al plano del boceto. A partir de {{VersionPlus/es|0.17}} las caras en el sólido también pueden ser utilizadas.

![](images/PartDesign_Pad_example.svg )

\"Boceto (A) mostrado a la izquierda; resultado final después de la operación de la pastilla (B) a la derecha\".

Nota:\'\' {{VersionMinus/es|0.16}} Si el croquis seleccionado se asigna a la cara de un sólido existente o a otra característica de diseño piezas, el pastilla se fusionará con él.

## Utilización

1.  Seleccione el boceto que se va acolchada. **Nota:** A partir de {{VersionPlus/es|0.17}} se puede utilizar alternativamente una cara del sólido existente.
2.  Pulse el **<img src="images/PartDesign_Pad.svg" width=16px> '''Pastilla'''**.
3.  Establezca los parámetros del Pastilla, vea las [Opciones](#Opciones.md) más abajo.
4.  Haga clic en **OK**.

## Opciones

Al crear un pastilla, la vista Combo cambia automáticamente al panel Tareas, mostrando el diálogo **Parámetros del pastilla**.

![](images/pad_parameters_cropped_es.png )

### Tipo

El tipo ofrece cinco formas diferentes de especificar la longitud a la que se extruirá la pastilla.

### Dimension

Introduce un valor numérico para la longitud del saliente. La dirección por defecto para la extrusión es saliendo del soporte, pero se puede cambiar seleccionando la opción **Invertir**. Las extrusiones se realizan normales [normales](http://en.wikipedia.org/wiki/Surface_normal) al plano de definición del croquis.

Con la opción **Simétrico al plano** el saliente se extenderá la mitad de la dimensión indicada hacia cada lado del plano de croquis.

No es posible indicar dimensiones negativas. Utiliza en cambio la opción **invertir**.

#### Dos dimensiones 

Permite introducir una segunda longitud en la cual el saliente debería extenderse en la dirección opuesta (dentro del soporte). De nuevo se puede cambiar seleccionado la opción **invertir**.

#### Hasta el último 

La pastilla se extruirá hasta la última cara del soporte en la dirección de extrusión. Si no hay soporte, aparecerá un mensaje de error.

#### Hasta el primero 

La pastilla se extruirá hasta la primera cara del soporte en la dirección de extrusión. Si no existe soporte, se mostrará un mensaje de error.

#### Hasta la cara 

La pastilla se extruirá hasta una cara del soporte que puede seleccionarse designándola. Si no existe soporte, no se aceptará ninguna selección.

### Longitud

Define la longitud de la pastilla. Se pueden utilizar múltiples unidades independientemente de las preferencias de unidades del usuario (m, cm, mm, nm, ft o \', in o \").

### Direction

#### Direction/edge

You can select the direction of the padding:

-   **Sketch normal** The sketch is extruded along its normal
-   **Select reference\...** The sketch is extruded along an edge of the 3D model. When this is method selected, you can click on any edge in the 3D model. This becomes then the direction vector for the padding. <small>(v0.20)</small> 
-   **Custom direction** The sketch is extruded along a direction that can be specified via vector values. <small>(v0.19)</small> 


<div class="mw-translate-fuzzy">

### Usar dirección personalizada 


</div>


<div class="mw-translate-fuzzy">


{{Version/es|0.19}}

Si está marcada, la dirección de la pastilla no será el vector normal del croquis sino el vector dado. Sin embargo, la longitud de la pastilla se establece de acuerdo con la dirección del vector normal.


</div>


<div class="mw-translate-fuzzy">

### Longitud a lo largo de la normal del boceto 


</div>

Si está marcada, la longitud de la pastilla se mide a lo largo de la normal del boceto, de lo contrario a lo largo de la dirección personalizada. {{Version/es|0.20}}

### Relleno a la cara 

Relleno desde la cara en la que terminará la pastilla. Esta opción sólo está disponible cuando **Tipo** es **Al último**, **Al primero** o **Hasta la cara**.

### Simétrico al plano 

Marque la casilla para extender la mitad de la longitud dada a cada lado del plano de croquis.

### Invertido

Invierte la dirección de la pastilla.

## Propiedades

-    **Type**: Type of ways how the pad will be extruded, see [Options](#Options.md).

-    **Length**: Defines the length of the pad, see [Options](#Options.md).

-    **Length2**: Second pad length in case the **Type** option **TwoLengths** is used, see [Options](#Options.md).

-    **Use Custom Vector**: <small>(v0.19)</small>  If checked, the pad direction will not be the normal vector of the sketch but the given vector, see [Options](#Options.md).

-    **Direction**: <small>(v0.19)</small>  Vector of the pad direction if **Use Custom Vector** is used.

-    **Along Sketch Normal**: <small>(v0.20)</small>  If *true*, the pad length is measured along the sketch normal. Otherwise and if **Use Custom Vector** is used, it is measured along the custom direction.

-    **Up To Face**: A face the pad will extrude up to, see [Options](#Options.md).

-    **Offset**: Offset from face in which the pad will end. This is only taken into account if the **Type** option **UpToLast**, **UpToFirst** or **UpToFace** is used.

-    **Refine**: <small>(v0.17)</small>  true or false. Cleans up residual edges left after the operation. This property is initially set according to the user\'s settings (found in *Preferences → Part design → General → Model settings*). It can be manually changed afterwards. This property will be saved with the FreeCAD document.

## Limitaciones


<div class="mw-translate-fuzzy">

-   Al igual que todas las características de Diseño piezas, Pastilla crea un sólido, por lo tanto, el boceto debe incluir un perfil cerrado o fallará con un error \"No se pudo validar la cara rota\". Puede haber múltiples perfiles cerrados dentro de uno más grande, siempre que ninguno se cruce entre sí (por ejemplo, un rectángulo con dos círculos en su interior).
-   El algoritmo utilizado para \'\' \'Al primero\' \'\' y \'\' \'Al último\' \'\' es:
    -   Crea una línea a través del centro de gravedad del boceto
    -   Encuentra todas las caras del soporte cortadas por esta línea
    -   Elija la cara donde el punto de intersección está más cerca / más alejado del boceto

:   Esto significa que la cara que se encuentra puede no ser siempre la que esperaba. Si se encuentra con este problema, utilice el tipo \'\' \'Up to face\' \'\' en su lugar y elija la cara que desee.
:   Para el caso muy especial de extrusión a una superficie cóncava, donde el boceto es más grande que esta superficie, la extrusión fallará. Este es un error no resuelto.

-    {{VersionMinus/es|0.16}}No hay limpieza automática, por ejemplo, de superficies planas adyacentes en una sola superficie. Puedes arreglar esto manualmente en el <img alt="" src=images/Workbench_Part.svg  style="width:16px;"> _ que crea una característica paramétrica.


</div>





{{PartDesign Tools navi

}}

---
[documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Pad/es
