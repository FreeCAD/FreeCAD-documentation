# Macro Screen Wiki/fr
{{Macro/fr
|Name=Macro Screen Wiki
|Name/fr=Macro Screen Wiki
|Icon=Macro_Screen_Wiki.png
|Description=Macro spéciale pour l'utilisateur du wiki. Cette macro permet de sauvegarder la vue 3D dans le format souhaité. La vue 3D ou la fenêtre 3D complète de FreeCAD prend les dimensions souhaitées. Une rotation de l'objet sélectionné ou de la vue 3D est possible; pour donner un angle de rotation, le nombre d'images est calculé automatiquement. Il est possible de donner un angle de départ et un angle d'arrivée. Vous devez utiliser un autre programme d'exemple Gimp pour assembler les images et créer le fichier animé.
|Author=Mario52
|Version=00.06b
|Date=2023/06/26
|FCVersion=0.19 et plus
|Download=[https://wiki.freecad.org/images/f/f5/Macro_Screen_Wiki.png Icône de la barre d'outils]
|SeeAlso=[Macro Copy3DViewToClipboard](Macro_Copy3DViewToClipboard/fr.md), [Macro Snip](Macro_Snip/fr.md)
}}

## Description

Cette macro permet à l\'utilisateur de sauvegarder la [vue 3D](3D_view/fr.md) dans le format souhaité. La vue 3D ou la fenêtre 3D complète de FreeCAD prend les dimensions souhaitées. Une rotation de l\'objet sélectionné ou de la vue 3D est possible; pour donner un angle de rotation, le nombre d\'images est calculé automatiquement; il est possible de donner un angle de départ et un angle d\'arrivée. Vous devez utiliser un autre programme d\'exemple Gimp pour assembler les images et créer le fichier animé.


{{Codeextralink|https://gist.githubusercontent.com/mario52a/61571ce0bd41af0471995df7c3ea855f/raw/2e2f5d1f30acd9fee9ea58596d0bcaa8d19f03f3/Macro_Screen_Wiki.FCMacro}}

![](images/Macro_Screen_Wiki_00.png )



*Fenêtre Image et configuration de la Macro Screen Wiki *

![](images/Macro_Screen_Wiki_01.png )



*Fenêtre Rotation de la Macro Screen Wiki*



## Utilisation

### Image options 

#### Definition

1.  
    {{RadioButton|400x200}}
    

2.  
    {{RadioButton|TRUE|600x400}}(Par défaut)

3.  
    {{RadioButton|1024x768}}
    

4.  
    {{RadioButton|320x240 (QVGA)}}
    

5.  
    {{RadioButton|320x480 (HVGA)}}
    

6.  
    {{RadioButton|400x300}}
    

7.  
    {{RadioButton|480x360}}
    

8.  
    {{RadioButton|640x480 (VGA)}}
    

9.  
    {{RadioButton|768x576 (PAL)}}
    

10. 
    {{RadioButton|800x600 (SVGA)}}
    

11. 
    {{RadioButton|960x720}}
    

12. 
    {{RadioButton|1024x768 (XGA)}}
    

#### Format image 

1.  
    {{SpinBox|600 px}}Longueur (Par défaut : 600 px)

2.  
    {{SpinBox|400 px}}Hauteur (Par défaut : 400 px)

#### Window

1.  
    {{RadioButton|Window FC}}: la fenêtre complète de FreeCAD

2.  
    {{RadioButton|TRUE|Screen 3D}}: la vue 3D de FreeCAD

#### BackGround Color 

1.  
    {{RadioButton|TRUE|Current}}(Par défaut)

2.  
    {{RadioButton|Color}}
    

3.  
    {{RadioButton|Transparent}}
    

4.  
    **Restore**
    

#### Command

1.  
    **Set Screen**: fenêtre ancrée

2.  
    **Tile Screen**: fenêtre volante

3.  
    **Save Image**: enregistre l\'image, par ex : **imageBox_000.png** (le \_000 est incrémenté à chaque nouvelle image)

4.  
    **Follow**: après avoir enregistré la première image, appuyez sur ce bouton pour enregistrer l\'image suivante avec le même nom. Les images sauvegardées sont incrémentées, par ex : **imageBox_001.png**, **imageBox_002.png**, **imageBox_003.png**, ![](images/Macro_Screen_Wiki_ToolBar_04_4b.png ) etc\...

5.  
    **New image**: enregistre une nouvelle image sans modifier le compteur

6.  
    **Rotation**: accès au menu de rotation (le titre de la section \"Image options\" en \"Rotation options\").

7.  
    **Quit**: \_\_\_Screen_Wiki end\_\_\_\_\_\_\_\_\_\_

8.  
    **ToolBar**: réduit la fenêtre d\'image dans une barre d\'outils, l\'option **Rotation** n\'est pas disponible dans ce mode.

    1.  ![](images/Macro_Screen_Wiki_ToolBar_01.png )![](images/Macro_Screen_Wiki_ToolBar_02.png )![](images/Macro_Screen_Wiki_ToolBar_03.png )![](images/Macro_Screen_Wiki_ToolBar_04.png )
    2.  Le bouton **[[Image:Macro_Screen_Wiki_ToolBar_04_6.png]]** Flip/Flop Y/N la mini barre d\'outils ![](images/Macro_Screen_Wiki_ToolBar_Mini.png )

### Rotation options 

#### Rotation on 

1.  
    {{RadioButton|3D View}}: la vue complète est pivotée

2.  
    {{RadioButton|TRUE|Object}}: l\'objet sélectionné subit une rotation

#### Axis

:   
    {{RadioButton|TRUE| {{ColoredText||red|'''X'''}}}}: rotation sur l\'axe X

:   
    {{RadioButton| {{ColoredText||Green|'''Y'''}}}}: rotation sur l\'axe Y

:   
    {{RadioButton| {{ColoredText||Blue|'''Z'''}}}}: rotation sur l\'axe Z

:   
    {{RadioButton| {{ColoredText||#995500|'''D'''}}}}: rotation sur la direction.

      - Pour utiliser cette option : sélectionnez d\'abord l\'objet, puis ensuite la ligne de référence. Si {{RadioButton|TRUE|{{ColoredText||#995500|'''D'''}}}} est coché et qu\'aucune ligne n\'est sélectionnée, la direction est `Vector(0, 0, 0)`

#### Point Rotation BoundBox 

1.  Object : rotation sur le centre de la boîte de délimitation de l\'objet sélectionné
2.  Sub Object : rotation sur le centre de la boîte de délimitation du sous-objet sélectionné

#### Angles

-   Angle Rotation

1.  
    **-**: diminue la valeur de 10 degrés

2.  
    {{SpinBox|0 Degrees}}: Valeur

3.  
    **+**: augmente la valeur de 10 degrés

-   Number images

1.  
    **-**: diminue la valeur de 10 images

2.  
    {{SpinBox|0 Images (+1)}}: Value

3.  
    **+**: augmente la valeur de 10 images

-   Angle Begin Rotation

1.  
    **-**: diminue la valeur de 10 degrés

2.  
    {{SpinBox|0 Degrees}}: Valeur : Angle de la rotation de départ

3.  
    **+**: augmente la valeur de 10 degrés

-   Degrees Angle End Rotation

1.  
    **-**: diminue la valeur de 10 degrés

2.  
    {{SpinBox|360 Degrees}}: Valeur : Angle de la rotation finale

3.  
    **+**: augmente la valeur de 10 degrés

#### Command 

-   Delay between 2 images

1.  
    {{SpinBox|0,00 Delay second}}: s\'il y a un problème d\'enregistrement des images à cause de la vitesse, alors ajoutez un délai de X secondes.

2.  
    {{CheckBox|Reverse}}: cochée, cette option inverse la rotation de la vue 3D ou de l\'objet.

3.  
    **Point center**: visualise point de rotation, si le point est visible il est inclus dans l\'image sauvée (PS: the point can be hidden by an object)

4.  
    {{CheckBox|TRUE|Original position}}: cette option rétablit la position originale de la vue 3D ou de l\'objet ayant subi une rotation. Au lieu que la vue 3D ou l\'objet reste dans la dernière position de la rotation.

5.  
    **Test Rot.**: teste la rotation sans sauver d\'images

6.  
    **Save the animation**: enregistre l\'animation



## Exemples

![](images/Macro_Screen_Wiki_03_Set_Screen.png )



*Écran capturé avec des dimensions de `640px x 400px*`

![](images/Macro_Screen_Wiki_04_Tile_Screen.png )



*Mêmes dimensions que l'image précédente, celle-ci est capturée en mode<br/>"Tuile d'écran"*

![](images/Macro_Screen_Wiki_Object_Direction_Object.gif )



*Mode d'animation : objet sélectionné et direction de la boîte de délimitation<br/>centre de l'objet. Les images doivent être assemblées avec une application<br/>tierce pour créer un .gif animé comme [https://daviesmediadesign.com/project/make-animated-gif-gimp/ GIMP] ou [https://www.screentogif.com ScreenToGif]*

![](images/Macro_Screen_Wiki_Object_Direction_SUBObject.gif )


**Mode d'animation : direction de l'objet sous-objet sélectionné.<br/>
Les images doivent être assemblées à l'aide d'une application tierce qui crée <br/>un .gif animé, comme [https://daviesmediadesign.com/project/make-animated-gif-gimp/ GIMP] ou [https://www.screentogif.com ScreenToGif]**

.

![](images/Macro_Screen_Wiki_07.png )



*La fenêtre de FreeCAD a été redimensionnée. La dimension peut être différente de la<br/>définition (selon le widget, la barre de titre etc... utilisés.)*

## Versions

Version=00.06: Version=00.06b: 2023/06/26 : sélectionner le nombre d\'images voulue, bouton pour visualiser la rotation sans sauvegarde, bouton visualiser le point de rotation, ajout du code de wmayer pour rotation au centre de l\'écran:


```python
                #https://forum.freecadweb.org/viewtopic.php?f=22&t=10157
                cam = Gui.ActiveDocument.ActiveView.getCameraNode()
                position = cam.position.getValue()
                orient = cam.orientation.getValue()
                focalDistance = cam.focalDistance.getValue()
                viewdir = coin.SbVec3f(0, 0, -1)
                viewdir = orient.multVec(viewdir)
                pointRotation = position + viewdir * focalDistance
                pointRotation = pointRotation2 = App.Vector(pointRotation.getValue()[0], pointRotation.getValue()[1], pointRotation.getValue()[2])

```

Version=00.05 : 2021/05/21 : ajout de code dans la section du fichier Save pour Linux Mint, QFileDialog ignore l\'extension. Seul le chemin+nom est affiché


```python
global switchQFileDialogMint
                ####  mint
                if switchQFileDialogMint == True:   #
                    Filter = Filter[Filter.find("."):Filter.find(")")]
                    SaveName = SaveName + Filter
                ####  mint
```

Version=00.04 : 2021/01/13 : ajout d\'une mini barre d\'outils

Version=0.03 : 2020/10/30 : création d\'une barre d\'outils pour l\'image et un nouveau bouton pour l\'image unique

Version=0.02 : 2020/05/04 : correction de la couleur du bouton bug (self.PB_01_Color obsolete)

Version=0.01 : 2020/03/21



---
⏵ [documentation index](../README.md) > Macro Screen Wiki/fr
