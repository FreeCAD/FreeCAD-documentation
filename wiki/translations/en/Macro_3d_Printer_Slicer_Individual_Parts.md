# Macro 3d Printer Slicer Individual Parts/en
{{Macro
|Name=Macro 3d Printer Slicer Individual Parts
|Icon=Macro_3d_Printer_Slicer_Individual_Parts.svg
|Description=Export to slicing software for 3D printers based on a similar macro by cae2100. Exports a single stl file for each visible part in the same directory as original design file, then opens it in slicing software.<br/>This code, when run, will export the currently open design to several STL files, named after the labels of the parts, and open it in the slicing software that you use. The macro is searching for '''[http://wiki.ultimaker.com/Cura Cura]''' in the path but you can add any other slicing by changing the string in the macro.  
|Author=WayofWood
|Version=1.1
|Date=2020-10-30
|FCVersion=All
|Download=[https://wiki.freecadweb.org/images/3/3d/Macro_3d_Printer_Slicer_Individual_Parts.svg ToolBar Icon]
|SeeAlso=[Macro 3d Printer Slicer](Macro_3d_Printer_Slicer.md) <img src="images/Macro_3d_Printer_Slicer.png" width=24px>
}}

## Description

This code, when run, will export the visible bodies at the top level (bodies deeper in the tree will be ignored) of the currently open design to individual STL files, and open them it in the slicing software that you use. This macro will look for **[Cura](http://wiki.ultimaker.com/Cura)** as the default but you can change it to any other slider by changing the SLICERAPP variable in the source code.

It is best used by creating a link to the macro on the toolbar, and when your ready to slice the object, just click it and your objects, as they appear on the screen in FreeCAD will appear on your slicing software\'s interface, ready to slice. It will also create several STL files with the same filename as the design file and the part label in the same directory as the design file.

<img alt="" src=images/Screenshot_Cura_Example.png  style="width:480px;">

## Script

The SLICERAPP variable can be changed to any slicing software of your choosing. If a specific object is not exported you might have to add the respective type to the doexport array.

ToolBar Icon <img alt="" src=images/Macro_3d_Printer_Slicer_Individual_Parts.svg  style="width:64px;">

**Macro_3d_Printer_Slicer_Individual_Parts.py**


{{MacroCode|code=
import FreeCAD
import Mesh
import sys
import math
import os
import subprocess

SLICERAPP= "cura"                   # Put your Slicer program here

# some fuctions
def getPlacement(quat,vect,obj):
  if quat[3] > -1  and quat[3] < 1:
    delta = math.acos(quat[3])*2.0
    scale = math.sin(delta/2)
    rx = quat[0]/scale
    ry = quat[1]/scale
    rz = quat[2]/scale
  else:
    delta = 0
    rx = 0
    ry = 0
    rz = 1
  info0 = "translation "+str(vect.x)+" "+str(vect.y)+" "+str(vect.z)
  info1 = "rotation "+str(rx)+" "+str(ry)+" "+str(rz)+" "+str(delta)
  return info0+" "+info1
# some definitions
placement = App.Placement(App.Vector(0,0,0),App.Rotation(0,0,0,1))
# user need to set this directory where slicing software is located
OutDir = FreeCAD.ActiveDocument.FileName.replace(".FCStd", "--")
visible_objs = []
# Get Objects in document
doc = App.ActiveDocument
objs = doc.Objects
stlFile = ""
stlFiles = [ SLICERAPP ]
# hide all
for obj in objs:
   print(obj.Label + "//" + obj.TypeId)
   print(len(obj.InList))
   if obj.ViewObject.isVisible() and hasattr(obj, 'Shape') and (len(obj.InList) <= 1):
      visible_objs.append(obj)
for obj in visible_objs:
  stlFile = OutDir+str(obj.Label)+".stl"
  Mesh.export([obj],stlFile)
  stlFiles.append(stlFile)
  print ("Exporting " + stlFile + "\n")
print ("Calling subprocess: " + str(stlFiles)+"\n")
subprocess.Popen(stlFiles)
}}

## Credits

Thanks to cae2100 for developing the original macro code - [also available here](Macro_3d_Printer_Slicer.md).
Thanks to [Wmayer](http://forum.freecadweb.org/viewtopic.php?f=10&t=4686) for his help in writing this script.
Original forum topic: <http://forum.freecadweb.org/viewtopic.php?f=10&t=4686>



---
![](images/Button_right.svg) [documentation index](../README.md) > Macro 3d Printer Slicer Individual Parts/en
