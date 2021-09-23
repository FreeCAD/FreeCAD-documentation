# Macro Screen Wiki/fr
{{Macro/fr
|Name=Macro Screen Wiki
|Icon=Macro_Screen_Wiki.png
|Description=Macro spéciale pour le Wiki passionné. Cette macro permet d'enregistrer la vue 3D au format souhaité. La vue 3D ou la fenêtre 3D complète de FreeCAD prend les dimensions souhaitées. Une rotation de l'objet sélectionné ou de la vue 3D est possible pour donner un angle de rotation le nombre d'images est calculé automatiquement il est possible de donner un angle de départ et un angle d'arrivée. Vous devez utiliser un autre programme d'exemple Gimp pour assembler les images et créer le fichier animé.
|Author=Mario52
|Version=00.05
|Date=2021/05/21
|FCVersion=0.19
|Download=Téléchargez [https://wiki.freecadweb.org/images/f/f5/Macro_Screen_Wiki.png Macro_Screen_Wiki.png] et copiez la dans la même répertoire que la macro
|SeeAlso= <img src="images/Macro_Copy3DViewToClipboard.png" width=24px>[Macro_Copy3DViewToClipboard](Macro_Copy3DViewToClipboard.md)<br/><img src="images/Snip.png" width=24px> [Macro_Snip](Macro_Snip.md)
}}

## Description

Macro spéciale pour le Wiki passionné. Cette macro permet d\'enregistrer la [vue 3D](3D_view/fr.md) au format souhaité. La vue 3D ou la fenêtre 3D complète de FreeCAD prend les dimensions souhaitées. Une rotation de l\'objet sélectionné ou de la vue 3D est possible pour donner un angle de rotation le nombre d\'images est calculé automatiquement il est possible de donner un angle de départ et un angle d\'arrivée. Vous devez utiliser un autre programme d\'exemple Gimp pour assembler les images et créer le fichier animé.


{{Codeextralink|https://gist.githubusercontent.com/mario52a/61571ce0bd41af0471995df7c3ea855f/raw/4fdc5b2db7ed3ed062a2575637e035f728b2e40d/Macro_Screen_Wiki.FCMacro}}

![](images/Macro_Screen_Wiki_00.png )


*Macro Screen Wiki Image et configuration de la fenêtre*

![](images/Macro_Screen_Wiki_01.png )


*Macro Screen Wiki Rotation window*

## Utilisation

### Images options 

#### Definition

1.  
    {{RadioButton|400x200}}
    

2.  
    {{RadioButton|TRUE|600x400}}(Default)

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
    {{SpinBox|600 px}}Longueur (Default: 600 px)

2.  
    {{SpinBox|400 px}}Hauteur (Default: 400 px)

#### Window

1.  
    {{RadioButton|Window FC}}: La fenêtre complète de FreeCAD

2.  
    {{RadioButton|TRUE|Screen 3D}}: La vue 3D de FreeCAD

#### BackGround Color 

1.  
    {{RadioButton|TRUE|Current}}(Default)

2.  
    {{RadioButton|Color}}
    

3.  
    {{RadioButton|Transparent}}
    

4.  
    **Restore**
    

#### Command

1.  
    **Set Screen**: Fenêtre Docked

2.  
    **Tile Screen**: Fenêtre volante

3.  
    **Save Image**: Sauve l\'image ex: {{FileName|imageBox_000.png}} (le \_000 toujours ajouté

4.  
    **Follow**: Après avoir enregistré la première image, appuyez sur ce bouton si vous souhaitez enregistrer l\'image suivante avec le même nom. Les images enregistrées sont incrémentées ex: {{FileName|imageBox_001.png}}, {{FileName|imageBox_002.png}}, {{FileName|imageBox_003.png}}, etc ..

5.  
    **New image**: Sauve une nouvelle image sans modifier le compteur

6.  
    **Rotation**: Accède au menu rotation (le titre de la section change de \"Image options\" en \"Rotation options\"

7.  
    **Quit**: \_\_\_Screen\_Wiki end\_\_\_\_\_\_\_\_\_\_

8.  
    **ToolBar**: Réduit la fenêtre image en une barre D\'Outils, le bouton **Rotation** n\'est pas disponible dans ce mode.

    1.  ![](images/Macro_Screen_Wiki_ToolBar_01.png )![](images/Macro_Screen_Wiki_ToolBar_02.png )![](images/Macro_Screen_Wiki_ToolBar_03.png )![](images/Macro_Screen_Wiki_ToolBar_04.png )
    2.  The button **[[Image:Macro_Screen_Wiki_ToolBar_04_6.png]]** Flip/Flop Y/N la mini Barre d\'outils ![](images/Macro_Screen_Wiki_ToolBar_Mini.png )

### Rotation options 

#### Rotation on 

1.  
    {{RadioButton|3D View}}w : Rotation de la vue 3D complète

2.  
    {{RadioButton|TRUE|Object}}: Seul l\'objet sélectionné est pivotée

#### Axis

:   
    {{RadioButton|TRUE| {{ColoredText||red|'''X'''}}}}: Rotation sur l\'axe X

:   
    {{RadioButton| {{ColoredText||Green|'''Y'''}}}}: Rotation sur l\'axe Y

:   
    {{RadioButton| {{ColoredText||Blue|'''Z'''}}}}Rotation sur l\'axe Z

:   
    {{RadioButton| {{ColoredText||#995500|'''D'''}}}}: Rotation sur une Direction.

    :\* Pour utilisez cette option, sélectionnez d\'abord l\'objet, ensuite: la ligne guide. Si {{RadioButton|TRUE|{{ColoredText||#995500|'''D'''}}}} est coché et qu\'aucun fil n\'est sélectionné, la direction est `Vector(0, 0, 0)`

#### Point Rotation BoundBox 

1.  Object: Rotation sur le centre BoundBox de l\'objet sélectionné
2.  Sub Object: Rotation sur le centre BoundBox du sous-objet sélectionné

#### Angles

-   Angle Rotation

1.  
    **-**: Diminue la valeur de 10 degrés

2.  
    {{SpinBox|0 Degrees}}: Value

3.  
    **+**: Augmentez la valeur de 10 degrés

-   Number images : L\'image numérique enregistrée avec les valeurs données est calculée (approximation + 1)
-   Angle Begin Rotation

1.  
    **-**: Diminue la valeur de 10 degrés

2.  
    {{SpinBox|0 Degrees}}: Value : Angle de début de rotation

3.  
    **+**: Augmentez la valeur de 10 degrés

-   Degrees Angle End Rotation

1.  
    **-**: Diminue la valeur de 10 degrés

2.  
    {{SpinBox|360 Degrees}}: Value : Angle de rotation de fin

3.  
    **+**: Augmentez la valeur de 10 degrés

#### Command 

-   Delay between 2 images

1.  
    {{SpinBox|0,00 Delay second}}: Délais entre deux images. Si vous avez un problème pour sauvegarder l\'image (ordinateur trop rapide) donnez une valeur \...

2.  
    {{CheckBox|Reverse}}: Checked, cette option inverse la vue de rotation 3D ou l\'objet

3.  
    {{CheckBox|TRUE|Original position}}: Cette option rétablit la position d\'origine de la vue 3D ou de l\'objet pivoté. Sinon, la vue 3D ou l\'objet restent dans la dernière position de la rotation

4.  
    **Save the animation**: Enregistrez l\'animation

## Exemples

![](images/Macro_Screen_Wiki_03_Set_Screen.png )


*Mode Set Ecran 640 px x 400 px*

![](images/Macro_Screen_Wiki_04_Tile_Screen.png )


*Mode Tile Screen 640 px x 400 px par ex: déplacez la fenêtre. L'image est enregistrée dans le même mode Définir l'écran ci-dessus*

![](images/Macro_Screen_Wiki_Object_Direction_Object.gif )


*Mode d'animation Objet sélectionné et direction BoundBox center Objet. <br/> Les images doivent être assemblées avec un autre programme pour créer un Gif animé <br/> Exemple [https://daviesmediadesign.com/project/make-animated-gif-gimp/ GIMP] ou [https://www.screentogif.com ScreenToGif]*

![](images/Macro_Screen_Wiki_Object_Direction_SUBObject.gif )


**Sous-objet Direction de l’objet d’animation sélectionné. <br/> Les images doivent être assemblées avec un autre programme pour créer un Gif animated<br/>Example [https://daviesmediadesign.com/project/make-animated-gif-gimp/ GIMP] ou [https://www.screentogif.com ScreenToGif]**

![](images/Macro_Screen_Wiki_07.png )


*La fenêtre FreeCAD a été redimensionnée. La dimension peut être différente de la définition (dépend du Widget, la barre de titre ... utilisés)*

## Versions

Version=00.05: 2021/05/21 : ajout du code dans la section Save file à cause de Linux Mint QFileDialog ignore l\'extension. Seul le Path+name est affiché


```python
global switchQFileDialogMint
                ####  mint
                if switchQFileDialogMint == True:   #
                    Filter = Filter[Filter.find("."):Filter.find(")")]
                    SaveName = SaveName + Filter
                ####  mint
```

Version=00.04: 2021/01/13 : ajout d\'un mini ToolBar

Version=0.03: 2020/10/30 : creation d\'une barre d\'outils pour sauver une image sans toucher au compteur

Version=0.02: 2020/05/04 : correction de la couleur du bouton bug (self.PB\_01\_Color obsolete)

Version = 00.01 : 2020/03/21 :

---
[documentation index](../README.md) > Macro Screen Wiki/fr
