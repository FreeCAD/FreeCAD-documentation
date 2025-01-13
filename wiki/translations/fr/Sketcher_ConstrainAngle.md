---
 GuiCommand:
   Name: Sketcher ConstrainAngle
   Name/fr: Sketcher Contrainte angulaire
   MenuLocation: Esquisse , Contraintes d'esquisse , Contrainte angulaire
   Workbenches: Sketcher_Workbench/fr
   Shortcut: **K** **A**
   SeeAlso: Sketcher_ConstrainPerpendicular/fr
---

# Sketcher ConstrainAngle/fr

## Description

L\'outil <img alt="" src=images/Sketcher_ConstrainAngle.svg  style="width:24px;"> [Sketcher Contrainte angulaire](Sketcher_ConstrainAngle/fr.md) fixe l\'angle entre deux arêtes (les lignes sont alors considérées comme infinies et les courbes ouvertes sont virtuellement étendues), l\'angle d\'une ligne avec l\'axe horizontal de l\'esquisse ou l\'angle d\'ouverture d\'un arc de cercle.



## Utilisation

Voir aussi : [Aides au dessin](Sketcher_Workbench/fr#Aides_au_dessin.md).



### [Mode continu](Sketcher_Workbench/fr#Modes_continus.md) 

1.  Assurez-vous qu\'il n\'y a pas de sélection.
2.  Il y a plusieurs façons de lancer l\'outil :
    -   
        {{Version/fr|1.0}}
        
        : si la [préférence](Sketcher_Preferences/fr#Général.md) des **contraintes de dimensions** est réglée sur {{Value|Outil unique}} (par défaut) : appuyez sur la flèche vers le bas à droite du bouton **<img src="images/Sketcher_Dimension.svg" width=|x16px><img src="images/Toolbar_flyout_arrow.svg" width=x16px>** et sélectionnez l\'option **<img src="images/Sketcher_ConstrainAngle.svg" width=16px> Contrainte angulaire** du menu déroulant.

    -   Si cette préférence a une valeur différente (et dans {{VersionMinus/fr|0.21}}) : appuyez sur le **<img src="images/Sketcher_ConstrainAngle.svg" width=16px> [Contrainte angulaire](Sketcher_ConstrainAngle/fr.md)**.

    -   Sélectionnez l\'option **Esquisse → Contraintes d'esquisse → <img src="images/Sketcher_ConstrainAngle.svg" width=16px> Contrainte angulaire** du menu.

    -   
        {{Version/fr|1.0}}
        
        : cliquez avec le bouton droit de la souris dans la [vue 3D](3D_view/fr.md) et sélectionnez l\'option **Dimension → <img src="images/Sketcher_ConstrainAngle.svg" width=16px> Contrainte angulaire** du menu contextuel.

    -   Utilisez le raccourci clavier : **K** puis **A**.
3.  Le curseur se transforme en croix avec l\'icône de l\'outil.
4.  Faites l\'une des choses suivantes :
    -   Sélectionner deux lignes.
    -   Sélectionner un point et deux arêtes (dans cet ordre).
    -   Sélectionner une arête, un point et une arête (idem).
5.  Si une [contrainte pilotante dimensionnelle](Sketcher_ToggleDrivingConstraint/fr.md) est créée, en fonction des [préférences](Sketcher_Preferences/fr#Affichage.md), une fenêtre de dialogue s\'ouvre pour [modifier sa valeur](Sketcher_Workbench/fr#Modifier_les_contraintes.md). Une valeur négative inversera la direction de l\'angle.
6.  Une contrainte d\'angle est ajoutée. Si un point et deux arêtes ont été sélectionnés, jusqu\'à deux [contraintes point sur objet](Sketcher_ConstrainPointOnObject/fr.md) peuvent également être ajoutées. Voir les [Exemples](#Entre_deux_arêtes_au_point.md).
7.  Vous pouvez continuer à créer des contraintes.
8.  Pour terminer, cliquez avec le bouton droit de la souris ou appuyez sur **Échap**, ou démarrez un autre outil de création de géométrie ou de contrainte.



### Mode unique 

1.  Faites l\'une des choses suivantes :
    -   Sélectionnez une seule ligne.
    -   Sélectionnez un seul arc de cercle.
    -   Sélectionnez deux lignes.
    -   Sélectionnez un point et deux arêtes (dans n\'importe quel ordre).
2.  Lancez l\'outil comme expliqué ci-dessus.
3.  Vous pouvez [modifier la valeur de la contrainte](Sketcher_Workbench/fr#Modifier_les_contraintes.md).
4.  Une contrainte d\'angle est ajoutée. Si un point et deux arêtes ont été sélectionnés, jusqu\'à deux [contraintes point sur objet](Sketcher_ConstrainPointOnObject/fr.md) peuvent également être ajoutées. Voir les [exemples](#Entre_deux_arêtes_au_point.md).



## Exemples



### Une seule ligne 

<img alt="" src=images/Sketcher_ConsraintAngle_mode1.png  style="width:400px;">

L\'angle de la ligne avec l\'axe X positif de l\'esquisse est fixe.



### Un seul arc de cercle 

<img alt="" src=images/Sketcher_ConsraintAngle_mode2.png  style="width:400px;">

L\'angle d\'ouverture de l\'arc est fixe.



### Entre deux lignes 

<img alt="" src=images/Sketcher_ConsraintAngle_mode3.png  style="width:400px;">

L\'angle entre les deux lignes est fixe. Il n\'est pas nécessaire que les lignes se croisent.



### Entre deux arêtes au point 

<img alt="" src=images/Sketcher_ConsraintAngle_mode4.png  style="width:400px;">

L\'angle entre les deux arêtes en un point donné est fixe. Le point peut être n\'importe quel point, par exemple le centre d\'un cercle, l\'extrémité d\'une arête ou l\'origine, il peut appartenir à l\'une ou l\'autre des arêtes ou aux deux, et il peut également être un [objet Point](Sketcher_CreatePoint/fr.md). Si nécessaire, des [contrainte(s) de point sur objet](Sketcher_ConstrainPointOnObject/fr.md) sont ajoutées pour s\'assurer que le point se trouve sur les deux arêtes (étendues). Ces contraintes supplémentaires sont appelées [contraintes d\'aide](Sketcher_helper_constraint/fr.md).



## Script

La Contrainte angle peut être créée depuis une [macros](Macros/fr.md) et depuis la console [Python](Python/fr.md) en utilisant : 
```python
# line slope angle
Sketch.addConstraint(Sketcher.Constraint('Angle',iline,angle))

# angular span of arc
Sketch.addConstraint(Sketcher.Constraint('Angle',iarc,angle))

# angle between lines
Sketch.addConstraint(Sketcher.Constraint('Angle',iline1,pointpos1,iline2,pointpos2,angle))

# angle-via-point (no helper constraints are added automatically when from python)
Sketch.addConstraint(Sketcher.Constraint('AngleViaPoint',icurve1,icurve2,geoidpoint,pointpos,angle))
``` où :

  - `Sketch` est un objet d\'esquisse:

  - `iline, iline1, iline2` sont des nombres entiers spécifiant les lignes par leurs nombres ordinaux dans `Sketch`.

  - `pointpos1, pointpos2` devrait être 1 pour point de départ et 2 pour le point de fin. Le choix des points permet de définir l\'angle interne (ou externe) et il affecte la façon dont la contrainte est dessinée à l\'écran.

  - `geoidpoint` et `pointpos` dans `AngleViaPoint` sont les indices précisant le point d\'intersection.

  - `angle` est la valeur d\'angle en radians. L\'angle est compté entre vecteurs tangents dans le sens antihoraire. Les vecteurs tangents pointent du début à la fin pour les lignes (ou vice versa si le point final est fourni dans l\'angle entre le mode de lignes) et le long du sens anti-horaire pour les cercles, arcs et ellipses.La valeur est également acceptée comme un angle (par exemple `App.Units.Quantity('45 deg')`)

La page [Sketcher Scripts](Sketcher_scripting/fr.md) explique les valeurs qui peuvent être utilisées pour `iline`, `iline1`, `iline2`, `pointpos1`, `pointpos2`, `geoidpoint` et `pointpos` et contient d\'autres exemples sur la façon de créer des contraintes à partir de scripts Python.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainAngle/fr
