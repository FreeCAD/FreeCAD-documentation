# Macro 3d Printer Slicer Individual Parts/it
{{Macro/it
|Name=Macro 3d Printer Slicer Individual Parts
|Name/it=Macro 3d Printer Slicer Individual Parts
|Icon=Macro_3d_Printer_Slicer_Individual_Parts.svg
|Description=Esporta in un software di slicing per stampanti 3D basato su una macro simile di cae2100. Esporta un singolo file STL per ogni parte visibile nella stessa directory del file di disegno originale, quindi lo apre nel software di slicing. <br/> Questo codice, una volta eseguito, esporterà il disegno attualmente aperto in diversi file STL, denominati in base alle etichette delle parti e aprirlo nel software di slicing che utilizzi. La macro sta cercando '' '[http   *//wiki.ultimaker.com/Cura Cura]' '' nel percorso ma è possibile aggiungere qualsiasi altra suddivisione modificando la stringa nella macro.
|Author=WayofWood
|Version=1.1
|Date=2020-10-30
|FCVersion=All
|Download=[https   *//wiki.freecadweb.org/images/3/3d/Macro_3d_Printer_Slicer_Individual_Parts.svg ToolBar Icon]
|SeeAlso=[Macro 3d Printer Slicer](Macro_3d_Printer_Slicer/it.md) <img src="images/Macro_3d_Printer_Slicer.png" width=24px>
}}

## Descrizione

Questo codice, quando viene eseguito, esporterà i corpi visibili al livello superiore (i corpi più in profondità nell\'albero verranno ignorati) del progetto attualmente aperto in singoli file STL e li aprirà nel software di slicing che usi. Questa macro cercherà **[Cura](http   *//wiki.ultimaker.com/Cura)** come impostazione predefinita, ma puoi cambiarla con qualsiasi altro cursore modificando la variabile SLICERAPP nel codice sorgente.

Viene utilizzato al meglio creando un collegamento alla macro sulla barra degli strumenti e quando sei pronto per tagliare l\'oggetto, fai clic su di esso e gli oggetti, come appaiono sullo schermo in FreeCAD, appariranno sull\'interfaccia del tuo software di taglio, pronti per tagliare . Creerà anche diversi file STL con lo stesso nome file del file di disegno e l\'etichetta della parte nella stessa directory del file di disegno.

<img alt="" src=images/Screenshot_Cura_Example.png  style="width   *480px;">

## Script

La variabile SLICERAPP può essere modificata in qualsiasi software di slicing di tua scelta. Se un oggetto specifico non viene esportato, potrebbe essere necessario aggiungere il rispettivo tipo all\'array doexport.

ToolBar Icon <img alt="" src=images/Macro_3d_Printer_Slicer_Individual_Parts.svg  style="width   *64px;">

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
def getPlacement(quat,vect,obj)   *
  if quat[3] > -1  and quat[3] < 1   *
    delta = math.acos(quat[3])*2.0
    scale = math.sin(delta/2)
    rx = quat[0]/scale
    ry = quat[1]/scale
    rz = quat[2]/scale
  else   *
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
for obj in objs   *
   print(obj.Label + "//" + obj.TypeId)
   print(len(obj.InList))
   if obj.ViewObject.isVisible() and hasattr(obj, 'Shape') and (len(obj.InList) <= 1)   *
      visible_objs.append(obj)
for obj in visible_objs   *
  stlFile = OutDir+str(obj.Label)+".stl"
  Mesh.export([obj],stlFile)
  stlFiles.append(stlFile)
  print ("Exporting " + stlFile + "\n")
print ("Calling subprocess   * " + str(stlFiles)+"\n")
subprocess.Popen(stlFiles)
}}

## Crediti

Grazie a cae2100 per aver sviluppato il codice macro originale - [also available here](Macro_3d_Printer_Slicer/it.md).
Thanks to [Wmayer](http   *//forum.freecadweb.org/viewtopic.php?f=10&t=4686) for his help in writing this script.
Original forum topic   * <http   *//forum.freecadweb.org/viewtopic.php?f=10&t=4686>



---
![](images/Right_arrow.png) [documentation index](../README.md) > Macro 3d Printer Slicer Individual Parts/it
