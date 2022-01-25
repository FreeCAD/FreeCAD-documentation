# Part Circle/cs
---
- GuiCommand:/cs   Name:Part_Circle   Name/cs:Díl Kružnice   MenuLocation:Díl → [Workbenches:[[Part_Workbench/cs   Díl](Part_CreatePrimitives/cs___Vytváření_zákl.geom.tvarů]] → Kružnice.md),  [OpenSCAD](OpenSCAD_Workbench/cs.md)|SeeAlso:..---


</div>

## Description

This command will create a circular curved edge. With the default values, the circular curved edge will be closed and therefore will be a circle. If the properties Angle 0 or Angle 1 are changed from their default values (0 and 360) the edge will be an open curve, an arc.

Alternatively a Part Circle can be initially defined from three points. Once created the circle will only contain the standard Part Circle properties and will no longer contain a reference to the creation points.

## Usage

A Circle geometric primitive is available from the Create Primitives dialogue in the Part workbench.

1.  Switch to the <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Part](Part_Workbench.md)
2.  There are several ways to access the Create Primitives dialogue:
    -   Press the <img alt="" src=images/Part_Primitives.svg  style="width:24px;"> [Primitives](Part_Primitives.md) button located in the Part toolbar
    -   Use the **Part → [Create primitives](Part_Primitives.md) → Circle**


<div class="mw-translate-fuzzy">

### Základní geometrické tvary 

+++
| ![](images/PartCirclePrimitivesOptions_it.png ) | Kružnice                      |
|                                                                              |                               |
|                                                                              | #### Parametr                 |
|                                                                              |                               |
|                                                                              | -              |
|                                                                              |     {{Parameter|Poloměr}}     |
|                                                                              |                            |
|                                                                              |     :                         |
|                                                                              |                               |
|                                                                              | -              |
|                                                                              |     {{Parameter|Úhel 1}}      |
|                                                                              |                            |
|                                                                              |     :                         |
|                                                                              |                               |
|                                                                              | -              |
|                                                                              |     {{Parameter|Úhel 2}}      |
|                                                                              |                            |
|                                                                              |     :                         |
|                                                                              |                               |
|                                                                              | -              |
|                                                                              |     {{Parameter|Ze tří bodů}} |
|                                                                              |                            |
|                                                                              |     :                         |
|                                                                              |                               |
|                                                                              | #### Umístění                 |
|                                                                              |                               |
|                                                                              | -                             |
|                                                                              | -                             |
+++


</div>

-    {{Parameter|Radius}}: the radius of the curved edge (arc or circle)

-    {{Parameter|Angle 0}}: start of the curved edge, (degrees anti-clockwise), the default value is 0

-    {{Parameter|Angle 1}}: end of the curved edge, (degrees anti-clockwise), the default value is 360



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Circle/cs
