---
- GuiCommand:/fr
   Name:Path ExportTemplate
   Name/fr:Path Exporter comme modèle
   MenuLocation:Path → Export Template
   Workbenches:[Path](Path_Workbench/fr.md)
   SeeAlso:[Path Feuille de configuration](Path_SetupSheet/fr.md)
---

# Path ExportTemplate/fr

## Description

L\'exportation des modèles de travail fournit un mécanisme pratique pour enregistrer les définitions de travail couramment utilisées à partir d\'un travail existant. Cela facilite la configuration des futurs travaux, qui sont en grande partie similaires, en permettant l\'importation de modèles de travail pendant le processus de création de travail.

L\'onglet **Édition → Préférences... → Path → Job Preferences, Defaults → Template** définit le modèle par défaut.

## Usage

1.  Sélectionnez l\'option **Path → <img src="images/Path_ExportTemplate.svg" width=16px> Export Template** dans le menu.
2.  Sélectionnez les éléments à inclure dans la boîte de dialogue de configuration **Export Template**.
3.  Le modèle doit être enregistré dans le répertoire Macro ou le répertoire Path, tel que configuré dans les [Path Préférences](Path_Preferences/fr.md).
4.  Le nom du modèle doit suivre le modèle {{FileName|job_<template name>.json}}. Dans la liste déroulante de sélection, le préfixe {{FileName|job_}} et l\'extension sont omis.
5.  Appuyez sur le bouton **OK** et enregistrez le modèle.

## Options

## Post-traitement 

-   Sélection du post-processeur
-   Paramètres du post-processeur
-   Nom du fichier de sortie

## Brut

-   Extent: Dimensions du brut
-   Placement: Position du brut

## Feuille de calcul conditions de démarrage 

-   Profondeur d\'usinage
-   Profondeurs de passe
-   Vitesses de déplacement de l\'outil

## Contrôleurs d\'outils 

-   Contrôleurs d\'outils sélectionnés.





{{Path_Tools_navi

}}

---
[documentation index](../README.md) > [Path](Path_Workbench.md) > Path ExportTemplate/fr
