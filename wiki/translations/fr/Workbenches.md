# Workbenches/fr
FreeCAD, à l\'instar de nombreuses applications de conception modernes telles que [Revit](https://fr.wikipedia.org/wiki/Revit) ou [CATIA](https://fr.wikipedia.org/wiki/CATIA), est basé sur le concept d\'[atelier](https://fr.wikipedia.org/wiki/Établi). Un atelier peut être considéré comme un ensemble d'outils spécialement regroupés pour une tâche donnée. Dans un atelier traditionnel de fabrication de meubles, vous disposeriez d\'une table de travail pour la personne qui travaille le bois, d\'une autre pour celle qui travaille avec des pièces métalliques et peut-être d\'une troisième pour la personne qui monte toutes les pièces ensemble.

Le même principe s\'applique dans FreeCAD. Les outils sont regroupés sous des ateliers, selon des tâches auxquelles ils sont destinés.

Lorsque vous passez d\'un atelier à un autre, les outils disponibles de l\'interface changent. Les barres d\'outils, les barres de commande et éventuellement d\'autres parties de l\'interface passent au nouvel atelier, mais le contenu de votre écran ne change pas. Vous pouvez, par exemple, commencer à dessiner des formes 2D avec l\'atelier Draft, puis les retravailler avec l\'atelier Part.

Remarquez que parfois, un Atelier est aussi appelé *Module*. Cependant, Ateliers et Modules sont deux choses différentes. Un Module est une extension de FreeCAD, tandis qu\'un Atelier est un type particulier de Module avec une interface graphique (GUI) (barres d\'outils et menus).



## Ateliers internes 



### Actuels

Les ateliers suivants sont intégrés à chaque installation de FreeCAD :

-   <img alt="" src=images/Freecad.svg  style="width:32px;"> [Std Base](Std_Base/fr.md). Ce n\'est pas vraiment un atelier mais plutôt une catégorie de commandes et d\'outils \"standards\" qui peuvent être utilisés dans tous les ateliers.

-   <img alt="" src=images/Workbench_Assembly.svg  style="width:32px;"> L\'[atelier Assembly](Assembly_Workbench/fr.md) pour la construction et la résolution d\'assemblages mécaniques. {{Version/fr|1.0}}

-   <img alt="" src=images/Workbench_BIM.svg  style="width:32px;"> L\'[atelier BIM](BIM_Workbench/fr.md) pour travailler avec des éléments architecturaux et créer des modèles [BIM](https://fr.wikipedia.org/wiki/Building_information_modeling). Il combine l\'atelier Arch et l\'ancien atelier BIM externe disponible dans la {{VersionMinus/fr|0.21}}.

-   <img alt="" src=images/Workbench_CAM.svg  style="width:32px;"> L\'[atelier CAM](CAM_Workbench/fr.md) est utilisé pour produire des instructions en G-Code. Cet atelier était appelé \"atelier Path\" {{VersionMinus/fr|0.21}}.

-   <img alt="" src=images/Workbench_Draft.svg  style="width:32px;"> L\'[atelier Draft](Draft_Workbench/fr.md) contient des outils 2D et des opérations de CAO 2D et 3D de base.

-   <img alt="" src=images/Workbench_FEM.svg  style="width:32px;"> L\'[atelier FEM](FEM_Workbench/fr.md) fournit un processus d\'analyse par éléments finis (FEA).

-   <img alt="" src=images/Workbench_Inspection.svg  style="width:32px;"> L\'[atelier Inspection](Inspection_Workbench/fr.md) est fait pour vous donner des outils spécifiques pour l\'examen des formes. Le projet en est encore à ses débuts.

-   <img alt="" src=images/Workbench_Material.svg  style="width:32px;"> L\'[atelier Material](Material_Workbench/fr.md) gère le système des matériaux de FreeCAD. {{Version/fr|1.0}}

-   <img alt="" src=images/Workbench_Mesh.svg  style="width:32px;"> L\'[atelier Mesh](Mesh_Workbench/fr.md) pour travailler avec des maillages triangulés.

-   <img alt="" src=images/Workbench_OpenSCAD.svg  style="width:32px;"> L\'[atelier OpenSCAD](OpenSCAD_Workbench/fr.md) pour l\'interopérabilité avec OpenSCAD et la réparation de l\'historique de modèle de [géométries de construction de solides](Constructive_solid_geometry/fr.md).

-   <img alt="" src=images/Workbench_Part.svg  style="width:32px;"> L\'[atelier Part](Part_Workbench/fr.md) pour travailler avec des primitives géométriques et des opérations booléennes.

-   <img alt="" src=images/Workbench_PartDesign.svg  style="width:32px;"> L\'[atelier PartDesign](PartDesign_Workbench/fr.md) pour créer des formes de pièces à partir d\'esquisses.

-   <img alt="" src=images/Workbench_Points.svg  style="width:32px;"> L\'[atelier Points](Points_Workbench/fr.md) pour travailler avec des nuages de points.

-   <img alt="" src=images/Workbench_Reverse_Engineering.svg  style="width:32px;"> L\'[atelier Reverse Engineering](Reverse_Engineering_Workbench/fr.md) est destiné à fournir des outils spécifiques pour convertir des formes/solides/mailles en fonctionnalités paramétriques compatibles avec FreeCAD.

-   <img alt="" src=images/Workbench_Robot.svg  style="width:32px;"> L\'[atelier Robot](Robot_Workbench/fr.md) pour étudier les mouvements des robots. Non maintenu pour le moment.

-   <img alt="" src=images/Workbench_Sketcher.svg  style="width:32px;"> L\'[atelier Sketcher](Sketcher_Workbench/fr.md) pour travailler avec des esquisses à géométrie contrainte.

-   <img alt="" src=images/Workbench_Spreadsheet.svg  style="width:32px;"> L\'[atelier Spreadsheet](Spreadsheet_Workbench/fr.md) pour créer et manipuler des données de feuilles de calcul.

-   <img alt="" src=images/Workbench_Surface.svg  style="width:32px;"> L\'[atelier Surface](Surface_Workbench/fr.md) fournit des outils pour créer et modifier des surfaces. Il est similaire à l\'outil [Part Générateur de formes](Part_Builder/fr.md), option Face à partir d\'arêtes.

-   <img alt="" src=images/Workbench_TechDraw.svg  style="width:32px;"> L\'[atelier TechDraw](TechDraw_Workbench/fr.md) pour produire des dessins techniques à partir de modèles 3D. C\'est le successeur de l\'[atelier Drawing](Drawing_Workbench/fr.md).

-   <img alt="" src=images/Workbench_Test.svg  style="width:32px;"> L\'[atelier Test](Testing/fr.md) est destiné au débogage de FreeCAD.



### Obsolètes

Les ateliers suivants ne sont plus inclus après la version 0.21 :

-   <img alt="" src=images/Workbench_Start.svg  style="width:32px;"> L\'[atelier Start](Start_Workbench/fr.md) vous permet de passer rapidement à l\'un des ateliers les plus courants.

-   <img alt="" src=images/Workbench_Web.svg  style="width:32px;"> L\'[atelier Web](Web_Workbench/fr.md) vous fournit une fenêtre de navigateur au lieu de la [vue 3D](3D_view/fr.md) dans FreeCAD.

Les ateliers suivants ne sont plus inclus après la version 0.20 :

-   <img alt="" src=images/Workbench_Drawing.svg  style="width:32px;"> L\'[atelier Drawing](Drawing_Workbench/fr.md) était utilisé pour produire des dessins techniques. L\'[atelier TechDraw](TechDraw_Workbench/fr.md) est son remplaçant plus avancé.

-   <img alt="" src=images/Workbench_Image.svg  style="width:32px;"> L\'[atelier Image](Image_Workbench/fr.md) était utilisé pour travailler avec des images bitmap. Ses fonctionnalités ont été intégrées dans [Std Base](Std_Base/fr.md). Voir [Std Importer](Std_Import/fr.md) et [Std Charger une image](Std_ViewLoadImage/fr.md).

-   <img alt="" src=images/Workbench_Raytracing.svg  style="width:32px;"> L\'[atelier Raytracing](Raytracing_Workbench/fr.md) était utilisé pour le lancer de rayons (rendu). L\'atelier externe [Render](https://github.com/FreeCAD/FreeCAD-render) peut être utilisé à la place.



## Ateliers externes 

Les ateliers de FreeCAD sont faciles à programmer en [Python](Python/fr.md). Pour cette raison, plusieurs personnes développent des ateliers additionnels en dehors des principaux développeurs de FreeCAD.

La page des [Ateliers externes](External_workbenches/fr.md) répertorie tout ce qui est connu de cette communauté. La plupart sont facilement installables à partir de FreeCAD, à l'aide du <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Gestionnaire des extensions](Std_AddonMgr/fr.md), situé dans le menu **Outils → Gestionnaire des extensions**.



---
⏵ [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > Workbenches/fr
