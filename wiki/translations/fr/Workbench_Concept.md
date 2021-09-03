




FreeCAD, à l\'instar de nombreuses applications de conception modernes telles que [Revit](wikipedia:Revit.md) ou [CATIA](wikipedia:CATIA.md), est basé sur le concept d\'[Atelier](https://fr.wikipedia.org/wiki/Établi). Un atelier peut être considéré comme un ensemble d'outils spécialement regroupés pour une tâche donnée. Dans un atelier de fabrication de meubles traditionnels, vous disposerez d\'une table de travail pour la personne qui travaille le bois, d\'une autre pour celui qui travaille avec des pièces métalliques et peut-être d\'une troisième pour le gars qui monte toutes les pièces ensemble.

Le même principe s\'applique dans FreeCAD. Les outils sont regroupés sous des ateliers, selon les tâches auxquelles ils sont destinés.

Quand vous basculez d\'un atelier à un autre, les outils disponibles dans l\'interface changent. Les barres d\'outils, les barres de commande et surement d\'autres parties de l\'interface basculent vers le nouvel atelier, mais le contenu de votre scène ne change pas. Vous pouvez par exemple commencer à dessiner des formes 2D dans la planche à dessin, puis continuer à travailler sur ces objets dans l\'atelier Pièce.


<div class="mw-translate-fuzzy">

Remarquez que parfois, un Atelier est aussi appelé un \"Module\". Cependant Atelier et Module sont deux choses différentes. Un Module est une extension de FreeCAD alors qu\'un Atelier est une configuration de l\'interface graphique qui regroupe quelques outils et menus. Habituellement chaque Module contient son propre Atelier, c\'est pour ça que les deux termes sont utilisés.


</div>

## Ateliers internes 


<div class="mw-translate-fuzzy">

Les ateliers suivants sont disponibles sur toutes les installations FreeCAD :


</div>

-   <img alt="" src=images/Freecad.svg  style="width:32px;"> [Std Base](Std_Base.md). This is not really a workbench, but rather a category of \'standard\' commands and tools that can be used in all workbenches.

-   <img alt="" src=images/Workbench_Arch.svg  style="width:32px;"> The [Arch Workbench](Arch_Workbench.md) for working with architectural elements.

-   <img alt="" src=images/Workbench_Draft.svg  style="width:32px;"> The [Draft Workbench](Draft_Workbench.md) contains 2D tools and basic 2D and 3D CAD operations.

-   <img alt="" src=images/Workbench_FEM.svg  style="width:32px;"> The [FEM Workbench](FEM_Workbench.md) provides Finite Element Analysis (FEA) workflow.

-   <img alt="" src=images/Workbench_Image.svg  style="width:32px;"> The [Image Workbench](Image_Workbench.md) for working with bitmap images.

-   <img alt="" src=images/Workbench_Inspection.svg  style="width:32px;"> The [Inspection Workbench](Inspection_Workbench.md) is made to give you specific tools for examination of shapes. It is still under development.

-   <img alt="" src=images/Workbench_Mesh.svg  style="width:32px;"> The [Mesh Workbench](Mesh_Workbench.md) for working with triangulated meshes.

-   <img alt="" src=images/Workbench_OpenSCAD.svg  style="width:32px;"> The [OpenSCAD Workbench](OpenSCAD_Workbench.md) for interoperability with OpenSCAD and repairing [constructive solid geometry](constructive_solid_geometry.md) (CSG) model history.

-   <img alt="" src=images/Workbench_Part.svg  style="width:32px;"> The [Part Workbench](Part_Workbench.md) for working with CAD parts.

-   <img alt="" src=images/Workbench_PartDesign.svg  style="width:32px;"> The [Part Design Workbench](PartDesign_Workbench.md) for building Part shapes from sketches.

-   <img alt="" src=images/Workbench_Path.svg  style="width:32px;"> The [Path Workbench](Path_Workbench.md) is used to produce G-Code instructions. It is still under development.

-   <img alt="" src=images/Workbench_Points.svg  style="width:32px;"> The [Points Workbench](Points_Workbench.md) for working with point clouds.

-   <img alt="" src=images/Workbench_Raytracing.svg  style="width:32px;"> The [Raytracing Workbench](Raytracing_Workbench.md) for working with ray-tracing (rendering).

-   <img alt="" src=images/Workbench_Reverse_Engineering.svg  style="width:32px;"> The [Reverse Engineering Workbench](Reverse_Engineering_Workbench.md) is intended to provide specific tools to convert shapes/solids/meshes into parametric FreeCAD-compatible features. It is still under development.

-   <img alt="" src=images/Workbench_Robot.svg  style="width:32px;"> The [Robot Workbench](Robot_Workbench.md) for studying robot movements.

-   <img alt="" src=images/Workbench_Sketcher.svg  style="width:32px;"> The [Sketcher Workbench](Sketcher_Workbench.md) for working with geometry-constrained sketches.

-   <img alt="" src=images/Workbench_Spreadsheet.svg  style="width:32px;"> The [Spreadsheet Workbench](Spreadsheet_Workbench.md) for creating and manipulating spreadsheet data.

-   <img alt="" src=images/Workbench_Start.svg  style="width:32px;"> The [Start Center Workbench](Start_Workbench.md) allows you to quickly jump to one of the most common workbenches.

-   <img alt="" src=images/Workbench_Surface.svg  style="width:32px;"> The [Surface Workbench](Surface_Workbench.md) provides tools to create and modify surfaces. It is similar as the Part Shape builder Face from edges.

-   <img alt="" src=images/Workbench_TechDraw.svg  style="width:32px;"> The [TechDraw Workbench](TechDraw_Workbench.md) for producing technical drawings from 3D models. It is the successor of the [Drawing Workbench](Drawing_Workbench.md).

-   <img alt="" src=images/Workbench_Test.svg  style="width:32px;"> The [Test Framework Workbench](Testing.md) is for debugging FreeCAD.

-   <img alt="" src=images/Workbench_Web.svg  style="width:32px;"> The [Web Workbench](Web_Workbench.md) provides you with a browser window instead of the [3D view](3D_view.md) within FreeCAD.

### Obsolètes


<div class="mw-translate-fuzzy">

Les ateliers suivants sont toujours inclus dans l\'installation de base à des fins de compatibilité, mais ils ne doivent plus être utilisés.

-   <img alt="" src=images/Workbench_Complete.svg  style="width:32px;"> L\'[Atelier Complete](Complete_Workbench/fr.md) contient toutes les commandes et fonctionnalités de tous les modules et établis répondant à certains critères de qualité. {{Obsolete/fr|0.17}}
-   <img alt="" src=images/Workbench_Drawing.svg  style="width:32px;"> L\'[Atelier Drawing](Drawing_Workbench/fr.md) a été utilisé pour afficher votre travail 3D sur une feuille 2D mais est maintenant obsolète. Il est toujours nécessaire de lire les anciens fichiers FreeCAD contenant un objet Drawing créé à l\'origine avec cet atelier. Voir l\' [Atelier TechDraw](TechDraw_Workbench/fr.md), qui est le remplacent le plus avancé. {{Obsolete/fr|0.17}}


</div>

-   <img alt="" src=images/Workbench_Complete.svg  style="width:32px;"> The [Complete Workbench](Complete_Workbench.md) holds all commands and features from all workbenches that met certain quality criteria. {{Obsolete|0.17}}

-   <img alt="" src=images/Workbench_Drawing.svg  style="width:32px;"> The [Drawing Workbench](Drawing_Workbench.md) was used for producing technical drawings but has now been deprecated. It is still needed to read old FreeCAD files that contain objects created with this workbench. The [TechDraw Workbench](TechDraw_Workbench.md) is its more advanced replacement. {{Obsolete|0.17}}

## Ateliers externes 

Les ateliers de FreeCad sont faciles à programmer en langage [Python](Python/fr.md), il y a pour cette raison plusieurs personnes qui développent des ateliers additionnels en dehors des principaux développeurs de FreeCAD.

La page [ateliers tiers](external_workbenches/fr.md) répertorie tout ce qui est connu de cette communauté. La plupart sont facilement installables à partir de FreeCAD, à l'aide du [Gestionnaire d'addons](Addon_Manager/fr.md), situé dans le menu **Outils → <img src="images/_AddonManager.svg" width=24px>, Gestionnaire d’addons**.

Et d\'autres ateliers sont toujours en développement !

Vous pouvez activer un atelier par le menu **Vue → Atelier**.







[Category:Workbenches{{\#translation:}}](Category:Workbenches.md)
