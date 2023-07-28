# <img alt="Icône de l\'atelier Mesh" src=images/Workbench_Mesh.svg  style="width:64px;"> Mesh Workbench/fr


{{TOCright}}



## Introduction

L\'<img alt="" src=images/Workbench_Mesh.svg  style="width:24px;"> [atelier Mesh](Mesh_Workbench/fr.md) manipule des [maillages triangulés](http://fr.wikipedia.org/wiki/Triangle_mesh). Les maillages (on utilise aussi le mot anglais [mesh](http://fr.wikipedia.org/wiki/Mesh_(Objet))) sont un type particulier d\'objets 3D, composés de triangles connectés par leurs arêtes et leurs sommets (aussi appelés vertices).

De nombreuses applications 3D utilisent les mailles comme leur principal type d\'objet 3D, comme [SketchUp](https://fr.wikipedia.org/wiki/SketchUp), [Blender](https://fr.wikipedia.org/wiki/Blender) , [Maya](https://fr.wikipedia.org/wiki/Autodesk_Maya) ou [Studio Max](https://fr.wikipedia.org/wiki/Autodesk_3ds_Max), utilisent les maillages comme principal type d\'objet 3D. Comme les maillages sont des objets très simples, ne contenant que des sommets (points), des arêtes et des faces triangulaires, ils sont très faciles à créer, à modifier, à subdiviser, à étirer, et peuvent facilement passer d\'une application à l\'autre sans perte de détails. En outre, comme les maillages contiennent des données très simples, les applications 3D peuvent généralement en gérer de très grandes quantités sans utiliser beaucoup de ressources. Pour ces raisons, les maillages sont souvent le type d\'objet 3D de choix pour les applications de cinéma, d\'animation et de création d\'images.

Cependant, dans le domaine de l\'ingénierie, les maillages présentent une grande limitation : ils ne peuvent pas définir avec précision les surfaces courbes. C\'est pourquoi FreeCAD s\'appuie à la place sur [Brep](https://fr.wikipedia.org/wiki/B-Rep). L\'atelier de maillage propose certaines commandes pour manipuler directement les maillages, mais il est le plus souvent utilisé pour importer des données de maillage 3D et les convertir en solide à utiliser avec l\'<img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [atelier Part](Part_Workbench/fr.md) ou l\'<img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [atelier PartDesign](PartDesign_Workbench/fr.md).

<img alt="" src=images/Mesh_example.jpg  style="width:500px;">



## Outils

Tous les outils de l\'atelier Mesh sont accessibles depuis le menu **Maillages**. Presque tous sont également disponibles dans l\'une des barres d\'outils Mesh.

-   <img alt="" src=images/Mesh_Import.svg  style="width:32px;"> [Importer un maillage](Mesh_Import/fr.md) : importe un objet maillé depuis un fichier.

-   <img alt="" src=images/Mesh_Export.svg  style="width:32px;"> [Exporter le maillage](Mesh_Export/fr.md) : exporte un objet maillé vers un fichier.

-   <img alt="" src=images/Mesh_FromPartShape.svg  style="width:32px;"> [Créer un maillage](Mesh_FromPartShape/fr.md) : crée des objets maillés à partir de la forme d\'objets.

-   <img alt="" src=images/Mesh_RemeshGmsh.svg  style="width:32px;"> [Affiner](Mesh_RemeshGmsh/fr.md) : remaille plus finement un objet maillé.

-   Analyser
    -   <img alt="" src=images/Mesh_Evaluation.svg  style="width:32px;"> [Evaluation](Mesh_Evaluation/fr.md) : évalue et répare un objet maillé.
    -   <img alt="" src=images/Mesh_EvaluateFacet.svg  style="width:32px;"> [Infos sur la face](Mesh_EvaluateFacet/fr.md) : affiche des informations sur les faces des objets maillés.
    -   <img alt="" src=images/Mesh_CurvatureInfo.svg  style="width:32px;"> [Info de courbures](Mesh_CurvatureInfo/fr.md) : affiche la courbure absolue des [courbures](Mesh_VertexCurvature/fr.md) aux points sélectionnés.
    -   <img alt="" src=images/Mesh_EvaluateSolid.svg  style="width:32px;"> [Solidité du maillage](Mesh_EvaluateSolid/fr.md) : vérifie si un objet maillé est solide.
    -   <img alt="" src=images/Mesh_BoundingBox.svg  style="width:32px;"> [Limites englobantes](Mesh_BoundingBox/fr.md) : affiche les coordonnées de la boîte englobante d\'un objet maillé.

-   <img alt="" src=images/Mesh_VertexCurvature.svg  style="width:32px;"> [Courbure](Mesh_VertexCurvature/fr.md) : crée des objets maillés de courbure pour les objets maillés.

-   <img alt="" src=images/Mesh_HarmonizeNormals.svg  style="width:32px;"> [Harmoniser les normales](Mesh_HarmonizeNormals/fr.md) : harmonise les normales d\'objets maillés.

-   <img alt="" src=images/Mesh_FlipNormals.svg  style="width:32px;"> [Inverser les normales](Mesh_FlipNormals/fr.md) : inverse les normales d\'objets maillés.

-   <img alt="" src=images/Mesh_FillupHoles.svg  style="width:32px;"> [Remplir les trous](Mesh_FillupHoles/fr.md) : remplit les trous dans des objets maillés.

-   <img alt="" src=images/Mesh_FillInteractiveHole.svg  style="width:32px;"> [Boucher un trou](Mesh_FillInteractiveHole/fr.md) : remplit des trous sélectionnés d\'objets maillés.

-   <img alt="" src=images/Mesh_AddFacet.svg  style="width:32px;"> [Ajouter un triangle](Mesh_AddFacet/fr.md) : ajoute des faces le long de la limite d\'un objet maillé ouvert.

-   <img alt="" src=images/Mesh_RemoveComponents.svg  style="width:32px;"> [Supprimer des composants](Mesh_RemoveComponents/fr.md) : supprime des faces d\'objets maillés.

-   <img alt="" src=images/Mesh_RemoveCompByHand.svg  style="width:32px;"> [Supprimer manuellement des composants](Mesh_RemoveCompByHand/fr.md) : supprime des composants d\'objets maillés.

-   <img alt="" src=images/Mesh_Segmentation.svg  style="width:32px;"> [Segmentation](Mesh_Segmentation/fr.md) : crée des segments maillés séparés pour des types de surface spécifiés d\'un objet maillé.

-   <img alt="" src=images/Mesh_SegmentationBestFit.svg  style="width:32px;"> [Segmentation adaptée](Mesh_SegmentationBestFit/fr.md) : crée des segments de maillage distincts pour des types de surface spécifiés d\'un maillage et peut identifier leurs paramètres.

-   <img alt="" src=images/Mesh_Smoothing.svg  style="width:32px;"> [Lissage](Mesh_Smoothing/fr.md) : lisse des objets maillés.

-   <img alt="" src=images/Mesh_Decimating.svg  style="width:32px;"> [Décimation](Mesh_Decimating/fr.md) : réduit le nombre de faces dans les objets maillés.

-   <img alt="" src=images/Mesh_Scale.svg  style="width:32px;"> [Echelle](Mesh_Scale/fr.md) : met à l\'échelle les objets maillés.

-   <img alt="" src=images/Mesh_BuildRegularSolid.svg  style="width:32px;"> [Solide régulier](Mesh_BuildRegularSolid/fr.md) : crée un objet maillé solide paramétrique régulier.

-   Opérations booléennes
    -   <img alt="" src=images/Mesh_Union.svg  style="width:32px;"> [Union](Mesh_Union/fr.md) : crée un objet maillé qui est l\'union de deux objets maillés.
    -   <img alt="" src=images/Mesh_Intersection.svg  style="width:32px;"> [Intersection](Mesh_Intersection/fr.md) : crée un objet maillé qui est l\'intersection de deux objets maillés.
    -   <img alt="" src=images/Mesh_Difference.svg  style="width:32px;"> [Différence](Mesh_Difference/fr.md) : crée un objet maillé qui est la différence de deux objets maillés.

-   Couper
    -   <img alt="" src=images/Mesh_PolyCut.svg  style="width:32px;"> [Couper le maillage](Mesh_PolyCut/fr.md) : coupe des faces entières à partir des objets maillés.
    -   <img alt="" src=images/Mesh_PolyTrim.svg  style="width:32px;"> [Ajuster](Mesh_PolyTrim/fr.md) : ajuste les faces et les parties de faces des objets maillés.
    -   <img alt="" src=images/Mesh_TrimByPlane.svg  style="width:32px;"> [Ajuster par plan](Mesh_TrimByPlane/fr.md) : ajuste les faces et les parties de faces d\'un côté d\'un plan à partir d\'un objet maillé.
    -   <img alt="" src=images/Mesh_SectionByPlane.svg  style="width:32px;"> [Section](Mesh_SectionByPlane/fr.md) : crée une coupe transversale à travers un objet maillé.
    -   <img alt="" src=images/Mesh_CrossSections.svg  style="width:32px;"> [Coupes](Mesh_CrossSections/fr.md) : crée plusieurs sections transversales à travers les objets maillés.

-   <img alt="" src=images/Mesh_Merge.svg  style="width:32px;"> [Fusionner](Mesh_Merge/fr.md) : crée un objet maillé en combinant les mailles d\'au moins deux objets maillés.

-   <img alt="" src=images/Mesh_SplitComponents.svg  style="width:32px;"> [Éclater par composants](Mesh_SplitComponents/fr.md) : divise un objet maillé en ses composants.

-   <img alt="" src=images/MeshPart_CreateFlatMesh.svg  style="width:32px;"> [Développer un maillage](MeshPart_CreateFlatMesh/fr.md) : crée une représentation à plat d\'un objet maillé.

-   <img alt="" src=images/MeshPart_CreateFlatFace.svg  style="width:32px;"> [Développer une face](MeshPart_CreateFlatFace/fr.md) : crée une représentation à plat d\'une face d\'un objet.



## Préférences

-   Il existe des [préférences d\'exportation liées aux formats Mesh](Import_Export_Preferences/fr#Formats_Mesh.md) mais elles ne s\'appliquent pas à cette commande. Elles sont utilisées par la commande [Std Exporter](Std_Export/fr.md).

Les préférences de l\'atelier Mesh se trouvent dans les catégories suivantes de l\'[éditeur de propriétés](Property_editor/fr.md) :

-   <img alt="" src=images/Preferences-display.svg  style="width:32px;"> [Affichage](Preferences_Editor/fr#Pr.C3.A9f.C3.A9rences_d.27affichage.md) : dans l\'onglet [Vue du maillage](Preferences_Editor/fr#Vue_maillage.md), plusieurs préférences peuvent être définies.
-   <img alt="" src=images/Preferences-openscad.svg  style="width:32px;"> [OpenSCAD](OpenSCAD_Preferences/fr.md) : les commandes [Mesh Union](Mesh_Union/fr.md), [Mesh Intersection](Mesh_Intersection/fr.md) et [Mesh Différence](Mesh_Difference/fr.md) nécessitent [OpenSCAD](http://www.openscad.org/) et utilisent la préférence **OpenSCAD executable** pour trouver son exécutable.



## Remarques

-   D\'autres outils de maillage sont disponibles dans l\'<img alt="" src=images/Workbench_OpenSCAD.svg  style="width:24px;"> [atelier OpenSCAD](OpenSCAD_Workbench/fr.md).
-   Voir [Mesh Scripts](Mesh_Scripting/fr.md) pour manipuler et créer des maillages en utilisant [Python](Python/fr.md).
-   Voir aussi [FreeCAD et l\'importation de maillage](FreeCAD_and_Mesh_Import/fr.md)
-   Voir [Asymptote](Asymptote/fr.md) pour exporter des maillages au format Asymptote.





{{Mesh Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > [Mesh](Category_Mesh.md) > Mesh Workbench/fr
