---
 GuiCommand:
   Name: PartDesign Pad
   Name/es: DiseñoPieza Pastilla
   MenuLocation: DiseñoPieza , Crear una característica aditiva , Pastilla
   Workbenches: PartDesign_Workbench/es
   SeeAlso: PartDesign_Pocket/es
---

# PartDesign Pad/es


</div>



## Descripción


<div class="mw-translate-fuzzy">

La **<img src="images/PartDesign_Pad.svg" width=16px> [DiseñoPieza Pastilla](PartDesign_Pad/es.md)** herramienta extrae un boceto en un sólido en una dirección normal al plano del boceto. A partir de {{VersionPlus/es|0.17}} las caras en el sólido también pueden ser utilizadas.


</div>

![](images/PartDesign_Pad_example.svg )

\"Boceto (A) mostrado a la izquierda; resultado final después de la operación de la pastilla (B) a la derecha\".



## Utilización


<div class="mw-translate-fuzzy">

1.  Seleccione el boceto que se va acolchada. **Nota:** A partir de {{VersionPlus/es|0.17}} se puede utilizar alternativamente una cara del sólido existente.
2.  Pulse el **<img src="images/PartDesign_Pad.svg" width=16px> '''Pastilla'''**.
3.  Establezca los parámetros del Pastilla, vea las [Opciones](#Opciones.md) más abajo.
4.  Haga clic en **OK**.


</div>



## Opciones


<div class="mw-translate-fuzzy">

Al crear un pastilla, la vista Combo cambia automáticamente al panel Tareas, mostrando el diálogo **Parámetros del pastilla**.


</div>


<div class="mw-translate-fuzzy">

![](images/pad_parameters_cropped_es.png )


</div>



### Tipo


<div class="mw-translate-fuzzy">

El tipo ofrece cinco formas diferentes de especificar la longitud a la que se extruirá la pastilla.


</div>



### Dimension


<div class="mw-translate-fuzzy">

Introduce un valor numérico para la longitud del saliente. La dirección por defecto para la extrusión es saliendo del soporte, pero se puede cambiar seleccionando la opción **Invertir**. Las extrusiones se realizan normales [normales](http://en.wikipedia.org/wiki/Surface_normal) al plano de definición del croquis.

Con la opción **Simétrico al plano** el saliente se extenderá la mitad de la dimensión indicada hacia cada lado del plano de croquis.

No es posible indicar dimensiones negativas. Utiliza en cambio la opción **invertir**.


</div>



#### Hasta el último 


<div class="mw-translate-fuzzy">

La pastilla se extruirá hasta la última cara del soporte en la dirección de extrusión. Si no hay soporte, aparecerá un mensaje de error.


</div>



#### Hasta el primero 


<div class="mw-translate-fuzzy">

La pastilla se extruirá hasta la primera cara del soporte en la dirección de extrusión. Si no existe soporte, se mostrará un mensaje de error.


</div>



#### Hasta la cara 


<div class="mw-translate-fuzzy">

La pastilla se extruirá hasta una cara del soporte que puede seleccionarse designándola. Si no existe soporte, no se aceptará ninguna selección.


</div>



#### Dos dimensiones 


<div class="mw-translate-fuzzy">

Permite introducir una segunda longitud en la cual el saliente debería extenderse en la dirección opuesta (dentro del soporte). De nuevo se puede cambiar seleccionado la opción **invertir**.


</div>

#### Up to shape 


<small>(v1.0)</small> 

: The pad will extend up to the selected shape. Optionally press the **Select shape** button and select a shape. Leave the **Select all faces** checkbox enabled or disable it, press the **Select faces** button and select the faces up to which the pad should be created.



### Relleno a la cara 


<div class="mw-translate-fuzzy">

Relleno desde la cara en la que terminará la pastilla. Esta opción sólo está disponible cuando **Tipo** es **Al último**, **Al primero** o **Hasta la cara**.


</div>



### Longitud


<div class="mw-translate-fuzzy">

Define la longitud de la pastilla. Se pueden utilizar múltiples unidades independientemente de las preferencias de unidades del usuario (m, cm, mm, nm, ft o \', in o \").


</div>

### 2nd length 

Defines the length of the pad in the opposite direction. This option is only available if **Type** is **Two dimensions**.



### Simétrico al plano 


<div class="mw-translate-fuzzy">

Marque la casilla para extender la mitad de la longitud dada a cada lado del plano de croquis.


</div>



### Invertido

Invierte la dirección de la pastilla.

### Direction

#### Direction/edge

You can select the direction of the extrusion:

-   **Sketch normal** or **Face normal:** The sketch or face is extruded in the direction of its normal. If you have selected several sketches or faces to be extruded, the normal of the first one will be used.
-   **Select reference\...:** The sketch or face is extruded in the direction of a straight edge or a [datum line](PartDesign_Line.md) selected from the Body.
-   **Custom direction:** The sketch or face is extruded in the direction of the specified vector.




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


<div class="mw-translate-fuzzy">

Si está marcada, la longitud de la pastilla se mide a lo largo de la normal del boceto, de lo contrario a lo largo de la dirección personalizada. {{Version/es|0.20}}


</div>

### Taper angle 

Tapers the pad in the extrusion direction by the given angle. A positive angle means the outer pad border gets wider. Note that inner structures receive the opposite taper angle. This is done to facilitate the design of molds and molded parts. This option is only available if **Type** is **Dimension** or **Two dimensions**.

### 2nd taper angle 

Tapers the pad in the opposite extrusion direction by the given angle. See **Taper angle**. This option is only available if **Type** is **Two dimensions**.



## Propiedades

### Data


{{TitleProperty|Pad}}

-    **Type|Enumeration**: Defines how the pad will be extruded, see [Options](#Options.md).

-    **Length|Length**: Defines the length of the pad, see [Options](#Options.md).

-    **Length2|Length**: Second pad length in case the **Type** is **TwoLengths**, see [Options](#Options.md).

-    **Use Custom Vector|Bool**: If checked, the pad direction will not be the normal vector of the sketch but the given vector, see [Options](#Options.md).

-    **Direction|Vector**: Vector of the pad direction if **Use Custom Vector** is used.

-    **Reference Axis|LinkSub**
    

-    **Along Sketch Normal|Bool**: If *true*, the pad length is measured along the sketch normal. Otherwise and if **Use Custom Vector** is used, it is measured along the custom direction.

-    **Up To Face|LinkSub**: A face the pad will extrude up to, see [Options](#Options.md).

-    **Offset|Length**: Offset from face in which the pad will end. This is only taken into account if the **Type** option **UpToLast**, **UpToFirst** or **UpToFace** is used.

-    **Taper Angle|Angle**
    

-    **Taper Angle2|Angle**
    


{{TitleProperty|Part Design}}

-    **Refine|Bool**: True or false. Cleans up residual edges left after the operation. This property is initially set according to the user\'s settings (found in **Preferences → Part Design → General → Model settings**).


{{TitleProperty|Sketch Based}}

-    **Profile|LinkSub**
    

-    **Midplane|Bool**
    

-    **Reversed|Bool**
    

-    **Allow Multi Face|Bool**
    



## Limitaciones


<div class="mw-translate-fuzzy">

-   Al igual que todas las características de Diseño piezas, Pastilla crea un sólido, por lo tanto, el boceto debe incluir un perfil cerrado o fallará con un error \"No se pudo validar la cara rota\". Puede haber múltiples perfiles cerrados dentro de uno más grande, siempre que ninguno se cruce entre sí (por ejemplo, un rectángulo con dos círculos en su interior).
-   El algoritmo utilizado para *\'Al primero\'* y *\'Al último\'* es:
    -   Crea una línea a través del centro de gravedad del boceto
    -   Encuentra todas las caras del soporte cortadas por esta línea
    -   Elija la cara donde el punto de intersección está más cerca / más alejado del boceto

:   Esto significa que la cara que se encuentra puede no ser siempre la que esperaba. Si se encuentra con este problema, utilice el tipo *\'Up to face\'* en su lugar y elija la cara que desee.
:   Para el caso muy especial de extrusión a una superficie cóncava, donde el boceto es más grande que esta superficie, la extrusión fallará. Este es un error no resuelto.

-    {{VersionMinus/es|0.16}}No hay limpieza automática, por ejemplo, de superficies planas adyacentes en una sola superficie. Puedes arreglar esto manualmente en el <img alt="" src=images/Workbench_Part.svg  style="width:16px;"> [Ambiente de trabajo Piezas](Part_Workbench/es.md) con **<img src="images/Part_RefineShape.svg" width=16px> [Piezas AfinarForma](Part_RefineShape/es.md)** (que crea un sólido no paramétrico no vinculado) o con el **<img src="images/OpenSCAD_RefineShapeFeature.svg" width=16px> [OpenSCAD FunciónRefinarForma](OpenSCAD_RefineShapeFeature/es.md)** del <img alt="" src=images/Workbench_OpenSCAD.svg  style="width:16px;"> [Ambiente de Trabajo de OpenSCAD](OpenSCAD_Workbench/es.md) que crea una característica paramétrica.


</div>


<div class="mw-translate-fuzzy">





</div>


{{PartDesign Tools navi

}}



---
⏵ [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Pad/es
