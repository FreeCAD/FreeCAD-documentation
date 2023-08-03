---
 GuiCommand:
   Name: Mesh SegmentationBestFit
   Name/fr: Mesh Segmentation adaptée
   MenuLocation: Maillages , Créer des segments de maillage de surfaces ajustées...
   Workbenches: Mesh_Workbench/fr
   SeeAlso: Mesh_Segmentation/fr
---

# Mesh SegmentationBestFit/fr

## Description

La commande **Segmentation adaptée** crée des segments de maillage séparés pour les types de surface spécifiés d\'un objet maillé. La commande peut également identifier leurs paramètres, lesquels peuvent être utiles lors de la reconfiguration d\'un objet maillé.



## Utilisation

1.  Si vous envisagez d\'identifier les paramètres d\'un type de surface, notez que la commande utilise la couleur rouge pour marquer les faces sélectionnées pour cette option. Pour les voir correctement :
    -   La **Display Mode** de l\'objet maillé devrait idéalement être {{Value|Flat lines}}, mais devrait au moins montrer des faces. Si nécessaire, utilisez la commande [Std Style de représentation](Std_DrawStyle/fr.md) pour remplacer cette propriété.
    -   La **Shape Color** de l\'objet maillé ne doit pas être rouge.
2.  Sélectionnez un seul objet maillé.
3.  Il existe plusieurs façons de lancer la commande :
    -   Appuyez sur le bouton **<img src="images/Mesh_SegmentationBestFit.svg" width=16px> [Segmenter le maillage par des surfaces adaptées...](Mesh_SegmentationBestFit/fr.md)**.
    -   Sélectionnez l\'option **Maillages → <img src="images/Mesh_SegmentationBestFit.svg" width=16px> Segmenter le maillage par des surfaces adaptées...** du menu.
4.  Le panneau des tâches **Segmentation du maillage** s\'ouvre.
5.  Appuyez sur l\'un des boutons **Paramètres...** pour identifier les paramètres d\'une surface :
    -   La boîte de dialogue **Ajustement de la surface** s\'ouvre.
    -   Sélectionnez une ou plusieurs faces appartenant à la surface :
        -   Appuyez sur le bouton **Région** et tout en maintenant le bouton gauche de la souris, dessinez une région, une spline fermée, dans la [vue 3D](3D_view/fr.md). Les faces qui tombent (partiellement) à l\'intérieur de la région seront sélectionnées.
        -   Appuyez sur le bouton **Triangle** pour sélectionner des faces une par une.
        -   Appuyez sur le bouton **Effacer** pour effacer la sélection.
    -   Appuyez sur le bouton **Calculer** pour calculer les paramètres.
    -   Appuyez sur le bouton **OK** ou **Annuler** pour fermer la boîte de dialogue.
6.  Sélectionnez le ou les types de surface pour lesquels vous souhaitez créer des segments de maillage :
    -   
        **Plan**
        

    -   
        **Cylindre**
        

    -   
        **Sphère**
        
7.  Spécifiez les valeurs de **Tolérance**.
8.  Spécifiez les valeurs **Nombre minimum de faces**.
9.  Appuyez sur le bouton **OK**.
10. La commande créera un [groupe](Std_Group/fr.md) contenant des objets maillés séparés, chacun étant un segment de l\'objet maillé d\'origine.
11. Si le groupe créé est vide, essayez à nouveau d\'utiliser la commande avec les paramètres modifiés.





{{Mesh Tools navi

}}



---
⏵ [documentation index](../README.md) > [Mesh](Mesh_Workbench.md) > Mesh SegmentationBestFit/fr
