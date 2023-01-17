---
- GuiCommand:/fr
   Name:Sketcher Split
   Name/fr:Sketcher Diviser
   MenuLocation:Sketch → Géométries d'esquisse → Diviser une arête
   Workbenches:[Sketcher](Sketcher_Workbench/fr.md)
   Shortcut:**G** **Z**
   Version:0.20
   SeeAlso:[Sketcher Ajuster](Sketcher_Trimming/fr.md)
---

# Sketcher Split/fr

## Description

Cet outil scinde une arête en deux, les contraintes applicables existantes étant copiées sur la nouvelle arête. La position du point où les arêtes se rencontrent n\'est pas contrainte. Les courbes périodiques (c\'est-à-dire les cercles, les ellipses et les B-splines périodiques) sont converties en courbes non périodiques (respectivement des arcs de cercles, des arcs d\'ellipses et des B-splines non périodiques).

![](images/SketcherSplitExample1.png ) ![](images/SketcherSplitExample2.png ) ![](images/SketcherSplitExample3.png )



## Utilisation

1.  Appuyez sur le bouton **[<img src=images/Sketcher_Split.svg style="width:16px"> [Diviser une arête](Sketcher_Split/fr.md)**. Le pointeur de la souris se transforme en une croix blanche avec un symbole de division rouge.
2.  Cliquez sur l\'arête à l\'endroit où vous voulez la diviser.
3.  À partir des arêtes de ligne et d\'arc, deux nouvelles arêtes seront créées, reliées au point cliqué. Un cercle est converti en arc avec le même point central et les mêmes contraintes que le cercle original.
4.  Appuyez sur **Echap** ou sur le bouton droit de la souris pour terminer la fonction.

## Limitations

-   Dans la {{VersionMinus/fr|0.20}}, l\'action n\'est pas prise en charge pour les ellipses, les paraboles, les hyperboles et les B-splines.



## Remarques

-   Toutes les coïncidences sont transférées - point de départ, point d\'arrivée et point central (le cas échéant).
-   La contrainte du point sur l\'objet est transférée à l\'arête la plus proche nouvellement créée.
-   Les contraintes verticales et horizontales sont copiées sur les deux nouveaux segments.
-   Les contraintes parallèles et perpendiculaires sont copiées pour les deux segments de ligne, pour l\'arc une seule fois, vers la partie la plus proche.
-   La contrainte d\'égalité n\'est transférée que pour les arêtes de l\'arc résultant, les segments de ligne ne la reçoivent pas.
-   La contrainte de symétrie n\'est actuellement pas transférée.
-   La contrainte de bloc n\'est pas transférée actuellement.
-   Les contraintes horizontales, verticales et de longueur entre les points sont transférées aux points extérieurs des nouvelles arêtes.
-   La contrainte de distance entre points n\'est attribuée qu\'une seule fois, au segment d\'arête le plus proche.
-   Les contraintes de rayon et de diamètre sont copiées sur tout arc résultant.
-   La contrainte d\'angle n\'est actuellement pas transférée.





{{Sketcher_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher Split/fr
