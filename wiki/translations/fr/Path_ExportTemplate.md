---
- GuiCommand:/fr
   Name:Path ExportTemplate
   Name/fr:Path Exporter un modèle
   MenuLocation:Path → Exporter comme modèle
   Workbenches:[Path](Path_Workbench/fr.md)
   SeeAlso:[Path Feuille de configuration](Path_SetupSheet/fr.md)
---

# Path ExportTemplate/fr

## Description

L\'outil <img alt="" src=images/Path_ExportTemplate.svg  style="width:24px;"> [Exporter un modèle](Path_ExportTemplate/fr.md) constitue un mécanisme pratique permettant de sauvegarder les définitions de tâches couramment utilisées à partir d\'une tâche existante. L\'importation de modèles de tâches au cours de la procédure de création d\'une tâche facilite la mise en place de futures tâches très similaires.


**Édition → Préférences... → Path → Préférences des tâches  → Valeurs par défaut → Modèle**

définit le modèle par défaut.



## Utilisation

1.  Sélectionnez l\'option **Path → <img src="images/Path_ExportTemplate.svg" width=16px> Exporter comme modèle** du menu.
2.  Sélectionnez les éléments à inclure dans la boîte de dialogue de configuration **Exporter comme modèle**.
3.  Le modèle doit être enregistré dans le répertoire Macro ou le répertoire Path, tel que configuré dans les [Path Préférences](Path_Preferences/fr.md).
4.  Le nom du modèle doit suivre le modèle **job_<template name>.json**. Lorsqu\'il est affiché dans la liste déroulante de la sélection, le préfixe **job_** et l\'extension sont omis.
5.  Appuyez sur le bouton **OK** et enregistrez le modèle.

## Options



## Post-traitement 

-   Sélection du post-processeur
-   Paramètres du post-processeur
-   Nom du fichier de sortie



## Brut

-   Marge : dimensions du brut
-   Placement : position du brut



## Feuille de réglage 

-   Profondeur d\'usinage
-   Profondeurs de passe
-   Vitesses de déplacement de l\'outil



## Contrôleurs d\'outils 

-   Contrôleurs d\'outils sélectionnés.





{{Path_Tools_navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [Path](Path_Workbench.md) > Path ExportTemplate/fr
