---
- GuiCommand:
   Name: Mesh RemoveCompByHand
   Name/fr: Mesh Suppression manuelle de composants
   MenuLocation: Maillages -> Supprimer manuellement des composants...
   Workbenches: Mesh Workbench/fr
   SeeAlso: Mesh_RemoveComponents/fr, Arch_SplitMesh/fr
---

# Mesh RemoveCompByHand/fr

## Description

La commande **Suppression manuelle de composants** supprime des composants d\'objets maillés.



## Utilisation

1.  Un composant fait référence à un groupe complet de faces connectées. Un objet maillé contient généralement un seul composant. Mais, par exemple après avoir utilisé la commande [Mesh Fusionner](Mesh_Merge/fr.md), un objet maillé peut contenir plusieurs composants.
2.  La commande utilise la couleur rouge pour marquer les composants sélectionnés. Pour les voir correctement :
    -   Le **Display Mode** des objets maillés doit montrer des faces. Si nécessaire, utilisez la commande [Std Style de représentation](Std_DrawStyle/fr.md) pour remplacer cette propriété.
    -   La **Shape Color** des objets maillés ne doit pas être rouge.
3.  Sélectionnez l\'option **Maillages → <img src="images/Mesh_RemoveCompByHand.svg" width=16px> Supprimer manuellement des composants... ** du menu.
4.  Le curseur se transforme en icône de main.
5.  Sélectionnez les composants que vous souhaitez supprimer dans la [vue 3D](3D_view/fr.md).
6.  Vous pouvez sélectionner **Effacer les faces sélectionnées** du menu contextuel de la vue 3D pour désélectionner tous les composants.
7.  Sélectionnez **Supprimer les faces sélectionnées** du menu contextuel de la vue 3D pour supprimer les composants sélectionnés.
8.  Sélectionnez **Quitter le mode de suppression** du menu contextuel de la vue 3D pour terminer la commande.





{{Mesh Tools navi

}}



---
⏵ [documentation index](../README.md) > [Mesh](Mesh_Workbench.md) > Mesh RemoveCompByHand/fr
