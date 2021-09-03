---
- GuiCommand:/fr
   Name:PartDesign_LinearPattern
   Name/fr:PartDesign Répétition linéaire
   MenuLocation:Conception de pièces → Appliquer un modèle → Répétition linéaire
   Workbenches:[PartDesign](PartDesign_Workbench/fr.md)
---

## Description

L\'outil **<img src=images/PartDesign_LinearPattern.svg style="width:24px"> '''Répétition linéaire'''** créé des copies d\'une fonction espacées également le long d\'une droite. A partir de {{VersionPlus/fr|0.17}}, l\'outil de modèle linéaire peut modéliser plusieurs fonctions.

![](images/PartDesign_LinearPattern_example.svg )

*Ci-dessus, une protrusion en forme de L (B) créée sur le dessus de la protrusion de base (A, aussi dénommée \"support\") est utilisée dans une répétition linéaire. Le résultat (C) est affiché à droite.*

## Utilisation

Pour créer un motif :

1.  Sélectionnez la fonctionnalité ({{Version/fr|0.19}} ou plusieurs fonctionnalités) à répéter.
2.  Appuyez sur le bouton **<img src=images/PartDesign_LinearPattern.svg style="width:24px"> '''Répétition linéaire'''**.
3.  Définissez la **Direction**. Voir [Options](#Options.md).
4.  Définissez la **Longueur** (distance) entre la dernière occurrence copiée et l\'entité d\'origine.
5.  Définissez le nombre **d\'occurrences**.
6.  Si vous avez plusieurs fonctionnalités dans le motif, leur ordre peut être important, voir par exemple l\'image dans [PartDesign Répétition circulaire](PartDesign_PolarPattern/fr#Utilisation.md). {{Version/fr|0.19}}, vous pouvez changer l\'ordre en faisant glisser la fonction dans la liste et vous verrez le résultat immédiatement en aperçu.
7.  Appuyez sur **OK**.

Pour ajouter ou supprimer des fonctionnalités d\'un modèle existant :

1.  Appuyez sur **Ajouter une fonction** pour ajouter une fonction à modeler. La fonction doit être visible dans la [vue 3D](3D_view/fr.md) :
    1.  Basculez vers l\'arborescence du modèle ;
    2.  Sélectionnez dans l\'arborescence la fonction à ajouter et appuyez sur **Barre d'espace** pour la rendre visible dans la [vue 3D](3D_view/fr.md) ;
    3.  Revenez au panneau Tâches ;
    4.  Sélectionnez la fonction dans la vue 3D ; il sera ajouté à la liste.
    5.  Répétez pour ajouter d\'autres fonctionnalités.
2.  Appuyez sur **Supprimer une fonction** pour supprimer une fonctionnalité de la liste, ou cliquez avec le bouton droit de la souris sur la fonctionnalité dans la liste et sélectionnez **Supprimer**.

## Options

![Paramètres de répétition linéaire sous la v0.16 et antérieures.](images/Linearpattern_parameters.png ) ![Paramètres de répétition linéaire sous la v0.17 et ultérieures.](images/Linearpattern_parameters_v017.png )

### Direction

Lors de la création d\'une répétition linéaire, la boîte de dialogue \'Paramètres de la répétition linéaire\' offre différentes manières de spécifier la direction de la répétition.

#### Axe d\'esquisse horizontal 

Utilise l\'axe horizontal de l\'esquisse comme direction.

#### Axe d\'esquisse vertical 

Utilise l\'axe vertical de l\'esquisse comme direction.

#### Axe normal à l\'esquisse 


{{VersionPlus/fr|0.17}}

Utilise l\'axe normal à l\'esquisse comme direction.

#### Sélectionnez une référence\... 

Vous permet de sélectionner une ligne de référence, l\'arête d\'un objet ou une ligne d\'une esquisse comme direction.

#### Axe d\'esquisse personnalisé 

Si l\'esquisse qui définit la fonction à répéter contient également une ou plusieurs ligne(s) de construction, alors la liste déroulante contiendra un axe d\'esquisse personnalisé pour chaque ligne de construction. La première ligne de la construction sera étiquetée *Sketch axis 0*.

#### Axe (X/Y/Z) 


{{VersionPlus/fr|0.17}}

Sélectionnez l\'un des axes standard de l\'origine du corps (X, Y ou Z) comme direction. 

## Limitations

-   Les formes répétées ne peuvent pas se chevaucher, sauf dans le cas spécifique de seulement deux occurrences (original plus une copie).
-   Les formes qui ne chevauchent pas le support original seront exclues. Ceci garantit qu\'une fonction PartDesign se compose toujours d\'un volume solide unique.
-   Les motifs PartDesign ne sont pas encore aussi optimisés que leurs homologues Draft. Donc, pour un plus grand nombre d\'instances, vous devriez envisager d\'utiliser [Draft Réseau orthogonal](Draft_OrthoArray/fr.md) à la place, combiné avec une opération booléenne Part. Cela peut entraîner des modifications majeures de votre modèle lorsque vous quittez PartDesign, ce qui signifie que vous ne pouvez pas simplement continuer avec d\'autres fonctionnalités PartDesign dans le même corps. Un exemple est présenté dans ce [Sujet de forum](https://forum.freecadweb.org/viewtopic.php?f=3&t=55192)
-   Pour d\'autres limitations, voir [PartDesign Symétrie](PartDesign_Mirrored/fr.md).





{{PartDesign Tools navi

}} 
