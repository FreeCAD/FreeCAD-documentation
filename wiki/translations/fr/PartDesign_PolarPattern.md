---
- GuiCommand:/fr
   Name:PartDesign_PolarPattern
   Name/fr:PartDesign Répétition circulaire
   MenuLocation:Conception de pièces → Appliquer un modèle → Répétition circulaire
   Workbenches:[PartDesign](PartDesign_Workbench/fr.md)
---

# PartDesign PolarPattern/fr

## Description

L\'outil *répétition circulaire* prend une fonction sélectionnée et produit à partir de celle-ci un ensemble de copies pivotées autour d\'un axe donné. À partir de la version 0.17, il peut copier plusieurs fonctions.

![](images/PartDesign_PolarPattern_example.png )

\'\'Ci-dessus : une cavité de forme oblongue (B) faite sur un solide de base (A, aussi dénommée \"support\") est utilisée pour une répétition circulaire. Le résultat (C) est affiché à droite.

## Utilisation

#### Pour créer un motif 

1.  (Optionnel) Sélectionnez la fonctionnalité (ou plusieurs fonctionnalités {{Version/fr|0.19}}) à répéter.
2.  Appuyez sur le bouton **<img src=images/PartDesign_PolarPattern.svg style="width:24px">** **Répétition circulaire**.
    -   Si vous n\'avez initialement sélectionné aucune fonctionnalité, vous pourrez sélectionner une fonctionnalité de base *unique*
3.  Définissez l**\'Axe**. Voir [Options](#Options.md).
4.  Définissez l**\'Angle** entre la dernière occurrence copiée et la fonction d\'origine.
5.  Définissez le nombre d**\'occurrences**.
6.  Si vous avez plusieurs fonctionnalités dans le motif, leur ordre peut être important, voir l\'image ci-dessous.
7.  Appuyez sur **OK**.

#### Organiser les fonctionnalités 

![](images/PartDesign_feature-order.gif ) 
*Effet de l'ordre des fonctionnalités*


{{Version/fr|0.19}}

Vous pouvez changer l\'ordre en faisant glisser l\'élément dans la liste et vous verrez le résultat immédiatement sous forme d\'aperçu.

#### Ajout de fonctionnalités 

###### v0.18

1.  Appuyez sur **Add feature** pour ajouter une fonction à modeler. La fonction doit être visible dans la [vue 3D](3D_view.md) :
2.  Basculez vers l\'arborescence du modèle ;
3.  Sélectionnez dans l\'arborescence la fonction à ajouter et appuyez sur **Barre d'espace** pour la rendre visible dans la [vue 3D](3D_view.md) ;
4.  Revenez au panneau Tâches ;
5.  Sélectionnez la fonction dans la vue 3D ; il sera ajouté à la liste.
6.  Répétez pour ajouter d\'autres fonctionnalités.

###### v0.19

1.  Appuyez sur **Add feature** pour ajouter une fonction à répéter.
2.  Basculez vers l\'arborescence du modèle ;
3.  Sélectionnez dans l\'arborescence la fonction à ajouter.
4.  Répétez pour ajouter d\'autres fonctionnalités.

#### Suppression de fonctionnalités 

-   Faites un clic droit sur la fonctionnalité dans la liste et sélectionnez *Remove*.

ou

###### v0.18 

1.  Appuyez sur **Remove feature** pour ajouter une fonction à modeler. La fonction doit être visible dans la [vue 3D](3D_view.md) :
2.  Basculez vers l\'arborescence du modèle ;
3.  Sélectionnez dans l\'arborescence la fonction à supprimer et appuyez sur **Barre d'espace** pour la rendre visible dans la [vue 3D](3D_view.md) ;
4.  Revenez au panneau Tâches ;
5.  Sélectionnez la fonction dans la vue 3D ; il sera ajouté à la liste.
6.  Répétez pour supprimer d\'autres fonctionnalités.

###### v0.19 

1.  Appuyez sur **Remove feature** pour supprimer une fonctionnalité de la liste.
2.  Basculez vers l\'arborescence du modèle ;
3.  Sélectionnez dans l\'arborescence la fonction à supprimer.
4.  Répétez pour supprimer d\'autres fonctionnalités.

## Options

![](images/Polarpattern_parameters.png )

### Axe

Lors de la création d\'une fonction de répétition circulaire, la boîte de dialogue *Paramètres de répétition circulaire* offre différentes façons de définir l\'axe de rotation du modèle.

#### Axe normal à l\'esquisse 

Un axe normal au plan d\'esquisse et centré sur l\'origine de l\'esquisse est utilisé comme axe de rotation de la répétition circulaire. En cochant **Inverser la direction**, la direction de la répétition peut être inversée.

#### Axe d\'esquisse horizontal 

Utilise l\'axe horizontal de l\'esquisse comme axe.

#### Axe d\'esquisse vertical 

Utilise l\'axe vertical de l\'esquisse comme axe.

#### Axe d\'esquisse personnalisé 

Si l\'esquisse qui définit la fonction à répéter contient également une ou plusieurs ligne(s) de construction, la liste déroulante contiendra un axe d\'esquisse personnalisé pour chaque ligne de construction. La première ligne de la construction sera étiquetée *Sketch axis 0*.

#### Axe (X/Y/Z) 


{{VersionPlus/fr|0.17}}

Sélectionne l\'un des axes standards de l\'origine du corps (X, Y ou Z).

#### Sélectionnez une référence\... 

Vous permet de sélectionner une ligne de référence, l\'arête d\'un objet ou une ligne d\'une esquisse comme axe.

### Angle et occurrences 

Spécifie l\'angle qui sera couvert par la répétition circulaire, ainsi que le nombre total de répétitions (y compris la forme d\'origine). Par exemple, quatre occurrences dans un angle de 180 degrés donnera un espacement de 60 degrés entre les répétitions. Il existe une exception : si l\'angle est de 360 degrés, puisque la première et la dernière occurrence sont identiques, quatre occurrences seront espacées de 90 degrés. 


## Limitations

-   Voir [Répétition linéaire](PartDesign_LinearPattern/fr#Limitations.md) pour d\'autres limitations.








{{PartDesign Tools navi

}}

---
[documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign PolarPattern/fr
