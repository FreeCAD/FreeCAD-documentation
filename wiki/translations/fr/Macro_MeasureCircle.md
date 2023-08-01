# Macro MeasureCircle/fr
{{Macro/fr
|Name=Macro MeasureCircle
|Icon=Macro_MeasureCircle.png
|Description=Calcule le rayon d'un cercle sur 3 points ou une ligne circulaire
|Author=galou_breizh
|Version=1.0
|Date=2016-04-08
|FCVersion=All
|Download=[https://www.freecadweb.org/wiki/images/b/bd/Macro_MeasureCircle.png ToolBar Icon]
}}

## Description

Cette macro calcule le rayon et centre du cercle en donnant 3 points ou une ligne circulaire. Une ligne est créée à partir du centre et du premier point pour l\'utiliser plus tard.


{{Codeextralink|https://raw.githubusercontent.com/FreeCAD/FreeCAD-macros/master/Information/MeasureCircle.FCMacro}}

## Utilisation

Copiez la macro dans votre répertoire de macros et lancez là, voir ici pour plus d\'informations sur [Comment installer une macro](How_to_install_macros.md)

Sélectionnez les vecteurs et le résultat s\'affiche dans la vue rapport. Les arêtes peuvent également être choisis et comptent comme deux sommets. Un bord circulaire peut également être sélectionné. Si deux arêtes sont sélectionnées le dernier vertex de la deuxième arête n\'est pas utilisés dans le calcul.

Sélectionnez les éléments et lancez la macro ou lancez la macro et sélectionnez les objets après le lancement. S\'il n\'y a pas d\'éléments sélectionné avant le lancement de la macro, vous devez sélectionner les éléments

## Script

La dernière version est téléchargeable sur [MeasureCircle.FCMacro](https://raw.githubusercontent.com/FreeCAD/FreeCAD-macros/master/Information/MeasureCircle.FCMacro) ou avec le <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Gestionnaire des extensions](Std_AddonMgr/fr.md).

ToolBar Icon ![](images/Macro_MeasureCircle.png )

**Macro_MeasureCircle.FCMacro**



---
![](images/Button_right.svg) [documentation index](../README.md) > Macro MeasureCircle/fr
