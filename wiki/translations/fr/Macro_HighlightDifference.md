# Macro HighlightDifference/fr

 {{Macro/fr
|Name=HighlightDifference
|Description=Crée un objet(s) différence entre deux objets qui se chevauchent
|Author=Gaël Ecorchard
|Version=1.0
|Date=2015-09-24
}}

## Description

Crée des objets calculés sur la différence du chevauchement des objets originaux. les nouveaux objets sont coloré en rouge et vert. les objets originaux ne sont pas modifiés mais rendu transparent à 80%. le volume de chaque nouveau objet est affiché dans la Vue rapport.


{{Codeextralink|https://raw.githubusercontent.com/FreeCAD/FreeCAD-macros/master/Utility/HighlightDifference.FCMacro}}

<img alt="Le résultat de la différence entre les deux objets est créé" src=images/Macro_HighlightDifference_02.png  style="width:400px;"> 
*Result difference two objects created*

## Exemple


<center>

Image:Macro HighlightDifference 00.png\|Objets originaux Image:Macro HighlightDifference 02.png\|Le résultat est coloré en rouge et vert (ici les objets sont décalés) Image:Macro HighlightDifference 01.png\|Les objets originaux sont transparents à 80% et non modifiés


</center>




## Script

**Macro\_HighlightDifference.FCMacro**

Le code est visible sur Github: [Utility/HighlightDifference.FCMacro](https://github.com/FreeCAD/FreeCAD-macros/blob/master/Utility/HighlightDifference.FCMacro).

## Liens

-   Voir la macro complémentaire [Macro\_HighlightCommon](Macro_HighlightCommon/fr.md)
-   La discussion sur le forum [\"collision detection\", overlapping](http://forum.freecadweb.org/viewtopic.php?f=22&t=12426)
