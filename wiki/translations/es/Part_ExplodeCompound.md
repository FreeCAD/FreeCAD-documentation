---
- GuiCommand   */es
   Name   *Part ExplodeCompound
   Name/es   *Pieza ExplotarCompuesto
   MenuLocation   *Pieza → Compuesto → Explotar Compuesto
   Version   *0.18.15506
   Workbenches   *[Pieza](Part_Workbench/es.md)
   SeeAlso   *[Pieza Hacer Compuesto](Part_Compound/es.md), [Borrador Bajada](Draft_Downgrade/es.md)
---

# Part ExplodeCompound/es


</div>

## Descripción


<div class="mw-translate-fuzzy">

Herramienta para dividir compuestos de formas, para que cada forma contenida (niño) esté disponible como un objeto separado en el árbol modelo. Los niños se ponen automáticamente en un [Grupo](Std_Group/es.md) si hay más de un niño.


</div>

Es semiparamétrico   * las formas de los niños se actualizarán a medida que cambie el compuesto fuente, pero si se cambia el número de niños en el compuesto, la explosión o bien perderá algunas formas, o tendrá objetos redundantes en un estado de error.

Las colocaciones de las formas extraídas siguen las colocaciones de los originales, más la propiedad de colocación de cada niño.

La herramienta también explotará las formas no compuestas en sus constituyentes de nivel inferior   * los compsólidos en sólidos, los sólidos en conchas, las conchas en caras, las caras en cables, los cables en bordes, los bordes en vértices.

## Utilización

1.  Invocar la Herramienta de explotar piezas de compuesto de varias maneras   *
    -   Presionando en la <img alt="" src=images/Part_ExplodeCompound.svg  style="width   *24px;"> en la barra de herramientas de pieza
    -   Usando la **Pieza → Compuesto → Explotar compuesto** entrada en el Pieza menú

## Casos de uso 


<div class="mw-translate-fuzzy">

-   Ajustar las posiciones de las formas hechas por <img alt="" src=images/Draft_Array.svg  style="width   *24px;"> [Draft Array](Draft_Array/es.md)
-   Obtención de piezas divididas a partir del resultado de <img alt="" src=images/Part_Slice.svg  style="width   *24px;"> [Pieza Slice](Part_Slice/es.md) y <img alt="" src=images/Part_Cut.svg  style="width   *24px;"> [Pieza Cut](Part_Cut/es.md)
-   Obtención de contornos individuales a partir de bocetos y rostros multicontorno
-   Obtención de un sólido puro a partir de un sólido en compuesto, para su uso en <img alt="" src=images/Workbench_FEM.svg  style="width   *24px;"> [MEF Ambiente de trabajo](FEM_Workbench/es.md).


</div>


<div class="mw-translate-fuzzy">





</div>



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part ExplodeCompound/es
