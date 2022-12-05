# Macro Copy3DViewToClipboard/it
<div class="mw-translate-fuzzy">


{{Macro/it
|Name=Macro Copy3DViewToClipboard
|Translate=Copia la vista 3D negli appunti
|Icon=Macro_Copy3DViewToClipboard.png
|Description=Copia il contenuto della vista 3D negli appunti
|Author=Mario52
|Version=00.01
|Date=2016-09-14
|FCVersion= <=0.17
|Download=[https://www.freecadweb.org/wiki/images/8/84/Macro_Copy3DViewToClipboard.png ToolBar Icon]
|SeeAlso=<img src="images/Snip.png" width=24px><br/>[Macro Screen Wiki](Macro_Screen_Wiki.md) <img src="images/Macro_Screen_Wiki.png" width=24px>
|Shortcut=G, Q
}}


</div>

## Descrizione


<div class="mw-translate-fuzzy">

La macro copia il contenuto della vista 3D negli appunti in immagine bitmap (BMP). La copia dentro Gimp no è possibile Gimp utilizza il suo metodo.


</div>


{{Codeextralink|https://gist.githubusercontent.com/mario52a/f5c3738f858f7b058897c6c235232cbe/raw/a10bc3b8789badc1e405541d4697d7286d9f0fd3/Macro_Copy3DViewToClipboard.FCMacro}}

## Uso

-   Eseguirla una volta per attivare macro (la macro viene caricata e rimane residente nella memoria del PC).
-   Premere **G** per catturare il contenuto della vista 3D e copiarlo negli appunti.
-   Premere **Q** pr uscire.


<div class="mw-translate-fuzzy">

Per avere un formato diverso modificare i valori nella riga 33 ad esempio:


</div>

line 33 : ***glw.resize(640, 480) \# reduce the SubWindow***

in

line 33 : ***glw.resize(800, 600) \# reduce the SubWindow***

## Discussione

Vedere la discussione nel [forum](http://forum.freecadweb.org/viewtopic.php?f=3&t=16731).

## Codice

L\'icona per la barra degli strumenti ![](images/Macro_Copy3DViewToClipboard.png )

**Macro_Copy3DViewToClipboard.FCMacro**


{{MacroCode|code=
# -*- coding: utf-8 -*-
import PySide
from PySide.QtGui import *
from PySide import QtGui ,QtCore
from PySide import QtOpenGL
#from gimpfu import *
 
__title__   = "Macro_Copy3DViewToClipboard"
__author__  = "Mario52"
__url__     = "http://www.freecadweb.org/index-fr.html"
__version__ = "00.01"
__date__    = "14/09/2016"
           
class ViewObserver:
    print "run FCGrab .."
 
    def logPosition(self, info):
        import tempfile
        import os
        from PySide import QtGui
 
        pos = info["Key"]
        if pos.upper() == "G":
            pos = ""
           
            mw=Gui.getMainWindow()
            gl=mw.findChildren(QtOpenGL.QGLWidget)
            glw=gl[0] # just use the first element
 
            originalsize = glw.size()                               # originalsize SubWindow
            print "originalsize : ",originalsize.width(),", ", originalsize.height()
 
            glw.resize(640, 480)                                    # reduce the SubWindow
            glw.show()
            Gui.SendMsgToActiveView("ViewFit")
            print "resize in : ",glw.frameGeometry().width()," ",glw.frameGeometry().height()
 
            i=glw.grabFrameBuffer()
            cb=QtGui.qApp.clipboard()
            cb.setImage(i)
            glw.resize(originalsize.width(), originalsize.height()) # restore originalsize SubWindow
            print "Grab"
 
        if (pos.upper() == "Q"):
            v.removeEventCallback("SoKeyboardEvent",c)
            print "End FCGrab"
 
 
v=Gui.activeDocument().activeView()
o = ViewObserver()
c = v.addEventCallback("SoKeyboardEvent",o.logPosition)

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Macro Copy3DViewToClipboard/it
