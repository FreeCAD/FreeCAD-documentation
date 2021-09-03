 {{UnfinishedDocu}} <img alt="" src=images/Lattice2_Lattice2.svg  style="width:240px;"> 
*align=center|L'icône de l'atelier externe Lattice2 FreeCAD*

## Préambule


{{VeryImportantMessage|Lattice2 est stable. De nouvelles fonctionnalités peuvent être ajoutées mais aucun changement de rupture n'est censé se produire.}}


{{TOCright}}

Le Lattice2 Workbench est un FreeCAD [Ateliers externes](External_workbenches/fr.md) qui sert à travailler avec des emplacements et des zones d\'emplacements. Il s\'agit d\'une sorte d\'atelier d\'assemblage mais en mettant l\'accent sur les zones. Il n\'y a pas de contraintes et de relations, il n\'y a que des zones de placements qui peuvent être générés, combinés, transformés, superposés et peuplés de formes.

Vous êtes-vous déjà demandé comment créer un assemblage avec FreeCAD? C\'est le but de l\'atelier (y compris l\'étiquetage des objets). De plus, des assemblages éclatés peuvent être réalisés avec l\'établi.

En outre, le plan de travail propose quelques outils à usage général, tels que la rétrogradation paramétrique, les boîtes englobantes, l\'outil d\'informations sur les formes et les outils permettant de travailler avec des collections de formes (composés).

L\'un des grands objectifs de conception de l\'établi est d\'être aussi paramétrique que possible.

## Références

-   Auteur: DeepSOIC
-   Home page: <https://github.com/DeepSOIC/Lattice2>
-   Source code on github: <https://github.com/DeepSOIC/Lattice2>

## Outils

Detail des descriptions dans [Lattice2 Github wiki](https://github.com/DeepSOIC/Lattice2/wiki)

### Barre d\'outils 

![](images/Lattice2-menu-orizz.png ) *Barre d'outils Lattice2*

### Commandes

-   <img alt="" src=images/Lattice2_Placement.svg  style="width:32px;"> [Placement](Lattice2_Placement.md)
    -   <img alt="" src=images/Lattice2_Placement.svg  style="width:24px;"> [Single Placement: Custom](Lattice2_Placement.md)
    -   <img alt="" src=images/Lattice2_Placement.svg  style="width:24px;"> [Single Placement: XY plane](Lattice2_Placement.md)
    -   <img alt="" src=images/Lattice2_Placement.svg  style="width:24px;"> [Single Placement: XZ plane](Lattice2_Placement.md)
    -   <img alt="" src=images/Lattice2_Placement.svg  style="width:24px;"> [Single Placement: YZ plane](Lattice2_Placement.md)
    -   <img alt="" src=images/Lattice2_Placement.svg  style="width:24px;"> [Single Placement: along X](Lattice2_Placement.md)
    -   <img alt="" src=images/Lattice2_Placement.svg  style="width:24px;"> [Single Placement: along Y](Lattice2_Placement.md)
    -   <img alt="" src=images/Lattice2_Placement.svg  style="width:24px;"> [Single Placement: along Z](Lattice2_Placement.md)
    -   <img alt="" src=images/Lattice2_Placement.svg  style="width:24px;"> [Single Placement: Euler angles](Lattice2_Placement.md)
    -   <img alt="" src=images/Lattice2_PlacementFromShape.svg  style="width:32px;"> [Placement of shape: Copy object.Placement](Lattice2_PlacementFromShape.md)
    -   <img alt="" src=images/Lattice2_PlacementFromShape.svg  style="width:32px;"> [Placement of shape: Center of bounding box](Lattice2_PlacementFromShape.md)
    -   <img alt="" src=images/Lattice2_PlacementFromShape.svg  style="width:32px;"> [Placement of shape: Center of mass](Lattice2_PlacementFromShape.md)
    -   <img alt="" src=images/Lattice2_PlacementFromShape.svg  style="width:32px;"> [Placement of shape: Inertial axis system](Lattice2_PlacementFromShape.md)
-   <img alt="" src=images/Lattice2_AttachablePlacement.svg  style="width:32px;"> [Attachable Placement](Lattice2_AttachablePlacement/fr.md)
-   <img alt="" src=images/Lattice2_LinearArray.svg  style="width:32px;"> [Generate linear array](Lattice2_LinearArray.md)
-   <img alt="" src=images/Lattice2_PolarArray.svg  style="width:32px;"> [Generate polar array](Lattice2_PolarArray.md)
-   <img alt="" src=images/Lattice2_ArrayFromShape.svg  style="width:32px;"> [Array from shape](Lattice2_ArrayFromShape.md)
    -   <img alt="" src=images/Lattice2_ArrayFromShape.svg  style="width:32px;"> [Internal placements](Lattice2_ArrayFromShape.md)
    -   <img alt="" src=images/Lattice2_ArrayFromShape.svg  style="width:32px;"> [Center of bounding box](Lattice2_ArrayFromShape.md)
    -   <img alt="" src=images/Lattice2_ArrayFromShape.svg  style="width:32px;"> [Center of mass](Lattice2_ArrayFromShape.md)
    -   <img alt="" src=images/Lattice2_ArrayFromShape.svg  style="width:32px;"> [Inertial axis system](Lattice2_ArrayFromShape.md)
-   <img alt="" src=images/Lattice2_InvertLattice.svg  style="width:32px;"> [Invert lattice](Lattice2_InvertLattice.md)
-   <img alt="" src=images/Lattice2_JoinArrays.svg  style="width:32px;"> [Join arrays](Lattice2_JoinArrays.md)
-   <img alt="" src=images/Lattice2_ArrayFilter.svg  style="width:32px;"> [Array filter](Lattice2_ArrayFilter.md)
    -   <img alt="" src=images/Lattice2_ArrayFilter.svg  style="width:32px;"> [Selected items](Lattice2_ArrayFilter.md)
    -   <img alt="" src=images/Lattice2_ArrayFilter.svg  style="width:32px;"> [Touching](Lattice2_ArrayFilter.md)
    -   <img alt="" src=images/Lattice2_ArrayFilter.svg  style="width:32px;"> [Within distance window](Lattice2_ArrayFilter.md)
    -   <img alt="" src=images/Lattice2_ArrayFilter.svg  style="width:32px;"> [Pointing at shape](Lattice2_ArrayFilter.md)
-   <img alt="" src=images/Lattice2_ExplodeArray.svg  style="width:32px;"> [Explode array](Lattice2_ExplodeArray.md)
-   <img alt="" src=images/Lattice2_ProjectArray.svg  style="width:32px;"> [Project array](Lattice2_ProjectArray.md)
-   <img alt="" src=images/Lattice2_ResampleArray.svg  style="width:32px;"> [Resample array](Lattice2_ResampleArray.md)
-   <img alt="" src=images/Lattice2_PopulateCopiesNormal.svg  style="width:32px;"> [Populate with copies](Lattice2_PopulateCopiesNormal.md)
    -   <img alt="" src=images/Lattice2_PopulateCopiesNormal.svg  style="width:32px;"> [Populate with copies](Lattice2_PopulateCopiesNormal.md)
    -   <img alt="" src=images/Lattice2_PopulateCopiesArray.svg  style="width:32px;"> [Populate with copies: Build array](Lattice2_PopulateCopiesArray.md)
    -   <img alt="" src=images/Lattice2_PopulateCopiesMove.svg  style="width:32px;"> [Moved object](Lattice2_PopulateCopiesMove.md)
-   <img alt="" src=images/Lattice2_PopulateChildrenNormal.svg  style="width:32px;"> [Populate with children](Lattice2_PopulateChildrenNormal.md)
    -   <img alt="" src=images/Lattice2_PopulateChildrenNormal.svg  style="width:32px;"> [Populate with children](Lattice2_PopulateChildrenNormal.md)
    -   <img alt="" src=images/Lattice2_PopulateChildrenArray.svg  style="width:32px;"> [Populate with children: Build array](Lattice2_PopulateChildrenArray.md)
    -   <img alt="" src=images/Lattice2_PopulateChildrenMove.svg  style="width:32px;"> [Moved children](Lattice2_PopulateChildrenMove.md)
-   <img alt="" src=images/Lattice2_ParametricDowngrade.svg  style="width:24px;"> [Parametric downgrade](Lattice2_ParametricDowngrade.md)
    -   <img alt="" src=images/Lattice2_ParametricDowngrade.svg  style="width:24px;"> [Downgrade to ](Lattice2_ParametricDowngrade.md)
    -   <img alt="" src=images/Lattice2_ParametricDowngrade.svg  style="width:24px;"> [Downgrade to Leaves](Lattice2_ParametricDowngrade.md)
    -   <img alt="" src=images/Lattice2_ParametricDowngrade.svg  style="width:24px;"> [Downgrade to CompSolids](Lattice2_ParametricDowngrade.md)
    -   <img alt="" src=images/Lattice2_ParametricDowngrade.svg  style="width:24px;"> [Downgrade to Shells](Lattice2_ParametricDowngrade.md)
    -   <img alt="" src=images/Lattice2_ParametricDowngrade.svg  style="width:24px;"> [Downgrade to OpenWires](Lattice2_ParametricDowngrade.md)
    -   <img alt="" src=images/Lattice2_ParametricDowngrade.svg  style="width:24px;"> [Downgrade to Faces](Lattice2_ParametricDowngrade.md)
    -   <img alt="" src=images/Lattice2_ParametricDowngrade.svg  style="width:24px;"> [Downgrade to Wires](Lattice2_ParametricDowngrade.md)
    -   <img alt="" src=images/Lattice2_ParametricDowngrade.svg  style="width:24px;"> [Downgrade to Edges](Lattice2_ParametricDowngrade.md)
    -   <img alt="" src=images/Lattice2_ParametricDowngrade.svg  style="width:24px;"> [Downgrade to Seam edges](Lattice2_ParametricDowngrade.md)
    -   <img alt="" src=images/Lattice2_ParametricDowngrade.svg  style="width:24px;"> [Downgrade to Non-seam edges](Lattice2_ParametricDowngrade.md)
    -   <img alt="" src=images/Lattice2_ParametricDowngrade.svg  style="width:24px;"> [Downgrade to Vertices](Lattice2_ParametricDowngrade.md)
-   <img alt="" src=images/Lattice2_SubLink.svg  style="width:32px;"> [Sub link](Lattice2_SubLink.md)
-   <img alt="" src=images/Lattice2_MakeCompound.svg  style="width:32px;"> [Make compound](Lattice2_MakeCompound.md)
-   <img alt="" src=images/Lattice2_ExplodeCompound.svg  style="width:32px;"> [Explode compound](Lattice2_ExplodeCompound.md)
-   <img alt="" src=images/Lattice2_FuseCompound.svg  style="width:32px;"> [Fuse compound](Lattice2_FuseCompound.md)
-   <img alt="" src=images/Lattice2_BoundingBox.svg  style="width:32px;"> [Bounding box](Lattice2_BoundingBox.md)
    -   <img alt="" src=images/Lattice2_BoundingBox.svg  style="width:32px;"> [Whole](Lattice2_BoundingBox.md)
    -   <img alt="" src=images/Lattice2_BoundingBoxCompound.svg  style="width:32px;"> [Children](Lattice2_BoundingBoxCompound.md)
-   <img alt="" src=images/Lattice2_ShapeString.svg  style="width:32px;"> [Shape string for array](Lattice2_ShapeString.md)
-   <img alt="" src=images/Lattice2_ParaSeries.svg  style="width:32px;"> [Para series](Lattice2_ParaSeries.md)
-   <img alt="" src=images/Lattice2_Inspect.svg  style="width:32px;"> [Inspect](Lattice2_Inspect.md)
    -   <img alt="" src=images/Lattice2_InspectSelection.svg  style="width:32px;"> [Inspect seletion](Lattice2_InspectSelection.md)
    -   <img alt="" src=images/Lattice2_InspectShape.svg  style="width:32px;"> [Shape info (feature)](Lattice2_InspectShape.md)
-   <img alt="" src=images/Lattice2_SubstituteObject.svg  style="width:32px;"> [Substitute object](Lattice2_SubstituteObject.md)
-   Exposer des liens vers des sous-éléments

Autre

-   Recalcule
    -   <img alt="" src=images/Lattice2_RecomputeMakeFeature.svg  style="width:32px;"> [Make recompute locher object](Lattice2_RecomputeMakeFeature.md):
    -   <img alt="" src=images/Lattice2_RecomputeLock.svg  style="width:32px;"> [Lock recomputes](Lattice2_RecomputeLock.md):
    -   <img alt="" src=images/Lattice2_RecomputeUnlock.svg  style="width:32px;"> [Unlock recomputes](Lattice2_RecomputeUnlock.md):
    -   <img alt="" src=images/Lattice2_RecomputeFeature.svg  style="width:32px;"> [Recompute feature](Lattice2_RecomputeFeature.md):
    -   <img alt="" src=images/Lattice2_RecomputeDocument.svg  style="width:32px;"> [Recompute document](Lattice2_RecomputeDocument.md):
    -   <img alt="" src=images/Lattice2_RecomputeForce.svg  style="width:32px;"> [Force recompute](Lattice2_RecomputeForce.md):
    -   <img alt="" src=images/Lattice2_RecomputeTouch.svg  style="width:32px;"> [Touch selected feature](Lattice2_RecomputeTouch.md):
-   <img alt="" src=images/Lattice2_Lattice2.svg  style="width:32px;"> Lattice2 Workbench icon

## Installation

**Conditions préalables** Lattice2 WB nécessite FreeCAD\>= v0.16.5155.

### Installation Automatique 

depuis v0.17, on peut utiliser le <img alt="" src=images/AddonManager.svg  style="width:24px;"> [Gestionnaire d\'Addon](Addon_Manager/fr.md) pour installer l\' <img alt="" src=images/Lattice2_Lattice2.svg  style="width:24px;"> atelier Lattice2. Utilisez 
**Outils → Gestionnaire d'Addon**

### Installation manuelle 

-   Faites défiler vers le haut de la page et cliquez sur le bouton \'télécharger le zip\'
-   Décompressez le contenu dans un dossier \"Lattice2\" créé dans \\Path\\to\\FreeCAD\\Mod et redémarrez FreeCAD.
-   Notez que InitGui.py (et le reste des fichiers .py) doivent se retrouver directement sous Mod\\Lattice2 (pas sous un répertoire imbriqué comme Mod\\Lattice2\\Lattice2).

Après avoir installé l\'atelier, il devrait apparaître en bas de la liste du sélecteur d\'atelier dans FreeCAD.

## Tutoriels

-   Tutoriels: [Gallery](https://github.com/DeepSOIC/Lattice2/wiki/Gallery)
-   [Tutoriel de base](https://github.com/DeepSOIC/Lattice2/wiki/Basic-Tutorial)
-   [Lattice2 dans PartDesign](https://github.com/DeepSOIC/Lattice2/wiki/PartDesign-Pattern-Tutorial)
-   [Faire un pédalier](https://github.com/DeepSOIC/Lattice2/wiki/Cogset-Tutorial)
-   [Modèles de fonctions dans l\'atelier Lattice2](https://www.youtube.com/watch?v=BXmeEGnhszo) par \@sliptonic

## Liens vers Lattice2 WB 

-   Wiki Lattice2: <https://github.com/DeepSOIC/Lattice2/wiki>
-   Wiki FreeCAD: <https://www.freecadweb.org/wiki/Lattice2_Workbench>
-   Forum FreeCAD: [Lattice workbench - la v2.0 devient stable](http://forum.freecadweb.org/viewtopic.php?t=12464)
-   Galerie: <https://github.com/DeepSOIC/Lattice2/wiki/Gallery>
-   Signaler les bogues: veuillez signaler les bogues sur <https://github.com/DeepSOIC/Lattice2/issues>

## Autres liens intéressants 

-   [Atelier Lattice1 (obsolète)](https://github.com/DeepSOIC/Lattice)
-   [Ateliers externes](External_workbenches/fr.md): Listes des ateliers de FreeCAD.
-   [Macros](Macros_recipes/fr.md)
-   [FreeCAD Portail communautaire](FreeCAD_Community_Portal/fr.md)




[Category:Addons{{\#translation:}}](Category:Addons.md) [Category:External Workbenches{{\#translation:}}](Category:External_Workbenches.md)
