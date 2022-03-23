---
- GuiCommand:/fr
   Name:OpenSCAD ExplodeGroup
   Name/fr:OpenSCAD Dégrouper
   MenuLocation:OpenSCAD → Dégrouper
‏‎   Workbenches:[OpenSCAD](OpenSCAD_Workbench.md)
---

# OpenSCAD ExplodeGroup/fr

## Description

Cette outil fait décompose une fusion ou un composé et le convertit en objets uniques en appliquant des couleurs aléatoires à ces objets.

## Utilisation

1.  Sélectionner fusion/composé à exploser
2.  Cliquez sur <img alt="" src=images/OpenSCAD_ExplodeGroup.svg  style="width:32px;"> ou choisissez **OpenSCAD** → **<img src="images/OpenSCAD_ExplodeGroup.svg" width=32px> Dégrouper** dans le menu principal.

## Limitations

La fonction ne fonctionne que sur les fusions/composés composés de

-   parties primitives de l\'atelier Part
-   pièces extrudées de l\'atelier Part
-   pièces révolution de l\'atelier Part

La fonctionnalité ne fonctionnera **PAS** sur

-   des protrusions/révolutions de l\'atelier de PartDesign
-   réseaux de l\'atelier Draft

## Remarques

Pour les réseaux de l\'atelier de Draft, utilisez l\'outil [Draft Désagréger](Draft_Downgrade/fr.md) de l\'atelier Draft.





{{OpenSCAD_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [OpenSCAD](OpenSCAD_Workbench.md) > OpenSCAD ExplodeGroup/fr
