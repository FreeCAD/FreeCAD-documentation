---
 GuiCommand:
   Name: Sketcher Split
   Name/fr: Sketcher Diviser
   MenuLocation: Esquisse , Outils d'esquisse , Diviser une arête
   Workbenches: Sketcher_Workbench/fr
   Shortcut: **G** **Z**
   Version: 0.20
   SeeAlso: Sketcher_Trimming/fr
---

# Sketcher Split/fr

## Description

L\'outil <img alt="" src=images/Sketcher_Split.svg  style="width:24px;"> [Sketcher Diviser](Sketcher_Split/fr.md) permet de diviser une arête. Si l\'arête est une courbe fermée (c\'est-à-dire un cercle, une ellipse ou une B-spline périodique), elle est convertie en courbe ouverte (respectivement un arc, un arc d\'ellipse ou une B-spline non périodique).



## Utilisation

Voir aussi : [Aides au dessin](Sketcher_Workbench/fr#Aides_au_dessin.md).

1.  Il y a plusieurs façons de lancer l\'outil :
    -   Appuyez sur le bouton **[<img src=images/Sketcher_Split.svg style="width:16px"> [Diviser une arête](Sketcher_Split/fr.md)**.
    -   Sélectionnez l\'option **Esquisse → Outils d'esquisse → <img src="images/Sketcher_Split.svg" width=16px> Diviser une arête** du menu.
    -   Utilisez le raccourci clavier : **G** puis **Z**.
2.  S\'il y a une précédente sélection, elle est effacée. L\'outil n\'accepte pas de présélection.
3.  Le curseur se transforme en croix avec l\'icône de l\'outil.
4.  Cliquez sur une arête à l\'endroit où elle doit être divisée.
5.  Si l\'arête d\'origine est une ligne ou une courbe ouverte, deux nouvelles arêtes sont créées et reliées par une [contrainte de coïncidence](Sketcher_ConstrainCoincident/fr.md). Pour les courbes fermées, une nouvelle courbe ouverte est créée, le nouveau point ne reçoit alors pas de contrainte de coïncidence. Les contraintes existantes applicables sont transférées à la/aux nouvelle(s) arête(s). Voir [Remarques](#Remarques.md).
6.  Cet outil fonctionne toujours en mode continu : il est possible de continuer à diviser les arêtes.
7.  Pour terminer, cliquez dans une zone vide de la [vue 3D](3D_view/fr.md), cliquez avec le bouton droit de la souris ou appuyez sur **Échap**, ou démarrez un autre outil de création de géométrie ou de contrainte.



## Remarques

-   Une contrainte de [coïncidence](Sketcher_ConstrainCoincident/fr.md) est appliquée aux centres des nouveaux arcs.
-   Les contraintes de [rayon](Sketcher_ConstrainRadius/fr.md) et de [diamètre](Sketcher_ConstrainDiameter/fr.md) sont copiées sur les nouveaux arcs (ce qui entraîne une redondance).
-   Les contraintes de coïncidence et les contraintes [Point sur l\'objet](Sketcher_ConstrainPointOnObject/fr.md) sont transférées sur la nouvelle arête la plus proche.
-   Les contraintes [horizontales](Sketcher_ConstrainHorizontal/fr.md) et [verticales](Sketcher_ConstrainVertical/fr.md) entre les points sont transférées vers la nouvelle arête la plus proche.
-   Les contraintes horizontales et verticales attachées aux lignes sont copiées sur les nouveaux segments de ligne.
-   Les contraintes [parallèles](Sketcher_ConstrainParallel/fr.md) et [perpendiculaire](Sketcher_ConstrainPerpendicular/fr.md) sont copiées sur les nouveaux segments de ligne, pour les nouveaux arcs, elles sont seulement copiées sur les plus proches.
-   Les contraintes de [distance horizontale](Sketcher_ConstrainDistanceX/fr.md), [distance verticale](Sketcher_ConstrainDistanceY/fr.md) et [distance](Sketcher_ConstrainDistance/fr.md) sont transférées vers la nouvelle arête la plus proche.
-   Les contraintes d\'[angle](Sketcher_ConstrainAngle/fr.md), de [symétrie](Sketcher_ConstrainSymmetric/fr.md) et de [blocage](Sketcher_ConstrainBlock/fr.md) ne sont actuellement pas transférées.



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher Split/fr
