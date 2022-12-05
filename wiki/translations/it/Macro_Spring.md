# Macro Spring/it
{{Macro/it
|Name=Spring Simul
|Icon=Macro_Spring.png
|Translate=Spring Simul
|Description=Simula il movimento di una molla.
|Author=Mario52
|Version=1.0
|Date=2014-09-29
|FCVersion=All
|Download=The file [http://forum.freecadweb.org/download/file.php?id=7679 Spring.FCStd]<br />[https://www.freecadweb.org/wiki/images/2/2d/Macro_Spring.png ToolBar Icon]
}}

## Descrizione

Simula la compressione e la distensione di una molla.

![](images/Spring_00.gif )

## Uso

Per eseguire la macro aprire in FreeCAD i 2 file indicati sotto (Spring.FCMacro e Spring.FCStd) con 2 schermi (Menu: Finestre → Affiancate) poi fare clic nella finestra e nella macro fare clic su **F6** (avvia macro), oppure avviare la macro con ![](images/Std_DlgMacroExecuteDirect.svg )

<img alt="" src=images/Spring_02.png  style="width:300px;">

## Il File 

[Spring.FCStd](http://forum.freecadweb.org/download/file.php?id=7679)

## Lo Script 

ToolBar Icon ![](images/Macro_Spring.png )

**Spring.FCMacro**


{{MacroCode|code=
import FreeCAD, FreeCADGui, Draft, Part
from FreeCAD import Base
import time

ii = iib = FreeCAD.getDocument("Spring").getObject("Helix001").Pitch.Value
i = ib = FreeCAD.getDocument("Spring").getObject("Helix001").Height.Value

pas = 1

for ii2 in range(int(60)):
    if pas == 0:
        if ii > iib-1:
            pas = 1
        else:
            ii += 1
            i = (ii * 10)
    else:
        if ii < 2:
            pas = 0
        else:
            ii -= 1
            i = (ii * 10)
   
    FreeCAD.getDocument("Spring").getObject("Helix001").Pitch = ii
    FreeCAD.getDocument("Spring").getObject("Helix001").Height = i
    App.Console.PrintMessage(str(ii2)+"  " + str(ii)+"  " + str(i)+"  " + str(pas) +"\n")
    Gui.updateGui()
    time.sleep(0.1)
    
}}

## Link

La pagina della discussione nel forum: [scripting animations](http://forum.freecadweb.org/viewtopic.php?f=22&t=7449#p62193)



---
![](images/Right_arrow.png) [documentation index](../README.md) > Macro Spring/it
