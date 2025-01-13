# Macro AeroFoil/fr
{{Macro/fr
|Name=Macro AeroFoil
|Name/fr=Macro AeroFoil
|Icon=AeroFoil.png
|Description=AeroFoil crée des courbes et des faces de profils aérodynamiques en utilisant des modèles prédéfinis, des fonctions algébriques et des fichiers DAT ou CSV.
|Author=Melwyncarlo
|Date=2021-03-10
|Version=2.0.1
|FCVersion={{VersionPlus/fr|0.17}}
|Download=[https://wiki.freecad.org/images/5/59/AeroFoil-reduced.png Icône de la barre d'outils]
|Links=[https://github.com/melwyncarlo/AeroFoil Github personnel- AeroFoil]<br>[https://github.com/FreeCAD/FreeCAD-macros/tree/master/ObjectCreation Github FreeCAD- AeroFoil]<br>[https://forum.freecadweb.org/viewtopic.php?f=22&t=56162 FC Forum - AeroFoil]
}}

## Description

**AeroFoil** est une macro pour être utilisée dans l\'application FreeCAD. AeroFoil crée des courbes et des faces de profils aérodynamiques en utilisant des modèles prédéfinis, des fonctions algébriques, ainsi que des fichiers DAT ou CSV importés.

![](images/AeroFoil-reduced.png )    Icône **AeroFoil Macro**.

La macro AeroFoil peut être téléchargée en utilisant le [gestionnaire des extensions](Std_AddonMgr/fr.md) intégré au logiciel FreeCAD.



#### Fonctions principales 

-   Affinement des points du profil aérodynamique
-   Génération de copies multiples de profils aérodynamiques
-   Sortie de courbes 2D et de faces planes
-   Création de DWire/polyligne et B-spline
-   Création de l\'atelier Sketcher et de l\'atelier Draft
-   Esquisses entièrement contraintes dans l\'atelier Sketcher
-   Génération de courbes de voilure divisées (supérieure et inférieure)
-   Solveurs NACA à 4 et 5 chiffres prêts à l\'emploi
-   Analyseur de fonctions de courbes symétriques et asymétriques
-   Analyseur de données de fichiers texte DAT et de feuilles de calcul CSV.
-   Entrée de la longueur de la corde en mm, cm, m, in, ft et yards.



#### Fonctions supplémentaires {{VersionPlus/fr|0.19}} 

Propriétés de l\'objet AeroFoil *(en lecture seulement)* :
{{Properties Title|Base}}

-    {{PropertyData/fr|Airfoil Type|String}}
    

-    {{PropertyData/fr|Airfoil Chord Length|Length}}
    

-    {{PropertyData/fr|Design Curve Type|String}}
    

-    {{PropertyData/fr|Number Of Points|Integer}}
    

\[\[<File:AeroFoil-output-types.gif%7Cframe%7Ccenter%7Calt=AeroFoil-output-types.gif>\|


<div style="text-align: center">

Légende : types de sortie de la macro AeroFoil


</div>

\]\]

\[\[<File:AeroFoil-input-types.gif%7Cframe%7Ccenter%7Calt=AeroFoil-input-types.gif>\|


<div style="text-align: center">

Légende : types d\'entrée de la macro AeroFoil


</div>

\]\]

## Installation

####  Linux

AeroFoil peut être installé manuellement, comme sous Windows, ou en utilisant le terminal de commande et ses commandes appropriées, comme indiqué dans le fichier [INSTALL](https://raw.githubusercontent.com/melwyncarlo/AeroFoil/main/INSTALL.sh).

Par défaut, le terminal de commande Linux peut être lancé en appuyant simultanément sur les touches suivantes du clavier :

**Control** + **Alt** + **T**



####  Windows

AeroFoil peut être installé à l\'aide des deux étapes suivantes :

1.  Téléchargez le fichier [AeroFoil.zip](https://github.com/melwyncarlo/AeroFoil/blob/main/AeroFoil.zip?raw=true).
2.  Extrayez le contenu du fichier ZIP dans l\'emplacement du répertoire de la macro utilisateur de FreeCAD.

Par défaut, le répertoire de la macro utilisateur de FreeCAD doit être situé à :

C:/Users/User_Name/AppData/Roaming/FreeCAD/Macro



## Utilisation

AeroFoil peut être chargé en effectuant les étapes suivantes :

1.  Lancez l\'application **FreeCAD**.
2.  Allez dans **Macro → Macros ...**.
3.  Cliquez sur l\'onglet **Macros utilisateur** dans la boîte de dialogue contextuelle.
4.  Sélectionnez **AeroFoil.FCMacro**.
5.  Cliquez sur **Execute**.

Une fois la macro AeroFoil chargée, suivez les instructions des boîtes de dialogue respectives, remplissez les données pertinentes et naviguez en conséquence. En cas d\'erreur ou d\'avertissement, vous en serez automatiquement informé. Si l\'on vous demande de signaler une erreur inattendue, communiquez l\'erreur en mentionnant la version de FreeCAD, en retraçant les étapes suivies et en indiquant si un résultat a été généré (et dans quelle mesure).



#### Remarques

   
  \(1\)   L\'exécution de la macro avec des points personnalisés et un affinement ne produit aucun changement visible.
  \(2\)   Les propriétés de l\'objet AeroFoil ne sont visibles que sur la version 0.19 du logiciel FreeCAD. Sur les versions antérieures, un avertissement s\'affiche sur la console. Cet avertissement n\'affectera pas le résultat.
          
   



#### Conseils à garder à l\'esprit pendant l\'utilisation 

1.  Pour les profils NACA, les deux derniers chiffres (combinés) ne peuvent pas avoir une valeur nulle ; l\'épaisseur ne peut pas être une valeur nulle.
2.  Les profils NACA à 5 chiffres sont limités aux modèles suivants (\'XX\' indique les deux derniers chiffres, l\'épaisseur, du profil) :
    -   210XX
    -   220XX
    -   221XX
    -   230XX
    -   231XX
    -   240XX
    -   241XX
    -   250XX
    -   251XX
3.  Pour les fonctions de courbe, n\'utilisez que les caractères et fonctions préétablis.
4.  Pour les fonctions de courbe, $2 * x$ est correct, alors que $2x$ est incorrect.
5.  Pour les fonctions de courbe, $y = f(x)$ va de **0** à **1**, tous deux inclus.
6.  Pour les fonctions de courbe, le *thêta* trigonométrique est en degrés (**θ °**)
7.  Pour les fonctions de courbe, le *thêta* trigonométrique va de **0°** à **360°**, sous réserve des limites de calcul.
8.  Les courbes ou les points qui se croisent entre **0** et **1**, tous deux exclusifs, renverront une erreur.
9.  Les courbes ou les points qui contiennent les données du profil inférieur ne peuvent pas être reflétés.
10. Pour les importations de fichiers, il est suggéré de laisser les numéros de ligne, de rangée et de colonne à leurs valeurs par défaut, sauf si vous êtes bien informé.
11. Augmenter des paramètres **refine** et **quantity** allonge le temps de calcul et les ressources.
12. La longueur absolue de la corde, en millimètres, ne peut être inférieure à **1mm**.

\[\[<File:AeroFoil-preset-functions.png%7Cframe%7Ccenter%7Calt=AeroFoil-preset-functions.png>\|


<div style="text-align: center">

Légende : caractéristiques et fonctions prédéfinies


</div>

\]\]

## Script


{{MacroCode|code=

__Title__         = "AeroFoil"
__Author__        = "Melwyncarlo"
__Version__       = "2.0.0"
__Date__          = "2021-03-09"
__Comment__       = "AeroFoil creates airfoil curves and faces using pre-defined models, algebraic functions, and DAT or CSV Files"
__Web__           = "https://github.com/melwyncarlo/AeroFoil"
__Wiki__          = "http://www.freecadweb.org/wiki/index.php?title=Macro_AeroFoil"
__Icon__          = "https://wiki.freecad.org/images/5/59/AeroFoil-reduced.png"
__Help__          = "Click on the AeroFoil button/macro, and follow the instructions in the subsequent dialog boxes."
__Status__        = "stable"
__Requires__      = "Freecad >= v0.17"
__Communication__ = "https://github.com/melwyncarlo/AeroFoil/issues"
__Files__         = "AeroFoil_UI_Files/AeroFoil_Initial_Dialog.ui, AeroFoil_UI_Files/AeroFoil_NACA4Digit_Dialog.ui, \
AeroFoil_UI_Files/AeroFoil_NACA5Digit_Dialog.ui, AeroFoil_UI_Files/AeroFoil_CurvesInput_Dialog.ui, \
AeroFoil_UI_Files/AeroFoil_PointsInput_Dialog.ui, AeroFoil_UI_Files/AeroFoil_DATInput_Dialog.ui, \
AeroFoil_UI_Files/AeroFoil_CSVInput_Dialog.ui, AeroFoil_UI_Files/AeroFoil_FileLoad_Dialog.ui, \
AeroFoil_UI_Files/AeroFoil_Final_Dialog.ui, AeroFoil_UI_Files/AeroFoil_Math_Functions_Box.ui, \
AeroFoil_UI_Files/AeroFoil_mfb_img.gif, AeroFoil_UI_Files/AeroFoil.svg"



#  OS: Ubuntu 18.04.5 LTS
#  Word size of OS: 64-bit
#  Word size of FreeCAD: 64-bit
#  Version: 0.18.4.
#  Build type: Release
#  Python version: 3.6.8
#  Qt version: 5.9.5
#  Coin version: 4.0.0a
#  OCC version: 7.3.0
#  Locale: English/UnitedKingdom (en_GB)

#  OS: Ubuntu 18.04.5 LTS (LXDE/Lubuntu)
#  Word size of OS  : 64-bit
#  Word size of FreeCAD: 64-bit
#  Version: 0.19
#  Build type: Release
#  Branch: unknown
#  Hash: 32200b604d421c4dad527fe587a7d047cf953b4f
#  Python version: 3.6.9
#  Qt version: 5.9.5
#  Coin versio: 4.0.0a
#  OCC version: 7.3.0
#  Locale: English/UnitedKingdom (en_GB)



}}


{{Codeextralink|https://raw.githubusercontent.com/melwyncarlo/AeroFoil/main/AeroFoil.FCMacro}}



## Liens

\[1\] [Dépôt Github d\'AeroFoil](https://github.com/melwyncarlo/AeroFoil)
\[2\] [Dépôt Github des macros FreeCAD - AeroFoil](https://github.com/FreeCAD/FreeCAD-macros/tree/master/ObjectCreation)
\[3\] [Page de discussion du forum FreeCAD - AeroFoil](https://forum.freecadweb.org/viewtopic.php?f=22&t=56162)
\[4\] [Airfoil Tools](http://airfoiltools.com/) contient environ 1 638 profils aérodynamiques différents.
\[5\] [UIUC Airfoil Coordinates Database](https://m-selig.ae.illinois.edu/ads/coord_database.html) contient près de 1 600 profils aérodynamiques différents.



---
⏵ [documentation index](../README.md) > Macro AeroFoil/fr
