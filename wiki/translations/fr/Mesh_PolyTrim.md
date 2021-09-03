---
- GuiCommand:/fr
   Name:Mesh PolyTrim
   Name/fr:Mesh Découper
   MenuLocation:Maillages → Cutting → Découper
   Workbenches:[Mesh](Mesh_Workbench/fr.md)
   SeeAlso:[Mesh Couper le maillage](Mesh_PolyCut/fr.md), [Mesh Créer une section](Mesh_TrimByPlane/fr.md)
---

## Description

La commande **Mesh Découper** permet de découper les faces et parties de faces à partir d\'objets maillés.

## Utilisation

1.  Pendant la commande, la [Vue 3D](3D_view/fr.md) ne peut pas être modifiée. Il est conseillé d\'aligner correctement la vue 3D en premier.
2.  Sélectionnez un ou plusieurs objets maillés.
3.  Il existe plusieurs façons d\'appeler la commande:
    -   Appuyez sur le bouton **<img src="images/Mesh_PolyTrim.svg" width=16px> [Découper un maillage avec une succession de points](Mesh_PolyTrim/fr.md)** button.
    -   Sélectionnez l\'option {{MenuCommand|Maillages → Cutting → <img src="images/Mesh_PolyTrim.svg" width=16px> Découper}} dans le menu.
4.  Définissez un polygone en sélectionnant des points dans la vue 3D.
5.  Sélectionnez une option dans le menu contextuel de la vue 3D:
    -   
        {{MenuCommand|Inner}}
        
        : supprime les faces et les parties de faces qui sont à l\'intérieur du polygone.

    -   
        {{MenuCommand|Outer}}
        
        : supprime les faces et les parties de faces qui sont en dehors du polygone.

    -   
        {{MenuCommand|Split}}
        
        : supprime les faces et les parties de faces qui sont en dehors du polygone et crée un nouvel objet maillé les contenant.

    -   
        {{MenuCommand|Cancel}}
        
        : annule la commande.





{{Mesh Tools navi

}}  
