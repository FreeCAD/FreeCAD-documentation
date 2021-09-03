---
- GuiCommand:
   Name:Fasteners BOM
   Name/fr:Fasteners BOM
   MenuLocation:Fasteners → BOM
   Workbenches:[Fasteners](Fasteners_Workbench/fr.md)
   Shortcut:Aucun
   SeeAlso:
---

## Description

<img alt="" src=images/Fasteners_BOM.svg  style="width:24px;"> [Fasteners BOM](Fasteners_BOM/fr.md) génère une nomenclature. Cet outil fait partie de [Fasteners](Fasteners_Workbench/fr.md), un [atelier externe](external_workbenches/fr.md).

## Utilisation

1.  Basculez vers <img alt="" src=images/Fasteners_workbench_icon.svg  style="width:24px;"> [Fasteners](Fasteners_Workbench.md) (installer à partir de <img alt="" src=images/AddonManager.svg  style="width:24px;"> [Gestionnaire d\'Addon](Addon_Manager/fr.md) si ce n\'est pas déjà fait)
2.  Appelez l\'outil de nomenclature des fixations de plusieurs manières:
    -   Appuyez sur le bouton <img alt="" src=images/Fasteners_BOM.svg  style="width:24px;">
    -   Utilisez l\'entrée {{MenuCommand|Fasteners → BOM}} dans le menu Fasteners
3.  Lorsqu\'il est appelé, l\'outil de nomenclature des fixations ajoute une feuille de calcul au document FreeCAD.
    -   La feuille de calcul représente la nomenclature des fixations utilisées dans l\'arborescence des fonctions du modèle.

<img alt="" src=images/BOM_example-1.FCStd.png  style="width:1000px;">

## Remarques

1.  Utilisez l\'<img alt="" src=images/Workbench_Spreadsheet.svg  style="width:24px;"> [atelier Spreadsheet](Spreadsheet_Workbench/fr.md) pour exporter la nomenclature au format csv qui peut également être lu et écrit par la plupart des autres applications de feuille de calcul telles que Microsoft Excel ou LibreOffice Calc .

## Limitations

## Propriétés


{{Properties_Title|Base}}

-    {{PropertyData/fr|Label}}: Nom donné par l\'utilisateur à la feuille de tableur dans la [vue en arborescence](tree_view/fr.md).

-    {{PropertyView/fr|View}}: Mode d\'affichage

-    {{PropertyView/fr|View}}: En haut lorsque sélectionné, désactivé, activé, objet, élément, par défaut: désactivé

-    {{PropertyView/fr|View}}: Style, forme ou cadre de sélection, par défaut: forme

-    {{PropertyView/fr|View}}: Affichage dans l\'arborescence, booléen, par défaut: vrai

-    {{PropertyView/fr|View}}: Visibilité, booléen, par défaut: vrai

## Script





{{Fasteners Tools navi

}} 

[Category:External Command Reference{{\#translation:}}](Category:External_Command_Reference.md)
