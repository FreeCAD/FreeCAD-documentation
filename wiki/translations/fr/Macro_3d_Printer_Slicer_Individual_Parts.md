# Macro 3d Printer Slicer Individual Parts/fr
{{Macro/fr
|Name=Macro 3d Printer Slicer Individual Parts
|Name/fr=Macro 3d Printer Slicer Individual Parts
|Icon=Macro_3d_Printer_Slicer_Individual_Parts.svg
|Description=Exportation vers un logiciel de découpage pour imprimantes 3D basé sur une macro similaire par cae2100. Exporte un seul fichier stl pour chaque partie visible dans le même répertoire que le fichier de dessin original, puis l'ouvre dans le logiciel de découpage. <br/> Ce code, lorsqu'il est exécuté, exporte le dessin actuellement ouvert vers plusieurs fichiers STL, nommés d'après les étiquettes des pièces et ouvrez-le dans le logiciel de découpage que vous utilisez. La macro recherche '' '[http://wiki.ultimaker.com/Cura Cura]' '' dans le chemin mais vous pouvez ajouter tout autre découpage en modifiant la chaîne dans la macro.
|Author=WayofWood
|Version=1.1
|Date=2020-10-30
|FCVersion=All
|Download=[https://wiki.freecadweb.org/images/3/3d/Macro_3d_Printer_Slicer_Individual_Parts.svg ToolBar Icon]
|SeeAlso=[Macro 3d Printer Slicer](Macro_3d_Printer_Slicer/fr.md) <img src="images/Macro_3d_Printer_Slicer.png" width=24px>
}}

## Description

Ce code, lorsqu\'il est exécuté, exportera les corps visibles au niveau supérieur (les corps plus profonds dans l\'arborescence seront ignorés) de la conception actuellement ouverte vers des fichiers STL individuels, et les ouvrira dans le logiciel de découpage que vous utilisez. Cette macro recherchera **[Cura](http://wiki.ultimaker.com/Cura)** comme valeur par défaut, mais vous pouvez la remplacer par n\'importe quel autre curseur en modifiant la variable SLICERAPP dans le code source.

Il est préférable de l\'utiliser en créant un lien vers la macro dans la barre d\'outils, et lorsque vous êtes prêt à découper l\'objet, cliquez simplement dessus et vos objets, tels qu\'ils apparaissent à l\'écran dans FreeCAD apparaîtront sur l\'interface de votre logiciel de découpage, prêts à découper. Il créera également plusieurs fichiers STL avec le même nom de fichier que le fichier de conception et l\'étiquette de pièce dans le même répertoire que le fichier de conception.

<img alt="" src=images/Screenshot_Cura_Example.png  style="width:480px;">

## Script

La variable SLICERAPP peut être remplacée par n\'importe quel logiciel de découpage de votre choix. Si un objet spécifique n\'est pas exporté, vous devrez peut-être ajouter le type correspondant au tableau doexport.

ToolBar Icon <img alt="" src=images/Macro_3d_Printer_Slicer_Individual_Parts.svg  style="width:64px;">

**Macro\_3d\_Printer\_Slicer\_Individual\_Parts.py**


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

Merci à cae2100 pour le développement du code macro d\'origine - [également disponible ici](Macro_3d_Printer_Slicer/fr.md).
Merci à [Wmayer](http://forum.freecadweb.org/viewtopic.php?f=10&t=4686) pour son aide dans l\'écriture de ce script.
Original forum topic: <http://forum.freecadweb.org/viewtopic.php?f=10&t=4686>

---
[documentation index](../README.md) > Macro 3d Printer Slicer Individual Parts/fr
