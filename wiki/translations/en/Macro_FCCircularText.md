# Macro FCCircularText/en
{{Macro
|Name=Macro FCCircularText
|Icon=FCCircularTextButtom.png
|Description={{ColoredText|#ff0000|#ffffff|Latest macro version supports a HiDPI layout (QGridLayout) and runs only on versions 0.18 or higher (requires PySide2/Qt5)}}<br/><br/>For backward compatible version of the macro see [https   *//gist.githubusercontent.com/mario52a/a25e802498bae6959335/raw/db47f78f2b20a35137ac213b8d1a62d30f525dcb/Macro_FCCircularText.FCMacro FCCircularText] and install manually. <br/><br/>This macro makes use of the [[Draft ShapeString]] tool to create a text line placed in different circular orientations, including circumferential and helical (in the fashion of a Trajan Column). It can also be used to create a clock face with Arabic numerals ''1, 2, 3,'' etc., or Roman numerals ''I, II, III,'' etc.
|Author=Mario52
|Version=0.21
|Date=2022/05/31
|FCVersion=0.19
|Download=[https   *//www.freecadweb.org/wiki/images/c/c1/FCCircularTextButtom.png ToolBar Icon]
}}

## Description

This macro makes use of the <img alt="" src=images/Draft_ShapeString.svg  style="width   *24px;"> [Draft ShapeString](Draft_ShapeString.md) tool to create a text line placed in different circular orientations, including circumferential and helical in the fashion of a [Trajan\'s Column](http   *//en.wikipedia.org/wiki/Trajan%27s_Column). It can also be used to create a clock face with Arabic numerals *1, 2, 3,* etc., or Roman numerals *I, II, III,* etc. This latter usage was inspired by the Forum thread [Macro to Create Clock Face](http   *//forum.freecadweb.org/viewtopic.php?f=22&t=5013&hilit=Clock) by FC community member, cblt2l.


{{Codeextralink|https   *//gist.githubusercontent.com/mario52a/a25e802498bae6959335/raw/febfd7cec2e4fcbe1abdc04161f464deb9d69691/Macro_FCCircularText.FCMacro}}


   *   <img alt="360 degree orientation" src=images/FCCircularText_01.png  style="width   *400px;">



*Example of the macro displaying text in a 360 degree orientation*

## Usage

Launch the macro folder **FcString** for created characters and a file **FcClock** for created clocks.

All the characters are and remain independent. When creating extrusions nothing is deleted. If Compound is created with **Run Comp** it is copied out of the folder.

The options are shaded by default and are active in all functions if they are checked {{CheckBox|TRUE|}}   *

-    {{CheckBox|Extrude Char.}}
    

-    {{CheckBox|Placement.}}
    

-    {{CheckBox|SP. inclination.}}
    

Except for one Clock Service Placement box **Z** is activated and moves the text in the direction **Z** to place the text on the support surface.

## Notes

-   This macro will gray-out (deactivate) options that are not relevant for a selected function.

## Interface

Overview

![GUI](images/FCCircularText_06.png ) 

### First section 

![](images/FCCircularText_07.png ) 

-   TextEdit window that lets you copy the text to display (click on the **Reset** allows to know the number of the input string that is displayed in the window title)

-   The **Reverse** button reverses the text

-    {{CheckBox|Word}}checked, this option consider the text as word, the text is cut on space and write the text word by word (instead character by character in normal use)

-   The **Help** button displays the wiki page in the FreeCAD browser

-   LineEdit   * display the path and name of file font

-    **Other**button for search the font in other directory in case all directory is not discovery automatically

-   ComboView to choose the font

-    **Origin**return to origin system font path ex   * \"C   */Windows/Fonts/\"

    -   Default ARIAL.TTF

#### Options available 

After the first use, you must modify the following parameters   *

**User parameter   *BaseApp/Preferences/Macros/FCMmacros/FCCircularText**

**switchModeTextList**

-   0 = normal text mode (and black) cuts the switchFontComBox
-   1 = allows switchFontComBox 1

**switchFontComBox**

-   0 = (and switchModeTextList= 1) text mode (in color) in ComboBox list, faster
-   1 = (and switchModeTextList= 1) fontFamily slower but more beautiful ComboBoxst!

**setSystemFonts**

-   0 = matplotlib.font\_manager.findSystemFonts(\"C   */\", \"ttf\")
-   do all the fonts (in all folders and sub-folders of the DD) time !!
-   1 = fontman.findSystemFonts(self.pathFont)
-   do all the fonts in the directory (and in all the sub-folders)

**seTtextAlignement**

-   0 = AlignLeft (default)
-   1 = AlignCenter
-   2 = AlignRight

setFontByDefault

-   Font by Default

**switchResetFALSE**

-   0 = reset (default)
-   1 = no reset (not recommended) some switches can remain open or close unexpectedly!

**Example**

![](images/FCCirculatText_Config_0000A0.png )

1.  switchModeTextList= `False`
2.  switchFontComBox = `False`
3.  setSystemFonts = `False`
4.  seTtextAlignement = 0




![](images/FCCirculatText_Config_1000A0.png )

1.  switchModeTextList= `True`
2.  switchFontComBox = `False`
3.  setSystemFonts = `False`
4.  seTtextAlignement = 0




![](images/FCCirculatText_Config_1001A0.png )

1.  switchModeTextList= `True`
2.  switchFontComBox = `False`
3.  setSystemFonts = `False`
4.  seTtextAlignement = 1 *(0=Left, 1=Centered, 2=Right)*




![](images/FCCirculatText_Config_1101A0.png )

1.  switchModeTextList= `True`
2.  switchFontComBox = `True`
3.  setSystemFonts = `False`
4.  seTtextAlignement = 1




### Second Section 

Configuring characters in FCCircularText

![](images/FCCircularText_08.png ) 

#### First zone 

Your choice    *

![](images/FCCircularText_09.png )


<center>

Image   *FCCircularText 20.png\|**Outdoor** Image   *FCCircularText 21.png\|**Indoor** Image   *FCCircularText 22.png\|**Helix** Image   *FCCircularText 23.png\|**Clock**


</center>




![](images/FCCircularText_24.png )

-    **Mode Stand**or **Mode Flat**    * The text will be placed standing or flat (same as clock) options **Outdoor** and **Indoor** are reversed.





<center>

Image   *FCCircularText 01.png\|**Mode Stand** **Outdoor** The text will be written up. Image   *FCCircularText\_40.png\|**Mode Flat** **Outdoor** The text will be placed flat.


</center>


<center>

Image   *FCCircularText 39.png\|**Mode Flat** **Indoor** The text will be placed flat. Image   *FCCircularText\_03.png\|**Mode Stand** **Indoor** The text will stand registered (same as clock).


</center>

#### Second area 

This section allows you to configure the overall behavior of characters in all the choices available but with some variation. If the command is not used in the option chosen, it will be grayed out.

![ left](images/FCCircularText_10.png )

-    {{SpinBox|10.0 mm}}**Radius of circle**    * Radius of the circle. (Default 10)

-    {{SpinBox|2.0 mm}}**Size character**    * Character height. (Default 2)

-    {{SpinBox|0 deg}}**Begin angle**    * Starting angle of the first character in the circle. (Default 0 °)

-    {{SpinBox|360 deg}}**End angle**    * Angle end of the last character of the text. (Default 360)

-    {{SpinBox|10.0 deg}}**Correction angle**    * Character correction angle to make it tangent to the circle. (Default 10 °)

-    {{SpinBox|0.15 mm}}**Correction radius**    * Fixed the radius of the circle characters (optional). (Default 0.15)

-
-    {{CheckBox|'''Extrude Char'''}}   * Checkbox extrusion characters. (Inactive Default)

-    {{CheckBox|'''Placement'''}}   * Text placement in the 3D view. (Inactive Default)

-    {{CheckBox|'''Sp. inclination'''}}   * Inclination of characters in three axes X, Y and Z (example to cover such a cone). (Inactive Default)




##### Outdoor

Default mode. The text is written on the outside of the circumference of the circle.


<center>

Image   *FCCircularText 20.png\|**Outdoor** Image   *FCCircularText 25.png\| Image   *FCCircularText 30.png\|


</center>

##### Indoor

The text is written on the inner side of the circumference of the circle


<center>

<File   *FCCircularText> 21.png\|**Indoor** Image   *FCCircularText 03.png\| Image   *FCCircularText 27.png\|


</center>

##### Helix

The text is entered on the outer circumference of a helix.


<center>

Image   *FCCircularText 22.png\| **Helix** Image   *FCCircularText 33.png\| Image   *FCCircularText 34.png\|


</center>

-   The helix area is hidden by default. The window is visible if the radio button {{RadioButton|TRUE|Helix}} is checked




![](images/FCCircularText_14.png )

-   All characters configuration options are available.
-   **Step of helix** which corresponds to the pitch of the helix turns and displays 2 (character height) by default.
-   \'\'\'Char. per turn \'\'\'activates and displays 10 by default, which corresponds to 10 characters per helical turn.




![](images/FCCircularText_15.png )

-   If **Step of helix** (helix pitch) is zero, Spinboxes **Base Helix** and **End Helix** are activated.
-   **Base Helix** provides the basis for starting the helix (even Placement Z). If \'\' \'Placement Z\' \'\' is different from zero, the starting point is added to Z Placement
-   **End Helix** End of the helix pitch of the helix will be calculated relative to the height and the number of characters per helical turn.

##### Clock

The figures are part of a circle with Arabic numerals or Romans.


<center>

Image   *FCCircularText 23.png\|**Clock** Image   *FCCircularText 35.png\|**Axial** Image   *FCCircularText 36.png\|**Redress**


</center>

-   By default, the section is hidden. The window is visible if the radio button {{RadioButton|TRUE|Clock}} is checked




![](images/FCCircularText_16.png )

-   When the selection is made, the following functions get dark and are usable   *
    1.  Begin angle.
    2.  End angle.
    3.  Correction angle.
    4.  Correction radius.
    5.  The buttom **Mode Stand** or **Mode Flat**.
-   The area **Clock** is activated.




![](images/FCCircularText_19.png )

-   **Radius of support**    * If a value is given, support will be created (default 0).
-   If **Support number face** is different from zero a support is created. (If \'\'\'Extrude support \'\'\'= zero then a face is created).
    -   1 = A circle is created (circle appears).
    -   2 = A rectangle is created (length = (Radius of media \* 1.5) width = Radius of support) (Rectangle appears).
    -   3 = A triangle is created (circumscribed) (Triangle appears).
    -   4 = A square is created (Radius of support) (Square appears).
    -   5 = A polygon with the number of faces displayed (circumscribed) (Polygon appears).
-   **Extrude support** is activated and an extrusion dimension can be given.




<img alt="" src=images/FCCircularText_18.png )![](images/FCCircularText_38.png  style="width   *200px;">  <img alt="" src=images/FCCircularText_17.png )![](images/FCCircularText_37.png  style="width   *200px;"> 

-   If **Support number face** is equal to zero there is no support.

-    **Mode Roman**   * The writing will be in Roman figures **I II III IIII V VI VII VIII IX X XI XII**

-    **Axial**   * The figures will be written axially.

### Path section 

![](images/FCCircularText_06_Path.png ) 

The title section change and display the length of the wire selected.

If you select one wire, arc, circle, line and edge the section Path is coloured in {{ColoredText|#E0F8E0|green}} and the unused command coloured in {{ColoredText|#F8E0E0|red}}

1.  
    {{RadioButton|Orthogonal}}the character is Orthogonal to the view

2.  
    {{RadioButton|Tangent}}the character is Tangent to point path on wire




1.  
    {{RadioButton|BB Base}}the point base of the character is to point path on the wire

2.  
    {{RadioButton|BB Center}}the bounBox center of the character is to point path on the wire

3.  
    {{RadioButton|BB Top}}the top boundBox of the character is to point path on the wire

the last Radio Button used is saved in the parameter of FreeCAD

### Command section 

![](images/FCCircularText_13.png ) 

-    **Exit**   * Leaves the macro.

-    **Reset**   * Reset all values and displays the number of characters displayed in the window.

-    **Run Comp**   * Launches the macro and creates a Compount object of all characters.

-    **Run**   * Launches the macro

### Parameters available 

Certain parameter are available in the parameters of FreeCAD see   * **Menu → Tools → Edit parameters...**

-   User parameter   * BaseApp/Preferences/Macros/FCMmacros/FCCircularText

-   -   
        `switchModeTextList`
        
           *

        -   
            `False`
            
            normal text mode (and black) turns off switchFontComBox

        -   
            `True`
            
            allow switchFontComBox 1 (default)

    -   
        `switchFontComBox`
        
           *

        -   
            `False`
            
            (and switchModeTextList = 1) text mode (in color) in Faster ComboBox list (default)

        -   
            `True`
            
            (and switchModeTextList = 1) font Family in ComboBox list slower but more beautiful!

    -   
        `setSystemFonts`
        
           *

        -   
            `False`
            
            matplotlib.font\_manager.findSystemFonts (\"C   * /\", \"ttf\") do all fonts (in all folders and subfolders of the HD) time !!

        -   
            `True`
            
            fontman.findSystemFonts (self.pathFont)make all the fonts in the directory (and in all the subfolders) (default)

    -   
        `seTtextAlignement`
        
           * 0 = AlignLeft (default) 1 = AlignCenter 2 = AlignRight

    -   
        `setFontByDefault`
        
           * Font by Default (the last used)

    -   
        `switchResetFALSE`
        
           * `False` reset (default), `True` no reset (not recommended) some switches can stay open or close unexpectedly!

    -   
        `setPathOrthogonal`
        
           * `True` `False`

    -   
        `setPathTangent`
        
           * `True` `False`

    -   
        `setPositionBase`
        
           * `True` `False`

    -   
        `setPositionCenter`
        
           * `True` `False`

    -   
        `setPositionTop`
        
           * `True` `False`

    -   
        `switchVersionSearch`
        
           * `True` `False`

    -   
        `Version`
        
           * FCCircularText version

Launch the macro folder **FcString** for created characters and a file **FcClock** for created clocks.

## Script

The button icon   *

\- in .PNG ![](images/FCCircularTextButtom.png )

\- in .SVG <File   *FCCircularTextButtom.svg>

(See [ Customize\_Toolbars](Customize_Toolbars.md) for more)

### Script 

**Macro\_Circular\_Text.FCMacro**

or download the script    *

\- on github [Macro\_FCCircularText.FCMacro](https   *//gist.github.com/mario52a/a25e802498bae6959335) ver 0.21 2022/05/31

\- at the forum [Extrude from curved surface of cylinder](http   *//forum.freecadweb.org/viewtopic.php?f=3&t=7384&p=87642#p87642)

## Example


<center>

Image   *FCCircularText 02.png\|Text beginning at 180 degrees (**Begin angle**) end at 360 degrees (**End angle**) external curve. Image   *FCCircularText 03.png\|Text set in an inner curve.


</center>



<center>

Image   *FCCircularText 04.png\|Text circular on internal and external curve. Image   *FCCircularText 05.png\|Circular text on a flat onbjet.


</center>



<center>

Image   *FCCircularText IndoorFlat 01.png\|Configuration Superior.(click to elarge) Image   *FCCircularText IndoorFlat 02.png\|Configuration Inferior.(click to elarge)


</center>



<center>

Image   *FCCircularText 26.png\|External curve. Image   *FCCircularText 28.png\|Internal curve.


</center>



<center>

Image   *FCCircularText 29.png\|Internal curve extrusion material designated and subtraction. Image   *FCCircularText 31.png\|External curve.


</center>



<center>

Image   *FCCircularText 32.png\|Internal curve with subtraction. Image   *FCCircularText 41.png\|Extrusion on a cone with \'\'\'Sp. Inclination \'\'\'45° axis Z.


</center>



<center>

Image   *FCCircularText 42.png\|Ring Internal curve with subtraction. Image   *FCCircularText 61.png\|Pivot character 0°, 90°, \....


</center>



<center>

Image   *FCCircularText\_Path\_00\_002\_000.png\| {{CheckBox|TRUE|Word}} The text is cutting on space character


</center>

==Example onto Ellipse==


<center>

Image   *FCCircularText 43.png\|Create your ellipse hers 100x50. Image   *FCCircularText 44.png\|Exrtude it 50 mm.


</center>



<center>

Image   *FCCircularText 45.png\|Discretize the perimeter and create points with the macro [Work Features](Macro_WorkFeatures.md).
Tab Point \> Point 2/3 \> Points=Cut (Wire) Image   *FCCircularText 46.png\|Create the circle to 3 points with the macro [Work Features](Macro_WorkFeatures.md).
Tab Circle Circle=(3 Points)


</center>



<center>

Image   *FCCircularText 47.png\|Create point center circle with the macro [Work Features](Macro_WorkFeatures.md).
Tab Point \> Point 1/3 \> Circle(s) center. Image   *FCCircularText 48.png\|Create the benchmark lines and configure FCCircularText.


</center>



<center>

Image   *FCCircularText 49.png\|Create the text with **Run Comp**. Image   *FCCircularText 50.png\|Select Ellipse Extrude, Shape and press the **<img src="images/Part_Cut.svg" width=16px> '''Part Cut'''** button.


</center>



<center>

Image   *FCCircularText 51.png\|Delete the circle, points and lines. Image   *FCCircularText 52.png\|Ellipses.


</center>

Mode relief   *


<center>

Image   *FCCircularText 53.png\|Create an ellipse. ![](images/Draft_Ellipse.svg ) Image   *FCCircularText 54.png\|Create a rectangle include all object. ![](images/Draft_Rectangle.svg )


</center>



<center>

Image   *FCCircularText 55.png\|Select the rectangle , the ellipse and make compound
Activate the Part module, then Menu Part \> Make compound. Image   *FCCircularText 56.png\|Extrude the compound of Solid.


</center>



<center>

Image   *FCCircularText 57.png\|Select Shape (text) , the compound and Cut. Image   *FCCircularText 58.png\|The text is cut in the shape of the ellipse.


</center>



<center>

Image   *FCCircularText 59.png\|Select the Ellipse extruded , the Cut (text) and fuse.


</center>


## Example section path 


<center>

Image   *FCCircularText\_Path\_00\_Orth\_Base\_000.png\|Text on BoundBox Base (normal) Image   *FCCircularText\_Path\_00\_Orth\_Center\_000.png\|Text on BoundBox Center character


</center>



<center>

Image   *FCCircularText\_Path\_00\_Orth\_Top\_000.png\|Text on BoundBox Top character Image   *FCCircularText\_Path\_00\_001\_000\_000.png\|Text on selected line   *
1   * Orthogonal
2   * Tangent


</center>

## Limitations


**Note**

it is possible that an error may occur between versions. Please post the issue on the forum and wait for the updated fix or rollback to a previous version of the macro. Thank you)

It is possible that two characters may overlap. If this happens, here\'s a workaround is available using the [Rotate-To-Point Macro](https   *//www.freecadweb.org/wiki/Macro_Rotate_To_Point).


<center>

Image   *FCCircularText Correction.gif\|Character overlap issue and the workaround


</center>

(not fully developed)

Planned   *

Writing on a path circular text of position object selected.

## Change log 

-   ver 0.21 2022/05/31    * adding button search other path fontmanuelly, and button return font origin of system

-   ver 0.20 2021/04/05    * adding icone in macro, Tab for diminish the heigth of the macro, remove all dimensions of widgets now fully compatible with the stylesheet, revisite the search version for compatibility and other little change.

-   ver 1.19 2021/03/15    * adding button **Delette** the last object created and the code `FreeCAD.ActiveDocument.openTransaction("FCCTc")` for Undo/Redo system

-   -   Adding CheckBox {{CheckBox|FALSE|Reset}} for switched/activated (*requested by users*) the natural reset after all push button **Run**and **Run comp**. This use checkBox is {{ColoredText|not advised}}, is you constade one malfunction pusch the **Reset** button or quit FCCircularText and restart.

-   ver 0.18 2021/01/19    * correction bug see [FCCircularText Macro issues](https   *//forum.freecadweb.org/viewtopic.php?f=22&t=54524&p=468687#p468687)

-   ver 0.17b 2020/09/28    * correction little bug (pl instead plm in path section) and arrange the window (dimension) Clock, Helix, Path

-   ver 0.17 2020/09/26    * adding create circular text on wire (curve, arc, spline, line \...) selected, mode word

ver 16d 2020/09/15    * see the [MasterCATZ commented Sep 14, 2020 message](https   *//gist.github.com/mario52a/a25e802498bae6959335)

delette the FC 0.18 test section   *


```python
#### Test FreeCAD.Version simple ############################################################################################################
if int(FreeCAD.Version()[1]) < 18   *      # Version de FreeCAD
    FreeCAD.Console.PrintMessage("This version " + __Title__ + " rmu  work with the FreeCAD 0.18 or higher." + "\n\n")
    FreeCAD.Console.PrintMessage("For the precedent version see the page " + "\n\n")
    FreeCAD.Console.PrintMessage("https   *//gist.githubusercontent.com/mario52a/a25e802498bae6959335/raw/db47f78f2b20a35137ac213b8d1a62d30f525dcb/Macro_FCCircularText.FCMacro" + "\n\n")
#### Test FreeCAD.Version simple ############################################################################################################
```

-   ver 0.16c 2020/07/24    * modify text proposed by Kunda1 [Please review FCVerticalText Macro](https   *//forum.freecadweb.org/viewtopic.php?f=22&t=48902#p418776)

-   ver 0.16b 2020/07/24    * correct **\_\_title\_\_** to **\_\_Title\_\_** in 0.18 FC test (see [Please review FCVerticalText Macro](https   *//forum.freecadweb.org/viewtopic.php?f=22&t=48902))

-   ver 0.16 2020/06/07    * little bug in Linux with the path, impost **PolicePath = \"/usr/share/fonts/\"** (stay on path /xx/xx/xx/xx/xx/xx/ on entry)

-   ver 0.15 2020/06/01    * For PySide2 Qt5 adding matplotlib fonts in comboView, config on parameter

-   ver 0.14-4 2020/04/25    * corrected for \"**DisplayMode = u\"Flat Lines**\"    *

-   ver 0.14-3 2020/04/25    * adapted for    *


```python
OS   * Windows 10 (10.0)
Word size of OS   * 64-bit
Word size of FreeCAD   * 64-bit
Version   * 0.19.20655 (Git)
Build type   * Release
Branch   * master
Hash   * e8e67e8c5ebbc9f9ed9ea67aba5b891969595ece
Python version   * 3.6.8
Qt version   * 5.12.1
Coin version   * 4.0.0a
OCC version   * 7.3.0
```

-   ver 0.14-2 2019/07/22 replace chr(176) (give error \<FC 0.18) and replace with the wmayer code, see [Fehler in Version 0.19 pre ??](https   *//forum.freecadweb.org/viewtopic.php?f=13&t=36380&p=308476#p308357)

       carDegrees = b' \xc2\xb0'.decode("utf-8")    #thanks wmayer [https   *//forum.freecadweb.org/viewtopic.php?f=13&t=36380&p=308476#p308357](https   *//forum.freecadweb.org/viewtopic.php?f=13&t=36380&p=308476#p308357)
       self.DS_InclinaisonX.setSuffix(carDegrees)
       self.DS_InclinaisonY.setSuffix(carDegrees)
       self.DS_InclinaisonZ.setSuffix(carDegrees)

-   ver 0.14-1 2019/06/11 replace \"°\" to chr(176)

-   ver 0.14 2019/04/27 compatible for Python 3.6.6 and Qt 5.6.2 (cause   * unicode() )


```python
latest testing   *

#OS   * Windows 10
#Word size of OS   * 64-bit
#Word size of FreeCAD   * 64-bit
#Version   * 0.19.16523 (Git)
#Build type   * Release
#Branch   * master
#Hash   * 9b3ec233c8b21e0df66fada487cd10f471d60cac
#Python version   * 3.6.6
#Qt version   * 5.6.2
#Coin version   * 4.0.0a
#OCC version   * 7.3.0
```

-   ver 0.13 30/01/2018 add feature Pivot for rotate the character on himself

-   ~~ver 0.13 09/08/2016 replace the button \"New font\" to \"fontComboBox\" cause , with Windows 10 the window Font stay empty the files are hidden~~

-   ver 0.12 03/07/2016 optimize the code for accept the decimal number in determination angle

replace the line 
```python
            for angleTr in range(debut,rotation,((rotation-debut)/nombre))   * 
``` to 
```python
            for angleTrFloat in range((debut*10000),(rotation*10000),int((round(((float(rotation)-float(debut))/float(nombre)),4)*10000)) )   *    # pour 4 decimales
                angleTr = (float(angleTrFloat)/10000)
```

-   ver 0.10 17/05/2015 adding lines 1365, 1366 only created more clock face ?? ()


```python
            supp.MakeFace = True
            App.activeDocument().recompute()
```

-   ver 0.9 11/05/2015 thank you NormandC for testing

replace 
```python
        self.DS_InclinaisonX.setSuffix(" X°")
        self.DS_InclinaisonY.setSuffix(" Y°")
        self.DS_InclinaisonZ.setSuffix(" Z°")
``` to 
```python
        self.DS_InclinaisonX.setSuffix(unicode(" X°"))
        self.DS_InclinaisonY.setSuffix(unicode(" Y°"))
        self.DS_InclinaisonZ.setSuffix(unicode(" Z°"))
```

-   ver 0.8 10/05/2015 replace \"**String=texte\[ii2\]**\" to \"**String=unicode(texte\[ii2\])**\" line 1290. cause \"**TypeError   * Property \'FontFile\'   * type must be str or unicode, not QString**\"\<span \\\>


```python

# ver 0.8 10/05/2015 /_ # testing with OS    *
##################################################################################################
# OS   * Ubuntu 14.04.1 LTS                          # OS   * Ubuntu 14.04.2 LTS
# Platform   * 32-bit                                # Word size of OS   * 32-bit
# Version   * 0.14.2935 (Git)                        # Word size of FreeCAD   * 32-bit
# Branch   * master                                  # Version   * 0.16.4928 (Git)
# Hash   * eab159b6ee675012bf79de838c206a311e911d85  # Branch   * master
# Python version   * 2.7.6                           # Hash   * d8f63bcfd10301f3d1e141cced4370f0782238d0
# Qt version   * 4.8.6                               # Python version   * 2.7.6
# Coin version   * 4.0.0a                            # Qt version   * 4.8.6
# SoQt version   * 1.6.0a                            # Coin version   * 4.0.0a
# OCC version   * 6.7.0                              # OCC version   * 6.8.0.oce-0.17
##################################################################################################
# OS   * Windows Vista                               # OS   * Windows Vista
# Word size of OS   * 32-bit                         # Word size of OS   * 32-bit
# Word size of FreeCAD   * 32-bit                    # Word size of FreeCAD   * 32-bit
# Version   * 0.15.4527 (Git)                        # Version   * 0.15.4671 (Git)
# Branch   * master                                  # Branch   * releases/FreeCAD-0-15
# Hash   * 0da2e4c45a9a259c26abd54c2a35393e1c15696f  # Hash   * 244b3aef360841646cbfe80a1b225c8b39c8380c
# Python version   * 2.7.8                           # Python version   * 2.7.8
# Qt version   * 4.8.6                               # Qt version   * 4.8.6
# Coin version   * 4.0.0a                            # Coin version   * 4.0.0a
# OCC version   * 6.7.1                              # OCC version   * 6.8.0.oce-0.17
##################################################################################################
```

-   ver 0.7 02/02/2015 suppression 2 str **App.Console.PrintMessage(str(PolicePath)+\"\\n\")** to **App.Console.PrintMessage((PolicePath)+\"\\n\")** that caused an error with the characters above 128 in the police path.
-   ver 0.6 23/11/2014 corrected \"texte = unicode(self.textEdit.toPlainText())\" now accept \"\'éèà@\...\"
-   ver 0.5 19/11/2014 Gui
-   ver 0.4 10/10/2014 add variable \"rotation\" in the loop (**for i in range(0,rotation,(rotation/nombre))   * \# 360 a parametrer**)
-   ver 0.4 27/08/2014 correction error of de radius (exterieur=0, debout=1)
-   ver 0.3 26/08/2014 add creation text of flat curve
-   ver 0.2 26/08/2014 add creation text of internal curve
-   ver 0.1

\(2537\)

### Links

To comment on the [Extrude from curved surface of cylinder](http   *//forum.freecadweb.org/viewtopic.php?f=3&t=7384)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Draft](Category_Draft.md) > Macro FCCircularText/en
