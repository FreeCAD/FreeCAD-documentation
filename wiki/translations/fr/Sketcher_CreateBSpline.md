---
- GuiCommand:/fr
   Name:Sketcher CreateBSpline
   Name/fr:Sketcher Créer B-spline
   MenuLocation: Sketch → Géométries d'esquisse → Créer une B-spline
   Workbenches: [Sketcher](Sketcher_Workbench/fr.md)
   Version:0.17
   SeeAlso:[Sketcher B-spline périodique](Sketcher_CreatePeriodicBSpline/fr.md)
---

## Description

Cet outil crée une courbe B-spline à partir de ses points de contrôle. (Voir [cette page](B-Splines/fr.md) pour plus d\'informations sur les B-splines).

![](images/Sketcher_B-spline_example01.png ) *Une courbe B-spline (en blanc) définie par 4 points de contrôle. On voit le polygone de contrôle en vert (les lignes droites reliant les points de contrôle) et les cercles de poids en jaune foncé. Le chiffre vert "3" au centre fait référence au [degré](Sketcher_BSplineIncreaseDegree/fr#Description.md) de la courbe B-spline et les chiffres "(4)" aux extrémités de la courbe B-spline font référence à leur [multiplicité du nœud](Sketcher_BSplineDecreaseKnotMultiplicity/fr#Description.md). Le chiffre rouge "3" indique le poids du point de contrôle qui est défini comme une contrainte de rayon par rapport au cercle du point de contrôle.*

## Utilisation

1.  Appuyez sur le bouton **<img src=images/Sketcher_CreateBSpline.svg style="width:16px"> [Créer une B-spline](Sketcher_CreateBSpline/fr.md)**.
2.  Créez une série de points en cliquant dans la vue 3D. Lorsque la commande est active, les points créés sont reliés par des lignes droites et un cercle de construction est créé au centre de chaque point.
3.  Cliquez avec le bouton droit pour terminer la saisie et générer la courbe.
4.  Selon les préférences, l\'outil peut rester actif pour tracer une nouvelle courbe. Cliquez à nouveau avec le bouton droit pour quitter la commande.

-   Il est possible de définir le poids des points de contrôle en modifiant les rayons des cercles. Les contraintes d\'égalité sur les cercles doivent d\'abord être supprimées. La valeur de la contrainte radiale est arbitraire, le poids des points de contrôle sera défini par les rayons relatifs des cercles. Son fonctionnement est similaire à celui de la gravité: plus un cercle est grand par rapport aux autres, plus la courbe sera attirée par le point de contrôle.
-   La visibilité du polygone de contrôle, du peigne de courbure, du degré et de la multiplicité des nœuds peut être activée/désactivée à partir de la barre d'outils [Outils d\'esquisse B-spline](Sketcher_Workbench/fr#Sketcher_B-spline_tools.md).
-   Consultez les autres outils de la barre d'outils [Outils d\'esquisse B-spline](Sketcher_Workbench/fr#Sketcher_B-spline_tools.md) pour plus d'outils d'édition B-spline.

## Limitations

-   De nombreux types de contraintes ne sont pas pris en charge pour le moment. Seuls les points de contrôle et les points d\'extrémité de la B-spline peuvent être contraints.
-   Les outils [ajuster l\'arête](Sketcher_Trimming/fr.md) et [prolonger l\'arête](Sketcher_Extend/fr.md) ne sont pas pris en charge.
-   La forme d\'une courbe B-spline ne peut être modifiée qu\'en faisant glisser l\'un des points de contrôle. Les nœuds situés sur la courbe ne peuvent pas être sélectionnés.





{{Sketcher Tools navi

}} 
