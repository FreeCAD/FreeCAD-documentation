---
 GuiCommand:
   Name: Sketcher ConstrainEqual
   Name/fr: Sketcher Contrainte d'égalité
   MenuLocation: Esquisse , Contraintes d'esquisse , Contrainte d'égalité
   Workbenches: Sketcher_Workbench/fr
   Shortcut: **E**
   SeeAlso: 
---

# Sketcher ConstrainEqual/fr

## Description

L\'outil <img alt="" src=images/Sketcher_ConstrainEqual.svg  style="width:24px;"> [Sketcher Contrainte d\'égalité](Sketcher_ConstrainEqual/fr.md) contraint les arêtes à avoir la même longueur (lignes) ou la même courbure (autres arêtes sauf les [B-splines](Sketcher_CreateBSpline/fr.md)). Les arêtes sélectionnées doivent être du même type. Les cercles et les arcs de cercle sont du même type (leurs rayons sont égaux), de même que les ellipses et les arcs elliptiques (leurs rayons majeurs et mineurs sont égaux).



## Utilisation

Voir aussi : [Aides au dessin](Sketcher_Workbench/fr#Aides_au_dessin.md).



### [Mode continu](Sketcher_Workbench/fr#Modes_continus.md) 

1.  Assurez-vous qu\'il n\'y a pas de sélection.
2.  Il y a plusieurs façons de lancer l\'outil :
    -   Appuyez sur le bouton **<img src="images/Sketcher_ConstrainEqual.svg" width=16px> [Contrainte d'égalité](Sketcher_ConstrainEqual/fr.md)**.

    -   Sélectionnez l\'option **Esquisse → Contraintes d'esquisse → <img src="images/Sketcher_ConstrainEqual.svg" width=16px> Contrainte d'égalité** du menu.

    -   
        {{Version/fr|1.0}}
        
        : cliquez avec le bouton droit de la souris dans la [vue 3D](3D_view/fr.md) et sélectionnez l\'option **Contrainte → <img src="images/Sketcher_ConstrainEqual.svg" width=16px> Contrainte d'égalité** dans le menu contextuel.

    -   Utilisez le raccourci clavier : **E**.
3.  Le curseur se transforme en croix avec l\'icône de l\'outil.
4.  Sélectionnez deux arêtes du même type.
5.  Une contrainte est ajoutée.
6.  Il est possible de continuer à créer des contraintes.
7.  Pour terminer, cliquez avec le bouton droit de la souris ou appuyez sur **Échap**, ou démarrez un autre outil de création de géométrie ou de contrainte.



### Mode unique 

1.  Sélectionnez une ou plusieurs arêtes.
2.  Invoquer l\'outil comme expliqué ci-dessus, ou avec l\'option supplémentaire suivante :
    -   
        {{Version/fr|1.0}}
        
        : Cliquez avec le bouton droit de la souris dans la [vue 3D](3D_view/fr.md) et sélectionnez l\'option **<img src="images/Sketcher_ConstrainEqual.svg" width=16px> Contrainte d'égalité** du menu contextuel.
3.  En fonction de la sélection, une ou plusieurs contraintes sont ajoutées.



## Script


```pythonSketch.addConstraint(Sketcher.Constraint('Equal', Edge1, Edge2))```

La page [Sketcher Scripts](Sketcher_scripting/fr.md) explique les valeurs qui peuvent être utilisées pour `Edge1` et `Edge2` et contient d\'autres exemples sur la façon de créer des contraintes à partir de scripts Python.



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainEqual/fr
