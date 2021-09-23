# Macro Mouse over cb/en
 {{Macro
|Name=Macro Mouse over cb
|Icon=Macro_Mouse_over_cb.png
|Description=This macro display in report view all elements below cursor (all elements covered by other elements will also be displayed)
|Author=Chris_G
|Version=00.00
|Date=2016-12-13
|FCVersion=All
|Download=[https://www.freecadweb.org/wiki/images/5/55/Macro_Mouse_over_cb.png Toolbar icon]
|SeeAlso=<img src=images/Macro_FC_element_selector.png style="width:Macro FC element selector](Macro_FC_element_selector.md) [24px">
}}

## Description

This macro display in report view all elements below cursor (all elements covered by other elements will also be displayed)

## Usage

Run the macro, the macro stay resident in memory.

## Script

Toolbar icon ![](images/Macro_Mouse_over_cb.png )

**Macro\_Mouse\_over\_cb.FCMacro**


{{MacroCode|code=
from pivy import coin
import FreeCADGui

def mouse_over_cb( event_callback):
    event = event_callback.getEvent()
    pos = event.getPosition().getValue()
    listObjects = FreeCADGui.ActiveDocument.ActiveView.getObjectsInfo((int(pos[0]),int(pos[1])))
    obj = []
    if listObjects:
        FreeCAD.Console.PrintMessage("\n *** Objects under mouse pointer ***")
        for o in listObjects:
            label = str(o["Object"])
            if not label in obj:
                obj.append(label)
        FreeCAD.Console.PrintMessage("\n"+str(obj))


view = FreeCADGui.ActiveDocument.ActiveView

mouse_over = view.addEventCallbackPivy( coin.SoLocation2Event.getClassTypeId(), mouse_over_cb )

# to remove Callback :
#view.removeEventCallbackPivy( coin.SoLocation2Event.getClassTypeId(), mouse_over_cb)

}}

## Links

The forum discussion [finding/selecting all elements below cursor](https://forum.freecadweb.org/viewtopic.php?f=10&t=19072)

Other similar macro [Selecting internal faces of a pressure vessel](https://forum.freecadweb.org/viewtopic.php?f=18&t=12381&p=151950#p151950) (download the file [FC\_element\_selector\_v1p1p1.py](https://forum.freecadweb.org/download/file.php?id=31041))
