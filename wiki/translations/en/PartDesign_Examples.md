# PartDesign Examples/en
{{TOCright}}

## Introduction

Sometimes you need a hint how powerful a tool is, without too much explanation.

This is a collection of examples that can be achieved with certain tools. For detailed explanations see the tool descriptions and search the web for tutorials.

## Pad

<img alt="" src=images/PartDesign_Pad.svg  style="width:24px;"> [PartDesign Pad](PartDesign_Pad.md) is a tool to create Pad objects, which are prismatic objects such as extrusion objects, cylinders, cones, cubes, wedges\...

Each object is based on an outline (yellow), that defines the cross-section shape (preferably made with the [Sketcher Workbench](Sketcher_Workbench.md)).

The outline is dragged along a direction (extruded) to provide the object with a thickness or a length.
By default it is the normal direction of the plane containing the outline (sketch plane). Optionally the direction can be altered by editing parameters in the properties panel or by selecting a separate straight line (white).


<div class="mw-collapsible mw-collapsed">

**Gallery**


<div class="mw-collapsible-content toccolours">

### Prismatic Primitives 

++++
| **Cylinder**      | <img alt="Cylinder" src=images/PartDesign_ExamplePad-01.png  style="width:200px;">           | -   Outline: **circle**.                             |
++++
| **Cube**          | <img alt="Cube" src=images/PartDesign_ExamplePad-02.png  style="width:200px;">                   | -   Outline: **square**.                             |
|                   |                                                                             | -   Extrusion length: equals length of square edges. |
++++
| **Cuboid**        | <img alt="Cuboid" src=images/PartDesign_ExamplePad-03.png  style="width:200px;">               | -   Outline: **rectangle**.                          |
++++
| **Regular Prism** | <img alt="Regular Prism" src=images/PartDesign_ExamplePad-04.png  style="width:200px;"> | -   Outline: **hexagon**.                            |
++++
| **Wedge**         | <img alt="Wedge" src=images/PartDesign_ExamplePad-05.png  style="width:200px;">                 | -   Outline: **triangle**.                           |
++++

### Prismatic Profiles 

++++
| **L-profile**        | <img alt="L-profile" src=images/PartDesign_ExamplePad-06.png  style="width:200px;">               | -   Outline: **L** shape.                                     |
|                      |                                                                                   |                                                               |
|                      |                                                                                   | :                                                             |
++++
| **C-profile**        | <img alt="C-profile" src=images/PartDesign_ExamplePad-07.png  style="width:200px;">               | -   Outline: **C** shape.                                     |
++++
| **Z-profile**        | <img alt="Z-profile" src=images/PartDesign_ExamplePad-11.png  style="width:200px;">               | -   Outline: **Z** shape.                                     |
++++
| **T-profile**        | <img alt="T-profile" src=images/PartDesign_ExamplePad-09.png  style="width:200px;">               | -   Outline: **T** shape.                                     |
++++
| **Double-T-profile** | <img alt="Double-T-profile" src=images/PartDesign_ExamplePad-10.png  style="width:200px;"> | -   Outline: **H** shape, with flange width \< flange offset. |
++++
| **H-profile**        | <img alt="H-profile" src=images/PartDesign_ExamplePad-08.png  style="width:200px;">               | -   Outline: **H** shape, with width = height.                |
++++


</div>


</div>

## Additive Pipe 

<img alt="" src=images/PartDesign_AdditivePipe.svg  style="width:24px;"> [PartDesign Additive pipe](PartDesign_AdditivePipe.md) is a tool to create AdditivePipe objects such as sweep objects, extrusion objects, rotation objects, cylinders, cones, cubes, pyramids, spheres\...

Each object is based on at least two lines (preferably made with the [Sketcher Workbench](Sketcher_Workbench.md)):

-   One outline (yellow), to define the cross-section shape.
-   One path (white), to sweep along.

It is not hard to realize that some objects can be created with other tools too, but would you have guessed how versatile this tool is without these examples?


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
| Regular **Prism** | <img alt="Regular Prism" src=images/PartDesign_ExamplePrism-05.png  style="width:200px;">         | -   Outline: regular **hexagon**.                         |
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

### Spiral and Helical Objects 

++++
| Coil Spring        | <img alt="Spring" src=images/PartDesign_ExampleSpring-01.png  style="width:200px;">                 | -   Outline: **circle**.                                                                                      |
|                    |                                                                                  | -   Path: <img alt="" src=images/Part_Helix.svg  style="width:16px;"> [Part Helix](Part_Helix.md).               |
++++
| Hairspring         | <img alt="Balance Spring" src=images/PartDesign_ExampleSpring-03.png  style="width:200px;"> | -   Outline: **rectangle**.                                                                                   |
| Balance Spring     |                                                                                  | -   Path: <img alt="" src=images/Part_Spiral.svg  style="width:16px;"> [Part Spiral](Part_Spiral.md).           |
++++
| **Volute Spring**, | <img alt="Volute Spring" src=images/PartDesign_ExampleSpring-04.png  style="width:200px;">   | -   Outline: **rectangle**.                                                                                   |
| Conical Spring     |                                                                                  | -   Path: <img alt="" src=images/Part_Helix.svg  style="width:16px;"> [Part Helix](Part_Helix.md) with an angle. |
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

### Options

#### Corner Transition 

A polyline can be used as a path, and the property **Transition** influences the shapes of the corners.

Transformed needs special attention as it can produce flat areas where the thickness is 0.

++++
| Parameter        | Iso View                                                                                         | Top View                                                                                         |
+==================+==================================================================================================+==================================================================================================+
| **Transformed**  | <img alt="Transformed iso view" src=images/PartDesign_ExampleProperty-01.png  style="width:200px;">   | <img alt="Transformed top view" src=images/PartDesign_ExampleProperty-02.png  style="width:200px;">   |
|                  |                                                                                                  |                                                                                                  |
|                  | :   Inner and outer corners are edges.                                                           | :   The basic shape does not follow the line orientation.                                        |
++++
| **Right corner** | <img alt="Right corner iso view" src=images/PartDesign_ExampleProperty-03.png  style="width:200px;"> | <img alt="Right corner top view" src=images/PartDesign_ExampleProperty-04.png  style="width:200px;"> |
|                  |                                                                                                  |                                                                                                  |
|                  | :   Inner and outer corners are edges.                                                           | :   The basic shape follows the line orientation.                                                |
++++
| **Round corner** | <img alt="Round corner iso view" src=images/PartDesign_ExampleProperty-05.png  style="width:200px;"> | <img alt="Round corner top view" src=images/PartDesign_ExampleProperty-06.png  style="width:200px;"> |
|                  |                                                                                                  |                                                                                                  |
|                  | :   The corners lying outside the path are rounded.                                              | :   The basic shape follows the line orientation.                                                |
++++

#### Orientation Mode 

++++
| Parameter     | Iso View                                                                                    | Top View                                                                                            |
+===============+=============================================================================================+=====================================================================================================+
| **Standard**  | <img alt="Standard iso view" src=images/PartDesign_ExampleProperty-07.png  style="width:200px;">    | <img alt="Standard top view" src=images/PartDesign_ExampleProperty-08.png  style="width:200px;">            |
|               |                                                                                             |                                                                                                     |
|               | :   Location and orientation follow the path.                                               | :   (If the object is twisted in an unexpected way, try Frenet)                                     |
|               | :                                                                                           |                                                                                                     |
++++
| **Fixed**     | <img alt="Fixed iso view" src=images/PartDesign_ExampleProperty-09.png  style="width:200px;">          | <img alt="Fixed top view" src=images/PartDesign_ExampleProperty-10.png  style="width:200px;">                  |
|               |                                                                                             |                                                                                                     |
|               | :   Location follows the path and orientation stays the same as basic shape.                | :   This tends to cause self intersections which lead to further errors: a ghost face in this case. |
++++
| **Frenet**    | <img alt="Frenet iso view" src=images/PartDesign_ExampleProperty-07.png  style="width:200px;">        | <img alt="Frenet top view" src=images/PartDesign_ExampleProperty-08.png  style="width:200px;">                |
|               |                                                                                             |                                                                                                     |
|               | :   Location and orientation follow the path, based on a different algorithm than Standard. | :   The basic shape follows the line orientation.                                                   |
++++
| **Auxiliary** |                                                                                             |                                                                                                     |
++++
| **Binormal**  |                                                                                             |                                                                                                     |
++++


</div>


</div>



---
![](images/Button_right.svg) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Examples/en
