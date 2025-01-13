---
 GuiCommand:
   Name: Assembly CreateJointGears
   Name/fr: Assembly Liaison courroie
   MenuLocation: Assemblage , Créer une liaison engrenage/courroie , Créer une liaison engrenage
   Workbenches: Assembly_Workbench/fr
   Shortcut: 
   Version: 1.0
   SeeAlso: 
---

# Assembly CreateJointGears/fr

## Description

L\'outil <img alt="" src=images/Assembly_CreateJointGears.svg  style="width:24px;"> [Assembly Liaison engrenage](Assembly_CreateJointGears/fr.md) permet de créer une liaison engrenage qui couple la rotation de deux parties de deux liaisons pivot différentes. Cette liaison peut être utilisée avec des liaisons déjà existantes pour simuler des engrenages droits, des engrenages coniques, des couronnes, des roues de friction, etc.



## Utilisation

1.  Vous pouvez sélectionner deux entités géométriques de deux pièces différentes qui ont été précédemment utilisées pour définir deux articulations en croix.
2.  Il y a plusieurs façons de lancer l\'outil :
    -   Appuyer sur le bouton **<img src="images/Assembly_CreateJointGears.svg" width=16px> [Créer une liaison engrenage](Assembly_CreateJointGears/fr.md)**.
    -   Sélectionnez l\'option **Assemblage → Créer une liaison engrenage/courroie → <img src="images/Assembly_CreateJointGears.svg" width=16px> Créer une liaison engrenage** du menu.
3.  La fenêtre de dialogue **Créer une liaison** s\'ouvre dans le [panneau des tâches](Task_panel/fr.md) avec la liste des entités présélectionnées.
4.  Pour les étapes suivantes, voir [Assemblage Liaison fixe](Assembly_CreateJointFixed/fr#Utilisation.md).



## Remarques

-   Radius1 et Radius2 font référence au cercle primitif des engrenages ou au diamètre extérieur des roues de friction. Ils ont leurs valeurs dans les propriétés **Distance** et **Distance2** et définissent le rapport entre les deux rotations.
-   Puisque les valeurs des deux rayons n\'ont pas d\'influence sur la distance entre les axes de rotation et que les unités sont de toute façon annulées, vous pouvez envisager d\'entrer des valeurs de diamètre, ou le nombre de dents (il n\'est donc pas nécessaire de trouver le diamètre primitif des engrenages coniques) pour les deux rayons.
-   Utilisez la même valeur pour les deux rayons pour relier les deux extrémités d\'un arbre flexible (si les rotations ne correspondent pas, inversez une articulation à révolutions ou utilisez l\'articulation à courroie à la place de celle-ci).



## Propriétés

Voir aussi : [Éditeur de propriétés](Property_editor/fr.md)

Un objet **Gears** est dérivé d\'un objet [App FeaturePython](App_FeaturePython/fr.md) et hérite de toutes ses propriétés. Voir [Assembly Liaison fixe](Assembly_CreateJointFixed/fr#Propriétés.md) pour des propriétés supplémentaires.





{{Assembly_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Assembly](Assembly_Workbench.md) > Assembly CreateJointGears/fr
