---
 GuiCommand:
   Name: Assembly CreateJointRackPinion
   Name/fr: Assembly Liaison crémaillère
   MenuLocation: Assemblage , Créer une liaison crémaillère
   Workbenches: Assembly_Workbench/fr
   Shortcut: **Q**
   Version: 1.0
   SeeAlso: 
---

# Assembly CreateJointRackPinion/fr

## Description

L\'outil <img alt="" src=images/Assembly_CreateJointRackPinion.svg  style="width:24px;"> [Assembly Liaison crémaillère](Assembly_CreateJointRackPinion/fr.md) permet de créer une liaison à crémaillère qui couple la translation d\'une partie d\'une liaison glissière et la rotation d\'une partie d\'une liaison pivot.



## Utilisation

1.  Vous pouvez sélectionner deux entités géométriques de deux pièces différentes qui ont été précédemment utilisées pour définir liaison glissière et une liaison pivot.
2.  Il y a plusieurs façons de lancer l\'outil :
    -   Appuyer sur le bouton **<img src="images/Assembly_CreateJointRackPinion.svg" width=16px> [Créer une liaison crémaillère](Assembly_CreateJointRackPinion/fr.md)**.
    -   Sélectionnez l\'option **Assemblage → <img src="images/Assembly_CreateJointRackPinion.svg" width=16px> Créer une liaison crémaillère** du menu.
    -   Utilisez le raccourci clavier : **Q**.
3.  La fenêtre de dialogue **Créer une liaison** s\'ouvre dans le [panneau des tâches](Task_panel/fr.md) avec la liste des entités présélectionnées.
4.  Pour les étapes suivantes, voir [Assemblage Liaison fixe](Assembly_CreateJointFixed/fr#Utilisation.md).



## Remarques

-   Le rayon primitif fait référence au cercle primitif du pignon. Il est enregistré dans la propriété **Distance** et sert de base au calcul du rapport entre la rotation et la translation.



## Propriétés

Voir aussi : [Éditeur de propriétés](Property_editor/fr.md)

Un objet **RackPinion** est dérivé d\'un objet [App FeaturePython](App_FeaturePython/fr.md) et hérite de toutes ses propriétés. Voir [Assembly Liaison fixe](Assembly_CreateJointFixed/fr#Propriétés.md) pour des propriétés supplémentaires.





{{Assembly_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Assembly](Assembly_Workbench.md) > Assembly CreateJointRackPinion/fr
