---
- GuiCommand:
   Name:Mesh Segmentation
   Name/fr:Mesh Segmentation
   MenuLocation:Maillages → Segmenter le maillage...
   Workbenches:[Mesh](Mesh_Workbench/fr.md)
   SeeAlso:[Mesh Segmentation adaptée](Mesh_SegmentationBestFit/fr.md)
---

# Mesh Segmentation/fr

## Description

La commande **Segmentation** crée des segments de maillage séparés pour des types de surface spécifiés d\'un maillage.



## Utilisation

1.  Sélectionnez un seul objet maillé.
2.  Il existe plusieurs façons de lancer la commande :
    -   Appuyez sur le bouton **<img src="images/Mesh_Segmentation.svg" width=16px> [Segmenter le maillage...](Mesh_Segmentation/fr.md)
**
    -   Sélectionnez l\'option **Maillages → <img src="images/Mesh_Segmentation.svg" width=16px> Segmenter le maillage...** du menu.
3.  Le panneau des tâches **Segmentation du maillage** s\'ouvre.
4.  Cochez éventuellement l\'option **Lissage du maillage** et spécifiez une valeur pour le lissage du maillage. Plus la valeur est élevée, plus le maillage est supposé lisse. La spécification de {{Value|0}} a le même effet que la désactivation de cette option. Ne sélectionnez pas cette option si vous souhaitez créer des segments plans.
5.  Sélectionnez le type de surface pour lequel vous souhaitez créer des segments de maillage. Vous pouvez sélectionner plusieurs types, mais cela peut conduire à de moins bons résultats. Les types de surface disponibles sont :
    -   
        **Plan**
        

    -   
        **Cylindre**
        

    -   
        **Sphère**
        

    -   
        **Forme libre**
        
6.  Spécifiez les paramètres requis. Assurez-vous que les valeurs **Tolérance** ne sont pas trop faibles et que les valeurs **Nombre minimum de faces** ne sont pas trop élevées.
7.  Appuyez sur le bouton **OK**.
8.  La commande créera un [groupe](Std_Group/fr.md) contenant des objets maillés séparés, chacun étant un segment de l\'objet maillé d\'origine.
9.  Si le groupe créé est vide, essayez à nouveau d\'utiliser la commande avec les paramètres modifiés.



## Remarques

-   La version actuelle de la commande a du mal à identifier les faces sur les bords des types de surface.
-   Dans certains cas, la commande [Mesh Segmentation adaptée](Mesh_SegmentationBestFit/fr.md) produira de meilleurs résultats.





{{Mesh Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [Mesh](Mesh_Workbench.md) > Mesh Segmentation/fr
