---
- TutorialInfo:/fr
   Topic:Exemple de semelle combinée
   Level:Intermédiaire
   Author:Shiv Charan
   FCVersion:0.20
---

# Example Combined Footing/fr





## Description

L\'outil [Renforts de semelle](Arch_Rebar_Footing_Reinforcement/fr.md) permet à l\'utilisateur de créer des barres de renforcement à l\'intérieur d\'un objet semelle [Arch Structure](Arch_Structure/fr.md).

Cette commande fait partie de l\'[atelier Reinforcement](Reinforcement_Workbench/fr.md), un [atelier externe](External_workbenches/fr.md) que vous pouvez installer avec le <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Gestionnaire des extensions](Std_AddonMgr/fr.md) via le menu **Outils → Gestionnaire des extensions → Reinforcement**.

Dans cet exemple, nous allons créer un ferraillage combiné d\'une semelle comme le montre la figure ci-dessous.

![](images/Combined_Footing_reinforcement.png ) 
*Un exemple de ferraillage combiné d'une semelle [Arch Structure](Arch_Structure/fr.md).*

![](images/Side_view_of_combined_footing_of_footing_reinforcement.png ) 
*Vue de droite de l'exemple du ferraillage de semelle donné*

![](images/Combined_footing_front_view_.png ) 
*Vue de face de l'exemple du ferraillage de semelle donné*

## Utilisation

1\. Sélectionnez la face verticale d\'une semelle **<img src="images/Arch_Structure.svg" width=16px> [Arch Structure](Arch_Structure/fr.md)** précédemment créée comme le montre l\'image ci-dessous.

![](images/FootingSelectedFace.png ) 
*Face sélectionnée de la semelle Arch Structure*

2\. Sélectionnez ensuite **[Footng Reinforcement](Arch_Rebar_Footing_Reinforcement/fr.md)** dans les outils d\'armature.

3\. Une boîte de dialogue de renfort de semelle apparaît à l\'écran, comme illustré ci-dessous.

![](images/Footing_Reinforcement_GUI_.png ) 
*Boîte de dialogue pour l'armature de la semelle*

4\. Sélectionnez le type de barre souhaité et les autres données d\'entrée pour les barres dans la direction parallèle à la face sélectionnée dans le maillage de renfort de la semelle comme le montre l\'image ci-dessous.

5\. Maintenant, cliquez sur le bouton Next ou sélectionnez Cross Rebars dans la vue en liste et les données souhaitées pour les données d\'entrée pour les barres dans la direction transversale de la face sélectionnée dans le maillage de renforcement de la semelle comme le montre l\'image ci-dessous.

6\. Cliquez sur suivant ou cliquez sur Columns dans la vue en liste et remplissez l\'entrée souhaitée pour les colonnes dans le renfort de la semelle. Ici, vous pouvez choisir d\'ajouter ou non des armatures secondaires dans les colonnes.

7\. Cliquez sur suivant ou cliquez sur Ties dans la vue en liste et remplissez les données souhaitées pour Ties dans les colonnes de renfort de la semelle.

8\. Cliquez sur suivant ou cliquez sur Main rebars dans la vue en liste et remplissez les données souhaitées pour les armatures principales dans les colonnes de renfort de la semelle.

Seulement si le contrôle des armatures secondaires est activé :

9\. Cliquez sur suivant ou cliquez sur XDir Secondary rebar dans la vue en liste et remplissez l\'entrée souhaitée pour les armatures secondaires dans la direction X dans une colonne dans le renfort de la semelle.

10\. Cliquez sur suivant ou cliquez sur YDir Secondary rebar dans la vue en liste et remplissez l\'entrée souhaitée pour les armatures secondaires dans la direction Y dans une colonne dans le renfort de la semelle.

11\. Cliquez sur **OK** ou **Apply** ou **Finish** pour générer le ferraillage des dalles.

12\. Cliquez sur **Cancel** pour quitter la boîte de dialogue.



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Reinforcement](Category_Reinforcement.md) > [Arch](Category_Arch.md) > Example Combined Footing/fr
