# Macro 3d Printer Slicer/de
{{Macro/de
|Name=Macro_3d_Printer_Slicer
|Icon=Macro_3d_Printer_Slicer.png
|Translate=Macro_3d_Printer_Slicer
|Description=Export in Slicing-Software für 3D-Drucker. Exportiert die STL-Datei in das gleiche Verzeichnis wie die ursprüngliche Designdatei und öffnet sie dann in Slicing-Software.<br/>Beim Ausführen wird dieser Code das aktuelle Design in eine STL-Datei und sie in der verwendeten Slicing-Software öffnen. Dieses Beispiel ist für '''[http://kisslicer.com/ KISSlicer]''', kann aber für '''[http://slic3r.org/ Slic3r]''', '''[http://wiki.ultimaker.com/Cura Cura]''', oder jede andere 3D-Drucker-Software angepasst werden. Er kann auch geringfügig angepasst werden, um CAM-Software für CNC-Maschinen zu öffnen.
|Author=cae2100
|Version=1.0
|Date=2013-10-10
|FCVersion=Alle
|Download=[https://www.freecadweb.org/wiki/images/9/96/Macro_3d_Printer_Slicer.png ToolBar Icon]
|SeeAlso=[Macro 3D-Drucker-Slicer Individuelle Teile](Macro_3d_Printer_Slicer_Individual_Parts.md) <img src="images/Macro_3d_Printer_Slicer_Individual_Parts.svg" width=24px>
}}

## Beschreibung

Wenn dieser Code ausgeführt wird, wird der derzeit geöffnete Entwurf in eine STL-Datei exportiert und in der von Ihnen verwendeten Slicing-Software geöffnet. Dieses Beispiel ist für **[KISSlicer](http://kisslicer.com/)**, kann aber zur Verwendung geändert werden **[Slic3r](http://slic3r.org/)**, **[Cura](http://wiki.ultimaker.com/Cura)**, oder eine andere 3D-Druckersoftware. Sie kann auch leicht modifiziert werden, um die CAM-Software für CNC-Maschinen zu öffnen.

Es wird am besten durch Erstellen eines Links zu dem Makro in der Symbolleiste verwendet. Wenn Sie zum Schneiden des Objekts bereit sind, klicken Sie einfach darauf. Das Objekt wird in FreeCAD auf dem Bildschirm angezeigt und erscheint auf der Benutzeroberfläche der Slicing-Software . Außerdem wird eine STL-Datei mit demselben Dateinamen wie die Designdatei in demselben Verzeichnis wie die Designdatei als Sicherung erstellt.

<img alt="" src=images/Macro_3d_Printer_Slicer_00.png  style="width:480px;">

## Skript

Die SLICER-Variable kann in eine beliebige Slicing-Software Ihrer Wahl geändert werden. Vergewissern Sie sich, dass Sie die Variable gesetzt haben, bevor Sie sie ausführen, oder es wird ein Fehler im Skript angezeigt.

ToolBar Icon ![](images/Macro_3d_Printer_Slicer.png )

**Macro\_3d\_Printer\_Slicer.py**


{{MacroCode|code=
import FreeCAD
import Mesh
import sys
import math
import os
import subprocess
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
OutDir = FreeCAD.ActiveDocument.FileName.replace(FreeCAD.ActiveDocument.Label + ".fcstd", "")
visible_objs = []
SLICER = "/kisslicer location/"                          # Put your Slicer program location here
os.chdir(SLICER)
# Get Objects in document
doc = App.ActiveDocument
objs = doc.Objects
# hide all
for obj in objs:
   if obj.ViewObject.isVisible():
      visible_objs.append(obj)
for obj in visible_objs:
  # get volume
  volume = obj.Shape.Volume
  # get Rotation and translation of volume
  quat = obj.Placement.Rotation.Q
  vect = obj.Placement.Base
  pinfo = getPlacement(quat,vect,obj)
  # reset placement, export it and set at original placement
  oldPlacement = obj.Placement
  obj.Placement = placement
  obj.Placement = oldPlacement   
stlFile = OutDir+str(doc.Label)+".stl"
Mesh.export(visible_objs,stlFile)
subprocess.Popen([SLICER + "KISSlicer", stlFile])
}}

## Credits

Dank an [Wmayer](http://forum.freecadweb.org/viewtopic.php?f=10&t=4686) für seine Hilfe beim Schreiben dieses Skripts.
Ursprüngliches Forumsthema: <http://forum.freecadweb.org/viewtopic.php?f=10&t=4686>

---
[documentation index](../README.md) > Macro 3d Printer Slicer/de
