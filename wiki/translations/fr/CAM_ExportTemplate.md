---
 GuiCommand:
   Name: CAM ExportTemplate
   Name/fr: CAM Exporter un modèle
   MenuLocation: CAM , Exporter comme modèle
   Workbenches: CAM_Workbench/fr
   SeeAlso: CAM_SetupSheet/fr
---

# CAM ExportTemplate/fr

## Description

L\'outil <img alt="" src=images/CAM_ExportTemplate.svg  style="width:24px;"> [Exporter un modèle](CAM_ExportTemplate/fr.md) fournit un mécanisme pratique pour sauvegarder les définitions de tâches couramment utilisées à partir d\'une tâche existante. Cela facilite la mise en place de futurs tâches, qui sont en grande partie similaires, en permettant l\'importation de modèles de tâches pendant le processus de création de tâches.


**Édition → Préférences... → CAM → Préférences des tâches  → Valeurs par défaut → Modèle**

définit le modèle par défaut.



## Utilisation

1.  Sélectionnez l\'option **CAM → <img src="images/CAM_ExportTemplate.svg" width=16px> Exporter comme modèle** du menu.
2.  Sélectionnez les éléments à inclure dans la fenêtre de dialogue de configuration **Exporter comme modèle**.
3.  Le modèle doit être enregistré dans le répertoire Macro ou le répertoire CAM, tel que configuré dans les [CAM Préférences](CAM_Preferences/fr.md).
4.  Le nom du modèle doit suivre le modèle **job_<template name>.json**. Lorsqu\'il est affiché dans la liste déroulante de la sélection, le préfixe **job_** et l\'extension sont omis.
5.  Appuyez sur le bouton **OK** et enregistrez le modèle.

## Options



## Post-traitement 

-   Sélection du post-processeur
-   Paramètres du post-processeur
-   Nom du fichier de sortie



## Brut

-   Marge : dimensions du brut
-   Position : position du brut



## Feuille de réglage 

-   Profondeur d\'usinage
-   Profondeurs de passe
-   Vitesses de déplacement de l\'outil



## Contrôleurs d\'outils 

-   Contrôleurs d\'outils sélectionnés.





{{CAM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [CAM](CAM_Workbench.md) > CAM ExportTemplate/fr
