---
- GuiCommand:
   Name:Mesh PolyCut
   Name/fr:Mesh Couper un maillage
   MenuLocation:Maillages → Couper → Couper le maillage
   Workbenches:[Mesh](Mesh_Workbench/fr.md)
   SeeAlso:[Mesh Ajuster](Mesh_PolyTrim/fr.md), [Mesh Ajuster par plan](Mesh_TrimByPlane/fr.md)
---

# Mesh PolyCut/fr

## Description

La commande **Couper un maillage** coupe des faces entières à partir d\'objets maillés.



## Utilisation

1.  Pendant la commande, la [vue 3D](3D_view/fr.md) ne peut pas être modifiée. Il est conseillé d\'aligner correctement la vue 3D en premier.
2.  Sélectionnez un ou plusieurs objets maillés.
3.  Il existe plusieurs manières de lancer la commande :
    -   Appuyez sur le bouton **<img src="images/Mesh_PolyCut.svg" width=16px> [Couper le maillage](Mesh_PolyCut/fr.md)**.
    -   Sélectionnez l\'option **Maillages → Couper → <img src="images/_Mesh_PolyCut.svg" width=16px> Couper la maillage** dans le menu.
4.  Définissez un polygone en sélectionnant des points dans la vue 3D.
5.  Sélectionnez une option dans le menu contextuel de la vue 3D :
    -   
        **Intérieur**
        
        : supprime les faces qui sont (partiellement) à l\'intérieur du polygone.

    -   
        **Extérieur**
        
        : supprime les faces qui sont complètement à l\'extérieur du polygone.

    -   
        **Scinder**
        
        : supprime les faces qui sont complètement à l\'extérieur du polygone et crée un nouvel objet maillé les contenant.

    -   
        **Annuler**
        
        : annule la commande.





{{Mesh Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [Mesh](Mesh_Workbench.md) > Mesh PolyCut/fr
