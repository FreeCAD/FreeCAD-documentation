# Part Ellipse/cs
---
- GuiCommand:/cs   Name:Part Ellipse   Name/cs:Díl Elipsa   MenuLocation:Díl → [Workbenches:[[Part_Workbench/cs   Díl](Part_CreatePrimitives/cs___Vytváření_zákl.geom.tvarů]] → Elipsa.md),  [OpenSCAD](OpenSCAD_Workbench/cs.md)|SeeAlso:..---


</div>


<div class="mw-translate-fuzzy">

### Základní geometrické tvary 

+--------------------------------------------------------------------------------+---------------------------------+
| ![](images/PartEllipsePrimitivesOptions_it.png ) | Elipsa                          |
|                                                                                |                                 |
|                                                                                | #### Parametr                   |
|                                                                                |                                 |
|                                                                                | -                |
|                                                                                |     {{Parameter|Velký poloměr}} |
|                                                                                |                              |
|                                                                                |                                 |
|                                                                                | -                |
|                                                                                |     {{Parameter|Malý poloměr}}  |
|                                                                                |                              |
|                                                                                |                                 |
|                                                                                | -                |
|                                                                                |     {{Parameter|Úhel 1}}        |
|                                                                                |                              |
|                                                                                |                                 |
|                                                                                | -                |
|                                                                                |     {{Parameter|Úhel 2}}        |
|                                                                                |                              |
|                                                                                |                                 |
|                                                                                | #### Umístění                   |
|                                                                                |                                 |
|                                                                                | -                               |
|                                                                                | -                               |
+--------------------------------------------------------------------------------+---------------------------------+


</div>

This command will create a elliptical curved edge. With the default values, the elliptical curved edge will be closed and therefore will be an ellipse. If the properties Angle 1 or Angle 2 are changed from their default values (0 and 360) the edge will be an open curve.

## Usage

The Create Primitives dialogue can be accessed via the [Primitives](Part_Primitives.md) icon <img alt="" src=images/Part_Primitives.svg  style="width:32px;"> located in the Part menu or the Part toolbar, in the Part Workbench.

## Properties

-   **Major radius:** the major radius of the ellipse, the default value is 4
-   **Minor radius:** the minor radius of the ellipse, the default value is 2
-   **Angle 1:** start of the edge of the ellipse or elliptical curved edge, (degrees anti-clockwise), the default value is 0
-   **Angle 2:** end of the edge of the ellipse or elliptical curved edge, (degrees anti-clockwise), the default value is 360

---
[documentation index](../README.md) > [Part](Part_Workbench.md) > Part Ellipse/cs
