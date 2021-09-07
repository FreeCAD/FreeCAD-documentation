


{{VeryImportantMessage|(November 2018) This information may be incomplete and outdated. For the latest API, see the [https://www.freecadweb.org/api autogenerated API documentation].}}


<div class="mw-translate-fuzzy">

Los objetos malla pueden ser manipulados añadiendo facetas, eliminando facetas, importando desde un archivo STL, transformando la malla y muchas opciones más. Para una descripción completa de lo que se puede hacer mira también la documentación del [Módulo de malla](Mesh_Workbench/es.md). Un objeto malla no se puede añadir a un documento existente directamente. Por lo tanto el documento debe crear un objeto con clase apropiada que soporte las mallas. Por ejemplo:


</div>

 {.python}
 m = Mesh.Mesh()
 ... # Manipulate the mesh
 d = FreeCAD.activeDocument() # Get a reference to the actie document
 f = d.addObject("Mesh::Feature", "Mesh") # Create a mesh feature
 f.Mesh = m # Assign the mesh object to the internal property
 d.recompute()



<div class="mw-translate-fuzzy">


{{APIFunction/es|addFacet|Facet|Añade una faceta a la malla| }}


{{APIFunction/es|addFacets|list|Añade una lista de facetas a la malla| }}


{{APIFunction/es|addMesh|Mesh|Combina esta malla con otra malla.| }}


{{APIFunction/es|clear| |Alisa la malla| }}


{{APIFunction/es|coarsen| |Desalisado de malla| }}


{{APIFunction/es|collapseEdge|Edge|Elimina una arista y ambas facetas que compartían esa arista| }}


{{APIFunction/es|collapseFacet|Facet|Elimina una faceta| }}


{{APIFunction/es|collapseFacets|list|Elimina una lista de facetas| }}


{{APIFunction/es|copy| |Crea una copia de esta malla|Un objeto malla}}


{{APIFunction/es|countComponents| |Obtiene el número de áreas topológicamente independientes|Un entero}}


{{APIFunction/es|countNonUniformOrientedFacets| |Obtiene el número de facetas mal orientadas|Un entero}}


{{APIFunction/es|countSegments| |Obtiene el número de segmentos que también podría ser 0|Un entero}}


{{APIFunction/es|crossSections| |Obtiene secciones de cruce de la malla a través de diversos planos| }}


{{APIFunction/es|difference|Mesh|Diferencia de esta y el objeto malla dado.| }}


{{APIFunction/es|fillupHoles| |Rellena agujeros| }}


{{APIFunction/es|fixDeformations| |Repara facetas deformadas| }}


{{APIFunction/es|fixDegenerations| |Elimina facetas degeneradas| }}


{{APIFunction/es|fixIndices| |Repara cualquier índice inválido| }}


{{APIFunction/es|fixSelfIntersections| |Repara auto-intersecciones| }}


{{APIFunction/es|flipNormals| |Invierte las normales de la malla| }}


{{APIFunction/es|foraminate| |Obtiene una lista de índices de facetas y puntos de intersección| }}


{{APIFunction/es|getPlanes| |Obtiene todos los planos de la malla como segmentos. En el peor de los casos cada triángulo se puede considerar un único plano si ninguno de sus vecinos es coplanar.| }}


{{APIFunction/es|getSegment|integer|Obtiene una lista de índices de facetas que describen un segmento| }}


{{APIFunction/es|getSeparateComponents| |Devuelve una lista conteniendo los diferentes componentes (áreas separadas) de la malla como mallas separadas|Una lista}}


{{APIFunction/es|harmonizeNormals| |Ajusta las facetas mal orientadas| }}


{{APIFunction/es|hasNonManifolds| |Comprueba si la malla tiene non-manifolds|Un booleano}}


{{APIFunction/es|hasNonUniformOrientedFacets| |Comprueba si la malla tiene facetas con orientación inconsistente| }}


{{APIFunction/es|hasSelfIntersections| |Comprueba si la malla intersecta consigo misma| }}


{{APIFunction/es|inner| |Obtiene la pieza dentro de la intersección| }}


{{APIFunction/es|insertVertex|Vertex|Inserta un vértice en una faceta| }}


{{APIFunction/es|intersect|Mesh|Intersección de esta y el objeto malla dado.| }}


{{APIFunction/es|isSolid| |Comprueba si la malla es un sólido| }}


{{APIFunction/es|meshFromSegment| |Crea una malla a partir de segmentos| }}


{{APIFunction/es|nearestFacetOnRay|tuple, tuple|Obtiene el índice y punto de intersección de las facetas más cercanas a un rayo. El primer parámetro es una tupla de tres números de coma flotante de un punto base del rayo, el segundo parámetro es una tupla de tres números de coma flotante para la orientación. El resultado es un diccionario con un índice y el punto de intersección o un diccionario vacio si no hay intersección.|Un diccionario}}


{{APIFunction/es|offset|float|Mueve el punto a lo largo de sus normales| }}


{{APIFunction/es|offsetSpecial|float|Mueve el punto a lo largo de su normal| }}


{{APIFunction/es|optimizeEdges| |Optimiza las aristas para conseguir mejores facetas| }}


{{APIFunction/es|optimizeTopology| |Optimiza las aristas para conseguir mejores facetas| }}


{{APIFunction/es|outer| |Obtiene la pieza fuera de la intersección| }}


{{APIFunction/es|printInfo| |Obtiene información detallada de la malla| }}


{{APIFunction/es|read| |Lee un objeto malla desde un archivo.| }}


{{APIFunction/es|refine| |Refina la malla| }}


{{APIFunction/es|removeComponents|integer|Elimina componentes con menos o igual número de facetas dadas| }}


{{APIFunction/es|removeDuplicatedFacets| |Elimina facetas duplicadas| }}


{{APIFunction/es|removeDuplicatedPoints| |Elimina puntos duplicados| }}


{{APIFunction/es|removeFacets|list|Elimina una lista de índices de facetas desde la malla| }}


{{APIFunction/es|removeFoldsOnSurface| |Elimina pliegues en superficies| }}


{{APIFunction/es|removeNonManifolds| |Elimina non-manifolds| }}


{{APIFunction/es|rotate| |Aplica una rotación a la malla| }}


{{APIFunction/es|setPoint|int, Vector|Establece el punto en el índice.| }}


{{APIFunction/es|smooth| |Suaviza la malla| }}


{{APIFunction/es|snapVertex| |Inserta una faceta nueva en el borde| }}


{{APIFunction/es|splitEdge| |Dividir arista| }}


{{APIFunction/es|splitEdges| |Dividir todas las aristas| }}


{{APIFunction/es|splitFacet| |Dividir faceta| }}


{{APIFunction/es|swapEdge| |Cambia la arista común con el vecino| }}


{{APIFunction/es|transform| |Aplica una trasformación a la malla| }}


{{APIFunction/es|transformToEigen| |Transforma la malla en su eigenbase| }}


{{APIFunction/es|translate|Vector|Aplica una translación a la malla| }}


{{APIFunction/es|unite|Mesh|Unión de esta y del objeto malla dado.| }}


{{APIFunction/es|write|string|Escribe el objeto malla en un archivo.| }}


{{APIFunction/es|writeInventor| |Escribe la malla en formato de OpenInventor en una cadena de texto.|Una cadena de texto}}


{{APIProperty/es|Area|El área del objeto malla.}}


{{APIProperty/es|CountFacets|El número de facetas del objeto malla.}}


{{APIProperty/es|CountPoints|El número de vértices del objeto malla.}}


{{APIProperty/es|Facets|Una colección de facetas; Con este atributo es posible tener acceso a las facetas de la malla: for p in mesh.Facets: print p}}


{{APIProperty/es|Points|Una colección de puntos de malla; Con este atributo es posible tener acceso a los puntos de la malla: for p in mesh.Points: print p.x, p.y, p.z}}


{{APIProperty/es|Topology|Los índices de los puntos y caras como tuplas.}}


{{APIProperty/es|Volume|El volumen del objeto malla.}}


{{APIProperty/es|BoundBox|La caja de abarque del objeto}}


{{APIProperty/es|Matrix|La transformación actualdel objeto como matriz}}


{{APIProperty/es|Placement|La transformación actual del objeto como colocación}}


</div>


 

[Category:API{{\#translation:}}](Category:API.md) [Category:Poweruser Documentation{{\#translation:}}](Category:Poweruser_Documentation.md)