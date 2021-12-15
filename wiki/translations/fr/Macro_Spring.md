# Macro Spring/fr
{{Macro/fr
|Name=Spring Simul
|Icon=Macro_Spring.png
|Description=Simulation de la compression/décompression d'un ressort.
|Author=Mario52
|Version=1.0
|Date=2014-09-29
|FCVersion=All
|Download=The file [http://forum.freecadweb.org/download/file.php?id=7679 Spring.FCStd]<br />[https://www.freecadweb.org/wiki/images/2/2d/Macro_Spring.png ToolBar Icon]
}}

## Description

Simule la compression et la décompression d\'un ressort.

![](images/Spring_00.gif )

## Utilisation

Ouvrir les deux fichiers ci-dessous (Spring.FCMacro et Spring.FCStd) dans FreeCAD avec deux fenêtres (menu Fenêtre → Mosaïque), cliquer dans la fenêtre et sur la macro puis faire **F6** (Déboguer la macro) pour exécuter la macro ou la lancer avec le bouton ![](images/Std_DlgMacroExecuteDirect.svg ).

<img alt="" src=images/Spring_02.png  style="width:300px;">

## Fichier

[Spring.FCStd](http://forum.freecadweb.org/download/file.php?id=7679)

## Script

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

## Liens

La discussion du forum (en anglais) : [scripting animations](http://forum.freecadweb.org/viewtopic.php?f=22&t=7449#p62193)

---
[documentation index](../README.md) > Macro Spring/fr
