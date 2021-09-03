

## Introduction

Dans FreeCAD, le mot \"[Shape](Shape/fr.md)\" est normalement utilisé pour faire référence à une classe [ Part TopoShape](Part_TopoShape.md) (`Part::TopoShape`), un type d\'objet qui donne un élément sa représentation géométrique et paramétrique 3D (cube, pyramide, sphère, cylindre, fusion, etc.).

Essentiellement, tous les objets affichés dans la [vue 3D](3D_view/fr.md) ont un [TopoShape](Part_TopoShape/fr.md), à l\'exception de \"[Mesh](Mesh/fr.md)\", qui ont un [MeshObject](Mesh_MeshObject/fr.md) (classe `Mesh::MeshObject`).

Voir [Part TopoShape](Part_TopoShape.md) pour plus d\'informations sur ce type d\'objet.

![](images/Shape_and_mesh.svg )


*A gauche: paramétrique [shape](Shape/fr.md) définie par les propriétés. A droite: [mesh](Mesh/fr.md) défini par des sommets et des surfaces triangulaires.*

## Utilisation

Les formes sont normalement créées par des fonctions internes de l\'[Atelier Part](Part_Workbench/fr.md) et sont finalement définies par le noyau de technologie [OpenCASCADE Technology](OpenCASCADE/fr.md) (OCCT).

Une fois qu\'une forme est créée, elle peut être utilisée et modifiée par tous les [ateliers](Workbenches/fr.md) en créant [objets scriptés](scripted_objects/fr.md) autour de cette forme.

Essentiellement, chaque objet dérivé d\'une [Part Feature](Part_Feature/fr.md) (classe `Part::Feature`) devrait contenir et manipuler une forme.

## Remarques

Dans un usage informel, une \"forme\" peut être n\'importe quelle figure géométrique visible dans la [vue 3D](3D_view/fr.md), et donc son concept peut être confondu avec celui de \"[Corps](Body/fr.md)\" ou \"[Partie](Part/fr.md)\".

Cependant, lorsque plus de précision est requise, la distinction doit être faite.

-   Un \"[Corps](Body/fr.md)\" est un objet dérivé d\'une [Part Feature](Part_Feature/fr.md) (classe `Part::Feature`), créé avec l\' [atelier PartDesign](PartDesign_Workbench/fr.md).
-   Un \"Shape\" est un objet interne, intégré dans le \"[Corps](Body/fr.md)\".
-   Un \"[Part](Part/fr.md)\" est utilisé pour regrouper plusieurs \"[Corps](Body/fr.md)\" pour former un [assemblage](assembly/fr.md). Une \"pièce\" a une collection de \"formes\", mais n\'a pas de \"forme\" qui lui soit propre.


 {{Document objects navi}} 

[Category:Glossary{{\#translation:}}](Category:Glossary.md)
