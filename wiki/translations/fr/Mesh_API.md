# Mesh API/fr
**(novembre 2018) Ces informations peuvent être incomplètes et obsolètes. Pour la dernière version de l'API, consultez la [https://www.freecadweb.org/api documentation de l'auto-génération de l'API].**

Les objets maillés peuvent être manipulés par l\'ajout de nouvelles facettes, suppression de facettes, l\'importation d\'un fichier STL, transformant le maillage et bien plus encore. Pour un aperçu complet de ce qui peut être fait voir aussi la documentation de l\'[atelier Mesh](Mesh_Workbench/fr.md). Un objet maillé ne peut pas être ajouté à un document existant directement. Par conséquent, le document doit créer un objet avec une classe propriété qui soutient les mailles. Exemple:


```python
m = Mesh.Mesh()
... # Manipule le maillage
d = FreeCAD.activeDocument() # Obtenir une référence au document actif
f = d.addObject("Mesh::Feature", "Mesh") # Créer une fonction maillage 
f.Mesh = m # affecter l'objet maillage à la propriété interne
d.recompute()
```


{{APIFunction|addFacet|Facet|Ajoute une facette à la maille| }}


{{APIFunction|addFacets|liste|Ajoute une liste de facettes à la maille| }}


{{APIFunction|addMesh|Mesh|Combine ce maillage avec un autre maillage|.}}


{{APIFunction|clear| |Efface la maille| }}


{{APIFunction|coarsen| |Grossit la maille| }}


{{APIFunction|collapseEdge|Bordure|Supprime une arête et deux facettes qui partagent cette arête | }}


{{APIFunction|collapseFacet|Facet|Supprime une facette| }}


{{APIFunction|collapseFacets|liste|Supprime une liste de facettes| }}


{{APIFunction|copy| |Crée une copie de ce maillage|un objet Mesh}}


{{APIFunction|countComponents| |Obtenir le nombre de zones topologiques indépendantes|un entier}}


{{APIFunction|countNonUniformOrientedFacets| |Obtenir le nombre de facettes de mal orientées|un entier}}


{{APIFunction|countSegments| |Obtenir le nombre de segments qui peut également être 0|un entier}}


{{APIFunction|crossSections| |Obtenir les sections du maillage à travers plusieurs plans| }}


{{APIFunction|difference|Mesh|Différence de cela et l'objet de maillage donné|.}}


{{APIFunction|fillupHoles| |trous pleins| }}


{{APIFunction|fixDeformations| |réparation de facettes déformées| }}


{{APIFunction|fixDegenerations| |Retirer facettes dégénérées| }}


{{APIFunction|fixIndices| |Réparation des indices invalides| }}


{{APIFunction|fixSelfIntersections| |réparation auto-intersections| }}


{{APIFunction|flipNormals| |inverser les normales de maillage| }}


{{APIFunction|foraminate| |Obtenir une liste des indices de facettes et les points d'intersection| }}


{{APIFunction|getPlanes| |Obtenir tous les plans de la maille comme segment. Dans le pire des cas, chaque triangle peut être considéré comme un seul plan si aucun de ses voisins n'est coplanaires|.}}


{{APIFunction|getSegment|entier|Obtenir une liste des indices de facettes qui décrit un segment| }}


{{APIFunction|getSeparateComponents| |Retourne une liste contenant les différents composants (zones séparées) de la maille comme maillages séparés|liste}}


{{APIFunction|harmonizeNormals| |Régler les facettes mal orientées| }}


{{APIFunction|hasNonManifolds| |Vérifiez si le maillage a des non-mutiples|un booléen}}


{{APIFunction|hasNonUniformOrientedFacets| |Vérifie si le maillage a des facettes avec une orientation incompatible| }}


{{APIFunction|hasSelfIntersections| |Vérifier si le maillage se croise| }}


{{APIFunction|inner| |Obtenir la partie intérieure de l'intersection| }}


{{APIFunction|insertVertex|Vertex|Insère un sommet dans une facette| }}


{{APIFunction|intersect|Mesh|Intersection de cela et l'objet maillage donné.| }}


{{APIFunction|isSolid| |Vérifiez si le maillage est un solide| }}


{{APIFunction|meshFromSegment| |Créer un maillage à partir d'un segment| }}


{{APIFunction|nearestFacetOnRay|tuple, tuple|Retourne l'index et le pont d'intersection de la facette la plus proche d'un rayon. Le premier paramètre est un tuple de trois flotteurs le point du rayon de base et le second paramètre est un uplet  de trois flotteurs pour la direction. Le résultat est un dictionnaire avec un index et le point d'intersection ou un dictionnaire vide s'il n'y a pas d'intersection|. Un dictionnaire}}


{{APIFunction|offset|float|Déplacez le point le long de leurs normales| }}


{{APIFunction|offsetSpecial|flotter|Déplacez le point le long de leurs normales| }}


{{APIFunction|optimizeEdges| |Optimiser les bords pour obtenir des facettes plus agréable| }}


{{APIFunction|optimizeTopology| |Optimiser les bords pour obtenir facettes plus agréable| }}


{{APIFunction|outer| |Obtenez la partie extérieure de l'intersection| }}


{{APIFunction|printInfo| |Obtenez des informations détaillées sur la maille| }}


{{APIFunction|read| |Lire dans un maillage à partir du fichier|.}}


{{APIFunction|refine| ||Affiner le maillage}}


{{APIFunction|removeComponents|entier|Suppression de composants avec moins ou égal au nombre de facettes donnés| }}


{{APIFunction|removeDuplicatedFacets| |Suppression facettes doubles| }}


{{APIFunction|removeDuplicatedPoints| |supprimer des points doubles| }}


{{APIFunction|removeFacets|liste|supprimer une liste d'indices de facettes du maillage| }}


{{APIFunction|removeFoldsOnSurface| |Supprimer plis sur des surfaces| }}


{{APIFunction|removeNonManifolds| |Retirer non collecteurs| }}


{{APIFunction|rotate| |Appliquer une rotation à la maille| }}


{{APIFunction|setPoint|int, Vector|Règle le point à l'index|.}}


{{APIFunction|smooth| |Lisser la maille| }}


{{APIFunction|snapVertex| |Insérer une nouvelle facette à la frontière| }}


{{APIFunction|splitEdge| |diviser les bords| }}


{{APIFunction|splitEdges| |diviser les bords | }}


{{APIFunction|splitFacet| |Diviser la facette | }}


{{APIFunction|swapEdge| |Remplacez le bord commun avec le voisin| }}


{{APIFunction|transform| |appliquer une transformation à la maille| }}


{{APIFunction|transformToEigen| |Transforme le maillage pour son eigenbase| }}


{{APIFunction|translate|Vecteur|Appliquer une translation à la maille| }}


{{APIFunction|unite|Mesh|Union de ceci avec l'objet de maillage donné|.}}


{{APIFunction|write|chaîne|Ecrire l'objet maillage dans le fichier|.}}


{{APIFunction|writeInventor| |Ecrire le maillage au format OpenInventor dans une chaine|. une chaîne}}


{{APIProperty|Area|. la zone de l'objet mesh}}


{{APIProperty|CountFacets|le nombre de facettes de l'objet mesh}}


{{APIProperty|CountPoints|le nombre de sommets de l'objet mesh}}


{{APIProperty|Facets|Une collection de facettes..; Avec cet attribut, il est possible d’avoir accès aux facettes du maillage: pour f dans mesh.Facets: print f. Facet.Points est une liste de tupels de coordonnées pour les sommets. Facet.PointIndices est une liste d'indices pour les sommets de la facette. ATTENTION! stocker les facettes dans une variable locale telle qu’elle est générée à la volée, chaque fois qu’on y accède.}}


{{APIProperty|Points|Une collection de points du maillage; Avec cet attribut, il est possible d'avoir accès à des points du maillage: pour p dans mesh.Points: Print p.x, p.y, p.z, p.Index.WARNING! stocke des points dans une variable locale, telle qu'elle est générée à la volée, à chaque accès.}}


{{APIProperty|Topology|les points et les indices de face comme tuple Topology[0] est une liste de tous les sommets. Chacun étant un tuple de 3 coordonnées. Topology[1] est une liste de tous les polygones. Chacune étant une liste d'indices de sommet dans Topology[0] AVERTISSEMENT! stocker la topologie dans une variable locale telle qu'elle est générée à la volée, à chaque accès.}}


{{APIProperty|Volume|le volume de l'objet mesh}}


{{APIProperty|BoundBox|la boîte englobante de l'objet}}


{{APIProperty|Matrix|la transformation actuelle de l'objet comme matrice}}


{{APIProperty|Placement|la transformation actuelle de l'objet comme placement}}


 

_ _

---
[documentation index](../README.md) > [API](Category_API.md) > [Mesh](Mesh_Workbench.md) > Mesh API/fr
