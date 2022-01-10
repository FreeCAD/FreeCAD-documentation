# Macro Bevel/fr
{{Macro/fr
|Name=Macro Bevel
|Icon=Bevel.svg
|Description=Biseautage des sommets sélectionnés des objets solides, paramétrique, compatible avec Part Design
|Author=TheMarkster
|Version=0.2021.12.23
|Date=2021-12-23
|FCVersion=Versions en Python 3
|Download=[https://wiki.freecadweb.org/File:bevel.svg Icône de la barre d'outils]
|Links=[https://github.com/mwganson/Bevel Documentation complète sur Github]
}}

## Description

Cette macro est utilisée pour biseauter les sommets sélectionnés des objets solides, elle fonctionne également avec les faces. Si l\'objet sélectionné est un Part Design élément, l\'objet paramétrique Bevel se placera dans le Part Design corps et d\'autres modélisations pourront être effectuées sur le même corps. Si l\'objet sélectionné n\'est pas un Part Design élément, un nouvel objet est ajouté à l\'arbre en tant qu\'objet Python standard et paramétrique.

Utilisation : sélectionnez les sommets dans la vue 3D que vous souhaitez biseauter et exécutez la macro. Vous pouvez également sélectionner l\'objet entier dans l\'arbre, auquel cas tous les sommets seront biseautés. Cet outil est très similaire à d\'autres outils d\'habillage dans FreeCAD, tels que les congés et les chanfreins et se comporte de la même manière que ces objets, sauf qu\'il est compatible avec les environnements de travail Part et Part Design.

La documentation complète se trouve sur github : [Bevel](https://github.com/mwganson/Bevel).

<img alt="" src=images/bevel_scr.png  style="width:600px;"> 
*Copie d'écran de Macro Bevel‎*

## Légende


{{Codeextralink|https://gist.github.com/mwganson/25ee4dc925c8bcf1182bd9979025ed2d/raw/1741a8f93a0af40dcd4f74dca33b106446f5e4ee/Bevel.FCMacro|Bevel.FCMacro}}

Icône de la barre d\'outils ![](images/Bevel.svg )

## Script

**Macro Bevel.FCMacro**


{{CodeDownload|https://gist.github.com/mwganson/25ee4dc925c8bcf1182bd9979025ed2d|Bevel.FCMacro}}

---
[documentation index](../README.md) > Macro Bevel/fr
