---
- GuiCommand:   Name:Mesh BuildRegularSolid   Workbenches:[[Mesh Workbench/hu   Háló]]|MenuLocation:Hálók → Szabályos tömör test…   Shortcut:   SeeAlso:---

## Description


<div class="mw-translate-fuzzy">

## Bemutatás

Hálóalaptestek létrehozása, mint például kockák, hengerek, kúpok, gömbök, ellipszoidok vagy tóruszok.


</div>

## Usage


<div class="mw-translate-fuzzy">

## Használat

1.  Válassza a ** Hálók** → **<img src="images/Mesh_BuildRegularSolid.svg" width=32px> Szabályos tömör test…** menüpontot a felső menüből.

![](images/Meshes_RegularSolid_Cube.jpg ) ![](images/Meshes_RegularSolid_Cylinder.jpg ) ![](images/Meshes_RegularSolid_Cone.jpg )
![](images/Meshes_RegularSolid_Sphere.jpg ) ![](images/Meshes_RegularSolid_Ellipsoid.jpg ) ![](images/Meshes_RegularSolid_Torus.jpg )


</div>

## Notes


<div class="mw-translate-fuzzy">

## Jegyzetek

Ezen hálós szabályos tömör testek paramétereinek megváltoztatásához jelölje ki azokat a fanézetben, és váltson át az adat lapra.


</div>

## Properties

Mesh objects created with this command inherit all [Mesh Feature](Mesh_Feature.md) properties. In addition each mesh object type has a number of properties to control its parametric behavior:

### <img alt="" src=images/Mesh_Cube.svg  style="width:32px;"> Cube {#mesh_cube.svg_cube}

#### Data


{{TitleProperty|Cube}}

-    **Height|FloatConstraint**: the height of the cube.

-    **Length|FloatConstraint**: the length of the cube.

-    **Width|FloatConstraint**: the width of the cube.

### <img alt="" src=images/Mesh_Cylinder.svg  style="width:32px;"> Cylinder {#mesh_cylinder.svg_cylinder}

#### Data {#data_1}


{{TitleProperty|Base}}

-    **Closed|Bool**: if set to `False`, the planar ends of the cylinder are left open.

-    **Edge Length|FloatConstraint**: the edge length of the faces in the mesh.

-    **Length|FloatConstraint**: the length of the cylinder.

-    **Radius|FloatConstraint**: the radius of the cylinder.

-    **Sampling|IntegerConstraint**: the number of faces along the curved surface.

### <img alt="" src=images/Mesh_Cone.svg  style="width:32px;"> Cone {#mesh_cone.svg_cone}

#### Data {#data_2}


{{TitleProperty|Base}}

-    **Closed|Bool**: if set to `False`, the planar end(s) of the cone are left open.

-    **Edge Length|FloatConstraint**: the edge length of the faces in the mesh.

-    **Length|FloatConstraint**: the length of the cone.

-    **Radius 1|FloatConstraint**: the first radius of the cone. Can be {{value|0}}.

-    **Radius 2|FloatConstraint**: the second radius of the cone. Can be {{value|0}}.

-    **Sampling|IntegerConstraint**: the number of faces along the curved surface.

### <img alt="" src=images/Mesh_Sphere.svg  style="width:32px;"> Sphere {#mesh_sphere.svg_sphere}

#### Data {#data_3}


{{TitleProperty|Base}}

-    **Radius|FloatConstraint**: the radius of the sphere.

-    **Sampling|IntegerConstraint**: the number of faces along both directions of the curved surface.

### <img alt="" src=images/Mesh_Ellipsoid.svg  style="width:32px;"> Ellipsoid {#mesh_ellipsoid.svg_ellipsoid}

#### Data {#data_4}


{{TitleProperty|Base}}

-    **Radius 1|FloatConstraint**: the first radius of the ellipsoid.

-    **Radius 2|FloatConstraint**: the second radius of the ellipsoid.

-    **Sampling|IntegerConstraint**: the number of faces along both directions of the curved surface.

### <img alt="" src=images/Mesh_Torus.svg  style="width:32px;"> Torus {#mesh_torus.svg_torus}

#### Data {#data_5}


{{TitleProperty|Base}}

-    **Radius 1|FloatConstraint**: the first (main) radius the torus.

-    **Radius 2|FloatConstraint**: the second radius of the torus.

-    **Sampling|IntegerConstraint**: the number of faces along both directions of the curved surface.





{{Mesh Tools navi

}}  
