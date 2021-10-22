---
- GuiCommand:/fr
   Name:PartDesign_MultiTransform
   Name/fr:PartDesign Transformation multiple
   MenuLocation:Conception de pièces → Appliquer un modèle → Créer une transformation multiple
   Workbenches:[PartDesign](PartDesign_Workbench/fr.md)
---

# PartDesign MultiTransform/fr

## Description

\'Créer un motif à partir de combinaisons de transformations\' - L\'outil **![](images/)_[Transformation_multiple](PartDesign_MultiTransform/fr.md)** prend une partie (ou un ensemble de) \'fonctionnalités\' en entrée et permet à l\'utilisateur d\'appliquer progressivement plusieurs transformations à cette fonctionnalité (ou à cet ensemble de fonctionnalités), en séquence, créant ainsi une transformation combinée ou composée.

Par exemple, pour produire la bride avec une double rangée de trous comme illustré ci-dessous, l\'utilisateur :

1.  sélectionne le trou en tant que \'fonctionnalité\' (base) dans l\'arbre du modèle
2.  clique sur l\'icône **![](images/)_[Transformation_multiple](PartDesign_MultiTransform/fr.md)**
3.  ajoute un motif linéaire avec deux occurrences dans la direction X
4.  ajoute un motif polaire à huit occurrences autour de l'axe des Y.

<img alt="" src=images/multitransform_example.png  style="width:600px;"> 
*Bride à double rangée de trous. Motif de trou créé avec l'outil 'Transformation multiple'.*

## Utilisation

Avant de commencer l'une des méthodes ci-dessous, assurez-vous que l'objet **![](images/)_[Corps](PartDesign_Body/fr.md)** est [actif](PartDesign_Body#Usage_Notes/fr.md). Dans le cas contraire, un message d\'erreur indiquera que vous avez besoin d\'un objet actif **![](images/)_[Corps](PartDesign_Body/fr.md)** avant d\'utiliser l\'outil **![](images/)_[Transformation_multiple](PartDesign_MultiTransform/fr.md)**.

### Méthode standard 

Avec cette méthode, on commence sans aucune fonction de transformation existante ni de sélection dans la fenêtre ou l\'arborescence de l\'objet Modèle.
Une fois lancée et complétée par cette méthode, la **![](images/)_[Transformation_multiple](PartDesign_MultiTransform/fr.md)** devrait devenir correctement le \"Tip\" (fonction résultante) de l\'objet Corps (Body).

1.  Cliquez sur **![](images/)_[Transformation_multiple](PartDesign_MultiTransform/fr.md)** pour lancer l\'opération.
2.  La fenêtre **Sélectionner une fonctionnalité** vous sera proposée.
    Dans la liste, sélectionnez une fonctionnalité initiale à utiliser pour les transformations puis cliquez sur **OK** pour continuer.
    Vous pouvez ajouter des fonctionnalités supplémentaires dans la liste déroulante àl\'étape suivante.

    :   <img alt="" src=images/PartDesign-MultiTransform-Select_feature.png  style="width:300px;">
3.  Les fenêtres **Messages de la fonction de transformation** et **MultiTransform parameters** s\'afficheront.
    Vous verrez l\'étiquette de l\'entité sélectionnée dans la liste des entités sous **Ajouter une fonction** et **Supprimer une fonction**.

    :   <img alt="" src=images/PartDesign-MultiTransform-General.png  style="width:300px;">
    :   Si vous souhaitez inclure des fonctions supplémentaires pour les transformations, procédez comme suit :

    1.  Cliquez sur le bouton **Ajouter une fonction** dans l\'outil de transformation.
    2.  Passer à l\'arborescence du modèle (cliquez sur l\'onglet **Modèle**)
    3.  Sélectionnez la fonction que vous souhaitez ajouter et rendez-la visible (barre d\'espace, **\'\'ou**\'\' clic droit et basculez la visibilité).
        :\'\'\'Remarque : \'\'\'ceci masquera la fonction auparavant visible.
    4.  Cliquez sur n\'importe quoi dans la vue 3D (fenêtre d\'affichage).
    5.  Cliquez sur l\'onglet **Tâches** de la vue combinée pour revenir à la fenêtre **MultiTransform parameters**.
    6.  Vous devriez voir la notification de la fonction récemment sélectionnée apparaître dans la liste des fonctions.
4.  En dessous de la vue liste des fonctions se trouve la liste des **Transformations**. Dans la vue, vous devriez voir le texte \"*Faites un clic droit pour ajouter*\".
5.  Ajoutez une transformation en cliquant avec le bouton droit de la souris dans la vue **Transformations** pour afficher la liste des options.

    :   <img alt="" src=images/PartDesign-MultiTransform-Transformations_Right_Click.png  style="width:300px;">

    1.  Ajoutez la transformation souhaitée en la sélectionnant dans la liste des options.
    2.  La nouvelle entrée de transformation apparaîtra dans la liste **Transformations** avec les paramètres correspondants apparaissant sous la liste.

        :   <img alt="" src=images/PartDesign-MultiTransform-Transformations-add_linear_pattern.png  style="width:300px;">
    3.  Réglez les paramètres pour la nouvelle transformation. (*Vous verrez l\'aperçu dans la fenêtre.*)
    4.  Cliquez sur le bouton **OK** situé sous ces paramètres pour enregistrer la nouvelle transformation.
6.  Continuez à ajouter des transformations dans l\'ordre duquel vous souhaitez les appliquer à l\'étape 5 ci-dessus.
7.  Vous pouvez également éditer, supprimer et déplacer (changer l\'ordre des) les transformations selon vos besoins en cliquant avec le bouton droit de la souris sur une transformation dans la liste **Transformations** et en sélectionnant l\'option correspondante.
8.  Lorsque vous avez terminé d\'ajouter et de modifier les transformations, cliquez sur le bouton **OK** tout en haut pour enregistrer le **![](images/)_[Transformation_multiple](PartDesign_MultiTransform/fr.md)** et quitter.

### Méthode alternative 1 

Cette méthode commence par une fonction de transformation existante dans l\'objet **![](images/)_[Corps](PartDesign_Body/fr.md)**.

1.  Dans l\'arborescence du modèle, dans le corps actif, sélectionnez les fonctions existantes à inclure.
2.  Cliquez sur le **![](images/)_[Transformation_multiple](PartDesign_MultiTransform/fr.md)** pour lancer l\'opération.
3.  Dans la liste des fonctions, vous verrez les notifications des fonctions que vous avez sélectionnées.
    Pour ajouter des fonctions supplémentaires, voir l**\'Étape 3** de la section [Méthode standard](PartDesign_MultiTransform#Standard_Method/fr.md) ci-dessus.
4.  Terminez en utilisant les **étapes 5 à 8** de la [Méthode standard](PartDesign_MultiTransform/fr#M.C3.A9thode_standard.md) au-dessus.

### Méthode alternative 2 

Cette méthode commence par plusieurs transformations de fonctions existantes et indépendantes dans l\'objet **![](images/)_[Corps](PartDesign_Body/fr.md)** - avec pour idée de les combiner. *Remarque:* pour combiner des transformations existantes, elles doivent se trouver dans le même objet Corps et doivent toutes utiliser la même fonction ou le même ensemble de fonctions dans chacune d\'elles.

1.  Dans l\'arborescence du modèle, depuis le Corps actif, sélectionnez l\'une des transformations existantes parmi celles que vous souhaitez inclure.
2.  Cliquez sur **![](images/)_[Transformation_multiple](PartDesign_MultiTransform/fr.md)** pour lancer l\'opération.
3.  Cliquez sur le bouton **OK** en haut pour enregistrer et quitter.
4.  Dans l\'arborescence des objets, sélectionnez **![](images/)_[Transformation_multiple](PartDesign_MultiTransform/fr.md)**.
5.  Dans la fenêtre *Propriété Vue*, localisez la propriété **Transformations** dans l\'onglet *Données*.
6.  Editez la propriété **Transformations** en cliquant sur sa valeur, puis cliquez sur la case ellipse apparue pour ouvrir la fenêtre **Liens** de cette propriété.
7.  Sélectionnez toutes les transformations d\'entités existantes à inclure. Les sélections multiples sont autorisées avec **CTRL** + clic.
8.  Cliquez sur **OK** pour enregistrer et fermer la fenêtre **Liens**.
9.  Cliquez sur le bouton **![](images/)_[Std_Rafraîchir](Std_Refresh/fr.md)** s\'il est activé.

Une fois lancé et complété de cette façon, **![](images/)_[Transformation_multiple](PartDesign_MultiTransform/fr.md)** pourrait ne pas devenir la fonction résultante de l\'objet Corps. Si elle doit être la fonction résultante:

1.  Cliquez avec le bouton droit de la souris sur la **![](images/)_[Transformation_multiple](PartDesign_MultiTransform/fr.md)**.
2.  Si disponible, choisissez \"**Désigner comme fonction résultante**\".

### Notes d\'utilisation 

-   Les transformations de fonctions prises en charge sont les suivantes : **<img src="images/PartDesign_Mirrored.svg" width=20px> [PartDesign Symétrie](PartDesign_Mirrored/fr.md)**, **<img src="images/PartDesign_LinearPattern.svg" width=20px> [PartDesign Répétition linéaire](PartDesign_LinearPattern/fr.md)**, **<img src="images/PartDesign_PolarPattern.svg" width=20px> [PartDesign Répétition circulaire](PartDesign_PolarPattern/fr.md)** et la transformation Mise à l\'echelle.
-   Chaque transformation liée à la **![](images/)_[Transformation_multiple](PartDesign_MultiTransform/fr.md)** doit utiliser la même fonction ou le même ensemble de fonctions pour chacune.

### Limitations

-   Une transformation Mise à l\'échelle ne doit pas être la première de la liste.
-   La transformation Mise à l\'échelle doit avoir le même nombre d\'occurrences que la transformation qui la précède immédiatement dans la liste.
-   Pour d\'autres limitations, voir **<img src="images/PartDesign_LinearPattern.svg" width=20px> [PartDesign Répétition linéaire](PartDesign_LinearPattern/fr.md)
**




## Options

+--------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ![](images/Multitransfrom_parameters.png ) | Lors de la création d\'une fonction de multitransformation, la boîte de dialogue \'paramètres de multitransformation\' propose deux listes différentes.                                                                                                                                                                                                                                                                                                                         |
|                                                                    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                    | ### Sélectionnez les originaux                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                    | La liste affiche les \'originaux\', les fonctions à appliquer. En cliquant sur une fonction, vous l\'ajouterez à la liste.                                                                                                                                                                                                                                                                                                                                                      |
|                                                                    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                    | ### Sélectionnez les transformations                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                    | Cette liste peut être complétée par une combinaison des transformations simples [PartDesign Symétrie](PartDesign_Mirrored/fr.md), [PartDesign Répétition linéaire](PartDesign_LinearPattern/fr.md), [PartDesign Répétition circulaire](PartDesign_PolarPattern/fr.md) et [PartDesign Mise à l\'échelle](PartDesign_Scaled/fr.md). Les transformations seront appliquées l\'une après l\'autre. Le menu contextuel offre les entrées suivantes : |
|                                                                    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                    | #### Modifier                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                    | Permet de modifier les paramètres d\'une transformation dans la liste (un double-clic aura le même effet)                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                    | #### Supprimer                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                    | Supprime une transformation de la liste                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                    | #### Ajouter une transformation                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                    | Ajoute une transformation à la liste                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                    | #### Monter/Descendre                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                    | Permet de changer l\'ordre des transformations dans la liste                                                                                                                                                                                                                                                                                                                                                                                                                    |
+--------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

## Exemples

![c\|800px](images/mt_example2.png ) 
*La plus petite protrusion a d'abord été configurée trois fois dans la direction X, puis redimensionnée deux fois plus grande (les trois occurrences ont donc les facteurs d'échelle 1.0, 1.5 et 2.0). Ensuite, une répétition polaire a été appliquée avec 8 occurrences.* ![c\|800px](images/mt_example3.png ) 
*La cavité a d'abord subit une symétrie sur le plan YZ puis fut configurée avec deux répétitions linéaires pour donner un motif rectangulaire.* 





{{PartDesign Tools navi

}}

---
[documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign MultiTransform/fr
