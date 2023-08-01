---
- GuiCommand:/fr
   Name:MeshPart CreateFlatMesh
   Name/fr:Mesh Développer un maillage
   MenuLocation:Maillages → Développer un maillage
   Workbenches:[Mesh](Mesh_Workbench/fr.md)
   Version:0.19
   SeeAlso:[Mesh Développer la face](MeshPart_CreateFlatFace/fr.md)
---

# MeshPart CreateFlatMesh/fr

## Description

La commande **Développer un maillage** crée une représentation plate d\'un objet maillé en le développant, en le dépliant. Le contour créé est une [Part Feature](Part_Feature/fr.md).

![](images/MeshPart_CreateFlatMesh_example.png ) 
*Un objet maillé et en rouge sa représentation aplatie*



## Utilisation

1.  Sélectionnez un seul objet maillé. Le maillage doit être \"développable\". Par exemple, pour développer un maillage cylindrique, il doit avoir des extrémités ouvertes et une couture ouverte. Les surfaces courbes doivent également avoir un maillage relativement fin. Utilisez la commande [Mesh Affiner](Mesh_RemeshGmsh/fr.md) si nécessaire.
2.  Sélectionnez l\'option **Maillages → <img src="images/MeshPart_CreateFlatMesh.svg" width=16px> Développer un maillage** du menu.



## Propriétés

Voir: [Part Feature](Part_Feature/fr.md).





{{Mesh Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [Mesh](Category_Mesh.md) > [MeshPart](MeshPart_Workbench.md) > MeshPart CreateFlatMesh/fr
