---
- GuiCommand:
   Name: OpenSCAD ExplodeGroup
   Name/fr: OpenSCAD Dégrouper
   MenuLocation: OpenSCAD -> Dégrouper
‏‎   Workbenches: OpenSCAD_Workbench
---

# OpenSCAD ExplodeGroup/fr

## Description

Cette outil fait décompose une fusion ou un composé et le convertit en objets uniques en appliquant des couleurs aléatoires à ces objets.

## Utilisation

1.  Sélectionner le fusion/composé à exploser
2.  Cliquer sur <img alt="" src=images/OpenSCAD_ExplodeGroup.svg  style="width:32px;"> ou choisissez **OpenSCAD** → **<img src="images/OpenSCAD_ExplodeGroup.svg" width=32px> Dégrouper** dans le menu principal.

## Limitations

La fonction ne fonctionne que sur les fusions/composés composés de :

-   Parties primitives de l\'atelier Part
-   Pièces extrudées de l\'atelier Part
-   Pièces issues de révolution de l\'atelier Part

La fonctionnalité ne fonctionnera **PAS** sur :

-   Des protrusions/révolutions de l\'atelier de Part Design
-   Des réseaux de l\'atelier Draft

## Remarques

Pour désagréger les réseaux de l\'atelier de Draft, utilisez l\'outil [Draft Désagréger](Draft_Downgrade/fr.md).





{{OpenSCAD_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [OpenSCAD](OpenSCAD_Workbench.md) > OpenSCAD ExplodeGroup/fr
