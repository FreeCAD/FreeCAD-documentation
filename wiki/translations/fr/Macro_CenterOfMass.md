# Macro CenterOfMass/fr
{{Macro/fr
|Name=Macro CenterOfMass
|Description=Donne la masse totale et la position du centre de masse de l'ensemble des objets sélectionnés. 
|Author=chupins, s-quirin
|Version=0.5.0
|Date=2022-04-06
|FCVersion>=0.19
}}

## Description

Donne la masse totale et la position du centre de masse de l\'ensemble des objets sélectionnés. Les densités de tous les objets peuvent être données. {{Codeextralink|https://raw.githubusercontent.com/FreeCAD/FreeCAD-macros/master/Information/CenterOfMass.FCMacro}}

![](images/CenterOfMass_exemple.png )

## Utilisation

Sélectionner les objets

Lancer la macro

## Script

Téléchargez la macro depuis GitHub : [Macro CenterOfMass.FCMacro](https://github.com/FreeCAD/FreeCAD-macros/blob/master/Information/CenterOfMass.FCMacro)

Téléchargez le fichier de l\'icône de la barre d\'outils et placez-le dans un sous-répertoire nommé CenterOfMass dans le répertoire de la macro : ![](images/Macro_CenterOfMass.png )

## Lien

La discussion sur le forum [Macro to compute center of mass](https://forum.freecadweb.org/viewtopic.php?f=24&t=31883)

## Version

0.5.0 / 2022-04-06 : réécriture complète par s-quirin (projet SyProLei (Université de la Sarre))

-   Nouveau : Base de code, exigence augmentée à Qt5.12+ et Python3 (FreeCAD 0.19).
-   Nouveau : Afficher la masse de chaque solide.
-   Nouveau : La fenêtre de démarrage est ancrée ou flottante (peut être définie dans l\'éditeur de paramètres).
-   Nouveau : La sélection correspond à l\'arborescence ou est triée par nom (peut être réglé dans l\'éditeur de paramètres).
-   Nouveau : Option pour sauvegarder les densités dans le document.
-   Amélioré : L\'aspect et la convivialité de la même interface que FreeCAD.
-   Amélioré : Palette de couleurs à échelle (du vert au rouge) pour colorier les formes.
-   Amélioré : Visualisation du déplacement du centre de masse sur la géométrie.
-   Amélioration : Suivi interne des unités.
-   Correction : Gestion des groupes et des objets de groupe.
-   Correction : Gestion de App::Link.
-   Correction : Remplacement d\'une classe Qt dépréciée.

0.4.2 / 2019-06-09: - vérifie le dernier numéro de version sur github et popup si ce n\'est pas la dernière version - mise à jour automatique du show CdG (s\'il existe) lorsque les densités sont modifiées - correction de bugs lors du changement de rayon

0.4.1/2019-05-25: Ajout d\'un bouton de densité par défaut, un curseur de sphère, modifie le comportement de la fenêtre, corrige un problème lié à la partie conteneur.

0.3.6 / 2019-05-22 : Le rayon des sphères représentant les centres de masse des solides dépend de leurs masses.

0.3.5 / 2019-05-21 : Correction des tableaus et clone.

0.3.4 / 2019-03-18 : Mineur.

0.3.3 / 2019-03-17 : Chargement des corrections .csv.

0.3.2/2019-03-14 : Ajout d\'un bouton poussoir de colorisation pour ajouter de la couleur aux formes en fonction de leur densité.

0.3.0 / 2019-03-03 : Compatibilité avec Python 3.

0.2.3 / 2018-11-22 : Nouveau nom d\'icône.

0.1.2 / 2018-11-10 :



---
![](images/Right_arrow.png) [documentation index](../README.md) > Macro CenterOfMass/fr
