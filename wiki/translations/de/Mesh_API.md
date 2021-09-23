# Mesh API/de



**(November 2018) Diese Information kann unvollständig und veraltet sein. Für die letzte API siehe die (engl.) [https://www.freecadweb.org/api autogenerierte API-Dokumentation].**

The Mesh objects can be manipulated by adding new facets, deleting facets, importing from an STL file, transforming the mesh and much more. For a complete overview of what can be done see also the [Mesh Workbench](Mesh_Workbench.md) documentation. A mesh object cannot be added to an existing document directly. Therefore the document must create an object with a property class that supports meshes. Example:


```python
m = Mesh.Mesh()
... # Manipulate the mesh
d = FreeCAD.activeDocument() # Get a reference to the actie document
f = d.addObject("Mesh::Feature", "Mesh") # Create a mesh feature
f.Mesh = m # Assign the mesh object to the internal property
d.recompute()
```


{{APIFunction|addFacet|Facet|Adds a facet to the mesh| }}


{{APIFunction|addFacets|list|Adds a list of facets to the mesh| }}


{{APIFunction|addMesh|Mesh|Combines this mesh with another mesh.| }}


{{APIFunction|clear| |Clears the mesh| }}


{{APIFunction|coarsen| |Coarsens the mesh| }}


{{APIFunction|collapseEdge|Edge|Removes an edge and both facets that share this edge| }}


{{APIFunction|collapseFacet|Facet|Removes a facet| }}


{{APIFunction|collapseFacets|list|Removes a list of facets| }}


{{APIFunction|copy| |Creates a copy of this mesh|a Mesh object}}


{{APIFunction|countComponents| |Get the number of topological independent areas|an integer}}


{{APIFunction|countNonUniformOrientedFacets| |Get the number of wrong oriented facets|an integer}}


{{APIFunction|countSegments| |Get the number of segments which may also be 0|an integer}}


{{APIFunction|crossSections| |Get cross-sections of the mesh through several planes| }}


{{APIFunction|difference|Mesh|Difference of this and the given mesh object.| }}


{{APIFunction|fillupHoles| |Fillup holes| }}


{{APIFunction|fixDeformations| |Repair deformed facets| }}


{{APIFunction|fixDegenerations| |Remove degenerated facets| }}


{{APIFunction|fixIndices| |Repair any invalid indices| }}


{{APIFunction|fixSelfIntersections| |Repair self-intersections| }}


{{APIFunction|flipNormals| |Flip the mesh normals| }}


{{APIFunction|foraminate| |Get a list of facet indices and intersection points| }}


{{APIFunction|getPlanes| |Get all planes of the mesh as segment. In the worst case each triangle can be regarded as single plane if none of its neighbors is coplanar.| }}


{{APIFunction|getSegment|integer|Get a list of facet indices that describes a segment| }}


{{APIFunction|getSeparateComponents| |Returns a list containing the different components (separated areas) of the mesh as separate meshes|a list}}


{{APIFunction|harmonizeNormals| |Adjust wrong oriented facets| }}


{{APIFunction|hasNonManifolds| |Check if the mesh has non-manifolds|a boolean}}


{{APIFunction|hasNonUniformOrientedFacets| |Checks if the mesh has facets with inconsistent orientation| }}


{{APIFunction|hasSelfIntersections| |Check if the mesh intersects itself| }}


{{APIFunction|inner| |Get the part inside of the intersection| }}


{{APIFunction|insertVertex|Vertex|Inserts a vertex into a facet| }}


{{APIFunction|intersect|Mesh|Intersection of this and the given mesh object.| }}


{{APIFunction|isSolid| |Check if the mesh is a solid| }}


{{APIFunction|meshFromSegment| |Create a mesh from segment| }}


{{APIFunction|nearestFacetOnRay|tuple, tuple|Get the index and intersection point of the nearest facet to a ray. The first parameter is a tuple of three floats the base point of the ray, the second parameter is ut uple of three floats for the direction. The result is a dictionary with an index and the intersection point or an empty dictionary if there is no intersection.|a dictionary}}


{{APIFunction|offset|float|Move the point along their normals| }}


{{APIFunction|offsetSpecial|float|Move the point along their normals| }}


{{APIFunction|optimizeEdges| |Optimize the edges to get nicer facets| }}


{{APIFunction|optimizeTopology| |Optimize the edges to get nicer facets| }}


{{APIFunction|outer| |Get the part outside the intersection| }}


{{APIFunction|printInfo| |Get detailed information about the mesh| }}


{{APIFunction|read| |Read in a mesh object from file.| }}


{{APIFunction|refine| |Refine the mesh| }}


{{APIFunction|removeComponents|integer|Remove components with less or equal to number of given facets| }}


{{APIFunction|removeDuplicatedFacets| |Remove duplicated facets| }}


{{APIFunction|removeDuplicatedPoints| |Remove duplicated points| }}


{{APIFunction|removeFacets|list|Remove a list of facet indices from the mesh| }}


{{APIFunction|removeFoldsOnSurface| |Remove folds on surfaces| }}


{{APIFunction|removeNonManifolds| |Remove non-manifolds| }}


{{APIFunction|rotate| |Apply a rotation to the mesh| }}


{{APIFunction|setPoint|int, Vector|Sets the point at index.| }}


{{APIFunction|smooth| |Smooth the mesh| }}


{{APIFunction|snapVertex| |Insert a new facet at the border| }}


{{APIFunction|splitEdge| |Split edge| }}


{{APIFunction|splitEdges| |Split all edges| }}


{{APIFunction|splitFacet| |Split facet| }}


{{APIFunction|swapEdge| |Swap the common edge with the neighbor| }}


{{APIFunction|transform| |Apply a transformation to the mesh| }}


{{APIFunction|transformToEigen| |Transform the mesh to its eigenbase| }}


{{APIFunction|translate|Vector|Apply a translation to the mesh| }}


{{APIFunction|unite|Mesh|Union of this and the given mesh object.| }}


{{APIFunction|write|string|Write the mesh object into file.| }}


{{APIFunction|writeInventor| |Write the mesh in OpenInventor format to a string.|a string}}


{{APIProperty|Area|the area of the mesh object.}}


{{APIProperty|CountFacets|the number of facets of the mesh object.}}


{{APIProperty|CountPoints|the number of vertices of the mesh object.}}


{{APIProperty|Facets|A collection of facets; With this attribute it is possible to get access to the facets of the mesh: for f in mesh.Facets: print f. Facet.Points is a list of coordinate-tupels for the vertices. Facet.PointIndices is a list of indice for the vertices of the facet. WARNING! store Facets in a local variable as it is generated on the fly, each time it is accessed.}}


{{APIProperty|Points|A collection of the mesh points; With this attribute it is possible to get access to the points of the mesh: for p in mesh.Points: print p.x, p.y, p.z,p.Index.WARNING! store Points in a local variable as it is generated on the fly, each time it is accessed.}}


{{APIProperty|Topology|the points and face indices as tuple. Topology[0] is a list of all vertices. Each being a tuple of 3 coordinates. Topology[1] is a list of all polygons. Each being a list of vertex indice into Topology[0] WARNING! store Topology in a local variable as it is generated on the fly, each time it is accessed.}}


{{APIProperty|Volume|the volume of the mesh object.}}


{{APIProperty|BoundBox|the BoundBox of the object}}


{{APIProperty|Matrix|the current transformation of the object as matrix}}


{{APIProperty|Placement|the current transformation of the object as placement}}


 

[Category:API](Category:API.md) [Category:Poweruser Documentation](Category:Poweruser_Documentation.md)
