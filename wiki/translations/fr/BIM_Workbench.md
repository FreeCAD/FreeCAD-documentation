# BIM Workbench/fr


 

<img alt="Icône de l\'atelier externe BIM" src=images/IFC.svg  style="width:128px;">


{{TOCright}}

## Introduction

L\'<img alt="" src=images/Workbench_BIM.svg  style="width:24px;"> [atelier BIM](BIM_Workbench/fr.md) est un [atelier externe](External_workbenches/fr.md) visant à implémenter des informations complètes sur le bâtiment [Building Information Modélisation](https://fr.wikipedia.org/wiki/Building_information_modeling) (BIM) et le flux des tâches dans FreeCAD. Il peut être installé à partir du <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Gestionnaire d\'Addon](Std_AddonMgr/fr.md).

L\'atelier BIM est basé sur l\'<img alt="" src=images/Workbench_Arch.svg  style="width:24px;"> [atelier Arch](Arch_Workbench/fr.md) intégré et les deux seront probablement fusionnés à l\'avenir. L\'atelier BIM est un \"méta-atelier\", destiné à rassembler de nombreux outils utiles d\'autres établis en un seul endroit et à créer un flux de travail plus pratique et convivial pour les utilisateurs expérimentés du BIM et les débutants. L\'atelier BIM dispose également de ses propres outils spécifiques, principalement des assistants et des outils de gestion, situés sous le menu **Management**.

Voir le [guide de migration BIM de FreeCAD](https://yorik.uncreated.net/blog/2020-010-freecad-bim-guide) pour un aperçu rapide si vous êtes déjà utilisateur d\'une autre application BIM.

Les développeurs de Draft, Arch et BIM collaborent également avec la [communauté OSArch](https://osarch.org) dans le but ultime d\'améliorer la conception des bâtiments en utilisant un logiciel entièrement gratuit.

<img alt="" src=images/BIM_workbench_presentation.png  style="width:800px;">

## Installation

L\'atelier BIM n\'est pas fourni avec le package FreeCAD par défaut, mais peut être facilement installé via l\'<img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Gestionnaire d\'Addon](Std_AddonMgr/fr.md). Pour le lancer, faire **Outils → [Gestionnaire d'Addon](Std_AddonMgr/fr.md)**. Le code de l\'atelier BIM est [hébergé et développé sur github](https://github.com/yorikvanhavre/BIM_Workbench) et peut également être installé manuellement en le copiant dans le répertoire {{FileName|MOD}} de FreeCAD.

**Remarque**

L\'atelier BIM est en cours de tâche et va changer souvent. Assurez-vous de le mettre à jour régulièrement ! Si le module [Python-Git](https://github.com/chidimo/python-git) est installé, l\'atelier BIM recherchera automatiquement les mises à jour disponibles au démarrage et affichera une icône dans la barre d\'état si une mise à jour est disponible.

Les outils répertoriés ci-dessous peuvent également ne pas tous être présents si votre version de FreeCAD n\'est pas entièrement à jour. L\'atelier BIM devrait cependant fonctionner de manière transparente sur toutes les versions de FreeCAD, il ne supprimera que les outils non disponibles.

## Commencer

<img alt="" src=images/BIM_welcome_screen.png  style="width:800px;">

Lorsque vous démarrez l\'atelier BIM pour la première fois, une boîte de dialogue de bienvenue s\'affiche, donnant un aperçu rapide du fonctionnement de l\'atelier et permettant à l\'utilisateur de démarrer un [tutoriel ludique](BIM_ingame_tutorial/fr.md). Le dialogue de bienvenue est également disponible dans le menu **aide**. Lorsque vous fermez l\'écran de bienvenue en cliquant sur OK, la [Boîte de dialogue configuration BIM](BIM_Setup/fr.md) s\'affiche. Elle permet à l\'utilisateur de définir rapidement certaines des préférences les plus courantes liées à BIM de FreeCAD sans qu\'il soit nécessaire de parcourir les pages complètes des paramètres de préférences FreeCAD.

L\'outil [Configuration du projet BIM](BIM_Project/fr.md) vous permet de configurer rapidement un projet BIM en renseignant certaines informations de base sur votre projet. Vous pouvez ensuite, par exemple, utiliser les différents outils de dessin 2D pour dessiner des repères et des lignes de base, Puis utiliser les différents outils de modélisation 3D pour créer automatiquement des objets BIM 3D à partir d\'eux. Une ligne, par exemple, peut devenir un mur simplement en la sélectionnant et en appuyant sur le bouton [Mur](Arch_Wall/fr.md).

Si vous êtes habitué à une autre application BIM, consultez notre [Tableau de compatibilité des applications BIM](BIM_application_compatibility_table/fr.md) pour connaître vos marques lors du démarrage avec FreeCAD.

<img alt="" src=images/BIM_tutorial_screenshot.png  style="width:800px;">

Le [BIM Tutoriel](BIM_ingame_tutorial/fr.md) est un moyen facile de se mettre rapidement sur la bonne voie avec l\'atelier BIM.

## Outils

L\'atelier BIM regroupe les outils de plusieurs autres ateliers FreeCAD, principalement [Draft](Draft_Workbench/fr.md), [Arch](Arch_Workbench/fr.md) et [Part](Part_Workbench/fr.md), grossièrement réorganisés en catégories logiques: **dessin 2D**, **modélisation 3D**, **annotation** et **modification**. La catégorie **gérer** contient des outils spécifiques à l\'atelier BIM.

De plus, si de tels [Ateliers externes](External_workbenches/fr.md) sont installés, des outils de [Reinforcement](Arch_Rebar/fr.md) (outils de barre de renforcement supplémentaires), [Fixations](Fasteners_Workbench/fr.md) (boulons et vis), [Flamingo/Dodo](Flamingo_Workbench/fr.md) (outils de structure métallique et de tuyauterie) et [Bibliothèque de pièces](Parts_Library/fr.md) sont automatiquement inclus dans l\'atelier BIM.

L\'atelier BIM ajoute également une série d\'éléments dans la **barre d\'état** de FreeCAD et quelques **éléments de menu contextuel**, accessibles en cliquant avec le bouton droit de la souris dans la vue 3D ou dans l\'arborescence.

### Dessin 2D 

Les objets 2D sont couramment utilisés comme aide à la rédaction ou pour tracer des lignes de base et des profils sur lesquels construire des objets BIM. Ils peuvent également être utilisés pour dessiner des symboles et des annotations dans votre modèle. En plus des esquisses, qui utilisent leur propre système de coordonnées, des objets 2D seront dessinés sur le [plan de travail](Draft_SelectPlane/fr.md) sélectionné.

-   <img alt="" src=images/Sketcher_NewSketch.svg  style="width:32px;"> [Nouvelle esquisse](Sketcher_NewSketch/fr.md): Crée une nouvelle esquisse et passe en mode de dessin. Les esquisses sont des objets 2D avancés avec prise en charge des contraintes
-   <img alt="" src=images/Draft_Line.svg  style="width:32px;"> [Ligne](Draft_Line/fr.md) : Trace un segment de ligne à partir de 2 points
-   <img alt="" src=images/Draft_Wire.svg  style="width:32px;"> [Filaire](Draft_Wire/fr.md) : Trace une ligne composée de plusieurs segments de lignes (polyligne)
-   <img alt="" src=images/Draft_Circle.svg  style="width:32px;"> [Cercle](Draft_Circle/fr.md) : Trace un cercle à partir du centre et du rayon
-   <img alt="" src=images/Draft_Arc.svg  style="width:32px;"> [Arc](Draft_Arc/fr.md) : Trace un segment d\'arc à partir du centre, rayon, angle de départ et angle d\'arrivée
-   <img alt="" src=images/Draft_Arc_3Points.svg  style="width:32px;"> [Arc 3Points](Draft_Arc_3Points.md): dessine un segment d\'arc circulaire à partir de trois points situés sur la circonférence
-   <img alt="" src=images/Draft_Ellipse.svg  style="width:32px;"> [Ellipse](Draft_Ellipse/fr.md) : Dessine une ellipse à partir de deux points opposés (coins)
-   <img alt="" src=images/Draft_Polygon.svg  style="width:32px;"> [Polygone](Draft_Polygon/fr.md) : Dessine un polygone régulier à partir du centre et du rayon et nombre de côtés
-   <img alt="" src=images/Draft_Rectangle.svg  style="width:32px;"> [Rectangle](Draft_Rectangle/fr.md) : Trace un rectangle à partir de 2 points opposés
-   <img alt="" src=images/Draft_BSpline.svg  style="width:32px;"> [B-Spline](Draft_BSpline/fr.md) : Dessine une courbe B-Spline à partir d\'une série de points
-   <img alt="" src=images/Draft_CubicBezCurve.svg  style="width:32px;"> [Cubic Bezier Curve](Draft_CubicBezCurve/fr.md): dessine une courbe de Bézier du troisième degré en faisant glisser deux points.
-   <img alt="" src=images/Draft_BezCurve.svg  style="width:32px;"> [Courbes de Bezier](Draft_BezCurve/fr.md): Dessine la courbe de Bézier à partir d\'une série de points
-   <img alt="" src=images/Draft_Point.svg  style="width:32px;"> [Point](Draft_Point/fr.md) : Insère un objet point

### Annotation

Les annotations sont des objets d\'aide visuels pouvant être placés dans votre modèle. Ils peuvent être utilisés pour exporter votre modèle directement vers un format 2D tel que [DXF](Draft_DXF/fr.md), ou être réutilisés lors de la création de vues 2D de votre modèle avec l\'[atelier TechDraw](TechDraw_Workbench/fr.md).

-   <img alt="" src=images/Draft_Text.svg  style="width:32px;"> [Texte](Draft_Text/fr.md) : dessine une annotation en texte multiligne
-   <img alt="" src=images/Draft_ShapeString.svg  style="width:32px;"> [ShapeString](Draft_ShapeString/fr.md) : dessine une ligne de texte comme géométrie
-   <img alt="" src=images/Draft_Dimension.svg  style="width:32px;"> [Cote](Draft_Dimension/fr.md) : trace une cote linéaire, angulaire, radiale ou de diamètre
-   <img alt="" src=images/Draft_Label.svg  style="width:32px;"> [Label](Draft_Label/fr.md): place une étiquette avec une flèche pointant vers un élément sélectionné
-   <img alt="" src=images/Arch_Axis.svg  style="width:32px;"> [Outils axes et grilles](Arch_Axis/fr.md) : crée un axe unique ou un tableau d\'axes dans le sens du document
-   <img alt="" src=images/Arch_Axis_System.svg  style="width:32px;"> [Système d\'axes](Arch_AxisSystem/fr.md) : crée un système d\'axes composé de jusqu\'à 3 séries d\'axes
-   <img alt="" src=images/Arch_Grid.svg  style="width:32px;"> [Grille](Arch_Grid/fr.md) : crée un objet de type grille dans le document
-   <img alt="" src=images/Arch_SectionPlane.svg  style="width:32px;"> [Plan de coupe](Arch_SectionPlane/fr.md): ajoute un plan de coupe au document. Les plans de coupe définissent des vues 2D telles que des plans, des coupes et des élévations
-   <img alt="" src=images/TechDraw_PageDefault.svg  style="width:32px;"> [Page](TechDraw_PageDefault/fr.md): crée une nouvelle page [TechDraw](TechDraw_Workbench/fr.md) à partir d\'un [modèle SVG](TechDraw_Templates/fr.md)
-   <img alt="" src=images/TechDraw_ArchView.svg  style="width:32px;"> [Vue architecturale](TechDraw_ArchView/fr.md): insère une vue d\'un plan de coupe sur une page

### 3D / modélisation BIM 

Les objets 3D et BIM sont les éléments du monde réel qui composeront votre projet BIM.

**Structure du bâtiment**: Ces outils vous aident à organiser votre maquette

-   <img alt="" src=images/Arch_Project.svg  style="width:32px;"> [Projet](Arch_Project/fr.md): Crée un projet comprenant des objets sélectionnés
-   <img alt="" src=images/Arch_Site.svg  style="width:32px;"> [Site](Arch_Site/fr.md): Crée un site incluant les objets sélectionnés.
-   <img alt="" src=images/Arch_Building.svg  style="width:32px;"> [Bâtiment](Arch_Building/fr.md) : Crée un bâtiment incluant les objets sélectionnés.
-   <img alt="" src=images/Arch_BuildingPart.png  style="width:32px;"> [Niveau](Arch_BuildingPart/fr.md) (Partie de bâtiment) : Crée un composant de bâtiment incluant des objets sélectionnés. Les parties de bâtiment sont couramment utilisées pour représenter les niveaux.
-   <img alt="" src=images/Arch_Space.svg  style="width:32px;"> [Espace](Arch_Space/fr.md): Crée un objet spatial dans le document.
-   <img alt="" src=images/Arch_Reference.svg  style="width:32px;"> [Référence](Arch_Reference/fr.md) : Lie des objets d\'un autre fichier FreeCAD à ce document.

**Outils BIM**: Ces outils construisent des composants BIM

-   <img alt="" src=images/Arch_Wall.svg  style="width:32px;"> [Mur](Arch_Wall/fr.md): crée un mur à partir de zéro ou à partir d\'un objet sélectionné comme base.
-   <img alt="" src=images/_Arch_CurtainWall.svg  style="width:32px;"> [Mur-rideau](Arch_CurtainWall/fr.md): crée un mur-rideau à partir de zéro ou en utilisant un objet sélectionné comme base
-   <img alt="" src=images/_BIM_Column.svg  style="width:32px;"> [Colonne](Arch_Structure/fr.md): crée un élément vertical [Structural](Arch_Structure/fr.md) à un point donné en utilisant éventuellement un objet sélectionné comme profil
-   <img alt="" src=images/_BIM_Beam.svg  style="width:32px;"> [Poutre](Arch_Structure/fr.md): crée un élément horizontal [Structural](Arch_Structure/fr.md) entre deux points en utilisant éventuellement un objet sélectionné comme profil
-   <img alt="" src=images/_BIM_Slab.svg  style="width:32px;"> [Dalle](Arch_Structure/fr.md): crée un élément plat [Structural](Arch_Structure/fr.md) en extrudant un objet plat sélectionné
-   <img alt="" src=images/Arch_Rebar_Straight.png  style="width:32px;"> <img alt="" src=images/Arch_Rebar_UShape.png  style="width:32px;"> <img alt="" src=images/Arch_Rebar_LShape.png  style="width:32px;"> <img alt="" src=images/Arch_Rebar_BentShape.png  style="width:32px;"> <img alt="" src=images/Arch_Rebar_Stirrup.png  style="width:32px;"> <img alt="" src=images/Arch_Rebar_ColumnReinforcement.svg  style="width:32px;"> <img alt="" src=images/Arch_Rebar_BeamReinforcement.svg  style="width:32px;"> <img alt="" src=images/Arch_Rebar_Helical.png  style="width:32px;"> <img alt="" src=images/Arch_Rebar.svg  style="width:32px;"> [Armatures](Arch_Rebar/fr.md): crée des barres d\'armature dans un élément de structure sélectionné à l\'aide d\'une esquisse. Nécessite l\'addon [Barres de renfort](Reinforcement_Addon/fr.md).
-   <img alt="" src=images/Arch_Window.svg  style="width:32px;"> [Fenêtre](Arch_Window/fr.md): crée une fenêtre à partir d\'un objet sélectionné comme base.
-   <img alt="" src=images/_BIM_Door.svg  style="width:32px;"> [Porte](Arch_Window/fr.md): crée un objet [Fenêtre](Arch_Window/fr.md) à l\'aide de préréglages de porte.
-   <img alt="" src=images/Arch_Pipe.svg  style="width:32px;"> <img alt="" src=images/Arch_PipeConnector.png  style="width:32px;"> [Outils de canalisations](Arch_Pipe/fr.md) : Crée des tuyaux et une connexion en coin ou en té entre 2 ou 3 tuyaux sélectionnés.
-   <img alt="" src=images/Arch_Stairs.svg  style="width:32px;"> [Escaliers](Arch_Stairs/fr.md): crée un objet escalier dans le document.
-   <img alt="" src=images/Arch_Roof.svg  style="width:32px;"> [Toiture](Arch_Roof/fr.md): crée un toit en pente à partir d\'une face sélectionnée.
-   <img alt="" src=images/Arch_Panel.svg  style="width:32px;"> <img alt="" src=images/Arch_Panel_Cut.svg  style="width:32px;"> <img alt="" src=images/Arch_Panel_Sheet.svg  style="width:32px;"> [Outils pour panneaux](Arch_Panel/fr.md) : Crée des objets panneaux et des découpes 2D à partir de ces panneaux.
-   <img alt="" src=images/Arch_Frame.svg  style="width:32px;"> [Ossature](Arch_Frame/fr.md): crée une ossature à partir d\'un objet 2D plan et d\'un profil.
-   <img alt="" src=images/Arch_Fence.svg  style="width:32px;"> [Clôture](Arch_Fence/fr.md): crée un objet clôture à partir d\'un objet de poteau et d\'un chemin sélectionnés
-   <img alt="" src=images/Arch_Truss.svg  style="width:32px;"> [Ferme](Arch_Truss/fr.md): crée une ferme à partir d\'une ligne sélectionnée ou à partir de zéro
-   <img alt="" src=images/BIM_Library.png  style="width:32px;"> [Bibliothèques](BIM_Library/fr.md): insère un objet d\'équipement ou de mobilier. Requiert l\'addon [Bibliothèque de pièces](Parts_Library/fr.md).
-   <img alt="" src=images/Arch_Component.png  style="width:32px;"> [Composant BIM](Arch_Component/fr.md): transforme tout objet sélectionné en objet BIM avec prise en charge IFC complète.

**Outils 3D génériques**: ces outils créent des objets 3D génériques qui peuvent être transformés ou utilisés en composants BIM.

-   <img alt="" src=images/Arch_Profile.svg  style="width:32px;"> [Profil](Arch_Profile/fr.md): crée un profil 2D paramétrique à utiliser par exemple dans les extrusions
-   <img alt="" src=images/BIM_Box.png  style="width:32px;"> [Boîte](BIM_Box/fr.md): dessine une boîte en spécifiant graphiquement ses dimensions.
-   <img alt="" src=images/Part_Builder.svg  style="width:32px;"> [Générateur de formes](Part_Builder/fr.md): outil avancé de création de formes complexes à partir de diverses primitives géométriques paramétriques.
-   <img alt="" src=images/Draft_Facebinder.svg  style="width:32px;"> [Faces liées](Draft_Facebinder/fr.md): crée un nouvel objet à partir de faces sélectionnées sur des objets existants.

### Outils de modification 

-   <img alt="" src=images/Draft_Move.svg  style="width:32px;"> [Déplacer](Draft_Move/fr.md) : Déplace l\'objet (ou des objets) d\'un emplacement à un autre.
-   <img alt="" src=images/BIM_Copy.png  style="width:32px;"> [Copier](BIM_Copy/fr.md): Copie l\'objet (ou des objets) d\'un emplacement à un autre.
-   <img alt="" src=images/Draft_Rotate.svg  style="width:32px;"> [Rotation](Draft_Rotate/fr.md) : Pivote l\'objet (ou les objets) d\'un angle de départ à un angle d\'arrivée.
-   <img alt="" src=images/Draft_Clone.svg  style="width:32px;"> [Clone](BIM_Clone/fr.md) : Clone les objets sélectionnés.
-   <img alt="" src=images/Draft_Offset.svg  style="width:32px;"> [Décalage](Draft_Offset/fr.md) : Déplace les segments d\'un objet à une certaine distance.
-   <img alt="" src=images/Part_Offset2D.svg  style="width:32px;"> [Décalage 2D](Part_Offset2D/fr.md) : Construit un fil parallèle à une certaine distance de l\'original ou agrandit/réduit une face plane. (version paramétrique)
-   <img alt="" src=images/Draft_Trimex.svg  style="width:32px;"> [Découper/prolonger (Trimex)](Draft_Trimex/fr.md) : Découpe ou prolonge un objet.
-   <img alt="" src=images/Draft_Scale.svg  style="width:32px;"> [Redimensionner](Draft_Scale/fr.md) : Redimensionne l\'objet (ou les objets) sélectionné(s) à partir d\'un point de base.
-   <img alt="" src=images/Draft_Stretch.svg  style="width:32px;"> [Étirer](Draft_Stretch/fr.md) : Étire les objets sélectionnés.
-   <img alt="" src=images/Draft_Array.png  style="width:32px;"> [Réseau](Draft_Array/fr.md) : Crée une matrice polaire ou rectangulaire de l\'objet sélectionné.
-   <img alt="" src=images/Draft_PathArray.png  style="width:32px;"> [Matrice de copies](Draft_PathArray/fr.md) : Crée une série d\'objets le long d\'un tracé (chemin).
-   <img alt="" src=images/Draft_Mirror.svg  style="width:32px;"> [Miroir](Draft_Mirror/fr.md) : Crée un objet miroir des objets sélectionnés.
-   <img alt="" src=images/Part_Extrude.svg  style="width:32px;"> [Extrusion](Part_Extrude/fr.md) : Extrude les faces planes d\'un objet.
-   <img alt="" src=images/Part_Cut.svg  style="width:32px;"> [Soustraction](Part_Cut/fr.md) : Coupe (soustrait) un objet d\'un autre.
-   <img alt="" src=images/Part_Fuse.svg  style="width:32px;"> [Union](Part_Fuse/fr.md) : Union de deux objets.
-   <img alt="" src=images/Part_Common.svg  style="width:32px;"> [Intersection](Part_Common/fr.md) : Extrait la partie commune (intersection) de deux objets.
-   <img alt="" src=images/Part_Compound.svg  style="width:32px;"> [Créer un composé](Part_Compound/fr.md) : Crée un composé à partir des objets sélectionnés.
-   <img alt="" src=images/Part_SimpleCopy.svg  style="width:32px;"> [Créer une copie simple](Part_SimpleCopy/fr.md) : Crée une copie simple de l\'objet sélectionné.
-   <img alt="" src=images/Draft_Upgrade.svg  style="width:32px;"> [Mettre à niveau](Draft_Upgrade/fr.md) : Joint des objets en un objet de plus haut niveau.
-   <img alt="" src=images/Draft_Downgrade.svg  style="width:32px;"> [Rétrograder](Draft_Downgrade/fr.md) : Explose des objets en objets de niveau inférieur.
-   <img alt="" src=images/Draft_Shape2DView.svg  style="width:32px;"> [Projection 2D](Draft_Shape2DView/fr.md) : Génère une projection 2D à partir d\'un objet 3D.
-   <img alt="" src=images/Draft_Draft2Sketch.png  style="width:32px;"> [Draft vers Esquisse](Draft_Draft2Sketch/fr.md) : Convertit un objet Draft en esquisse (Sketcher) et vice versa.
-   <img alt="" src=images/Arch_CutPlane.svg  style="width:32px;"> [Coupe Plane](Arch_CutPlane/fr.md) : Coupe un objet selon un plan défini.
-   <img alt="" src=images/Arch_Add.svg  style="width:32px;"> [Add](Arch_Add/fr.md) : Ajouter un objet à un composant.
-   <img alt="" src=images/Arch_Remove.svg  style="width:32px;"> [Remove](Arch_Remove/fr.md) : Soustraire ou effacer un ou des objets d\'un composant.

### Outils de gestion 

-   <img alt="" src=images/BIM_Setup.png  style="width:32px;"> [Configuration BIM](BIM_Setup/fr.md): configure certaines des préférences FreeCAD les plus couramment utilisées pour le BIM.
-   <img alt="" src=images/BIM_Project.png  style="width:32px;"> [Configuration du Projet](BIM_Project/fr.md): permet de créer des objets de base tels qu\'un [site](Arch_Site/fr.md), un [bâtiment](Arch_Building/fr.md) et des [axes](Arch_Axis/fr.md) en remplissant les informations de base du projet.
-   <img alt="" src=images/BIM_Views.png  style="width:32px;"> [Gestionnaire de vues et de niveaux](BIM_Views/fr.md): gère les différentes vues et niveaux de votre projet.
-   <img alt="" src=images/BIM_Windows.png  style="width:32px;"> [Gestionnaire de fenêtres](BIM_Windows/fr.md): gère les portes et fenêtres de votre projet.
-   <img alt="" src=images/BIM_IfcElements.png  style="width:32px;"> [Gestionnaire d\'éléments IFC](BIM_IfcElements/fr.md): gère la manière dont les différents éléments de votre projet seront exportés vers IFC.
-   <img alt="" src=images/BIM_IfcProperties.svg  style="width:32px;"> [Gestionnaire de propriétés IFC](BIM_IfcProperties/fr.md): gère les propriétés IFC des différents éléments.
-   <img alt="" src=images/BIM_IfcQuantities.svg  style="width:32px;"> [Gestionnaire de quantité IFC](BIM_IfcQuantities/fr.md): gère comment les quantités de vos objets sont explicitement exportées vers IFC.
-   <img alt="" src=images/BIM_Classification.png  style="width:32px;"> [Gestionnaire de classification](BIM_Classification/fr.md): gère le lien entre les objets et les matériaux de votre projet et les systèmes de classification tels que [Uniclass](https://en.wikipedia.org/wiki/Uniclass).
-   <img alt="" src=images/Draft_VisGroup.svg  style="width:32px;"> [Gestionnaire de calques](BIM_Layers/fr.md): gère les calques de votre document.
-   <img alt="" src=images/Arch_Material_Group.svg  style="width:32px;"> [Matériau](Arch_SetMaterial/fr.md): gère les matériaux ou un [multimatériau](Arch_MultiMaterial/fr.md) de l\'objet sélectionné.
-   <img alt="" src=images/Arch_Schedule.svg  style="width:32px;"> [Feuille de données](Arch_Schedule/fr.md): crée différents types de feuilles de données.
-   <img alt="" src=images/BIM_Preflight.svg  style="width:32px;"> [Vérifications préalables](BIM_Preflight/fr.md): effectue différentes vérifications sur votre modèle avant d\'exporter vers IFC.
-   <img alt="" src=images/Draft_AnnotationStyleEditor.svg  style="width:32px;"> [Editeur styles d\'annotations](Draft_AnnotationStyleEditor/fr.md): gère les styles des annotations utilisés par les textes et les cotes.

## Tutoriels et apprentissage 

-   [Tutoriels sur ce wiki Arch & BIM](Tutorials/fr#Architecture_et_BIM.md)
-   [\"BIM with FreeCAD\" série de vidéos de Yorik](https://www.youtube.com/playlist?list=PLmKdGVtV5Vnt2cj4IZIv9FM39QHaE1ZaU)
-   [\"FreeCAD tutorials\" série de vidéos de Regis](https://www.youtube.com/playlist?list=PLDd21g-eSHwkkxVOfVmR8ObpPN5QbL7ye)
-   [\"Quinta Monroy\" série de vidéos de Regis](https://www.youtube.com/playlist?list=PLDd21g-eSHwnAYyutuKhrPY51skaBhrVU)

## Ateliers externes 

Les ateliers FreeCAD sont faciles à programmer en [ Python](Python/fr.md), de ce fait de nombreuses personnes développent des ateliers supplémentaires en dehors des développeurs principaux de FreeCAD.

La page des [ateliers externes](External_workbenches/fr.md) contient des informations et des tutoriels sur certains d'entre eux, et le projet [FreeCAD Addons](https://github.com/FreeCAD/FreeCAD-addons) vise à les rassembler et à les rendre facilement installables depuis FreeCAD.

De nouveaux ateliers sont en développement, restez à l\'écoute !




[Category:Addons](Category:Addons.md) [Category:External Workbenches](Category:External_Workbenches.md) [Category:BIM](Category:BIM.md)
