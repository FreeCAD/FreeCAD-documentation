  {{Macro
|Name=Macro Copy3DViewToClipboard
|Icon=Macro_Copy3DViewToClipboard.png
|Description=Macro will copy the contents of the 3D view to the clipboard in image bitmap (BMP).<br/>The copy in Gimp is not possible Gimp use his model in memory.
|Author=Mario52
|Version=00.01
|Date=2016-09-14
|FCVersion= <=0.17
|Download=[https://www.freecadweb.org/wiki/images/8/84/Macro_Copy3DViewToClipboard.png ToolBar Icon]
|Shortcut=G, Q
|SeeAlso=[Macro Snip](Macro_Snip.md) <img src="images/Snip.png" width=24px><br/>[Macro Screen Wiki](Macro_Screen_Wiki.md) <img src="images/Macro_Screen_Wiki.png" width=24px>
}}

## Description

Macro will copy the contents of the 3D view to the clipboard in image bitmap (BMP). The copy in Gimp is not possible Gimp use his model in memory.

 

## How To Use {#how_to_use}

-   Run once to activate macro (the macro is loaded resident into the memory of the PC).
-   Press **G** to grab the contents of the 3d view and copy them to the clipboard.
-   Press **Q** to quit.

PS: if you wild other format modify the values of the line number 33 ex: 

line 33 : ***glw.resize(640, 480) \# reduce the SubWindow***

 to 

Line 33 : ***glw.resize(800, 600) \# reduce the SubWindow***



## Discussion

See [forum-thread here](http://forum.freecadweb.org/viewtopic.php?f=3&t=16731).

## Code

The icon for you toolbar ![](images/Macro_Copy3DViewToClipboard.png )



**Macro\_Copy3DViewToClipboard.FCMacro**


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




