---
 GuiCommand:
   Name: Assembly CreateJointScrew
   Name/fr: Assembly Liaison hélicoïdale
   MenuLocation: Assemblage , Créer une liaison hélicoïdale
   Workbenches: Assembly_Workbench/fr
   Shortcut: **W**
   Version: 1.0
   SeeAlso: 
---

# Assembly CreateJointScrew/fr

## Description

L\'outil <img alt="" src=images/Assembly_CreateJointScrew.svg  style="width:24px;"> [Assembly Liaison hélicoïdale](Assembly_CreateJointScrew/fr.md) permet de créer une liaison hélicoïdale qui couple la translation d\'une partie d\'une liaison glissière et la rotation d\'une partie d\'une liaison pivot. Cette liaison peut être utilisée avec les liaisons déjà existantes pour simuler un engrenage à vis sans fin.



## Utilisation

1.  Vous pouvez sélectionner deux entités géométriques de deux formes différentes qui ont été précédemment utilisées pour définir une liaison glissière et une liaison pivot.
2.  Il y a plusieurs façons de lancer l\'outil :
    -   Appuyer sur le bouton **<img src="images/Assembly_CreateJointScrew.svg" width=16px> [Créer une liaison hélicoïdale](Assembly_CreateJointScrew/fr.md)**.
    -   Sélectionnez l\'option **Assemblage → <img src="images/Assembly_CreateJointScrew.svg" width=16px> Créer une liaison hélicoïdale** du menu.
    -   Utilisez le raccourci clavier : **W**.
3.  La fenêtre de dialogue **Créer une liaison** s\'ouvre dans le [panneau des tâches](Task_panel/fr.md) avec la liste des entités présélectionnées.
4.  Pour les étapes suivantes, voir [Assemblage Liaison fixe](Assembly_CreateJointFixed/fr#Utilisation.md).



## Remarques

-   Le rayon primitif fait référence au pas d\'une vis (mère). Il est stocké dans **Distance** et définit la translation pour un tour de vis.



## Propriétés

Voir aussi : [Éditeur de propriétés](Property_editor/fr.md)

Un objet **Screw** est dérivé d\'un objet [App FeaturePython](App_FeaturePython/fr.md) et hérite de toutes ses propriétés. Voir [Assembly Liaison fixe](Assembly_CreateJointFixed/fr#Propriétés.md) pour des propriétés supplémentaires.





{{Assembly_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Assembly](Assembly_Workbench.md) > Assembly CreateJointScrew/fr
