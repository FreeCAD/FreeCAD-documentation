# Macro FCInfo ToolBar/pl
{{Macro
|Name=Macro FCCInfo ToolBar
|Icon=FCInfoToolBar.png
|Description=Gives information about the selected shape and can display a conversion of radius, diameter, length, area, volume ... in different units (metric and imperial) in a toolBar. The information to be displayed in real time is parametrizable in the Parameter of FreeCAD.
|Author=Mario52
|Version=00.04
|Date=2023/06/28
|FCVersion=0.18 and more
|Download=[https://wiki.freecadweb.org/images/9/9d/FCInfoToolBar.png The toolBar icon]
|SeeAlso=[Arch Survey](Arch_Survey.md) <img src="images/Arch_Survey.svg" width=32px></br>[Macro FCInfo](Macro_FCInfo.md) <img src="images/FCInfo.png" width=32px></br>[Macro FCInfoGlass](Macro_FCInfoGlass.md) <img src="images/Macro_FCInfoGlass.png" width=32px>
}}

## Description

Gives information about the selected shape and can display a conversion of radius, diameter, length, area, volume \... in different units (metric and imperial) in a toolBar. The information to be displayed is parametrizable in the Parameter of FreeCAD.


{{Codeextralink|https://gist.githubusercontent.com/mario52a/e382adbe41747788ad15a18eb206a872/raw/40ca52f49edb1e29c70f0eaef42934aec19ca594/FCInfo_ToolBar.FCMacro}}

![FCInfo_ToolBar](images/Macro_FCInfo_ToolBar_00.png ) 
*FCInfo_ToolBar*

## Usage

After run the macro, go to Menu → Tools → Edit parameters \... :BaseApp/Preferences/Macros/FCMmacros/FCInfo_ToolBar

and check the info to display.

The complete info hare displayed in the ToolTip window, the checked option is visible if the \"\*\" is displayed.

Use the button reset after change one option in the parameter window.

The Unit size can be selected : km, hm, dam, m, dm, cm, mm, µm, nm, pm, fm, inch, link, foot, yard, perch, chain, furlong, mile, league, nautique.

![FCInfo_ToolBar the info toolTip](images/Macro_FCInfo_ToolBar_01.png ) 
*FCInfo_ToolBar the info toolTip*

## Options

The options are located in the Parameter of FreeCAD:

*Menu → Tools → Edit parameters \... :BaseApp/Preferences/Macros/FCMmacros/FCInfo_ToolBar*

-   ***switch_User_ToolbarIconSize***
    -   if = `False`: the icon toolBar respect the FreeCAD value for the icon size
    -   if = `True`: the icon take the values of the variable **seT_User_sizeIconX** and **seT_User_sizeIconY**

-   ***seT_User_sizeIconX***
    -   set the value X of the Icon

-   ***seT_User_sizeIconY***
    -   set the value Y of the Icon

-   ***seT_User_setFixed_Tool_Bar_Width***
    -   set the Width of the ToolBar

-   ***seT_User_setFixed_Tool_Bar_Height***
    -   set the Height of the ToolBar

-   ***switch_User_Work_With_Preselection***
    -   Work With the Preselectiond, update the data in real time

-   ***seT_User_StyleSheetColorToolBar***
    -   set the color of the toolBar in HTML format example : **#F8E6E0**
    -   if the value is **0** the toolBar take the system color

-   ***seT_User_DecimalValue***
    -   give the number of decimal of the number (Default **2**)

-   ***seT_User_TextHeigthValue***
    -   give the text height of the toolBar

-   ***switch_User_Display_objectName***
    -   display the object Name ()

-   ***switch_User_Display_SubElementName***
    -   display the SubElementName ()

-   ***switch_User_Display_ShapeType***
    -   display the Shape type (TyS:)

-   ***switch_User_Display_TypeId***
    -   display the TypeId (TyI:)

-   ***switch_User_Display_RadiusObject***
    -   display the radius and the diameter (r:) \[D:\]

-   ***switch_User_Display_LengthObject***
    -   display the Length of the edge selected or the Perimeter of the face selected
        -   (L:) display the Length of the wire, edge, line selected
        -   (P:) display the Perimeter if the face is selected

-   ***switch_User_Display_SommeAllEdgesObject***
    -   display the somme of the all edge of the object selected (Se:)

-   ***switch_User_Display_NumberFacesMesh***
    -   display the number of Faces of the Mesh object (Nf:)

-   ***switch_User_Display_NumberPointsMeshPoints***
    -   display the number of points of the Mesh object (Np:)

-   ***switch_User_Display_NumberEdgesMesh***
    -   display the number of edges of the Mesh object (Ne:)

-   ***switch_User_Display_AreaObject***
    -   display the area of the object (A:)

-   ***switch_User_Display_AreaSubObject***
    -   display the area of the face selected (Af:)

-   ***switch_User_Display_VolumeObject***
    -   display the volume of the object (V:)

-   ***switch_User_Display_BsplineObject***
    -   display the number of node of the Bspline selected
        -   (BSpline) display the number of node of the BSpline
        -   (BSrA) BSPline radius approximative first radius of the BSpline
        -   (BSS) BSPline Points Shape number points of the Bspline (case Shape)
        -   (BSc) BSPline Points Sub Object number points of sub object selected (case Edge)

-   ***switch_User_Display_CentreObject***
    -   display the center of the circle (if one circle is detected) or of the object selected
        -   (Ce:) display the center of circle (if detected), face, edge \... BBoxCenter of face, edge \... Sub selection\" + \"\\n\\n\")

-   ***switch_User_Display_CentreBoundBoxObject***
    -   display the boundingBox center of the object (BBCe:)

-   ***switch_User_Display_Position***
    -   display the coordinates point mouse pointed (Pos:)

-   ***switch_User_NotInfoOnBeginning***
    -   if it is `False` the info (this information) is displayed
    -   if it is `True` the info is not displayed

-   ***seT_User_UnitSymbolSquare***
    -   give the symbol square (Default **2**)

-   ***seT_User_UnitSymbolCube***
    -   give the symbol cube (Default **3**)

-   ***seT_User_UnitSymbolMicro***
    -   give the symbol micro (Default **u**)

## For automatic Run 

#### in command line 

In your shortcut *verify your right path*

\"Complete_path_of_FreeCAD\" \"Complete_path_of_the_macro.FCMacro\"

example:


```python
"C:/FreeCAD_0.20.26858_Win-LPv12.5.4_vc17.x-x86-64/bin/FreeCAD.exe" "C:/Users/User/AppData/Roaming/FreeCAD/Macro/FCInfo_ToolBar.FCMacro"
```

#### in Mod directory 

1.  After install the macro with [Addon Manager](Std_AddonMgr.md)
2.  Create the *FCInfo_ToolBar* directory
3.  Copy the macro FCInfo_ToolBar.FCMacro (copy not move) in the *FCInfo_ToolBar* directory and rename it in FCInfo_ToolBar.py
4.  Create a file named InitGui.py
5.  Paste the code in InitGui.py:


```python
#### FC Version: 0.1 #16/02/2022
#### Mario52
#### FCInfo_ToolBar : mini FCInfo ####
#
import importlib
from importlib import reload
import FreeCAD, FreeCADGui
App = FreeCAD
Gui = FreeCADGui


switch_User_NotRunAuto = FreeCAD.ParamGet("User parameter:BaseApp/Preferences/Macros/FCMmacros/FCInfo_ToolBar").GetBool("switch_User_NotRunAuto")
## switch_User_NotRunAuto 0 (False) = run the macro in begin
## switch_User_NotRunAuto 1 (True)  = not run automatic the macro


if switch_User_NotRunAuto == False:
    import FCInfo_ToolBar
    #reload(FCInfo_ToolBar)
    FreeCAD.ParamGet("User parameter:BaseApp/Preferences/Macros/FCMmacros/FCInfo_ToolBar").SetBool("switch_User_NotRunAuto", False)
    #FreeCAD.Console.PrintMessage("InitGui Ok FCInfo_ToolBar" + "\n")
```

1.  save the file
2.  run FreeCAD
3.  if the macro not run (normal) execute the macro FCInfo_ToolBar.FCMacro as a normal macro
4.  the next start of FreeCAD the macro must start automatically

enjoy

## Link

The forum discussion [Feature request: coordinates display](https://forum.freecadweb.org/viewtopic.php?f=8&t=66294)

## Version

version 00.04 28/06/2023 : correction styleSheet and:


```python
                        sommeEdgesSTR = str(sommeEdges)
```

replaced by: 
```python
                        sommeEdgesSTR = str(round(sommeEdges * uniteM, seT_User_DecimalValue)) + " " + uniteMs
```

version: (00.02 +) 00.03 2022/03/22 : add somme all edges

version: 00.02 2022/03/14 : add calcul in real time (with preselection), dimension of toolBar, add info mesh and points

version: 00.01 2022/02/16 :



---
![](images/Right_arrow.png) [documentation index](../README.md) > Macro FCInfo ToolBar/pl
