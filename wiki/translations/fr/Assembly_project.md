# Assembly project/fr




{{VeryImportantMessage|
Ce plan de développement est probablement obsolète. Pour plus d'informations, voir [Plan de développement](Development_roadmap/fr.md).<br>
Si vous n'êtes pas impliqué dans le développement discuté ici :<br>
!!! S'IL VOUS PLAÎT, NE MODIFIEZ PAS ET NE TRADUISEZ PAS !!!
}}


{{TOCright}}

Voici, le détail du projet de module **Assembly** (Assemblage) dans le cadre de la [feuille de route du développement](Development_roadmap/fr.md)

## Buts et principes 

Il s\'agit d\'un projet de développement logiciel visant à mettre en place des capacités de d\'assemblage et de création de produits. Il requiert l\'implémentation de certaines **caractéristiques de base** dans les modules CAD de FreeCAD **Part et Assembly**.

Les étapes de développement sont planifiées et suivies dans le système de suivi des problèmes pour obtenir un journal des changements bien documenté : [système de suivi](https://www.freecadweb.org/tracker/)

Voir aussi les développements en cours dans [Ateliers externes](External_workbenches/fr.md) et la section [Assemblage et animations](External_workbenches/fr#Assembly.md).

## Résultats

Le but du projet est de permettre aux utilisateurs de FreeCAD d\'accomplir une conception comme celle-ci :

<img alt="" src=images/Gripper.jpg  style="width:400px;">

Elle sera obtenue à l\'aide d\'un **atelier d\'assemblage** pour mettre tous les différents types de pièces ensemble à l\'aide de contraintes, tout en restant aussi proche que possible de la spécification [ISO 10303](http://fr.wikipedia.org/wiki/Standard_pour_l'échange_de_données_de_produit) pour permettre l\'échange facile de données.

Un autre objectif est d\'utiliser **[ODE](http://fr.wikipedia.org/wiki/Open_Dynamics_Engine)** pour la [cinématique](http://fr.wikipedia.org/wiki/Cinématique).

## Des idées 

### Modèle multiple 

<img alt="" src=images/MultiModel.png  style="width:600px;">

Une caractéristique clé de conception du monde réel, est la capacité de fractionner une conception en morceaux maniables. Il est impossible de travailler sur tous les aspects de la conception en même temps ou séparément. C\'est vrai pour les formes géométriques et aussi, pour les tâches d\'ingénierie comme [FEM](http://fr.wikipedia.org/wiki/Méthode_des_éléments_finis) ou [CAM](http://fr.wikipedia.org/wiki/Fabrication_assistée_par_ordinateur).
Il faut que FreeCAD aie la possibilité de fractionner les modèles. Cela ouvre quelques possibilités :

-   **Fin de chargement** -seulement besoin de ressources telles que les graphiques et de la mémoire vive pour le projet, sur lequel vous travaillez.
-   [**ingénierie concourante**](http://fr.wikipedia.org/wiki/Ingénierie_concourante)-permet à beaucoup de personnes de travailler sur le même projet.
-   [*\' Contrôle de version*\'](http://fr.wikipedia.org/wiki/Gestion_de_versions)- mieux contrôler les différents aspects de la conception, et bien d\'autres choses encore\...

Un multi-projet pourrait ressembler à ceci :

### Gestion de projet 

Multi-modèle signifie beaucoup de fichiers appartenant à un seul projet, probablement dans un répertoire commun. Un fichier de projet et un navigateur de projet peuvent être utiles pour organiser les fichiers. Il peut également enregistrer des informations supplémentaires sur le projet ou un site Web du projet.

1\. Deux modes, le mode **Simple** et le mode **Projet**. Le mode **simple** est un document qui réunit tous les assemblages et pièces dans un seul document. Si un projet est ouvert ou créé, FreeCAD est en mode projet.

2\. Le mode **projet**, la position du fichier **.FCPrj** sur le disque est définit dans un répertoire racine. Tous les fichiers dans le répertoire ci-dessous sont définis avec les chemins d\'accès relatifs à la racine. Une vue supplémentaire sur le côté gauche concerne le **ProjectExplorer** qui montre l'historique des fichiers manipulés. Le répertoire racine est également utilisé en tant que root pour, un **SVN sand box**, ce qui permet de contrôler, la version du fichier et le partager facilement. Les références externes, (vers un chemin à l\'extérieur de la racine, un partage de serveur ou une ressource web) seront manipulés et montrés de manière indépendantes dans le **ProjectExplorer** (un pseudo chemin pour chaque serveur de fichiers ou serveur web). Cela permet d\'obtenir un aperçu rapide, sur les références externes et les ré-acheminer.

### Droits d\'auteurs 

Le droit d\'auteur des modèles 3D est maintenant un champ intéressant. Les modèles 3D relèvent du droit d\'auteur. Le droit d\'auteur appartient au créateur du projet 3D. IL est seulement possible de protéger la forme géométrique, qui est représentée par le modèle, par un brevet ou un brevet de conception (US). Mais les brevets couvrent uniquement la création d\'une forme physique pour gagner de l\'argent. À titre d\'exemple, [le brevet de conception de souris Microsoft](http://patft1.uspto.gov/netacgi/nph-Parser?Sect1=PTO1&Sect2=HITOFF&d=PALL&p=1&u=%2Fnetahtml%2FPTO%2Fsrchnum.htm&r=1&f=G&l=50&s1=D464,651.PN.&OS=PN/D464,651&RS=PN/D464,651).

Nous ne devons donc pas oublier le créateur (titulaire du droit d\'auteur) et tout type de licence pour chaque modèle/produit/fichier de conception. Pour la licence, j\'utiliserais les licences de type [Créative Commons](http://creativecommons.org/).

Clés d\'abréviation pour licences CC:

-   BY = Attribution only
-   BY-ND = Attribution-NoDerivatives
-   BY-NC-ND = Attribution-NonCommercial- NoDerivatives
-   BY-NC = Attribution-NonCommercial
-   BY-NC-SA = Attribution-NonCommercial- ShareAlike
-   BY-SA = Attribution-ShareAlike
-   PD = Dédié à ou marqué comme appartenant au domaine public via l\'un de nos outils du domaine public ou tout autre ouvrage du domaine public; les adaptations d\'œuvres du domaine public peuvent être créées et concédées sous licence par le créateur selon les conditions de licence souhaitées

De plus, un lien URL vers le document de licence complet (dans le cas de licences personnalisées).

### ISO 10303 

La norme [ISO 10303](http://fr.wikipedia.org/wiki/ISO_10303) (STEP) est très importante dans ce domaine. C\'est le seul bon standard, largement diffusé et reconnu sur la définition des structures de produits que je connaisse.

<img alt="" src=images/Product_structure_modeling_Process-Data_diagram.gif  style="width:500px;">

Ici, certains liens avec des info :

-   [ISO 10303](http://fr.wikipedia.org/wiki/ISO_10303) sur Wikipedia
-   [ISO 10303-11](http://fr.wikipedia.org/wiki/Express) sur le language de modélisation (EXPRESS)
-   [A Wikipedia article](http://en.wikipedia.org/wiki/Product_Structure_Modeling) sur la modélisation d\'un produit
-   [Overview of Part 41 \-- Fundamentals of Product Description and Support](http://www.steptools.com/support/stdev_docs/express/step_irs/index.html#part41)
-   [Overview of Part 44 (edition 2) \-- Product Structure Configuration](http://www.steptools.com/support/stdev_docs/express/step_irs/index.html#part44)
-   [Examples of small AP 214 files](http://www.steptools.com/support/stdev_docs/express/ap214/index.html)

### Assemblages et contraintes 

Un rôle important dans la construction de gros projets est pris en charge par les contraintes d\'assemblage, qui formulent certaines règles sur la manière d\'assembler les pièces d\'un produit. Principalement, ce sont Fixe, Face-à-Face, Angle, Décalage et certains types d\'instanciation du modèle. Si les pièces changent, un solveur spécialisé de contraintes a besoin de les suivre. Ce solveur est fondamentalement différent du solveur du Sketcher. Je pense que nous devons avoir une approche graphique basée sur lui\...

### Cinématique

Une autre étape serait d\'utiliser [ODE](http://ode.org/), ou librairies similaires, pour assembler les pièces et les contraintes permettant de faire une simulation cinématique du système mécanique. Cela permettrait de visualiser le système mécanique en situation de fonctionnement et de vérifier d\'éventuelles collisions.

### Contrôle des mises à jour 

Un point important est le contrôle de version et de développement distribué. Avec la conception de multi modèle, nous sommes capables de fractionnez des projets en petits morceaux et pouvons distribuer le travail à plusieurs équipes. Pour un développeur de logiciels, les termes « distribué » et « Version » sont familiers, alors pourquoi ne pas utiliser un [CVL](http://fr.wikipedia.org/wiki/Gestion_de_version_décentralisée#Gestion_de_versions_d.C3.A9centralis.C3.A9e). Une bonne comparaison peut être trouvée [ici](http://en.wikipedia.org/wiki/Comparison_of_revision_control_software#Technical_information).

Puisque nous traitons de gros volumes de données, qui ne peuvent pas être facilement comparable, nous sommes limités à ceux qui utilisent le modèle persistant. Tout système d\'archivage aura de graves problèmes avec nos données (testés personnellement avec les fichiers [Mercurial](http://fr.wikipedia.org/wiki/Mercurial) et [Catia](http://fr.wikipedia.org/wiki/CATIA)). Après séparation entre les commerciaux et le non libre, restent essentiellement [Git](http://fr.wikipedia.org/wiki/Git) et [SVN](http://subversion.apache.org/).

Faire le travail à l\'aide de Git nous laisse avec deux grosses limitations :

-   Git est très complexe ; fusion des ramifications et de marquage le long d\'un chemin de développement non linéaire, sans parler de fusion avec des référentiels distants (push, pull) ajoutera beaucoup de complexité dans cette affaire. Le cacher à l\'utilisateur sera une tâche ardue.
-   Git dispose de gestionnaires de fusion (merge) et de comparaison (diff) pour certains types de fichiers ; nous avons besoin d\'un gestionnaire pour le format fcstd. Ce gestionnaire doit examiner deux documents FreeCAD et inspecter et fusionner les différences dans les objets, les fonctions et paramètres. Cela aussi n\'est pas facile !

Mais l\'utilisation de git ouvre beaucoup de possibilités dont même des systèmes PLM de première classe rêveraient\...

## Organisation

Ici certaines tâches de développement nécessaires à une conception pour un assemblage convenable :

### Infrastructure

l\'ensemble demande des changements dans le système de base, et la couche de l\'infrastructure de FreeCAD.

#### Multi-modèle 

Multi-Model était à l'esprit depuis le début de la conception de FreeCAD. Par conséquent, nous avons une interface multi-documents et pouvons charger des documents illimités. Mais nous devons surtout mettre à niveau 3D-Viewer pour pouvoir afficher plus d\'un document dans sa vue (Arborescences de pièces).

#### Arborescences de pièces 

La composition de l\'assemblage des pièces et des sous-ensembles est le flux principal du travail, les outils de groupage (stack) des pièces dans une arborescence doivent être mis en œuvre. Contrairement à un **DocumentObjectGroup**, le groupe de l\'assemblage doit faire face à la visibilité et le positionnement des \"enfants\". Le mieux est de faire l\'empilage ViewProvider l\'un sur l\'autre. Pour cela nous avons besoin d\'une sorte d\'interface ClaimChildren() pour les ViewProviders.

#### Interface unifiée Glisser/Déposer/Copier/Coller 

Une interface permet au **ViewProvider** et aux ateliers un contrôle total sur les opérations glisser/déplacer/copier/coller dans l\'arborescence ou dans la vue 3D.

#### Ressources externes 

Manipulation des liens \"dopés\" (à partir de navigateurs internes ou externes). Moyens de chargement de ressources sur les connexions potentiellement lentes (http).

### Matériel

Décrire le matériel et ses propriétés est un sujet essentiell d\'un système de CAO/DAO. Les matériau possèdent beaucoup de propriétés et de noms, fortement dépendants de leurs utilisation. Par exemple FEM et génie mécanique, ont des manières et normes différentes pour décrire le matériel.

Pour la désignation du matériel, une page spéciale est ouverte : [Matériel](Material/fr.md)

### Modèles d\'objets 

Arbre de classe pour le traitement avec les concepts nécessaires. Références, interfaces, documents, liens, vues, composés, contraintes, configurations et beaucoup plus\...

## Boucle de vérification STEP 

Implémentation d\'un premier importateur STEP pour plus que la géométrie et la couleur afin de vérifier si le modèle objet est valable pour une utilisation plus large.

### Solveur d\'assemblage de contraintes 

Définir l\'interface d\'un solveur d\'assemblage de contraintes très similaire à l\'interface du solveur d\'esquisse.

### Interface de simulation physique 

Interface permettant à un logiciel de simulation physique (externe) (multi), de prendre le contrôle de la position des parties de l\'assemblage. Cela permettrait d\'utiliser la bibliothèque logicielle \"bullet\" ou \"ODE\" pour faire des tests de cinématiques et [DMU](http://fr.wikipedia.org/wiki/Maquette_numérique) (Digital Mock-Up).

## Actions suivantes 

-   Modeles d\'objets
-   \...

[Category:Roadmap](Category:Roadmap.md)
