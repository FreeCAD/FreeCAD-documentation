---
- GuiCommand:/es
   Name:Sketcher External
   Name/es:Croquizador Externo
   MenuLocation:Croquis → Croquizador Geometrías → Croquizador Externo
   Workbenches:[Croquizador](Sketcher_Workbench/es.md)
   Shortcut:X
   SeeAlso:[Croquizador ModoConstrucción](Sketcher_ToggleConstruction/es.md)
---

## Descripción

Usa la herramienta **<img src="images/Sketcher_External.svg" width=16px> [Geometría externa](Sketcher_External/es.md)** cuando necesites aplicar una restricción entre la geometría del croquis y algo fuera del mismo. Funciona insertando una geometría de construcción vinculada en el croquis. El color por defecto de los bordes vinculadas externamente es el magenta. Al igual que con la geometría de construcción no vinculada estándar (azul), la geometría vinculada externamente sólo es visible cuando el croquis está en modo de edición y no se utiliza directamente en el resultado posterior del uso del croquis en otra herramienta. Ambos tipos de geometría de construcción pueden utilizarse como referencia para las restricciones dentro del croquis.

Una nota de precaución, usar esta herramienta para enlazar con la geometría (sólida) generada puede llevar a resultados inesperados debido a [Problema de denominación topológica](Topological_naming_problem/es.md). Vea también [Consejo para modelos estables](Feature_editing/es#Consejo_para_modelos_estables.md).

<FILE:Sketcher_ExternalEsempio1.png>

## Utilización

-   Crear un nuevo croquis, o abrir un croquis existente.
-   Haga clic en el botón \'Croquizador Externo\'.
-   Selecciona un borde o un vértice que quieras enlazar en el croquis.
-   Pulsa Esc, o selecciona otra herramienta para dejar de importar geometría al croquis.

### Reglas de selección 

-   Sólo se permiten bordes y vértices de objetos del mismo sistema de coordenadas.

Es decir, el croquis y el objeto deben estar en el mismo cuerpo (en el ambiente de trabajo de Diseño Piezas), o en la misma Pieza (en el ambiente de trabajo Pieza), o ambos fuera de cualquier pieza y cuerpo.

For example, If the open sketch is in Body, you can use another sketch from Body as external geometry, but you can\'t use a sketch from Body001, or an edge from a Part Cube in the root of the project. Use Shapebinder feature to bring in a copy of the object into the coordinate system of open sketch. Then you will be able to use edges/vertices of Shapebinder object.

-   No circular dependencies are allowed.

That means, you can\'t link to Pocket made with this sketch. You can\'t link to any object that depends on the sketch.

Sketch doesn\'t have to be on any face in order to use this tool. Links directly between sketches are possible, and encouraged, as they are more reliable.

### Appearance When Successfully Linked 

A (default magenta) coloured line will be overlaid when an edge is successfully linked (the vertices will be red), and will be visible in your sketch only while your sketch is in edit mode.

### Similarity to Construction Lines 

External geometry (default colour magenta) lines are similar (default colour blue) [Contruction lines](Sketcher_ToggleConstruction.md) except in that the external geometry magenta lines are parametrically linked back to an element of the solid to which the sketch is mapped. Construction geometry are lines that are internal to the sketch, are only visible when the sketch is in edit mode and will be used for constraint references only, and not directly for later solid operations, like Pad or Pocket.

### Use Of External Geometry in a PartDesign Workbench Work Flow 

In the PartDesign workbench work flow, the External Geometry tool is used to assist in the positioning of an aspect of the solid you are constructing, relative to the previous stage in its construction. PartDesign workbench is intended to produce one single solid, therefore these sketches with external geometry are used to create a new feature of that one single solid.

The external geometry can, for example, be used as a reference for a constraint being used to position a hole in an object at a specific location relative to an edge or vertex.

### Uso de la geometría externa en un flujo de trabajo del ambiente de trabajo Pieza 

You can use any Part geometry that is in coordinate system of the sketch. It is advised to link to the earliest feature possible, as it forms a more stable link.

## Ejemplo

This, below, is a sketch mapped to the top face of a solid created from a Pad of a previous sketch. The magenta lines are External Geometry linked to two edges of this pre-existing Pad.

In this case they are used as a reference for tangency constraints with the circumferences of one circle. They are also used as the reference for a horizontal and a vertical constraint to locate the centre of the second circle relative to the end and top of the Pad.

<FILE:Sketcher_ExternalEsempio2.png>

This is the same sketch in edit mode, with the Pad upon which it is mapped hidden.

<FILE:Sketcher_ExternalEsempio4.png>

When the sketch edit mode is closed, external Geometry lines are not visible.

<FILE:Sketcher_ExternalEsempio3.png>





{{Sketcher Tools navi

}}  
