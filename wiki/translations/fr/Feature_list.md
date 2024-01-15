# Feature list/fr
Il s\'agit d\'une liste étendue, mais non complète, des fonctionnalités que FreeCAD implémente.






## Notes de versions 

-   [Notes de version 0.21](Release_notes_0.21/fr.md) - Août 2023
-   [Notes de version 0.20](Release_notes_0.20/fr.md) - Juin 2022
-   [Notes de version 0.19](Release_notes_0.19/fr.md) - Mars 2021
-   [Notes de version 0.18](Release_notes_0.18/fr.md) - Mars 2019
-   [Notes de version 0.17](Release_notes_0.17/fr.md) - Avril 2018
-   [Notes de version 0.16](Release_notes_0.16/fr.md) - Avril 2016
-   [Notes de version 0.15](Release_notes_0.15/fr.md) - Mars 2015
-   [Notes de version 0.14](Release_notes_0.14/fr.md) - Mars 2014
-   [Notes de version 0.13](Release_notes_0.13/fr.md) - Janvier 2013
-   [Notes de version 0.12](Release_notes_0.12/fr.md) - Décembre 2011
-   [Notes de version 0.11](Release_notes_0.11/fr.md) - Mars 2011



## Fonctions principales 

-   ![](images/_Feature1.jpg ) Un **noyau géométrique** complet basé sur [Open CASCADE Technology](https://fr.wikipedia.org/wiki/Open_CASCADE_Technology) permettant des opérations 3D complexes sur des formes complexes, avec prise en charge native de concepts tels que les [B-Rep](https://fr.wikipedia.org/wiki/B-Rep), les [NURBS](https://fr.wikipedia.org/wiki/NURBS) (courbes et surfaces), un large éventail de modules géométriques, d\'opérations booléennes, des [arrondis et congés](https://fr.wikipedia.org/wiki/Arrondi_et_cong%C3%A9) ainsi que la prise en charge des formats [STEP](https://fr.wikipedia.org/wiki/Standard_pour_l%27%C3%A9change_de_donn%C3%A9es_de_produit) et [IGES](https://fr.wikipedia.org/wiki/Initial_Graphics_Exchange_Specification)




-   ![](images/Feature3.jpg ) Un **modèle paramétrique** complet. Tous les objets construits dans FreeCAD sont paramétriques, ce qui signifie que leurs formes sont basées sur des [propriétés](Property/fr.md) ou peuvent même dépendre d\'autres objets. Toutes les modifications sont recalculées à la demande et enregistrées dans la pile annuler/rétablir. Les nouveaux types d\'objet peuvent être ajoutés très facilement et peuvent même être totalement [programmés en Python](Scripted_objects/fr.md).
-   ![](images/Feature4.jpg ) L**\'architecture modulaire** permet aux modules (plugins) d\'ajouter des fonctionnalités à l\'application de base. Ces extensions peuvent être aussi complexes qu\'une nouvelle application programmée en **[C++](https://fr.wikipedia.org/wiki/C%2B%2B)** ou aussi simple qu\'un **[Script Python](Power_users_hub/fr.md)** ou encore une [macro](Macros/fr.md) que vous avez enregistrée. Vous avez un accès complet à la console **[Python](http://www.python.org/)** intégrée pour concevoir vos macros ou exécuter des scripts externes, à pratiquement n\'importe quelle partie de FreeCAD que ce soit pour la création, la transformation, la représentation [géométrique](Topological_data_scripting/fr.md) 2D ou 3D de votre [Graphe de scène](Scenegraph/fr.md) ou même l\'[interface de FreeCAD](PySide/fr.md) elle-même.
-   ![](images/Feature5.jpg ) L\'importation/exportation de **formats standards** tels que [STEP](https://fr.wikipedia.org/wiki/Standard_pour_l%27%C3%A9change_de_donn%C3%A9es_de_produit), [IGES](https://fr.wikipedia.org/wiki/Initial_Graphics_Exchange_Specification), [OBJ](https://fr.wikipedia.org/wiki/Obj), [STL](https://fr.wikipedia.org/wiki/Fichier_de_st%C3%A9r%C3%A9olithographie), [DXF](https://fr.wikipedia.org/wiki/Drawing_eXchange_Format), [SVG](http://fr.wikipedia.org/wiki/Scalable_Vector_Graphics), [DAE](https://fr.wikipedia.org/wiki/Collaborative_Design_Activity), [SFI](https://fr.wikipedia.org/wiki/Industry_Foundation_Classes) ou [OFF](https://people.sc.fsu.edu/~jburkardt/data/off/off.html), [NASTRAN](https://fr.wikipedia.org/wiki/Nastran), [VRML](https://fr.wikipedia.org/wiki/Virtual_Reality_Markup_Language), outre le format de fichier originaire de FreeCAD****[FCStd](File_Format_FCStd/fr.md)****. Le niveau de compatibilité entre FreeCAD et un format de fichier donné peut varier car cela dépend du module qui l\'implémente.
-   ![](images/Feature7.jpg ) Le module [Sketcher](Sketcher_Workbench/fr.md) est un solveur de contraintes qui permet de faire des esquisses des formes 2D géométriques contraintes. L\'esquisse 2D contrainte avec Sketcher permet aujourdh\'ui de construire plusieurs types de contraintes géométriques et de les utiliser comme la base de construction d\'autres objets tout au long de l\'utilisation de FreeCAD.
-   ![](images/_Feature8.jpg ) Le module [TechDraw](TechDraw_Workbench/fr.md) avec les options telles que vue détaillée, coupes, cotations et autres permet de générer des vues 2D sur feuille à partir de vos modèles 3D. Ce module produit des feuilles au format SVG ou PDF prêtes à être exportées.
-   ![](images/Feature-arch.jpg ) Le module [Arch](Arch_Workbench/fr.md) permet d\'utiliser [BIM](http://fr.wikipedia.org/wiki/Building_Information_Modeling) comme processus de travail et est compatible avec le format [IFC](http://fr.wikipedia.org/wiki/Industry_Foundation_Classes).
-   ![](images/Feature-CAM.jpg ) Le module [Path](Path_Workbench/fr.md) est dédié à l\'usinage mécanique [Fabrication assistée par ordinateur](https://fr.wikipedia.org/wiki/Fabrication_assist%C3%A9e_par_ordinateur) (FAO). Avec le module Path, vous êtes en mesure d\'afficher et de modifier le [G code](https://fr.wikipedia.org/wiki/Programmation_de_commande_num%C3%A9rique) contrôlant votre machine. 
-   ![](images/_Feature_spreadsheet.png ) Une [Feuille de calcul intégrée](Spreadsheet_Workbench/fr.md) et un [analyseur d\'expression](Expressions/fr.md) permettent de piloter des feuilles basées sur des formules ou de récupérer des données à partir de modèles. 




## Fonctions générales 

-   **FreeCAD est multiplate-forme**. Le logiciel fonctionne et se comporte exactement de la même manière sur Windows, Linux, macOS et d\'autres plateformes.

-   **FreeCAD est une application entièrement graphique**. FreeCAD possède une Interface Graphique Utilisateur développée sur le célèbre framework [Qt](https://www.qt.io/) avec une visualisation 3D basée sur [Open Inventor](wikipedia:fr:Inventor_(bibliothèque_logicielle).md) qui permet un rendu rapide des travaux en 3D et une représentation graphique de ces mêmes travaux très accessible.

-   **FreeCAD peut aussi fonctionner en ligne de commande**, avec une utilisation réduite des ressources. En ligne de commande, FreeCAD s\'exécute sans son interface, mais avec tous ses outils géométriques. Il est possible, par exemple de l\'utiliser comme serveur pour produire du contenu destiné à d\'autres applications.

-   **peut être importé en tant que [module Python](Embedding_FreeCAD/fr.md)**. FreeCAD peut être importé dans toute application capable d\'exécuter des scripts Python. Comme en mode ligne de commande, la partie interface de FreeCAD n\'est pas disponible, mais tous les outils de géométrie sont accessibles.

-   **Le concept d\'atelier**. Dans l\'interface FreeCAD, les outils sont regroupés en [ateliers](Workbenches/fr.md) (environnement de travail). Ceci permet d\'afficher uniquement les outils nécessaires à la réalisation d\'une tâche particulière, tout en maintenant une interface épurée et réactive ainsi qu\'une application rapide à charger.

-   **Le framework Plugin/Module pour le chargement de fonctionnalités et de types de données**. FreeCAD est composé d\'une application de base avec un certain nombre de modules, chargés uniquement lorsque cela est nécessaire. La plupart des outils et des types de géométrie sont stockés dans des modules. Les modules se comportent comme des plugins. En plus du chargement différé, des modules individuels peuvent être ajoutés ou supprimés d\'une installation existante de FreeCAD.

-   **Objets paramétrables et associatifs**. Tous les objets d\'un document FreeCAD peuvent être définis par des paramètres. Ces paramètres peuvent être modifiés à la volée et recalculés à tout instant. Les relations entre les objets sont ainsi mémorisées de sorte que la modification d\'un objet entraîne la modification de tous les objets qui dépendent de lui.

-   **Formes primitives paramétriques**. Des objets dit primitifs tels que cube, sphère, cylindre, cône ou tore peuvent être générés en spécifiant leurs contraintes géométriques.

-   **Opérations de modification** graphiques. Freecad permet d\'effectuer des translations, rotations, mises à l\'échelle, symétries axiale, décalage (soit simple soit comme ici [Jung/Shin/Choi](https://www.researchgate.net/publication/240754626_Self-intersection_Removal_in_Triangular_Mesh_Offsetting)) ou la conversion de forme dans n\'importe quel plan de l\'espace 3D.

-   **[Géométrie de construction de solides ](Constructive_solid_geometry/fr.md) (opérations booléennes)** comme **union**, **différence** et **intersection**.

-   **Création graphique de géométrie planaire**. Des lignes, des polylignes, des rectangles, des B-splines et des arcs circulaires ou elliptiques peuvent être créés graphiquement dans n\'importe quel plan de l\'espace 3D.

-   Modélisation à l\'aide d**\'extrusions** droites ou de révolution, de **sections** et de **congés**.

-   Composants topologiques tels que les **sommets, contours, fils** et les **plans**.

-   **Vérification et réparation**. Freecad a des outils de vérification des maillages (test solide, test de non-double-variété, test d\'auto-intersection) et de réparation des maillages (remplissage de trous et orientation uniforme).

-   **Annotations**. Freecad peut insérer des annotations de textes ou de dimensions.

-   **Framework annuler / rétablir**. Il est possible de tout annuler / rétablir dans Freecad avec un accès à l\'historique d\'annulation. Plusieurs étapes peuvent être annulées en une seule fois.

-   **Gestion des opérations**. L\'historique d\'annulation conserve les opérations du document et non pas les seules actions. Ainsi, chaque outil est capable de définir exactement ce qui doit être annulé ou refait.

-   **Framework de [scripting](Power_users_hub/fr.md) intégré**. FreeCAD intègre un interpréteur [Python](http://www.python.org/), ainsi qu\'une interface de programmation qui couvre presque chaque partie de l\'application (l\'interface, la géométrie, et sa représentation dans l\'environnement 3D). L\'interpréteur peut exécuter de simples commandes autant que des scripts complexes, et à vrai dire des modules entiers peuvent même être programmés complètement en [Python](http://www.python.org/).

-   **Console Python intégrée**. L\'interpréteur Python comprend une console avec coloration syntaxique, auto-complétion et explorateur de classes. Les commandes Python peuvent être écrites directement dans FreeCAD et renvoyer immédiatement des résultats, permettant aux créateurs de scripts de tester les fonctionnalités à la volée, d\'explorer le contenu des modules et d\'en apprendre facilement davantage sur FreeCAD.

-   **Correspondance interaction utilisateur et console**. Tout ce que l\'utilisateur fait dans l\'interface FreeCAD exécute du code Python qui peut être affiché dans la console et enregistré en macros.

-   **Enregistrement et édition complets de [macros](Macros/fr.md)**. Les commandes Python exécutées lorsque l\'utilisateur manipule l\'interface peuvent être enregistrées, éditées au besoin et bien sûr sauvegardées afin d\'être reproduites ultérieurement.

-   **Format de fichier composé (basé sur ZIP)**. Les documents FreeCAD sauvegardés avec l\'extension **.[FCStd](File_Format_FCStd/fr.md)** peuvent contenir de nombreuses informations de nature différente, telles que la géométrie, des scripts, ou encore des icônes. Le fichier **.FCStd** est lui-même un conteneur zip, donc un fichier FreeCAD sauvegardé qui a déjà été compressé.

-   **Interface Graphique Utilisateur entièrement personnalisable / programmable**. L\'interface de FreeCAD basée sur [Qt](https://www.qt.io/) est entièrement accessible via l\'interpréteur Python. Outre les fonctions simples que FreeCAD fournit lui-même aux différents environnements de travail, l\'ensemble du framework Qt est également accessible, permettant n\'importe quelle opération sur l\'interface utilisateur, telles que la création, l\'ajout, l\'ancrage, la modification ou la suppression de widgets et de barres d\'outils.

-   **Créateur de miniatures**. (actuellement seul le système Linux le permet) les icônes des documents FreeCAD représentent le contenu du fichier dans la plupart des gestionnaires de fichiers, comme par exemple Nautilus sous GNOME.

-   **Un installeur modulaire MSI**. L\'installeur de Freecad permet une installation flexible sur les systèmes Windows. Les paquets pour les systèmes Ubuntu sont également maintenus.



## Ateliers externes 

Des utilisateurs avancés ont créé différents [Ateliers externes](External_workbenches/fr.md).



---
⏵ [documentation index](../README.md) > [User Documentation](Category_User Documentation.md) > Feature list/fr
