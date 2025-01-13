---
 TutorialInfo:r
   Topic: FEM
   Level: Intermédiaire
   Time: 1 heure
   Author: User:M42kus
   FCVersion: 0.17
---

# Extend FEM Module/fr





L\'atelier FEM prend déjà en charge un grand nombre de contraintes différentes et plusieurs solveurs. Malgré cela, les utilisateurs ont souvent besoin de contraintes qui ne sont pas encore prises en charge par FreeCAD. Cette page est le point de départ d\'une série de tutoriels et d\'autres ressources décrivant comment étendre l\'atelier FEM en utilisant le cadre existant. Bien que cette série puisse également être utile aux développeurs de logiciels, l\'idée est de permettre aux utilisateurs de FEM ayant un peu d\'intérêt pour le codage en Python d\'ajouter eux-mêmes les éléments dont ils ont besoin.

Ajouter de nouvelles contraintes, équations ou solveurs est généralement un travail de routine. Le faire pour la première fois n\'est pas aussi facile qu\'il puisse paraître. Une compréhension des sujets suivants sera utile :

-   Faire des scripts en Python dans FreeCAD.
    -   [Tutoriel sur les scripts Python](Python_scripting_tutorial/fr.md)
    -   [Débuter avec les scripts](FreeCAD_Scripting_Basics/fr.md)
-   Extension de FreeCAD avec Python.
    -   [Objets créés par script](Scripted_objects/fr.md)
-   Une bonne compréhension du solveur auquel il faut ajouter de nouveaux objets (par exemple CalculiX ou Elmer) est importante.
-   Un peu de connaissances sur les systèmes de compilation, en particulier cmake (le système de compilation utilisé par FreeCAD)



## La compilation (cmake) 

Le système de compilation doit être modifié indépendamment des objets qui seront ajoutés à l\'atelier FEM. Chaque module Python (fichier) doit être enregistré. L\'atelier FEM exige que chaque nouveau module Python soit enregistré dans `Mod/Fem/CMakeLists.txt`. Ceci est vrai quel que soit le type de module Python (GUI ou non-GUI). L\'endroit exact où le module doit être inséré dépend du rôle du module. Le solveur, les équations et les contraintes utilisent tous des listes différentes. La recherche de fichiers similaires et l\'insertion du nouveau fichier dans la même liste fonctionnent la plupart du temps.

À titre **d\'exemple**, ajoutons une nouvelle contrainte appelée  pour cette contrainte. Une nouvelle contrainte nécessite au moins les nouveaux modules suivants :

-    `constraint_<name>.py`
    

-    `view_constraint_<name>.py`
    

-    `CommandFemConstraint<name>.py`(peut-être pas nécessaire)

Ces trois fichiers doivent être ajoutés à `Mod/Fem/CMakeLists.txt` ainsi qu\'à `Mod/Fem/App/CMakeLists.txt`. Toutes les lignes de code insérées sont indiquées par un **+** au départ.


**Mod/Fem/CMakeLists.txt**


{{code|code=
SET(FemObjects_SRCS
    femobjects/__init__.py
    femobjects/base_fempythonobject.py
    femobjects/constraint_bodyheatsource.py
    femobjects/constraint_electrostaticpotential.py
    femobjects/constraint_flowvelocity.py
    femobjects/constraint_initialflowvelocity.py
+   femobjects/constraint_initialflowpressure.py
    femobjects/constraint_selfweight.py
...
    femobjects/solver_ccxtools.py
)
...
SET(FemGuiViewProvider_SRCS
    femviewprovider/__init__.py
    femviewprovider/view_base_femconstraint.py
    femviewprovider/view_base_femobject.py
    femviewprovider/view_constraint_bodyheatsource.py
    femviewprovider/view_constraint_electrostaticpotential.py
    femviewprovider/view_constraint_flowvelocity.py
+   femviewprovider/view_constraint_flowpressure.py
    femviewprovider/view_constraint_initialflowvelocity.py
    femviewprovider/view_constraint_selfweight.py
...
    femviewprovider/view_solver_ccxtools.py
)
}}



## Organisation des sources 

Pour organiser le code Python, le module FEM utilise l\'approche suivante. Le module est divisé en plusieurs paquets :

-    `femobjects`, qui contient tous les proxys Pythonnon GUI pour les objets document et

-    `femviewproviders`contenant tout ce qui concerne l\'interface graphique, comme les proxys Python pour le fournisseur de vue

-   Les panneaux de tâches en C ++ sont stockés dans \'`Gui`\',

-   les icônes se trouvent dans \'`Gui/Resources/icons/`\',

-   Les fichiers .ui sont stockés dans les commandes \'`Gui/Resources/ui/`\'.

Un paquet ne suit pas ce modèle : `femsolver`. Il a sa place au même niveau que `femobjects` et `femguiobjects` (`src/Mod/Fem/femsolver`). Le paquet contient des modules relatifs au solveur et aux équations et est organisé de la manière suivante :

    .femsolver
    .femsolver.elmer
    .femsolver.elmer.equations
    .femsolver.calculix
    .femsolver.calculix.equations
    .femsolver.z88
    .femsolver.z88.equations



## Le solveur 

Dans FreeCAD, un solveur peut être divisé en deux parties :

-   L\'une est l\'objet document utilisé par l\'utilisateur pour interagir avec le solveur. Grâce à lui, les paramètres du solveur peuvent être définis et il est également utilisé pour contrôler le processus de résolution.
-   L\'autre est ce que l\'on appelle les tâches d\'un solveur. Le processus de résolution est divisé en ces tâches, à savoir : *vérification, préparation, résolution et résultats*. Ces tâches consistent à exporter l\'analyse dans un format compris par l\'exécutable du solveur, à lancer l\'exécutable et à charger les résultats dans FreeCAD.

La plupart des fichiers liés à un solveur sont dans un sous-paquet du paquet `femsolver` (par exemple, pour Elmer c\'est dans `femsolver/elmer`). La liste suivante énumère tous les fichiers liés à la mise en œuvre d\'un solveur. Ce sont les fichiers qui doivent être copiés et modifiés pour ajouter une prise en charge à un nouveau solveur à FreeCAD. L\'exemple donné est tiré de l\'implémentation du solveur d\'Elmer.

-   **femsolver/elmer/solver.py:** objet document visible dans l\'arborescence. Il est implémenté en Python via un proxy document et un proxy de visualisation.
-   **femsolver/elmer/tasks.py:** module contenant une classe de tâches par tâche requise pour une implémentation du solveur. Ces tâches divisent le processus de résolution d'une analyse en plusieurs étapes: vérification, préparation, résolution, résultats.
-   **femcommands/commands.py:** ajoute l\'objet document du solveur au document actif. Il est nécessaire pour accéder à l\'objet solveur à partir de l\'interface graphique.



## Équations

Une équation représente une propriété physique particulière qui doit être prise en compte lors de la résolution de l'analyse (par exemple flux, chaleur). Tous les solveurs de FreeCAD ne supportent pas (toutes) les équations. Les équations sont représentées par des objets enfants du solveur correspondant. Dans l\'arborescence, cela ressemble à ceci :

-   Solveur Elemer
    -   Elasticité
    -   Chaleur
    -   Flux
    -   Electrostatique

La plupart des options spécifiques au solveur (par ex. le nombre maximal d\'itérations, la méthode de résolution, etc.) sont définies via les objets équation. Une conséquence de cela est que chaque solveur doit avoir sa propre implémentation de la \"même\". équation. CalculiX pourrait avoir un objet Heat différent de celui d\'Elmer. Pour éviter d\'avoir plusieurs boutons pour la même propriété physique dans l\'interface graphique, chaque objet du solveur ajoute ses équations.

L\'implémentation réelle peut être divisée en une partie générique et une partie spécifique au solveur. La partie générique se trouve dans le module `femsolver.equationbase`. La partie spécifique du solveur réside dans des sous paquets d\'équations des paquets du solveur (par exemple `femsolver/elmer/equations`).

L\'ajout d\'une nouvelle équation à Elmer devrait être très facile. Pour les nouveaux venus, il existe un tutoriel qui explique comment ajouter une nouvelle équation à Elmer en ajoutant le solveur d\'élasticité existant à FreeCAD : [Tutoriel pour ajouter des équations FEM](Add_FEM_Equation_Tutorial/fr.md).



## Contraintes

Les contraintes définissent les conditions aux limites du problème à résoudre. Dans FreeCAD, les contraintes ne sont pas spécifiques à un solveur particulier. Une configuration de problème peut être résolue par tous les résolveurs prenant en charge toutes les conditions de l\'analyse.

L\'ajout de nouvelles contraintes est assez simple. Pour les nouveaux arrivants, il existe un tutoriel : [FEM Tutoriel pour ajouter des contraintes](Add_FEM_Constraint_Tutorial/fr.md).



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > Extend FEM Module/fr
