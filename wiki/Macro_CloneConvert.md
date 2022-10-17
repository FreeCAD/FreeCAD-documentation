# Macro CloneConvert
{{Macro
|Name=Macro CloneConvert
|Icon=Macro_CloneConvert.png
|Description={{ColoredText|#ff0000|#ffffff| Latest update   * GUI modified for HiDPI support (QGridLayout). Runs ≥v0.18 (PySide2 Qt5)}}<br/><br/> 
For previous versions see [https   *//gist.githubusercontent.com/mario52a/9f2f2f6144e1307a048f1840ef99300c/raw/0a141260ad8d5f67f0fc18b9b40ef37757c06c65/Macro_CloneConvert.FCMacro Macro_CloneConvert] and install manually.<br/><br/>Creates a Clone/Copy/Compound of the object(s) and then converted into a chosen position and size (''inch, mm, m, µm''...) or free. The base object is recognized in ''mm'' (FreeCAD base).
|Author=mario52
|Version=0.15
|Date=2020-06-06
|FCVersion= ≥0.18
|Download=[https   *//www.freecadweb.org/wiki/images/0/0a/Macro_CloneConvert.png ToolBar Icon]
}}

## Description

Creates a clone or copy of the object and then converts it into a chosen position and size (*inch, mm, m, µm*\...) or free. The base object is recognized in *mm* (FreeCAD base)

 

## Usage

1.  Run the macro
2.  Set the XYZ settings
3.  Choose \"Clone\" or \"Copy\"
4.  Choose a measurement unit
5.  Select your object
6.  Click **Ok**

## Notes

-   If no value is entered a copy or clone will be created without modification.
-   If no object is selected the **Ok** button will be colored in red.

The value of the **BoundingBox**, **Volume** and **Surface** is displayed in the [Report view](Report_view.md), in the case of **Copy** multiple object, the display will show BoundingBox 0.0.

The base is the mm example with a **1 mm** side of cube   *

Select in the comboBox **inch**, **1 inch = 25.4 mm** , the fields **\"Scale free\"** automatically adjusts to 25.4 (the values ​​in **\"Scale-free\"** can be changed separately). Click **Ok** button, the clone created will have **25,4 mm x 25,4 mm x 25,4 mm**

**150%** = **1,50** in the **\"Scale free\"** fields
**104%** = **1,04** in the **\"Scale free\"** fields

Inverse operation    *

If you want to reduce an object ex   * a cube 25.4 mm (1 inch) in cube 1 mm sides, use the following formula, **1 / 25.4 = 0.0393700** and enter the value **0,0393700** (with comma) in the Scale field XY and Z.

In a cube of 5 mm, made​​ **5 / 25.4 = 0.1968503** and enter the value **0,1968503** (with comma) in the Scale field XY and Z.

**50%** = **0,50** in the **\"Scale free\"** fields
**4%** = **0,04** in the **\"Scale free\"** fields
Predefined units are   * km, hm, dam, m, dm, cm, **mm**, µm, nm, inch, link, foot, yard, perch, chain, furlong, mile, league, nautique.
<img alt="CloneConvert" src=images/Macro_CloneConvert_01.png  style="width   *350px;">

-   **Mode**
-   **Clone    *** The object(s) clone are create
-   **Copy    *** One copy of the objet(s) is create
-   **Comp    *** One compound of the objet(s) is create
-   **Increm.    *** incrementing the coordinates data to the original coordinates of the object (Placement, Rotation \...)
    If this is not checked the Placement begin in coordinates 0,0,0 of FreeCAD
    In case a compound Placement information is \[0,0,0\] the Placement begin in the position of object
    If the real location is away from the base coordinates 0,0,0 use the **ValueAt()** button for the real Placement of the subObject selected Face, Wire, Line \....
-   **Unique    *** If this checkBox is checked and multiple object selected, the clone created is one unique object

-   **Coordinates**
-   ****...**    *** This button align the YZ values on the value of X to have the same values ​​XYZ (or manually). Two click reset the coordinates values to 0.0
-   **Coordinate X    *** Move the copy to the Coordinate X selected (Base 0,0,0 if Increm. is not checked)
-   **Coordinate Y    *** Move the copy to the Coordinate Y selected (Base 0,0,0 if Increm. is not checked)
-   **Coordinate Z    *** Move the copy to the Coordinate Z selected (Base 0,0,0 if Increm. is not checked)

-   **Rotation**
-   ****...**    *** This button align the Pitch and Roll values on the value of Yaw to have the same values ​​Rotation (or manually)
    Two click reset the rotations values to 0.0
-   **Yaw (Z )    *** Rotate the copy to the axis Z (Yaw) (Begin 0 if Increm. is not checked)
-   **Pitch ( Y )    *** Rotate the copy to the axis Y (Pitch) (Begin 0 if Increm. is not checked)
-   **Roll ( X )    *** Rotate the copy to the axis X (Roll) (Begin 0 if Increm. is not checked)

-   **Scale predefined**
-   **Scale predefined    *** predefined scales in units, km, hm, dam, m, dm, cm, **mm**, µm, nm, inch, link, foot, yard, perch, chain, furlong, mile, league, nautique or choose a free value in the Scale free field.

-   **Number copy**
-   **Number copy    *** number of copies

-   **Scale free**
-   ****...**    *** This button align the Scales values on the value of Scale X to have the same values ​​XYZ (or manually)
    Two click reset the scales values to 1.0
-   **Scale X    *** free scale , if the value is negative **( -10)** , the object is scaled **x 10** and will be reversed in the X axis, to reduce the shape give a decimal value **(0,5)**
-   **Scale Y    *** free scale , if the value is negative **( -10)** , the object is scaled **x 10** and will be reversed in the Y axis, to reduce the shape give a decimal value **(0,5)**
-   **Scale Z    *** free scale , if the value is negative **( -10)** , the object is scaled **x 10** and will be reversed in the Z axis, to reduce the shape give a decimal value **(0,5)**

-   ****ValueAt()**    *** Give the valueAt() the subObject selected Face, Wire, Line \...
    This option is useful in case a compound Placement information \[0,0,0\] and its real location is away from the base coordinates 0,0,0 (gives no provide information about the rotation of the object)
-   ****Ok**    *** the OK button validates and launches the command, if no object is selected the **Ok** button will be coloured in red
-   ****Reset**    *** the Reset button puts all the values to zero
-   ****Quit**    *** the Quit button exit the macro




## Script

The icon ![](images/Macro_CloneConvert.png )

**Macro_CloneConvert.FCMacro**

Download the macro to Gist [Macro_CloneConvert.FCMacro](https   *//gist.github.com/mario52a/9f2f2f6144e1307a048f1840ef99300c)

## Revision

06/06/2020 ver 0.15 = icon

20/05/2020 ver 0.14 = grid layout PySide2 Qt5

15/09/2019 ver 0.13 = replace the grec sign micro to \"um\", replace all \"\_translate(\"MainWindow\", \"mm\", None)\" to \"mm\" and comment line \"text.encode(\'utf-8\')\" cause not work with FC 0.19 18.213

01/06/2019 ver 0.12 = adapted for 0.19 et correction \"Copy   *legacy=True\" and ShapeColor \.....

30/03/2018 ver 0.11 = odd checkBox, if multi selection the clone are object unique or object separate

07/06/2017 ver 0.10 = replace Draft\...Copy to Part..Shape cause section Copy    * not draw copy scaled of object but copy not scaled ??

14/06/2016 ver 0.9 = adding the choice of number of copies and labels optimization

31/01/2016 ver 0.8 = modify the buttons reset section for two click for reset (in case modification the value)

30/01/2016 ver 0.7 = rewriting code with Placement and Increment and adding buttons Compound, Increment, ValueAt(),

26/01/2016 ver 0.6 = correction placement with many objets Copy

26/07/2015 ver 0.5 = correction rotate many objects Function Copy

25/07/2015 ver 0.4 = adding rotation

11/08/2014 replace \"AttributeError\" to \"Exception\"

02/07/2014 ver. 0.3 = modified to operate PyQt4 and PySide

09/05/2014 ver. 0.2 = adding function \"Copy\"



---
![](images/Right_arrow.png) [documentation index](../README.md) > Macro CloneConvert
