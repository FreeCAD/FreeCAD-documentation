---
- GuiCommand:
   Name:TechDraw ExtensionVertexAtIntersection
   MenuLocation:TechDraw → Extensions: centerlines and threading → Draw circle centerlines
   Workbenches:[TechDraw](TechDraw_Workbench.md)
   Shortcut:
   Version:0.20
   SeeAlso:
---

# TechDraw ExtensionVertexAtIntersection

## Description

The <img alt="" src=images/TechDraw_ExtensionVertexAtIntersection.svg  style="width:24px;"> **VertexAtIntersection** tool adds vertex(es) at intersection of lines.

 <img alt="" src=images/TechDraw_ExtensionVertexAtIntersectionExample.png  style="width:200px;">  
*On the right two created vertexes (1) and (2)*

## Usage

1.  Select two lines, circles or arcs of circle.
2.  Press the **<img src="images/TechDraw_ExtensionVertexAtIntersection.svg" width=16px> [VertexAtIntersection](TechDraw_ExtensionVertexAtIntersection.md)** button.
3.  Vertex(es) are added at each intersection point.

-   If line segments are selected, the supporting strait lines are used.
-   If arcs of circle are selected, the supporting circles are used.
-   If the selected objects have no intersection (parallel lines, distance of circle centers is to far etc.) nothing is created.




 {{TechDraw_Tools_navi}}

---
[documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw ExtensionVertexAtIntersection
