---
 GuiCommand:
   Name: Sketcher ConstrainSymmetric
   Name/fr: Sketcher Contrainte de symétrie
   MenuLocation: Esquisse , Contraintes d'esquisse , Contrainte de symétrie
   Workbenches: Sketcher_Workbench/fr
   Shortcut: **S**
   SeeAlso: 
---

# Sketcher ConstrainSymmetric/fr

## Description

L\'outil <img alt="" src=images/Sketcher_ConstrainSymmetric.svg  style="width:24px;"> [Sketcher Contrainte de symétrie](Sketcher_ConstrainSymmetric/fr.md) permet de contraindre deux points à être symétriques autour d\'une ligne ou d\'un axe, ou autour d\'un troisième point.



## Utilisation

Voir aussi : [Aides au dessin](Sketcher_Workbench/fr#Aides_au_dessin.md).



### [Mode continu](Sketcher_Workbench/fr#Modes_continus.md) 

1.  Assurez-vous qu\'il n\'y a pas de sélection.
2.  Il y a plusieurs façons de lancer l\'outil :
    -   Appuyez sur le bouton **<img src="images/Sketcher_ConstrainSymmetric.svg" width=16px> [Contrainte de symétrie](Sketcher_ConstrainSymmetric/fr.md)**.

    -   Sélectionnez l\'option **Esquisse → Contraintes de l'esquisse → <img src="images/Sketcher_ConstrainSymmetric.svg" width=16px> Contrainte de symétrie** dans le menu.

    -   
        {{Version/fr|1.0}}
        
        : cliquez avec le bouton droit de la souris dans la [vue 3D](3D_view/fr.md) et sélectionnez l\'option **Contrainte → <img src="images/Sketcher_ConstrainSymmetric.svg" width=16px> Contrainte de symétrie** du menu contextuel.

    -   Utilisez le raccourci clavier : **S**.
3.  Le curseur se transforme en croix avec l\'icône de l\'outil.
4.  Effectuez l\'une des opérations suivantes :
    -   Sélectionnez deux points et un point de symétrie (dans cet ordre).
    -   Sélectionnez deux points et une ligne de symétrie (idem).
    -   Sélectionnez un point, une ligne de symétrie et un autre point (idem).
    -   Sélectionnez une ligne et un point de symétrie (idem).
5.  Une contrainte est ajoutée.
6.  Il est possible de continuer à créer des contraintes.
7.  Pour terminer, cliquez avec le bouton droit de la souris ou appuyez sur **Échap**, ou démarrez un autre outil de création de géométrie ou de contrainte.



### Mode unique 

1.  Faites l\'une des choses suivantes :
    -   Sélectionnez deux points et un point de symétrie (dans cet ordre).
    -   Sélectionnez deux points et une ligne de symétrie (dans n\'importe quel ordre).
    -   Sélectionnez une ligne et un point de symétrie (idem).
2.  Lancez l\'outil comme expliqué ci-dessus, ou avec l\'option supplémentaire suivante :
    -   
        {{Version/fr|1.0}}
        
        : cliquez avec le bouton droit de la souris dans la [vue 3D](3D_view/fr.md) et sélectionnez l\'option **Contrainte → <img src="images/Sketcher_ConstrainSymmetric.svg" width=16px> Contrainte de symétrie** du menu contextuel.
3.  Une contrainte est ajoutée.



## Remarques

-   Les flèches de cette contrainte indiquent la couleur des contraintes dimensionnelles.



## Script

Deux points et une ligne de symétrie :


```pythonSketch.addConstraint(Sketcher.Constraint('Symmetric', Line1, PointOfLine1, Line2, PointOfLine2, SymmetryLine))```

Deux points et un point de symétrie :


```pythonSketch.addConstraint(Sketcher.Constraint('Symmetric', Line1, PointOfLine1, Line2, PointOfLine2, LineS, PointOfLineS))```

Une ligne et un point de symétrie (dans l\'interface graphique, on peut sélectionner une ligne et un point. Cela utilise en interne la même forme que ci-dessus avec les deux extrémités de la même ligne) :


```pythonSketch.addConstraint(Sketcher.Constraint('Symmetric', Line, 1, Line, 2, LineS, PointOfLineS))```

La page [Sketcher Scripts](Sketcher_scripting/fr.md) explique les valeurs qui peuvent être utilisées pour `Line1`, `Line2`, `LineS`, `Line`, `PointOfLine1`, `PointOfLine2` et `PointOfLineS` et contient d\'autres exemples sur la façon de créer des contraintes à partir de scripts Python.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainSymmetric/fr
