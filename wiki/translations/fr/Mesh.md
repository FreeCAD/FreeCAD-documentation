# Mesh/fr
## Introduction

Dans FreeCAD, le mot \"_\".

Les maillages sont des objets très simples, ne contenant que des sommets (points), des arêtes et des faces triangulaires. En général, ils sont faciles à créer, à modifier, à subdiviser et à étirer, et peuvent être transmis d\'une application à une autre sans aucune perte de détails. De plus, comme les maillages contiennent des données très simples, les applications 3D comme les logiciels d\'animation et les jeux vidéo peuvent en gérer de très grandes quantités (millions de triangles) sans utiliser beaucoup de ressources informatiques.

Cependant, dans le domaine de l\'ingénierie, les maillages présentent une grande limitation: ils ne sont constitués que de surfaces et n\'ont pas d\'informations de \"masse\", ils ne se comportent donc pas comme des \"solides\". Cela signifie que les opérations à base de solides, comme l\'[addition ou la soustraction booléennen](Part_Boolean/fr.md) sont difficiles à effectuer sur les maillages. De plus, comme ils sont définis par des points individuels, ils sont difficiles à décrire de façon paramétrique.

Voir [Mesh MeshObject](Mesh_MeshObject/fr.md) pour plus d\'informations sur ce type d\'objet, et voir [Polygon mesh](https://en.wikipedia.org/wiki/Polygon_mesh) pour des informations génériques dans les systèmes informatiques.

![](images/Shape_and_mesh.svg )


*A gauche: paramétrique _ défini par des sommets et des surfaces triangulaires.*

## Utilisation

Les maillages sont normalement créés par des fonctions internes de [Mesh Workbench](Mesh_Workbench/fr.md), ou par l\'importation de fichiers au format de maillage, comme STL et OBJ.

Essentiellement, chaque objet dérivé d\'une [Mesh Feature](Mesh_Feature/fr.md) (classe `Mesh::Feature`) devrait contenir et manipuler un maillage.

Étant donné que FreeCAD est principalement conçu pour être un modeleur solide, il est mieux adapté pour traiter les solides [Shapes](Shape/fr.md). Il peut importer et afficher des maillages dans la [vue 3D](3D_view/fr.md), mais pour les transformer ou créer une nouvelle géométrie, le maillage doit d\'abord être converti en [Shape](Shape/fr.md) (voir [Part ShapeFromMesh ](Part_ShapeFromMesh/fr.md)). Dans de nombreux cas, cette conversion n\'est pas automatique et nécessite de recréer la géométrie à l\'aide de techniques de modélisation solides, en utilisant les outils [Part](Part_Workbench/fr.md) et [PartDesign](PartDesign_Workbench/fr.md).

## Maillage par éléments finis 

Dans FreeCAD, le mot \"[Mesh](Mesh/fr.md)\" peut également faire référence à un objet spécifique qui sera utilisé dans l\'analyse par éléments finis (FEA).

Lorsqu\'un objet avec un solide _ (`Mesh::Feature` classe).

Pour plus d\'informations, voir [Atelier FEM](FEM_Workbench/fr.md) et [FEM Mesh](FEM_Mesh/fr.md).

## Plus d\'informations 

-   [Géométrie polygonale (maillage)](https://forum.freecadweb.org/viewtopic.php?f=8&t=47493)


{{Mesh Tools navi

}} {{FEM Tools navi}} {{Document objects navi}} 

_

---
[documentation index](../README.md) > [Glossary](Category_Glossary.md) > Mesh/fr
