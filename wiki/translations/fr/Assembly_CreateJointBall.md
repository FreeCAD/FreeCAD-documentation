---
 GuiCommand:
   Name: Assembly CreateJointBall
   Name/fr: Assembly Liaison bille
   MenuLocation: Assemblage , Créer une liaison bille
   Workbenches: Assembly_Workbench/fr
   Shortcut: **B**
   Version: 1.0
   SeeAlso: 
---

# Assembly CreateJointBall/fr

## Description

L\'outil <img alt="" src=images/Assembly_CreateJointBall.svg  style="width:24px;"> [Assembly Liaison bille](Assembly_CreateJointBall/fr.md) crée une liaison bille (liaison sphérique) entre deux pièces sélectionnées en un seul point, permettant une rotation libre autour du point tout en gardant les deux pièces connectées en ce point.



## Utilisation

1.  Vous pouvez sélectionner deux entités géométriques de deux formes différentes. Les autres sélections seront rejetées.
2.  Il y a plusieurs façons de lancer l\'outil :
    -   Appuyez sur le bouton **<img src="images/Assembly_CreateJointBall.svg" width=16px> [Créer une liaison bille](Assembly_CreateJointBall/fr.md)**.
    -   Sélectionnez l\'option **Assemblage → <img src="images/Assembly_CreateJointBall.svg" width=16px> Créer une liaison bille** du menu.
    -   Utilisez le raccourci clavier : **B**.
3.  La fenêtre de dialogue **Créer une liaison** s\'ouvre dans le [panneau des tâches](Task_panel/fr.md) avec la liste des entités présélectionnées.
4.  Pour les étapes suivantes, voir [Assemblage Liaison fixe](Assembly_CreateJointFixed/fr#Utilisation.md).



## Propriétés

Voir aussi : [Éditeur de propriétés](Property_editor/fr.md)

Un objet **Ball** est dérivé d\'un objet [App FeaturePython](App_FeaturePython/fr.md) et hérite de toutes ses propriétés. Voir [Assembly Liaison fixe](Assembly_CreateJointFixed/fr#Propriétés.md) pour des propriétés supplémentaires.





{{Assembly_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Assembly](Assembly_Workbench.md) > Assembly CreateJointBall/fr
