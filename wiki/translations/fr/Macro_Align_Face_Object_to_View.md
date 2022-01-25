# Macro Align Face Object to View/fr
{{Macro/fr
|Name=Macro Align Face Object to View
|Icon=Macro_Align_Face_Object_to_View.png
|Description=Cette macro dirige la face de l'objet sur la face de la vue active.
|Author=Mario52
|Version=0.1
|Date=2015-01-16
|Download=[https://www.freecadweb.org/wiki/images/d/d5/Macro_Align_Face_Object_to_View.png ToolBar Icon]
|FCVersion=Toutes
|SeeAlso=[32px|FCCamera](File:FCCamera_00.png.md) [Macro_FCCamera](Macro_FCCamera/fr.md)
}}

## Description

Cette macro dirige la face de l\'objet sur la face de la vue active (caméra). Dans le cas de la face d\'un perçage (ou interne ou cylindre), face à l\'écran.

## Utilisation

-   Sélectionnez une face de votre objet et lancez la macro.
-   Votre sélection fait face à l\'écran.

## Script

Icône de la barre d\'outils ![](images/Macro_Align_Face_Object_to_View.png )

**Macro\_Align\_Face\_Object\_to\_View.FCMacro**


{{MacroCode|code=
# This macro directs the face of the object on the side of the ActiveView (camera)
# extact FCCamera
# 16/01/2015

__title__="Macro_Align_Face_Object_to_View"
__author__ = "Mario52"

import pivy
from pivy import coin

try:
    v=Gui.Selection.getSelectionEx()[0].SubObjects[0].Surface.Axis    # to Axis
#    v = Gui.Selection.getSelectionEx()[0].SubObjects[0].normalAt(0,0) # normalAt
    r=App.Rotation(App.Vector(0,0,1),v)
    Gui.ActiveDocument.ActiveView.setCameraOrientation(r.Q)
except Exception:
    App.Console.PrintError("Select a face and run the macro"+"\n")

}}

## Links

Original macro by wmayer [Looking for some helpful GUI-commands](http://forum.freecadweb.org/viewtopic.php?f=3&t=7029&p=56735&hilit=Shape.Face4#p56735)



---
![](images/Right_arrow.png) [documentation index](../README.md) > Macro Align Face Object to View/fr
