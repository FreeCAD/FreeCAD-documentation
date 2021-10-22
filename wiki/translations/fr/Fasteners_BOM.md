---
- GuiCommand:
   Name:Fasteners BOM
   Name/fr:Fasteners Nomenclature
   MenuLocation:Fasteners → BOM
   Workbenches:[Fasteners](Fasteners_Workbench/fr.md)
---

# Fasteners BOM/fr

## Description

<img alt="" src=images/Fasteners_BOM.svg  style="width:24px;"> [Fasteners Nomenclature](Fasteners_BOM/fr.md) génère une nomenclature. Cet outil fait partie des [ateliers externes](External_workbenches/fr.md) appelé [Fasteners](Fasteners_Workbench/fr.md).

## Utilisation

1.  Basculez vers <img alt="" src=images/Fasteners_workbench_icon.svg  style="width:24px;"> _ si ce n\'est pas déjà fait)
2.  Appelez l\'outil de nomenclature des fixations de plusieurs manières:
    -   Appuyez sur le bouton <img alt="" src=images/Fasteners_BOM.svg  style="width:24px;">
    -   Utilisez l\'entrée **Fasteners → BOM** dans le menu Fasteners
3.  Lorsqu\'il est appelé, l\'outil de nomenclature des fixations ajoute une feuille de calcul au document FreeCAD.
    -   La feuille de calcul représente la nomenclature des fixations utilisées dans l\'arborescence des fonctions du modèle.

<img alt="" src=images/BOM_example-1.FCStd.png  style="width:1000px;">

## Remarques

1.  Utilisez l\'<img alt="" src=images/Workbench_Spreadsheet.svg  style="width:24px;"> [atelier Spreadsheet](Spreadsheet_Workbench/fr.md) pour exporter la nomenclature au format csv qui peut également être lu et écrit par la plupart des autres applications de feuille de calcul telles que Microsoft Excel ou LibreOffice Calc.

## Limitations

## Propriétés


{{Properties_Title|Base}}

-    **Label**: nom donné par l\'utilisateur à la feuille de tableur dans la [vue en arborescence](Tree_view/fr.md).

-    **View**: mode d\'affichage

-    **View**: en haut lorsque sélectionné, désactivé, activé, objet, élément, par défaut: désactivé.

-    **View**: style, forme ou cadre de sélection, par défaut: forme.

-    **View**: affichage dans l\'arborescence, booléen, par défaut: vrai.

-    **View**: visibilité, booléen, par défaut: vrai.

## Script





{{Fasteners Tools navi

}} 

_

---
[documentation index](../README.md) > [External Command Reference](Category_External Command Reference.md) > Fasteners BOM/fr
