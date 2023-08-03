---
 GuiCommand:
   Name: Mesh FillInteractiveHole
   Name/fr: Mesh Boucher un trou
   MenuLocation: Maillages , Boucher un trou
   Workbenches: Mesh_Workbench/fr
   SeeAlso: Mesh_FillupHoles/fr, Mesh_AddFacet/fr
---

# Mesh FillInteractiveHole/fr

## Description

La commande **Boucher un trou** remplit les trous sélectionnés dans les objets maillés.



## Utilisation

1.  Il existe plusieurs façons de lancer la commande :
    -   Appuyez sur le bouton **<img src="images/Mesh_FillInteractiveHole.svg" width=16px> [Boucher un trou](Mesh_FillInteractiveHole/fr.md)
**
    -   Sélectionnez l\'option **Maillages → <img src="images/Mesh_FillInteractiveHole.svg" width=16px> Boucher un trou** du menu.
2.  Le curseur se transforme en icône triangulaire.
3.  Sélectionnez une face qui partage une arête avec le trou que vous souhaitez fermer.
4.  Le trou est fermé.
5.  Répétez éventuellement cette opération pour fermer des trous supplémentaires.
6.  Si nécessaire, vous pouvez utiliser [Std Annuler](Std_Undo/fr.md) pour annuler la dernière action de la commande.
7.  Sélectionnez l\'option **Quitter le mode de remplissage des trous** du menu contextuel de la [vue 3D](3D_view/fr.md) pour terminer la commande.



## Remarques

-   Si les arêtes d\'un trou ne se trouvent pas dans le même plan, le résultat de la commande peut dépendre de la face sélectionnée.





{{Mesh Tools navi

}}



---
⏵ [documentation index](../README.md) > [Mesh](Mesh_Workbench.md) > Mesh FillInteractiveHole/fr
