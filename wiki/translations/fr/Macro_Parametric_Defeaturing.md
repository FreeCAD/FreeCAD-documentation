# Macro Parametric Defeaturing/fr
{{Macro/fr
|Name=Macro Parametric Defeaturing
|Icon=parametric_defeaturing.svg
|Description=Cette macro est similaire à l'outil [defeaturing](Part_Defeaturing/fr.md) de [Part Workbench](Part_Workbench/fr.md), mais elle est paramétrique et fonctionne également dans [PartDesign](PartDesign_Workbench/fr.md). Pour l'utiliser    * sélectionnez les faces des caractéristiques que vous souhaitez supprimer du modèle et exécutez la macro. Les faces sont utilisées dans le defeaturing, pas les arêtes ou les sommets. Les faces utilisées peuvent être modifiées ultérieurement et l'objet se reconstruira automatiquement.<br/>

Le paramétrage est généralement une bonne chose dans la modélisation 3D, mais comme le defeaturing repose sur les noms des faces    * Face1, Face2, etc., il est vulnérable aux problèmes de dénomination topologique et peut se briser si des changements sont apportés à l'objet source original défait, lorsque ces changements entraînent une renumérotation des noms de face. La défausse est également un processus délicat, donc le succès n'est pas toujours garanti.<br/>

La documentation complète se trouve sur github   * [https   *//github.com/mwganson/parametric_defeaturing Parametric Defeaturing].<br/>

|Author=TheMarkster
|Version=0.2021.10.10.rev2
|Date=2021-10-10.rev2
|FCVersion=python version 3
|Download=[https   *//wiki.freecadweb.org/File   *parametric_defeaturing.svg ToolBar Icon]
|Links=[https   *//github.com/mwganson/parametric_defeaturing Documentation complète sur Github]
}}

## Description

Cette macro est similaire à l\'outil [defeaturing](Part_Defeaturing/fr.md) de [Part Workbench](Part_Workbench/fr.md), mais elle est paramétrique et fonctionne également dans [PartDesign](PartDesign_Workbench/fr.md). Pour l\'utiliser    * sélectionnez les faces des caractéristiques que vous souhaitez supprimer du modèle et exécutez la macro. Les faces sont utilisées dans le defeaturing, pas les arêtes ou les sommets. Les faces utilisées peuvent être modifiées ultérieurement et l\'objet se reconstruira automatiquement.

Le paramétrage est généralement une bonne chose dans la modélisation 3D, mais comme le defeaturing repose sur les noms des faces    * Face1, Face2, etc., il est vulnérable aux problèmes de dénomination topologique et peut se briser si des changements sont apportés à l\'objet source original défait, lorsque ces changements entraînent une renumérotation des noms de face. La défausse est également un processus délicat, donc le succès n\'est pas toujours garanti.

La documentation complète se trouve sur github   * [Parametric Defeaturing](https   *//github.com/mwganson/parametric_defeaturing).

<img alt="" src=images/parametric_defeaturing_scr2.png  style="width   *600px;"> 
*Capture d'écran de la macro paramétrique de defeaturing‎*

## Légende


{{Codeextralink|https   *//gist.github.com/mwganson/0d55a5c51b1d6ff488b7a2f62bf50656/raw/140e9118deb955981a1ea499778cbf2521818e40/parametric_defeaturing.FCMacro|parametric_defeaturing.FCMacro}}

Icône de la barre d\'outils ![](images/parametric_defeaturing.svg )

## Script

**Macro parametric_defeaturing.FCMacro**


{{CodeDownload|https   *//gist.github.com/mwganson/0d55a5c51b1d6ff488b7a2f62bf50656|parametric_defeaturing.FCMacro}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Macro Parametric Defeaturing/fr
