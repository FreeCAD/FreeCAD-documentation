---
- GuiCommand:/es   Name:Arch Stairs   Name/es:Arch Stairs   Workbenches:[[Arch Module/es   Arch]]|MenuLocation:Arch → Stairs   Shortcut:S R---


</div>


<div class="mw-translate-fuzzy">

## Descripción

La herramienta de escaleras le permite construir automáticamente varios tipos de escaleras. Por el momento, solo se admiten escaleras rectas (con o sin un rellano central). Las escaleras se pueden construir desde cero, o desde una recta [line](Draft_Line.md), en cuyo caso las escaleras siguen la línea. Si la línea no es horizontal, pero tiene una inclinación vertical, las escaleras también seguirán su pendiente.


</div>

Consulte la entrada [Stairs en wikipedia](http://en.wikipedia.org/wiki/Stairs) para obtener una definición de los diferentes términos utilizados para describir las partes de las escaleras.

<img alt="" src=images/Arch_Stairs_example.jpg  style="width:640px;">


<div class="mw-translate-fuzzy">

*En la imagen de arriba, se crearon dos escaleras, una con una estructura masiva y un rellano, y otra con un único larguero.*


</div>

## Opciones

-   Las escaleras comparten las propiedades y comportamientos comunes de todos [ Arch Components](Arch_Component.md)


<div class="mw-translate-fuzzy">

## Utilización

Presiona el botón **<img src="images/Arch_Stairs.png" width=32px> Escaleras
**, o pulsa las teclas **S**, **R**

1.  Ajuste las propiedades deseadas. Algunas partes de las escaleras, como la estructura, pueden no aparecer inmediatamente, ya que alguna de las propiedades lo hace imposible, como un grosor de estructura de 0.


</div>

## Propiedades

### Datos

#### Arquitectura

-    {{PropertyData/es|Align}}: La alineación de las escaleras en su línea base, si es aplicable

-    {{PropertyData/es|Base}}: Editar (aún no implementado)

-    {{PropertyData/es|Height}}: La altura total de las escaleras

-    {{PropertyData/es|Length}}: La longitud total de las escaleras si no se ha definido ninguna línea base

-    {{PropertyData/es|Width}}: El ancho de las escaleras

#### Base

-    {{PropertyData/es|Label}}: Nombre de usuario del objeto (UTF8)

-    {{PropertyData/es|Placement}}:

#### Escalones

-    {{PropertyData/es|Nosing}}: Tamaño de las superposición de los peldaños

-    {{PropertyData/es|Number of risers}}: Número de peldaños en las escaleras

-    {{PropertyData/es|Riser Height}}: La altura de los peldaños

-    {{PropertyData/es|Tread Depth}}: La profundidad de las huellas

-    {{PropertyData/es|Tread Thickness}}: El espesor de las huellas

-    {{PropertyData/es|Align}}: La alineación de estas escaleras en su línea base, si corresponde.

-    {{PropertyData/es|Base}}: La línea base de estas escaleras, si hay alguna.

-    {{PropertyData/es|Height}}: La altura total de estas escaleras, si no se basa en una línea de base, o la línea de base es horizontal.

-    {{PropertyData/es|Length}}: La longitud total de estas escaleras si no se define una línea de base.

-    {{PropertyData/es|Width}}: El ancho de estas escaleras.

Escalones

-    {{PropertyData/es|Nosing}}: El tamaño de la nariz.

-    {{PropertyData/es|Number of Steps}}: La cantidad de escalones (peralte) en estas escaleras.

-    {{PropertyData/es|Riser Height}}: La altura de los peraltes

-    {{PropertyData/es|Tread Depth}}: La profundidad de las huellas.

-    {{PropertyData/es|Tread Thickness}}: El grosor de las huellas.

Estructura

-    {{PropertyData/es|Landings}}: El tipo de rellanos.

-    {{PropertyData/es|Stringer Offset}}: El desplazamiento entre el borde de las escaleras y la estructura.

-    {{PropertyData/es|Stringer Width}}: El ancho de los largueros.

-    {{PropertyData/es|Structure}}: El tipo de estructura de estas escaleras.

-    {{PropertyData/es|Structure Thickness}}: El espesor de la estructura.

-    {{PropertyData/es|Winders}}: Tipo de escalones no rectangulares


<div class="mw-translate-fuzzy">

## Limitaciones

-   No disponible antes de la versión 0.14 de FreeCAD
-   Solo escaleras rectas están disponibles en este momento
-   Ver la entrada [foro](http://forum.freecadweb.org/viewtopic.php?f=23&t=6534) para las escaleras en círculo.
-   Ver el [anuncio del foro](http://forum.freecadweb.org/viewtopic.php?f=9&t=4564).


</div>


<div class="mw-translate-fuzzy">

## Programación


</div>


<div class="mw-translate-fuzzy">

Las escaleras se pueden crear a partir de scripts de Python y [macros](macros/es.md) utilizando la siguiente función:


</div>


```python
Stairs = makeStairs(baseobj=None, length=None, width=None, height=None, steps=None, name="Stairs")
```


<div class="mw-translate-fuzzy">

-   Crea un objeto de escaleras con los atributos dados.
-   Devuelve el nuevo objeto de escaleras.


</div>

Ejemplo: 
```python
import Arch

Stairs = Arch.makeStairs(length=5000, width=1200, height=3000, steps=14)
```


<div class="mw-translate-fuzzy">


</div>


 

[Category:Arch/es](Category:Arch/es.md)
