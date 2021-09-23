# Macro ObjectInfo
{{Macro
|Name=Macro ObjectInfo
|Description=This WorkBench lets you know the volume information surface area, center of mass and moment of intertia of the selected object.
|Author=keithsloan52
|Version=1.0
|Date=2012-11-09
|FCVersion=Until 0.17 '''and PyQt4'''
|Download=This is not a macro but one WorkBench, uncompress the .zip file and paste the complete directory in the Mod user directory [https://github.com/KeithSloan/FreeCAD_Info/archive/master.zip Info]
|SeeAlso=<img src=images/Arch_Survey.svg style="width:Arch Survey|24px"> [Arch Survey](Arch_Survey.md)
}}

## Description

This WorkBench lets you know the volume information surface area, center of mass and moment of intertia of the selected object.

<img alt="" src=images/ObjectInfoIt.png  style="width:480px;">

## Installation

If you\'re on Linux, you need to create a folder named \"Mod\" in the .FreeCAD hidden folder which is located in your Home folder. Then create a folder named \"Info\" in the \"Mod\" folder, and extract the content of the archive in it. On Windows, I have no idea where that would be. Use the same procedure to Windows in C:\\Program Files\\FreeCAD\\Mod.

## Usage

Then start FreeCAD, open your STEP file and switch to the \"Info\" workbench with the workbench switcher or by going to the View → Workbench menu. Now select your solid, and click on the \"Info\" icon; the left taskbar will show some information on the model, including volume, surface area, center of mass and moment of intertia.

## Code

 {{MacroCode|code=
import webbrowser 

##########
# WorkBenche
# Code used to download the zip file from FreeCAD
##########

FreeCAD.Console.PrintMessage("\n" + "You must download the Info.zip file in the author github KeithSloan/FreeCAD_Infosite" + "\n")
FreeCAD.Console.PrintMessage("http://keithsloan.dynu.com/Keith&Jenny/" + "\n")
webbrowser.open("https://github.com/KeithSloan/FreeCAD_Info/archive/master.zip")

}}

## Links

A FreeCAD user created a user-friendly \"Info\" module which you can get here: <http://www.sloan-home.co.uk/FreeCAD/Info/Info.html>

From Forum [Info Workbench - Help with icons please.](http://forum.freecadweb.org/viewtopic.php?f=10&t=3185)

---
[documentation index](../README.md) > Macro ObjectInfo
