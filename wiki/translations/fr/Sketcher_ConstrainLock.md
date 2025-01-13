---
 GuiCommand:
   Name: Sketcher ConstrainLock
   Name/fr: Sketcher Contrainte fixe
   MenuLocation: Esquisse , Contraintes d'esquisse , Contrainte fixe
   Workbenches: Sketcher_Workbench/fr
   Shortcut: **K** **L**
   SeeAlso: Sketcher_ConstrainBlock/fr
---

# Sketcher ConstrainLock/fr

## Description

L\'outil <img alt="" src=images/Sketcher_ConstrainLock.svg  style="width:24px;"> [Sketcher Contrainte fixe](Sketcher_ConstrainLock/fr.md) applique des contraintes de [distance horizontale](Sketcher_ConstrainDistanceX/fr.md) et de [distance verticale](Sketcher_ConstrainDistanceY/fr.md) à des points. Si un seul point est sélectionné, les contraintes font référence à l\'origine de l\'esquisse. Si deux points ou plus sont sélectionnés, les contraintes font référence au dernier point de la sélection.



## Utilisation

Voir aussi : [Aides au dessin](Sketcher_Workbench/fr#Aides_au_dessin.md).



### [Mode continu](Sketcher_Workbench/fr#Modes_continus.md) 

1.  Assurez-vous qu\'il n\'y a pas de sélection.
2.  Il y a plusieurs façons de lancer l\'outil :
    -   
        {{Version/fr|1.0}}
        
        : si la [préférence](Sketcher_Preferences/fr#Général.md) des **contraintes des dimensions** est réglée sur {{Value|Outil unique}} (par défaut) : appuyez sur la flèche vers le bas à droite du bouton **<img src="images/Sketcher_Dimension.svg" width=|x16px><img src="images/Toolbar_flyout_arrow.svg" width=x16px>** et sélectionnez l\'option **<img src="images/Sketcher_ConstrainLock.svg" width=16px> Contrainte fixe** du menu déroulant.

    -   Si cette préférence a une valeur différente (et dans {{VersionMinus/fr|0.21}}) : appuyez sur le bouton **<img src="images/Sketcher_ConstrainLock.svg" width=16px> [Contrainte fixe](Sketcher_ConstrainLock/fr.md)**.

    -   Sélectionnez l\'option **Esquisse → Contraintes d'esquisses → <img src="images/Sketcher_ConstrainLock.svg" width=16px> Contrainte fixe** du menu.

    -   
        {{Version/fr|1.0}}
        
        : cliquez avec le bouton droit de la souris dans la [vue 3D](3D_view/fr.md) et sélectionnez l\'option **Dimension → <img src="images/Sketcher_ConstrainLock.svg" width=16px> Contrainte fixe** du menu contextuel.

    -   Utilisez le raccourci clavier : **K** puis **L**.
3.  Le curseur se transforme en croix avec l\'icône de l\'outil.
4.  Sélectionnez un seul point.
5.  Deux contraintes sont ajoutées.
6.  Continuez à créer des contraintes, si vous le souhaitez.
7.  Pour terminer, cliquez avec le bouton droit de la souris ou appuyez sur **Échap**.



### Mode unique 

1.  Sélectionnez un ou plusieurs points.
2.  Lancez l\'outil comme expliqué ci-dessus.
3.  En fonction de la sélection, deux contraintes ou plus sont ajoutées.



## Remarques

-   Il n\'y a pas d\'invite automatique à modifier les valeurs des contraintes. Si nécessaire, les valeurs peuvent être [modifiées manuellement](Sketcher_Workbench/fr#Modifier_les_contraintes.md).





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainLock/fr
