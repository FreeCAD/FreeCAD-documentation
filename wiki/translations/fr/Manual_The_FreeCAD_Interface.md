# Manual:The FreeCAD Interface/fr
{{Manual:TOC}}

FreeCAD est basé sur le [framework Qt](https://fr.wikipedia.org/wiki/Qt) et se caractérise par une interface simple et directe. Les utilisateurs de CAO les plus expérimentés pourront identifier les similitudes avec d\'autres logiciels, tandis que les nouveaux utilisateurs trouveront qu\'il est facile de naviguer et de découvrir les différentes options offertes par FreeCAD. Voici l\'apparence par défaut de FreeCAD :

<img alt="" src=images/FreeCAD_022_Start.png  style="width:600px;">

La page de démarrage sert d\'écran d\'accueil, conçu pour faciliter l\'accès rapide et facile aux principales zones de FreeCAD qu\'un utilisateur pourrait souhaiter explorer. Grâce à elle, les utilisateurs peuvent sans effort créer de nouvelles pièces, ouvrir des fichiers récents et lancer des dessins en 2D. En outre, il comporte des raccourcis vers des ressources utiles telles que des tutoriels et des forums d\'utilisateurs, qui sont inestimables pour les débutants et les utilisateurs expérimentés à la recherche de conseils ou d\'astuces. Les utilisateurs peuvent facilement personnaliser l\'apparence de la page de démarrage en fonction de leurs préférences.

Au fur et à mesure que vous vous familiarisez avec FreeCAD, vous pouvez ajuster les paramètres dans les préférences. Vous pouvez ainsi configurer FreeCAD pour qu\'il s\'ouvre directement dans l\'un des ateliers avec un nouveau document prêt à l\'emploi lorsque vous le lancez. Vous pouvez également fermer l\'onglet Page de démarrage et créer manuellement un nouveau document.

<img alt="" src=images/FreeCAD_022_PartDesign.png  style="width:600px;">



### Les ateliers 

FreeCAD utilise un système appelé « ateliers », similaire aux cadres conceptuels utilisés dans les logiciels de conception avancés tels que Revit ou CATIA. L\'idée d\'un atelier est analogue aux stations spécialisées d\'un laboratoire scientifique, où différents postes de travail sont équipés pour des types d\'expériences distincts. Dans un laboratoire, vous pouvez avoir une zone dédiée à la chimie, une autre à la biologie et une troisième à la physique, chacune équipée des outils spécifiques nécessaires à ces disciplines.

Dans le contexte de FreeCAD, chaque atelier est adapté à un type de tâche particulier, organisant tous les outils nécessaires à cette activité dans une seule interface. Lorsque vous passez d\'un atelier à l\'autre, l\'ensemble des outils et des commandes visibles dans l\'interface utilisateur s\'adapte pour refléter les besoins de la tâche sélectionnée, bien que le contenu du projet ou la « scène » sur laquelle vous travaillez ne change pas. Cela permet des transitions transparentes dans le flux de travail, par exemple en commençant une conception avec des formes 2D de base dans l\'atelier Draft, puis en élaborant ces conceptions avec des outils de modélisation avancés dans l\'atelier Part.

Les termes « Atelier » et « Module » sont parfois utilisés de manière interchangeable, mais ils ont des significations distinctes dans FreeCAD. Un module est une extension qui ajoute des fonctionnalités à FreeCAD, alors qu\'un atelier est un type spécifique de module équipé de ses propres composants d\'interface utilisateur tels que les barres d\'outils et les menus, conçus pour faciliter des types de tâches spécifiques. Ainsi, chaque atelier est un module, mais tous les modules ne sont pas des ateliers.

Le contrôle le plus important de l\'interface FreeCAD est le sélecteur d'atelier (Workbench) que vous utilisez pour passer d\'un atelier à l\'autre :

<img alt="" src=images/FreeCAD_WB.png  style="width:600px;">

-   <img alt="" src=images/Workbench_Assembly.svg  style="width:32px;"> L\'[atelier Assembly](Assembly_Workbench/fr.md) pour la construction et la résolution d\'assemblages mécaniques. {{Version/fr|1.0}}

-   <img alt="" src=images/Workbench_BIM.svg  style="width:32px;"> L\'[atelier BIM](BIM_Workbench/fr.md) pour travailler avec des éléments architecturaux et créer des modèles [BIM](https://fr.wikipedia.org/wiki/Building_information_modeling). Il combine l\'atelier Arch et l\'ancien atelier BIM externe disponible dans la {{VersionMinus/fr|0.21}}.

-   <img alt="" src=images/Workbench_CAM.svg  style="width:32px;"> L\'[atelier CAM](CAM_Workbench/fr.md) est utilisé pour produire des instructions en G-Code. Cet atelier était appelé \"atelier Path\" {{VersionMinus/fr|0.21}}.

-   <img alt="" src=images/Workbench_Draft.svg  style="width:32px;"> L\'[atelier Draft](Draft_Workbench/fr.md) contient des outils 2D et des opérations de CAO 2D et 3D de base.

-   <img alt="" src=images/Workbench_FEM.svg  style="width:32px;"> L\'[atelier FEM](FEM_Workbench/fr.md) fournit un flux de travail d\'analyse par éléments finis (FEA).

-   <img alt="" src=images/Workbench_Inspection.svg  style="width:32px;"> L\'[atelier Inspection](Inspection_Workbench/fr.md) est fait pour vous donner des outils spécifiques pour l\'examen des formes. Il en est encore aux premiers stades de développement.

-   <img alt="" src=images/Workbench_Material.svg  style="width:32px;"> L\'[atelier Material](Material_Workbench/fr.md) gère le système des matériaux de FreeCAD. {{Version/fr|1.0}}

-   <img alt="" src=images/Workbench_Mesh.svg  style="width:32px;"> L\'[atelier Mesh](Mesh_Workbench/fr.md) pour travailler avec des maillages triangulés.

-   <img alt="" src=images/Workbench_OpenSCAD.svg  style="width:32px;"> L\'[atelier OpenSCAD](OpenSCAD_Workbench/fr.md) pour l\'interopérabilité avec OpenSCAD et la réparation de [Géométrie Solide Constructive](Constructive_solid_geometry/fr.md) (CSG).

-   <img alt="" src=images/Workbench_Part.svg  style="width:32px;"> L\' [atelier Part](Part_Workbench/fr.md) pour travailler avec des primitives géométriques et des opérations booléennes.

-   <img alt="" src=images/Workbench_PartDesign.svg  style="width:32px;"> L\'[atelier PartDesign](PartDesign_Workbench/fr.md) pour créer des formes de pièces à partir d\'esquisses.

-   <img alt="" src=images/Workbench_Points.svg  style="width:32px;"> L\'[atelier Points](Points_Workbench/fr.md) pour travailler avec des nuages de points.

-   <img alt="" src=images/Workbench_Reverse_Engineering.svg  style="width:32px;"> L\'[atelier Reverse Engineering](Reverse_Engineering_Workbench/fr.md) est destiné à fournir des outils spécifiques pour convertir des formes/solides/mailles en fonctionnalités paramétriques compatibles avec FreeCAD.

-   <img alt="" src=images/Workbench_Robot.svg  style="width:32px;"> L\'[atelier Robot](Robot_Workbench/fr.md) pour étudier les mouvements des robots. Non maintenu pour le moment.

-   <img alt="" src=images/Workbench_Sketcher.svg  style="width:32px;"> L\'[atelier Sketcher](Sketcher_Workbench/fr.md) pour travailler avec des esquisses à géométrie contrainte.

-   <img alt="" src=images/Workbench_Spreadsheet.svg  style="width:32px;"> L\'[atelier Spreadsheet](Spreadsheet_Workbench/fr.md) pour créer et manipuler des données de feuilles de calcul.

-   <img alt="" src=images/Workbench_Surface.svg  style="width:32px;"> L\'[atelier Surface](Surface_Workbench/fr.md) fournit des outils pour créer et modifier des surfaces. Il est similaire à l\'outil [Part Générateur de formes](Part_Builder/fr.md) à partir des arêtes.

-   <img alt="" src=images/Workbench_TechDraw.svg  style="width:32px;"> L\'[atelier TechDraw](TechDraw_Workbench/fr.md) pour produire des dessins techniques à partir de modèles 3D. C\'est le successeur de l\'[atelier Drawing](Drawing_Workbench/fr.md).

-   <img alt="" src=images/Workbench_Test.svg  style="width:32px;"> L\'[atelier Test](Testing/fr.md) est destiné au débogage de FreeCAD.

Les ateliers déconcertent souvent les nouveaux utilisateurs, car il n\'est pas toujours facile de savoir dans quel atelier chercher un outil spécifique. Mais ils s\'apprennent rapidement et, au bout d\'un certain temps, ils leur paraîtront naturels. Les nouveaux utilisateurs se rendent rapidement compte que les ateliers sont un moyen pratique d\'organiser la multitude d\'outils offerts par FreeCAD. En outre, les ateliers sont entièrement personnalisables.



### L\'interface

Regardons mieux les différentes parties de l\'interface :

<img alt="" src=images/FreeCAD_022_Interface.png  style="width:800px;">

La fenêtre principale de l\'application peut être divisée en 11 sections :

1.  La [zone de vue principale](main_view_area/fr.md) qui peut contenir différentes fenêtres à onglets.
2.  La [vue 3D](3D_view/fr.md), normalement intégrée à la [zone de vue principale](main_view_area/fr.md). La vue 3D est l\'élément central de l\'interface. Elle affiche et permet de manipuler les objets sur lesquels vous travaillez. Il est possible d\'avoir plusieurs vues du même document (ou des mêmes objets) ou d\'avoir plusieurs documents ouverts simultanément. De plus, chaque vue peut être détachée de la fenêtre principale séparément.
3.  L\'onglet Modèle et l\'onglet [Tâches](Task_panel/fr.md).
    1.  L\'onglet Modèle vous montre le contenu et la structure de votre document.
    2.  L\'onglet Tâches est l\'endroit où FreeCAD vous demandera des valeurs spécifiques à l\'atelier et à l\'outil que vous utilisez (par exemple les dimensions d\'un objet).
4.  L\'[éditeur de propriétés](Property_editor/fr.md) qui apparaît lorsque l\'onglet Modèle est actif dans l\'interface. Il permet de gérer les propriétés exposées publiquement des objets du document. Il se compose des sections Data et View, qui présentent respectivement les propriétés de visualisation et les propriétés paramétriques des objets.
5.  La [fenêtre de sélection](Selection_view/fr.md) qui indique les objets ou les sous-éléments d\'objets (sommets, arêtes, faces) qui sont sélectionnés.
6.  La [vue rapport](Report_view/fr.md) où sont affichés les messages, les avertissements et les erreurs.
7.  La [console Python](Python_console/fr.md) où toutes les commandes exécutées sont imprimées et où vous pouvez entrer du code Python.
8.  La [barre d\'état](Status_bar/fr.md) où apparaissent certains messages et infobulles.
9.  La zone de la barre d\'outils, où les barres d\'outils sont ancrées.
10. Le [sélecteur d\'atelier](Std_Workbench.md) où vous sélectionnez l\'[atelier](Workbenches/fr.md) actif.
11. Le [menu standard](Standard_Menu.md) qui contient les opérations de base du programme.

La plupart des panneaux ci-dessus peuvent être cachés ou révélés par **Affichage → Panneaux**.



### Personnalisation de l\'interface 

L\'interface de FreeCAD est conçue pour une personnalisation poussée. Toutes les barres d\'outils et tous les panneaux peuvent être déplacés, empilés ou même ancrés dans diverses configurations selon les préférences de l\'utilisateur. En outre, ils peuvent être fermés puis rouverts selon les besoins. Au-delà de ces capacités, les utilisateurs disposent de nombreuses autres options, notamment la possibilité de créer des barres d\'outils personnalisées avec des outils sélectionnés dans l\'un des ateliers disponibles, et d\'attribuer ou de modifier des raccourcis clavier pour rationaliser le flux de travail. Cette flexibilité permet aux utilisateurs d\'adapter l\'environnement à leurs besoins et préférences spécifiques.

Ces options de personnalisation avancées sont disponibles à partir du menu **Outils → Personnaliser...** :

<img alt="" src=images/FreeCAD_022_Customization.png  style="width:600px;">

**Pour en savoir plus** :

-   [Pour commencer avec FreeCAD](Getting_started/fr.md)
-   [Personnalisation de l\'interface](Interface_Customization/fr.md)
-   [Ateliers](Workbenches/fr.md)
-   [En savoir plus sur Python](https://www.python.org)



---
⏵ [documentation index](../README.md) > Manual:The FreeCAD Interface/fr
