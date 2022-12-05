# Macro ObjectInfo/fr
{{Macro/fr
|Name=Macro ObjectInfo
|Description=Cet atelier vous permet de connaître la surface, le volume, le centre de masse et le moment d’inertie de l’objet sélectionné.
|Author=keithsloan52
|Version=1.0
|Date=2012-11-09
|FCVersion=Until 0.17 '''and PyQt4'''
|Download=Ce n'est pas une macro mais un atelier, décompressez le fichier .zip et collez le répertoire complet dans le répertoire utilisateur Mod [https://github.com/KeithSloan/FreeCAD_Info/archive/master.zip Info]
|SeeAlso=[Arch Survey|<img src=images/Arch_Survey.svg style="width:24px"> [Arch Survey](Arch_Survey/fr.md)
}}

## Description

Cet atelier vous permet de connaître les informations de volume, surface, centre de gravité et le moment d\'inertie de l\'objet sélectionné.

<img alt="" src=images/ObjectInfoIt.png  style="width:480px;">

## Installation

Si vous êtes sous Linux, vous devez créer un dossier nommé \"Mod\" dans le dossier caché **.FreeCAD** qui se trouve dans votre dossier personnel. Ensuite, créez un dossier nommé \"Info\" dans le dossier \"Mod\", et extraire le contenu de l\'archive dans le dossier \"Info\". Sous Windows faites la même procédure dans le répertoire C:\\Program Files\\FreeCAD\\Mod.

## Utilisation

Ensuite, lancez FreeCAD, ouvrez votre fichier STEP et passez à l\'atelier \"Info\" avec le sélecteur d\'atelier ou en allant à Affichage → Workbench. Maintenant, sélectionnez votre solide et cliquez sur l\'icône \"Info\". La barre des tâches de gauche indiquera des informations sur le modèle: volume, surface, centre de masse et moment d\'inertie.

## Code


{{MacroCode|code=
import webbrowser 

##########
# WorkBenche
# Code used to download the zip file from FreeCAD
##########

FreeCAD.Console.PrintMessage("\n" + "You must download the Info.zip file in the author github KeithSloan/FreeCAD_Infosite" + "\n")
FreeCAD.Console.PrintMessage("http://keithsloan.dynu.com/Keith&Jenny/" + "\n")
webbrowser.open("https://github.com/KeithSloan/FreeCAD_Info/archive/master.zip")

}}

## Liens

Un utilisateur FreeCAD créé un module convivial \"Info\" que vous pouvez obtenir ici: <http://www.sloan-home.co.uk/FreeCAD/Info/Info.html>

Sur le Forum [Info Workbench - Help with icons please.](http://forum.freecadweb.org/viewtopic.php?f=10&t=3185)



---
![](images/Right_arrow.png) [documentation index](../README.md) > Macro ObjectInfo/fr
