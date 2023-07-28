---
- GuiCommand:/fr
   Name:Sketcher ToggleConstruction
   Name/fr:Sketcher Géométrie de construction
   MenuLocation:Esquisse → Géométries d'esquisse → Basculer le mode de la géométrie de construction
   Workbenches:[Sketcher](Sketcher_Workbench/fr.md)
   Shortcut:**G** **N**
   SeeAlso:[Sketcher Contraintes pilotantes](Sketcher_ToggleDrivingConstraint/fr.md)
---

# Sketcher ToggleConstruction/fr

## Description

Cet outil permet de basculer les géométries sélectionnées de/vers le mode de construction. Cela concerne toutes les géométries.

La géométrie de construction est un outil important de Sketcher. Lorsque vous utilisez une esquisse pour une opération 3D, la géométrie de construction est ignorée.

En **[<img src=images/Sketcher_EditSketch.svg style="width:16px"> [mode d'édition d'esquisse](Sketcher_EditSketch/fr.md)**, la géométrie de construction est affichée en bleu, et ne deviendra pas verte lorsqu\'une esquisse est entièrement contrainte. Une fois que vous **[<img src=images/Sketcher_LeaveSketch.svg style="width:16px"> [quittez le mode d'édition d'esquisse](Sketcher_LeaveSketch/fr.md)**, la géométrie de construction est masquée dans la [vue 3D](3D_view/fr.md).

Les lignes de construction peuvent être utilisées comme axe de rotation par la fonction **[<img src=images/PartDesign_Revolution.svg style="width:16px"> [PartDesign Révolution](PartDesign_Revolution/fr.md)**.

<img alt="" src=images/Sketcher_ConstructionMode_fr_01.png  style="width:480px;">



## Utilisation

Il y a deux façons d\'utiliser cet outil :

1.  Sans que rien ne soit sélectionné dans la [vue 3D](3D_view/fr.md) :
    -   Activez le mode construction en cliquant sur le bouton **[<img src=images/Sketcher_ToggleConstruction.svg style="width:16px"> [Basculer le mode de la géométrie de construction](Sketcher_ToggleConstruction/fr.md)** ou en utilisant l\'entrée **Esquisse → Géométries d'esquisse → [<img src=images/Sketcher_ToggleConstruction.svg style="width:16px"> Basculer le mode de la géométrie de construction** du menu Esquisse.
    -   Cela changera la couleur pour la création de nouveaux éléments géométriques en bleu.
    -   Les éléments géométriques nouvellement créés seront désormais créés en mode construction.
2.  Avec un ou plusieurs éléments géométriques sélectionnés dans la [vue 3D](3D_view/fr.md).
    -   Activez l\'outil en cliquant sur le bouton **[<img src=images/Sketcher_ToggleConstruction.svg style="width:16px"> [Basculer le mode de la géométrie de construction](Sketcher_ToggleConstruction/fr.md)** ou en le sélectionnant dans le menu.
    -   Les éléments sélectionnés passent alors en mode construction.
    -   Ensuite, les éléments nouvellement créés seront à nouveau des géométries normales.



## Remarques

-    **[<img src=images/Sketcher_CreatePoint.svg style="width:16px"> [Sketcher Point](Sketcher_CreatePoint/fr.md)**créera toujours des points en mode construction, quel que soit l\'état du basculement de la barre d\'outils. Sélectionnez les points souhaités dans la [vue 3D](3D_view/fr.md) après la création et cliquez sur **[<img src=images/Sketcher_ToggleConstruction.svg style="width:16px"> [Basculer le mode de la géométrie de construction](Sketcher_ToggleConstruction/fr.md)** pour les transformer en géométrie normale.





{{Sketcher_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ToggleConstruction/fr
