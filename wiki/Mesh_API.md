# Mesh API

The functions in this module allow working with mesh objects.
A set of functions are provided for reading in registered mesh
file formats to either a new or existing document.

open(string) -- Create a new document and a Mesh feature
                to load the file into the document.
insert(string, string) -- Create a Mesh feature to load
                          the file into the given document.
Mesh() -- Create an empty mesh object.





### Functions

#### <img src="images/Arrow-right.svg" style="width:16px;"> calculateEigenTransform

calculateEigenTransform(seq(Base.Vector))
Calculates the eigen Transformation from a list of points.
calculate the point's local coordinate system with the center
of gravity as origin. The local coordinate system is computed
this way that u has minimum and w has maximum expansion.
The local coordinate system is right-handed.



#### <img src="images/Arrow-right.svg" style="width:16px;"> createBox

Create a solid mesh box



#### <img src="images/Arrow-right.svg" style="width:16px;"> createCone

Create a tessellated cone



#### <img src="images/Arrow-right.svg" style="width:16px;"> createCylinder

Create a tessellated cylinder



#### <img src="images/Arrow-right.svg" style="width:16px;"> createEllipsoid

Create a tessellated ellipsoid



#### <img src="images/Arrow-right.svg" style="width:16px;"> createPlane

Create a mesh XY plane normal +Z



#### <img src="images/Arrow-right.svg" style="width:16px;"> createSphere

Create a tessellated sphere



#### <img src="images/Arrow-right.svg" style="width:16px;"> createTorus

Create a tessellated torus



#### <img src="images/Arrow-right.svg" style="width:16px;"> export

export(objects, filename, [tolerance=0.1, exportAmfCompressed=True])
Export a list of objects into a single file identified by filename.
tolerance is in mm and specifies the maximum acceptable deviation
between the specified objects and the exported mesh.
exportAmfCompressed specifies whether exported AMF files should be
compressed.



#### <img src="images/Arrow-right.svg" style="width:16px;"> insert

insert(string|mesh,[string])
Load or insert a mesh into the given or active document.



#### <img src="images/Arrow-right.svg" style="width:16px;"> minimumVolumeOrientedBox

minimumVolumeOrientedBox(seq(Base.Vector)) -- Calculates the minimum
volume oriented box containing all points. The return value is a
tuple of seven items:
    center, u, v, w directions and the lengths of the three vectors.



#### <img src="images/Arrow-right.svg" style="width:16px;"> open

open(string)
Create a new document and a Mesh feature to load the file into
the document.



#### <img src="images/Arrow-right.svg" style="width:16px;"> polynomialFit

polynomialFit(seq(Base.Vector)) -- Calculates a polynomial fit.



#### <img src="images/Arrow-right.svg" style="width:16px;"> read

Read a mesh from a file and returns a Mesh object.



#### <img src="images/Arrow-right.svg" style="width:16px;"> show

show(shape,[string]) -- Add the mesh to the active document or create one if no document exists.



#### <img src="images/BIM_Column.svg" style="width:16px;"> [Edge](Edge_API.md)

Edge in mesh
This is an edge of a facet in a MeshObject. You can get it by e.g. iterating over the facets of a
mesh and calling getEdge(index).



#### <img src="images/BIM_Column.svg" style="width:16px;"> Facet

Facet in mesh
This is a facet in a MeshObject. You can get it by e.g. iterating a
mesh. The facet has a connection to its mesh and allows therefore
topological operations. It is also possible to create an unbounded facet e.g. to create
a mesh. In this case the topological operations will fail. The same is
when you cut the bound to the mesh by calling unbound().



#### <img src="images/BIM_Column.svg" style="width:16px;"> Feature

The Mesh::Feature class handles meshes.
The Mesh.MeshFeature() function is for internal use only and cannot be used to create instances of this class.
Therefore you must have a reference to a document, e.g. 'd' then you can create an instance with
d.addObject("Mesh::Feature").



#### <img src="images/BIM_Column.svg" style="width:16px;"> [Mesh](Mesh_API.md)

Mesh() -- Create an empty mesh object.

This class allows one to manipulate the mesh object by adding new facets, deleting facets, importing from an STL file,
transforming the mesh and much more.
For a complete overview of what can be done see also the documentation of mesh.
A mesh object cannot be added to an existing document directly. Therefore the document must create an object
with a property class that supports meshes.
Example:
  m = Mesh.Mesh()
  ... # Manipulate the mesh
  d = FreeCAD.activeDocument() # Get a reference to the actie document
  f = d.addObject(":Feature", "Mesh") # Create a mesh feature
  f.Mesh = m # Assign the mesh object to the internal property
  d.recompute()



#### <img src="images/BIM_Column.svg" style="width:16px;"> MeshPoint

Point in mesh
This is a point in a MeshObject. You can get it by e.g. iterating a
mesh. The point has a connection to its mesh and allows therefore
topological operations. It is also possible to create an unbounded mesh point e.g. to create
a mesh. In this case the topological operations will fail. The same is
when you cut the bound to the mesh by calling unbound().









---
![](images/Button_right.png) [documentation index](../README.md) > [API](Category_API.md) > [Poweruser Documentation](Category_Poweruser Documentation.md) > [Mesh](Mesh_Workbench.md) > Mesh API
