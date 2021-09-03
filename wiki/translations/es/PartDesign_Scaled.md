---
- GuiCommand:/es   Name:PartDesign_Scaled   Workbenches:[[PartDesign Workbench/es   Diseño de Piezas]], Complete|MenuLocation:Diseño de Piezas → MultiTransform---


</div>


<div class="mw-translate-fuzzy">

## Introducción

\'La operación Escalar\' - Esta operación toma un conjunto de uno o más operaciones seleccionadas como su entrada (los \'originales\'), y los escala por un factor dado. Ya que el escalado se realiza alrededor del centro de gravedad de las operaciones seleccionadas, normalmente desaparecen dentro de las versiones escaladas. Por tanto, normalmente sólo es útil utilizar escalar como parte de una operación de MultiTransformación.


</div>

\'Scale features\' - This tool takes a set of one or more selected features as its input (the \'originals\'), and scales them by a given factor. Since the scaling takes place around the centre of gravity of the selected features, they usually disappear inside the scaled versions. Therefore, normally it is only useful to use scaling as part of the MultiTransform feature.

Starting from FreeCAD 0.15, this operation is not available directly, but was incorporated into the [MultiTransform](PartDesign_MultiTransform.md) tool.

## Opciones

+----------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| ![](images/Scaled_parameters.png ) | Cuando se crea una operación de Escalar, el letrero de diálogo de \'parámetros de escalado\' ofrece las siguientes opciones:                              |
|                                                    |                                                                                                                                                           |
|                                                    | ### Selecionar los originales {#selecionar_los_originales}                                                                                                |
|                                                    |                                                                                                                                                           |
|                                                    | La lista que muestra los \'originales\' contiene las operaciones que van a ser escaladas. Seleccionado cualquier operación se añadirá a la lista.         |
|                                                    |                                                                                                                                                           |
|                                                    | ### Factor e instancias {#factor_e_instancias}                                                                                                            |
|                                                    |                                                                                                                                                           |
|                                                    | Especifica el máximo factor con respecto al cual la operaciones se van a escalar, y el número total de formas escaladas (incluida la operación original). |
+----------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+





<div class="mw-translate-fuzzy">

## Limitaciones

-   El escalado siempre se realiza con el centro de gravedad de la operación como punto base.
-   Mira la [operación de matriz lineal](PartDesign_LinearPattern/es.md) para ver más limitaciones





</div>

## Examples

![c\|center\|800px](images/mt_example2.png ) The smallest pad was first patterned three times in X direction and then scaled to factor two (so the three occurrences have scaling factor 1.0, 1.5 and 2.0). Then a polar pattern was applied with 8 occurrences.

Since the scaling is done with respect to the center of gravity, in the case of a pad, it is necessary that the pad penetrate also in the main body, otherwise the scaled objects are floating, detached from the body. To have a pad that intersects the main body can be used \"two dimensions\" type or \"simmetric to plane\" option. 
