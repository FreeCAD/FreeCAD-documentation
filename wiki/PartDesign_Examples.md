# PartDesign Examples
{{TOCright}}



## Introduction

Sometimes you need a hint how powerful a tool is, without too much explanation.

This is a collection of examples what can be achieved with certain tools. For detailed explanations see the tool descriptions and search the web for tutorials.

## Additive Pipe 

<img alt="" src=images/PartDesign_AdditivePipe.svg  style="width:24px;"> [PartDesign Additive pipe](PartDesign_AdditivePipe.md) is a tool to create AdditivePipe objects such as sweep objects, extrusion objects, rotation objects, cylinders, cones, cubes, pyramids, spheres\...

Each object is based on at least of two lines (Preferably made with the Sketcher):

-   One outline (yellow), to define the cross-section shape.
-   One path (white), to sweep along.

It is not hard to realise that some objects can be created by other tools, too, but would you have guessed how versatile this tool is without those examples?


<div class="mw-collapsible mw-collapsed">

**Gallery**


<div class="mw-collapsible-content toccolours">

### Circular Sweep Objects 

++++
| **Sphere**         | <img alt="Sphere" src=images/PartDesign_ExampleSphere-01.png  style="width:200px;">                                | -   Outline: a**180° arc** and a **line** connecting the end points.                                                                      |
|                    |                                                                                                 | -   Path: full **circle**.                                                                                                                |
++++
| **Sphere Segment** | <img alt="Sphere Segment 240°" src=images/PartDesign_ExampleSphere-02.png  style="width:200px;">      | -   Outline: a **180° arc** and a **line** connecting the end points.                                                                     |
|                    |                                                                                                 | -   Path: a **240° arc**.                                                                                                                 |
|                    |                                                                                                 |                                                                                                                                           |
|                    |                                                                                                 | :   This function can create segments of any angle except 180° exactly, because it has a problem with start and end plane being coplanar. |
++++
| **Hemisphere**     | <img alt="Hemisphere" src=images/PartDesign_ExampleSphere-03.png  style="width:200px;">                        | -   Outline: a **90° arc** and two perpendicular **lines** connecting the end points.                                                     |
|                    |                                                                                                 | -   Path: a full **circle**.                                                                                                              |
++++
| **Torus**          | <img alt="Torus" src=images/PartDesign_ExampleTorus-01.png  style="width:200px;">                                   | -   Outline: full **circle**.                                                                                                             |
|                    |                                                                                                 | -   Path: full **circle**.                                                                                                                |
++++
| **Cone**           | <img alt="Cone" src=images/PartDesign_ExampleTorus-04.png  style="width:200px;">                                     | -   Outline: **triangle** with one edge lying on the centreline.                                                                          |
|                    |                                                                                                 | -   Path: full **circle**.                                                                                                                |
++++
| **Cylinder**       | <img alt="Cylinder" src=images/PartDesign_ExampleTorus-02.png  style="width:200px;">                             | -   Outline: **rectangle** with one edge lying on the centreline.                                                                         |
|                    |                                                                                                 | -   Path: full **circle**.                                                                                                                |
++++
| **Pipe**           | <img alt="Pipe (Hollow Cylinder)" src=images/PartDesign_ExampleTorus-03.png  style="width:200px;"> | -   Outline: **rectangle**.                                                                                                               |
| Hollow Cylinder    |                                                                                                 | -   Path: full **circle**.                                                                                                                |
++++

### Prismatic Objects 

Straight Sweep Objects

++++
| **Cylinder**      | <img alt="Cylinder" src=images/PartDesign_ExamplePrism-01.png  style="width:200px;">                   | -   Outline: **circle**.                                  |
|                   |                                                                                       | -   Path: straight **line**.                              |
++++
| **Cube**          | <img alt="Cube" src=images/PartDesign_ExamplePrism-02.png  style="width:200px;">                           | -   Outline: **square**.                                  |
|                   |                                                                                       | -   Path: straight **line**, same length as square edges. |
++++
| **Cuboid**        | <img alt="Cuboid" src=images/PartDesign_ExamplePrism-03.png  style="width:200px;">                       | -   Outline: **rectangle**.                               |
|                   |                                                                                       | -   Path: straight **line**.                              |
++++
| **Wedge**         | <img alt="Wedge" src=images/PartDesign_ExamplePrism-04.png  style="width:200px;">                         | -   Outline: **triangle**.                                |
|                   |                                                                                       | -   Path: straight **line**.                              |
++++
| Regular **Prism** | <img alt="Cylinder" src=images/PartDesign_ExamplePrism-05.png  style="width:200px;">                   | -   Outline: regular **hexagon**.                         |
|                   |                                                                                       | -   Path: straight **line**.                              |
++++
| Star-shaped Prism | <img alt="Star-shaped Prism" src=images/PartDesign_ExamplePrism-06.png  style="width:200px;"> | -   Outline: regular **star-shape**.                      |
|                   |                                                                                       | -   Path: straight **line**.                              |
++++
| Double-T Beam     | <img alt="Double-T Beam" src=images/PartDesign_ExamplePrism-07.png  style="width:200px;">         | -   Outline: **beam section**.                            |
|                   |                                                                                       | -   Path: straight **line**.                              |
++++

### Conical Objects 

++++
| **Cone**       | <img alt="Cone" src=images/PartDesign_ExampleConic-01.png  style="width:200px;">                     | -   Outlines: Base: full **circle**, Top: **point**. |
|                |                                                                                 | -   Path: straight **line**.                         |
|                |                                                                                 |                                                      |
|                |                                                                                 | :   (Tip point is an end point of an auxiliary line) |
++++
| **Pyramid**    | <img alt="Pyramid" src=images/PartDesign_ExampleConic-02.png  style="width:200px;">               | -   Outlines: Base: **square**, Top: **point**.      |
|                |                                                                                 | -   Path: straight **line**.                         |
|                |                                                                                 |                                                      |
|                |                                                                                 | :   (Tip point is an end point of an auxiliary line) |
++++
| Tilted Pyramid | <img alt="Tilted Pyramid" src=images/PartDesign_ExampleConic-03.png  style="width:200px;"> | -   Outlines: Base: **square**, Top: **point**.      |
|                |                                                                                 | -   Path: straight **line**.                         |
|                |                                                                                 |                                                      |
|                |                                                                                 | :   (Tip point is the end point of the path)         |
++++

### Curved Sweep Objects 

++++
| **Hose**        | <img alt="Hose" src=images/PartDesign_ExampleSweep-01.png  style="width:200px;">               | -   Outline: 2 concentric **circles**.                     |
| (Pipe)          |                                                                           | -   Path: curved **line**.                                 |
++++
| Square **Pipe** | <img alt="Square Pipe" src=images/PartDesign_ExampleSweep-02.png  style="width:200px;"> | -   Outline: 2 concentric **squares**.                     |
|                 |                                                                           | -   Path: curved **line**.                                 |
++++
| **Wire**        | <img alt="Wire" src=images/PartDesign_ExampleSweep-04.png  style="width:200px;">               | -   Outline: **circle**.                                   |
|                 |                                                                           | -   Path: curved **line**.                                 |
++++
| Horn            | <img alt="Horn" src=images/PartDesign_ExampleSweep-03.png  style="width:200px;">               | -   Outlines: Base: **circle**, Top: (smaller) **circle**. |
|                 |                                                                           | -   Path: curved **line**.                                 |
++++
| Legendary       | <img alt="Hex-Wrench" src=images/PartDesign_ExampleSweep-05.png  style="width:200px;">   | -   Outline: **hexagon**.                                  |
| **Hex-Wrench**  |                                                                           | -   Path: curved **line**.                                 |
++++

### Transition Objects 

++++
| Square to Circle | <img alt="Curvy transition object" src=images/PartDesign_ExampleTrans-01.png  style="width:200px;">       | -   Outlines: Base: **square**, Top: **circle**.       |
| via path         |                                                                                                         | -   Path: curved **line**.                             |
++++
| Square to Circle | <img alt="Straight transition object" src=images/PartDesign_ExampleTrans-02.png  style="width:200px;"> | -   Outlines: Base: **square**, Top: **circle**.       |
| direct           |                                                                                                         | -   Path: straight **line**.                           |
++++
| Polygon to Star  | <img alt="Polygon to Star" src=images/PartDesign_ExampleTrans-03.png  style="width:200px;">                       | -   Outlines: Base: **pentagon**, Top: **star shape**. |
|                  |                                                                                                         | -   Path: straight **line**.                           |
++++


</div>


</div>



---
![](images/Right_arrow.png) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Examples
