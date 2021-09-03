---
- GuiCommand:/es
   Name:PartDesign Pocket
   Name/es:DiseñoPieza Cajera
   MenuLocation:DiseñoPieza → Crear una característica substractivo → Cajera
   Workbenches:[DiseñoPieza](PartDesign_Workbench/es.md)
   SeeAlso:[DiseñoPieza Pastilla](PartDesign_Pad/es.md)
---

## Descripción

La herramienta **Cajera** recorta un sólido extruyendo un boceto (o una cara del sólido) en una trayectoria recta y restándolo del sólido.

![](images/PartDesign_Pocket_example.svg ) El perfil del boceto (A) fue mapeado a la cara superior del sólido de la base (B); resultado después de cajear a través de la derecha. \'\'

## Uso

1.  Seleccione el croquis que se va a cajear.

    :   El croquis debe estar mapeado a la cara plana de un sólido existente o a una característica de Diseño Pieza, o aparecerá un mensaje de error. {{VersionMinus/es|0.16}}
2.  Pulse el **<img src="images/PartDesign_Pocket.svg" width=16px> '''Cajera''' **.
3.  Establezca los parámetros del Cajera (véase la siguiente sección).
4.  Haga clic en Aceptar.

## Opciones

![](images/Pocket_options_es.png )

Al crear una cajera, el cuadro de diálogo **Parámetros de la cajera** ofrece cinco formas diferentes de especificar la longitud (profundidad) a la que se extruirá la cajera:

### Dimensión

Introduzca un valor numérico para la profundidad de la cajera. La dirección por defecto de la extrusión es hacia el interior del soporte. Las extrusiones se producen [normal](http://en.wikipedia.org/wiki/Surface_normal) respecto al plano de croquis que las define. No son posibles las cotas negativas. Utilice la opción **Invertida** en su lugar.

### Al principio 

La cajera se extruirá hasta la primera cara del soporte en la dirección de extrusión. En otras palabras, cortará a través de todo el material hasta llegar a un espacio vacío.

### Por todo 

La cajera cortará todo el material en la dirección de extrusión. Con la opción **Simétrico al plano** la cajera cortará todo el material en ambas direcciones.**Nota:** Por razones técnicas, **por todo** es en realidad una cajera de 10 metros de profundidad. Si necesitas cajeras más profundos, utiliza *Dimensión*.

### Hasta la cara 

La cajera se extruirá hasta una cara del soporte que se puede elegir haciendo clic sobre ella.

### Dos dimensiones 

Permite introducir una segunda longitud en la que la cajera debe extenderse en sentido contrario (hacia el interior del soporte). De nuevo se puede cambiar marcando la opción **Invertida**. {{VersionPlus/es|0.17}}

## Limitaciones

-   Utiliza el tipo **Dimensión** o **Por todo** si es posible porque los otros tipos a veces dan problemas cuando se crea un patrón con ellos
-   En otros casos, la operación de cajera tiene las mismas [limitaciones](PartDesign_Pad/es#Limitaciones.md) que la operación de pastilla.

## Enlaces útiles 

Un [ejemplo](http://forum.freecadweb.org/viewtopic.php?f=3&t=3733&start=10) con la práctica en el foro.





{{PartDesign Tools navi

}} 
