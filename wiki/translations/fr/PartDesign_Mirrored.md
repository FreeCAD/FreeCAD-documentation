---
- GuiCommand:/fr
   Name:PartDesign_Mirrored
   Name/fr:PartDesign Symétrie
   MenuLocation:Conception de pièces → Appliquer un modèle → Symétrie
   Workbenches:[PartDesign](PartDesign_Workbench/fr.md)
---

# PartDesign Mirrored/fr

## Description

L\'outil **Symétrie** copie symétriquement des fonctions par rapport à un plan.

![](images/PartDesign_Mirrored_example.svg )



*Ci-dessus : une fonction Pocket a été créée à partir d'un croquis contenant un cercle (A), la poche a ensuite été utilisée pour créer une fonction miroir. L'axe vertical d'esquisse (B) a été utilisé comme axe de symétrie. Le résultat (C) est affiché à droite.*

## Utilisation

Pour créer une mise en miroir :

1.  Sélectionnez la ou les fonctionnalités à mettre en miroir.
2.  Appuyez sur le bouton **<img src=images/_PartDesign_Mirrored.svg style="width:24px"> '''Symétrie'''**.
3.  Si vous avez plusieurs fonctionnalités dans la mise en miroir, leur ordre peut être important, voir par exemple l\'image dans la [PartDesign Répétition circulaire](PartDesign_PolarPattern/fr#Utilisation.md). {{Version/fr|0.19}}, vous pouvez changer l\'ordre en faisant glisser la fonction dans la liste et vous verrez le résultat immédiatement en aperçu.
4.  Définissez le miroir **Plan**. Voir [Options](#Options.md).
5.  Appuyez sur **OK**.

Pour ajouter ou supprimer des fonctionnalités d\'un modèle existant :

1.  Appuyez sur **Ajouter une fonction** pour ajouter une fonction à modeler. La fonction doit être visible dans la [vue 3D](3D_view/fr.md) :
    1.  Basculez vers l\'arborescence du modèle ;
    2.  Sélectionnez dans l\'arborescence la fonction à ajouter et appuyez sur **Barre d'espace** pour la rendre visible dans la [vue 3D](3D_view/fr.md) ;
    3.  Revenez au panneau Tâches ;
    4.  Sélectionnez la fonction dans la vue 3D ; il sera ajouté à la liste.
    5.  Répétez pour ajouter d\'autres fonctionnalités.
2.  Appuyez sur **Supprimer une fonction** pour supprimer une fonctionnalité de la liste, ou cliquez avec le bouton droit de la souris sur la fonctionnalité dans la liste et sélectionnez *Supprimer*.

## Options

![Paramètres de symétrie](images/Mirrored_parameters_v017.png )

### Plan

Lors de la création d\'une fonction symétrique, la boîte de dialogue **Paramètres de symétrie** propose différentes manières de spécifier la ligne ou le plan symétrique.

#### Axe d\'esquisse horizontal 

Utilise l\'axe horizontal de l\'esquisse comme axe de symétrie.

#### Axe d\'esquisse vertical 

Utilise l\'axe vertical de l\'esquisse comme axe de symétrie.

#### Sélectionnez une référence \... 

Vous permet de sélectionner un plan (comme une face d\'un objet) pour l\'utiliser comme plan de symétrie.

#### Axe personnalisé d\'esquisse 

Si l\'esquisse qui définit la fonction à symétriser contient également une ou plusieurs ligne(s) de construction, alors la liste déroulante contiendra un axe d\'esquisse personnalisé pour chaque ligne de construction. La première ligne de la construction sera étiquetée *Sketch axis 0*. L\'image ci-dessous est un exemple avec l\'esquisse en mode d\'édition affichant une ligne de construction utilisée comme axe de symétrie.

![](images/PartDesign_Mirrored_axis_fromconstructionlines.jpg )

#### Plan (XY/XZ/YZ) 

Sélectionnez l\'un des plans standards de l\'origine du Corps (XY, XZ ou YZ).

### Aperçu

Le résultat de la symétrie peut être prévisualisé en temps réel avant de cliquer sur **OK** en cochant *Réactualiser la vue*. 

## Limitations

-   La fonction de symétrie ne peut pas symétriser un solide entier. Pour cela, voir [Mise en miroir](Part_Mirror/fr.md).

-   La fonction de symétrie doit intersecter le solide (aussi appelé *support*) sur lequel elle est basée, sinon la commande échouera.





{{PartDesign Tools navi

}}

---
[documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Mirrored/fr
