---
 GuiCommand:
   Name: Sketcher ConstrainParallel
   Name/fr: Sketcher Contrainte parallèle
   MenuLocation: Esquisse , Contraintes d'esquisse , Contrainte parallèle
   Workbenches: Sketcher_Workbench/fr
   Shortcut: **P**
   SeeAlso: 
---

# Sketcher ConstrainParallel/fr

## Description

L\'outil <img alt="" src=images/Sketcher_ConstrainParallel.svg  style="width:24px;"> [Sketcher Contrainte parallèle](Sketcher_ConstrainParallel/fr.md) contraint les lignes à être parallèles.



## Utilisation

Voir aussi : [Aides au dessin](Sketcher_Workbench/fr#Aides_au_dessin.md).



### [Mode continu](Sketcher_Workbench/fr#Modes_continus.md) 

1.  Assurez-vous qu\'il n\'y a pas de sélection.
2.  Il y a plusieurs façons de lancer l\'outil :
    -   Appuyez sur le bouton **<img src="images/Sketcher_ConstrainParallel.svg" width=16px> [Contrainte parallèle](Sketcher_ConstrainParallel/fr.md)**.

    -   Sélectionnez l\'option **Esquisse → Contraintes d'esquisse → <img src="images/Sketcher_ConstrainParallel.svg" width=16px> Contrainte parallèle** du menu.

    -   
        {{Version/fr|1.0}}
        
        : cliquez avec le bouton droit de la souris dans la [vue 3D](3D_view/fr.md) et sélectionnez l\'option **Contrainte → <img src="images/Sketcher_ConstrainParallel.svg" width=16px> Contrainte parallèle** du menu contextuel.

    -   Utilisez le raccourci clavier : **P**.
3.  Le curseur se transforme en croix avec l\'icône de l\'outil.
4.  Sélectionnez deux lignes.
5.  Une contrainte est ajoutée.
6.  Il est possible de continuer à créer des contraintes.
7.  Pour terminer, cliquez avec le bouton droit de la souris ou appuyez sur **Échap**, ou démarrez un autre outil de création de géométrie ou de contrainte.



### Mode unique 

1.  Sélectionnez deux lignes ou plus. {{Version/fr|1.0}} : des points peuvent être inclus dans la sélection, mais ils seront ignorés.
2.  Lancez l\'outil comme expliqué ci-dessus, ou avec l\'option supplémentaire suivante :
    -   
        {{Version/fr|1.0}}
        
        : cliquez avec le bouton droit de la souris dans la [vue 3D](3D_view/fr.md) et sélectionnez l\'option **<img src="images/Sketcher_ConstrainParallel.svg" width=16px> Contrainte parallèle** du menu contextuel.
3.  En fonction de la sélection, une ou plusieurs contraintes sont ajoutées.



## Script


```pythonSketch.addConstraint(Sketcher.Constraint('Parallel', Line1, Line2))```

La page [Sketcher Scripts](Sketcher_scripting/fr.md) explique les valeurs qui peuvent être utilisées pour `Line1` et `Line2` et contient d\'autres exemples sur la façon de créer des contraintes à partir de scripts Python.



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainParallel/fr
