# Mesh Workbench/fr






<img alt="Icône de l\'atelier Mesh" src=images/Workbench_Mesh.svg  style="width:128px;">


{{TOCright}}

## Introduction

L\'<img alt="" src=images/Workbench_Mesh.svg  style="width:24px;"> [atelier Mesh](Mesh_Workbench/fr.md) manipule des [maillages triangulés](http://fr.wikipedia.org/wiki/Triangle_mesh). Les maillages (on utilise aussi le mot anglais [mesh](http://fr.wikipedia.org/wiki/Mesh_(Objet))) sont un type particulier d\'objets 3D, composés de triangles connectés par leurs arêtes et leurs sommets (aussi appelés vertices).

De nombreuses applications 3D utilisent les mailles comme leur principal type d\'objet 3D, comme [SketchUp](http://en.wikipedia.org/wiki/Sketchup), [Blender](http://en.wikipedia.org/wiki/Blender_(software)) , [maya](http://en.wikipedia.org/wiki/Maya_(software)) ou [3D Studio Max](http://en.wikipedia.org/wiki/3d_max), utilisent des maillages comme type principal d\'objet 3D. Puisque les mailles sont des objets très simples, ne contenant que des sommets (points), des bords et des faces (triangulaires), elles sont très faciles à créer, modifier, subdiviser, étirer, et peuvent facilement être transmises d\'une application à l\'autre sans aucune perte. D\'ailleurs, comme ils contiennent des données très simples, les applications 3D peuvent généralement gérer de très grandes quantités d\'entre elles sans aucun problème. Pour ces raisons, les mailles sont souvent le type d\'objet 3D choisies pour les applications travaillant avec des films, des animations, et la création d\'image.

Cependant, dans le domaine de l\'ingénierie, les maillages présentent une grande limitation: ils ne peuvent pas définir avec précision les surfaces courbes. C\'est pourquoi FreeCAD s\'appuie à la place sur [Brep](https://fr.wikipedia.org/wiki/B-Rep). L\'atelier de maillage propose certaines commandes pour manipuler directement les maillages, mais il est le plus souvent utilisé pour importer des données de maillage 3D et les convertir en solide à utiliser avec l\'<img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [atelier Part](Part_Workbench/fr.md) ou l\'<img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [atelier PartDesign](PartDesign_Workbench/fr.md).

<img alt="" src=images/Mesh_example.jpg  style="width:500px;">

## Outils

Tous les outils de l\'atelier Mesh sont accessibles depuis le menu **Maillages**. Presque tous sont également disponibles dans l\'une des barres d\'outils Mesh.

-   <img alt="" src=images/Mesh_Import.svg  style="width:32px;"> [Importer un maillage\...](Mesh_Import/fr.md): Importe un objet maillé depuis un fichier.

-   <img alt="" src=images/Mesh_Export.svg  style="width:32px;"> [Exporter le maillage\...](Mesh_Export/fr.md): Exporte un objet maillé depuis un fichier.

-   <img alt="" src=images/Mesh_FromPartShape.svg  style="width:32px;"> [Créer un maillage à partir d\'une forme\...](Mesh_FromPartShape/fr.md): Crée des objets maillés à partir de la forme d\'objets.

-   <img alt="" src=images/Mesh_RemeshGmsh.svg  style="width:32px;"> [Affinage\...](Mesh_RemeshGmsh/fr.md): Affine un objet maillé. {{Version/fr|0.19}}

-   Analyse
    -   <img alt="" src=images/Mesh_Evaluation.svg  style="width:32px;"> [Évaluer et réparer le maillage\...](Mesh_Evaluation/fr.md): Evalue et répare un objet maillé.
    -   <img alt="" src=images/Mesh_EvaluateFacet.svg  style="width:32px;"> [Infos sur la face](Mesh_EvaluateFacet/fr.md): Affiche des informations sur les faces des objets maillés.
    -   <img alt="" src=images/Mesh_CurvatureInfo.svg  style="width:32px;"> [Info de courbures](Mesh_CurvatureInfo/fr.md): Affiche la courbure absolue des [objets de courbure](Mesh_VertexCurvature/fr.md) aux points sélectionnés.
    -   <img alt="" src=images/Mesh_BoundingBox.svg  style="width:32px;"> [Boundings info\...](Mesh_BoundingBox.md): Affiche les coordonnées de la boîte de délimitation d\'un objet maillé.
    -   <img alt="" src=images/Mesh_EvaluateSolid.svg  style="width:32px;"> [Vérification du maillage du solide](Mesh_EvaluateSolid/fr.md): Vérifie si un objet maillé est solide.
    -   <img alt="" src=images/Mesh_BoundingBox.svg  style="width:32px;"> [Boîte englobante](Mesh_BoundingBox/fr.md): Affiche les coordonnées de la boîte englobante d\'un objet maillé.

-   <img alt="" src=images/Mesh_VertexCurvature.svg  style="width:32px;"> [Tracé de courbure](Mesh_VertexCurvature/fr.md): Crée des objets maillés de courbure pour les objets maillés.

-   <img alt="" src=images/Mesh_HarmonizeNormals.svg  style="width:32px;"> [Harmoniser les normales](Mesh_HarmonizeNormals/fr.md): harmonise les normales d\'objets maillés.

-   <img alt="" src=images/Mesh_FlipNormals.svg  style="width:32px;"> [Inverser les normales](Mesh_FlipNormals/fr.md): Inverse les normales d\'objets maillés.

-   <img alt="" src=images/Mesh_FillupHoles.svg  style="width:32px;"> [Remplir les trous\...](Mesh_FillupHoles/fr.md): Remplit les trous dans des objets maillés.

-   <img alt="" src=images/Mesh_FillInteractiveHole.svg  style="width:32px;"> [Boucher un trou](Mesh_FillInteractiveHole/fr.md): Remplit des trous sélectionnés d\'objets maillés.

-   <img alt="" src=images/Mesh_AddFacet.svg  style="width:32px;">[Ajouter un triangle](Mesh_AddFacet/fr.md): Ajoute des faces le long de la limite d\'un objet maillé ouvert.

-   <img alt="" src=images/Mesh_RemoveComponents.svg  style="width:32px;"> [Supprimer des composants\...](Mesh_RemoveComponents/fr.md): Supprime des faces d\'objets maillés.

-   <img alt="" src=images/Mesh_RemoveCompByHand.svg  style="width:32px;"> [Supprimer manuellement des composants\...](Mesh_RemoveCompByHand/fr.md): Supprime des composants d\'objets maillés.

-   <img alt="" src=images/Mesh_Segmentation.svg  style="width:32px;"> [Diviser le maillage\...](Mesh_Segmentation/fr.md): Crée des segments maillés séparés pour des types de surface spécifiés d\'un objet maillé.

-   <img alt="" src=images/Mesh_SegmentationBestFit.svg  style="width:32px;"> [Crée des segments de maillage à partir des surfaces les mieux ajustées\...](Mesh_SegmentationBestFit/fr.md): Crée des segments maillés séparés pour des types de surface spécifiés d\'un objet maillé.

-   <img alt="" src=images/Mesh_Smoothing.svg  style="width:32px;"> [Lisser\...](Mesh_Smoothing/fr.md): Lisse des objets maillés.

-   <img alt="" src=images/Mesh_Decimating.svg  style="width:32px;"> [Décimation\...](Mesh_Decimating/fr.md): Réduit le nombre de faces dans les objets maillés. {{Version/fr|0.19}}

-   <img alt="" src=images/Mesh_Scale.svg  style="width:32px;"> [Echelle\...](Mesh_Scale/fr.md): Met à l\'échelle les objets maillés.

-   <img alt="" src=images/Mesh_BuildRegularSolid.svg  style="width:32px;"> [Solide régulier\...](Mesh_BuildRegularSolid/fr.md): Crée un objet maillé solide paramétrique régulier.

-   Opérations Booléennes
    -   <img alt="" src=images/Mesh_Union.svg  style="width:32px;"> [Union](Mesh_Union/fr.md): Crée un objet maillé qui est l\'union de deux objets maillés.
    -   <img alt="" src=images/Mesh_Intersection.svg  style="width:32px;"> [Intersection](Mesh_Intersection/fr.md): Crée un objet maillé qui est l\'intersection de deux objets maillés.
    -   <img alt="" src=images/Mesh_Difference.svg  style="width:32px;"> [Différence](Mesh_Difference/fr.md): Crée un objet maillé qui est la différence de deux objets maillés.

-   Coupe
    -   <img alt="" src=images/Mesh_PolyCut.svg  style="width:32px;"> [Couper le maillage](Mesh_PolyCut/fr.md): Coupe des faces entières à partir des objets maillés.
    -   <img alt="" src=images/Mesh_PolyTrim.svg  style="width:32px;"> [Découper](Mesh_PolyTrim/fr.md): Ajuste les faces et les parties de faces des objets maillés.
    -   <img alt="" src=images/Mesh_TrimByPlane.svg  style="width:32px;"> [Ajuster le maillage avec un plan](Mesh_TrimByPlane/fr.md): Ajuste les faces et les parties de faces d\'un côté d\'un plan à partir d\'un objet maillé.
    -   <img alt="" src=images/Mesh_SectionByPlane.svg  style="width:32px;"> [Créer une section à partir d\'un maillage ou d\'un plan ](Mesh_SectionByPlane/fr.md): Crée une coupe transversale à travers un objet maillé.
    -   <img alt="" src=images/Mesh_CrossSections.svg  style="width:32px;"> [Coupes\...](Mesh_CrossSections/fr.md): Crée plusieurs sections transversales à travers les objets maillés. {{Version/fr|0.19}}

-   <img alt="" src=images/Mesh_Merge.svg  style="width:32px;"> [Fusionner](Mesh_Merge/fr.md): Crée un objet maillé en combinant les mailles d\'au moins deux objets maillés.

-   <img alt="" src=images/Mesh_SplitComponents.svg  style="width:32px;"> [Séparer par composants](Mesh_SplitComponents/fr.md): Divise un objet maillé en ses composants. {{Version/fr|0.19}}

-   <img alt="" src=images/MeshPart_CreateFlatMesh.svg  style="width:32px;"> [Développer un objet maillé](MeshPart_CreateFlatMesh/fr.md): crée une représentation à plat d\'un objet maillé. {{Version/fr|0.19}}

-   <img alt="" src=images/MeshPart_CreateFlatFace.svg  style="width:32px;"> [Développer une face](MeshPart_CreateFlatFace/fr.md): Crée une représentation à plat d\'une face d\'un objet de forme. {{Version/fr|0.19}}

## Préférences

-   Il existe des [préférences d\'exportation liées aux formats Mesh](Import_Export_Preferences/fr#Formats_Mesh.md) mais elles ne s\'appliquent pas à cette commande. Elles sont utilisées par la commande [Std Exporter](Std_Export/fr.md).

Les préférences de l\'atelier Mesh se trouvent dans les catégories suivantes de l\'[Éditeur de propriétés](Property_editor/fr.md):

-   <img alt="" src=images/Preferences-display.svg  style="width:32px;"> [Affichage](Preferences_Editor/fr#Pr.C3.A9f.C3.A9rences_d.27affichage.md): Dans l\'onglet [Vue du maillage](Preferences_Editor/fr#Vue_maillage.md), plusieurs préférences peuvent être définies.
-   <img alt="" src=images/Preferences-openscad.svg  style="width:32px;"> [OpenSCAD](OpenSCAD_Preferences/fr.md): Les commandes [Mesh Union](Mesh_Union.md), [Mesh Intersection](Mesh_Intersection/fr.md) et [Mesh Différence](Mesh_Difference/fr.md) nécessitent [OpenSCAD](http://www.openscad.org/) et utilisez la préférence **OpenSCAD executable** pour trouver son exécutable.

## Remarques

-   D\'autres outils de maillage sont disponibles dans l\'<img alt="" src=images/Workbench_OpenSCAD.svg  style="width:24px;"> [atelier OpenSCAD](OpenSCAD_Workbench/fr.md).
-   Voir [Scripts pour le maillage](Mesh_Scripting/fr.md) pour manipuler et créer des maillages en utilisant [Python](Python/fr.md).
-   Voir aussi [FreeCAD et l\'importation de maillage](FreeCAD_and_Mesh_Import/fr.md)
-   Voir [Asymptote](Asymptote/fr.md) pour exporter des maillages au format Asymptote.





{{Mesh Tools navi

}} 

[Category:Workbenches](Category:Workbenches.md)
