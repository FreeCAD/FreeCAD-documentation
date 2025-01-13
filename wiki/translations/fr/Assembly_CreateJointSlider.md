---
 GuiCommand:
   Name: Assembly CreateJointSlider
   Name/fr: Assembly Liaison glissière
   MenuLocation: Assemblage , Créer une liaison glissière
   Workbenches: Assembly_Workbench/fr
   Shortcut: **S**
   Version: 1.0
   SeeAlso: 
---

# Assembly CreateJointSlider/fr

## Description

L\'outil <img alt="" src=images/Assembly_CreateJointSlider.svg  style="width:24px;"> [Assembly Liaison glissière](Assembly_CreateJointSlider/fr.md) crée une liaison glissière (également appelée liaison prismatique) entre deux pièces sélectionnées, permettant un mouvement linéaire le long d\'un seul axe tout en limitant la rotation.



## Utilisation

1.  Vous pouvez sélectionner deux entités géométriques de deux formes différentes. Les autres sélections seront rejetées.
2.  Il y a plusieurs façons de lancer l\'outil :
    -   Appuyez sur le **<img src="images/Assembly_CreateJointSlider.svg" width=16px> [Créer une liaison glissière](Assembly_CreateJointSlider/fr.md)**.
    -   Sélectionnez l\'option **Assemblage → <img src="images/Assembly_CreateJointSlider.svg" width=16px> Créer une liaison glissière** du menu.
    -   Utilisez le raccourci clavier : **S**.
3.  La fenêtre de dialogue **Créer une liaison** s\'ouvre dans le [panneau des tâches](Task_panel/fr.md) avec la liste des entités présélectionnées.
4.  Pour les étapes suivantes, voir [Assemblage Liaison fixe](Assembly_CreateJointFixed/fr#Utilisation.md).



## Propriétés

Voir aussi : [Éditeur de propriétés](Property_editor/fr.md)

Un objet **Slider** est dérivé d\'un objet [App FeaturePython](App_FeaturePython/fr.md) et hérite de toutes ses propriétés. Voir [Assembly Liaison fixe](Assembly_CreateJointFixed/fr#Propriétés.md) pour des propriétés supplémentaires.





{{Assembly_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Assembly](Assembly_Workbench.md) > Assembly CreateJointSlider/fr
