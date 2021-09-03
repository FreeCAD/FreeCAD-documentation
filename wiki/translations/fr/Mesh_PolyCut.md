---
- GuiCommand:/fr
   Name:Mesh PolyCut
   Name/fr:Mesh Couper un maillage
   MenuLocation:Maillages → Cutting → Couper le maillage
   Workbenches:[Mesh](Mesh_Workbench/fr.md)
   SeeAlso:[Mesh Découper](Mesh_PolyTrim/fr.md), [Mesh Créer une section](Mesh_TrimByPlane/fr.md)
---

## Description

La commande **Mesh Couper un maillage** coupe des faces entières à partir d\'objets maillés.

## Utilisation

1.  Pendant la commande, la [Vue 3D](3D_view.md) ne peut pas être modifiée. Il est conseillé d\'aligner correctement la vue 3D en premier.
2.  Sélectionnez un ou plusieurs objets maillés.
3.  Il existe plusieurs manières d\'appeler la commande:
    -   Appuyez sur le bouton **<img src="images/Mesh_PolyCut.svg" width=16px> [Mesh Coupe un maillage à l'aide du polygone sélectionné](Mesh_PolyCut/fr.md)**.
    -   Sélectionnez l\'option {{MenuCommand|Maillages → Cutting → <img src="images/_Mesh_PolyCut.svg" width=16px> Couper la maillage}} dans le menu.
4.  Définissez un polygone en sélectionnant des points dans la vue 3D.
5.  Sélectionnez une option dans le menu contextuel de la vue 3D:
    -   
        {{MenuCommand|Intérieur}}
        
        : supprime les faces qui sont (partiellement) à l\'intérieur du polygone.

    -   
        {{MenuCommand|Extérieur}}
        
        : supprime les faces qui sont complètement à l\'extérieur du polygone.

    -   
        {{MenuCommand|Scinder}}
        
        : supprime les faces qui sont complètement à l\'extérieur du polygone et crée un nouvel objet maillé les contenant.

    -   
        {{MenuCommand|Annuler}}
        
        : annule la commande.





{{Mesh Tools navi

}}  
