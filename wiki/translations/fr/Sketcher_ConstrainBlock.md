---
 GuiCommand:
   Name: Sketcher ConstrainBlock
   Name/fr: Sketcher Contrainte de blocage
   MenuLocation: Esquisse , Contraintes d'esquisse , Contrainte de blocage
   Workbenches: Sketcher_Workbench/fr
   Shortcut: **K** **B**
   Version: 0.17
   SeeAlso: Sketcher_ConstrainLock/fr
---

# Sketcher ConstrainBlock/fr

## Description

L\'outil <img alt="" src=images/Sketcher_ConstrainBlock.svg  style="width:24px;"> [Sketcher Contrainte de blocage](Sketcher_ConstrainBlock/fr.md) permet de bloquer les arêtes en place à l\'aide d\'une seule contrainte. Il est principalement destiné aux [B-splines](Sketcher_CreateBSpline/fr.md), qui peuvent être difficiles à contraindre complètement autrement.

La contrainte de blocage n\'affecte que les parties librement déplaçables d\'une arête. Les arêtes bloquées peuvent avoir d\'autres contraintes, et l\'application de contraintes supplémentaires à une arête bloquée peut la modifier.



## Utilisation

Voir aussi : [Aides au dessin](Sketcher_Workbench/fr#Aides_au_dessin.md).



### [Mode continu](Sketcher_Workbench/fr#Modes_continus.md) 

1.  Assurez-vous qu\'il n\'y a pas de sélection.
2.  Il y a plusieurs façons de lancer l\'outil :
    -   Appuyez sur le bouton **<img src="images/Sketcher_ConstrainBlock.svg" width=16px> [Bloc de contrainte](Sketcher_ConstrainBlock.md)**.

    -   Sélectionnez l\'option **Esquisse → Contraintes d'esquisse → <img src="images/Sketcher_ConstrainBlock.svg" width=16px> Contrainte de blocage** dans le menu.

    -   
        {{Version/fr|1.0}}
        
        : cliquez avec le bouton droit de la souris dans la [vue 3D](3D_view/fr.md) et sélectionnez l\'option **Contrainte → <img src="images/Sketcher_ConstrainBlock.svg" width=16px> Contrainte de blocage** dans le menu contextuel.

    -   Utilisez le raccourci clavier : **K** puis **B**.
3.  Le curseur se transforme en croix avec l\'icône de l\'outil.
4.  Sélectionnez une seule arête.
5.  Une contrainte est ajoutée.
6.  Il est possible de continuer à créer des contraintes.
7.  Pour terminer, cliquez avec le bouton droit de la souris ou appuyez sur **Échap**, ou démarrez un autre outil de création de géométrie ou de contrainte.



### Mode unique 

1.  Sélectionnez une ou plusieurs arêtes.
2.  Invoquer l\'outil comme expliqué ci-dessus, ou avec l\'option supplémentaire suivante :
    -   
        {{Version/fr|1.0}}
        
        : Cliquez avec le bouton droit de la souris dans la [vue 3D](3D_view/fr.md) et sélectionnez l\'option **<img src="images/Sketcher_ConstrainBlock.svg" width=16px> Contrainte de blocage ** du menu contextuel.
3.  En fonction de la sélection, une ou plusieurs contraintes sont ajoutées.



## Script


```pythonSketch.addConstraint(Sketcher.Constraint('Block', Edge))```

La page [Sketcher Scripts](Sketcher_scripting/fr.md) explique les valeurs qui peuvent être utilisées pour `Edge` et contient d\'autres exemples sur la façon de créer des contraintes à partir de scripts Python.



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainBlock/fr
