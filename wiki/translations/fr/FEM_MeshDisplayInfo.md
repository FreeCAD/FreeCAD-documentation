---
- GuiCommand:/fr
   Name:FEM MeshDisplayInfo
   Name/fr:FEM Affichage des informations du maillage FEM
   MenuLocation:Menu contextuel sur l'objet maillé → Afficher les informations sur le maillage FEM
   Workbenches:[FEM](FEM_Workbench/fr.md)
   SeeAlso:[FEM Tutoriel](FEM_tutorial/fr.md)
---

# FEM MeshDisplayInfo/fr

## Description

Affiche les statistiques de base du maillage existant - nombre de nœuds et d\'éléments de chaque type. En particulier, le nombre total des éléments suivants est affiché :

-   Nœuds,
-   Arêtes,
-   Faces,
-   Polygones,
-   Volumes,
-   Polyèdres,

\* Arêtes linéaires,

-   Faces linéaires,
-   Volumes linéaires,

\* Arêtes quadratiques,

-   faces quadratiques,
-   Triangles quadratiques,
-   quadrangles quadratiques,
-   Volumes quadratiques,
-   hexaèdres quadratiques,
-   Tétraèdres quadratiques,
-   Prismes quadratiques,
-   Pyramides quadratiques.

## Utilisation

1.  Créez d\'abord un maillage d\'éléments finis (en utilisant l\'une des techniques disponibles).
2.  Sélectionnez le maillage dans la [Vue en arborescence](Tree_view/fr.md).
3.  Faites un clic droit dessus et choisissez le bouton **<img src="images/FEM_MeshDisplayInfo.svg" width=16px> [Afficher les informations sur le maillage FEM](FEM_MeshDisplayInfo/fr.md)**.
4.  Pour fermer la fenêtre FEM Mesh Info, cliquez sur **OK**.

## Script


{{code|code=
# setup some model with a fem mesh to print information from
from femexamples.ccx_cantilever_faceload import setup
setup()
# print the fem mesh information
print(App.ActiveDocument.Mesh.FemMesh)
}}

donnera le résultat suivant :


{{code|code=
>>> print(App.ActiveDocument.Mesh.FemMesh)
========================== Dump contents of mesh ==========================


1) Total number of nodes:       228
2) Total number of edges:       0
3) Total number of faces:       0
4) Total number of polygons:    0
5) Total number of volumes:     79
6) Total number of polyhedrons: 0

7) Total number of linear edges:    0
8) Total number of linear faces:    0
9) Total number of linear volumes:  0

10) Total number of quadratic edges:    0
11) Total number of quadratic faces:    0
12) Total number of quadratic volumes:  79
12.1) Number of quadratic hexahedrons:  0
12.2) Number of quadratic tetrahedrons: 79
12.3) Number of quadratic prisms:       0
12.4) Number of quadratic pyramids:     0

===========================================================================
}}





{{FEM Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM MeshDisplayInfo/fr
