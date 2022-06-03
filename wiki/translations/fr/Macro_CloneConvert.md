# Macro CloneConvert/fr
{{Macro/fr
|Name=Macro CloneConvert
|Icon=Macro_CloneConvert.png
|Description={{ColoredText|#ff0000|#ffffff|Dernière mise à jour    * GUI modifiée pour le support HiDPI (QGridLayout). Fonctionne ≥v0.18 (PySide2 Qt5)}}<br/><br/>. 
Pour les versions précédentes, voir [https   *//gist.githubusercontent.com/mario52a/9f2f2f6144e1307a048f1840ef99300c/raw/0a141260ad8d5f67f0fc18b9b40ef37757c06c65/Macro_CloneConvert.FCMacro Macro_CloneConvert] et l'installer manuellement.<br/><br/>Crée un Clone/Copie/Composé de l'objet ou des objets, puis converti dans une position et une taille choisie (''inch, mm, m, µm''...) ou au choix. L'objet de base est reconnu en ''mm'' (base FreeCAD).
|Author=mario52
|Version=0.15
|Date=2020-06-06
|FCVersion= ≥0.18
|Download=[https   *//www.freecadweb.org/wiki/images/0/0a/Macro_CloneConvert.png ToolBar Icon]
}}

## Description

Crée un clone ou une copie de l\'objet puis le convertit dans une position et une taille choisie (*inch, mm, m, µm*\...) ou libre. L\'objet de base est reconnu en *mm* (base FreeCAD).


{{Codeextralink|https   *//gist.githubusercontent.com/mario52a/9f2f2f6144e1307a048f1840ef99300c/raw/39bc54e90b80053a5af76b0b17694cb53697aebd/Macro_CloneConvert.FCMacro}}

## Utilisation

1.  Exécuter la macro
2.  Définissez les paramètres XYZ
3.  Choisissez \"Clone\" ou \"Copie\".
4.  Choisissez une unité de mesure
5.  Sélectionnez votre objet
6.  Cliquez sur **Ok**.

## Remarques

-   Si aucune valeur n\'est entrée une copie ou un clone sera créé sans modification.
-   Si aucun objet n\'est sélectionné le bouton **Ok** change de couleur et devient rouge si l\'opération c\'est bien déroulée le **Ok** devient vert.

La valeur de **BoundingBox**, **Volume** et **Surface** est affichée dans la [Vue Rapport](Report_view/fr.md) dans le cas de **Copier** plusieurs objets, l\'affichage montrera BoundingBox 0.0.

La base est l\'exemple du mm avec un cube de **1 mm** de côtés   *

Sélectionnez dans la liste déroulante (combobox) l\'unité **inch** (pouce), la valeur des champs **Scales free** s\'ajustent automatiquement à **25,4** mm qui correspond à un pouce (ces champs peuvent être modifiés séparément). Cliquez sur le bouton **Ok**, le clone de l\'objet ici le cube de **1 mm** de côtés aura comme dimensions **25,4 mm x 25,4 mm x 25,4 mm**.

**150%** = **1,50** dans les champs **\"Scale free\"**
**104%** = **1,04** dans les champs **\"Scale free\"**

Opération inverse    *

Si vous voulez réduire un objet par exemple le cube de 25,4 mm (1 pouce) en un cube de 1 mm de côtés, utilisez la formule suivante ,

**1 / 25,4 = 0,0393700** et entrez la valeur **0,0393700** (avec une virgule) dans les champs Scale free XY et Z.

Dans un cube de 5 mm, faites **5 / 25,4 = 0,1968503** et entrez la valeur **0,1968503** (avec une virgule) dans les champs Scale free XY et Z.

**50%** = **0,50** dans les champs **\"Scale free\"**
*\' 4%*\' = **0,04** dans les champs **\"Scale free\"**

Les unités prédéfinies sont    * km, hm, dam, m, dm, cm, **mm**, µm, nm, inch, link, foot, yard, perch, chain, furlong, mile, league, nautique.
<img alt="CloneConvert" src=images/Macro_CloneConvert_01.png  style="width   *350px;">

-   **Mode**
-   **Clone    *** Crée un clone de ou des objet(s) sélectionné(s).
-   **Copy    *** Crée une copie de ou des objet(s) sélectionné(s).
-   **Comp    *** Crée un compound de ou des objet(s) sélectionné(s)
-   **Increm.    *** incrémente les coordonnées à la position (Placement, Rotation \... ) actuelle de la sélection
    Si la case n\'est pas activée le Placement commence aux coordonnées 0,0,0 de FreeCAD
    Dans le cas d\'un compound, le placement renseigné dans la vue combinée est \[0,0,0\], le placement commence à la position de l\'objet
    Dans ce cas le Placement ne commence pas à la position 0,0,0 utilisez le bouton **ValueAt()**
    pour obtenir le Placement réel du sous objet sélectionné Face, Wire, Line \....
-   **Unique    *** Si cette case est cochée et que plusieurs objets sont sélectionnés il sera créé un seul objet à l\'échelle demandée, si non les objets créés sont indépendants.

-   **Coordonnées**
-   ****...**    *** Ce bouton aligne les valeurs YZ à la valeur X pour obtenir le mêmes valeurs ​​XYZ (ou manuellement)
    Deux clics sur le bouton mettent les coordonnées à 0.0
-   **Coordinate X    *** Déplace l\'objet aux coordonnées de placement X (facultatif) (Base 0,0,0 si Increm. n\'est pas activé)
-   **Coordinate Y    *** Déplace l\'objet aux coordonnées de placement Y (facultatif) (Base 0,0,0 si Increm. n\'est pas activé)
-   **Coordinate Z    *** Déplace l\'objet aux coordonnées de placement Z (facultatif) (Base 0,0,0 si Increm. n\'est pas activé)

-   **Rotation**
-   ****...**    *** Ce bouton aligne les valeurs Pitch et Roll à la valeur Pitch pour obtenir le mêmes valeurs ​​XYZ (ou manuellement)
    Deux clics sur le bouton mettent les coordonnées à 0.0
-   **Yaw (Z )    *** Donne un angle de rotation dans l\'axe Z (Yaw) (Début 0 si Increm. n\'est pas validé)
-   **Pitch ( Y )    *** Donne un angle de rotation dans l\'axe Y (Pitch) (Début 0 si Increm. n\'est pas validé)
-   **Roll ( X )    *** Donne un angle de rotation dans l\'axe X (Roll) (Début 0 si Increm. n\'est pas validé)

-   **Scale predefined**
-   **Scale predefined    ***Les unités d\'échelle predefinies, km, hm, dam, m, dm, cm, **mm**, µm, nm, inch, link, foot, yard, perch, chain, furlong, mile, league, nautique ou choisissez une valeur libre dans les champs Scale free.

-   \'\'\'Number copy \'\'\'
-   **Number copy    *** Nombre de copies désirées

-   **Scale free**
-   ****...**    *** Ce bouton aligne les valeurs YZ à la valeur X pour obtenir le mêmes valeurs ​​XYZ (ou manuellement)
    Deux clics sur le bouton mettent les coordonnées à 1.0
-   **Scale X    *** échelle libre, si la valeur entrée est négative ex   * **( -10)** , l\'objet sera mis à l\'échelle de **10** fois et sera inversé dans l\'axe **X**, pour réduire l\'objet, il faut entrer une valeur décimale exemple **(0,5)** réduira l\'objet de 1/2 dans l\'axe X.
-   ****...**    *** Ce bouton aligne la valeur des axes YZ à la valeur de X si vous voulez que les trois valeurs XYZ soient égales.
-   **Scale Y    *** échelle libre, si la valeur entrée est négative ex   * **( -10)** , l\'objet sera mis à l\'échelle de **10** fois et sera inversé dans l\'axe **Y**, pour réduire l\'objet, il faut entrer une valeur décimale exemple **(0,5)** réduira l\'objet de 1/2 dans l\'axe Y.
-   **Scale Z    *** échelle libre, si la valeur entrée est négative ex   * **( -10)** , l\'objet sera mis à l\'échelle de **10** fois et sera inversé dans l\'axe **Z**, pour réduire l\'objet, il faut entrer une valeur décimale exemple **(0,5)** réduira l\'objet de 1/2 dans l\'axe Z.

-   ****ValueAt()**    *** Donne le vecteur valueAt() du sous objet sélectionné Face, Wire, Line \...
    Cette option est intéressante lorsque les données de Placement renseignées sont \[0,0,0\] et que l\'emplacement réel de l\'objet est éloigné des coordonnées de base \[0,0,0\]
    (ne donne pas de renseignement sur la rotation de l\'object)
-   ****Ok**    *** Le bouton **OK** valide et lance la commande, si aucun objet n\'est sélectionné le bouton **Ok** se colore en rouge.
-   ****Reset**    *** Le bouton **Reset** met toutes les variables à zéro
-   ****Quit**    *** Le bouton **Quit** quitte la macro.




## Script

L\'icône de la macro ![](images/Macro_CloneConvert.png ) qui servira pour votre barre d\'outils

**Macro\_CloneConvert.FCMacro**

Téléchargez la macro sur Gist [**Macro\_CloneConvert.FCMacro**](https   *//gist.github.com/mario52a/9f2f2f6144e1307a048f1840ef99300c)

## Révisions

06/06/2020 ver 0.15 = icon

20/05/2020 ver 0.14 = grid layout PySide2 Qt5

ver 0.13 = 15/09/2019 remplacé le signe grec micro par \"um\" (trop de problèmes avec caractères ascii au dessus de 127) , remplacé tous les \"\_translate(\"MainWindow\", \"mm\", None)\" par \"mm\" et commenté la ligne \"text.encode(\'utf-8\')\" ne fonctionne pas avec la version 0.19 18.213

01/06/2019 ver 0.12 = adapté pour 0.19 et correction \"Copy   *legacy=True\" et ShapeColor \.....

30/03/2018 ver 0.11 = ajout checkBox, si multi sélection le clone est un objet unique ou des objets séparés

07/06/2017 ver 0.10 = replace Draft\...Copy to Part..Shape cause section Copy    * ne pas fait pas de copie mise à l\'échelle de l\'objet mais copie l\'objet sans mise à l\'échelle ??

14/06/2016 ver 0.9 = Ajout du choix du nombre de copies et optimisation des étiquettes

31/01/2016 ver 0.8 = modification des boutons reset des sections il faut cliquer deux fois sur le bouton pour mettre les valeurs à 0(indispensable en cas de modification des valeurs)

30/01/2016 ver 0.7 = réécriture du code avec Placement et Increment et ajout des boutons Compound, Increment, ValueAt(),

26/01/2016 ver 0.6 = correction placement avec plusieurs objets (copy)

26/07/2015 ver 0.5 = correction rotation avec plusieurs objets fonction Copy

25/07/2015 ver 0.4 = ajout rotation

11/08/2014 replace \"AttributeError\" to \"Exception\"

02/07/2014 ver. 0.3 = modification fonctionne avec PyQt4 et PySide

09/05/2014 ver. 0.2 = ajout de la fonction \"Copy\"



---
![](images/Right_arrow.png) [documentation index](../README.md) > Macro CloneConvert/fr
