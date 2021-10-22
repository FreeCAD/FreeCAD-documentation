---
- GuiCommand:/fr
   Name:Mesh_RemoveComponents
   Name/fr:Mesh Supprimer des composants
‎   MenuLocation:Maillages → Supprimer des composants...
   Workbenches:[Mesh](Mesh_Workbench/fr.md)
   SeeAlso:[Mesh Suppression manuelle de composants](Mesh_RemoveCompByHand/fr.md), [Arch Séparer un objet Mesh](Arch_SplitMesh/fr.md)
---

# Mesh RemoveComponents/fr

## Description

La commande **Mesh Supprimer des composants** supprime des composants d\'objets maillés.

![](images/Meshes_RemoveComponents.jpg ) 
*Le panneau de tâches Supprimer des composants*

## Utilisation

1.  La commande utilise la couleur rouge pour marquer les faces sélectionnées. Pour les voir correctement:
    -   Le {{PropertyView/fr|Display Mode}} des objets maillés devrait idéalement être {{Value|Flat lines}}, mais devrait au moins montrer des faces. Si nécessaire, utilisez la commande [Std Style de représentation](Std_DrawStyle/fr.md) pour remplacer cette propriété.
    -   La {{PropertyView/fr|Shape Color}} des objets maillés ne doit pas être rouge.
2.  Il existe plusieurs façons d\'appeler la commande:
    -   Appuyez sur le bouton **<img src="images/Mesh_RemoveComponents.svg" width=16px> [Supprimer les composants de topologie indépendants du maillage](Mesh_RemoveComponents/fr.md)
**
    -   Sélectionnez l\'option **Maillages → <img src="images/_Mesh_RemoveComponents.svg" width=16px> Supprimer des composants...** dans le menu.
3.  Le panneau des tâches **Remove components** s\'ouvre.
4.  Utilisez une ou plusieurs des options **Select** pour sélectionner des visages:
    -   Appuyez sur le bouton **Region** et tout en maintenant le bouton gauche de la souris, dessinez une région, une spline fermée, dans la [vue 3D](3D_view/fr.md). Les faces qui correspondent aux **Options de la région** et tombent (partiellement) à l\'intérieur de la région seront sélectionnées.
    -   Appuyez sur le bouton **All** pour sélectionner tous les visages.
    -   Appuyez sur le bouton **Components** pour sélectionner tous les composants avec moins que le nombre maximum de faces spécifié. Ici, un composant fait référence à un groupe complet de faces connectées. Un objet maillé contient généralement un seul composant. Mais, par exemple après avoir utilisé la commande [Mesh Fusionner](Mesh_Merge/fr.md), un objet maillé peut contenir plusieurs composants.
    -   Appuyez sur le bouton **Pick triangle** pour sélectionner une seule face dans la vue 3D. Si l\'option **Sélectionner tout le composant** est cochée, la sélection d\'une face entraînera la sélection du composant entier auquel appartient la face.
5.  Utilisez éventuellement une ou plusieurs des options **Deselect** pour désélectionner les visages. Ces options sont identiques aux options **Select**, sauf que le nombre de faces pour le bouton **Components** est un nombre minimum.
6.  Appuyez éventuellement sur le bouton **Invert** pour inverser la sélection.
7.  Appuyez sur le bouton **Delete** pour supprimer les visages sélectionnés.
8.  Appuyez sur le bouton **Close** pour fermer le panneau des tâches et terminer la commande.





{{Mesh Tools navi

}}

---
[documentation index](../README.md) > [Mesh](Mesh_Workbench.md) > Mesh RemoveComponents/fr
