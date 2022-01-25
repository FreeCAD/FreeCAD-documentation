# Macro FCCamera/pl
{{Macro
|Name=Macro FCCamera
|Icon=FCCamera_00.png
|Description={{ColoredText|#ff0000|#ffffff|New version GUI modifyed for the HD dpi (QGridLayout) run only FC version 0.18 and more (PySide2 Qt5)}}<br/><br/> 
For the precedent version see [https://gist.githubusercontent.com/mario52a/4aa545c23b323cf68824/raw/42dc3ef73dc8db463a03b175f5a7f1f6978e3293/Macro%2520FCCamera.FCMacro FCCamera] and install it manually.<br/><br/> 
This macro can rotate the screen in a defined angle and the defined axis and creates a plan to face the screen to create a form in the specified plan positions the selected face facing the screen, to detect the position of the camera, align view to face or to axis, align the object to view.
|Author=Mario52
|Version=0.14
|Date=2020/10/20
|FCVersion=0.18 and more
|Download= 
}}

## Description

This macro can rotate the screen in a defined angle and the defined axis and creates a plan to face the screen to create a form in the specified plan positions the selected face facing the screen, to detect the position of the camera, align view to face or to axis, align the object to view.


{{Codeextralink|https://gist.githubusercontent.com/mario52a/4aa545c23b323cf68824/raw/98d90ee303e9fa5d6aed6e9f2e36e7ca1a18ca19/Macro%2520FCCamera.FCMacro}}

## Usage

![FCCamera](images/Macro_FCCamera_00.png )

**Camera of Axis**: The dialog box to enter the rotation value angle in degrees.

**Angle rotation Axis in degrees**: Select the rotation axis **X, Y,** or **Z**.

**Axe of rotation**

-   <img alt="" src=images/FCCamera_01.png  style="width:24px;"> **Accept the rotation** : Accept the rotation give to angle selected

**Virtual**

-   <img alt="" src=images/FCCamera_02.png  style="width:24px;"> **Detect camera orientation** : Detect the camera orientation and print in report view. The returned value is the value provided by the function getCameraOrientation().

**Align view to face selected**

-   <img alt="" src=images/FCCamera_03.png  style="width:24px;"> **To Face.** : Align the view to the selected face. Click and repeat the click for **NormalAt** : \"(0,0,1) (0,0,-1) (0,1,0) (0,-1,0) (1,0,0) (-1,0,0)\"

-   <img alt="" src=images/FCCamera_04.png  style="width:24px;"> **To Axis.** : Align the view to Axis face selected. Click and repeat the click for **Surface Axis** : \"(0,0,1) (0,0,-1) (0,1,0) (0,-1,0) (1,0,0) (-1,0,0)\"

-   <img alt="" src=images/FCCamera_05.png  style="width:24px;"> **Align object to view.** : Align the object selected to the actual view. The changed values are : Rotation Axis((X, Y, Z), Angle) Same Euler angles : Yaw, Pitch, Roll, The Translation is not modify.

-   <img alt="" src=images/FCCamera_06.png  style="width:24px;"> **Create plane of view.** : A circular plane is created facing the screen to mouse click coordinates on an object. The radius of the plane is equal to the maximum dimension of BoundBox. If no object is selected, the plane is created to 0, 0, 0 coordinates with a radius of 20 mm. The radius is modifiable to line 515:


```python
        rayon = 20                            # Radius of plane
```

-    **[<img src=images/FCCamera_07.png style="width:24px"> Reset.**: Reset all values.

-    ** [<img src=images/FCCamera_00.png style="width:24px"> Photo.**: Section save the screen rotation an image in angle value

-    ** [<img src=images/FCCamera_08.png style="width:24px"> Quit.**: Quit FCCamera.

## Section Photo 

![FCCamera](images/Macro_FCCamera_00b.png ) 

-    **ComboBox Actual **: choice your screen definition for the image format

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

-   Line 1 : Number image calculated by the angle give (ex: angle 60 degrees = 360 (complete rotation) / 60 (angle) = 6 images

-   Line 2 : The definition of screen used

-   Background image :
    -   Actual : save image with the screen colour actual
    -   White : save image with the screen colour white
    -   Black : save image with the screen colour black

-    **[<img src=images/FCCamera_00.png style="width:24px"> Launch**: Open the file window , give the name and the path

-    **[<img src=images/FCCamera_07.png style="width:24px"> Reset**: Reset the default value

-    **[<img src=images/FCCamera_00.png style="width:24px"> Return**: Quit the photo panel and return to FCCamera panel




## Links

Related Links with FCCamera

[Macro Rotate View](Macro_Rotate_View.md), [Macro Align Object to View](Macro_Align_Object_to_View.md), [Macro Align Face Object to View](Macro_Align_Face_Object_to_View.md), [Macro WorkFeatures](Macro_WorkFeatures.md)

Discussion Forum [MACRO:Work Feature 2014\_12](http://forum.freecadweb.org/viewtopic.php?f=22&t=9056)

## Script

Download the icon files [FCCamera\_Icones.zip](https://forum.freecadweb.org/download/file.php?id=79288)

Download the macro to Gist [**Macro FCCamera.FCMacro**](https://gist.github.com/mario52a/4aa545c23b323cf68824)

## Examples

### How to place an angle hole 


<center>

<File:FCCamera> 09.png\|Create your object <File:FCCamera> 10.png\|Create one cylinder and positionning this
Give your axis, angle inclination and click the button <img alt="" src=images/FCCamera_01.png  style="width:24px;"> 
**Accept the rotation**


</center>


<center>

<File:FCCamera> 11.png\|Select your cylinder for create your hole <File:FCCamera> 12.png\|In FCCamera click the button <img alt="" src=images/FCCamera_05.png  style="width:24px;"> 
**Align Object to View**


</center>


<center>

<File:FCCamera> 13.png\|The cylinder moves to 15 degrees (take the camera position)
do your Boolean operation <File:FCCamera> 14.png\|Your hole 15 degrees


</center>

The same result can be achieved by creating a plan in the corner gave the mouse click position and a sketch.


<center>

<File:Macro_FCCamera_Align_To_Face.gif%7CExample> placement spring to face axis


</center>


<center>

<File:Test_FCCamera_Photo_01.gif%7CExample> photo rotation and save images (you must create one animate Gif [with GIMP](https://www.gimp.org/))


</center>

## Version

-   **ver 0.14 (20/10/2020):** correction bug \"Grid\" not accepted

-   **ver 0.13 (28/06/2020):** adding files image in source code, create plane \"On point, Center face, BBox center, Center Mass\", gridLayout

-   **ver 00.12.1 (12/02/2020):** suppress the bad character lines 674 and 675 (accent\...) again

-   **ver 12 (01/08/2019):** compatible Python 3 ( print to print() )

-   **ver 11 (13/01/2018):** minor

-   **ver 10 (13/01/2018):** add \"def centerBoundBoxGlobal():\"

-   **ver 09 (08/01/2018):** minor

-   **ver 08 (08/01/2018):** supp \"Pyqt4\" and adjust number image
-   **ver 07 (03/01/2018):** add photo panel and rotation to axis selected (wire, edge, line )

-   **ver 0.6 (13/12/2016):** new system for search the macro path directly in the preferences

#path = FreeCAD.ConfigGet("AppHomePath")
#path = FreeCAD.ConfigGet("UserAppData")
#path = "your path"
param = FreeCAD.ParamGet("User parameter:BaseApp/Preferences/Macro")# macro path
path = param.GetString("MacroPath","") + "/"                        # macro path
path = path.replace("\\","/")
App.Console.PrintMessage("Path locality to FCCamera.....images.png [ " + path + " ]"+"\n")

-   **ver 0.5 06/09/2016:** correct name \"FCCamera\_Axis\_rotation\_X.png\" in reset block

-   **ver 0.4 28/02/2016 :** add display all camera detection and the [Direction](http://forum.freecadweb.org/viewtopic.php?f=13&t=14213#p114667)

-   **ver 0.3 18/03/2015 :** modify line 492 replace \"**pl.Base = App.Vector(0,0,0)**\" to \"**pl.Base = sel\[0\].Placement.Base**\" now no longer moves the form at point (0,0,0) and leaves has the coordinates

-   **ver 0.2 25/02/2015 :** correct names files in for compatibility Linux (case sensitive) thanks microelly2



---
![](images/Right_arrow.png) [documentation index](../README.md) > Macro FCCamera/pl
