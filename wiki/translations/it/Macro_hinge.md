 {{Macro/it
|Name=Hinge Simul
|Icon=Macro hinge.png
|Translate=Hinge Simul
|Description=Simula il movimento di una cerniera.
|Author=Mario52
|Version=1.0
|Date=2014-09-09
|FCVersion=All
|Download=The File [http://forum.freecadweb.org/download/file.php?id=7628 20140908b_Hinge-1.fcstd]<br />[https://www.freecadweb.org/wiki/images/a/a8/Macro_hinge.png ToolBar Icon]
}}

## Descrizione

Simula il movimento di una cerniera di una porta.

![](images/Hing_00.gif )

## Uso

Per eseguire la macro aprire in FreeCAD i 2 file (20140908b\_Hinge-1.FCMacro e 20140908b\_Hinge-1.FCStd) in 2 schermi (Menu: Finestre -\> Affiancate) poi fare clic nella finestra e nella macro fare clic su F6 (avvia macro), oppure avviare la macro con ![](images/Std_DlgMacroExecuteDirect.svg )

<img alt="" src=images/Hing_01.png  style="width:300px;">

## Il File {#il_file}

[20140908b\_Hinge-1.fcstd](http://forum.freecadweb.org/download/file.php?id=7628)

## Lo Script {#lo_script}

ToolBar Icon ![](images/Macro_hinge.png )

**20140908b\_Hinge-1.FCMacro**


{{MacroCode|code=
import FreeCAD, FreeCADGui, Draft, Part
from FreeCAD import Base
import time

ii = 0
pas = 0
for ii2 in range(180):
    if pas == 0:
        if ii > 90:
            pas = 1
        ii += 5
    else:
        if ii < 1:
            pas = 0
        ii -= 5
   
    App.getDocument("_0140908b_Hinge_1").Fusion.Placement=App.Placement(App.Vector(0,0,0), App.Rotation(App.Vector(0,0,1),ii), App.Vector(44.4,6.9,0))
    App.Console.PrintMessage(str(ii2)+"  " + str(ii)+"  " + str(pas) +"\n")
    Gui.updateGui()
    time.sleep(0) #modify the time here

}}

## Link

La pagina della discussione: [Struggling with LinearPattern (again)](http://forum.freecadweb.org/viewtopic.php?f=3&t=7606&p=62086#p62086) 
