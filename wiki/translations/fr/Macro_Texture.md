# Macro Texture/fr
{{Macro/fr
|Name=Macro Texture
|Icon=FCTexture.png
|Description=Créer une image 3D à partir d'une image BMP 8 bits (256 couleurs).<br/>En d'autres termes, elle permet de construire très facilement un projet 3D à partir d'une image bitmap utilisant les niveaux de gris (256 nuances de gris).<br/>Si une image BMP 32 bits est sélectionnée, l'image est représentée en points.<br/>La macro '''FCCreaLoft Macro Loft''' est utilisée pour automatiser l'opération de multi lissage.
|Author=Mario52
|Version=0.14c
|Date=2021/01/16
|FCVersion=0.18 et ultérieur
|Download=_
|SeeAlso=_ [Macro Loft](Macro_Loft/fr.md)
}}

## Description


<div class="mw-translate-fuzzy">

## Description 

Cette petite macro permet de construire très facilement un projet 3D à partir d\'une image bitmap avec 256 nuances de gris.


</div>

J\'espère que cette macro va changer notre façon de penser lors de la modélisation avec la CAO et la conversion CNC en objets 3D avec peu ou pas d\'intervention.

Tout devient possible quelle que soit la complexité de l\'image!

La macro <img alt="FCCreaLoft" src=images/FCCreaLoft.png  style="width:32px;"> [Macro Loft](Macro_Loft/fr.md) est utilisé pour automatiser les opérations de multi lissage.


{{Codeextralink|https://gist.githubusercontent.com/mario52a/262317bc7d8555885b0e/raw/3ec2ab127d8ad01a6b657aa5df9a6127ff07c7c0/Macro%2520FCTexture.FCMacro}}

<img alt="" src=images/Texture_004_Honda.png  style="width:480px;">


<div class="mw-translate-fuzzy">

<img alt="Texture 004 Honda" src=images/Texture_004_Honda.png  style="width:480px;"> 
*Texture 004 Honda*


</div>

## Usage


<div class="mw-translate-fuzzy">

## Utilisation

Cette macro nécessite une image en 256 nuances de gris (0-255). Par conséquent, avant d\'exécuter la macro, convertissez votre image en niveaux de gris (noir et blanc). Lors de l\'exécution de la macro, le nombre de couleurs est détecté automatiquement. Note : si l\'image a plus de 256 couleurs, une autre fonction est attendue (WIP). Chaque couleur (niveau de gris) est considérée comme une profondeur, le blanc (255) le niveau haut et le noir (0) le niveau le plus bas (profond).


</div>

La configuration se fait avant l\'ouverture du fichier, les valeurs par défaut sont les réglages prévu pour obtenir un projet de dimensions :

-   largeur de l\'image en points dans la coordonnée **X**,
-   hauteur de l\'image en points dans la coordonnée **Y**,
-   profondeur ou épaisseur du projet filtré sur 10 mm (en mode Brut, sur 256 mm) dans la coordonnée **Z**.

Le fichier image se déroule à la manière d\'un scanner x1 x2 x3 \.... par incrément de 1 mm dans FreeCAD de même pour la valeur y de 1 mm à la fois. La valeur de z est donnée par la valeur de la couleur. Ces valeurs sont paramétrables dans la macro.

Remarque importante : selon la taille de l\'image, le projet peut devenir très volumineux! Par exemple, une simple image de (100px x 100px) largeur/hauteur sera : **100 x 100 = 10000 points**. Chacun des 10 000 points correspond à une coordonnée, ce qui signifie donc 10000 coordonnées X, 10000 Y et 10000 Z dans la réalité.

### Interface


<div class="mw-translate-fuzzy">

<img alt="Texture 002" src=images/Texture_002.png  style="width:300px;">


</div>

#### Coordinates


<div class="mw-translate-fuzzy">

#### Coordonnées

-    **Coordinate X <img src="images/Std_CoordinateSystem.svg" width=24px>**{{SpinBox|0,00 mm}} : La position des coordonnées **X** de l\'objet (par défaut: 0).

-    **Coordinate Y <img src="images/Std_CoordinateSystem.svg" width=24px>**{{SpinBox|0,00 mm}} : La position de la coordonnée **Y** de l\'objet (par défaut: 0).

-    **Coordinate Z <img src="images/Std_CoordinateSystem.svg" width=24px>**{{SpinBox|0,00 mm}} : La position de la coordonnée **Z** de l\'objet (par défaut: 0).


</div>

#### Stretching


<div class="mw-translate-fuzzy">

#### Étirement

-    **Stretching X**{{SpinBox|0,00 mm}} : rétrécissement ou agrandissement du **X** (longueur) de l\'objet (par défaut : 0)

-    **Stretching Y**{{SpinBox|0,00 mm}} : rétrécissement ou agrandissement du **Y** (hauteur) de l\'objet (par défaut : 0)

-    **Stretching Z**{{SpinBox|0,00 mm}} : rétrécissement ou agrandissement du **Z** (profondeur) de l\'objet (par défaut : 0).


</div>

#### Inversion


<div class="mw-translate-fuzzy">

#### Inversion 

-    {{CheckBox|Axis X}}: inverse les coordonnées *X* de l\'image.

-    {{CheckBox|Axis Y}}: inverse les coordonnées *Y* de l\'image.

-    {{CheckBox|Axis Z}}: inverse les coordonnées *Z* de l\'image.


</div>

#### 8 bit Mode 


<div class="mw-translate-fuzzy">

#### Mode 8 Bits 

La valeur de début de l\'opération s\'adapte automatiquement à la fonction choisie : 0 si le réglage est sur noir (**Black**) ou sur 255 si le réglage est sur blanc (**White**) ou 19 si le réglage est sur noir (**Black**)


</div>

-    {{RadioButton|TRUE|<img src="images/Draft_Wire.svg" width=24px> Wire}}: Construit la ligne (les vecteurs) sous forme de Wire.

-    {{RadioButton|<img src="images/Draft_BSpline.svg" width=24px> Bspline}}: Construit la ligne (les vecteurs) sous forme de Bspline.

-    {{RadioButton|<img src="images/Workbench_Points.svg" width=24px> Cloud}}: Construire les vecteurs de points dans un nuage de points.

-    {{RadioButton|<img src="images/Draft_Point.svg" width=24px> Point}}: Crée un point à chaque pixel (vecteur) (Note : cette procédure est gourmande en ressources CPU)

-    {{CheckBox|Nuance}}: Si l\'option ombre est cochée, la couleur du point est représentée sous forme d\'image.

#### 32 bit Mode 


<div class="mw-translate-fuzzy">

#### Mode 32 Bits 

-    {{RadioButton|TRUE|Photo}}: le mode photo est automatiquement activé lorsqu\'une **image 32 bits** est détectée. (Note : cette procédure est gourmande en ressources CPU)

-    {{RadioButton|Plan}}: permet d\'importer une **image 32 bits** et d\'ignorer le fond du plan. Par défaut le fond de plan est noir à ignorer les couleurs sont ajustables avec la commande **Capping**. Si Blanc est coché, le fond a ignorer sera blanc. (Note : cette procédure est gourmande en ressources CPU)


</div>

#### File


<div class="mw-translate-fuzzy">

#### Fichier

-    {{CheckBox|.pcd}}: si coché, un fichier (originalName.bmp.pcd) est enregistré dans le même répertoire que le fichier (pcd v0.7).

-    {{CheckBox|.asc}}: si coché, un fichier (originalName.bmp.asc) est enregistré dans le même répertoire que le fichier. Ce fichier peut être utilisé comme un nuage de points (format : X Y Z).


</div>

#### Capping (10mm) 


<div class="mw-translate-fuzzy">

#### Ecrêtement (10 mm) 

-   Slider : Entrez la hauteur du formulaire. La hauteur est affichée sur le cadre du titre.

-    {{SpinBox|0 height}}: Entrez la hauteur du formulaire. La hauteur est affichée dans le cadre titre.

-   Mode brut {{CheckBox|20}} : Permet de régler le nombre de couleurs (profondeur). Le mode par défaut est de 0-20 (ce qui constitue un filtre et permet d\'obtenir plus de détails selon la complexité de l\'image) ; une fois coché, le mode est de 0 à 255 (toute la gamme des couleurs).

-    {{CheckBox}}: cette option permet d\'accéder à la fenêtre de saisie des contours

-    {{SpinBox|0/2 Contour}}: cette fenêtre de saisie donne la ligne de contour. ne pas utiliser (ex : 0 pour la base).

-   Capping {{CheckBox|White}} : cette fonction peut être réalisée sur le choix des couleurs, blanc (par défaut) ou noir. Les degrés de la règle de plafonnement 20 à 0 (ou 255 à 0) si la case est cochée sur **W** (non cochée) ou 0 à 20 (ou 0 à 255) si la case est cochée sur **B**. (non coché) ou 0 à 20 (ou 0 à 255) si la case est cochée sur **B**. (cochée).

-    {{SpinBox|20 Capping}}: cette fenêtre de saisie donne les degrés d\'ecrêtement.


</div>

#### Command


<div class="mw-translate-fuzzy">

#### Commande

-    **File and launch**: Ouvre le fichier image et lance la conversion.

-    **Help**:

    -   Pour modifier le paramètre disponible: allez dans **Outils → Editeur de paramètres\...**
    -   \_\_L\'étape globale de la fenêtre de saisie:\_\_
    -   Paramètre utilisateur: **BaseApp/Preferences/Macros/FCMmacros/FCTexture → SingleStep**
    -   Ajustez la valeur souhaitée (1.0 par défaut)
    -   \_\_Pour la recherche si la macro est mise à jour:\_\_
    -   Paramètre utilisateur: **BaseApp/Preferences/Macros/FCMmacros/FCTexture → switchVesionMacroSearch**
    -   Réglez switchVesionMacroSearch sur `True` (`False` par défaut)


</div>

-    **Quit**: sort de la fonction.

## Script

Les icônes .png <img alt="" src=images/FCTexture.png  style="width:64px;"> et .svg<img alt="" src=images/FCTexture.svg  style="width:64px;">

**Macro\_Texture.FCMacro**

Téléchargez la macro sur Gist [Macro FCTexture.FCMacro](https://gist.github.com/mario52a/262317bc7d8555885b0e)

## Exemples

Les images ont été inclinées pour accentuer l\'effet 3D.


<center>

<File:FCTexture_008.png%7CHonda>


</center>



<center>

<File:Macro_FCTexture_008b.png%7CUn> exemple de réalisation avec l\'option contour


</center>


<center>

<File:Texture> Nano Photo.png\|Ici un exemple d\'une image .bmp convertie en points et restaure l\'image dans FreeCAD. La largeur de l\'image est de 6.5 nm
[Merci à Yorik pour avoir donné son autorisation pour l\'utilisation de son logo](http://forum.freecadweb.org/viewtopic.php?f=24&t=5893#p47075) Image:Texture NanoDesign.png\|Ici un exemple d\'une image bmp convertie en objet 3D de 6.7 nm de large.
[Merci à Yorik pour avoir donné son autorisation pour l\'utilisation de son logo](http://forum.freecadweb.org/viewtopic.php?f=24&t=5893#p47075)


</center>



<center>

Image:Texture 001 Logo.png\|Le logo de FreCAD. Image:Texture 002 Fe FC.png\|Une partie du fond décran de FreeCAD (Le [fichier](http://forum.freecadweb.org/viewtopic.php?f=3&t=4708&start=10#p46353) sur le forum).


</center>



<center>

Image:Texture\_003\_napperon.png\|Une portion d\'une nappe de table. Image:Texture\_005\_larme.png\|Une tôle larmée.


</center>



<center>

<File:FCTexture> 006.png\|Mode Plan: Dans l\'image de gauche le fond blanc a été ignoré et toutes les autres couleurs sont affichées, dans l\'image de droite la couleur noire a été ignorée et toutes les autres couleurs sont affichées (le niveau peut être modifié avec l\'option \"Capping\")(un [exemple](http://forum.freecadweb.org/viewtopic.php?f=3&t=6123&hilit=teobo&start=10#p49024) sur le forum).


</center>



<center>

<File:Texture> Topographie.png\|Exemple avec une image représentant la topographie d\'un terril chaque gradin correspond à un degrés de couleur différent.


</center>



<center>

<File:FCTexture_007_FreeCAD_ASCII_00.png%7CExemple> d\'image convertie en caractères ASCII (pas encore implémenté).


</center>



<center>

[File:FCTexture\_Example.gif\|Procédure](File:FCTexture_Example.gif%7CProcédure) pour créer un solide:
**1:** Créer les lofts avec l\'outil <img alt="" src=images/Part_RuledSurface.svg  style="width:24px;">ou avec la <img alt="FCCreaLoft" src=images/FCCreaLoft.png  style="width:32px;"> [Macro Loft](Macro_Loft/fr.md)
**2:** Sélectionnez l\'ensemble et faites une opération d\'extrusion avec l\'outil <img alt="" src=images/Part_Extrude.svg  style="width:24px;">
**3A:** Pour Linux téléchargez _
**3B:** Pour Windows téléchargez [GmshMesh2.zip](http://forum.freecadweb.org/download/file.php?id=15220) dézippez le fichier et installez le dans votre répertoire Mod (author ulrich1a)
**4:** Créez votre objet Mesh et utilisez le.


</center>



<center>

<File:FCTexture> Example Mesh.png\|Votre objet converti en objet mesh avec [GmshMesh.](Macro_GMSH.md)


</center>


## Links


<div class="mw-translate-fuzzy">

## Liens

La discussion sur [le forum](http://forum.freecadweb.org/viewtopic.php?f=24&t=5893) pour donner vos impressions.


</div>


<div class="mw-translate-fuzzy">

La macro <img alt="FCCreaLoft" src=images/FCCreaLoft.png  style="width:32px;"> [Macro Loft](Macro_Loft/fr.md) pour automatiser le multi loft.


</div>

[apply hair cell texture](http://forum.freecadweb.org/viewtopic.php?f=3&t=4708&start=10#p46353)

[How to handle pdf import properly and feasibly?](http://forum.freecadweb.org/viewtopic.php?f=3&t=6123&hilit=teobo&start=10#p49024)

## Revision

-   Ver 0.14c : 15-01-2021 inclusion de **Gui.SendMsgToActiveView(\"ViewFit\")**

-   Ver 0.14b : 15-01-2021 Creation de Tab Coordinate et Tab Stretching pour diminuer la hauteur pour écrans 15\"

-   ver 0.14 : 06/01/2021 modifie la procédure de chemin de recherche et ajoute une option de préférence: rechercher la nouvelle macro mise à jour


```python
                ####new2
                pathFile      = os.path.dirname(SaveName) + "/"  #= C:/Provisoire400/
                formatFichier = os.path.splitext(SaveName)[1]    #= .png
                SaveName      = os.path.splitext(SaveName)[0]    #= /home/kubuntu/.FreeCAD/Macro/Texture_007_H #= C:/Provisoire400/image3D
                SaveNameformatFichier = SaveName + formatFichier #= C:/Provisoire400/image3D.png
                ####new2
                FreeCAD.ParamGet("User parameter:BaseApp/Preferences/Macros/FCMmacros/FCTexture").SetString("Path",pathFile)
                ####new
```

-   ver 0.13b: 30/12/2020 ajout **time.clock()** et **time.process\_time()** for Python 3xyz\...
-   ver 0.13 : 17/04/2020 Layout et PySide2 Qt5
-   ver 0.12 : 04/08/2019 ajout d\'un bouton pour height
-   ver 0.11 :03/07/2019 adapte à Python 3
-   ver 0.10 : 28/12/2016 ajout sauve les coordonnées des points en .pcd, .asc affichage en mode points cloud, auteur de la forme, contour
-   ver 0.9 : 12/12/2016 ajout d\'une fonction de sauvegarde de fichier ascii .asc pour le point cloud
-   ver 0.8 : 16/03/2016 ajout d\'une progressBar
-   ver 0.7 : 03/09/2014 supprime \"**translate**\" oubliés et correction des erreurs de dysfonctionnement causés par le passage de PyQt vers Pyside !
-   ver 0.6 : 26/08/2014 supprime tous les \"**\_translate**\"
-   ver 0.5 : 25/08/2014 supprime \"**\_translate (\" MainWindow \",**\" Stretching X \"**, None)**\" qui empêchaient l\'affichage des tooltip avec PySide (Windows Vista)

-   ver 0.4 : 08/08/2014 PyQt4 PySide

ver 0.3 : 28/03/2014 :commenté la ligne \"**\# self.checkBox\_5.setAccessibleName(\_fromUtf8(\"\"))**\" qui a causé une erreur d\'exécution à partir de la version FreeCAD : Version: 0.14.3343 (Git), Python version: 2.7.6, Qt version: 4.8.5

---
[documentation index](../README.md) > Macro Texture/fr
