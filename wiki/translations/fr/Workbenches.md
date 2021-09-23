# Workbenches/fr
FreeCAD, à l\'instar de nombreuses applications de conception modernes telles que [Revit](wikipedia:Revit.md) ou [CATIA](wikipedia:CATIA.md), est basé sur le concept d\'[Atelier](https://fr.wikipedia.org/wiki/Établi). Un atelier peut être considéré comme un ensemble d'outils spécialement regroupés pour une tâche donnée. Dans un atelier de fabrication de meubles traditionnels, vous disposerez d\'une table de travail pour la personne qui travaille le bois, d\'une autre pour celui qui travaille avec des pièces métalliques et peut-être d\'une troisième pour le gars qui monte toutes les pièces ensemble.

Le même principe s\'applique dans FreeCAD. Les outils sont regroupés sous des ateliers, selon les tâches auxquelles ils sont destinés.

Quand vous basculez d\'un atelier à un autre, les outils disponibles dans l\'interface changent. Les barres d\'outils, les barres de commande et surement d\'autres parties de l\'interface basculent vers le nouvel atelier, mais le contenu de votre scène ne change pas. Vous pouvez par exemple commencer à dessiner des formes 2D dans la planche à dessin, puis continuer à travailler sur ces objets dans l\'atelier Pièce.

Remarquez que parfois, un Atelier est aussi appelé un \"Module\". Cependant Atelier et Module sont deux choses différentes. Un Module est une extension de FreeCAD, tandis qu\'un Workbench (Atelier) est un type spécial de Module avec une configuration GUI (barres d\'outils et menus).

## Ateliers internes 

Les ateliers suivants sont intégrés à chaque installation de FreeCAD :

-   <img alt="" src=images/Freecad.svg  style="width:32px;"> [Std Base](Std_Base/fr.md). Ce n\'est pas vraiment un atelier mais plutôt une catégorie de commandes et d\'outils \'standards\' qui peuvent être utilisés dans tous les ateliers.

-   <img alt="" src=images/Workbench_Arch.svg  style="width:32px;"> L\'[atelier Arch](Arch_Workbench/fr.md) pour travailler avec des éléments architecturaux.

-   <img alt="" src=images/Workbench_Draft.svg  style="width:32px;"> L\'[atelier Draft](Draft_Workbench/fr.md) contient des outils 2D et des opérations de CAO 2D et 3D de base.

-   <img alt="" src=images/Workbench_FEM.svg  style="width:32px;"> L\'[atelier FEM](FEM_Workbench/fr.md) fournit un flux de travail d\'analyse par éléments finis (FEA).

-   <img alt="" src=images/Workbench_Image.svg  style="width:32px;"> L\'[atelier Image](Image_Workbench/fr.md) pour travailler avec des images bitmap.

-   <img alt="" src=images/Workbench_Inspection.svg  style="width:32px;"> L\'[atelier Inspection](Inspection_Workbench/fr.md) est fait pour vous donner des outils spécifiques pour l\'examen des formes. Il est toujours en cours de développement.

-   <img alt="" src=images/Workbench_Mesh.svg  style="width:32px;"> L\'[atelier Mesh](Mesh_Workbench/fr.md) pour travailler avec des maillages triangulés.

-   <img alt="" src=images/Workbench_OpenSCAD.svg  style="width:32px;"> L\'[atelier OpenSCAD](OpenSCAD_Workbench/fr.md) pour l\'interopérabilité avec OpenSCAD et la réparation de [Géométrie Solide Constructive](Constructive_solid_geometry/fr.md) (CSG).

-   <img alt="" src=images/Workbench_Part.svg  style="width:32px;"> L\'[atelier Part](Part_Workbench/fr.md) pour travailler avec des pièces de CAO.

-   <img alt="" src=images/Workbench_PartDesign.svg  style="width:32px;"> L\'[atelier Part Design](PartDesign_Workbench/fr.md) pour créer des formes de pièces à partir de dessins.

-   <img alt="" src=images/Workbench_Path.svg  style="width:32px;"> L\'[atelier Path](Path_Workbench/fr.md) est utilisé pour produire des instructions en G-code. Il est toujours en cours de développement.

-   <img alt="" src=images/Workbench_Points.svg  style="width:32px;"> L\'[atelier Points](Points_Workbench/fr.md) pour travailler avec des nuages de points.

-   <img alt="" src=images/Workbench_Raytracing.svg  style="width:32px;"> Le [atelier Raytracing](Raytracing_Workbench/fr.md) pour travailler avec le lancer de rayons (rendu).

-   <img alt="" src=images/Workbench_Reverse_Engineering.svg  style="width:32px;"> L\'[atelier Reverse Engineering](Reverse_Engineering_Workbench/fr.md) est destiné à fournir des outils spécifiques pour convertir des formes/solides/mailles en fonctionnalités paramétriques compatibles avec FreeCAD. Il est toujours en cours de développement.

-   <img alt="" src=images/Workbench_Robot.svg  style="width:32px;"> L\'[atelier Robot](Robot_Workbench/fr.md) pour étudier les mouvements des robots.

-   <img alt="" src=images/Workbench_Sketcher.svg  style="width:32px;"> L\'[atelier Sketcher](Sketcher_Workbench/fr.md) pour travailler avec des esquisses à géométrie contrainte.

-   <img alt="" src=images/Workbench_Spreadsheet.svg  style="width:32px;"> L\'[atelier Spreadsheet](Spreadsheet_Workbench/fr.md) pour créer et manipuler des données de feuilles de calcul.

-   <img alt="" src=images/Workbench_Start.svg  style="width:32px;"> L\'[Atelier Start](Start_Workbench/fr.md) vous permet de passer rapidement à l\'un des ateliers les plus courants.

-   <img alt="" src=images/Workbench_Surface.svg  style="width:32px;"> Le [atelier Surface](Surface_Workbench/fr.md) fournit des outils pour créer et modifier des surfaces. Il est similaire à l\'outil Part Générateur de formes à partir des bords.

-   <img alt="" src=images/Workbench_TechDraw.svg  style="width:32px;"> L\'[atelier TechDraw](TechDraw_Workbench/fr.md) pour produire des dessins techniques à partir de modèles 3D. C\'est le successeur de l\'[atelier Drawing](Drawing_Workbench/fr.md).

-   <img alt="" src=images/Workbench_Test.svg  style="width:32px;"> L\'[atelier Test](Testing/fr.md) est destiné au débogage de FreeCAD.

-   <img alt="" src=images/Workbench_Web.svg  style="width:32px;"> L\'[atelier Web](Web_Workbench/fr.md) vous fournit une fenêtre de navigateur au lieu de la [3D view](3D_view/fr.md) dans FreeCAD.

### Obsolètes

Les ateliers suivants sont toujours inclus dans l\'installation de base à des fins de compatibilité, mais ils ne doivent plus être utilisés.

-   <img alt="" src=images/Workbench_Complete.svg  style="width:32px;"> Le [Complete Workbench](Complete_Workbench/fr.md) contient toutes les commandes et fonctionnalités de tous les établis qui ont satisfait à certains critères de qualité. {{Obsolete/fr|0.17}}

-   <img alt="" src=images/Workbench_Drawing.svg  style="width:32px;"> L\'[atelier Drawing](Drawing_Workbench/fr.md) était utilisé pour produire des dessins techniques mais est maintenant déprécié. Il est encore nécessaire pour lire les anciens fichiers FreeCAD qui contiennent des objets créés avec cet atelier. Le [atelier TechDraw](TechDraw_Workbench/fr.md) est son remplaçant plus avancé. {{Obsolete/fr|0.17}}

## Ateliers externes 

Les ateliers de FreeCad sont faciles à programmer en langage [Python](Python/fr.md), il y a pour cette raison plusieurs personnes qui développent des ateliers additionnels en dehors des principaux développeurs de FreeCAD.

La page [ateliers tiers](external_workbenches/fr.md) répertorie tout ce qui est connu de cette communauté. La plupart sont facilement installables à partir de FreeCAD, à l'aide du [Gestionnaire d'addons](Addon_Manager/fr.md), situé dans le menu **Outils → <img src="images/_AddonManager.svg" width=24px>, Gestionnaire d’addons**.

Et d\'autres ateliers sont toujours en développement !

Vous pouvez activer un atelier par le menu **Vue → Atelier**.







[Category:Workbenches](Category:Workbenches.md)

---
[documentation index](../README.md) > Workbenches/fr
