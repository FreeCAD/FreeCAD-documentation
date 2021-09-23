# Macro 3d Printer Slicer/it
 {{Macro/it
|Name=Macro_3d_Printer_Slicer
|Icon=Macro_3d_Printer_Slicer.png
|Translate=Slicer per stampanti 3D
|Description=Esporta verso il software slicer per stampanti 3D. Esporta il file stl nella stessa directory del file originale del disegno, poi lo apre con il software di analisi.
|Author=cae2100
|Version=1.0
|Date=2013-10-10
|FCVersion=All
|Download=[https://www.freecadweb.org/wiki/images/9/96/Macro_3d_Printer_Slicer.png ToolBar Icon]
|SeeAlso=[Macro 3d Printer Slicer Individual Parts](Macro_3d_Printer_Slicer_Individual_Parts/it.md) <img src="images/Macro_3d_Printer_Slicer_Individual_Parts.svg" width=24px>
}}

## Descrizione

Questo codice esporta il progetto attivo in un file STL, e lo apre con il software di analisi preferito. Questo esempio è adatto a **[KISSlicer](http://kisslicer.com/)**, ma può essere modificato e utilizzato con **[Slic3r](http://slic3r.org/)**, **[Cura](http://wiki.ultimaker.com/Cura)**, o qualsiasi altro software per stampanti 3d. Può anche essere leggermente modificato per essere aperto dai software CAM per macchine CNC (a controllo numerico).

È meglio creare prima un collegamento nella barra degli strumenti che punti alla macro poi, quando si è pronti per analizzare l\'oggetto, fare clic su di esso per far apparire l\'oggetto nell\'interfaccia del software di analisi, così come appare nello schermo di FreeCAD e pronto per essere analizzato. Inoltre, è possibile creare un file STL con lo stesso nome del file del progetto e nella stessa directory del file originale, come backup.

<img alt="" src=images/Macro_3d_Printer_Slicer_00.png  style="width:480px;">

## Script

La variabile SLICER può essere cambiata a piacere per adattare il codice a qualsiasi software di analisi, basta accertarsi di impostarla, prima di eseguire lo script altrimenti si riceve un messaggio di errore.

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

## Ringraziamenti

Grazie a [Wmayer](http://forum.freecadweb.org/viewtopic.php?f=10&t=4686) per il suo aiuto nella stesura di questo script.

Discussione nel forum : <https://forum.freecadweb.org/viewtopic.php?f=10&t=4686> 
