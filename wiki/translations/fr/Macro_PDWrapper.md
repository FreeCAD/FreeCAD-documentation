# Macro PDWrapper/fr
{{Macro/fr
|Name=Macro Pdwrapper
|Icon=Workbench_PartDesign.svg
|Description=Encapsuler des solides non-PartDesign pour travailler dans PartDesign
|Author=TheMarkster
|Version=0.2022.02.01
|Date=2022-02-01
|FCVersion=Versions en Python 3
|Download=[https://wiki.freecadweb.org/File:Workbench_PartDesign.svg Icône de la barre d'outils]
|Links=[https://github.com/mwganson/pdwrapper Documentation complète sur Github]
}}

## Description

PDWrapper encapsule les solides créés dans d\'autres ateliers à l\'intérieur d\'un objet PartDesign::FeaturePython afin qu\'ils se comportent comme s\'il s\'agissait de caractéristiques natives de PartDesign. La capture d\'écran ci-dessous montre un filet de Part Workbench d\'une boîte additive PartDesign encapsulée dans un objet PDWrapper de type Common Additive. Mais PDWrapper peut faire plus que simplement encapsuler des solides non-PartDesign pour les utiliser dans un corps PartDesign. Il peut également encapsuler des caractéristiques de PartDesign et en modifier la nature. Par exemple, vous pouvez encapsuler un trou PartDesign dans un type additif PDWrapper et transformer le trou en tige filetée (en supposant que le trou soit fileté). Avec PDWrapper, vous pouvez créer des types de primitives qui ne sont pas disponibles, comme les types Common (Intersection) et les types XOR. Il permet également d\'inclure/exclure dynamiquement certaines caractéristiques solides de la forme de l\'extrémité du corps.

Les exemples et la documentation complète se trouvent sur github : [PDWrapper](https://github.com/mwganson/pdwrapper).

<img alt="" src=images/Pdwrapper_scr.png  style="width:600px;"> 
*Copie d'écran de la Macro PDWrapper*

## Légende


{{Codeextralink|https://gist.github.com/mwganson/4106e84eeaaf4d6e056cd286cbc39170/raw/43a51ea22174953fb4e9083337fa48a2c92eabbb/Pdwrapper.FCMacro|Pdwrapper.FCMacro}}

Icône de la barre d\'outils ![](images/Workbench_PartDesign.svg )

## Script

**Macro Pdwrapper.FCMacro**


{{CodeDownload|https://gist.github.com/mwganson/4106e84eeaaf4d6e056cd286cbc39170|Pdwrapper.FCMacro}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Macro PDWrapper/fr
