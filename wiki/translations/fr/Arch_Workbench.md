# <img alt="Icône de l\'Atelier Arch" src=images/Workbench_Arch.svg  style="width:64px;"> Arch Workbench/fr


{{TOCright}}

## Introduction

L\'<img alt="" src=images/Workbench_Arch.svg  style="width:24px;"> [atelier Arch](Arch_Workbench/fr.md) fournit un flux de travail de type [BIM](http://fr.wikipedia.org/wiki/Building_Information_Modeling) à FreeCAD avec des fonctionnalités telles le support des entités architecturales entièrement paramétriques comme les murs, poutres, les toits, les fenêtres, les escaliers, les tuyaux et les meubles. Il prend en charge les fichiers de classes de base de l\'industrie ([IFC](Arch_IFC/fr.md)) et la production de plans d\'étage 2D en combinaison avec l\'<img alt="" src=images/Workbench_TechDraw.svg  style="width:24px;"> [atelier TechDraw](TechDraw_Workbench/fr.md).

L\'atelier Arch importe tous les outils de l\'<img alt="" src=images/Workbench_Draft.svg  style="width:24px;"> [atelier Draft](Draft_Workbench/fr.md) car il utilise ses objets 2D pour créer des objets architecturaux paramétriques 3D. Néanmoins, Arch peut également utiliser des formes solides créées avec d\'autres ateliers tels que <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Part](Part_Workbench/fr.md) et <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [PartDesign](PartDesign_Workbench/fr.md).

La fonctionnalité BIM de FreeCAD est maintenant progressivement divisée en cet atelier Arch qui contient des outils architecturaux de base et l\'<img alt="" src=images/Workbench_BIM.svg  style="width:24px;"> [Atelier BIM](BIM_Workbench/fr.md), disponible depuis le <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Gestionnaire des extensions](Std_AddonMgr/fr.md). Cet atelier BIM ajoute une nouvelle couche d\'interface en plus des outils Arch dans le but de rendre le flux de travail BIM plus intuitif et convivial. Voir [FreeCAD BIM migration guide](https://yorik.uncreated.net/blog/2020-010-freecad-bim-guide).

Les développeurs de Draft, Arch et BIM collaborent également avec la [communauté OSArch](https://osarch.org) dans le but ultime d\'améliorer la conception des bâtiments en utilisant un logiciel entièrement gratuit.

<img alt="" src=images/Screenshot_arch_window.jpg  style="width:600px;">



## Outils

Ces outils permettent la création d\'objets architecturaux.

-   <img alt="" src=images/Arch_Wall.svg  style="width:32px;"> [Mur](Arch_Wall/fr.md) : crée un mur à partir de rien ou en utilisant un objet sélectionné comme base.

-   <img alt="" src=images/Arch_Structure.svg  style="width:32px;"> [Structure](Arch_Structure/fr.md) : crée un élément structurel à partir de rien ou en utilisant un objet sélectionné comme base.

-   <img alt="" src=images/Arch_CompRebarStraight.png  style="width:48px;"> [Armatures](Arch_CompRebarStraight/fr.md) : ces outils ne sont disponibles que si l\'[atelier Reinforcement](Reinforcement_Workbench/fr.md) a été installé.

  -<img alt="" src=images/Arch_Rebar_Straight.svg  style="width:32px;"> [Armature droite](Arch_Rebar_Straight/fr.md) : crée une barre de ferraillage droite dans un élément de structure sélectionné.

  -<img alt="" src=images/Arch_Rebar_UShape.svg  style="width:32px;"> [Armature en U](Arch_Rebar_UShape/fr.md) : crée une barre de ferraillage en forme de U dans un élément de structure sélectionné.

  -<img alt="" src=images/Arch_Rebar_LShape.svg  style="width:32px;"> [Armature en L](Arch_Rebar_LShape/fr.md) : crée une barre de ferraillage en forme de L dans un élément de structure sélectionné.

  -<img alt="" src=images/Arch_Rebar_Stirrup.svg  style="width:32px;"> [Armature en étrier](Arch_Rebar_Stirrup/fr.md) : crée une barre de ferraillage en étriers dans un élément de structure sélectionné.

  -<img alt="" src=images/Arch_Rebar_BentShape.svg  style="width:32px;"> [Armature cintrée](Arch_Rebar_BentShape/fr.md) : crée une barre de ferraillage de forme cintrée dans un élément de structure sélectionné.

  -<img alt="" src=images/Arch_Rebar_Helical.svg  style="width:32px;"> [Armature hélicoïdale](Arch_Rebar_Helical/fr.md) : crée une barre de ferraillage hélicoïdale dans un élément de structure sélectionné.

  - <img alt="" src=images/Arch_Rebar_ColumnReinforcement.svg  style="width:32px;"> [Armature en colonne](Arch_Rebar_ColumnReinforcement/fr.md) : crée des barres de ferraillage dans une colonne rectangulaire sélectionnée.

  - <img alt="" src=images/Arch_Rebar_BeamReinforcement.svg  style="width:32px;"> [Poutre](Arch_Rebar_BeamReinforcement/fr.md) : crée des barres de ferraillage dans une poutre sélectionnée.

  - <img alt="" src=images/Arch_Rebar_Slab_Reinforcement.svg  style="width:32px;"> [Renfort de dalle](Arch_Rebar_Slab_Reinforcement/fr.md) : crée des barres de ferraillage dans une dalle sélectionnée.

  - <img alt="" src=images/Arch_Rebar_Footing_Reinforcement.svg  style="width:32px;"> [Renfort de semelle](Arch_Rebar_Footing_Reinforcement/fr.md) : crée des barres de ferraillage à l\'intérieur d\'une semelle sélectionnée.

  -<img alt="" src=images/Arch_Rebar.svg  style="width:32px;"> [Armature personnalisée](Arch_Rebar/fr.md) : crée une barre de ferraillage personnalisée dans un élément de structure sélectionné à l\'aide d\'une esquisse.

-   <img alt="" src=images/Arch_CurtainWall.svg  style="width:32px;"> [Mur-rideau](Arch_CurtainWall/fr.md) : crée un mur-rideau à partir de rien ou en utilisant un objet sélectionné comme base. {{Version/fr|0.19}}

-   <img alt="" src=images/Arch_BuildingPart.svg  style="width:32px;"> [Partie de bâtiment](Arch_BuildingPart/fr.md) : crée une partie de bâtiment incluant les objets sélectionnés.

-   <img alt="" src=images/Arch_Project.svg  style="width:32px;"> [Projet](Arch_Project/fr.md) : crée un projet incluant les objets sélectionnés.

-   <img alt="" src=images/Arch_Site.svg  style="width:32px;"> [Site](Arch_Site/fr.md) : crée un site incluant les objets sélectionnés.

-   <img alt="" src=images/Arch_Building.svg  style="width:32px;"> [Bâtiment](Arch_Building/fr.md) : crée un bâtiment incluant les objets sélectionnés.

-   <img alt="" src=images/Arch_Floor.svg  style="width:32px;"> [Niveau](Arch_Floor/fr.md) : crée un niveau incluant les objets sélectionnés.

-   <img alt="" src=images/Arch_Reference.svg  style="width:32px;"> [Référence externe](Arch_Reference/fr.md) : lie les objets d\'un autre fichier FreeCAD dans le document en cours.

-   <img alt="" src=images/Arch_Window.svg  style="width:32px;"> [Fenêtre](Arch_Window/fr.md) : crée une fenêtre à partir de rien ou en utilisant un objet sélectionné comme base.

-   <img alt="" src=images/Arch_Roof.svg  style="width:32px;"> [Toit](Arch_Roof/fr.md) : crée un toit incliné à partir d\'une polyligne sélectionnée.

-   <img alt="" src=images/Arch_CompAxis.png  style="width:48px;"> [Outils pour les axes](Arch_CompAxis/fr.md)

  - <img alt="" src=images/Arch_Axis.svg  style="width:32px;"> [Axes](Arch_Axis/fr.md) : ajoute un réseau d\'axes à 1 direction.

  - <img alt="" src=images/Arch_AxisSystem.svg  style="width:32px;"> [Système d\'axes](Arch_AxisSystem/fr.md) : ajoute un système d\'axes composé de plusieurs axes.

  - <img alt="" src=images/Arch_Grid.svg  style="width:32px;"> [Grille](Arch_Grid/fr.md) : ajoute un objet de type grille.

-   <img alt="" src=images/Arch_SectionPlane.svg  style="width:32px;"> [Plan de coupe](Arch_SectionPlane/fr.md) : ajoute un objet plan de coupe.

-   <img alt="" src=images/Arch_Space.svg  style="width:32px;"> [Espace](Arch_Space/fr.md) : crée un objet volume vide.

-   <img alt="" src=images/Arch_Stairs.svg  style="width:32px;"> [Escalier](Arch_Stairs/fr.md) : crée un objet escalier.

-   <img alt="" src=images/Arch_CompPanel.png  style="width:48px;"> [Outils pour les panneaux](Arch_CompPanel/fr.md)

  - <img alt="" src=images/Arch_Panel.svg  style="width:32px;"> [Panneaux](Arch_Panel/fr.md) : crée un objet panneau à partir d\'un objet 2D sélectionné.

  - <img alt="" src=images/Arch_Panel_Cut.svg  style="width:32px;"> [Découpe de panneaux](Arch_Panel_Cut/fr.md) : crée une vue coupée en 2D à partir d\'un panneau.

  - <img alt="" src=images/Arch_Panel_Sheet.svg  style="width:32px;"> [Feuille de panneau](Arch_Panel_Sheet/fr.md) : crée une feuille de découpe 2D comprenant des découpes de panneaux ou d\'autres objets 2D.

  - <img alt="" src=images/Arch_Nest.svg  style="width:32px;"> [Calepinage](Arch_Nest/fr.md) : permet d\'imbriquer plusieurs objets plats à l\'intérieur d\'une forme conteneur.

-   <img alt="" src=images/Arch_Equipment.svg  style="width:32px;"> [Équipement](Arch_Equipment/fr.md) : crée un objet d\'équipement ou de mobilier.

-   <img alt="" src=images/Arch_Frame.svg  style="width:32px;"> [Ossature](Arch_Frame/fr.md) : crée un objet ossature à partir d\'une mise en page sélectionnée.

-   <img alt="" src=images/Arch_Fence.svg  style="width:32px;"> [Clôture](Arch_Fence/fr.md) : crée un objet clôture à partir d\'un poteau et d\'un chemin sélectionnés. {{Version/fr|0.19}}

-   <img alt="" src=images/Arch_Truss.svg  style="width:32px;"> [Treillis](Arch_Truss/fr.md) : crée un treillis à partir d\'une ligne sélectionnée ou de zéro. {{Version/fr|0.19}}

-   <img alt="" src=images/Arch_Profile.svg  style="width:32px;"> [Profilé](Arch_Profile/fr.md) : crée un profilé 2D paramétrique. {{Version/fr|0.19}}

-   <img alt="" src=images/Arch_CompSetMaterial.png  style="width:48px;"> [Outils pour les matériaux](Arch_CompSetMaterial/fr.md)

  - <img alt="" src=images/Arch_SetMaterial.svg  style="width:32px;"> [Matériau](Arch_SetMaterial/fr.md) : crée un matériau et l\'attribue aux objets sélectionnés, le cas échéant.

  - <img alt="" src=images/Arch_MultiMaterial.svg  style="width:32px;"> [Matériaux multiples](Arch_MultiMaterial/fr.md) : crée un multi-matériau et l\'attribue aux objets sélectionnés, le cas échéant.

-   <img alt="" src=images/Arch_Schedule.svg  style="width:32px;"> [Nomenclature](Arch_Schedule/fr.md) : crée différents types de nomenclatures.

-   <img alt="" src=images/Arch_CompPipe.png  style="width:48px;"> [Outils pour la tuyauterie](Arch_CompPipe/fr.md)

  - <img alt="" src=images/Arch_Pipe.svg  style="width:32px;"> [Conduite](Arch_Pipe/fr.md) : crée une conduite.

  - <img alt="" src=images/Arch_PipeConnector.svg  style="width:32px;"> [Raccord](Arch_PipeConnector/fr.md) : crée un raccord en angle ou un raccord en T entre 2 ou 3 conduites sélectionnées.



### Outils de transformation 

Ce sont des outils de modification d\'objets architecturaux.

-   <img alt="" src=images/Arch_CutPlane.svg  style="width:32px;"> [Couper suivant un plan](Arch_CutPlane/fr.md) : découpe un objet en fonction d\'un plan.

-   <img alt="" src=images/Arch_CutLine.svg  style="width:32px;"> [Couper suivant une ligne](Arch_CutLine/fr.md) : découpe un objet en fonction d\'une ligne. {{Version/fr|0.19}}

-   <img alt="" src=images/Arch_Add.svg  style="width:32px;"> [Ajouter](Arch_Add/fr.md) : ajoute des objets à un composant.

-   <img alt="" src=images/Arch_Remove.svg  style="width:32px;"> [Soustraire](Arch_Remove/fr.md) : soustrait ou supprime des objets d\'un composant.

-   <img alt="" src=images/Arch_Survey.svg  style="width:32px;"> [Prendre des cotes](Arch_Survey/fr.md) : permet de rentrer ou de sortir du mode prise de cotes.



### Utilitaires

Ce sont des outils supplémentaires, pour vous aider dans des tâches spécifiques.

-   <img alt="" src=images/Arch_Component.svg  style="width:32px;"> [Composant](Arch_Component/fr.md) : crée un composant Arch non-paramétrique.

-   <img alt="" src=images/Arch_CloneComponent.svg  style="width:32px;"> [Composant de clone](Arch_CloneComponent/fr.md) : produit des composants Arch qui sont des clones d\'objets Arch sélectionnés (à ne pas confondre avec [Draft Clone](Draft_Clone/fr.md)).

-   <img alt="" src=images/Arch_SplitMesh.svg  style="width:32px;"> [Diviser un maillage](Arch_SplitMesh/fr.md) : divise un maillage sélectionné en composants séparés.

-   <img alt="" src=images/Arch_MeshToShape.svg  style="width:32px;"> [Maillage vers une forme](Arch_MeshToShape/fr.md) : convertit un maillage en une forme, en unifiant les faces coplanaires.

-   <img alt="" src=images/Arch_SelectNonSolidMeshes.svg  style="width:32px;"> [Sélection de Sélection de maillages non-manifoldz non-manifold](Arch_SelectNonSolidMeshes/fr.md) : sélectionne tous les maillages non-manifold de la sélection courante ou du document.

-   <img alt="" src=images/Arch_RemoveShape.svg  style="width:32px;"> [Supprimer la forme](Arch_RemoveShape/fr.md) : rend l\'objet Arch basé sur une forme cubique entièrement paramétrique.

-   <img alt="" src=images/Arch_CloseHoles.svg  style="width:32px;"> [Fermer les trous](Arch_CloseHoles/fr.md) : ferme les trous dans un objet de forme sélectionné.

-   <img alt="" src=images/Arch_MergeWalls.svg  style="width:32px;"> [Fusionner des murs](Arch_MergeWalls/fr.md) : fusionne deux ou plusieurs murs.

-   <img alt="" src=images/Arch_Check.svg  style="width:32px;"> [Vérification](Arch_Check/fr.md) : vérifie si les objets sélectionnés sont des solides et ne contiennent pas de défauts.

-   <img alt="" src=images/Arch_ToggleIfcBrepFlag.svg  style="width:32px;"> [Bascule marqueur Brep IFC](Arch_ToggleIfcBrepFlag/fr.md) : force un objet sélectionné à être exporté en tant que [IfcFacetedBrep](http://www.buildingsmart-tech.org/ifc/IFC4/final/html/schema/ifcgeometricmodelresource/lexical/ifcfacetedbrep.htm).

-   <img alt="" src=images/Arch_3Views.svg  style="width:32px;"> [3 Vues à partir d\'un maillage](Arch_3Views/fr.md) : crée des vues de dessus, de face et de côté à partir d\'un [maillage](Mesh_Workbench/fr.md).

-   <img alt="" src=images/Arch_IfcSpreadsheet.svg  style="width:32px;"> [Tableur IFC](Arch_IfcSpreadsheet/fr.md) : crée une feuille de calcul pour stocker les propriétés [IFC](Arch_IFC/fr.md) d\'un objet.

-   <img alt="" src=images/Arch_ToggleSubs.svg  style="width:32px;"> [Bascule des sous composants](Arch_ToggleSubs/fr.md) : affiche ou cache les sous-composants d\'un objet Arch.



### Préférences

-   <img alt="" src=images/Preferences-arch.svg  style="width:32px;"> [Préférences](Arch_Preferences/fr.md) : préférences pour l\'apparence par défaut des murs, structures, armatures, fenêtres, escaliers, panneaux, tuyaux, grilles et axes.



### Formats de fichiers 

-   [IFC](Arch_IFC/fr.md) : Industry Foundation Classes
-   [DAE](Arch_DAE/fr.md) : format de maillage de Collada
-   [OBJ](Arch_OBJ/fr.md) : format de maillage OBJ (seulement en exportation)
-   [JSON](Arch_JSON/fr.md) : JavaScript Object Notation format (seulement en exportation)
-   [3DS](Arch_3DS/fr.md) : format 3DS (seulement en importation)
-   [SHP](Arch_SHP/fr.md) : shapefiles GIS (seulement en importation)

## API

L\'atelier Arch peut être utilisé dans des scripts [Python](Python/fr.md) et dans des [macros](Macros/fr.md) grâce aux fonctions [Arch Python API](Arch_API/fr.md).



## Tutoriels

-   [Migrer de Revit vers FreeCAD](Migrating_to_FreeCAD_from_Revit/fr.md)
-   [Architecture workflow](http://yorik.uncreated.net/guestblog.php?tag=freecad) : un exemple de la manière dont FreeCAD peut commencer à avoir sa place préliminaire dans un flux de travail d'architecture.
-   [Tutoriel Arch](Arch_tutorial/fr.md)(v0.14)
-   [Tutoriel Arch sur le blog de Yorik](http://yorik.uncreated.net/guestblog.php?2012=180)(v0.13)
-   [Présentation Vidéo de l\'atelier Arch](https://www.youtube.com/watch?v=lTDOeHapv_E) (2016)
-   [Tutoriel panneaux Arch](Arch_panel_tutorial/fr.md) (v0.15)
-   [Chapitre sur la modélisation BIM dans le Guide de l\'Utilisateur FreeCAD](Manual:BIM_modeling/fr.md)
-   [Importation de fichiers STL ou OBJ](Import_from_STL_or_OBJ/fr.md)
-   [Exportation de fichiers STL ou OBJ](Export_to_STL_or_OBJ/fr.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > Arch Workbench/fr
