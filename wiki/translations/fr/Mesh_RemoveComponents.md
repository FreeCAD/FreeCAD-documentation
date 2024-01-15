---
 GuiCommand:
   Name: Mesh_RemoveComponents
   Name/fr: Mesh Supprimer des composants
‎   MenuLocation: Maillages , Supprimer des composants...
   Workbenches: Mesh_Workbench/fr
   SeeAlso: Mesh_RemoveCompByHand/fr, Arch_SplitMesh/fr
---

# Mesh RemoveComponents/fr

## Description

La commande **Supprimer des composants** supprime des composants d\'objets maillés.

<img alt="" src=images/Meshes_RemoveComponents.jpg  style="width:300px;"> 
*Le panneau de tâches Supprimer des composants*



## Utilisation

1.  La commande utilise la couleur rouge pour marquer les faces sélectionnées. Pour les voir correctement :
    -   
        **Display Mode**
        
        des objets maillés devrait idéalement être {{Value|Flat lines}}, mais devrait au moins montrer des faces. Si nécessaire, utilisez la commande [Std Style de représentation](Std_DrawStyle/fr.md) pour remplacer cette propriété.

    -   
        **Shape Color**
        
        des objets maillés ne doit pas être rouge.
2.  Il existe plusieurs façons de lancer la commande :
    -   Appuyez sur le bouton **<img src="images/Mesh_RemoveComponents.svg" width=16px> [Supprimer des composants...](Mesh_RemoveComponents/fr.md)
**
    -   Sélectionnez l\'option **Maillages → <img src="images/_Mesh_RemoveComponents.svg" width=16px> Supprimer des composants...** du menu.
3.  Le panneau des tâches **Supprimer des composants** s\'ouvre.
4.  Utilisez une ou plusieurs des options **Sélectionner** pour sélectionner des faces :
    -   Appuyez sur le bouton **Région** et tout en maintenant le bouton gauche de la souris, dessinez une région, une spline fermée, dans la [vue 3D](3D_view/fr.md). Les faces qui correspondent aux **Options de la région** et tombent (partiellement) à l\'intérieur de la région seront sélectionnées.
    -   Appuyez sur le bouton **Tous** pour sélectionner tous les faces.
    -   Appuyez sur le bouton **Composants** pour sélectionner tous les composants avec moins que le nombre maximum de faces spécifié. Ici, un composant fait référence à un groupe complet de faces connectées. Un objet maillé contient généralement un seul composant. Mais, par exemple après avoir utilisé la commande [Mesh Fusionner](Mesh_Merge/fr.md), un objet maillé peut contenir plusieurs composants.
    -   Appuyez sur le bouton **Choisir un triangle** pour sélectionner une seule face dans la vue 3D. Si l\'option **Sélectionner le composant en entier** est cochée, la sélection d\'une face entraînera la sélection du composant entier auquel appartient la face.
5.  Utilisez éventuellement une ou plusieurs des options **Désélectionner** pour désélectionner les faces. Ces options sont identiques aux options **Sélectionner**, sauf que le nombre de faces pour le bouton **Composants** est un nombre minimum.
6.  Vous pouvez appuyer sur le bouton **Inverser** pour inverser la sélection.
7.  Appuyez sur le bouton **Supprimer** pour supprimer les faces sélectionnées.
8.  Appuyez sur le bouton **Fermer** pour fermer le panneau des tâches et terminer la commande.





{{Mesh Tools navi

}}



---
⏵ [documentation index](../README.md) > [Mesh](Mesh_Workbench.md) > Mesh RemoveComponents/fr
