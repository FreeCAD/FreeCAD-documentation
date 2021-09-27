# <img alt="Icône de l\'Atelier Arch" src=images/Workbench_Arch.svg  style="width:64px;"> Arch Workbench/fr


{{TOCright}}

## Introduction

L\'<img alt="" src=images/Workbench_Arch.svg  style="width:24px;"> _) et la production de plans d\'étage 2D en combinaison avec l\'<img alt="" src=images/Workbench_TechDraw.svg  style="width:24px;"> [atelier TechDraw](TechDraw_Workbench/fr.md).

L\'atelier Arch importe tous les outils de l\'<img alt="" src=images/Workbench_Draft.svg  style="width:24px;"> _ et <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [PartDesign](PartDesign_Workbench/fr.md).

La fonctionnalité BIM de FreeCAD est maintenant progressivement divisée en cet atelier Arch qui contient des outils architecturaux de base et l\'<img alt="" src=images/Workbench_BIM.svg  style="width:24px;"> _. Cet atelier BIM ajoute une nouvelle couche d\'interface en plus des outils Arch dans le but de rendre le flux de travail BIM plus intuitif et convivial. Voir [FreeCAD BIM migration guide](https://yorik.uncreated.net/blog/2020-010-freecad-bim-guide).

Les développeurs de Draft, Arch et BIM collaborent également avec la [communauté OSArch](https://osarch.org) dans le but ultime d\'améliorer la conception des bâtiments en utilisant un logiciel entièrement gratuit.

<img alt="" src=images/Screenshot_arch_window.jpg  style="width:600px;">

## Outils

Ces outils permettent la création d\'objets architecturaux.

-   <img alt="" src=images/Arch_Wall.svg  style="width:32px;"> [Mur](Arch_Wall/fr.md) : crée un mur à partir de zéro ou à partir d\'un objet sélectionné.
-   <img alt="" src=images/Arch_CurtainWall.svg  style="width:32px;"> [Mur-rideau](Arch_CurtainWall/fr.md) : crée un mur-rideau à partir de zéro ou en utilisant un objet sélectionné comme base. {{Version/fr|0.19}}
-   <img alt="" src=images/Arch_Structure.svg  style="width:32px;"> [Élément structurel](Arch_Structure/fr.md) : crée un élément de structure à partir de zéro ou à partir d\'un objet sélectionné.

-   <img alt="" src=images/Arch_CompRebarStraight.png  style="width:48px;"> [Outils barres de renfort](Arch_CompRebarStraight/fr.md) : l\'atelier de renforcement augmente les structures d'architecture.
    -   <img alt="" src=images/Arch_Rebar_Straight.png  style="width:32px;"> [Armature droite](Arch_Rebar_Straight/fr.md) : crée une barre de renfort rectiligne dans un élément structurel sélectionné
    -   <img alt="" src=images/Arch_Rebar_UShape.png  style="width:32px;"> [Armature en U](Arch_Rebar_UShape/fr.md) : crée une barre de renfort en U dans un élément structurel sélectionné
    -   <img alt="" src=images/Arch_Rebar_LShape.png  style="width:32px;"> [Armature en L](Arch_Rebar_LShape/fr.md) : crée une barre de renfort en L dans l\'élément de structurel sélectionné
    -   <img alt="" src=images/Arch_Rebar_BentShape.png  style="width:32px;"> [Armature cintrée](Arch_Rebar_BentShape/fr.md): crée une barre de renfort en Z dans l\'élément structurel sélectionné
    -   <img alt="" src=images/Arch_Rebar_Stirrup.png  style="width:32px;"> [Armature en étrier](Arch_Rebar_Stirrup/fr.md) : crée une barre de renfort en forme d\'étrier dans l\'élément structurel sélectionné
    -   <img alt="" src=images/Arch_Rebar_Helical.png  style="width:32px;"> [Armature hélicoïdale](Arch_Rebar_Helical/fr.md) : crée une barre de renfort hélicoïdale dans l\'élément structurel sélectionné
    -   <img alt="" src=images/Arch_Rebar_ColumnReinforcement.png  style="width:32px;"> [Renfort des colonnes d\'armature](Arch_Rebar_ColumnReinforcement/fr.md) : crée des barres d\'armature à l\'intérieur d\'un objet Column Arch Structure.
    -   <img alt="" src=images/Arch_Rebar_ColumnReinforcement.png  style="width:32px;"> [Renfort armature 2 cadres 6 barres](Arch_Rebar_ColumnReinforcement_TwoTiesSixRebars/fr.md) : crée des barres de renforcement à l\'intérieur d\'un objet Column Arch Structure.
    -   <img alt="" src=images/Arch_Rebar_BeamReinforcement.png  style="width:32px;"> [Renfort poutre](Arch_Rebar_BeamReinforcement/fr.md) : crée des barres d\'armature à l\'intérieur d\'un objet Beam Arch Structure.
    -   <img alt="" src=images/Arch_Rebar.svg  style="width:32px;"> [Armature personnalisée](Arch_Rebar/fr.md) : crée une barre d\'armature personnalisée dans un élément structurel sélectionné à l\'aide d\'une esquisse.

-   <img alt="" src=images/Arch_Floor.svg  style="width:32px;"> [Étage](Arch_Floor/fr.md) : crée un étage incluant les objets sélectionnés.
-   <img alt="" src=images/Arch_BuildingPart.svg  style="width:32px;"> [Partie de bâtiment (niveau)](Arch_BuildingPart/fr.md) : crée un composant de bâtiment incluant des objets sélectionnés.
-   <img alt="" src=images/Arch_Building.svg  style="width:32px;"> [Bâtiment](Arch_Building/fr.md) : crée un bâtiment incluant les objets sélectionnés.
-   <img alt="" src=images/Arch_Site.svg  style="width:32px;"> [Site](Arch_Site/fr.md) : crée un site incluant les objets sélectionnés.
-   <img alt="" src=images/Arch_Project.svg  style="width:32px;"> [Project](Arch_Project/fr.md) : crée un projet avec inclusion de l\'objet sélectionné
-   <img alt="" src=images/Arch_Reference.svg  style="width:32px;"> [Référence](Arch_Reference/fr.md) : lie des objets d\'un autre fichier FreeCAD à ce document.
-   <img alt="" src=images/Arch_Window.svg  style="width:32px;"> [Fenêtre](Arch_Window/fr.md) : crée une fenêtre à partir d\'un objet sélectionné.
-   <img alt="" src=images/Arch_SectionPlane.svg  style="width:32px;"> [Plan de coupe](Arch_SectionPlane/fr.md) : ajoute un plan de coupe au document.

-   <img alt="" src=images/Arch_CompAxis.png  style="width:48px;"> [Outils axes](Arch_CompAxis/fr.md) : l\'outil Axe vous permet de placer une série d\'axes dans le document actuel.
    -   <img alt="" src=images/Arch_Axis.svg  style="width:32px;"> [Axes](Arch_Axis/fr.md) : ajoute un (des) Axe(s) dans le document.
    -   <img alt="" src=images/Arch_Axis_System.svg  style="width:32px;"> [Système d\'Axes](Arch_AxisSystem/fr.md) : ajoute un système d\'axes composé de plusieurs axes au document
    -   <img alt="" src=images/Arch_Grid.svg  style="width:32px;"> [Grid](Arch_Grid/fr.md) : ajoute un objet de type grille dans le document

-   <img alt="" src=images/Arch_Roof.svg  style="width:32px;"> [Toiture](Arch_Roof/fr.md) : crée un toit en pente à partir d\'une face sélectionnée.
-   <img alt="" src=images/Arch_Space.svg  style="width:32px;"> [Espace](Arch_Space/fr.md) : crée un objet volume dans le document.
-   <img alt="" src=images/Arch_Stairs.svg  style="width:32px;"> [Escaliers](Arch_Stairs/fr.md) : crée un objet escalier dans le document.

-   <img alt="" src=images/Arch_CompPanel.png  style="width:48px;"> [Outils panneaux](Arch_CompPanel/fr.md) : vous permet de construire toutes sortes d\'éléments de type panneau.
    -   <img alt="" src=images/Arch_Panel.svg  style="width:32px;"> [Panneau](Arch_Panel/fr.md) : crée un objet panneau à partir de zéro ou d\'un objet 2D sélectionné.
    -   <img alt="" src=images/Arch_Panel_Cut.svg  style="width:32px;"> [Découpe de panneau](Arch_Panel_Cut/fr.md) : crée, dans le document 3D, une vue 2D plane pour le découpage d\'un panneau {{Version/fr|0.17}}
    -   <img alt="" src=images/Arch_Panel_Sheet.svg  style="width:32px;"> [Panneau de feuille](Arch_Panel_Sheet/fr.md) : crée une feuille de coupe 2D comprenant des découpes de panneaux ou d\'autres objets 2D {{Version/fr|0.17}}
    -   <img alt="" src=images/Arch_Nest.svg  style="width:32px;"> [Économiseur](Arch_Nest/fr.md) : permet d\'optimiser l\'imbrication de plusieurs objets plats à l\'intérieur d\'un conteneur défini en vue d\'une découpe {{Version/fr|0.17}}

-   <img alt="" src=images/Arch_Frame.svg  style="width:32px;"> [Ossature](Arch_Frame/fr.md) : crée une ossature à partir d\'un objet 2D plan et d\'un profil.
-   <img alt="" src=images/Arch_Fence.svg  style="width:32px;"> [Clôture](Arch_Fence.md) : crée un objet clôture à partir d\'une clôture et d\'un chemin sélectionnés. {{Version/fr|0.19}}
-   <img alt="" src=images/Arch_Truss.svg  style="width:32px;"> [Ferme](Arch_Truss/fr.md) : Crée une ferme à partir d\'une ligne sélectionnée ou à partir de zéro. {{Version/fr|0.19}}
-   <img alt="" src=images/Arch_Equipment.svg  style="width:32px;"> [Équipement](Arch_Equipment/fr.md) : crée un objet équipement à partir d\'un objet sélectionné.
-   <img alt="" src=images/Arch_Profile.svg  style="width:32px;"> [Profilé](Arch_Profile/fr.md) : crée un profilé 2D paramétrique. {{Version/fr|0.19}}

-   <img alt="" src=images/Arch_CompPipe.png  style="width:48px;"> [Outils canalisations](Arch_CompPipe/fr.md) {{Version/fr|0.17}}
    -   <img alt="" src=images/Arch_Pipe.svg  style="width:32px;"> [Tuyaux](Arch_Pipe/fr.md) : crée un tuyau. {{Version/fr|0.17}}
    -   <img alt="" src=images/Arch_PipeConnector.svg  style="width:32px;"> [Connecteur de tuyaux](Arch_PipeConnector/fr.md) : crée un onglet ou une connexion en Té entre deux ou trois tuyaux sélectionnés.

-   <img alt="" src=images/Arch_CompSetMaterial.png  style="width:48px;"> [Outils matériaux](Arch_CompSetMaterial/fr.md) : les outils Matériau permettent d\'ajouter des matériaux au document actif.
    -   <img alt="" src=images/Arch_SetMaterial.svg  style="width:32px;"> [Matériau](Arch_SetMaterial/fr.md) : crée ou modifie l\'attribut matériau de l\'objet sélectionné.
    -   <img alt="" src=images/Arch_MultiMaterial.svg  style="width:32px;"> [Multi-Matériaux](Arch_MultiMaterial/fr.md) : crée un objet multi-matériaux (couches) et l\'attribue aux objets sélectionnés, le cas échéant {{Version/fr|0.17}}
-   <img alt="" src=images/Arch_Schedule.svg  style="width:32px;"> [Feuille de données](Arch_Schedule/fr.md) : permet de collecter dans une feuille de calcul toutes sortes de données.

### Outils de transformation 

Ce sont des outils de modification d\'objets architecturaux.

-   <img alt="" src=images/Arch_CutLine.svg  style="width:32px;"> [Couper suivant une ligne](Arch_CutLine/fr.md) : coupe un objet selon une ligne. {{Version/fr|0.19}}
-   <img alt="" src=images/Arch_CutPlane.svg  style="width:32px;"> [Couper suivant un plan](Arch_CutPlane/fr.md) : coupe un objet selon un plan défini.
-   <img alt="" src=images/Arch_Add.svg  style="width:32px;"> [Ajouter](Arch_Add/fr.md) : ajouter un objet à un composant.
-   <img alt="" src=images/Arch_Remove.svg  style="width:32px;"> [Soustraire](Arch_Remove/fr.md) : soustraire ou effacer un ou des objets d\'un composant.
-   <img alt="" src=images/Arch_Survey.svg  style="width:32px;"> [Prise de cotes](Arch_Survey/fr.md) : permet de prendre rapidement des mesures et des informations sur un modèle.

### Utilitaires

Ce sont des outils supplémentaires, pour vous aider dans des tâches spécifiques.

-   <img alt="" src=images/Arch_Component.svg  style="width:32px;"> [Composant](Arch_Component/fr.md) : crée un composant Arch non paramétrique.
-   <img alt="" src=images/Arch_CloneComponent.svg  style="width:32px;"> _).
-   <img alt="" src=images/Arch_SplitMesh.svg  style="width:32px;"> [Fractionner un maillage](Arch_SplitMesh/fr.md) : fractionne un maillage sélectionné en composants distincts.
-   <img alt="" src=images/Arch_MeshToShape.svg  style="width:32px;"> [Maillage vers une forme](Arch_MeshToShape/fr.md) : convertit un maillage en une forme, unifiant des faces coplanaires.
-   <img alt="" src=images/Arch_SelectNonManifold.svg  style="width:32px;"> [Sélectionner maillages non solides](Arch_SelectNonSolidMeshes/fr.md) : sélectionne tous les maillages non solides dans la sélection en cours ou du document.
-   <img alt="" src=images/Arch_RemoveShape.svg  style="width:32px;"> [Supprimer la forme](Arch_RemoveShape/fr.md) : tente de transformer un objet **arch** basé sur une forme cubique en objet entièrement paramétrique.
-   <img alt="" src=images/Arch_CloseHoles.svg  style="width:32px;"> [Fermer les trous](Arch_CloseHoles/fr.md) : ferme les trous dans une forme sélectionnée.
-   <img alt="" src=images/Arch_MergeWalls.svg  style="width:32px;"> [Fusionner des murs](Arch_MergeWalls/fr.md) : fusionne deux ou plusieurs murs.
-   <img alt="" src=images/Arch_Check.svg  style="width:32px;"> [Vérifier](Arch_Check/fr.md) : vérifie si les objets sélectionnés sont des solides et ne contiennent pas de défauts.
-   <img alt="" src=images/IFC.svg  style="width:32px;"> _.
-   <img alt="" src=images/Arch_ToggleIfcBrepFlag.svg  style="width:32px;"> [Basculer en IFC Brep](Arch_ToggleIfcBrepFlag/fr.md) : force l\'exportation de l\'objet sélectionné en un [IfcFacetedBrep](http://www.buildingsmart-tech.org/ifc/IFC4/final/html/schema/ifcgeometricmodelresource/lexical/ifcfacetedbrep.htm).
-   <img alt="" src=images/Arch_3Views.svg  style="width:32px;"> _.
-   <img alt="" src=images/Arch_IfcSpreadsheet.svg  style="width:32px;"> _ d\'un objet.
-   <img alt="" src=images/Arch_ToggleSubs.svg  style="width:32px;"> [Afficher/Cacher les sous composants](Arch_ToggleSubs/fr.md) : affiche ou cache les sous composants d\'un objet Arch.

### Préférences

-   <img alt="" src=images/Preferences-arch.svg  style="width:32px;"> [Arch Préférences](Arch_Preferences/fr.md) : préférences pour l\'aspect par défaut des murs, des structures, des barres d\'armature, des fenêtres, des escaliers, des panneaux, des tuyaux, des grilles et axes.

### Formats de fichiers 

-   [IFC](Arch_IFC/fr.md) : Industry Foundation Classes
-   [DAE](Arch_DAE/fr.md) : Format de maillage Collada
-   [OBJ](Arch_OBJ/fr.md) : Format mesh (seulement exportation)
-   [JSON](Arch_JSON/fr.md) : JavaScript Object Notation format (seulement exportation)
-   [3DS](Arch_3DS/fr.md) : 3DS format (seulement importation)
-   [SHP](Arch_SHP/fr.md) : Fichiers de formes GIS (seulement importation)

## API

L\'atelier Arch peut être utilisé dans des scripts [Python](Python/fr.md) et dans des [macros](macros/fr.md) grâce aux fonctions [Arch Python API](http://www.freecadweb.org/api/Arch.html).

## Tutoriels

-   [Architecture workflow](http://yorik.uncreated.net/guestblog.php?tag=freecad) : Un exemple de la manière dont FreeCAD peut commencer à avoir sa place préliminaire dans un flux de travail d'architecture.
-   [Tutoriel Arch](Arch_tutorial/fr.md)(v0.14)
-   [Tutoriel Arch sur le blog de Yorik](http://yorik.uncreated.net/guestblog.php?2012=180)(v0.13)
-   [Présentation Vidéo de l\'atelier Arch](https://www.youtube.com/watch?v=lTDOeHapv_E) (2016)
-   [Tutoriel panneaux Arch](Arch_panel_tutorial/fr.md) (v0.15)
-   _
-   [Importation de fichiers STL ou OBJ](Import_from_STL_or_OBJ/fr.md)
-   [Exportation de fichiers STL ou OBJ](Export_to_STL_or_OBJ/fr.md)





 

_

---
[documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > Arch Workbench/fr
