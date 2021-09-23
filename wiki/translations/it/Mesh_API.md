# Mesh API/it



**(Novembre 2018) Queste informazioni potrebbero essere incomplete e obsolete. Per l'ultima API, vedere la pagina [https://www.freecadweb.org/api Documentazione API autogenerata].**


<div class="mw-translate-fuzzy">

Gli oggetti mesh possono essere manipolati aggiungendo nuove sfaccettature, cancellando delle sfaccettature, importando da un file STL, trasformando la rete e in molti altri modi. Per una panoramica completa di ciò che si può fare vedere anche la documentazione del [Modulo Mesh](Mesh_Workbench/it.md). Un oggetto mesh non può essere aggiunto direttamente ad un documento esistente. Pertanto, il documento deve creare un oggetto con una classe appropriataa che supporta le mesh. Esempio:


</div>


```python
m = Mesh.Mesh()
... # Manipulate the mesh
d = FreeCAD.activeDocument() # Get a reference to the actie document
f = d.addObject("Mesh::Feature", "Mesh") # Create a mesh feature
f.Mesh = m # Assign the mesh object to the internal property
d.recompute()
```


{{APIFunction|addFacet|Facet|Aggiunge una sfaccettatura alla maglia| }}


{{APIFunction|addFacets|list|Aggiunge un elenco di sfaccettature alla maglia| }}


{{APIFunction|addMesh|Mesh|Combina questa mesh con un'altra mesh.| }}


{{APIFunction|clear| |Cancella la mesh| }}


{{APIFunction|coarsen| |Rende grossolana la mesh| }}


{{APIFunction|collapseEdge|Edge|Rimuove un bordo e entrambe le sfaccettature che condividono questo bordo| }}


{{APIFunction|collapseFacet|Facet|Rimuove una sfaccettatura| }}


{{APIFunction|collapseFacets|list|Rimuove una seriea di sfaccettature| }}


{{APIFunction|copy| |Crea una copia di questa maglia | un oggetto Mesh}}


{{APIFunction|countComponents| |Ottiene il numero di aree topologiche indipendenti | un intero}}


{{APIFunction|countNonUniformOrientedFacets| |Ottiene il numero di sfaccettature orientate male | un intero}}


{{APIFunction|countSegments| |Ottiene il numero di segmenti che possono essere anche 0 | un numero intero}}


{{APIFunction|crossSections| |Ottiene sezioni trasversali della rete attraverso diversi piani| }}


{{APIFunction|difference|Mesh|Differenze tra questo oggetto e l'oggetto mesh dato.| }}


{{APIFunction|fillupHoles| |Riempie i fori| }}


{{APIFunction|fixDeformations| |Ripara le faccette deformate| }}


{{APIFunction|fixDegenerations| |Rimuove le sfaccettature degenerate| }}


{{APIFunction|fixIndices| |Ripara eventuali indici non validi| }}


{{APIFunction|fixSelfIntersections| |Ripara le autointersezioni| }}


{{APIFunction|flipNormals| |Inverte le normali delle mesh| }}


{{APIFunction|foraminate| |Ottiene un elenco di indici delle faccette e dei punti di intersezione| }}


{{APIFunction|getPlanes| |Ottiene tutti i piani della rete come segmento. Nel caso peggiore ogni triangolo può essere considerato come unico piano se nessuno dei suoi vicini è complanare.| }}


{{APIFunction|getSegment|integer|Ottiene un elenco di indici delle faccette che descrivono un segmento| }}


{{APIFunction|getSeparateComponents| |Restituisce una lista contenente le diverse componenti (aree separate) della rete come mesh separate |una lista}}


{{APIFunction|harmonizeNormals| |Regola le sfaccettature orientate male| }}


{{APIFunction|hasNonManifolds| |Controlla se la mesh contiene non-manifolds | un booleano}}


{{APIFunction|hasNonUniformOrientedFacets| |Verifica se la rete ha dellle sfaccettature con orientamento incoerente| }}


{{APIFunction|hasSelfIntersections| |Controlla se la mesh si interseca| }}


{{APIFunction|inner| |Ottiene la parte interna all'intersezione| }}


{{APIFunction|insertVertex|Vertex|Inserisce un vertice in una sfaccettatura| }}


{{APIFunction|intersect|Mesh|Intersezione tra questo oggetto e l'oggetto mesh dato.| }}


{{APIFunction|isSolid| |Controlla se la mesh è un solido| }}


{{APIFunction|meshFromSegment| |Creare una mesh da un segmento| }}


{{APIFunction|nearestFacetOnRay|tuple, tuple|Get the index and intersection point of the nearest facet to a ray. The first parameter is a tuple of three floats the base point of the ray, the second parameter is ut uple of three floats for the direction. The result is a dictionary with an index and the intersection point or an empty dictionary if there is no intersection.|a dictionary}}


{{APIFunction|offset|float|Sposta il punto lungo le sue normali| }}


{{APIFunction|offsetSpecial|float|Sposta il punto lungo le sue normali| }}


{{APIFunction|optimizeEdges| |Ottimizza i bordi per ottenere delle faccette migliori| }}


{{APIFunction|optimizeTopology| |Ottimizza i bordi per ottenere delle faccette migliori| }}


{{APIFunction|outer| |Ottiene la parte al di fuori l'intersezione| }}


{{APIFunction|printInfo| |Ottiene informazioni dettagliate sulla mesh| }}


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


{{APIProperty|Facets|A collection of facets; With this attribute it is possible to get access to the facets of the mesh: for p in mesh.Facets: print f. Facet.Points is a list of coordinate-tupels for the vertices. Facet.PointIndices is a list of indice for the vertices of the facet. WARNING! store Facets in a local variable as it is generated on the fly, each time it is accessed.}}


{{APIProperty|Points|A collection of the mesh points; With this attribute it is possible to get access to the points of the mesh: for p in mesh.Points: print p.x, p.y, p.z, p.Index.WARNING! store Points in a local variable as it is generated on the fly, each time it is accessed.}}


{{APIProperty|Topology|the points and face indices as tuple. Topology[0] is a list of all vertices. Each being a tuple of 3 coordinates. Topology[1] is a list of all polygons. Each being a list of vertex indice into Topology[0] WARNING! store Topology in a local variable as it is generated on the fly, each time it is accessed.}}


{{APIProperty|Volume|the volume of the mesh object.}}


{{APIProperty|BoundBox|the BoundBox of the object}}


{{APIProperty|Matrix|the current transformation of the object as matrix}}


{{APIProperty|Placement|the current transformation of the object as placement}}


 

[Category:API](Category:API.md) [Category:Poweruser Documentation](Category:Poweruser_Documentation.md)
