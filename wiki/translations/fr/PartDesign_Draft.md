---
- GuiCommand:
   Name:PartDesign_Draft
   Name/fr:PartDesign Dépouille
   MenuLocation:Part Design → Appliquer une fonction d'habillage → Dépouille
   Workbenches:[PartDesign](PartDesign_Workbench/fr.md)
---

# PartDesign Draft/fr

## Description

L\'outil <img alt="" src=images/PartDesign_Draft.svg  style="width:24px;"> **PartDesign Dépouille** crée des dépouilles angulaires sur les faces sélectionnées d\'un objet. Il ajoute un objet **Draft** au document avec sa représentation correspondante dans la [Vue en arborescence](Tree_view/fr.md).

   --
  ![Sélectionnez une ou plusieurs faces de l\'objet avant de lancer l\'outil. Ici, 2 faces ont été sélectionnées.](images/PartDesign_Draft-01.png ) ![Montre les paramètres de dépouille dans le panneau de tâches.](images/PartDesign_Draft-02.png ) ![2 faces ont été ajoutées, et une dépouille de 10 degrés a été appliquée. Le plan inférieur est resté identique, tandis que la dépouille a réduit le plan supérieur](images/PartDesign_Draft-03.png ) ![Le plan neutre a été déplacé vers le haut. Maintenant, le plan supérieur est resté identique, tandis que la dépouille a agrandi le plan inférieur.](images/PartDesign_Draft-04.png ) ![La direction de la dépouille est réglée sur le bord inférieur droit, ce qui fait que la dépouille est tirée vers la gauche.](images/PartDesign_Draft-05.png ) ![Cocher la case Inverser la direction a permis d\'appliquer une dépouille vers l\'intérieur plutôt que vers l\'extérieur.](images/PartDesign_Draft-06.png )   
   --




## Utilisation

### Ajouter une dépouille 

1.  Vous pouvez accessoirement [activé](PartDesign_Body/fr#Statut_actif.md) le corps auquel appliquer la dépouille.
2.  Sélectionnez une ou plusieurs faces du corps.
3.  Il existe plusieurs façons de lancer l\'outil :
    -   Appuyez sur le bouton **<img src="images/PartDesign_Draft.svg" width=16px> [Dépouille](PartDesign_Draft/fr.md)**.
    -   Sélectionnez l\'option **Part Design → Appliquer une fonction d'habillage → <img src="images/PartDesign_Draft.svg" width=16px> Dépouille** dans le menu.
4.  S\'il n\'y a pas de corps actif, et qu\'il y a deux corps ou plus dans le document, le dialogue **Corps actif requis** s\'ouvrira et vous invitera à en activer un. S\'il n\'y a qu\'un seul corps, il sera activé automatiquement.
5.  Le [Panneau des tâches](Task_panel/fr.md) des **Paramètres de la dépouille**. Voir [Options](#Options.md) pour plus d\'informations.
6.  Appuyez sur le bouton **OK** pour terminer.

:   *Souvenez-vous* :
    -   Puisqu\'il doit y avoir au moins une face pour la fonction, la dernière face restant dans la liste ne peut pas être retirée.

### Modifier une dépouille 

1.  Faites l\'une des choses suivantes :
    -   Double-cliquez sur l\'objet Draft dans la [Vue en arborescence](Tree_view/fr.md).
    -   Cliquez avec le bouton droit de la souris sur l\'objet Draft dans la [Vue en arborescence](Tree_view/fr.md) et sélectionnez **Modifier Dépouille** dans le menu contextuel.
2.  Le [Panneau des tâches](Task_panel/fr.md) des **Paramètres de la dépouille** s\'ouvre. Voir [Options](#Options.md) pour plus d\'informations.
3.  Appuyez sur le bouton **OK** pour terminer.

## Options

-    **Ajouter une face**: Ajoutez des faces à la sélection en appuyant sur le bouton **Ajouter une face** et en sélectionnant d\'autres faces.

-    **Supprimer une face**: Choisissez un moyen de supprimer des faces de la sélection :

    -   Sélectionnez une ou plusieurs faces dans la liste et appuyez sur la touche **Suppr** ou cliquez avec le bouton droit de la souris sur la liste et sélectionnez **Enlever** dans le menu contextuel.
    -   Appuyez sur le bouton **Supprimer une face**. Toutes les faces précédemment sélectionnées sont surlignées en violet. Sélectionnez chaque visage à supprimer.

-    **Angle de dépouille**: Définissez l\'angle de dépouille en entrant une valeur ou en cliquant sur les flèches haut/bas.

-    **Plan neutre**: Définissez le plan neutre en appuyant sur le bouton **Plan neutre** et en sélectionnant le plan qui doit rester identique.

-    **Direction**: Définissez la direction de la dépouille en appuyant sur le bouton **Direction**, puis sélectionnez une arête. La direction de la dépouille n\'est effective que si le plan neutre a été défini. Les résultats peuvent être imprévisibles.

-    **Inverser la direction de la dépouille**: Inversez la direction de la dépouille en cochant la case **Inverser la direction de la dépouille**. Cela fera basculer la dépouille entre des angles positifs et négatifs.

## Remarques

-   L\'outil Dépouille ne fonctionne que sur les faces qui ne sont pas connectées tangentiellement à d\'autres faces. Une erreur courante consiste à essayer d\'appliquer une dépouille à une face à laquelle un congé a déjà été appliqué. Pour résoudre ce problème, retirez le congé, appliquez la dépouille si nécessaire, puis réappliquez le congé.

## Propriétés

Voir aussi : [Éditeur de propriétés](Property_editor/fr.md)

Un objet Part Dépouille est dérivé d\'un [Part Feature](Part_Feature/fr.md) et hérite de toutes ses propriétés. Il possède également les propriétés supplémentaires suivantes :

### Données


{{Properties_Title|Base}}

-    **Angle|Angle**: Ne peut pas être négatif. Valeur par défaut : {{value|1.5 °}}.

-    **Reversed|Bool**: Valeur par défaut : `False`.

-    **Base|LinkSub**: Sous-lien vers la liste des arêtes et des faces sélectionnées de l\'élément parent.

-    **Support Transform|Bool**: Inclut la forme additive/soustractive de base lorsqu\'elle est utilisée dans les caractéristiques de motif. S\'il est désactivé, seule la partie habillée de la forme est utilisée pour le modelage. Valeur par défaut : `False`.

-    **Add Sub Shape|PartShape|hidden**.

-    **Base Feature|Link|hidden**: Lien vers l\'élément parent.

-    **_ Body|LinkHidden|hidden**: Lien vers le corps du parent.


{{Properties_Title|Draft}}

-    **Plan neutre|LinkSub**: Sous-lien vers la liste de l\'élément parent contenant le plan neutre.

-    **Direction de l'attraction|LinkSub**
    


{{Properties_Title|Part Design}}

-    **Refine|Bool**: Raffiner la forme (nettoyer les arêtes redondantes) après l\'ajout/soustraction. La valeur par défaut est déterminée par la préférence **Affiner automatiquement le modèle après une opération d'esquisse**. Voir [PartDesign Préférences](PartDesign_Preferences/fr#G.C3.A9n.C3.A9ral.md).





{{PartDesign Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Draft/fr
