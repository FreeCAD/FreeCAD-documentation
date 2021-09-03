---
- GuiCommand:/es
   Name:PartDesign_Revolution
   Name/es:DiseñoPiezas Rotación
   MenuLocation:DiseñoPiezas -> Rotación
   Workbenches:[DiseñoPiezas](PartDesign_Workbench/es.md)
---


</div>

## Descripción

La herramienta *Rotación* crea un sólido girando un boceto seleccionado o un objeto 2D sobre un eje dado. ![](images/PartDesign_Revolution_example.svg ) \"Arriba: el bosquejo (A) gira 270 grados en sentido contrario a las agujas del reloj alrededor del eje (B); el sólido resultante (C) se muestra a la derecha.

## Utilización

1.  Select the sketch to be revolved. v0.17 and above A face on the existing solid can alternatively be used.
2.  Press the **<img src="images/PartDesign_Revolution.svg" width=24px> '''Revolution'''** button.
3.  Set the Revolution parameters (see next section).
4.  Press **OK**.

## Opciones

Al crear una revolución, el diálogo *Parámetros de la revolución* ofrece varios parámetros que especifican cómo debe girar el boceto.

+----------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ![](images/partdesign_revolution_parameters.png ) | ### Axis                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                  |                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                  | This option specifies the axis about which the sketch is to be revolved.                                                                                                                                                                                                                                                                                                     |
|                                                                                  |                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                  | -   **Vertical sketch axis**: selects the vertical sketch axis.                                                                                                                                                                                                                                                                                                              |
|                                                                                  | -   **Horizontal sketch axis**: selects the horizontal sketch axis.                                                                                                                                                                                                                                                                                                          |
|                                                                                  | -   **Sketch axis**: v0.16 and below selects a construction line contained in the sketch used by the Revolution. The first construction line created in the sketch will be labelled *Sketch axis 0*. The drop down list will contain one custom sketch axis for each construction line.                 |
|                                                                                  | -   **Construction line**: v0.17 and above selects a construction line contained in the sketch used by the Revolution. The drop down list will contain an entry for each construction line. The first construction line created in the sketch will be labelled *Construction line 1*.                  |
|                                                                                  | -   **Base (X/Y/Z) axis**: v0.17 and above selects the X, Y or Z axis of the Body\'s Origin;                                                                                                                                                                                                           |
|                                                                                  | -   **Select reference\...**: v0.17 and above allows selection in the 3D view of an edge on the Body, or a [datum line](PartDesign_Line.md).                                                                                                                                                   |
|                                                                                  |                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                  | ### Angle                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                  |                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                  | This controls the angle through which the revolution is to be formed, e.g. 360° would be a full, contiguous revolution. The images in the [examples](#Examples.md) section demonstrate some of the possibilities with specifying different angles. It is not possible to specify negative angles (use the **Reversed** option instead) or angles greater than 360° . |
|                                                                                  |                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                  | ### Symmetric to plane {#symmetric_to_plane}                                                                                                                                                                                                                                                                                                                                 |
|                                                                                  |                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                  | If checked, the revolution will extend half of the specified angle in both directions from the sketch plane.                                                                                                                                                                                                                                                                 |
|                                                                                  |                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                  | ### Reversed                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                  |                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                  | If checked, the direction of revolution is reversed from default clockwise to counterclockwise.                                                                                                                                                                                                                                                                              |
+----------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+




### Propiedades

Below are properties which can be defined after creation of the feature. Data properties *Base* and *Axis* are uneditable.

-    **Angle**: angle of rotation. See [Angle](#Angle.md).

-    **Label**: label given to the operation, can be changed at convenience.

-    **Midplane**: true or false. See [Symmetric to plane](#Symmetric_to_plane.md).

-    **Reversed**: true or false. See [Reversed](#Reversed.md).

-    **Refine**: v0.17 and above true or false. If set to true, cleans the solid from residual edges left by features. See [Part RefineShape](Part_RefineShape.md) for more details.

## Ejemplos

![Example revolution using a construction line as the Revolution axis: In this image the angle is 75°, revolution is about the construction line (Sketch axis 0)](images/PartDesign_Revolution_axis_fromconstructionlines1.jpg ) 

## Useful links {#useful_links}

A [detailed example of use](http://forum.freecadweb.org/viewtopic.php?f=3&t=3674) on the forum.





{{PartDesign Tools navi

}} 
