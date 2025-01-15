---
 GuiCommand:
   Name: Sketcher ConstrainCoincidentUnified
   Name/fr: Sketcher Contrainte de coïncidence unifiée
   MenuLocation: Esquisse , Contraintes d'esquisse , Contrainte de coïncidence
   Workbenches: Sketcher_Workbench/fr
   Shortcut: **C**
   Version: 1.0
   SeeAlso: Sketcher_ConstrainCoincident/fr, Sketcher_ConstrainPointOnObject/fr
---

# Sketcher ConstrainCoincidentUnified/fr

## Description

L\'outil <img alt="" src=images/Sketcher_ConstrainCoincidentUnified.svg  style="width:24px;"> [Sketcher ConstrainCoincidentUnified](Sketcher_ConstrainCoincidentUnified/fr.md) crée une contrainte de coïncidence entre des points, fixe des points sur des arêtes ou des axes (les lignes sont alors considérées comme infinies et les courbes ouvertes sont virtuellement étendues), ou crée une contrainte concentrique entre des cercles, des arcs et/ou des ellipses (en faisant coïncider leurs centres).

Cet outil remplace les commandes [Sketcher Contrainte de coïncidence](Sketcher_ConstrainCoincident/fr.md) et [Sketcher Contrainte point sur objet](Sketcher_ConstrainPointOnObject/fr.md) si l\'option **Unifier la contrainte de coïncidence et la contrainte de point sur objet** est sélectionnée dans les [préférences](Sketcher_Preferences/fr#Général.md).



## Utilisation

Voir aussi : [Aides au dessin](Sketcher_Workbench/fr#Aides_au_dessin.md).



### [Mode continu](Sketcher_Workbench/fr#Modes_continus.md) 

1.  Assurez-vous qu\'il n\'y a pas de sélection.
2.  Il y a plusieurs façons de lancer l\'outil :
    -   Appuyez sur le bouton **<img src="images/Sketcher_ConstrainCoincidentUnified.svg" width=16px> [Contrainte de coïncidence](Sketcher_ConstrainCoincidentUnified/fr.md)**.
    -   Sélectionnez l\'option **Esquisse → Contraintes d'esquisse → <img src="images/Sketcher_ConstrainCoincidentUnified.svg" width=16px> Contrainte de coïncidence** du menu.
    -   Cliquez avec le bouton droit de la souris dans la [vue 3D](3D_view/fr.md) et sélectionnez l\'option **Contrainte → <img src="images/Sketcher_ConstrainCoincidentUnified.svg" width=16px> Contrainte de coïncidence** du menu contextuel.
    -   Utilisez le raccourci clavier : **C**.
3.  Le curseur se transforme en croix avec l\'icône de l\'outil.
4.  Effectuez l\'une des opérations suivantes :
    -   Sélectionnez deux points.
    -   Sélectionnez deux bords de cercles, d\'arcs, d\'ellipses ou d\'arcs d\'ellipses.
    -   Sélectionnez un seul point et une seule arête (dans n\'importe quel ordre).
5.  Une contrainte est ajoutée.
6.  Il est possible de continuer à créer des contraintes.
7.  Pour terminer, cliquez avec le bouton droit de la souris ou appuyez sur **Échap**, ou démarrez un autre outil de création de géométrie ou de contrainte.



### Mode unique 

1.  Faites l\'une des choses suivantes :
    -   Sélectionnez deux points ou plus.
    -   Sélectionnez deux ou plusieurs arêtes de cercles, d\'arcs, d\'ellipses ou d\'arcs d\'ellipses.
    -   Sélectionnez un seul point et une seule arête (dans n\'importe quel ordre).
    -   Sélectionnez plusieurs points et une seule arête (idem).
    -   Sélectionnez un seul point et plusieurs arêtes (idem).
2.  Lancez l\'outil comme expliqué ci-dessus, ou avec l\'option supplémentaire suivante :
    -   Cliquez avec le bouton droit de la souris dans la [vue 3D](3D_view/fr.md) et sélectionnez l\'option **Contrainte → <img src="images/Sketcher_ConstrainCoincidentUnified.svg" width=16px> Contrainte de coïncidence** du menu contextuel.
3.  En fonction de la sélection, une ou plusieurs contraintes sont ajoutées.



## Remarques

-    {{Version/fr|1.0}}: les points avec des contraintes coïncidentes sont marqués avec la [couleur](Sketcher_Preferences/fr#Affichage.md) des **symboles de contrainte**.



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainCoincidentUnified/fr
