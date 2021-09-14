# Macro FCCamera/fr

 {{Macro/fr
|Name=Macro FCCamera
|Icon=FCCamera_00.png
|Description={{ColoredText|#ff0000|#ffffff|New version GUI modifyed for the HD dpi (QGridLayout) run only FC version 0.18 and more (PySide2 Qt5)}}<br/>For the precedent version see [https://gist.githubusercontent.com/mario52a/4aa545c23b323cf68824/raw/42dc3ef73dc8db463a03b175f5a7f1f6978e3293/Macro%2520FCCamera.FCMacro FCCamera] and install it manually.<br/><br/>
Cette macro peut faire pivoter l'écran selon un angle défini et l'axe défini et crée un plan pour faire face à l'écran afin de créer un formulaire dans les positions du plan spécifiées : la face sélectionnée faisant face à l'écran, pour détecter la position de la caméra, aligner la vue sur la face ou sur l'axe, aligner l'objet à voir.
|Author=Mario52
|Version=0.14
|Date=2020/10/20
|FCVersion=0.18 et plus
|Download=
}}

## Description

Cette macro peut faire pivoter l\'écran dans un angle et axe défini et crée un plan face à l\'écran pour créer un objet dans les positions réglées, positionner la face sélectionnée face à l\'écran, peut détecter la position de la caméra, aligner la vue de la face ou de l\'axe face à l\'écran et de modifier les paramètres (Lacet, Tangage, Roulis) de l\'objet pour l\'aligner dans la position de la camera.


{{Codeextralink|https://gist.githubusercontent.com/mario52a/4aa545c23b323cf68824/raw/98d90ee303e9fa5d6aed6e9f2e36e7ca1a18ca19/Macro%2520FCCamera.FCMacro}}

## Utilisation

![FCCamera](images/Macro_FCCamera_00.png )

**Camera of Axis**: Boîte de dialogue pour entrer les valeurs de rotation en degrés (la rotation se fait sur un angle à la fois).

**Angle de rotation de l\'axe en degrés**: sélectionneé l\'axe de rotation **X, Y,** ou **Z**.

**Axe of rotation**

-   <img alt="" src=images/FCCamera_01.png  style="width:24px;"> **Accept the rotation** : Effectue la rotation dans l\'angle donné.

**Virtual**

-   <img alt="" src=images/FCCamera_02.png  style="width:24px;"> **Detect camera orientation** : Detecte l\'orientation de la camera et affiche les résultats dans la vue rapport. Les valeurs retournées proviennent de la fonction **getCameraOrientation()**.

**Align view to face selected**

-   <img alt="" src=images/FCCamera_03.png  style="width:24px;"> **To Face.** : Aligne la face sélectionnée sur la vue 3D (face à l\'écran). Chaque clic change la vue de l\'objet sélectionné pour **NormalAt** : \"(0,0,1) (0,0,-1) (0,1,0) (0,-1,0) (1,0,0) (-1,0,0)\"

-   <img alt="" src=images/FCCamera_04.png  style="width:24px;"> **To Axis.** : Aligne sur la vue 3D l\'axe de la face sélectionnée (face à l\'écran). Chaque clic change la vue de l\'objet sélectionné pour **Surface Axis** : \"(0,0,1) (0,0,-1) (0,1,0) (0,-1,0) (1,0,0) (-1,0,0)\"

-   <img alt="" src=images/FCCamera_05.png  style="width:24px;"> **Align object to view.** : Aligne l\'objet sélectionné à la vue actuelle. Les valeurs modifiées sont : Rotation Axis((X, Y, Z), Angle) même que Euler angles : Lacet (Yaw), Tangage (Pitch), Roulis (Roll), la translation n\'est pas modifiée.

-   <img alt="" src=images/FCCamera_06.png  style="width:24px;"> **Create plane of view.** : Un plan circulaire est créé face à l\'écran aux coordonnées du clic de souris sur l\'objet. Le rayon du plan circulaire est égal à la plus grande dimension du BoundBox. Si aucun objet n\'est sélectionné le plan est créé aux coordonnées 0, 0, 0 avec un rayon de 20 mm. Le rayon du plan par défaut peut être modifié à la ligne 515:


```python
        rayon = 20                            # Radius of plane
```

-   <img alt="" src=images/FCCamera_07.png  style="width:24px;"> **Reset.** : Reset toutes les valeurs.
-   <img alt="" src=images/FCCamera_08.png  style="width:24px;"> **Quit.** : Quitte FCCamera.

## Section Photo 

![FCCamera](images/Macro_FCCamera_00b.png ) 

-    **ComboBox Actual **: choisissez votre définition d\'écran qui déterminera les dimensions de l\'image

    -   Available (pre-defined):
        -   \"Actual\" (definition actual of screen)
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

-   Line 1 : Nombre d\'images calculées avec l\'angle donné (ex: angle 60 degrés = 360 (rotation complete) / 60 (angle) = 6 images

-   Line 2 : Définition de l\'écran utilisé

-   Background image :
    -   Actual : sauve l\'image avec écran et couleurs actuels
    -   White : sauve l\'image avec écran fond blanc
    -   Black : sauve l\'image avec écran fond noir

-    **<img src=images/FCCamera_00.png style="width:24px"> Launch**: Ouvre un fichier donner le nom et le chemin

-    **<img src=images/FCCamera_07.png style="width:24px"> Reset**: Reset les valeurs par défaut

-    **<img src=images/FCCamera_00.png style="width:24px"> Return**: Quitte la fenêtre de photo et retourne au panneau FCCamera




## Liens

Liens en rapport avec FCCamera et codes originaux ayants servi dans la macro

-   [Macro Rotate View](Macro_Rotate_View/fr.md),
-   [Macro Align Object to View](Macro_Align_Object_to_View/fr.md),
-   [Macro Align Face Object to View](Macro_Align_Face_Object_to_View/fr.md),
-   [Macro WorkFeatures](Macro_WorkFeatures/fr.md)

Discussion sur le Forum [MACRO:Work Feature 2014\_12](http://forum.freecadweb.org/viewtopic.php?f=22&t=9056)

## Script

Téléchargez le paquet d\'icons [FCCamera\_Icones.zip](https://forum.freecadweb.org/download/file.php?id=79288)

Téléchargez la macro sur Gist [**Macro FCCamera.FCMacro**](https://gist.github.com/mario52a/4aa545c23b323cf68824)

## Exemples

### Comment créer un forage dans un angle défini 


<center>

<File:FCCamera> 09.png\|Créez votre objet <File:FCCamera> 10.png\|Créez votre cylindre et positionnez le
Donnez votre axes, angle et cliquez sur le bouton <img alt="" src=images/FCCamera_01.png  style="width:24px;"> 
**Accept the rotation**


</center>


<center>

<File:FCCamera> 11.png\|Sélectionnez le cylindre qui servira de forage <File:FCCamera> 12.png\|dans FCCamera cliquez sur le bouton <img alt="" src=images/FCCamera_05.png  style="width:24px;"> 
**Align Object to View**


</center>


<center>

<File:FCCamera> 13.png\|le cylindre est incliné de 15 degrés (suivant la position de la camera)
faites votre opération booléenne <File:FCCamera> 14.png\|Votre forage effectué à 15 degrés


</center>

Le même résultat peut être obtenu en créant un plan à la position du clic de la souris puis cliquez sur <img alt="" src=images/FCCamera_06.png  style="width:24px;"> **Create plane of view.**.


<center>

<File:Macro_FCCamera_Align_To_Face.gif%7CExemple> de placement d\'un ressort sur une face d\'après son axe


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

-   **ver 0.5 06/09/2016:** correction du nom \"FCCamera\_Axis\_rotation\_X.png\" dans le bloc reset

-   **ver 0.4 28/02/2016 :** affichage de tous les renseignements de la caméra et calcul de la [Direction](http://forum.freecadweb.org/viewtopic.php?f=13&t=14213#p114667)

-   **ver 0.3 18/03/2015 :** modié line 492 remplacé \"**pl.Base = App.Vector(0,0,0)**\" par \"**pl.Base = sel\[0\].Placement.Base**\" maintenant ne se déplace plus la forme au point (0,0,0) mais à partir des coordonnées d\'origine

-   **ver 0.2 25/02/2015 :** correction des noms des fichiers (Linux est sensible à la casse) merci microelly2
