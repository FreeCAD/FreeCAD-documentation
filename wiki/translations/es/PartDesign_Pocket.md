---
 GuiCommand:
   Name: PartDesign Pocket
   Name/es: DiseñoPieza Cajera
   MenuLocation: Part Design , Crear una característica substractivo , Cajera
   Workbenches: PartDesign_Workbench/es
   SeeAlso: PartDesign_Pad/es
---

# PartDesign Pocket/es

## Description


<div class="mw-translate-fuzzy">

## Descripción

La herramienta **Cajera** recorta un sólido extruyendo un boceto (o una cara del sólido) en una trayectoria recta y restándolo del sólido.


</div>

![](images/PartDesign_Pocket_example.svg ) El perfil del boceto (A) fue mapeado a la cara superior del sólido de la base (B); resultado después de cajear a través de la derecha. \'\'

## Usage


<div class="mw-translate-fuzzy">

## Uso

1.  Seleccione el croquis que se va a cajear.

    :   El croquis debe estar mapeado a la cara plana de un sólido existente o a una característica de Diseño Pieza, o aparecerá un mensaje de error. {{VersionMinus/es|0.16}}
2.  Pulse el **<img src="images/PartDesign_Pocket.svg" width=16px> '''Cajera''' **.
3.  Establezca los parámetros del Cajera (véase la siguiente sección).
4.  Haga clic en Aceptar.


</div>




<div class="mw-translate-fuzzy">

## Opciones

![](images/Pocket_options_es.png )


</div>

When creating a pocket, or after double-clicking an existing pocket in the [Tree view](Tree_view.md), the **Pocket parameters** task panel is shown. It offers the following settings:

![](images/PartDesign_Pocket_Taskpanel.png )

### Type

Type offers five different ways of specifying the length of the pocket:

#### Dimension


<div class="mw-translate-fuzzy">

Al crear una cajera, el cuadro de diálogo **Parámetros de la cajera** ofrece cinco formas diferentes de especificar la longitud (profundidad) a la que se extruirá la cajera:

### Dimensión

Introduzca un valor numérico para la profundidad de la cajera. La dirección por defecto de la extrusión es hacia el interior del soporte. Las extrusiones se producen [normal](http://en.wikipedia.org/wiki/Surface_normal) respecto al plano de croquis que las define. No son posibles las cotas negativas. Utilice la opción **Invertida** en su lugar.

### Al principio 

La cajera se extruirá hasta la primera cara del soporte en la dirección de extrusión. En otras palabras, cortará a través de todo el material hasta llegar a un espacio vacío.

### Por todo 

La cajera cortará todo el material en la dirección de extrusión. Con la opción **Simétrico al plano** la cajera cortará todo el material en ambas direcciones.**Nota:** Por razones técnicas, **por todo** es en realidad una cajera de 10 metros de profundidad. Si necesitas cajeras más profundos, utiliza *Dimensión*.


</div>

#### Through all 

The pocket will extend up to the last face of the support it encounters in its direction. With the option **Symmetric to plane** the pocket will cut through all material in both directions. Note that for technical reasons, *Through All* is actually a 10 meter deep pocket. If you need deeper pockets, use the type **Dimension**.

#### To first 

The pocket will extend up to the first face of the support it encounters in its direction.

#### Up to face 


<div class="mw-translate-fuzzy">

### Hasta la cara 

La cajera se extruirá hasta una cara del soporte que se puede elegir haciendo clic sobre ella.

### Dos dimensiones 

Permite introducir una segunda longitud en la que la cajera debe extenderse en sentido contrario (hacia el interior del soporte). De nuevo se puede cambiar marcando la opción **Invertida**. {{VersionPlus/es|0.17}}


</div>

#### Two dimensions 

This allows to enter a second length in which the pocket should extend in the opposite direction. The directions can be switched by checking the **Reversed** option.

#### Up to shape 


<small>(v1.0)</small> 

: The pocket will extend up to the selected shape. Optionally press the **Select shape** button and select a shape. Leave the **Select all faces** checkbox enabled or disable it, press the **Select** button and select the faces up to which the pocket should be created.

### Offset to face 

Offset from face at which the pocket will end. This option is only available if **Type** is **Through all**, **To first** or **Up to face**.

### Length

Defines the length of the pocket. This option is only available if **Type** is **Dimension** or **Two dimensions**. The length is measured along the direction vector, or along the normal of the sketch or face. Negative values are not possible. Use the **Reversed** option instead.

### 2nd length 

Defines the length of the pocket in the opposite direction. This option is only available if **Type** is **Two dimensions**.

### Symmetric to plane 

Check this option to extrude half the given length to either side of the sketch or face, if **Type** is **Dimension**, or **Through all** if that is the **Type**.

### Reversed

Reverses the direction of the pocket.

### Direction

#### Direction/edge

You can select the direction of the extrusion:

-   **Sketch normal** or **Face normal:** The sketch or face is extruded in the opposite direction of its normal. If you have selected several sketches or faces to be extruded, the normal of the first one will be used.
-   **Select reference\...:** The sketch or face is extruded in the opposite direction of a straight edge or a [datum line](PartDesign_Line.md) selected from the Body.
-   **Custom direction:** The sketch or face is extruded in the direction of the specified vector.

#### Show direction 

If checked, the pocket direction will be shown. In case the pocket uses a **Custom direction**, it can be changed.

#### Length along sketch normal 

If checked, the pocket length is measured along the sketch or face normal, otherwise along the custom direction.

### Taper angle 

Tapers the pocket in the extrusion direction by the given angle. A positive angle means the outer pocket border gets wider. Note that inner structures receive the opposite taper angle. This is done to facilitate the design of molds and molded parts. This option is only available if **Type** is **Dimension** or **Two dimensions**.

### 2nd taper angle 

Tapers the pocket in the opposite extrusion direction by the given angle. See **Taper angle**. This option is only available if **Type** is **Two dimensions**.

## Properties

### Data


{{TitleProperty|Part Design}}

-    **Refine|Bool**: True or false. Cleans up residual edges left after the operation. This property is initially set according to the user\'s settings (found in **Preferences → Part Design → General → Model settings**).


{{TitleProperty|Pocket}}

-    **Type|Enumeration**: Defines how the pocket will be extruded, see [Options](#Options.md).

-    **Length|Length**: Defines the length of the pocket, see [Options](#Options.md).

-    **Length2|Length**: Second pocket length in case the **Type** is **TwoLengths**, see [Options](#Options.md).

-    **Use Custom Vector|Bool**: If checked, the pocket direction will not be the normal vector of the sketch but the given vector, see [Options](#Options.md).

-    **Direction|Vector**: Vector of the pocket direction if **Use Custom Vector** is used.

-    **Reference Axis|LinkSub**
    

-    **Along Sketch Normal|Bool**: If *true*, the pocket length is measured along the sketch normal. Otherwise and if **Use Custom Vector** is used, it is measured along the custom direction.

-    **Up To Face|LinkSub**: A face the pocket will extrude up to, see [Options](#Options.md).

-    **Offset|Length**
    

-    **Taper Angle|Angle**
    

-    **Taper Angle2|Angle**
    


{{TitleProperty|Sketch Based}}

-    **Profile|LinkSub**
    

-    **Midplane|Bool**
    

-    **Reversed|Bool**
    

-    **Allow Multi Face|Bool**
    

## Limitations


<div class="mw-translate-fuzzy">

## Limitaciones

-   Utiliza el tipo **Dimensión** o **Por todo** si es posible porque los otros tipos a veces dan problemas cuando se crea un patrón con ellos
-   En otros casos, la operación de cajera tiene las mismas [limitaciones](PartDesign_Pad/es#Limitaciones.md) que la operación de pastilla.


</div>





{{PartDesign Tools navi

}}



---
⏵ [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Pocket/es
