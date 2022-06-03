# Copying Objects/es
{{TOCright}}

## Overview


<div class="mw-translate-fuzzy">

## Vista general 

Como muchos otros programas, FreeCAD también tiene la capacidad de copiar/cortar y de pegar objetos (párrafos, celdas de hojas de cálculo, imágenes, etc.). [Documento](Document_structure/es.md) objetos pueden ser copiados libremente dentro de un documento o entre documentos usando el **<img src="images/Std_Copy.svg" width=24px>[Copiar](Std_Copy/es.md)**, **<img src="images/Std_Paste.svg" width=24px> [Pegar](Std_Paste/es.md)** y **[Duplicar la selección](Std_DuplicateSelection/es.md)** comandos.


</div>

![](images/Copy_past_duplicate.png )


<div class="mw-translate-fuzzy">

Por favor, considere que los objetos copiados no dependen del original. Si quieres clones dependientes por favor usa <img alt="" src=images/Draft_Clone.svg  style="width   *24px;"> [Clon del ambiente de trabajo Borrador](Draft_Clone/es.md) o <img alt="" src=images/PartDesign_Clone.svg  style="width   *24px;"> [ Clon del ambiente de trabajo DiseñoPiezas](PartDesign_Clone/es.md). Si necesita un clon dependiente o una réplica paramétrica, también puede usar <img alt="" src=images/Part_SimpleCopy.svg  style="width   *24px;"> [ La copia simple del ambiente de trabajo Piezas](Part_SimpleCopy/es.md). Para clones con patrones, por favor, mira en la [ sección Otros Métodos](Copying_Objects/es#Otros_Métodos.md) de esta página.


</div>

## Copying Linked Objects 


<div class="mw-translate-fuzzy">

## Notas

-   Si un objeto a copiar tiene enlaces a objetos que no están en la selección, FreeCAD preguntará si los objetos no seleccionados deben ser incluidos en la operación de copia. {{Version/es|0.14}}


</div>

## Finding and Positioning Pasted Object(s) 


<div class="mw-translate-fuzzy">

## Búsqueda y posicionamiento de los objetos pegados 

Después de la operación de Copiar/Pegar, puede que no sea obvio dónde se encuentran los nuevos objetos en la ventana del Documento. Esto se debe a que el nuevo objeto tiene la misma propiedad [Colocación](Placement/es.md) que el original. Active la propiedad Visibilidad (**Barra espaciadora**) para ocultar el original. A continuación, utilice el cuadro de diálogo Colocación para mover la copia a su posición correcta.


</div>

## Other Methods 


<div class="mw-translate-fuzzy">

## Otros métodos 

Como la mayoría de las cosas en FreeCAD, hay muchas maneras de hacer una copia. Para más ideas, mira   *

-   DiseñoPieza   * [Espejo](PartDesign_Mirrored/es.md), [Patrón lineal](PartDesign_LinearPattern/es.md), [Patrón polar](PartDesign_PolarPattern/es.md), [MultiTransformación](PartDesign_MultiTransform/es.md).
-   Pieza   * [Espejo](Part_Mirror/es.md), [Crear copia simple](Part_SimpleCopy/es.md)
-   Borrador   * [Desplazamiento](Draft_Offset/es.md), [Escala](Draft_Scale/es.md), [Arreglo](Draft_Array/es.md), [Arreglo Trayectoria](Draft_PathArray/es.md), [Clón](Draft_Clone/es.md), [Espejar](Draft_Mirror/es.md)


</div>



---
![](images/Right_arrow.png) [documentation index](../README.md) > Copying Objects/es
