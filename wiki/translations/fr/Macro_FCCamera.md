# Macro FCCamera/fr
{{Macro/fr
|Name=Macro FCCamera
|Icon=FCCamera_00.png
|Description={{ColoredText|#ff0000|#ffffff|Nouvelle version de l'interface modifiée pour HD dpi (QGridLayout) fonctionnant uniquement avec FC version 0.18 et plus (PySide2 Qt5)}}<br/>Pour les versions précédentes, voir [https://gist.githubusercontent.com/mario52a/4aa545c23b323cf68824/raw/42dc3ef73dc8db463a03b175f5a7f1f6978e3293/Macro%2520FCCamera.FCMacro FCCamera] et l'installer manuellement.<br/><br/>
Cette macro peut faire pivoter l'écran selon un angle défini et l'axe défini et crée un plan pour faire face à l'écran afin de créer un formulaire dans les positions du plan spécifiées : la face sélectionnée faisant face à l'écran, pour détecter la position de la caméra, aligner la vue sur la face ou sur l'axe, aligner l'objet à voir.
|Author=Mario52
|Version=0.14
|Date=2020/10/20
|FCVersion=0.18 et plus
|Download=
}}

## Description

Cette macro permet de faire pivoter l\'écran selon un angle et un axe définis et de créer un plan face à l\'écran pour créer une forme dans le plan spécifié, de positionner la face sélectionnée face à l\'écran, de détecter la position de la caméra, d\'aligner la vue sur la face ou sur l\'axe, d\'aligner l\'objet sur la vue.


{{Codeextralink|https://gist.githubusercontent.com/mario52a/4aa545c23b323cf68824/raw/98d90ee303e9fa5d6aed6e9f2e36e7ca1a18ca19/Macro%2520FCCamera.FCMacro}}



## Utilisation

<img alt="FCCamera" src=images/Macro_FCCamera_00.png  style="width:250px;">

**Camera of Axis** : boîte de dialogue pour entrer les valeurs de rotation en degrés (la rotation se fait sur un angle à la fois).

**Angle de rotation de l\'axe en degrés** : sélectionner l\'axe de rotation **X**, **Y** ou **Z**.

**Axe of rotation**

-   <img alt="" src=images/FCCamera_01.png  style="width:24px;"> **Accept the rotation** : effectue la rotation selon l\'angle donné.

**Virtual**

-   <img alt="" src=images/FCCamera_02.png  style="width:24px;"> **Detect camera orientation** : détecte l\'orientation de la camera et affiche les résultats dans la vue rapport. Les valeurs retournées proviennent de la fonction **getCameraOrientation()**.

**Align view to face selected**

-   <img alt="" src=images/FCCamera_03.png  style="width:24px;"> **To Face.** : aligne la face sélectionnée sur la vue 3D (face à l\'écran). Chaque clic change la vue de l\'objet sélectionné pour **NormalAt** : \"(0,0,1) (0,0,-1) (0,1,0) (0,-1,0) (1,0,0) (-1,0,0)\"

-   <img alt="" src=images/FCCamera_04.png  style="width:24px;"> **To Axis.** : aligne la vue sur la face de l\'axe sélectionnée. (face à l\'écran). Chaque clic change la vue de l\'objet sélectionné pour **Surface Axis** : \"(0,0,1) (0,0,-1) (0,1,0) (0,-1,0) (1,0,0) (-1,0,0)\"

-   <img alt="" src=images/FCCamera_05.png  style="width:24px;"> **Align object to view.** : aligne l\'objet sélectionné à la vue en cours. Les valeurs modifiées sont : Rotation Axis((X, Y, Z), Angle), Euler angles identiques : Lacet (Yaw), Tangage (Pitch), Roulis (Roll), la translation n\'est pas modifiée.

-   <img alt="" src=images/FCCamera_06.png  style="width:24px;"> **Create plane of view.** : un plan circulaire est créé face à l\'écran aux coordonnées du clic de souris sur l\'objet. Le rayon du plan circulaire est égal à la plus grande dimension du boîte englobante. Si aucun objet n\'est sélectionné le plan est créé aux coordonnées 0, 0, 0 avec un rayon de 20 mm. Le rayon du plan par défaut peut être modifié à la ligne 515 :


```python
        rayon = 20                            # Radius of plane
```

-    **[<img src=images/FCCamera_07.png style="width:24px"> Reset.**: réinitialise toutes les valeurs

-    **[<img src=images/FCCamera_00.png style="width:24px"> Photo.**: section enregistrant la rotation de l\'écran d\'une image en valeur d\'angle

-    **[<img src=images/FCCamera_08.png style="width:24px"> Quit.**: quitter FCCamera




## Section Photo 

<img alt="FCCamera" src=images/Macro_FCCamera_00b.png  style="width:250px;"> 

-    **ComboBox Actual **: choisir la définition de l\'écran déterminera les dimensions de l\'image

    -   Available (pre-defined) :
        -   \"Actual\" (définition en cours de l\'écran)
        -   \"Icon 16 x 16\"
        -   \"Icon 32 x 32\"
        -   \"Icon 64 x 64\"
        -   \"Icon 128 x 128\"
        -   \"CGA 320 x 200\"
        -   \"QVGA 320 x 240\"
        -   \"VGA 640 x 480\"
        -   \"SVGA 800 x 600\"
        -   \"XGA 1024 x 768\"
        -   \"XGA+ 1152 x 864\"
        -   \"SXGA 1280 x 1024\"
        -   \"SXGA+ 1400 x 1050\"
        -   \"UXGA 1600 x 1200\"
        -   \"QXGA 2048 x 1536\"
        -   \"Free\"

-    **SpinBox X and Y **
    

-    **ComboBox  Format image**-   Available :
        -   \"BMP \*.bmp\"
        -   \"ICO \*.ico\"
        -   \"JPEG \*.jpeg\"
        -   \"JPG \*.jpg\"
        -   \"PNG \*.png\" (by default)
        -   \"PPM \*.ppm\"
        -   \"TIF \*.tif\"
        -   \"TIFF \*.tiff\"
        -   \"XBM \*.xbm\"
        -   \"XPM \*.xpm\"

-   Line 1 : nombre d\'images calculées avec l\'angle donné (ex : angle 60 degrés = 360 (rotation complete) / 60 (angle) = 6 images

-   Line 2 : définition de l\'écran utilisé

-   Background image :
    -   Actual : sauve l\'image avec écran et couleurs actuels
    -   White : sauve l\'image avec écran fond blanc
    -   Black : sauve l\'image avec écran fond noir

-    **[<img src=images/FCCamera_00.png style="width:24px"> Launch**: ouvrir la fenêtre du fichier, donner le nom et le chemin d\'accès.

-    **[<img src=images/FCCamera_07.png style="width:24px"> Reset**: réinitialiser la valeur par défaut

-    **[<img src=images/FCCamera_00.png style="width:24px"> Return**: quitter le panneau photo et revenir au panneau FCCamera






## Liens

Liens en rapport avec FCCamera

-   [Macro Rotate View](Macro_Rotate_View/fr.md),
-   [Macro Align Object to View](Macro_Align_Object_to_View/fr.md),
-   [Macro Align Face Object to View](Macro_Align_Face_Object_to_View/fr.md),
-   [Macro WorkFeatures](Macro_WorkFeatures/fr.md)

Discussion sur le Forum [MACRO:Work Feature 2014_12](http://forum.freecadweb.org/viewtopic.php?f=22&t=9056)

## Script

Téléchargez le paquet d\'icons [FCCamera_Icones.zip](https://forum.freecadweb.org/download/file.php?id=79288)

Téléchargez la macro sur Gist [**Macro FCCamera.FCMacro**](https://gist.github.com/mario52a/4aa545c23b323cf68824)



## Exemples



### Comment créer un forage dans un angle défini 


<center>

<File:FCCamera> 09.png\|Créez votre objet <File:FCCamera> 10.png\|Créez votre cylindre et positionnez le ainsi.
Donnez votre axe, angle et cliquez sur le bouton <img alt="" src=images/FCCamera_01.png  style="width:24px;"> 
**Accept the rotation**


</center>


<center>

<File:FCCamera> 11.png\|Sélectionnez le cylindre qui servira de forage <File:FCCamera> 12.png\|Dans FCCamera, cliquez sur le bouton <img alt="" src=images/FCCamera_05.png  style="width:24px;"> 
**Align Object to View**


</center>


<center>

<File:FCCamera> 13.png\|Le cylindre se déplace de 15 degrés (il prend la position de la caméra). Effectuez votre opération booléenne. <File:FCCamera> 14.png\|Votre perçage est à 15 degrés


</center>

Le même résultat peut être obtenu en créant un plan dans le coin donné par la position du clic de la souris et une esquisse.


<center>

<File:Macro_FCCamera_Align_To_Face.gif%7CExemple> du positionnement d\'un ressort sur un axe d\'une face


</center>


<center>

<File:Test_FCCamera_Photo_01.gif%7CExemple> d\'utilisation de la section photo rotation avec sauvegarde des fichiers images (vous pouvez créer un Gif animé avec [GIMP](https://www.gimp.org/))


</center>



## Versions

-   **ver 0.14 (20/10/2020):** correction du bogue \"Grid\" non accepté

-   **ver 0.13 (28/06/2020):** ajout des images dans le code souece, creation du plan \"On point, Center face, BBox center, Center Mass\", gridLayout

-   **ver 00.12.1 (12/02/2020):** suppression des mauvais caractères lignes 674 et 675 (accent\...) encore

-   **ver 12 (01/08/2019):** compatible Python 3 ( print to print() )

-   **ver 11 (13/01/2018):** mineur

-   **ver 10 (13/01/2018):** ajout \"def centerBoundBoxGlobal():\" pour version 0.17

-   **ver 09 (08/01/2018):** mineur

-   **ver 08 (08/01/2018):** supp \"Pyqt4\" and adjust number image
-   **ver 07 (03/01/2018):** ajout du panneau photo et de la rotation sur un axe de direction aléatoire sélectionné (wire, edge, line )

-   **ver 0.6 (13/12/2016):** nouveau système de recherche du chemin des macros directement dans les préférences.

#path = FreeCAD.ConfigGet("AppHomePath")
#path = FreeCAD.ConfigGet("UserAppData")
#path = "your path"
param = FreeCAD.ParamGet("User parameter:BaseApp/Preferences/Macro")# macro path
path = param.GetString("MacroPath","") + "/"                        # macro path
path = path.replace("\\","/")
App.Console.PrintMessage("Path locality to FCCamera.....images.png [ " + path + " ]"+"\n")

-   **ver 0.5 06/09/2016:** correction du nom \"FCCamera_Axis_rotation_X.png\" dans le bloc reset

-   **ver 0.4 28/02/2016 :** affichage de tous les renseignements de la caméra et calcul de la [Direction](http://forum.freecadweb.org/viewtopic.php?f=13&t=14213#p114667)

-   **ver 0.3 18/03/2015 :** modié line 492 remplacé \"**pl.Base = App.Vector(0,0,0)**\" par \"**pl.Base = sel\[0\].Placement.Base**\" maintenant ne se déplace plus la forme au point (0,0,0) mais à partir des coordonnées d\'origine

-   **ver 0.2 25/02/2015 :** correction des noms des fichiers (Linux est sensible à la casse) merci microelly2



---
![](images/Button_right.svg) [documentation index](../README.md) > Macro FCCamera/fr
