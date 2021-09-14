# Macro Screen Wiki/ru




{{Macro
|Name=Macro Screen Wiki
|Icon=Macro_Screen_Wiki.png
|Description=Special macro for the Wiki Worker. This macro allows to save the 3D view in the desired format. The 3D view or the full 3D window of FreeCAD takes the desired dimensions. A rotation of the selected object or of the 3D view is possible to give a rotation angle the number of images is calculated automatically it is possible to give a departure angle and an arrival angle. You must use another Gimp example program to assemble the images and create the animated file.
|Author=Mario52
|Version=00.05
|Date=2021/05/21
|FCVersion=0.19
|Download=Download the [https://wiki.freecadweb.org/images/f/f5/Macro_Screen_Wiki.png Macro_Screen_Wiki.png] image and paste it in the same directory of the macro
|SeeAlso= <img src="images/Macro_Copy3DViewToClipboard.png" width=24px>[Macro_Copy3DViewToClipboard](Macro_Copy3DViewToClipboard.md)<br/><img src="images/Snip.png" width=24px> [Macro_Snip](Macro_Snip.md)
}}

## Описание

Данный макрос позволяет пользователю сохранить [3D-вид](3D_view/ru.md) в нужном формате. Окно 3D-вида FreeCAD принимает нужные размеры. При повороте выбранного объекта или 3D-изображения можно задать угол поворота. Количество изображений рассчитывается автоматически, можно задать начальный и конечный угол. Для создания анимированного файла вы должны использовать дополнительную программу для сборки изображений например Gimp.


{{Codeextralink|https://gist.githubusercontent.com/mario52a/61571ce0bd41af0471995df7c3ea855f/raw/4fdc5b2db7ed3ed062a2575637e035f728b2e40d/Macro_Screen_Wiki.FCMacro}}

![](images/Macro_Screen_Wiki_00.png )


*Macro Screen Wiki Image and configuration window*

![](images/Macro_Screen_Wiki_01.png )


*Macro Screen Wiki Rotation window*

## Использование

### Настройки изображения 

#### Definition

1.  
    {{RadioButton|400x200}}
    

2.  
    {{RadioButton|TRUE|600x400}}(По умолчанию)

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
    {{SpinBox|600 px}}Length (Default: 600 px)

2.  
    {{SpinBox|400 px}}Height (Default: 400 px)

#### Окно

1.  
    {{RadioButton|Window FC}}: The complete FreeCAD window

2.  
    {{RadioButton|TRUE|Screen 3D}}: The 3D view of FreeCAD

#### Цвет Фона 

1.  
    {{RadioButton|TRUE|Current}}(Default)

2.  
    {{RadioButton|Color}}
    

3.  
    {{RadioButton|Transparent}}
    

4.  
    **Restore**
    

### Команды

1.  
    **Set Screen**: Docked window

2.  
    **Tile Screen**: Fly window

3.  
    **Save Image**: Save the image ex: {{FileName|imageBox_000.png}} (the \_000 is incremented with each new image)

4.  
    **Follow**: After saving the first image, press this button to save the next image with the same name. The images saved is incremented ex: {{FileName|imageBox_001.png}}, {{FileName|imageBox_002.png}}, {{FileName|imageBox_003.png}}, ![](images/Macro_Screen_Wiki_ToolBar_04_4b.png ) etc\...

5.  
    **New Image**: Save one new image without change the counter

6.  
    **Rotation**: Access to the rotation menu (the title of the section \"Image options\" change to \"Rotation options\"

7.  
    **Quit**: \_\_\_Screen\_Wiki end\_\_\_\_\_\_\_\_\_\_

8.  
    **ToolBar**: Reduce the image window in a toolBar, the **Rotation** option is not available in this mode

    1.  ![](images/Macro_Screen_Wiki_ToolBar_01.png )![](images/Macro_Screen_Wiki_ToolBar_02.png )![](images/Macro_Screen_Wiki_ToolBar_03.png )![](images/Macro_Screen_Wiki_ToolBar_04.png )
    2.  The button **[[Image:Macro_Screen_Wiki_ToolBar_04_6.png]]** Flip/Flop Y/N the mini toolBar ![](images/Macro_Screen_Wiki_ToolBar_Mini.png )

### Настройки поворота 

#### Rotation on 

1.  
    {{RadioButton|3D View}}: The complete view is rotated

2.  
    {{RadioButton|TRUE|Object}}: The object selected is rotated

#### Axis

:   
    {{RadioButton|TRUE| {{ColoredText||red|'''X'''}}}}: Rotation on X axis

:   
    {{RadioButton| {{ColoredText||Green|'''Y'''}}}}: Rotation on Y axis

:   
    {{RadioButton| {{ColoredText||Blue|'''Z'''}}}}: Rotation on Z axis

:   
    {{RadioButton| {{ColoredText||#995500|'''D'''}}}}: Rotation on Direction.

    :\* To use this option: select first the object, then afterwards select the wire guideline. If {{RadioButton|TRUE|{{ColoredText||#995500|'''D'''}}}} is checked and no wire is selected the direction is `Vector(0, 0, 0)`

#### Point Rotation BoundBox 

1.  Object: Rotation on the BoundBox center of the object selected
2.  Sub Object: Rotation on the BoundBox center of the sub object selected

#### Углы

-   Angle Rotation

1.  
    **-**: Decrease the value by 10 degrees

2.  
    {{SpinBox|0 Degrees}}: Value

3.  
    **+**: Increase the value by 10 degrees

-   Number images: The number image saved with the values given is calculated (approximation + 1)
-   Angle Begin Rotation

1.  
    **-**: Decrease the value by 10 degrees

2.  
    {{SpinBox|0 Degrees}}: Value: Angle of the starting rotation

3.  
    **+**: Increase the value by 10 degrees

-   Degrees Angle End Rotation

1.  
    **-**: Decrease the value by 10 degrees

2.  
    {{SpinBox|360 Degrees}}: Value: Angle of the end rotation

3.  
    **+**: Increase the value by 10 degrees

#### Command

-   Delay between 2 images

1.  
    {{SpinBox|0,00 Delay second}}: If there is a problem saving images due to speed, then add a delay of X seconds.

2.  
    {{CheckBox|Reverse}}: Checked, this option reverses the rotation 3D view or Object

3.  
    {{CheckBox|TRUE|Original position}}: This option restores the original position of the 3D View or the Object rotated. Instead fo the 3D view or the Object staying in the last position of the rotation.

4.  
    **Save the animation**: Save the animation

## Примеры

![](images/Macro_Screen_Wiki_03_Set_Screen.png )


*Captured screen with dimensions of `640px x 400px*`

![](images/Macro_Screen_Wiki_04_Tile_Screen.png )


*Same dimensions as the previous image, this one is captured as 'Tile Screen'.*

![](images/Macro_Screen_Wiki_Object_Direction_Object.gif )


*Animation mode: Object selected and direction BoundBox center Object.<br/>The images must be assembled with a 3rd party application to create an animated .gif<br/>such as [https://daviesmediadesign.com/project/make-animated-gif-gimp/ GIMP] or [https://www.screentogif.com ScreenToGif]*

![](images/Macro_Screen_Wiki_Object_Direction_SUBObject.gif )


*Animation Object Direction SubObject selected.<br/>The images must be assembled with a 3rd party application that creates an animated .gif<br/>such as [https://daviesmediadesign.com/project/make-animated-gif-gimp/ GIMP] or [https://www.screentogif.com ScreenToGif]*

![](images/Macro_Screen_Wiki_07.png )


*The FreeCAD window resized. The dimension may be different from the definition (depending on the Widget, title bar etc... used.)*

## Версии

Version=00.05: 2021/05/21 : adding code in Save file section for Linux Mint QFileDialog ignore the extension. Only the Path+name is displayed


```python
global switchQFileDialogMint
                ####  mint
                if switchQFileDialogMint == True:   #
                    Filter = Filter[Filter.find("."):Filter.find(")")]
                    SaveName = SaveName + Filter
                ####  mint
```

Version=00.04: 2021/01/13 : adding mini ToolBar

Version=0.03: 2020/10/30 : create a tool bar for the image and new button for unique image

Version=0.02: 2020/05/04 : correct bug color button (self.PB\_01\_Color obsolete)

Version=0.01: 2020/03/21
