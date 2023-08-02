# Mesh BuildRegularSolid/ro
---
- GuiCommand:   Name: Mesh BuildRegularSolid   Workbenches: Mesh Workbench   Mesh|MenuLocation: Meshes -> Regular solid...   Shortcut:    SeeAlso: ---

## Description


<div class="mw-translate-fuzzy">

## Introducere

Creați primitive tip plasă, cum ar fi cuburi, cilindri, conuri, sfere, elipsoid, torus.


</div>

## Usage


<div class="mw-translate-fuzzy">

## Utilizare

Choose ** Meshes** → **<img src="images/Mesh_BuildRegularSolid.svg" width=32px> Regular solid...** from the top menu.
![](images/Meshes_RegularSolid_Cube.jpg ) ![](images/Meshes_RegularSolid_Cylinder.jpg ) ![](images/Meshes_RegularSolid_Cone.jpg )
![](images/Meshes_RegularSolid_Sphere.jpg ) ![](images/Meshes_RegularSolid_Ellipsoid.jpg ) ![](images/Meshes_RegularSolid_Torus.jpg )


</div>

## Notes


<div class="mw-translate-fuzzy">

## Notes 

Pentru a schimba parametrii acestor componente solide regulate, evidențiați-le în vizualizarea arborescentă și comutați la tab-ul de date.


</div>

## Properties

Mesh objects created with this command inherit all [Mesh Feature](Mesh_Feature.md) properties. In addition each mesh object type has a number of properties to control its parametric behavior:

### <img alt="" src=images/Mesh_Cube.svg  style="width:32px;"> Cube 

#### Data


{{TitleProperty|Cube}}

-    **Height|FloatConstraint**: the height of the cube.

-    **Length|FloatConstraint**: the length of the cube.

-    **Width|FloatConstraint**: the width of the cube.

### <img alt="" src=images/Mesh_Cylinder.svg  style="width:32px;"> Cylinder 

#### Data 


{{TitleProperty|Base}}

-    **Closed|Bool**: if set to `False`, the planar ends of the cylinder are left open.

-    **Edge Length|FloatConstraint**: the edge length of the faces in the mesh.

-    **Length|FloatConstraint**: the length of the cylinder.

-    **Radius|FloatConstraint**: the radius of the cylinder.

-    **Sampling|IntegerConstraint**: the number of faces along the curved surface.

### <img alt="" src=images/Mesh_Cone.svg  style="width:32px;"> Cone 

#### Data 


{{TitleProperty|Base}}

-    **Closed|Bool**: if set to `False`, the planar end(s) of the cone are left open.

-    **Edge Length|FloatConstraint**: the edge length of the faces in the mesh.

-    **Length|FloatConstraint**: the length of the cone.

-    **Radius 1|FloatConstraint**: the first radius of the cone. Can be {{value|0}}.

-    **Radius 2|FloatConstraint**: the second radius of the cone. Can be {{value|0}}.

-    **Sampling|IntegerConstraint**: the number of faces along the curved surface.

### <img alt="" src=images/Mesh_Sphere.svg  style="width:32px;"> Sphere 

#### Data 


{{TitleProperty|Base}}

-    **Radius|FloatConstraint**: the radius of the sphere.

-    **Sampling|IntegerConstraint**: the number of faces along both directions of the curved surface.

### <img alt="" src=images/Mesh_Ellipsoid.svg  style="width:32px;"> Ellipsoid 

#### Data 


{{TitleProperty|Base}}

-    **Radius 1|FloatConstraint**: the first radius of the ellipsoid.

-    **Radius 2|FloatConstraint**: the second radius of the ellipsoid.

-    **Sampling|IntegerConstraint**: the number of faces along both directions of the curved surface.

### <img alt="" src=images/Mesh_Torus.svg  style="width:32px;"> Torus 

#### Data 


{{TitleProperty|Base}}

-    **Radius 1|FloatConstraint**: the first (main) radius the torus.

-    **Radius 2|FloatConstraint**: the second radius of the torus.

-    **Sampling|IntegerConstraint**: the number of faces along both directions of the curved surface.





{{Mesh Tools navi

}}



---
⏵ [documentation index](../README.md) > [Mesh](Mesh_Workbench.md) > Mesh BuildRegularSolid/ro
