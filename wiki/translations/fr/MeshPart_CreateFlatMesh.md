---
- GuiCommand:/fr
   Name:MeshPart CreateFlatMesh
   Name/fr:MeshPart Développer un objet maillé
   MenuLocation:Maillages → Unwrap Mesh
   Workbenches:[Mesh](Mesh_Workbench/fr.md)
   SeeAlso:[MeshPart Développer une face](MeshPart_CreateFlatFace/fr.md)
---

# MeshPart CreateFlatMesh/fr

## Description

La commande **MeshPart Développer un objet maillé** crée une représentation plate d\'un objet maillé en le développant, en le dépliant. Le contour créé est une [Part Feature](Part_Feature/fr.md).

![](images/MeshPart_CreateFlatMesh_example.png ) 
*Un objet maillé et en rouge sa représentation plate*

## Utilisation

1.  Sélectionnez un seul objet maillé. Le maillage doit être «déballable». Par exemple, pour dérouler un maillage cylindrique, il doit avoir des extrémités ouvertes et une couture ouverte. Les surfaces courbes doivent également avoir un maillage relativement fin. Utilisez la commande [Mesh Affinage](Mesh_RemeshGmsh/fr.md) si nécessaire.
2.  Sélectionnez l\'option **Maillages → <img src="images/MeshPart_CreateFlatMesh.svg" width=16px> Unwrap Mesh** dans le menu.

## Propriétés

Voir: [Part Feature](Part_Feature/fr.md).





{{Mesh Tools navi

}}

---
[documentation index](../README.md) > [MeshPart](MeshPart_Workbench.md) > MeshPart CreateFlatMesh/fr
