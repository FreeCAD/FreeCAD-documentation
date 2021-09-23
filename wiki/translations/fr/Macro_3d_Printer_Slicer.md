# Macro 3d Printer Slicer/fr
 {{Macro/fr
|Name=Macro_3d_Printer_Slicer
|Icon=Macro_3d_Printer_Slicer.png
|Description=Exporter le projet dans un logiciel de tranchage pour utilisation dans une imprimantes 3D. Exporte le fichier stl dans le même répertoire que fichier original, puis l'ouvre dans le logiciel de tranchage.
|Author=cae2100
|Version=1.0
|Date=2013-10-10
|FCVersion=All
|Download=[https://www.freecadweb.org/wiki/images/9/96/Macro_3d_Printer_Slicer.png ToolBar Icon]
|SeeAlso=[Macro 3d Printer Slicer Individual Parts](Macro_3d_Printer_Slicer_Individual_Parts/fr.md) <img src="images/Macro_3d_Printer_Slicer_Individual_Parts.svg" width=24px>
}}

## Description

Copiez le code suivant, lorsqu\'il est exécuté, il exporte le projet en fichier .STL pour l\'ouvrir dans le logiciel de découpage en tranches que vous utilisez. Cet exemple est écrit pour le logiciel **[KISSlicer](http://kisslicer.com/)**, mais peut être modifié pour être utilisé avec **[Slic3r](http://slic3r.org/)**, **[Cura](http://wiki.ultimaker.com/Cura)** ou tout autre logiciel pour imprimante 3d. Il peut également être légèrement modifié pour être ouvert dans un logiciel de FAO pour machines CNC.

Il est préférable de créer un lien dans la barre d\'outils qui pointe vers la macro, quand vous êtes prêt à trancher l\'objet, cliquez simplement sur le bouton et votre objet sera affiché sur l\'interface de votre logiciel de tranchage, tel qu\'il apparaît dans l\'écran de FreeCAD et prêt à être tranché. Il créera également un fichier .STL avec le même nom et dans le même répertoire que le fichier original.

<img alt="" src=images/Macro_3d_Printer_Slicer_00.png  style="width:480px;">

## Script

Le script peut être modifiés pour être utilisé avec n\'importe quel logiciel de tranchage de votre choix, assurez-vous juste de modifier le script avant de l\'exécuter, ou une erreur d\'exécution de script sera signalée.

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

Merci à [Wmayer](http://forum.freecadweb.org/viewtopic.php?f=10&t=4686) pour son aide dans la rédaction de ce script. 
