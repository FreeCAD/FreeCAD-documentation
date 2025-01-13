# Macro Editor Assistant/fr
{{Macro/fr
|Name=Macro Editor Assistant
|Icon=Editor_Assistant_Icon.svg
|Description=Étend les fonctions de l'éditeur Python intégré à FreeCAD
|Author=TheMarkster
|Version=2.01
|Date=2024-10-10
|FCVersion=0.21 ou plus
|Download=[https://wiki.freecadweb.org/File:Editor_Assistant_Icon.svg Icône de la barre d'outils]
|SeeAlso=
|Links=[https://github.com/mwganson/Editor_Assistant Documentation sur Github]
}}

## Description

Editor Assistant étend les capacités de l\'éditeur Python intégré à FreeCAD. L\'éditeur est assez bon dans ce qu\'il fait, mais il est quelque peu limité dans ses fonctionnalités. Cette macro tente de compléter l\'éditeur en ajoutant certaines de ces fonctionnalités manquantes, y compris : recherche et remplacement, signets, références d\'aide, instantanés, diffs, mise en évidence de la recherche, insertion d\'extraits de texte via un mécanisme de modèles, et plus encore.



## Utilisation

Installez et exécutez la macro. Une nouvelle boîte de dialogue apparaîtra comme un troisième onglet dans la vue Combo. En tant que troisième onglet, cette boîte de dialogue n\'interférera pas avec les autres boîtes de dialogue de tâches qui doivent utiliser l\'onglet Tâche pour leurs boîtes de dialogue. (Si vous préférez, vous pouvez lancer la macro comme une fenêtre flottante ancrable en maintenant la touche Alt enfoncée pendant l\'exécution de la macro).

La macro comprendra un widget de liste montrant tous les éditeurs ouverts en cours. L\'éditeur sélectionné sera l\'éditeur utilisé auquel les fonctions de la macro seront appliquées. Lorsque vous sélectionnez un éditeur dans le widget de liste, cet éditeur reçoit le focus. (Mais la sélection d\'un nouvel éditeur dans le widget d\'onglets de la zone MDI n\'en fait pas l\'éditeur courant). De temps en temps, lorsque de nouvelles fenêtres sont ouvertes et que d\'autres sont fermées, vous devrez rafraîchir le widget de liste en appuyant sur le bouton Refresh.

La documentation complète se trouve sur GitHub : [Editor Assistant](https://github.com/mwganson/Editor_Assistant).

<img alt="" src=images/Editor_Assistant_scr1.png  style="width:400px;"> 
*Capture d'écran de la Macro Editor Assistant*



## Légende


{{Codeextralink|https://gist.github.com/mwganson/20475dad57d9b659190f082d20e3bde6/raw/f3a9d8fa95e8c3f264f376b06f5566c8b03eff5a/Editor_Assistant.FCMacro|Editor_Assistant.FCMacro}}

Icône de la barre d\'outils ![](images/Editor_Assistant_Icon.svg )

## Script

**Macro Editor_Assitant.FCMacro**


{{CodeDownload|https://gist.github.com/mwganson/20475dad57d9b659190f082d20e3bde6|Editor_Assitant.FCMacro}}



---
⏵ [documentation index](../README.md) > Macro Editor Assistant/fr
