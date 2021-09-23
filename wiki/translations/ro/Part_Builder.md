---
- GuiCommand:/ro
   Name:Part Shapebuilder
   Name/ro:Part Shapebuilder
   MenuLocation:Part -> Shapebuilder...
|
   Workbenches:[Part](Part_Workbench/ro.md)
   SeeAlso:[Part CreatePrimitives](Part_CreatePrimitives/ro.md)
---

# Part Builder/ro


</div>

## Description


<div class="mw-translate-fuzzy">

## Descriere

A tool to create more complex shapes from various parametric geometric primitives.


</div>


<div class="mw-translate-fuzzy">

## Use

This tool will let you create shapes by creating

1.  Edge from two vertices
2.  Face from vertices
    1.  Select vertices bounding the face in the 3D view
    2.  Select if face should be planar
    3.  Click on ** Create**
    4.  Object will be created in 3D view and will be listed in tree view
3.  Wire from edges <small>(v0.18)</small> \#\#Select a set of adjacent edges in the 3D view
    1.  Click on ** Create**
4.  Face from edges
    1.  Select a closed set of edges bounding the face in the 3D view
    2.  Select if face should be planar
    3.  Click on ** Create**
    4.  Object will be created in 3D view and will be listed in tree view
5.  Shell from faces
    1.  Select faces in the 3D view
    2.  Select if the shape should be refined
    3.  Select if all faces should be included in shell
    4.  Click on ** Create**
    5.  Object will be created in 3D view and will be listed in tree view
6.  Solid from shell
    1.  Select if the shape should be refined
    2.  Click on ** Create**
    3.  Object will be created in 3D view and will be listed in tree view


</div>

This tool can create the following objects:

### Edge from two vertices 

1.  Select two vertices
2.  Click on **Create**

![](images/Edge_from_verts-1.gif )

### Wire from edges 

1.  Select a set of adjacent edges in the [3D view](3D_view.md)
2.  Click on **Create**

![](images/Wire_from_edges-1.gif )

### Face from vertices 

1.  Select vertices bounding the face in the [3D view](3D_view.md)
2.  Select if face should be planar
3.  Click on **Create**
4.  Object will be created in [3D view](3D_view.md) and will be listed in [tree view](Tree_view.md)

![](images/Face_from_verts.gif )

### Face from edges 

1.  Select a closed set of edges bounding the face in the [3D view](3D_view.md)
2.  Select if face should be planar
3.  Click on **Create**
4.  Object will be created in [3D view](3D_view.md) and will be listed in [tree view](Tree_view.md)

![](images/Face_from_edges.gif )

### Shell from faces 

1.  Select faces in the [3D view](3D_view.md)
2.  Select if the shape should be refined
3.  Select if all faces should be included in shell
4.  Click on **Create**
5.  Object will be created in [3D view](3D_view.md) and will be listed in [tree view](Tree_view.md)

### Solid from shell 

1.  Select if the shape should be refined
2.  Click on **Create**
3.  Object will be created in [3D view](3D_view.md) and will be listed in [tree view](Tree_view.md)

## Notes


<div class="mw-translate-fuzzy">

## Note

Un posibil flux de lucru ar putea fi:

-   Draw a wireframe-model of your shape using the tools in the draft-workbench (for example line and dwire)
-   Create all faces with \"face from edges\"
-   Create a \"shell from faces\"
-   Create a \"solid from shell\"


</div>

---
[documentation index](../README.md) > [Part](Part_Workbench.md) > Part Builder/ro
