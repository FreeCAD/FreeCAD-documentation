 {{Macro/de
|Name=Simuliert Scharnierbewegung
|Icon=Macro hinge.png
|Description=Scharnier Simulation.
|Author=Mario52
|Version=1.0
|Date=2014-09-09
|FCVersion=Alle
|Download=Die Datei [http://forum.freecadweb.org/download/file.php?id=7628 20140908b_Hinge-1.fcstd]<br />[https://www.freecadweb.org/wiki/images/a/a8/Macro_hinge.png ToolBar Symbol]
}}

## Beschreibung

Simuliert Scharnierbewegung

![](images/Hing_00.gif )

## Verwendet

Öffne die 2 Dateien (20140908b\_Hinge-1.FCMacro und 20140908b\_Hinge-1.FCStd) in FreeCAD mit 2 Bildschirmen (Menü: Fenster \> Kacheln) und klicke in das Fenster und das Makro und klicke F6 (Makro debuggen), um das Makro auszuführen oder führe das Makro mit ![](images/Std_DlgMacroExecuteDirect.svg ) aus

<img alt="" src=images/Hing_01.png  style="width:300px;">

## Die Datei {#die_datei}

[20140908b\_Hinge-1.fcstd](http://forum.freecadweb.org/download/file.php?id=7628)

## Skript

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

## Verweis

Die Diskussionsseite [Probleme mit LinearMustern (wiederholt)](http://forum.freecadweb.org/viewtopic.php?f=3&t=7606&p=62086#p62086) 
