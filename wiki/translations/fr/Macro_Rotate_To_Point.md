# Macro Rotate To Point/fr
{{Macro/fr
|Name=Macro Rotate To Point
|Icon=Macro_Rotate_To_Point.svg
|Description=Macro pour faire tourner un objet sur lui-même sur un axe de rotation : centre de la boîte, centre de masse, direction du fil ou dernier point cliqué. <br/>Vous pouvez sauvegarder les coordonnées travaillées dans un fichier coordonnées [(0.06,1.30,0.0),(85.0,0.0,0.0)] ou dans une macro complète pour créer une animation.
|Author=Mario52
|Version=00.11
|Date=2022/10/17
|FCVersion=0.19 et plus
|Download=[https://www.freecadweb.org/wiki/images/d/d1/Macro_Rotate_To_Point.svg Icône de la barre d'outils]
}}

## Description

Macro pour faire tourner un objet sur lui-même avec l\'axe de rotation étant soit le :

-   centre de la boîte
-   centre de masse
-   direction du fil
-   dernier point cliqué
-   sur un chemin

Vous pouvez enregistrer dans un fichier toutes les coordonnées travaillées et les sauvegarder dans un fichier \"Coordonnées \[(0.06,1.30,0.0),(85.0,0.0,0.0)\],\" ou dans une macro complète avec différentes options (Créer une image de série) pour créer une animation, augmentation/diminution, pause, yoyo\...


{{Codeextralink|https://gist.githubusercontent.com/mario52a/2fc48333deca5a31e6232c29a9db5e4c/raw/d9419d4bb13e36940eb2f56c3c469ea4182827ee/Macro%2520Rotate%2520To%2520Point.FCMacro}}

## Utilisation

1.  Téléchargez la macro depuis le <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Gestionnaire des extensions](Std_AddonMgr/fr.md)
2.  Exécutez la macro
3.  Sélectionnez un objet
4.  Choisissez l\'une des orientations suivantes :

![Interface Rotate to point](images/Macro_Rotate_To_Point_00.png )

### \[1\] Position Rotation 

*Première opération*

![ \[1\] Position Rotation](images/Macro_Rotate_To_Point_Position-Rotation00.png )

-    {{CheckBox|Translation}}: Si ce checkBox est {{CheckBox|TRUE|activé}} la rotation est désactivée, le placement de l\'objet se fait sur l\'axe ou le chemin sélectionné.

*Le SpinBox {{SpinBox|1,00000 Degrees}} est réinitialisé à `0.0` et coloré en rouge.*

-   Le chronomètre affiche le temps passé avec votre macro préférée.

### \[2\] Translation Rotation 

*Seconde opération*

![\[2\]Translation Rotation](images/Macro_Rotate_To_Point_Translation-Rotation00.png )

### Point Rotation 

-   Boundbox Center : Sélectionnez la rotation du centre BoundBox à l\'axe
-   Center of Mass : Sélectionnez la rotation du centre de masse à l\'axe
-   Point Clicked : Sélectionnez le dernier clic de souris comme point de rotation de l\'axe
    -   1 : Sélectionnez l\'objet
    -   2 : Utilisez la touche **CTRL** pour choisir un objet supplémentaire

### Axis Rotation 

-   Rotation(Z) Yaw : Axe de lacet
-   Rotation(Y) Pitch : Axe de tanguage
-   Rotation(X) Roll : Axe de roulis
-   Rotation(D) Direction : Rotation autour de la ligne, bord sélectionné
-   Follow the path : Suivez le chemin créé par le fil, la ligne, le bord.
    -   1 : Sélectionnez l\'objet
    -   2 : Sélectionnez le chemin
    -   3 : Sélectionnez la distance

*Le SpinBox {{SpinBox|1,00000 Degrees}} ESTs réinitialisé à `0.0` et coloré en rouge*

### Coordinates Point clicked 

![Rotate To Point Coordinate-On-Point-Clicked](images/Macro_Rotate_To_Point_Coordinate-On-Point-Clicked_00.png )

-   DoubleSpinBox : Coordonnée X au clic de la souris (modifiable uniquement avec le mode \"Point Clicked\")
-   DoubleSpinBox : Coordonnée Y au clic de la souris (modifiable uniquement avec le mode \"Point Clicked\")
-   DoubleSpinBox : Coordonnée Z au clic de la souris (modifiable seulement avec le mode \"Point Clicked\")

### \[3\] Work (Box : Cube) 

\"Troisième opération\"

![Macro Rotate To Point Work](images/Macro_Rotate_To_Point_Work_00.png )

-    {{CheckBox|View}}: Si la case est cochée, la vue revient sur la dernière vue de l\'objet sélectionné (fonctionne avec la comboBox en dessous) et tous les paramètres sont restaurés.

-    **Point**: Si cette case à cocher est cochée, un point est créé pour visualiser l\'axe de rotation des points: rouge X, vert Y, bleu Z.

-    **Center**: Un point est créé au centre du cercle.

-    {{ComboBox|Box}}: Liste de tous les objets utilisés. Si le choix de l\'objet est fait ici, le zoom *(si la vue checkBox est cochée)* est retourné et tous les paramètres restaurés..

-    {{ComboBox|0}}: Valeurs prédéfinies.

-    {{ComboBox|1.0}}: Sélectionne une valeur utilisée.

-    **- Invert**: Inverse le signe Positif/Négatif de la valeur affichée.

-    {{SpinBox|0,0000}}: Entrez la modification.

-    **Apply**: Applique la modification à l\'objet.

-   Line Edit: L\'édition de ligne affiche les coordonnées d\'origine de l\'axe sélectionné + les données d\'entrée données dans la spinBox

-   Les coordonnées sont affichées

### Data to save 

![Rotate To Point Data-To-Save](images/Macro_Rotate_To_Point_Data-To-Save_00.png )

-   Fenêtre d\'affichage des coordonnées mémorisées

-    **Clear**: Supprime et nettoie l\'éditeur de texte

-    **Delete**: Efface la ligne sélectionnée

-    {{CheckBox|Memo on Click}}:

-    **Memorize**: Mémorise et affiche les coordonnées

-    **Save**: Sauve les données dans un fichier

-    {{CheckBox|Macro}}:

    -   Mode normal {{CheckBox|Macro}} Les coordonnées sont sauvegardées dans ce mode : **\[(0.06,1.30,0.0),(85.0,0.0,0.0)\],**

    -   Mode macro {{CheckBox|TRUE|0,0 Coordinate}} Les coordonnées sont sauvées dans une macro complète (un ou plusieurs objet(s)) directement dans votre répertoire de macros avec le même nom que le document et l\'extension .FCMacro
        -   **Options de la macro**
        -   **\_\_pompe\_\_\_\_engrenage\_\_** : Nom du document
        -   **\_\_22 Coordinates\_\_** : Nombre de coordonnées
        -   **Type Key Q to Quit** : Quitte la macro
        -   **Type Key A to Create serial image** : crée une série d\'images pour créer un Animate GIF (avec Gimp ou autre)
        -   **Type Key D to Decrease speed** : Diminue la vitesse de l\'animation
        -   **Type Key I to Increase speed** : Augmente la vitesse de l\'animation
        -   **Type Key P to Pause/Continue or key RETURN or ESCAPE** : Pause / Animation
        -   **Type Key S to Step by Step (key RETURN or ESCAPE to continue)** : Pas à pas (Step by Step)
        -   **Type Key V to reVerse** : reVerse la video
        -   **Type Key Y to YoYo** : du début à la fin et reverse de la fin au début
        -   **Type Key M for this message** : Affiche ce memo
        -   Pour utiliser ces options, cliquez avrc la souris dans la vue 3D et tapez la clé désirée.
        -   \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

    -   
        {{CheckBox|Memo on Click}}
        
        : Mode normal. Les données ne sont pas sauvées dans la fenêtre de mémorisation, vous devez sauver les coordonnées avec le bouton **Memo (2)** (Le compteur affiche le nombre de coordonnées sauvées)

    -   
        {{CheckBox|TRUE|Memo on Demand}}
        
        : Mode Memo on Click. Les données sont automatiquement sauvées a chaque clic sur le bouton **Apply**

-    **Copy**: Mémoriser le contenu de la fenêtre dans format Rotate_To_Point : `["Body004001",(0.0,0.0,-1.5),(0.0,0.0,0.0)],`

### Command

![Rotate To Point Command](images/Macro_Rotate_To_Point_Command_00.png )

-    **Quit**: Quitter la macro.

-    **Original**: Après avoir modifié les données de l\'objet, vous pouvez revenir à l\'emplacement d\'origine, si vous n\'avez pas désélectionné l\'objet actuel.

-    **0,0,0**: Cette option place l\'objet en coordonnées de base `0,0,0`.

-    **Reset**: Réinitialisez les données dans la macro et désélectionnez l\'objet en cours (même clic de souris dans la [vue 3D](3D_view/fr.md)).

Icône pour la barre d\'outils (PNG) ![](images/Macro_Rotate_To_Point.png ) ou (SVG) ![](images/Macro_Rotate_To_Point.svg )

## Exemple

![](images/Macro_Rotate_To_Point_01.gif )

## Liens

Le forum [feature req: placement - rotate part around its midpoint](http://forum.freecadweb.org/viewtopic.php?f=8&t=20925)

Mes macro sur Gist [mario52a](https://gist.github.com/mario52a)

## Version

2022/10/17 Version=00.11 : nouvelle organisation GUI, Déplacement sur un chemin, restitution de la vue et des données de l\'objet, Bouton Copy, ajout menu Image dans la macro sauvée, ajout d\'un \"QtWidgets.QScrollArea()\" \...

2021/03/08 Version=00.10 : ajout du zoom sur l\'objet cliqué, valeur mémoire, valeurs imposées

2021/02/25 Version=00.09 : correction de la macro créée : cause multi objets possible


{{Code|
App.ActiveDocument.getObject(p[0]).Placement
}}

instead {{Code|
myObject.Placement
}}

2021/02/22 Version=00.08c : correct le center facePoint (19h26 Paris)

2021/02/22 Version=00.08b : correct le center facePoint (17h23 Paris)

2021/02/22 Version=00.08 : ajout sauvegarde du fichier macro avec un ou plusieurs objets déplacés

2021/01/24 Version=00.07 : ajout de l\'option R: reverse

2021/01/12 ver 00.06 : ajout de la section Data et d\'autres options

2020/03/07 ver 00.05.2 : correction du bug translation effacée \"direction = myObject.Placement.Rotation.multVec(direction)\"

2020/03/01 ver 00.05.1 : correction de la position du test \"FreeCAD version\"

2020/02/29 ver 00.05 : conversion pour Hdpi (Layout) et ajout fonction Direction

06/04/2019 ver 00.04 : Python 3

29/03/2018 ver 00.03 : commenter les lignes \"FreeCAD.ActiveDocument.recompute()\" le changement de valeur est trop lente dans FreeCAD 0.17\.... voir [FC0.17 recompute strange behaviour (regression)](https://www.forum.freecadweb.org/viewtopic.php?f=10&t=27732&p=224195#p224195)

27/03/2017 ver 00.02 : modification du spinbox \"Pos\" maintenant accepte les valeurs négatives

05/03/2017 ver 00.01 : ajout de 3 boîtes de dialogue pour afficher les coordonnées X Y Z au clic de souris

04/03/2017 ver 00.00



---
⏵ [documentation index](../README.md) > Macro Rotate To Point/fr
