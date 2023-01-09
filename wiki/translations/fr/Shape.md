# Shape/fr
## Introduction

Dans FreeCAD, le mot \"[Shape](Shape/fr.md)\" est normalement utilisé pour faire référence à une classe [ Part TopoShape](Part_TopoShape.md) (`Part::TopoShape`), un type d\'objet qui donne un élément sa représentation géométrique et paramétrique 3D (cube, pyramide, sphère, cylindre, fusion, etc.).

Essentiellement, tous les objets affichés dans la [vue 3D](3D_view/fr.md) ont un [TopoShape](Part_TopoShape/fr.md), à l\'exception des \"[maillages](Mesh/fr.md)\", qui ont un [MeshObject](Mesh_MeshObject/fr.md) (classe `Mesh::MeshObject`).

Voir [Part TopoShape](Part_TopoShape.md) pour plus d\'informations sur ce type d\'objet.

![](images/Shape_and_mesh.svg )



*A gauche: une [shape](Shape/fr.md) paramétrique définie par les propriétés. A droite: un [mesh](Mesh/fr.md) défini par des sommets et des surfaces triangulaires.*

## Utilisation

Les formes sont normalement créées par des fonctions internes de l\'[Atelier Part](Part_Workbench/fr.md) et sont finalement définies par le noyau de technologie [OpenCASCADE Technology](OpenCASCADE/fr.md) (OCCT).

Une fois qu\'une forme est créée, elle peut être utilisée et modifiée par tous les [ateliers](Workbenches/fr.md) en créant [objets scriptés](scripted_objects/fr.md) autour de cette forme.

Essentiellement, chaque objet dérivé d\'une [Part Feature](Part_Feature/fr.md) (classe `Part::Feature`) devrait contenir et manipuler une forme.

## Remarques

Dans un usage informel, une \"Shape\" peut être n\'importe quelle figure géométrique visible dans la [vue 3D](3D_view/fr.md), et donc son concept peut être confondu avec celui de \"[Corps](Body/fr.md)\" ou \"[Part](Part/fr.md)\".

Cependant, lorsque plus de précision est requise, la distinction doit être faite.

-   Un \"[Corps](Body/fr.md)\" est un objet dérivé d\'une [Part Feature](Part_Feature/fr.md) (classe `Part::Feature`), créé avec l\'[atelier PartDesign](PartDesign_Workbench/fr.md).
-   Un \"Shape\" est un objet interne, intégré dans le \"[Corps](Body/fr.md)\".
-   Un \"[Part](Part/fr.md)\" est utilisé pour regrouper plusieurs \"[Corps](Body/fr.md)\" pour former un [assemblage](assembly/fr.md). Un \"Part\" a une collection de \"Shapes\", mais n\'a pas de \"Shape\" qui lui soit propre.


 {{Document objects navi}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Glossary](Category_Glossary.md) > [Part](Category_Part.md) > Shape/fr
