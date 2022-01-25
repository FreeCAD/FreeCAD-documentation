# Macro WireFilter/fr
{{Macro/fr
|Name=Macro WireFilter
|Icon=Wirefilter.svg
|Description=Filtrez les lignes à partir d'esquisses, décalages 2D, échelles, réorganisez l'ordre des lignes.
|Author=TheMarkster
|Version=0.2021.12.13
|Date=2021-12-13
|FCVersion=Les versions en Python 3
|Download=[https://wiki.freecadweb.org/File:Wirefilter.svg Icône de la barre d'outils]
|Links=[https://github.com/mwganson/wirefilter Documentation complète sur Github]
}}

## Description

WireFilter est une macro qui peut être utilisée pour filtrer certains fils d\'une esquisse. Elle peut également être utilisée sur tout objet comportant des fils, comme un solide. Avec WireFilter, vous pouvez faire un décalage 2D d\'un fil, vous pouvez mettre le fil à l\'échelle, vous pouvez utiliser l\'un des 4 facemakers différents (Part::FaceMakerBullseye, Part::FaceMakerCheese, Part::FaceMakerSimple, ou Part::FaceMakerExtrusion) si vous voulez faire une face. Vous pouvez également réinitialiser l\'ordre des fils, ce qui peut être utile lorsqu\'un lissage s\'entrecroise parce que l\'ordre des fils est différent avec les 2 esquisses utilisées.

Les exemples et la documentation complète se trouvent sur github : [WireFilter](https://github.com/mwganson/wirefilter).

Dans la capture d\'écran ci-dessous, WireFilter est utilisé pour créer des faces à partir d\'une esquisse en œil de bœuf (avec des trous imbriqués dans d\'autres trous) à utiliser avec un PartDesign::Pad. Normalement, Pad ne peut pas gérer de telles esquisses, mais si nous créons la face pour elle (à l\'aide de FaceMakerBullseye) et que nous sélectionnons les faces pour le Pad, il sera en mesure d\'en faire une protrusion.

<img alt="" src=images/Wirefilter_scr1.png  style="width:600px;"> 
*Copie d'écran de la Macro WireFilter*

## Problèmes connus 

Parfois, la protrusion ne peut pas trouver la normale correcte et le WireFilter est généré dans la mauvaise direction. Cela peut être corrigé en activant la propriété Fix Normal de l\'objet WireFilter, qui définit la direction personnalisée de Pad sur la normale correcte. Cela fonctionne également pour un extrusion lorsqu\'il ne parvient pas à trouver la normale correcte.

## Légende


{{Codeextralink|https://gist.github.com/mwganson/0aedd5e9057650d0a1f0483f3cc2fa6c/raw/bfff4a29d8484f02bda2a49fea196dad21752280/wirefilter.FCMacro|wirefilter.FCMacro}}

Icône de la barre d\'outils ![](images/Wirefilter.svg )

## Script

**Macro Wirefilter.FCMacro**


{{CodeDownload|https://gist.github.com/mwganson/0aedd5e9057650d0a1f0483f3cc2fa6c|Wirefilter.FCMacro}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Macro WireFilter/fr
