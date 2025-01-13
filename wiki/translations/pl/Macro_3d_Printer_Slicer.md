# Macro 3d Printer Slicer/pl
{{Macro/pl
|Name=Macro_3d_Printer_Slicer
|Translate=Makrodefinicja: 3d Printer Slicer
|Icon=Macro_3d_Printer_Slicer.png
|Description=Umożliwia eksport do oprogramowania do cięcia dla drukarek 3D. Eksportuje plik stl do tego samego katalogu co oryginalny plik projektu, a następnie otwiera go w oprogramowaniu do cięcia.<br/>Kod ten, po uruchomieniu, wyeksportuje aktualnie otwarty projekt do pliku STL i otworzy go w używanym oprogramowaniu do cięcia. Przykład ten jest przeznaczony dla '''[http://kisslicer.com/ KISSlicer]''', ale można go zmodyfikować, aby używać '''[http://slic3r.org/ Slic3r]''', '''[http://wiki.ultimaker.com/Cura Cura]''' lub dowolnego innego oprogramowania do drukarek 3D. Można go również nieznacznie zmodyfikować, aby otworzyć oprogramowanie CAM dla maszyn CNC. 
|Author=cae2100
|Version=1.0
|Date=2013-10-10
|FCVersion=wszystkie
|Download=[https://www.freecadweb.org/wiki/images/9/96/Macro_3d_Printer_Slicer.png ToolBar Icon]
|SeeAlso=[Makro 3d Printer Slicer Individual Parts](Macro_3d_Printer_Slicer_Individual_Parts/pl.md) <img src="images/Macro_3d_Printer_Slicer_Individual_Parts.svg" width=24px>
}}

## Opis

Ten kod, po uruchomieniu, wyeksportuje aktualnie otwarty projekt do pliku STL i otworzy go w używanym oprogramowaniu do krojenia. Ten przykład dotyczy **[KISSlicer](http://kisslicer.com/)**, ale można go zmodyfikować tak, aby używał **[Slic3r](http://slic3r.org/)**, **[Cura](http://wiki.ultimaker.com/Cura)** lub dowolnego innego oprogramowania do drukarek 3D. Można go również nieznacznie zmodyfikować, aby otworzyć oprogramowanie CAM dla maszyn CNC.

Najlepiej używać go poprzez utworzenie linku do makra na pasku narzędzi, a gdy będziesz gotowy do cięcia obiektu, po prostu kliknij go, a obiekt, tak jak pojawia się na ekranie w FreeCAD, pojawi się w interfejsie oprogramowania do cięcia, gotowy do cięcia. Zostanie również utworzony plik STL o tej samej nazwie co plik projektu w tym samym katalogu co plik projektu jako kopia zapasowa.

<img alt="" src=images/Macro_3d_Printer_Slicer_00.png  style="width:480px;">

## Skrypt

Zmienna SLICER może zostać zmieniona na dowolny wybrany program do krojenia, po prostu upewnij się, że ustawiłeś ją przed uruchomieniem, w przeciwnym razie skrypt zgłosi błąd.

ToolBar Icon ![](images/Macro_3d_Printer_Slicer.png )

**Macro_3d_Printer_Slicer.py**


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

## Podziękowania

Dziękujemy użytkownikowi [Wmayer](http://forum.freecadweb.org/viewtopic.php?f=10&t=4686) za pomoc w napisaniu tego skryptu.
Oryginalny temat na forum: <http://forum.freecadweb.org/viewtopic.php?f=10&t=4686>



---
⏵ [documentation index](../README.md) > Macro 3d Printer Slicer/pl
