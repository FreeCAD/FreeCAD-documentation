# Basic Sketcher Tutorial/fr



{{TutorialInfo/fr
|Topic= Esquisse
|Level= Débutant
|Time=60 minutes
|Author=[http://freecadweb.org/wiki/index.php?title=User:Drei Drei] et vocx
|FCVersion=0.19
|Files=[https://forum.freecadweb.org/viewtopic.php?f=36&t=43594 Basic Sketcher tutorial updated]
}}

## Introduction

Ce didacticiel vise à présenter au lecteur le flux de travail de base de l\'[Atelier Esquisse](Sketcher_Workbench/fr.md).

L\'<img src=images/PartDesign_Pad.svg style="width:atelier Sketcher](Sketcher_Workbench/fr.md) existe en tant qu \'atelier autonome, il peut donc être utilisé pour dessiner des objets 2D (planaires) génériques. Cependant, il est principalement utilisé en conjonction avec l\'<img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [atelier PartDesign](PartDesign_Workbench/fr.md). Une esquisse fermée est normalement utilisée pour créer une surface ou un profil à extruder dans un solide [PartDesign Corps](PartDesign_Body/fr.md) avec une opération telle que **[16px"> [PartDesign Protrusion](PartDesign_Pad/fr.md)**.

Le lecteur pratiquera:

-   Création d\'une géométrie de construction
-   Création d\'une géométrie réelle
-   Application de contraintes géométriques
-   Application de contraintes de référence
-   Obtention d\'un profil fermé

Pour une description plus approfondie de l\'esquisse, lisez le [Manuel de référence pour Sketcher](Sketcher_reference/fr.md).

![](images/00_Sk01_Sketcher_fully_constrained_final.png ) *Résultat final de l'esquisse avec toute la géométrie entièrement contrainte y compris la géométrie de construction pour le support.*

## Installation

1\. Ouvrez FreeCAD, créez un nouveau document vide avec **Fichier → <img src=images/Std_New.svg style="width:16px"> [Nouveau](Std_New/fr.md)**.

:   1.1. Basculez vers l\'[atelier Sketcher](Sketcher_Workbench/fr.md) depuis le [sélectionneur d\'atelier](Std_Workbench/fr.md) ou le **[menu affichage](Std_View_Menu/fr.md) → Atelier → Sketcher**.

Quelques actions à retenir:

-   Appuyez sur le bouton droit de la souris ou appuyez une fois sur **Echap** sur le clavier pour désélectionner l\'outil actif en mode édition.
-   Pour quitter le mode d\'édition d\'esquisse, appuyez sur le bouton **Fermer** dans le [Panneau des tâches](Task_Panel/fr.md) ou appuyez deux fois sur **Echap** au le clavier.
-   Pour entrer à nouveau en mode édition, double-cliquez sur l\'esquisse dans la <img src=images/Sketcher_EditSketch.svg style="width:vue en arborescence](tree_view/fr.md) ou sélectionnez-la puis cliquez sur **[16px"> [Sketcher Modifier l'esquisse](Sketcher_EditSketch/fr.md)**.

## Création d\'une esquisse 

2\. Cliquez sur **<img src="images/Sketcher_NewSketch.svg‎‎" width=16px> [Créer une nouvelle esquisse](Sketcher_NewSketch/fr.md)**.

:   2.1. Choisissez l\'orientation de l\'esquisse, c\'est-à-dire l\'un des plans de base XY, XZ ou YZ. Choisissez également si vous souhaitez une orientation inversée et un décalage par rapport au plan de base.
:   2.2. Nous utiliserons le plan et les options par défaut.
:   2.3. Cliquez sur **OK** pour commencer à construire l\'esquisse.

Nous sommes maintenant dans le mode d\'édition d\'esquisse. Une fois là, nous sommes en mesure d\'utiliser la majorité des outils de cet atelier.


**Remarque:**

la [vue en arborescence](tree_view/fr.md) basculera en [Panneau des tâches](Task_Panel/fr.md). Dans cette interface, développez la section **Edit controls** et assurez-vous que l\'option **Auto constraints** est activée. D\'autres options peuvent être modifiées, notamment la taille de la grille visible et si nous voulons nous y accrocher. Dans ce tutoriel, nous ne nous accrocherons pas à la grille et nous la cacherons également. Dans d\'autres sections du [Panneau des tâches](Task_Panel/fr.md), vous pouvez également voir quels éléments géométriques et contraintes ont été définis.

<img alt="" src=images/01_Sk01_Sketcher_Task_panel.png  style="width:" height="400px;">


*Partie supérieure du [Panneau des tâches](Task_Panel/fr.md) de l'esquisse.*

## Création de la géométrie 

3\. La géométrie de construction est utilisée pour guider la création d\'une \"vraie\" géométrie. La géométrie réelle sera celle montrée en dehors du mode d\'édition d\'esquisse, tandis que la géométrie de construction ne sera montrée qu\'à l\'intérieur du mode d\'édition. Par conséquent, vous pouvez utiliser autant de géométrie de construction que nécessaire pour créer de vraies formes.

:   3.1. Cliquez sur **<img src="images/Sketcher_ToggleConstruction.svg" width=16px> [Sketcher Basculer en géométrie de construction](Sketcher_ToggleConstruction/fr.md)**. Les éléments géométriques seront désormais dessinés en **Construction mode**.
:   3.2. Cliquez sur **<img src="images/Sketcher_Line.svg" width=16px> [Sketcher Ligne](Sketcher_CreateLine/fr.md)**.
:   3.3. Approchez-vous de l\'origine de l\'esquisse, le point doit être en surbrillance et à l\'approche de votre curseur, l\'icône <img alt="" src=images/Constraint_PointOnPoint.svg  style="width:32px;"> [Sketcher Contrainte de coïncidence](Sketcher_ConstrainCoincident/fr.md) apparaîtra.
:   3.4. Cliquez sur le point puis déplacez le pointeur pour commencer à dessiner une nouvelle ligne à partir de celui-ci. Déplacez le pointeur de sorte que la ligne ait une longueur d\'environ {{Value|30 mm}}. Vous n\'avez pas besoin d\'être très précis dans cette étape. Plus tard, nous définirons la bonne dimension.
:   3.5. Répétez cette procédure quatre fois de plus pour placer les lignes de construction en étoile. Ne vous inquiétez pas trop de leur taille ou de leur position, il suffit de les étendre dans les quatre quadrants.
:   3.6. Maintenant quitter le mode de construction, en cliquant simplement à nouveau sur **<img src=images/Sketcher_ToggleConstruction.svg style="width:16px"> [Sketcher Basculer en géométrie de construction](Sketcher_ToggleConstruction/fr.md)**.


**Remarque 1:**

jusqu\'à présent, l\'outil [Sketcher Ligne](Sketcher_CreateLine/fr.md) est toujours actif. Cela signifie que nous pouvons continuer à cliquer dans la [vue 3D](3D_view/fr.md) pour dessiner autant de lignes que nous voulons. Si nous souhaitons quitter cet outil, nous pouvons appuyer sur le bouton droit de la souris ou appuyer une fois sur **Echap** sur le clavier. En faisant cela, le pointeur ne créera plus de lignes, ce sera juste un pointeur nous permettant de sélectionner les objets que nous venons de créer. Dans ce mode pointeur, nous pouvons sélectionner et faire glisser les extrémités de chaque ligne pour ajuster son placement.


**Remarque 2:**

n\'appuyez pas sur **Echap** une deuxième fois car cela ferait quitter le mode d\'édition d\'esquisse. Si vous faites cela, entrez de nouveau dans le mode d\'édition en double-cliquant sur l\'esquisse dans la [vue en arborescence](tree_view/fr.md).

Jetez à nouveau un œil au [Panneau des tâches](Task_Panel/fr.md). La section **Solver messages** indique déjà que l\'esquisse est sous-contrainte et mentionne le nombre de **degrés de liberté**.

Consultez les sections **Constraints** et **Elements** pour voir les nouvelles contraintes et lignes répertoriées. Une fois que vos esquisses contiennent plusieurs éléments, il peut être difficile de les sélectionner dans la [vue 3D](3D_view/fr.md). Vous pouvez donc utiliser ces listes pour sélectionner l\'objet que vous souhaitez exactement.

<img alt="" src=images/02_Sk01_Sketcher_construction.png  style="width:" height="400px;">


*Lignes de construction formant une étoile avec son centre à l'origine.*

## Géométrie réelle 

La géométrie réelle doit créer une forme fermée si elle doit être utilisée comme un profil pouvant être extrudé par des outils tels que **<img src=images/PartDesign_Pad.svg style="width:16px"> [PartDesign Protrusion](PartDesign_Pad/fr.md)**.

Assurez-vous que vous n\'êtes pas en mode construction en cliquant sur **<img src=images/Sketcher_ToggleConstruction.svg style="width:16px"> [Basculer la construction](Sketcher_ToggleConstruction/fr.md)**, si vous n\'avez pas déjà quitté ce mode.

### Les arcs extérieurs 

4\. Créez un cercle.

:   4.1. Cliquez sur **<img src=images/Sketcher_Circle.svg style="width:16px"> [Sketcher Cercle](Sketcher_CreateCircle.md)**.
:   4.2. Cliquez sur **origine** de l\'esquisse pour positionner son point central.
:   4.3. Cliquez n\'importe où dans la [vue 3D](3D_view/fr.md) pour définir le rayon de circonférence comme distance par rapport à l\'origine. Faites-le d\'environ {{Value|8 mm}}. Encore une fois, la dimension sera fixée ultérieurement.

5\. Créez une série d\'arcs.

:   5.1. Cliquez sur **<img src=images/Sketcher_Arc.svg style="width:16px"> [Sketcher Créer un arc...](Sketcher_CreateArc/fr.md)**.
:   5.2. Approchez-vous de l\'extrémité de l\'une des lignes de construction et cliquez dessus. Cela définira le point central de l\'arc circulaire sur <img alt="" src=images/Constraint_PointOnPoint.svg  style="width:32px;"> [coincidant](Sketcher_ConstrainCoincident/fr.md) avec l\'extrémité de cette ligne.
:   5.3. Cliquez une fois dans la [vue 3D](3D_view/fr.md) à un emplacement arbitraire pour définir simultanément le rayon de l\'arc et son premier point final. Définissez un rayon approximatif de {{Value|8 mm}}.
:   5.4. Déplacez le pointeur dans le sens inverse des aiguilles d\'une montre pour tracer un arc dont la concavité pointe vers l\'origine de l\'esquisse. Cliquez pour définir le point final de l\'arc, en définissant un arc circulaire qui balaye approximativement {{Value|180°}} ou un demi-cercle.
:   5.5. Répétez ces étapes avec chaque ligne de construction, de sorte que chacune d\'elles ait un arc circulaire à son extrémité. Nous appellerons ces arcs O-arcs pour les arcs extérieurs.

<img alt="" src=images/03_Sk01_Sketcher_outer_arcs.png  style="width:" height="400px;">


*Arcs de cercle ajoutés aux extrémités des lignes de construction. Ainsi qu'un cercle central.*

### Les arcs intérieurs 

6\. Créez un arc entre chaque paire des O-arcs précédents.

:   6.1. Toujours avec l\'outil **<img src=images/Sketcher_Arc.svg style="width:16px"> [Sketcher Créer un arc...](Sketcher_CreateArc/fr.md)** actif, cliquez quelque part entre deux O-arcs mais plus loin de l\'origine de l\'esquisse, pour définir le point central d\'un nouvel arc.
:   6.2. Cliquez quelque part près du point final d\'un O-arc et déplacez le pointeur pour balayer un autre arc finissant près d\'un autre point final d\'un O-arc différent comme si vous essayiez de joindre les points des extrémités. Cette fois, la concavité doit pointer loin de l\'origine.
:   6.3. Répétez ces étapes pour que chaque paire de O-arcs ait un nouvel arc entre elles. Nous appellerons ces arcs I-arcs pour les arcs vers l\'intérieur.

Pour résumer, les O-arcs devraient avoir leur courbure pointant vers l\'extérieur et leur concavité pointant vers l\'origine de l\'esquisse; les I-arcs devraient avoir leur courbure pointant vers l\'intérieur et leur concavité pointant loin de la même origine.

<img alt="" src=images/04_Sk01_Sketcher_inner_arcs.png  style="width:" height="400px;">


*Arcs de cercle ajoutés entre le premier ensemble d'arcs placé.*

## Contraintes

Jetez à nouveau un œil au [Panneau des tâches](Task_Panel/fr.md). En raison des nouveaux éléments géométriques que nous avons dessinés, la section **Solver messages** indique encore plus **degrees of freedom**. Un **degree of freedom** (degré de liberté) (DOF) indique un mouvement possible d\'un élément. Par exemple, un point peut être déplacé dans les directions horizontale et verticale, il a donc deux degrés de liberté. Une ligne est définie par deux points donc au total elle a quatre degrés de liberté. Si nous fixons l\'un de ces points, alors le système entier n\'a que deux degrés de liberté disponibles. Si nous fixons en outre le mouvement horizontal du point restant, il ne nous reste qu\'un degré de liberté; et si nous fixons également le mouvement vertical de ce point, alors le dernier degré de liberté disparaît et la ligne ne peut plus bouger de sa position.

Jusqu\'à présent, lorsque nous avons dessiné des lignes et des courbes, l\'esquisse nous a ajouté des contraintes automatiques, celles qui maintiennent les lignes liées à l\'origine et les O-arcs liés aux lignes de construction. Mais nous n\'avons pas ajouté d\'autres contraintes explicites afin que les formes géométriques puissent toujours être déplacées dans de nombreuses directions. **Les contraintes sont des \"règles\" qui nous indiquent dans quelles conditions un objet géométrique peut se déplacer et dans quelle mesure.** Elles sont utilisées pour éliminer les degrés de liberté afin que l\'esquisse ait une forme stable. Si nous éliminons tous les degrés de liberté, l\'esquisse est **entièrement contrainte** et a une forme fixe, c\'est-à-dire que ses points ne peuvent pas bouger du tout. En général, c\'est une bonne idée de contraindre complètement les esquisses car cela se traduira par des modèles stables.

Il existe deux principaux types de contraintes:

-    **Geometric constraints**définit les caractéristiques des formes sans spécifier les dimensions exactes, par exemple, l\'horizontalité, la verticalité, le parallélisme, la perpendicularité et la tangence.

-    **Datum constraints**définit les caractéristiques des formes en spécifiant les dimensions, par exemple, une longueur numérique ou un angle.

## Contraintes géométriques 

### Longueur et rayon égaux 

7\. Contraignez géométriquement les lignes et les arcs.

:   7.1. Sélectionnez les cinq lignes de construction. Vous n\'avez qu\'à cliquer une fois pour sélectionner un élément.
:   7.2. Appuyez sur **<img src=images/Constraint_EqualLength.svg style="width:16px"> [Sketcher Créeer une contrainte d'égalité...](Sketcher_ConstrainEqual/fr.md)**.
:   
    **Remarque:**cela ne crée que quatre contraintes. Les contraintes sont enchaînées, la première ligne a la même longueur que la seconde, qui a la même longueur que la troisième, qui a encore la même longueur que la quatrième, qui a la même longueur que la cinquième. Donc dans ce cas, la première et la cinquième longueur ont la même longueur.





:   7.3. Sélectionnez les cinq O-arcs, ceux centrés sur l\'extrémité d\'une ligne de construction.
:   7.4. Appuyez sur **<img src=images/Constraint_EqualLength.svg style="width:16px"> [Sketcher Créeer une contrainte d'égalité...](Sketcher_ConstrainEqual/fr.md)**.
:   7.5. Répétez avec tous les I-arcs, ceux entre les O-arcs.
:   
    **Remarque:**encore une fois les contraintes sont enchaînées. Par conséquent, tous les arcs en O auront le même rayon et tous les arcs en I auront le même rayon. A ce moment, la valeur spécifique de ces longueurs n\'est pas fixe. Vous pouvez utiliser le pointeur pour faire glisser un point et voir comment l\'esquisse est mise à jour tout en respectant les contraintes en place.





:   7.6. Sélectionnez la ligne de construction la plus proche de l\'axe vertical.
:   7.7. Appuyez sur **<img src=images/Constraint_Vertical.svg style="width:16px"> [‎Sketcher Créer une contrainte verticale...](‎Sketcher_ConstrainVertical.md)** (facultatif). Si vous avez tracé la ligne de construction vers le bas sur l\'axe Y, un <img alt="" src=images/Constraint_PointOnObject.svg  style="width:32px;"> [Sketcher Fixer un point sur un objet](Sketcher_ConstrainPointOnObject/fr.md) automatique a déjà été placé, en maintenant la ligne de construction verticale. Dans ce cas, aucun <img alt="" src=images/Constraint_Vertical.svg  style="width:32px;"> [‎Sketcher contrainte verticale](‎Sketcher_ConstrainVertical/fr.md) supplémentaire n\'est nécessaire.


**Remarque 1:**

lorsque vous ajoutez des contraintes, des symboles de superposition indiquant le type de contrainte apparaissent sur la géométrie ans la [vue 3D](3D_view/fr.md). Si ces symboles obscurcissent votre vue, vous pouvez les masquer en décochant la contrainte dans le [Panneau des tâches](Task_Panel/fr.md). Notez également que le nombre de degrés de liberté diminue après l\'ajout de chaque contrainte.


**Remarque 2:**

si vous souhaitez désactiver temporairement la contrainte, vous pouvez la sélectionner et appuyer sur **<img src=images/Sketcher_ToggleActiveConstraint.svg style="width:16px"> [Sketcher Activation des contraintest](Sketcher_ToggleActiveConstraint/fr.md)** . Lorsque vous souhaitez l\'appliquer à nouveau, appuyez à nouveau sur le même bouton.

<img alt="" src=images/05a_Sk01_Sketcher_equality_constraints_lines.png  style="width:" height="400px;"> <img alt="" src=images/05b_Sk01_Sketcher_equality_constraints_O-arcs.png  style="width:" height="400px;">

<img alt="" src=images/05c_Sk01_Sketcher_equality_constraints_I-arcs.png  style="width:" height="400px;">


*Esquisse avec des contraintes d'égalité appliquées aux lignes de construction et aux deux ensembles d'arcs.*

### Tangence

8\. Appliquez la tangence aux arcs.

:   8.1. Sélectionnez un point d\'extrémité d\'un O-arc puis le point d\'extrémité le plus proche de l\'I-arc adjacent.
:   8.2. Appuyez sur **<img src=images/Constraint_Tangent.svg style="width:16px"> [Sketcher Créer une contrainte tangente...](Sketcher_ConstrainTangent/fr.md)**. Cela permet aux deux arcs adjacents de se connecter en douceur à leurs extrémités.
:   8.3. Répétez l\'opération pour tous les points d\'extrémité des O-arcs et I-arcs pour obtenir un profil fermé.


**Remarque:**

L\'application de la contrainte tangentielle déplacera très souvent la géométrie afin de produire une connexion lisse. Vous devrez peut-être utiliser le pointeur pour repositionner un peu les points avant d\'appliquer la prochaine contrainte tangentielle. Essayez de placer les points d\'extrémité de manière à ce que deux arcs ne soient pas trop éloignés l\'un de l\'autre afin qu\'ils puissent être connectés avec une ligne courte plutôt qu\'une longue.

À partir de cette étape, nous avons maintenant créé un profil fermé, car tous les arcs ont été liés ensemble. Nous pouvons maintenant fournir des contraintes de référence pour fixer la forme de l\'esquisse. Alors que les dimensions des lignes et des arcs ne sont pas fixées, nous pouvons faire glisser les points de l\'esquisse et observer les modifications de l\'esquisse entière.

<img alt="" src=images/06_Sk01_Sketcher_tangency_constraints.png  style="width:" height="400px;">


*Esquisse avec des contraintes tangentielles appliquées aux arcs, ce qui ferme la forme.*

## Contraintes sur les valeurs 

Ces contraintes spécifient les distances numériques entre deux points et les angles entre deux lignes.

### Distances et angles 

9\. Ajustez la taille des lignes de construction.

:   9.1. Sélectionnez la ligne de construction contrainte verticalement.
:   9.2. Appuyez sur **<img src=images/Constraint_VerticalDistance.svg style="width:16px"> [Sketcher Contrainte distance en Y](Sketcher_ConstrainDistanceY/fr.md)** (verticale).
:   9.3. Définissez la longueur sur {{Value|30 mm}}. Étant donné que toutes les lignes de construction sont contraintes d\'avoir la même longueur, toutes ces lignes ajustent leurs tailles en même temps.

10\. Ajustez l\'angle entre les lignes de construction.

:   10.1. Sélectionnez la ligne de construction verticale et la ligne de construction la plus proche.
:   10.2. Appuyez sur **<img src=images/Constraint_InternalAngle.svg style="width:16px"> [Sketcher Fixer l'angle...](Sketcher_ConstrainAngle/fr.md)**.
:   10.3. Réglez l\'angle sur {{Value|72°}}..
:   10.4. Répétez la même procédure pour chaque paire de lignes de construction et utilisez le même angle.
:   
    **Remarque:**à ce stade, l\'esquisse peut avoir très peu de degrés de liberté, ce qui signifie que sa forme ne peut pas être trop modifiée. Si vous essayez d\'ajouter plus de contraintes, celles-ci peuvent provoquer un conflit avec les contraintes précédemment ajoutées. Si tel est le cas, n\'ajoutez pas ces contraintes et passez aux étapes suivantes.

<img alt="" src=images/07a_Sk01_Sketcher_length_constraint.png  style="width:" height="400px;"> <img alt="" src=images/07b_Sk01_Sketcher_angle_constraint.png  style="width:" height="400px;">


*Esquisse avec contrainte de longueur appliquée à une ligne de construction verticale (gauche) et contraintes d'angle à trois paires de lignes de construction (droite).*

### Rayon

11\. Ajustez la taille des arcs.

:   11.1. Sélectionnez l\'un des arcs en O, centré sur l\'extrémité d\'une ligne de construction.
:   11.2. Appuyez sur **<img src=images/Constraint_Radius.svg style="width:16px"> [Sketcher Contrainte radiale](Sketcher_ConstrainRadius.md)**.
:   11.3. Définissez le rayon à {{Value|8 mm}}. Étant donné que tous les O-arcs sont contraints d\'avoir le même rayon, tous ces arcs ajustent leurs tailles en même temps.
:   11.4. Sélectionnez l\'un des I-arcs, entre deux O-arcs.
:   11.5. Appuyez sur **<img src=images/Constraint_Radius.svg style="width:16px"> [Sketcher Contrainte radiale](Sketcher_ConstrainRadius.md)**.
:   11.6. Définissez le rayon à {{Value|11 mm}}. Étant donné que tous les I-arcs sont contraints d\'avoir le même rayon, tous ces arcs ajustent leurs tailles en même temps.

<img alt="" src=images/08a_Sk01_Sketcher_radius_1_constraint.png  style="width:" height="400px;"> <img alt="" src=images/08b_Sk01_Sketcher_radius_2_constraint.png  style="width:" height="400px;">


*Esquisse avec des contraintes de rayon appliquées aux arcs extérieurs (gauche) et intérieurs (droite).*


:   11.7. Enfin, sélectionnez le cercle au centre de l\'esquisse, appuyez sur **<img src=images/Constraint_Radius.svg style="width:16px"> [Sketcher Contrainte radiale](Sketcher_ConstrainRadius.md)** et définissez la valeur à {{Value|8 mm}}.

Nous devrions nous retrouver avec un croquis entièrement contraint. Cela peut être confirmé en remarquant le changement de couleur de la géométrie réelle et par le message affiché dans le [Panneau des tâches](Task_Panel/fr.md).

<img alt="" src=images/09_Sk01_Sketcher_fully_constrained.png  style="width:" height="400px;">


*Esquisse avec toutes les contraintes géométriques et de référence appliquées.*

## Extrusion

12\. Maintenant que nous avons une esquisse entièrement contrainte, elle peut être utilisée pour créer un corps solide.

:   12.1. Quittez le mode d\'édition d\'esquisse en appuyant sur le bouton **Fermer** ou en appuyant deux fois sur **Echap**. L\'esquisse doit apparaître dans la [vue en arborescence](tree_view/fr.md) et la [vue 3D](3D_view/fr.md).
:   12.2. Basculez vers [Atelier PartDesign](PartDesign_Workbench/fr.md).
:   12.3. L\'esquisse étant sélectionnée dans la <img src=images/PartDesign_Body.svg style="width:vue en arborescence](tree_view/fr.md), appuyez sur **[16px"> [PartDesign Corps](PartDesign_Body/fr.md)**, choisissez le plan XY par défaut, et appuyez sur **OK**. L\'esquisse doit maintenant apparaître à l\'intérieur du corps.
:   12.4. Sélectionnez l\'esquisse, puis appuyez sur **<img src=images/PartDesign_Pad.svg style="width:16px"> [PartDesign Protrusion](PartDesign_Pad/fr.md)**, choisissez les options par défaut et appuyez sur **OK** pour créer un extrusion solide.

<img alt="" src=images/09b_Sk01_Sketcher_fully_constrained_clean.png  style="width:" height="400px;"> <img alt="" src=images/10_Sk01_Sketcher_solid_extrusion.png  style="width:" height="400px;">


*A gauche: l'esquisse entièrement contrainte avec seulement les contraintes les plus importantes. A droite: l'extrusion solide produite avec [PartDesign Protrusion](PartDesign_Pad/fr.md).*

## Informations supplémentaires 

Pour une description plus approfondie de l\'esquisse, consultez la documentation [Atelier Sketcher](Sketcher_Workbench/fr.md) et lisez également le [Manuel de référence pour Sketcher](Sketcher_reference/fr.md).

Contraindre une esquisse peut se faire de différentes manières. En général, il est recommandé d\'utiliser d\'abord les contraintes géométriques et de minimiser le nombre de contraintes de référence, car cela simplifie la tâche du solveur de contraintes internes. Pour étudier cela, répétez cet exemple, en ajoutant maintenant les contraintes dans un ordre différent.

-   D\'abord contraindre les lignes de construction avant de dessiner les arcs.
-   Ou contraignez la taille des arcs avant de les rendre tangents.
-   Ou définissez l\'angle des lignes de construction avant d\'ajouter d\'autres éléments.
-   Essayez d\'utiliser une autre géométrie de construction.


{{Tutorials navi

}} {{Sketcher Tools navi}} 

[Category:Sketcher/fr](Category:Sketcher/fr.md)
