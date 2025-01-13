---
 GuiCommand:
   Name: Assembly CreateJointBelt
   Name/fr: Assembly Liaison courroie
   MenuLocation: Assemblage , Créer une liaison engrenage/courroie , Créer une liaison courroie
   Workbenches: Assembly_Workbench/fr
   Shortcut: 
   Version: 1.0
   SeeAlso: 
---

# Assembly CreateJointBelt/fr

## Description

L\'outil <img alt="" src=images/Assembly_CreateJointBelt.svg  style="width:24px;"> [Assembly Liaison courroie](Assembly_CreateJointBelt/fr.md) permet de créer une liaison courroie qui couple la rotation de deux parties de deux liaisons tournantes distinctes. Cette liaison peut être utilisée avec des liaisons déjà existantes pour simuler des courroies de transmission, des engrenages de synchronisation, etc.



## Utilisation

1.  Vous pouvez sélectionner deux entités géométriques de deux pièces différentes qui ont été précédemment utilisées pour définir deux articulations en croix.
2.  Il y a plusieurs façons de lancer l\'outil :
    -   Appuyer sur le bouton **<img src="images/Assembly_CreateJointBelt.svg" width=16px> [Créer une liaison courroie](Assembly_CreateJointBelt/fr.md)**.
    -   Sélectionnez l\'option **Assemblage → Créer une liaison engrenage/courroie → <img src="images/Assembly_CreateJointBelt.svg" width=16px> Créer une liaison courroie** dans le menu.
3.  La fenêtre de dialogue **Créer une liaison** s\'ouvre dans le [panneau des tâches](Task_panel/fr.md) avec la liste des entités présélectionnées.
4.  Pour les étapes suivantes, voir [Assemblage Liaison fixe](Assembly_CreateJointFixed/fr#Utilisation.md).



## Remarques

-   Radius1 et Radius2 font référence au cercle primitif des engrenages de synchronisation ou au diamètre extérieur des poulies. Ils ont leurs valeurs dans les propriétés **Distance** et **Distance2** et définissent le rapport entre les deux rotations.
-   Utilisez la même valeur pour les deux rayons afin de relier les deux extrémités d\'un arbre flexible (si les rotations ne correspondent pas, inversez une [liaison pivot](Assembly_CreateJointRevolute/fr.md) ou utilisez la [liaison engrenage](Assembly_CreateJointGears/fr.md) à la place de celle-ci).



## Propriétés

Voir aussi : [Éditeur de propriétés](Property_editor/fr.md)

Un objet **Belt** est dérivé d\'un objet [App FeaturePython](App_FeaturePython/fr.md) et hérite de toutes ses propriétés. Voir [Assembly Liaison fixe](Assembly_CreateJointFixed/fr#Propriétés.md) pour des propriétés supplémentaires.





{{Assembly_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Assembly](Assembly_Workbench.md) > Assembly CreateJointBelt/fr
