---
- GuiCommand:
   Name:Arch Stairs
   Name/es:Arch Stairs
   Workbenches:[Arch](Arch_Workbench/es.md)
   MenuLocation:Arch - Stairs
   Shortcut:**S** **R**
---

# Arch Stairs/es


</div>

## Description


<div class="mw-translate-fuzzy">

## Descripción

La herramienta de escaleras le permite construir automáticamente varios tipos de escaleras. Por el momento, solo se admiten escaleras rectas (con o sin un rellano central). Las escaleras se pueden construir desde cero, o desde una recta [line](Draft_Line.md), en cuyo caso las escaleras siguen la línea. Si la línea no es horizontal, pero tiene una inclinación vertical, las escaleras también seguirán su pendiente.


</div>


<div class="mw-translate-fuzzy">

Consulte la entrada [Stairs en wikipedia](http://en.wikipedia.org/wiki/Stairs) para obtener una definición de los diferentes términos utilizados para describir las partes de las escaleras.


</div>

<img alt="" src=images/Arch_Stairs_example.jpg  style="width:600px;">


<div class="mw-translate-fuzzy">

*En la imagen de arriba, se crearon dos escaleras, una con una estructura masiva y un rellano, y otra con un único larguero.*


</div>



## Opciones


<div class="mw-translate-fuzzy">

-   Las escaleras comparten las propiedades y comportamientos comunes de todos [ Arch Components](Arch_Component.md)


</div>

## Usage


<div class="mw-translate-fuzzy">

## Utilización

Presiona el botón **<img src="images/Arch_Stairs.png" width=32px> Escaleras
**, o pulsa las teclas **S**, **R**

1.  Ajuste las propiedades deseadas. Algunas partes de las escaleras, como la estructura, pueden no aparecer inmediatamente, ya que alguna de las propiedades lo hace imposible, como un grosor de estructura de 0.


</div>

<img alt="" src=images/Arch_Stairs_Complex_Example.png  style="width:600px;"> 
*Complex stairs based on a selection of lines and wired as shown on the left.<br>
In red the wires used for the landings at Z&equals;1500mm, Z&equals;3000mm and Z&equals;4500mm.<br>
In black the lines connecting them used for the flights.
*



## Propiedades

### Data


{{TitleProperty|Segment and Parts}}

-    **Abs Top|Vector**: (read-only) The absolute top level the stairs lead to.

-    **Last Segment|Link**: Last segment (flight or landing) of an Arch Stairs connecting to this segment. The start level of the stairs will be the end level of this last segment.

-    **Outline Left|VectorList**: The left outline of the stairs.

-    **Outline Left All|VectorList**: The left outline of all segments of the stairs.

-    **Outline Right|VectorList**: The right outline of the stairs.

-    **Outline Right All|VectorList**: The right outline of all segments of the stairs.

-    **Railing Height Left|Length**: Height of the left railing of the stairs or landing.

-    **Railing Height Right|Length**: Height of the right railing of the stairs or landing.

-    **Railing Left|LinkHidden**: The left railing object. <small>(v0.20)</small> : Property type updated from {{Incode|String}} to {{Incode|LinkHidden}}.

-    **Railing Offset Left|Length**: Offset of the left railing from the edge of the stairs or landing.

-    **Railing Offset Right|Length**: Offset of the right railing from the edge of the stairs or landing.

-    **Railing Right|LinkHidden**: The right railing object. <small>(v0.20)</small> : Property type updated from {{Incode|String}} to {{Incode|LinkHidden}}.


{{TitleProperty|Stairs}}


<div class="mw-translate-fuzzy">

-    {{PropertyData/es|Align}}: La alineación de estas escaleras en su línea base, si corresponde.

-    {{PropertyData/es|Base}}: La línea base de estas escaleras, si hay alguna.

-    {{PropertyData/es|Height}}: La altura total de estas escaleras, si no se basa en una línea de base, o la línea de base es horizontal.

-    {{PropertyData/es|Length}}: La longitud total de estas escaleras si no se define una línea de base.

-    {{PropertyData/es|Width}}: El ancho de estas escaleras.


</div>


<div class="mw-translate-fuzzy">

Escalones


</div>


<div class="mw-translate-fuzzy">

-    {{PropertyData/es|Nosing}}: El tamaño de la nariz.

-    {{PropertyData/es|Number of Steps}}: La cantidad de escalones (peralte) en estas escaleras.

-    {{PropertyData/es|Riser Height}}: La altura de los peraltes

-    {{PropertyData/es|Tread Depth}}: La profundidad de las huellas.

-    {{PropertyData/es|Tread Thickness}}: El grosor de las huellas.


</div>


<div class="mw-translate-fuzzy">

Estructura


</div>


<div class="mw-translate-fuzzy">

-    {{PropertyData/es|Landings}}: El tipo de rellanos.

-    {{PropertyData/es|Stringer Offset}}: El desplazamiento entre el borde de las escaleras y la estructura.

-    {{PropertyData/es|Stringer Width}}: El ancho de los largueros.

-    {{PropertyData/es|Structure}}: El tipo de estructura de estas escaleras.

-    {{PropertyData/es|Structure Thickness}}: El espesor de la estructura.

-    {{PropertyData/es|Winders}}: Tipo de escalones no rectangulares


</div>

## Limitations


<div class="mw-translate-fuzzy">

## Limitaciones

-   No disponible antes de la versión 0.14 de FreeCAD
-   Solo escaleras rectas están disponibles en este momento
-   Ver la entrada [foro](http://forum.freecadweb.org/viewtopic.php?f=23&t=6534) para las escaleras en círculo.
-   Ver el [anuncio del foro](http://forum.freecadweb.org/viewtopic.php?f=9&t=4564).


</div>

## Scripting


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



---
![](images/Button_right.svg) [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch Stairs/es
