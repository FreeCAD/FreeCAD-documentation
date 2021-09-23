# Macro CenterOfMass/fr
{{Macro/fr
|Name=Macro CenterOfMass
|Description=Donne la masse totale et la position du centre de masse de l'ensemble des objets sélectionnés. 
|Author=schupin
|Version=0.4.2
|Date=2019-06-09
|FCVersion=0.18
|Download=Téléchargez l'ensemble des icônes [https://forum.freecadweb.org/download/file.php?id=84270 Macro_CenterOfMass_Icon] et placez le dossier dans le même répertoire de vos macros.
}}

## Description

Donne la masse totale et la position du centre de masse de l\'ensemble des objets sélectionnés. Les densités de tous les objets peuvent être données. {{Codeextralink|https://raw.githubusercontent.com/chupins/FreeCAD-macros/SC_Branch/Information/CenterOfMass.FCMacro}}

![](images/Macro_CenterOfMass_01.png )

Les valeurs (masse et centre de masse) peuvent être sauvegardés dans une feuille de calcul ![](images/Macro_CenterOfMass_02.png ) 

## Utilisation

Sélectionner les objets

Lancer la macro

## Script

Fichiers d\'icônes à télécharger et coller dans un sous répertoire nommé CenterOfMass à côté du fichier principal

Icône de la toolBar

![](images/Macro_CenterOfMass.png )

![](images/Macro_CenterOfMass_save.png ) ![](images/Macro_CenterOfMass_com.png ) ![](images/Macro_CenterOfMass_compute.png ) ![](images/Macro_CenterOfMass_import.png ) ![](images/Macro_CenterOfMass_material.png )![](images/Macro_CenterOfMass_colorify.png )

Download the [Macro\_CenterOfMass\_Icon](https://forum.freecadweb.org/download/file.php?id=84270) package and extract it in the same directory of the macro. 

**Macro CenterOfMass.FCMacro** Téléchargement sur Github

[Macro CenterOfMass.FCMacro](https://github.com/chupins/FreeCAD-macros/blob/SC_Branch/Information/CenterOfMass.FCMacro)

## Lien

La discussion sur le forum [Macro to compute center of mass](https://forum.freecadweb.org/viewtopic.php?f=24&t=31883)

## Version

0.4.2/2019-06-09: - vérifie le dernier numéro de version sur github et popup si ce n\'est pas la dernière version - mise à jour automatique du show CdG (s\'il existe) lorsque les densités sont modifiées - correction de bugs lors du changement de rayon

0.4.1/2019-05-25: Ajout d\'un bouton de densité par défaut, un curseur de sphère, modifie le comportement de la fenêtre, corrige un problème lié à la partie conteneur

0.3.6 / 2019-05-22 : Le rayon des sphères représentant les centres de masse de chaque solide dépend de chaque masse

0.3.2/2019-03-14 : ajouté un bouton colorify pour donner une couleur aux formes en fonction de leurs densités

0.3.5 / 2019-05-21 : correction du tableau clone

0.3.4 / 2019-03-18 : minor

0.3.3 / 2019-03-17 : lecture du .csv corrections

0.3.2/2019-03-14 : ajouté un bouton colorify pour donner une couleur aux formes en fonction de leurs densités

0.3.0 / 2019-03-03 : python 3 compatibility

0.2.3 / 2018-11-22 : nouveaux nom pour les icônes

0.1.2 / 2018-11-10 : xx

---
[documentation index](../README.md) > Macro CenterOfMass/fr
