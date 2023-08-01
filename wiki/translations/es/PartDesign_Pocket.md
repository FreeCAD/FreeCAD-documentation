---
- GuiCommand:/es
   Name:PartDesign Pocket
   Name/es:DiseñoPieza Cajera
   MenuLocation:DiseñoPieza → Crear una característica substractivo → Cajera
   Workbenches:[DiseñoPieza](PartDesign_Workbench/es.md)
   SeeAlso:[DiseñoPieza Pastilla](PartDesign_Pad/es.md)
---

# PartDesign Pocket/es


</div>

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

When selecting a single sketch, it can have multiple enclosed profiles inside a larger one, for example a rectangle with two circles inside it. But the profiles may not intersect each other. <small>(v0.20)</small> 


<div class="mw-translate-fuzzy">

## Opciones

![](images/Pocket_options_es.png )


</div>

When creating a pocket, the the **Pocket parameters** dialog will be shown. It offers the following settings:

![](images/pocket_parameters_cropped.png )

### Type

Type offers five different ways of specifying the length to which the pocket will be extruded:

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

The pocket will extrude through all objects in the extrusion direction. With the option **Symmetric to plane** the pad will cut through all material in both directions.**Note:** For technical reasons, *Through All* is actually a 10 meter deep pocket. If you need deeper pockets, use the type **Dimension**.

#### To first 

The pocket will extrude up to the first face of the support in the extrusion direction. In other words, it will cut through all material until it reaches an empty space.

#### Up to face 


<div class="mw-translate-fuzzy">

### Hasta la cara 

La cajera se extruirá hasta una cara del soporte que se puede elegir haciendo clic sobre ella.

### Dos dimensiones 

Permite introducir una segunda longitud en la que la cajera debe extenderse en sentido contrario (hacia el interior del soporte). De nuevo se puede cambiar marcando la opción **Invertida**. {{VersionPlus/es|0.17}}


</div>

#### Two dimensions 

This allows to enter a second length in which the pocket should extend in the opposite direction (into the support). The directions can be switched by ticking the **Reversed** option.

### Length

Defines the length of the pocket. Multiple units can be used independently of the user\'s units preferences (m, cm, mm, nm, ft or \', in or \"). This option is only available when **Type** is either **Dimension** or **Two dimensions**.

### Offset to face 

Offset from face at which the pocket will end. This option is only available when **Type** is either **Through all**, **To first** or **Up to face**.

### Direction


<small>(v0.20)</small> 

#### Direction/edge

You can select the direction of the extrusion:

-   **Face/Sketch normal** The sketch or face is extruded along its normal. If you have selected several sketches or faces to be extruded, the normal of the first one will be used. <small>(v0.20)</small> 
-   **Select reference\...** The sketch is extruded along an edge of the 3D model. When this is method selected, you can click on any edge in the 3D model and it becomes the direction vector for the extrusion.
-   **Custom direction** The sketch is extruded along a direction that can be specified via vector values.

#### Show direction 

If checked, the pocket direction will be shown. In case the pocket uses a **Custom direction**, it can be changed.

#### Length along sketch normal 

If checked, the pocket length is measured along the sketch normal, otherwise along the custom direction.

### Symmetric to plane 

Tick the checkbox to extrude half of the given length to either side of the sketch or plane.

### Reversed

Reverses the direction of the pocket.

### Taper angle 


<small>(v0.20)</small> 

Tapers the pocket in the extrusion direction by the given angle. A positive angle means the outer pocket border gets wider. This option is only available if **Type** is either **Dimension** or **Two dimensions**. Note that inner structures receive the opposite taper angle. This is done to facilitate the design of molds and molded parts.

Limitations:

-   Sketches containing [B-Splines](B-Splines.md) often cannot be properly tapered. This is a limitation of the [OpenCASCADE](OpenCASCADE.md) kernel that FreeCAD uses.
-   For larger angles tapering will fail if the end face of the pocket would have fewer edges than the start face/sketch.

### 2nd length 

Defines the length of the pocket in the opposite extrusion direction. Multiple units can be used independently of the user\'s units preferences (m, cm, mm, nm, ft or \', in or \"). This option is only available if **Type** is **Two dimensions**.

### 2nd taper angle 


<small>(v0.20)</small> 

Tapers the pocket in the opposite extrusion direction by the given angle. A positive angle means the outer pocket border gets wider. This option is only available if **Type** is **Two dimensions**. Note that inner structures receive the opposite taper angle. This is done to facilitate the design of molds and molded parts.

## Properties

-    **Type**: Type of ways how the pocket will be extruded, see [Options](#Options.md).

-    **Length**: Defines the length of the pocket, see [Options](#Options.md).

-    **Length2**: Second pocket length in case the **Type** is **TwoLengths**, see [Options](#Options.md).

-    **Use Custom Vector**: <small>(v0.20)</small>  If checked, the pocket direction will not be the normal vector of the sketch but the given vector, see [Options](#Options.md).

-    **Direction**: <small>(v0.20)</small>  Vector of the pocket direction if **Use Custom Vector** is used.

-    **Along Sketch Normal**: <small>(v0.20)</small>  If *true*, the pocket length is measured along the sketch normal. Otherwise and if **Use Custom Vector** is used, it is measured along the custom direction.

-    **Up To Face**: A face the pocket will extrude up to, see [Options](#Options.md).

-    **Refine**: True or false. Cleans up residual edges left after the operation. This property is initially set according to the user\'s settings (found in **Preferences → Part design → General → Model settings**). It can be manually changed afterwards. This property will be saved with the FreeCAD document.

## Limitations


<div class="mw-translate-fuzzy">

## Limitaciones

-   Utiliza el tipo **Dimensión** o **Por todo** si es posible porque los otros tipos a veces dan problemas cuando se crea un patrón con ellos
-   En otros casos, la operación de cajera tiene las mismas [limitaciones](PartDesign_Pad/es#Limitaciones.md) que la operación de pastilla.


</div>





{{PartDesign Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Pocket/es
