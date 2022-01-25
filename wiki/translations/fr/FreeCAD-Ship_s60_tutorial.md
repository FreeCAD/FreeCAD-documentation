---
- TutorialInfo:/fr
   Topic:Atelier Bateau
   Level:Débutant
   Time:
   Author:
   FCVersion:
   Files:
---

# FreeCAD-Ship s60 tutorial/fr





## Introduction


<div class="mw-translate-fuzzy">

Dans ce tutoriel nous allons travailler avec comme exemple le navire \"Series 60\" de l\'université de l\'Iowa. Ce tutoriel montre comment travailler avec un navire à une coque symétrique, mais les multicoques et les coques asymétriques peuvent être traités de la même manière.


</div>


<div class="mw-translate-fuzzy">

Vous pouvez en apprendre plus sur [FreeCAD-Ship ici](Ship_Workbench/fr.md)


</div>

## Charger la forme de base 


<div class="mw-translate-fuzzy">

### Introduction 

FreeCAD-Ship utilise des **Entités Navires (Ship entities)** qui doivent être créées à partir de la forme de base. Cette forme doit être un solide, ou un ensemble de solides. Les pré-requis suivants doivent être respéctés:

-   La forme de la coque doit être intégralement fournie (y compris les parties symétriques).
-   Le côté tribord doit se situer dans les *y* négatifs.
-   Le point d\'origine (0,0,0) est à l\'intersection de la section au milieu du navire (à mi-distance des perpendiculaires avant et arrière) et de la *ligne de base*.


</div>

![Illustration des pré-requis pour la forme de base](images/FreeCAD-Ship-SignCriteria.jpg )


<center>

Illustration des pré-requis pour la forme de base


</center>


<div class="mw-translate-fuzzy">

### Chargement de la géométrie de la série 60 

Afin d\'aider les nouveaux utilisateurs, FreeCAD-Ship comprend un chargeur d\'exemples de géométries, avec le choix suivant:

-   Série 60 de l\'Université d\'Iowa
-   Wigley Canonical Ship
-   Série 60 Catamaran
-   Wigley Catamaran


</div>


<div class="mw-translate-fuzzy">

![Icone de chargement des exemples de formes de navires.](images/FreeCAD-Ship-LoadIco.png )  Icône de chargement d\'Exemples de Géométrie de Bateaux\</ span\>


</div>

En exécutant le menu (Ship design/Load an example ship geometry) une boîte de dialogue apparaît. Sélectionnez **Series 60 from Iowa University** et appuyez sur *OK*. L\'outil charge un nouveau document avec la forme **s60\_IowaUniversity**.


<div class="mw-translate-fuzzy">


**<center>'''Attention avant de continuer!'''</center>
<center>Vous travaillez maintenant avec le fichier exemple d'origine.</center>
<center>Pour préserver l'original intact, vous devez enregistrer votre travail avec un autre nom avant de le modifier</center>**


</div>

## Créer un objet navire 

Pour créer un *objet navire* sélectionnez la forme de base et exécutez l\'outil de création de navire (Ship design/Create a new ship).


<div class="mw-translate-fuzzy">

![Outil création de navire.](images/FreeCAD-Ship-Ico.png )


<center>

Icone de l\'outil création de navire


</center>


</div>


<div class="mw-translate-fuzzy">

La boite de dialogue de Création de navire apparaît, ainsi que des annotations sur la vue 3D. Les annotations disparaitront quand vous fermerez l\'outil, pas d\'inquiétude.


</div>


<div class="mw-translate-fuzzy">

Les principales informations liées au navire doivent alors être saisies (FreeCAD-Ship demande une saisie progressive des données, les opérations de base exigent seulement les informations de base, plus de données deviennent nécessaires quand les opérations deviennent plus compliquées).


</div>

### Données du navire 

Les principales dimensions doivent être saisies ici:

-   Longueur: [Longueur entre perpendiculaires](http://fr.wikipedia.org/wiki/Longueur_entre_perpendiculaires), 25.5 m pour ce navire.
-   Largeur : [Maître bau](http://fr.wikipedia.org/wiki/Ma%C3%AEtre-bau), 3.389 m pour ce navire.
-   Tirant d\'eau: 1.0 m pour ce navire.

![Annotations sur la vue de côté](images/FreeCAD-Ship-S60ShipCreationFront.png )


<center>

Annotations de longueur.


</center>

Couramment, la longueur entre perpendiculaires dépend du tirant d\'eau. Si vous ne connaissez pas la longueur du navire vous pouvez saisir le tirant d\'eau et ajuster la longueur.

![Annotations vue de face](images/FreeCAD-Ship-S60ShipCreationSide.png )


<center>

Annotations largeur .


</center>

Le même procédé vaut pour ajuster la largeur. Notez que la valeur demandée est la largeur totale même si l\'annotation sur la vue 3D n\'est portée que sur la moitié tribord.


<div class="mw-translate-fuzzy">

Quand vous appuyez sur **OK** le programme crée votre nouvel objet navire appelé \"Ship\". Vous pouvez changer le nom dans l\'onglet *Données* (propriété *Label*). Nous n\'avons plus besoin de la forme de base, vous pouvons donc la masquer (selectionner et appuyer sur **espace**).


</div>

![Ship instance icon](images/FreeCAD-Ship-ShipInstance.png )


<center>

Icône exemple de Navire.


</center>


<div class="mw-translate-fuzzy">

À partir de là, vous devez avoir sélectionné \'\'\' Ship \'\'\' avant d\'exécuter un outil FreeCAD-Ship.


</div>


<div class="mw-translate-fuzzy">

## Lignes de dessin 

FreeCAD-Ship fournit un outil qui facilite l\'obtention d\'un plan de lignes à partir du dessin des lignes de navire


</div>


<div class="mw-translate-fuzzy">

![Outline draw tool.](images/FreeCAD-Ship-OutlineDrawIco.png )


<center>

Icône de l\'outil de dessin de lignes


</center>


</div>

Le dessin des lignes est un ensemble de lignes à partir de coupes de section dans les 3 axes, qui afficheront éventuellement la géométrie de la coque dans un plan de lignes. Nous devons fournir les lignes pour les 3 vues suivantes:

-   Plan du corps (à l\'aide des coupes transversales)
-   Plan transparent (en utilisant les coupes longitudinales)
-   Plan à mi-largeur (en utilisant les coupes des lignes de Flottaison)


<div class="mw-translate-fuzzy">

### Coupes transversales 

Habituellement, il faut effectuer 21 sections transversales équidistantes entre perpendiculaires. Pour le faire, FreeCAD fournit un outil automatique pour le faire, il suffit de sélectionner le type de sections *\' Transversales **, aller à la zone** Créer automatiquement*\' et définir le nombres de sections **21** , puis appuyez sur **Créer des sections**.


</div>

![Outline draw transversal sections preview.](images/S60OutlineTransversal.png )


<center>

Aperçu des sections transversales du schéma


</center>


<div class="mw-translate-fuzzy">

Le tableau des sections est rempli, et l\'aperçu des sections intitulé \'\' \'Dessin du Contour\' \'\' s\'affiche. Habituellement, des sections supplémentaires ont été ajoutées à la proue et à la poupe, où des courbures plus complexes sont enregistrées, afin de le faire aller à la fin de la table, et faire **double-clic** sur l\'élément vide pour l\'éditer, en appuyant sur intro pour confirmer. Ajouter les sections suivantes:


</div>


<div class="mw-translate-fuzzy">

-   X~22~ = -12.1125 m
-   X~23~ = 12.1125 m


</div>

Selon la complexité de la géométrie de la coque, l\'aperçu des sections peut prendre un certain temps. Pour supprimer une section, il suffit de la remplir avec un texte vide et appuyez sur Entrée.


<div class="mw-translate-fuzzy">

### Coupes longitudinales 

Deux coupes longitudinales doivent être ajoutées, alors sélectionnez le type de sections **Longitudinale**, allez dans la zone **Créer automatiquement** et définissez le nombres de sections **2** , puis appuyez sur \'\'\'Créer des sections \'\'\'. Le tableau des sections est rempli et l\'aperçu des sections est mis à jour.


</div>


<div class="mw-translate-fuzzy">

### Lignes de Flottaison 

6 lignes de flottaison entre la ligne de base et le traçage de conception doivent être ajoutées, sélectionnez alors le type de sections \'\' \'Waterlines\' \'\', accédez à la zone \'\' \'Créer automatiquement\' \'\' et définissez \'\' \'\' 5 \'\' \'(Z = 0 m ne sera pas considéré, ajoutez-le manuellement si vous en avez besoin), puis appuyez sur \'\' \'Créer des sections\' \'\'. Le tableau des sections est rempli et l\'aperçu des sections est mis à jour.


</div>

Plusieurs lignes d\'eau supplémentaires doivent être ajoutées:

-   Z  6 \</ sub\> = 1,2 m
-   Z  7 \</ sub\> = 1,4 m
-   Z  8 \</ sub\> = 1,6 m
-   Z  9 \</ sub\> = 1,8 m
-   Z  10 \</ sub\> = 2,0 m


<div class="mw-translate-fuzzy">

### Exécuter un Tracer 

Sélectionnez **échelle 1: 100** et appuyez sur **Accepter** pour laisser l\'outil générer les sections 3D dans un nouvel objet.


</div>

![Resultant sections.](images/FreeCAD-Ship-S60Outline3DSections.png )


<center>

Sections résultantes


</center>


<div class="mw-translate-fuzzy">

Pour tracer ces sections, vous pouvez utiliser l\' [ Atelier de mise en plan de dessins](Drawing_Workbench/fr.md):


</div>

![ centre \| Plan de traçage des contours.](images/_FreeCAD-Ship-S60OutlinePlot.png )


<center>

 Traçage des contours.


</center>


<div class="mw-translate-fuzzy">

## Courbe des zones transversales 

Un paramètre hydrodynamique typique de conception de navire est la courbe des zones transversales, qui récupère certains indicateurs sur le comportement de la coque (résistance au remorquage, sécheresse, \...). FreeCAD-Ship fournit un outil simple pour effectuer une courbe de zones transversales.


</div>

![ center \|areas curve tool icon.](images/_FreeCAD-Ship-AreaCurveIco.png )


<center>

 Icône de l\'outil de courbe des zones transversales.


</center>


<div class="mw-translate-fuzzy">

Lorsque l\'outil est exécuté, une boîte de dialogue de tâche est affichée et la surface libre pré-ajoutée est créée à la vue 3D (l\'aperçu de la surface libre sera supprimé lorsque l\'outil sera fini, alors ne vous inquiétez pas pour lui). Dans la boîte de dialogue des tâches, les données d\'entrée et de sortie sont présentes.


</div>


<div class="mw-translate-fuzzy">

### Données d\'entrée 

Le dessin et et l\'orientation (angle de rotation de la Coque et \'\'bordure \'\', positif si le tirant arrière peut augmenter) doit être fourni. Plusieurs courbes de zones peuvent être effectuées, selon les situations de chargement du navire, mais deux parcelles typiques doivent être effectuées:

-   Concevoir une courbe de zones transversales: sans angle de rotation et en utilisant un ébauche de conception, 1,0 m dans ce cas.
-   Courbe maximale des courbes transversales: sans angle de rotation et tirant maximum autorisé, 2,0 m dans ce cas.


</div>


<div class="mw-translate-fuzzy">

### Données de sortie 

Certaines données pertinentes sont affichées en temps réel:

-   **L**: Longueur entre les perpendiculaires, valeur définie lors de la création de l\'exemple du navire.
-   **B**: Largeur sélectionné lors de la création du navire.
-   **T**: projection actuelle au centre du navire.
-   **Trim**: angle de réglage.
-   **T~AP~**: après dessin perpendiculaire.
-   **T~FP~**: avant dessin perpendiculaire.
-   **Displacement**: déplacement de navire (eau salée considérée, diviser par 1,025 afin de connaître le volume déplacé).
-   **XCB**: coordonnée du point central de la flottabilité X (par rapport à la section du centre).


</div>


<div class="mw-translate-fuzzy">

Lorsque le bouton \'\' \'Accepter\' \'\' est pressé, un tracé est effectué (en fonction de la complexité de la géométrie, cela peut prendre un certain temps, vous pouvez voir la progression sur le terminal et arrêter le travail en appuyant sur \'\'\'Ctrl + C \'\'). Lorsque la tâche est terminée, FreeCAD générera un tracé (voir la documentation [ documentation du module de traçage](Plot_Workbench/fr.md)) et une feuille de diffusion (voir le [ Tableau de calcul](Spreadsheet_Workbench/fr.md)).


</div>

<img alt="Design draft transversal areas curve. " src=images/FreeCAD-Ship-s60Areas.png  style="width:800px;">


<center>

Conception du dessin des zones de courbes transversales. 


</center>

Vous pouvez exécuter le dessin maximum des courbes des zones transversales afin de voir les différences (par exemple, vous remarquez que la courbe des zones passe a travers des longueurs perpendiculaires maintenant).

## Hydrostatique

Le calcul hydrostatiques est une étape critique de la conception du navire car il faut connaître les principaux paramètres de stabilité de la coque . Les hydrostatiques de l\'universitaire de l\'Iowa.sont des données obligatoires afin que les certificats de sociétés de classification soient expédiés et reliés aux données de condition de chargement (poids et position de gravité) qui fournissent des données essentielles sur la stabilité du navire. FreeCAD-Ship fournit un outil pour obtenir les principales courbes hydrostatiques (les courbes GZ sont étudiées dans un autre outil).

![ center\|Hydrostatics tool icon.](images/_FreeCAD-Ship-HydrostaticsIco.png )


<center>

 icône de l\'outil Hydrostatiques. 


</center>

Lorsque l\'outil est exécuté, une boîte de dialogue de tâche s\'affiche. Habituellement, les courbes hydrostatiques sont présentées pour chaque angle de coupe, dans ce tutoriel, seul l\'angle de coupe verticale sera considéré (0º), avec un intervalle autour de chaque dessin de condition de chargement. Étant donné que nous ne savons pas quelles conditions de chargement nous pouvons obtenir, nous considérerons presque le contingent de possibilités (Habituellement, pour obtenir autant de résolution que possible, les architectes navals font correspondre l\'intervalle à des projets réalisables).

Nous établissons donc les données suivantes:

-   **Trim** = 0 deg
-   **Minimum Draft** = 0.1 m
-   **Maximum Draft** = 2.0 m
-   **Nombre de points** = 39. Beaucoup de points ou des géométries vraiment complexes impliquent de longs temps de calcul, dans ce cas, environ 1 minute sera être utilisée.


<div class="mw-translate-fuzzy">

Lorsque le bouton \'\' \'Accepter\' \'\' est pressé, les tracées sont effectués (voir la documentation [ documentation du module de traçage](Plot_Workbench/fr.md)) et une feuille de calcul est générée (voir la [ Documentation de la table de calcul](Spreadsheet_Workbench/fr.md).)


</div>

<img alt="Hydrostatics curves." src=images/FreeCAD-Ship-HydrostaticsCurves.png  style="width:800px;">


<center>

Courbes Hydrostatiques. 


</center>


<div class="mw-translate-fuzzy">

## Continuer à apprendre FreeCAD-Ship 

Maintenant, vous êtes prêt à continuer à apprendre [Ship](Ship_Workbench/fr.md), [ Ici](FreeCAD-Ship_s60_tutorial_(II)/fr.md) se trouve le deuxième chapitre du bateau universitaire de l\'Iowa de la Série 60.


</div>

The [FreeCAD Ship s60 tutorial (II)](FreeCAD-Ship_s60_tutorial_(II).md) is the second chapter of Series 60 from Iowa university ship.


{{Ship Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Ship](Category_Ship.md) > FreeCAD-Ship s60 tutorial/fr
