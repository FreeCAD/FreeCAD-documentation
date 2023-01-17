---
- GuiCommand:/fr
   Name:Sketcher CreatePeriodicBSpline
   Name/fr:Sketcher B-spline périodique
   MenuLocation:Esquisse → Géometries d'esquisse → Créer une B-spline périodique
   Workbenches:[Sketcher](Sketcher_Workbench/fr.md)
   Shortcut:**G** **B** **P**
   Version:0.17
   SeeAlso:[Sketcher B-spline simple](Sketcher_CreateBSpline/fr.md)
---

# Sketcher CreatePeriodicBSpline/fr

## Description

Cet outil trace une courbe B-spline périodique (fermée) à partir de ses points de contrôle. (Voir [cette page](B-Splines/fr.md) pour plus d\'informations sur les B-splines).

![](images/Sketcher_Periodic_B-spline_example01.png )



*Une courbe B-spline périodique (en blanc) composée de 5 points. Sur la photo, le polygone de contrôle en vert (les lignes droites reliant les points rouges), les cercles de poids en bleu et le peigne de courbure en vert. Le chiffre (3) au centre fait référence au degré de la spline B et les chiffres (1) et (2) des nœuds situés sur la courbe font référence à leur multiplicité.*



## Utilisation

1.  Appuyez sur le bouton **[<img src=images/Sketcher_CreatePeriodicBSpline.svg style="width:16px"> [Créer une B-spline périodique](Sketcher_CreatePeriodicBSpline/fr.md)**.
2.  Créez une série de points en cliquant dans la [vue 3D](3D_view/fr.md). Lorsque la commande est active, les points créés sont reliés par des lignes droites et un cercle de construction est créé au centre de chaque point.
3.  Vous pouvez appuyer sur **D** avant de terminer l\'entrée pour définir le degré du B-Spline. {{Version/fr|0.20}}
4.  Vous pouvez appuyer sur **Retour arrière** avant de terminer l\'entrée pour supprimer le dernier point de contrôle créé. {{Version/fr|0.20}}
5.  Cliquez sur le premier point, ou faites un clic-droit avec la souris pour terminer la saisie et générer la courbe.
6.  Selon les préférences, l\'outil peut rester actif pour tracer une nouvelle courbe. Cliquez à nouveau avec le bouton droit pour quitter la commande.

-   Il est possible de définir le poids des points de contrôle en modifiant les rayons des cercles. Les contraintes d\'égalité sur les cercles doivent d\'abord être supprimées. La valeur de la contrainte radiale est arbitraire, le poids des points de contrôle sera défini par les rayons relatifs des cercles. Son fonctionnement est similaire à celui de la gravité: plus un cercle est grand par rapport aux autres, plus la courbe sera attirée par le point de contrôle.
-   La visibilité du polygone de contrôle, du peigne de courbure, du degré et de la multiplicité des nœuds peut être activée/désactivée à partir de la barre des [outils B-spline](Sketcher_Workbench/fr#Outils_d.27esquisse_B-spline.md).
-   Consultez les autres outils de la barre des [outils B-spline](Sketcher_Workbench/fr#Outils_d.27esquisse_B-spline.md) pour plus d'outils d'édition des B-splines.

## Limitations

-   De nombreux types de contraintes ne sont pas pris en charge pour le moment. Seuls les points de contrôle et les nœuds de la B-spline peuvent être contraints.
-   Les outils [ajuster l\'arête](Sketcher_Trimming/fr.md) et [prolonger l\'arête](Sketcher_Extend/fr.md) ne sont pas pris en charge.
-   La forme d\'une courbe B-spline ne peut être modifiée qu\'en faisant glisser l\'un des points de contrôle. Les nœuds situés sur la courbe ne peuvent pas être sélectionnés.





{{Sketcher_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CreatePeriodicBSpline/fr
