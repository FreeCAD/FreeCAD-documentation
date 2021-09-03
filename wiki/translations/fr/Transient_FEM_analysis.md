 {{UnfinishedDocu}}


{{TutorialInfo/fr
|Topic= Analyse FEM transitoire
|Level= 
|Time=
|Author=
|FCVersion=
|Files=
}}

## Contexte

## Créer le modèle 

1.  À partir d\'un nouveau projet FreeCAD, nous construisons notre bande bimétallique dans l\'<img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [atelier Part](Part_Workbench/fr.md)
2.  Dessinez un <img alt="" src=images/Part_Box.svg  style="width:24px;"> [Cube](Part_Box/fr.md) Solid et renommez-le en `aluminium`.
3.  Donnez-lui les dimensions 100 x 10 x 2 mm (longueur x largeur x hauteur).
4.  Créez un deuxième [Cube](Part_Box/fr.md) \'Acier\' solide avec les mêmes dimensions
5.  Décalez cette pièce de 2 mm le long de l\'axe Z (via **Placement → Position → z**).
6.  Sélectionnez les deux solides (en utilisant la touche **Shift** + clic de souris) et créez <img alt="" src=images/Part_BooleanFragments.svg  style="width:24px;"> [Fragments booléens](Part_BooleanFragments/fr.md) à partir d\'eux
7.  Renommez ces fragments booléens en `bimetal strip`
8.  Dans l\'[Éditeur de propriétés](Property_editor/fr.md), nous changeons le mode de **Standard** à **CompSolid**. (Cela devrait également fonctionner en utilisant la commande [Part Composé](Part_Compound/fr.md) au lieu de <img alt="" src=images/Part_BooleanFragments.svg  style="width:24px;"> [Fragments booléens](Part_BooleanFragments/fr.md), cependant avec des formes croisées plus complexes, il pourrait y avoir des problèmes avec l\'analyse FEM plus tard. Donc, il vaut mieux s\'habituer à utiliser les fragments booléens en premier lieu.) Le résultat devrait ressembler à ceci:

<img alt="" src=images/Transient_FEM_Bimetal_(1).JPG  style="width:700px;">

## Préparation et exécution de l\'analyse FEM 

### Affecter les matériaux 

Dans l'atelier FEM, nous créons une nouvelle <img alt="" src=images/FEM_Analysis.svg  style="width:20px;"> analyse et ajoutons un nouveau <img alt="" src=images/FEM_MaterialSolid.svg  style="width:20px;"> matériau à l\'analyse. Dans la fenêtre de tâches à venir, nous sélectionnons l\'un des alliages d\'aluminium prédéfinis. Sous \'geometry reference selector\' (sélecteur de référence de géométrie), nous affectons le matériau à la bande inférieure de notre modèle en définissant le mode de sélection sur \'solid\', en cliquant sur \'add\' et en sélectionnant une face ou un bord de la bande inférieure. Dans la vue liste, \'BooleanFragments:Solid1\' devrait apparaître.

<img alt="" src=images/Transient_FEM_Bimetal_(2).JPG  style="width:700px;">

Nous fermons la fenêtre de la tâche et répétons les étapes pour créer un deuxième matériau « acier » (carte de matériau \'CalculiX-Steel\') et l\'affecter à la bande supérieure (\'BooleanFragments:Solid2\').

## Création du maillage 

Puisqu\'une analyse par éléments finis a évidemment besoin d\'éléments pour travailler, nous devons convertir notre modèle en un maillage. L\'atelier FEM propose deux outils de maillage: Netgen et GMSH. Nous allons faire ici avec Netgen: avec l\'objet booléen \'bimetal strip\' sélectionné, nous cliquons sur l\'<img alt="" src=images/FEM_MeshNetgenFromShape.svg  style="width:20px;"> icône Netgen dans l\'atelier FEM. Dans la fenêtre de tâches suivante, nous devons faire différentes sélections, en partant du haut:

-   Max. taille est la taille maximale (en millimètres) d\'un élément. Plus petite est la taille maximale des éléments, plus nous en aurons - généralement, le résultat devient plus précis, mais avec une augmentation considérable du temps de calcul. Nous l\'avons fixé à 10.
-   Deuxième ordre signifie que, des nœuds supplémentaires seront créés dans chaque élément. Cela augmente le temps de calcul, mais constitue généralement un bon choix s\'il s\'agit de se s\'adapter, comme dans notre analyse. Nous vous laissons tester.
-   Finesse : sélectionnez la manière dont le modèle doit être découpé en éléments. Pour les modèles plus complexes avec des courbures et des intersections, nous pouvons augmenter le nombre d\'éléments dans ces régions pour obtenir de meilleurs résultats (au prix de plus de temps de calcul, bien sûr). Les utilisateurs experts peuvent également le définir sur Défini par l\'utilisateur et fixer les paramètres suivants. Pour notre modèle rectangulaire simple, le choix de la finesse n\'a pas beaucoup d\'impact, nous le laisserons à un niveau modéré.
-   Optimiser : une sorte de post-traitement après le maillage. Nous le gardons activé.

Un clic sur \'Appliquer\' lance le mailleur et - le temps dépendant de votre ordinateur - une image filaire apparaît sur notre modèle. Le mailleur a dû créer environ 4000 nœuds.

<img alt="" src=images/Transient_FEM_Bimetal_(3).JPG  style="width:700px;">

### Assigner des conditions aux limites 

Une analyse FEM n\'aboutirait à rien, car rien n\'influe encore sur notre modèle. Ajoutons donc un peu de température: choisissez la <img alt="" src=images/FEM_ConstraintInitialTemperature.svg  style="width:20px;"> température initiale à partir de l'atelier FEM et réglez-la sur 300 K. Ici, aucune partie du modèle ne peut être sélectionnée, car ce réglage s'applique à l'ensemble du modèle.

Ensuite, utilisons <img alt="" src=images/FEM_ConstraintTemperature.svg  style="width:20px;"> pour la température agissant sur une face. Sélectionnons les deux faces à une extrémité de la bande (Ctrl + bouton gauche souris) et cliquons sur \'Ajouter\' dans la fenêtre de tâche. Deux faces de l\'objet Ensemble Booléen doivent apparaître dans la liste ainsi que de petites icônes de température sur le modèle. Réglons la température à 400 K et fermons la fenêtre de tâche. Au début de l\'analyse, les faces sélectionnées obtiendront une élévation instantanée de la température de 300 à 400 K. La chaleur sera conduite le long des bandes de métal et provoquera la torsion de la bande.

<img alt="" src=images/Transient_FEM_Bimetal_(4).JPG  style="width:700px;">

Avant de pouvoir exécuter l\'analyse, une condition limite supplémentaire doit être définie: l\'analyse ne peut être exécutée que si notre modèle est fixé quelque part dans l\'espace. Avec <img alt="" src=images/FEM_ConstraintFixed.svg  style="width:20px;"> sélectionnons les deux mêmes faces que pour le 400 K ci-dessus et ajoutons les à la liste. Des barres rouges apparaîtront sur le modèle, indiquant que ces faces sont fixes dans l'espace et qu'elles ne peuvent pas se déplacer pendant l'analyse.

<img alt="" src=images/Transient_FEM_Bimetal_(5).JPG  style="width:700px;">

### Lancer l\'analyse 

L\'analyse doit déjà contenir un objet de solveur \'[FEM Outils du solveur CalculixCxx](FEM_SolverCalculixCxxtools/fr.md)\'. Sinon, ajoutons en un en utilisant l\'icône <img alt="" src=images/FEM_SolverCalculixCxxtools.svg  style="width:20px;"> du solveur dans la barre d'outils (il existe deux icônes identiques, le solveur expérimental devrait également fonctionner). L\'objet solveur a une liste de propriétés comme ci-dessous dans la section de gauche de la fenêtre. Ici, sélectionnons les options suivantes (laisser celles non mentionnées inchangées):

-   Type d\'analyse : Nous souhaitons effectuer une analyse thermomécanique. Les autres options resteraient uniquement statiques (aucun effet de température), fréquence (oscillations) ou uniquement pour vérifier la validité du modèle.
-   État d\'équilibre Thermo Mech : L\'état d\'équilibre signifie que le solveur retournera un seul résultat à l\'atteinte de l\'équilibre physique. Nous ne voulons PAS faire cela, nous aimerions obtenir plusieurs résultats résolus dans le temps (analyse transitoire). Alors définissons-le sur false.
-   Durée : nous voudrions que notre analyse s\'arrête après 60 secondes (c-à-d. le temps de simulation, pas le temps réel).

<img alt="" src=images/Transient_FEM_Bimetal_(6).JPG  style="width:700px;">

Après avoir double-cliqué sur l\'objet solveur, vérifions que \'thermomechanical\' est sélectionné et exécutons \'write .inp file\'. Cela prend généralement quelques secondes (ou beaucoup plus pour les modèles plus grands) et renvoie un message \'write completed\' (écriture terminée) dans la zone ci-dessous. Maintenant, commençons le calcul avec \'run CalculiX\'. Après un certain temps, les derniers messages \'CalculiX done without error!\' et \'Chargement des ensembles de résultats\...\' devraient apparaître. Lorsque la minuterie du bas est arrêtée, fermons la fenêtre de tâche (Avec des modèles plus grands et/ou des ordinateurs plus lents, FreeCAD peut se figer et nous ne verrons pas la minuterie fonctionner. Mais soyez patient, dans la plupart des cas CalculiX fonctionne toujours en arrière-plan et produira éventuellement des résultats).

Nous devrions maintenant avoir plusieurs <img alt="" src=images/FEM_ResultShow.svg  style="width:20px;"> objets de résultat FEM listés. En double-cliquant, vous pouvez ouvrir chacun d'eux et visualiser les températures, les déplacements et les contraintes calculés. Nous pouvons visualiser la déformation en sélectionnant \"Afficher\" dans la section \"Déplacement\". Comme les déplacements absolus sont faibles, utilisons le \'Factor\' (multiplicateur) pour exagérer les valeurs.

<img alt="" src=images/Transient_FEM_Bimetal_(7).JPG  style="width:700px;">

Dans FreeCAD, nous pouvons utiliser <img alt="" src=images/FEM_PostPipelineFromResult.svg  style="width:20px;"> [pipelines](FEM_PostPipelineFromResult/fr.md) pour faire du post-traitement des résultats. Alternativement, nous pouvons exporter les résultats au format VTK et les importer dans des post-processeurs dédiés tels que ParaView. Pour l'exportation de plusieurs résultats (comme pour cette analyse), une [macro](Macro_export_transient_FEM_results/fr.md) est disponible.

## Téléchargements

-   [Exemple de fichier sans les résultats (200 kB)](https://drive.google.com/file/d/1m3RiJ-JM7QSJ6YDhZnafHIbyL92V6sYU/view?usp=sharing)

-   [Exemple de fichier avec les résultats (10 MB)](https://drive.google.com/file/d/157aIdVpIyfpVW9WxL-ReGz0FIsQebH_q/view?usp=sharing)

## Autre éxemple 

-   [Exemple bimétallique analytique](https://forum.freecadweb.org/viewtopic.php?f=18&t=43040&start=10#p366664). L\'exemple analytique présenté dans le forum est inclus dans les exemples FreeCAD FEM. Il peut être démarré par Python à partir de femexamples.thermomech\_bimetall import setup setup()


{{Tutorials navi

}} {{FEM Tools navi}} 
