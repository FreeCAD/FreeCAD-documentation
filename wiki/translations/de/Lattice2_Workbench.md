# Lattice2 Workbench/de
} <img alt="" src=images/Lattice2_Lattice2.svg  style="width:240px;"> 
*align=center|Das FreeCAD Lattice2 Externer Arbeitsbereichssymbol*

## Einführung


**Lattice2 ist stabil. Es können neue Funktionen hinzugefügt werden, aber es sollen keine bahnbrechenden Änderungen vorgenommen werden.**


{{TOCright}}

Der Lattice2 Arbeitsbereich ist eine FreeCAD [Externer Arbeitsbereich](external_workbenches/de.md), der dem Zweck dient, mit Platzierungen und Platzierungsanordnungen zu arbeiten. Es ist eine Art Zusammenbau Arbeitsbereich, jedoch mit Schwerpunkt auf Anordnungen. Es gibt keine Beschränkungen und Beziehungen, es gibt nur Platzierungsfelder, die erzeugt, kombiniert, transformiert, überlagert und mit Formen bestückt werden können.

Ever wondered how to create a protractor with FreeCAD? That\'s the aim of the workbench (including tick labeling). Also, exploded assemblies can be made with the workbench.

Additionally, the workbench features a few general-purpose tools, such as parametric downgrade, bounding boxes, shape info tool, and tools for working with collections of shapes (compounds).

One of the big design goals of the workbench is being as parametric as possible.

## Referenzen

-   Autor: DeepSOIC
-   Startseite: <https://github.com/DeepSOIC/Lattice2>
-   Quellcode auf github: <https://github.com/DeepSOIC/Lattice2>

## Werkzeuge

Detaillierte Beschreibung auf dem [Lattice2 Github wiki](https://github.com/DeepSOIC/Lattice2/wiki)

### Werkzeugleiste

![](images/Lattice2-menu-orizz.png ) *Lattice2 Werkzeugleiste*

### Befehle

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
-   <img alt="" src=images/Lattice2_AttachablePlacement.svg  style="width:32px;"> [Attachable Placement](Lattice2_AttachablePlacement.md)
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
-   Expose links to subelements

Other

-   Recomputes
    -   <img alt="" src=images/Lattice2_RecomputeMakeFeature.svg  style="width:32px;"> [Make recompute locher object](Lattice2_RecomputeMakeFeature.md):
    -   <img alt="" src=images/Lattice2_RecomputeLock.svg  style="width:32px;"> [Lock recomputes](Lattice2_RecomputeLock.md):
    -   <img alt="" src=images/Lattice2_RecomputeUnlock.svg  style="width:32px;"> [Unlock recomputes](Lattice2_RecomputeUnlock.md):
    -   <img alt="" src=images/Lattice2_RecomputeFeature.svg  style="width:32px;"> [Recompute feature](Lattice2_RecomputeFeature.md):
    -   <img alt="" src=images/Lattice2_RecomputeDocument.svg  style="width:32px;"> [Recompute document](Lattice2_RecomputeDocument.md):
    -   <img alt="" src=images/Lattice2_RecomputeForce.svg  style="width:32px;"> [Force recompute](Lattice2_RecomputeForce.md):
    -   <img alt="" src=images/Lattice2_RecomputeTouch.svg  style="width:32px;"> [Touch selected feature](Lattice2_RecomputeTouch.md):
-   <img alt="" src=images/Lattice2_Lattice2.svg  style="width:32px;"> Lattice2 Workbench icon

## Installation

**Prerequisites** Lattice2 WB requires FreeCAD \>= v0.16.5155.

### Automatische Installation 

As of v0.17 one can use the <img alt="" src=images/AddonManager.svg  style="width:24px;"> [Addon Manager](Addon_Manager.md) to install the <img alt="" src=images/Lattice2_Lattice2.svg  style="width:24px;"> Lattice2 Workbench. Use {MenuCommand\|Tools → Addon Manager}}

### Manuelles Einrichten 

-   Scroll to the top of the page, and click \'download zip\' button
-   Unpack the contents into a \"Lattice2\" folder created in \\Path\\to\\FreeCAD\\Mod, and restart FreeCAD.
-   Note that InitGui.py (and the rest of .py files) should end up directly under Mod\\Lattice2 (not under nested directory like Mod\\Lattice2\\Lattice2).

After you install the workbench, it should appear at the bottom of list of workbench selector in FreeCAD.

## Tutorien

-   Tutorials: [Gallery](https://github.com/DeepSOIC/Lattice2/wiki/Gallery)
-   [Basic Tutorial](https://github.com/DeepSOIC/Lattice2/wiki/Basic-Tutorial)
-   [Lattice2 in PartDesign](https://github.com/DeepSOIC/Lattice2/wiki/PartDesign-Pattern-Tutorial)
-   [Making a Cogset](https://github.com/DeepSOIC/Lattice2/wiki/Cogset-Tutorial)
-   [Feature Patterns in Lattice2 Workbench](https://www.youtube.com/watch?v=BXmeEGnhszo) by \@sliptonic

## Verknüpfungen zum Lattice2 Arbeitsbereich 

-   Lattice2 Wiki: <https://github.com/DeepSOIC/Lattice2/wiki>
-   FreeCAD Wiki: <https://www.freecadweb.org/wiki/Lattice2_Workbench>
-   FreeCAD Forum: [Lattice workbench - v2.0 is becoming stable](http://forum.freecadweb.org/viewtopic.php?t=12464)
-   Gallery: <https://github.com/DeepSOIC/Lattice2/wiki/Gallery>
-   Report bugs: Please report bugs at <https://github.com/DeepSOIC/Lattice2/issues>

## Andere nützliche Verknüpfungen 

-   [Lattice aka Lattice1 Workbench (obsolete)](https://github.com/DeepSOIC/Lattice)
-   [External Workbenches](External_Workbenches.md): List of FreeCAD workbenches.
-   [Macros recipes](Macros_recipes.md)
-   [FreeCAD Community Portal](FreeCAD_Community_Portal.md)




_ _

---
[documentation index](../README.md) > [Addons](Category_Addons.md) > Lattice2 Workbench/de
