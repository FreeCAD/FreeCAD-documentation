---
- TutorialInfo:/fr
   Topic:Ship Workbench
   Level: Beginner
   Time:
   Author:
   FCVersion:
   Files:
---

# FreeCAD-Ship s60 tutorial (II)/fr





## Présentation

Avant de commencer ce didacticiel, veuillez vous assurer que vous avez déjà effectué [la première partie](FreeCAD-Ship_s60_tutorial/fr.md).

Pour en savoir plus sur l\'atelier Ship, consultez la page wiki qui lui est consacrée : [atelier Ship](Ship_Workbench/fr.md).

## Introduction

Dans ce tutoriel, nous allons travailler avec des poids et des réservoirs afin de calculer la courbe GZ, le paramètre de stabilité hydrostatique le plus important. GZ est le moment statique généré lorsque le navire prend un angle de roulis, bien sûr, puisque le bras GZ est positif, le navire a un moment positif et tentera de reprendre sa position verticale. Cependant, lorsque GZ tourne sur des nombres négatifs, la stabilité du navire n\'est plus, provoquant une situation critique.

IMO - International Maritime Organization (Organisation maritime internationale) a défini les critères suivants:

-   *GM* \>= 0.15 m. *GM* (metacentric height) hauteur métacentrique est la tangente initiale de la courbe *GZ*
-   La valeur maximale *GZ* doit être placée sur plus de 30 degrés d\'angle de roulis.
-   Avec un angle de roulis de 30 degrés, la valeur *GZ* doit être d\'au moins 0,2 m.
-   La zone concernée par la courbe *GZ* avec un angle de roulis maximal de 40 degrés doit être d\'au moins 0,090 m · rad.
-   La zone concernée par la courbe en *GZ* avec un angle de roulis inférieur à 30 degrés doit être d\'au moins 0,055 m · rad.
-   La zone concernée par la courbe \"GZ\" entre 30 et 40 degrés d\'angle de roulis doit être d\'au moins 0,030 m · rad.

Dans ce tutoriel, nous allons régler les poids et les réservoirs de notre bateau de la série 60, dans une situation simulée.

## Poids des navires 

Afin de pouvoir calculer la courbe GZ, nous devons connaître les poids des navires et leur position à chaque angle de roulis. Les poids seront donc divisés en deux catégories:

-   Des poids fixes, entièrement liés aux mouvements des navires.
-   Les réservoirs, où la forme du fluide change avec l'angle, nécessitent un calcul du centre de gravité à chaque position.

L\'atelier Ship fournit deux outils différents pour générer chaque instance.

![Weights definition tool icon.](images/FreeCAD-Ship-WeightIco.png )


<center>

Icône de l\'outil de définition des poids.


</center>

L\'outil de définition des poids peut être utilisé pour définir la première catégorie de poids. Lorsque vous lancez l\'outil pour la première fois (avec l\'instance de bateau sélectionnée), l\'atelier Ship initialise les poids du bateau avec un bateau léger (égal au déplacement du bateau) qui est placé sur la coordonnée X du centre de gravité de la géométrie du bateau, et à la hauteur du tirant d\'eau de conception. En général, il existe au moins deux poids pertinents :

-   Structure.
-   Moteur principal (ou plusieurs).

Donc nous allons le changer. En double-cliquant sur chaque cellule, nous pouvons modifier la valeur en définissant les pondérations suivantes:

-   Structure, 15000 kg, (-0.1, 0, 1.25) m
-   Moteur tribord, 5000 kg, (-6.5, -0.65, 0.5) m
-   Moteur côté bâbord, 5000 kg, (-6.5, 0.65, 0.5) m
-   Moteur de secours, 2500 kg, (0.2, 0, 2.5) m

![Aperçu 3D de Définition des poids.](images/FreeCAD-Ship-S60WeightsPreview.png )


<center>

Aperçu 3D de Définition des poids.


</center>

La position des poids est indiquée dans la [Vue 3D](3D_view/fr.md). Remarque : les annotations seront supprimées lorsque l\'outil sera fermé. Lorsque vous appuyez sur **Accept**, les poids seront enregistrés dans votre instance de bateau.

## Réservoirs

Les réservoirs doivent être créés au-dessus d\'une géométrie solide, comme l\'instance du bateau, donc la première étape consiste à créer deux réservoirs d\'étrave (un par côté du bateau) des géométries solides que nous allons considérer (généralement les bateaux ont beaucoup de réservoirs pour le carburant, l\'eau douce, l\'eau salée, le chargement, etc).

### Génération de la géométrie 

Afin de générer des réservoirs, nous chargeons [l\'atelier Part](Part_Workbench/fr.md) et créons un solide.

Nous devons modifier la boîte, donc nous la sélectionnons dans l\'arborescence **Attributes and tags**, et nous passons de la vue à l\'onglet Données. Développez Placement, et à l\'intérieur Position, et définissez *x* à 1.5, et z à -1. Nous voulons également modifier la longueur de la boîte en la changeant pour 5.0 (notez que les unités peuvent être en mm, n\'y prêtez pas attention).

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

Maintenant nous pouvons sélectionner **StarboardTankGeom** et exécuter l\'outil de génération d\'instance de réservoir, où certaines données doivent être fournies. Nous définirons 40% du niveau de remplissage et 925 kg/m $\mathrm{m}^{3}$ (approche carburant). Lorsque vous cliquez sur **Accept**, une nouvelle instance de réservoir appelée **Tank** est générée. Nous pouvons la renommer en **StarboardTank** et masquer **StarboardTankGeom**.

Nous pouvons répéter le même processus afin de générer **PortTank**.

![Vue des poids générés.](images/FreeCAD-Ship-S60WeightsTanksPreview.png )


<center>

Vue des poids générés.


</center>

La figure montre le résultat de notre navire que nous allons calculer.

### Calcul de la courbe GZ 

L\'atelier Ship fournit un outil permettant de calculer facilement une courbe \"GZ\".

<img alt="Icône de l\'outil de calcul de courbe GZ." src=images/Ship_GZ.svg  style="width:128px;">


<center>

Icône de l\'outil de calcul de courbe GZ.


</center>

Avec l\'instance **Ship** sélectionnée, nous pouvons exécuter l\'outil. La première chose que nous pouvons voir dans la boîte de dialogue ouverte est une liste de toutes les instances de réservoir trouvées dans le document actif. Nous voulons utiliser les deux, donc nous cliquons sur les réservoirs remarqués avec un arrière-plan différent.

Pour connaître le déplacement et le tirant d\'eau résultants du navire, nous pouvons appuyer sur **Actualiser le déplacement et le tirant d\'eau**, en prenant un peu de temps pour le calcul. Nous recevons les données suivantes:

-   Déplacement = 37505.5 kg
-   Tirant d\'eau = 0.818664 m

Nous sommes donc dans une situation non chargée, où le tirant d\'eau est nettement plus bas que le tirant d\'eau initial. Des tirants d\'eau plus bas impliquent généralement une stabilité moindre du navire. Le tirant d\'eau dépend des conditions de chargement. Par conséquent, si nous nous attendons vraiment à ce qu\'un navire puisse être utilisé dans ces conditions de chargement, nous pouvons envisager de mettre en place des citernes à ballast.

Nous pouvons également calculer automatiquement l\'assiette du navire, opération qui peut prendre environ une minute, en récupérant que notre navire présente un angle d\'assiette de 0,95 degré (positif par la poupe). Dans cet exemple, nous allons travailler sans angle de découpe (0 degré).

La demande de l\'outil prend également en compte les angles de roulis. Dans ce cas, nous voulons connaître tous les comportements du navire afin de pouvoir définir:

-   Angle de roulis de départ de 0 degrés.
-   Angle de roulis final de 180 degrés.
-   46 points. Un pour chaque intervalle de 2 degrés. Le calcul de GZ peut prendre un certain temps, alors tenez compte du nombre de points demandé.

Lorsque nous appuyons sur **Accept**, l\'outil commence le calcul. Si vous exécutez FreeCAD depuis le terminal, vous pouvez voir la progression du travail. Dans quelques secondes, nous recevrons la courbe GZ.

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

La valeur maximale de *GZ* est placée à plus de 30 degrés (45 degrés), soit 0,25 m à 30 degrés (0,2 m est le minimum). Jusqu\'à 30 degrés, la surface au-dessous de la courbe \"GZ\" est de 0,065 m.rad, et jusqu\'à 40 degrés, nous avons 0,092 m.rad, soit la zone comprise entre 30 et 40 degrés de 0,027 m.rad. Donc, notre navire ne répond pas aux exigences de l'OMI. La solution est de placer des réservoirs de ballast.

D\'autre part, le bateau dans cette mauvaise condition a des valeurs positives *GZ* jusqu\'à 95 degrés d\'angle de roulis, mais n\'a pas été suffisant pour les exigences de stabilité de l\'OMI, montrant les critères difficiles imposés sur ce point.

Bien entendu, cet exemple n'est pas réel (d'abord, tous les réservoirs de carburant ne peuvent pas être placés dans la structure à double fond ni dans le côté de la coque), mais constituent un bon exemple pour apprendre à utiliser l\'[atelier Ship](Ship_Workbench/fr.md) .


{{Ship Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Ship](Category_Ship.md) > FreeCAD-Ship s60 tutorial (II)/fr
