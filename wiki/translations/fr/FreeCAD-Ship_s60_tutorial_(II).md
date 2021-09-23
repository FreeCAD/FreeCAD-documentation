# FreeCAD-Ship s60 tutorial (II)/fr
{{TutorialInfo/fr
|Topic=Ship Workbench
|Level= Beginner
|Time=
|Author=
|FCVersion=
|Files=
}}

## Overview

Avant de commencer ce didacticiel, veuillez vous assurer que vous avez déjà effectué [la première partie](FreeCAD-Ship_s60_tutorial/fr.md).


<div class="mw-translate-fuzzy">

Vous pouvez en apprendre plus sur[FreeCAD-Ship ici](Ship_Workbench/fr.md)


</div>

## Introduction

Dans ce tutoriel, nous allons travailler avec des poids et des réservoirs afin de calculer la courbe GZ, le paramètre de stabilité hydrostatique le plus important. GZ est le moment statique généré lorsque le navire prend un angle de roulis, bien sûr, puisque le bras GZ est positif, le navire a un moment positif et tentera de reprendre sa position verticale. Cependant, lorsque GZ tourne sur des nombres négatifs, la stabilité du navire n\'est plus, provoquant une situation critique.

IMO - International Maritime Organization (Organisation maritime internationale) a défini les critères suivants:

-   *GM* \>= 0.15 m. *GM* (metacentric height) hauteur métacentrique est la tangente initiale de la courbe *GZ*
-   La valeur maximale *GZ* doit être placée sur plus de 30 degrés d\'angle de roulis.
-   Avec un angle de roulis de 30 degrés, la valeur *GZ* doit être d\'au moins 0,2 m.
-   La zone concernée par la courbe *GZ* avec un angle de roulis maximal de 40 degrés doit être d\'au moins 0,090 m · rad.
-   La zone concernée par la courbe en *GZ* avec un angle de roulis inférieur à 30 degrés doit être d\'au moins 0,055 m · rad.
-   La zone concernée par la courbe \"GZ\" entre 30 et 40 degrés d\'angle de roulis doit être d\'au moins 0,030 m · rad.


<div class="mw-translate-fuzzy">

Dans ce didacticiel, nous allons définir des poids et des réservoirs pour notre navire de la série 60, dans une situation irréelle.


</div>

## Poids des navires 

Afin de pouvoir calculer la courbe GZ, nous devons connaître les poids des navires et leur position à chaque angle de roulis. Les poids seront donc divisés en deux catégories:

-   Des poids fixes, entièrement liés aux mouvements des navires.
-   Les réservoirs, où la forme du fluide change avec l'angle, nécessitent un calcul du centre de gravité à chaque position.


<div class="mw-translate-fuzzy">

FreeCAD-Ship fournit deux outils différents pour générer chaque instance.


</div>

![Weights definition tool icon.](images/FreeCAD-Ship-WeightIco.png )


<center>

Icône de l\'outil de définition des poids.


</center>


<div class="mw-translate-fuzzy">

L\'outil de définition des poids peut être utilisé pour définir la première catégorie de poids. Lorsque vous lancez l\'outil pour la première fois (avec l\'instance de navire sélectionnée), FreeCAD-Ship initialise les poids du navire avec Navire léger (égal au déplacement du navire) placé à la coordonnée X du centre de gravité de la géométrie du navire et à la hauteur de consigne. Habituellement, vous avez au moins 2 poids pertinents:

-   Structure.
-   Moteur principal (ou plusieurs d\'entre eux).


</div>


<div class="mw-translate-fuzzy">

Donc nous allons le changer. En double-cliquant sur chaque cellule, nous pouvons modifier la valeur en définissant les pondérations suivantes:

-   Structure, 15000 kg, (-0.1, 0, 1.25) m
-   Moteur tribord, 5000 kg, (-6.5, -0.65, 0.5) m
-   Moteur côté bâbord, 5000 kg, (-6.5, 0.65, 0.5) m
-   Moteur de secours, 2500 kg, (0.2, 0, 2.5) m


</div>

![Aperçu 3D de Définition des poids.](images/FreeCAD-Ship-S60WeightsPreview.png )


<center>

Aperçu 3D de Définition des poids.


</center>


<div class="mw-translate-fuzzy">

La position des poids est affichée en vue 3D. Ces annotations seront supprimées lorsque vous terminerez avec l\'outil, alors ne faites pas attention à cela. Lorsque vous appuyez sur **Accepter**, les poids seront stockés dans votre instance de navire.


</div>


<div class="mw-translate-fuzzy">

## Réservoirs

Les réservoirs doivent être créés au-dessus de la géométrie solide, comme dans l\'exemple du navire. La première étape consiste à créer deux réservoirs d\'étrave (un par côté du navire). Des géométries solides que nous prendrons en compte (les navires ont généralement beaucoup de réservoirs pour le carburant, l\'eau douce, l\'eau salée, charge, etc.).


</div>

### Génération de la géométrie 

Afin de générer des réservoirs, nous chargeons [l\'atelier Part](Part_Workbench/fr.md) et créons un solide.


<div class="mw-translate-fuzzy">

Nous devons éditer la boîte, nous la sélectionnons donc dans l\'arborescence **Attributs et balises**, et passons de l\'onglet Affichage à l\'onglet Données. Décompressez Placement, et à l\'intérieur Position, et définissez *x* sur 1,5, et z sur -1. Nous voulons changer la longueur de la boîte et la changer pour 5.0 (notez que les unités peuvent être en mm, ne vous en occupez pas).


</div>

La géométrie du réservoir fait partie intégrante de la géométrie de boîte et de navire créée. Vous pouvez ainsi masquer l\'instance **Ship**, et afficher la géométrie **s60\_IowaUniversity**. En sélectionnant la case et **s60\_IowaUniversity**, nous pouvons utiliser l\'opération commune générant la géométrie de notre réservoir tribord.

![Géométrie de réservoir générée.](images/FreeCAD-Ship-S60TankGeometry.png )


<center>

Géométrie de réservoir générée.


</center>

Nous pouvons effectuer une opération à bâbord en sélectionnant notre géométrie tribord et en exécutant l'outil miroir, en sélectionnant XZ comme plan miroir.

Afin de convertir la géométrie en une forme solide habituelle de nos réservoirs et de récupérer notre géométrie **s60\_IowaUniversity**, nous pouvons charger [l\'atelier Draft](Draft_Workbench/fr.md), et avec la géométrie du réservoir tribord sélectionnée, exécuter Mettre à jour, puis répéter avec la géométrie du réservoir latéral. Nous pouvons renommer les géométries en:

-   StarboardTankGeom
-   PortTankGeom

Nous pouvons supprimer la boîte créée, dont nous n'avons plus besoin.

### Génération d\'intances de réservoir 

Si vous rechargez [l\'atelier FreeCAD-Ship](Ship_Workbench/fr.md) une autre fois, nous pouvons trouver un outil générateur d\'instances de réservoir.

![Icône d\'outil de génération d\'instance de réservoir.](images/FreeCAD-Ship-TankIco.png )


<center>

Icône d\'outil de génération d\'instance de réservoir.


</center>


<div class="mw-translate-fuzzy">

Nous pouvons maintenant sélectionner **StarboardTankGeom** et exécuter l\'outil de génération d\'instance de réservoir, où certaines données doivent être fournies. Nous définirons 40% du niveau de remplissage et 925 kg/m $\mathrm{m}^{3}$ (approche carburant). Lorsque vous cliquez sur \"Accepter\", une nouvelle instance de réservoir appelée **Réservoir** est générée. Nous pouvons la renommer en **StarboardTank** et masquer **StarboardTankGeom**.


</div>

Nous pouvons répéter le même processus afin de générer **PortTank**.

![Vue des poids générés.](images/FreeCAD-Ship-S60WeightsTanksPreview.png )


<center>

Vue des poids générés.


</center>

La figure montre le résultat de notre navire que nous allons calculer.


<div class="mw-translate-fuzzy">

### Calcul de la courbe GZ 

FreeCAD-Ship fournit un outil permettant de calculer facilement une courbe \"GZ\".


</div>

<img alt="Icône de l\'outil de calcul de courbe GZ." src=images/Ship_GZ.svg  style="width:128px;">


<center>

Icône de l\'outil de calcul de courbe GZ.


</center>


<div class="mw-translate-fuzzy">

Avec l\'instance **Ship** sélectionnée, nous pouvons exécuter l\'outil. La première chose que nous pouvons voir dans la boîte de dialogue ouverte est une liste de toutes les instances de réservoir trouvées dans le document actif. Nous voulons utiliser les deux, donc nous cliquons sur les réservoirs remarqués avec un arrière-plan différent.


</div>

Pour connaître le déplacement et le tirant d\'eau résultants du navire, nous pouvons appuyer sur **Actualiser le déplacement et le tirant d\'eau**, en prenant un peu de temps pour le calcul. Nous recevons les données suivantes:

-   Déplacement = 37505.5 kg
-   Tirant d\'eau = 0.818664 m


<div class="mw-translate-fuzzy">

Nous sommes donc dans une situation non chargée, où le tirant d\'eau est nettement plus bas que le tirant d\'eau initial. Des tirants d\'eau plus bas impliquent généralement une stabilité moindre du navire. Le tirant d\'eau dépend des conditions de chargement. Par conséquent, si nous nous attendons vraiment à ce qu\'un navire puisse être utilisé dans ces conditions de chargement, nous pouvons envisager de mettre en place des citernes à ballast.


</div>

Nous pouvons également calculer automatiquement l\'assiette du navire, opération qui peut prendre environ une minute, en récupérant que notre navire présente un angle d\'assiette de 0,95 degré (positif par la poupe). Dans cet exemple, nous allons travailler sans angle de découpe (0 degré).

La demande de l\'outil prend également en compte les angles de roulis. Dans ce cas, nous voulons connaître tous les comportements du navire afin de pouvoir définir:

-   Angle de roulis de départ de 0 degrés.
-   Angle de roulis final de 180 degrés.
-   46 points. Un pour chaque intervalle de 2 degrés. Le calcul de GZ peut prendre un certain temps, alors tenez compte du nombre de points demandé.


<div class="mw-translate-fuzzy">

Lorsque nous appuyons sur l\'outil **Accepter**, le calcul démarre. Si vous utilisez FreeCAD depuis un terminal, vous pouvez voir l'avancement des travaux. Dans quelques secondes, nous recevrons la courbe GZ.


</div>

Cet outil utilise également [pyxplot](http://www.pyxplot.org.uk/) et [ghostscript](http://www.ghostscript.com/). Vous pouvez voir où le fichier de sortie **gz.dat** a été placé dans la vue du rapport (Vue/Vues/Rapport), et le charger avec le logiciel de feuille de données (par exemple, [libreOffice](http://www.libreoffice.org)). A proximité du fichier de données, plusieurs fichiers auxiliaires ont également été créés:

-   **gz.dat**: Données de courbe GZ calculées.
-   **gz.pyxplot**: pyxplot layout in order to plot the curve.
-   **gz.eps**: Version d\'image EPS.
-   **gz.png**: Version d\'image PNG.

Ces fichiers seront écrasés si vous exécutez l\'outil une autre fois.

### Résultats

<img alt="Courbe résultante GZ." src=images/FreeCAD-Ship-s60GZ.png  style="width:800px;">


<center>

Courbe résultante GZ.


</center>


<div class="mw-translate-fuzzy">

La valeur maximale de *GZ* est placée à plus de 30 degrés (45 degrés), soit 0,25 m à 30 degrés (0,2 m est le minimum). Jusqu\'à 30 degrés, la surface au-dessous de la courbe \"GZ\" est de 0,065 m.rad, et jusqu\'à 40 degrés, nous avons 0,092 m.rad, soit la zone comprise entre 30 et 40 degrés de 0,027 m.rad. Donc, notre navire ne répond pas aux exigences de l'OMI. La solution est de placer des réservoirs de ballast.


</div>


<div class="mw-translate-fuzzy">

D\'autre part, le navire, dans ce mauvais état, a une valeur positive de *GZ* pouvant atteindre un angle de roulis allant jusqu\'à 95 degrés, mais n\'a pas été respecté pour les exigences de stabilité de l\'OMI, ce qui montre les conditions rigoureuses imposées à cet article.


</div>


<div class="mw-translate-fuzzy">

Bien entendu, cet exemple n'est pas réel (d'abord, tous les réservoirs de carburant ne peuvent pas être placés dans la structure à double fond ni dans le côté de la coque), mais constituent un bon exemple pour apprendre à utiliser [FreeCAD-Ship](Ship_Workbench/fr.md) .


</div>


{{Ship Tools navi

}}

---
[documentation index](../README.md) > FreeCAD-Ship s60 tutorial (II)/fr
