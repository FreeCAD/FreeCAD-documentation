---
 GuiCommand:
   Name: Assembly CreateJointDistance
   Name/fr: Assembly Liaison distance
   MenuLocation: Assemblage , Créer une liaison distance
   Workbenches: Assembly_Workbench/fr
   Shortcut: **D**
   Version: 1.0
   SeeAlso: 
---

# Assembly CreateJointDistance/fr

## Description

L\'outil <img alt="" src=images/Assembly_CreateJointDistance.svg  style="width:24px;"> [Assembly Liaison distance](Assembly_CreateJointDistance/fr.md) crée une liaison distance entre deux pièces sélectionnées, fixant la distance entre les deux pièces.



## Utilisation

1.  Vous pouvez sélectionner deux entités géométriques de deux formes différentes. Les autres sélections seront rejetées.
2.  Il y a plusieurs façons de lancer l\'outil :
    -   Appuyez sur le bouton **<img src="images/Assembly_CreateJointDistance.svg" width=16px> [Créer une liaison distance](Assembly_CreateJointDistance/fr.md)**.
    -   Sélectionnez l\'option **Assemblage → <img src="images/Assembly_CreateJointDistance.svg" width=16px> Créer une liaison distance** du menu.
    -   Utilisez le raccourci clavier : **D**.
3.  La fenêtre de dialogue **Créer une liaison** s\'ouvre dans le [panneau des tâches](Task_panel/fr.md) avec la liste des entités présélectionnées.
4.  Pour les étapes suivantes, voir [Assemblage Liaison fixe](Assembly_CreateJointFixed/fr#Utilisation.md).



## Remarques

L\'infobulle indique qu\'une distance de 0 entraîne une liaison coplanaire entre les éléments planaires sélectionnés, ou une liaison tangente entre un élément cylindrique et un élément planaire. Aucune de ces options ne semble fonctionner dans la version hebdomadaire 0.22.-.37645.



## Propriétés

Voir aussi : [Éditeur de propriétés](Property_editor/fr.md)

Un objet **Distance** est dérivé d\'un objet [App FeaturePython](App_FeaturePython/fr.md) et hérite de toutes ses propriétés. Voir [Assembly Liaison fixe](Assembly_CreateJointFixed/fr#Propriétés.md) pour des propriétés supplémentaires.





{{Assembly_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Assembly](Assembly_Workbench.md) > Assembly CreateJointDistance/fr
