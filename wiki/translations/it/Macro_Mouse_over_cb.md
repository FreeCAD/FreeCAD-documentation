# Macro Mouse over cb/it
<div class="mw-translate-fuzzy">


{{Macro/it
|Name=Macro Mouse over cb
|Icon=Macro_Mouse_over_cb.png
|Translate=Macro Mouse over cb
|Description= Questa macro mostra tutti gli elementi di sotto il mouse.
|Author=Chris_G
|Version=00.00
|Date=2016-12-13
|FCVersion=All
|Download=[https   *//www.freecadweb.org/wiki/images/5/55/Macro_Mouse_over_cb.png Toolbar icon]
|SeeAlso=[Macro FC element selector](Macro_FC_element_selector.md) [<img src=images/Macro_FC_element_selector.png style="width   *24px">
}}


</div>

## Descrizione


<div class="mw-translate-fuzzy">

Questa macro mostra tutti gli elementi sotto il mouse (verranno visualizzati anche tutti gli elementi coperti da altri elementi)


</div>


<div class="mw-translate-fuzzy">

## Utilizzazione


</div>

Lancia la macro, la macro sta residente in memoria

## Codice

Toolbar icon ![](images/Macro_Mouse_over_cb.png )

**Macro_Mouse_over_cb.FCMacro**


{{MacroCode|code=
from pivy import coin
import FreeCADGui

def mouse_over_cb( event_callback)   *
    event = event_callback.getEvent()
    pos = event.getPosition().getValue()
    listObjects = FreeCADGui.ActiveDocument.ActiveView.getObjectsInfo((int(pos[0]),int(pos[1])))
    obj = []
    if listObjects   *
        FreeCAD.Console.PrintMessage("\n *** Objects under mouse pointer ***")
        for o in listObjects   *
            label = str(o["Object"])
            if not label in obj   *
                obj.append(label)
        FreeCAD.Console.PrintMessage("\n"+str(obj))


view = FreeCADGui.ActiveDocument.ActiveView

mouse_over = view.addEventCallbackPivy( coin.SoLocation2Event.getClassTypeId(), mouse_over_cb )

# to remove Callback    *
#view.removeEventCallbackPivy( coin.SoLocation2Event.getClassTypeId(), mouse_over_cb)

}}

## Elenco

La discussione sul foro [finding/selecting all elements below cursor](https   *//forum.freecadweb.org/viewtopic.php?f=10&t=19072)

Altra similare macro [Selecting internal faces of a pressure vessel](https   *//forum.freecadweb.org/viewtopic.php?f=18&t=12381&p=151950#p151950) (carica il file [FC_element_selector_v1p1p1.py](https   *//forum.freecadweb.org/download/file.php?id=31041))



---
![](images/Right_arrow.png) [documentation index](../README.md) > Macro Mouse over cb/it
