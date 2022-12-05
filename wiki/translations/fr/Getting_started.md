# Getting started/fr
{{TOCright}}

## Avant-propos 

FreeCAD est une [application de modélisation paramétrique](About_FreeCAD/fr.md) 3D. Elle est principalement destinée à la conception mécanique, mais sert aussi à toutes les utilisations où vous avez besoin de modéliser des objets de précision et de contrôler l\'historique de la modélisation 3D.

FreeCAD est en cours de développement depuis 2002 et propose une grande liste de [fonctions](Feature_list/fr.md). Des capacités manquent encore mais il est assez puissant pour une utilisation amateur et de petits ateliers. Il existe une communauté d\'utilisateurs enthousiastes en pleine croissance qui participent au [forum FreeCAD](http://forum.freecadweb.org/index.php) et vous pouvez trouver [nombreux exemples](http://forum.freecadweb.org/viewforum.php?f=24) de projets de qualité développés avec FreeCAD. Voir aussi [FreeCAD utilisé en production](FreeCAD_used_in_production.md).

Comme tous les projets de logiciels libres, FreeCAD dépend de sa communauté pour se développer, gagner en fonctionnalités et corriger les bogues. N\'oubliez pas cela lorsque vous utilisez FreeCAD. Si vous l\'aimez, vous pouvez [faire un don](Donate/fr.md) et [Contribuer à FreeCAD](Help_FreeCAD/fr.md) de diverses manières, comme par exemple rédiger de la documentation et faire des traductions.

Voir aussi :

-   [Migrer vers FreeCAD depuis Fusion360](Migrating_to_FreeCAD_from_Fusion360/fr.md)
-   [Tutoriels](Tutorials/fr.md)
-   [Tutoriels vidéo](Video_tutorials/fr.md)

## Installation

Tout d\'abord (si ce n\'est pas déjà fait) téléchargez et installez FreeCAD. Consultez la page de [téléchargements](Download/fr.md) pour plus d\'informations sur les mises à jour et versions actuelles et les instructions d\'installation pour votre système d\'exploitation ([Windows](Installing_on_Windows/fr.md), [Linux](Installing_on_Linux/fr.md) ou [Mac](Installing_on_Mac/fr.md)). Il y a des paquets d\'installation pour Windows (.msi), pour Debian et Ubuntu (.deb), openSUSE (.rpm) et Mac OSX. FreeCAD est disponible dans les gestionnaires de paquets de plusieurs autres distributions Linux. Une [AppImage](AppImage/fr.md) autonome exécutable est également disponible et fonctionne sur la plupart des systèmes 64 bits Linux récents. FreeCAD est open source et donc vous pouvez également récupérer le code source et le [compiler](Compiling/fr.md) vous-même.

## Explorer l\'interface 

<img alt="" src=images/FreeCAD_interface_base_divisions.svg  style="width:1024px;">



*L'interface standard de FreeCAD*


**Pour une explication complète voir [Interface](Interface/fr.md).**


:   1\. La [zone de vue principale](main_view_area/fr.md), qui peut contenir différentes fenêtres à onglets, principalement la [vue 3D](3D_view/fr.md).
:   2\. La [vue 3D](3D_view/fr.md), affichant les objets géométriques de votre document.
:   3\. La [vue arborescente](Tree_view/fr.md) (partie de la [vue combinée](combo_view/fr.md)), qui montre l\'historique et la hiérarchie de construction des les objets dans votre document ; il peut également afficher le [panneau des tâches](task_panel/fr.md) pour les commandes actives.
:   4\. L\'[éditeur de propriétés](property_editor/fr.md) (partie de la [vue combinée](combo_view/fr.md)), qui vous permet d\'afficher et de modifier les propriétés des objets sélectionnés.
:   5\. Le [panneau de sélection](selection_view/fr.md), qui indique les objets ou les sous-éléments des objets (sommets, arêtes, faces) sélectionnés.
:   6\. La [vue rapport](report_view/fr.md) (ou fenêtre de sortie) qui est la fenêtre où FreeCAD affiche des messages, avertissements et erreurs.
:   7\. La [console Python](Python_console/fr.md), où sont affichées toutes les commandes exécutées par FreeCAD, et qui permet de saisir du code [Python](Python/fr.md).
:   8\. La [barre de status](status_bar/fr.md), où certains messages et info-bulles apparaissent.
:   9\. La zone de la barre d\'outils, où les barres d\'outils sont ancrées.
:   10\. Le [sélecteur d\'atelier](Std_Workbench/fr.md), dans lequel vous sélectionnez l\'[atelier](workbenches/fr.md) actif.
:   11\. Le [menu standard](Standard_Menu/fr.md), qui contient les opérations de base du programme.

Le concept principal de l\'interface FreeCAD est qu\'il est composé d\'[ateliers](workbenches/fr.md). Un atelier est une collection d\'outils adaptés pour une tâche spécifique, comme travailler avec des [maillages](Mesh_Workbench/fr.md), faire du [dessin 2D](Draft_Workbench/fr.md), ou faire des [esquisses contraintes](Sketcher_Workbench/fr.md). Vous pouvez changer l\'[atelier](Std_Workbench.md) actuel avec le sélecteur d\'ateliers (7). Vous pouvez [personnaliser](Interface_Customization/fr.md) les outils inclus dans chaque atelier, ajouter des outils provenant d\'autres ateliers ou même créer vos propres outils, que nous appelons [macros](Macros/fr.md). Les points de départ largement utilisés sont [l\'atelier PartDesign](PartDesign_Workbench/fr.md) et [l\'atelier Part](Part_Workbench/fr.md).

Lorsque vous démarrez FreeCAD pour la première fois, la page Start s\'affiche. Voici son apparence sous la version 0.19 :

<img alt="" src=images/Start_center_0.19_screenshot.png  style="width:600px;">

La page Start permet de passer rapidement à l\'un des ateliers les plus usuels, ouvrir un des fichiers récents ou voir les dernières nouvelles du monde de FreeCAD. Vous pouvez modifier l\'atelier par défaut dans l\'[éditeur de préférences](Preferences_Editor/fr.md).

## Naviguer dans l\'espace 3D 

FreeCAD propose différents [modes de navigation](Mouse_navigation/fr.md), qui changent la façon dont vous utilisez votre souris pour interagir avec les objets de la vue 3D et la vue elle-même. L\'un d\'eux est spécialement conçu pour les [touchpads](Mouse_navigation/fr#Mode_Touchpad.md) où le bouton central de la souris n\'est pas utilisé. Le mode de navigation par défaut est le [mode CAD](Mouse_navigation/fr#Mode_CAD.md). Vous pouvez rapidement changer le mode de navigation utilisé par le bouton **[<img src=images/NavigationCAD_dark.svg style="width:16px">** dans la [barre d\'état](Status_bar/fr.md) ou en cliquant avec le bouton droit de la souris sur une zone vide de la [Vue_3D](3D_view/fr.md).

Plusieurs vue prédéfinies (vue de dessus, vue de face, etc.) sont disponibles dans le menu Affichage, dans la barre d\'outils ainsi que par des raccourcis numériques (**1**, **2**, etc\...). Un clic droit sur un objet ou sur une zone vide de la vue 3D vous donne un accès rapide à certaines opérations courantes, telles que la définition d\'une vue particulière, ou localiser un objet dans l\'arborescence.

## Premiers pas avec FreeCAD 

L\'objectif de FreeCAD est de vous permettre de créer des modèles 3D de haute précision, de maintenir un contrôle serré de ces modèles (être capable de revenir en arrière dans l\'historique de la modélisation et de modifier les paramètres) et finalement de construire ces modèles (via l\'impression 3D, l\'usinage CNC ou même les chantiers de construction). Il est donc très différent des autres applications 3D conçues pour d\'autres fins, tels que le film d\'animation ou les jeux. Sa courbe d\'apprentissage peut être ardue, spécialement si c\'est votre premier contact avec la modélisation 3D. Si vous êtes bloqués à un moment donné, n\'oubliez pas que l\'amicale communauté des utilisateurs du [forum forum de FreeCAD](http://forum.freecadweb.org/index.php) pourrait être en mesure de vous sortir d'embarras sans délai.

L\'atelier que vous utiliserez à l\'aide de FreeCAD dépend du type de travail à effectuer : Si vous travaillez sur des modèles mécaniques, ou plus généralement tous les petits objets, vous aurez probablement envie d\'essayer l\'[atelier PartDesign](PartDesign_Workbench/fr.md). Si vous voulez travailler en 2D, passez à l\'[atelier Draft](Draft_Workbench/fr.md) ou l\'[atelier Sketcher](Sketcher_Workbench/fr.md) si vous avez besoin de contraintes. Si vous voulez faire de la modélisation BIM, lancez l\'[atelier Arch](Arch_Workbench/fr.md). Et si vous venez du monde OpenSCAD, essayez l\'[atelier OpenSCAD](OpenSCAD_Workbench/fr.md). Il existe également de nombreux ateliers développés par la communauté, les [ateliers externes](External_workbenches/fr.md).

Vous pouvez changer d\'atelier à tout moment et aussi changer les [préférences](Interface_Customization/fr.md) de votre atelier favori pour ajouter des outils d\'autres ateliers.

## Travailler avec PartDesign et l\'atelier Sketcher 

L\'atelier [PartDesign](PartDesign_Workbench/fr.md) est spécialement conçu pour construire des objets complexes, à partir de formes simples et en ajoutant ou en supprimant des opérations (que nous appelons \"fonctions\"), jusqu\'à obtention de votre objet final. Toutes les fonctions que vous avez appliquées durant le processus de modélisation sont stockées dans une vue distincte appelée [Vue Modèle](Document_structure/fr.md), qui contient également les autres objets de votre document. Vous pouvez considérer un objet PartDesign comme une succession d\'opérations, chacune appliquée au résultat de la précédente, formant une grande chaîne structurée. Dans l\'arborescence, vous voyez votre objet final, mais vous pouvez développer et récupérer tous les états précédents et modifier leurs paramètres, qui mettent automatiquement à jour l\'objet final.

L\'atelier PartDesign fait un usage intensif d\'un autre atelier, l\'atelier [Sketcher](Sketcher_Workbench/fr.md). Le Sketcher vous permet de dessiner des formes 2D, puis de leur appliquer des contraintes. Par exemple, vous pourriez dessiner un rectangle et définir la taille d\'un côté à l\'aide d\'une contrainte de longueur. Ce côté ne pourra plus être redimensionné (à moins d\'éditer et modifier cette contrainte).

Les formes 2D faites avec le Sketcher servent beaucoup dans l\'atelier PartDesign, par exemple pour extruder des volumes 3D, ou dessiner des zones sur la face de votre objet, qui seront ensuite évidées ou extrudées de son volume principal. Il s\'agit d\'un flux de production typique de PartDesign :

1.  Créez une nouvelle esquisse
2.  Dessinez un profil fermé (assurez-vous que tous les points sont joints)
3.  Fermez l\'esquisse
4.  Extrudez-l\'esquisse en un objet 3D avec l\'outil Protrusion
5.  Sélectionnez une face du solide extrudé
6.  Créez une seconde esquisse (cette fois elle sera dessinée sur la face sélectionnée)
7.  Dessinez un profil fermé
8.  Fermez l\'esquisse
9.  Créez une cavité à partir de la seconde esquisse, sur le premier objet

Ce qui vous donne un objet comme ceci :

<img alt="" src=images/Partdesign_example.jpg  style="width:600px;">

À tout moment, vous pouvez sélectionner les esquisses originales et les modifier, ou changer les paramètres d\'extrusion des opérations de protrusion ou de cavité, qui mettront automatiquement à jour l\'objet final.

## Travailler avec les ateliers Draft et Arch 

Les ateliers [Draft](Draft_Workbench/fr.md) et [Arch](Arch_Workbench/fr.md) se comportent un peu différemment des autres ateliers ci-dessus, bien qu\'ils suivent les mêmes règles communes à l\'ensemble de FreeCAD. En bref, alors que le Sketcher (esquisse) et PartDesign sont faits principalement pour concevoir des pièces uniques, Draft et Arch sont faits pour faciliter votre travail lorsque vous travaillez avec plusieurs objets simples.

L\'[atelier Draft](Draft_Workbench/fr.md) vous propose des outils 2D un peu semblables à ce que vous pouvez trouver dans les applications de CAO 2D traditionnelles telles que [AutoCAD](https://fr.wikipedia.org/wiki/AutoCAD). Cependant, le dessin 2D étant loin du champ d\'application de FreeCAD, ne vous attendez pas à y trouver la gamme complète d\'outils que ces applications offrent. La plupart des outils Draft travaillent non seulement dans un plan 2D, mais également dans l\'espace 3D et bénéficient de systèmes spéciaux d\'assistance tels que les [Plans de travail](Draft_SelectPlane/fr.md) et l\'[aimantation d\'objet](Draft_Snap/fr.md).

L\'[atelier Arch](Arch_Workbench/fr.md) ajoute des outils de modélisation [BIM](http://fr.wikipedia.org/wiki/Building_Information_Modeling) à FreeCAD, vous permettant de construire des modèles architecturaux à partir d\'objets paramétriques. L\'atelier Arch s\'appuie beaucoup sur les autres modules tels que Draft et le Sketcher. Tous les outils Draft sont également présents dans l\'atelier Arch, et la plupart des outils Arch font usage des systèmes d\'assistance Draft.

Le travail typique avec les ateliers Arch et Draft peut être :

1.  Dessiner plusieurs lignes avec l\'outil Draft Line
2.  Sélectionner chaque ligne et cliquer sur l\'outil Mur pour construire un mur sur chacune d\'elle
3.  Sélectionner les murs et les joindre en cliquant sur l\'outil Ajouter un composant
4.  Créer un objet Étage et déplacer vos murs sous celui-ci dans l\'arborescence
5.  Créer un objet Bâtiment et déplacer votre plancher sous celui-ci dans l\'arborescence
6.  Créer une fenêtre en cliquant sur l\'outil Fenêtre, sélectionner un paramètre prédéfini, puis cliquer sur une face d\'un mur
7.  Ajouter des cotes en réglant d\'abord le plan de travail si nécessaire, puis en utilisant l\'outil Cote

Le résultat sera :

<img alt="" src=images/Arch_workflow_example.jpg  style="width:600px;">

Plus d\'informations sur la page [tutoriels](Tutorials/fr.md).

## Addons, Macro et ateliers externe 

FreeCAD, en tant que logiciel open source, offre la possibilité de compléter ses ateliers avec des addons.

Le principe des [extensions](Addon/fr.md) est basé sur le développement d\'un atelier complémentaire. Tout utilisateur peut développer une fonction qu\'il estime manquante pour ses propres besoins ou, finalement, pour la communauté. Avec le forum, l\'utilisateur peut demander un avis, une aide. Il peut partager, ou non, l\'objet de son développement selon les règles du droit d\'auteur à définir. Gratuit pour elle/lui. Pour le développer, l\'utilisateur dispose de fonctions [scriptées](scripting/fr.md).

Il existe deux types d\'addons :

1.  [Macros](Macros/fr.md) : courts extraits de code Python fournissant un nouvel outil ou de nouvelles fonctionnalités. Les macros commencent généralement par simplifier ou automatiser la tâche de dessin ou d\'édition d\'un objet particulier. Si plusieurs de ces macros sont collectées dans un répertoire, l\'intégralité du répertoire peut être distribué en tant que nouveau plan de travail.
2.  [Ateliers externes](External_workbenches/fr.md) : un ensemble d\'outils programmés en Python ou en C++ qui étend FreeCAD de manière importante. Si un atelier est suffisamment développé et bien documenté, il peut être inclus comme l'un des ateliers de base de FreeCAD. Sous [Ateliers externes](External_workbenches/fr.md), vous trouverez le principe et une liste des bibliothèques existantes.

## Script

Et enfin, une des caractéristiques les plus puissantes de FreeCAD est l\'environnement de [programmation de macros](scripting/fr.md). À partir de la console Python intégrée (ou depuis n\'importe quel autre éditeur de macro Python), vous pouvez accéder à presque n\'importe quelle partie de FreeCAD, créer ou modifier la géométrie, modifier la représentation de ces objets dans la scène 3D ou accéder et modifier l\'interface de FreeCAD. Les scripts Python peuvent aussi s\'utiliser par [des Macros](Macros/fr.md), lesquelles fournissent une méthode simple pour créer des commandes personnalisées.

## Nouveautés

-   Voir les [notes de versions](Feature_list/fr#Notes_de_versions.md) pour la liste détaillée des évolutions.





{{Userdocnavi/fr}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Getting started/fr
