# Macro Copy3DViewToClipboard/fr
{{Macro/fr
|Name=Macro Copy3DViewToClipboard
|Icon=Macro_Copy3DViewToClipboard.png
|Description=Cette macro copie le contenu de la vue 3D redimensionnée en 640 x 480 pixels dans la mémoire en image bitmap (BMP). La copie dans Gimp n'est pas possible Gimp utilise sa propre méthode pour la fonction copier.
|Author=Mario52
|Version=00.01
|Date=2016-09-14
|FCVersion= <=0.17
|Download=[https://www.freecadweb.org/wiki/images/8/84/Macro_Copy3DViewToClipboard.png ToolBar Icon]
|Shortcut=G Q
|SeeAlso=[Macro Snip](Macro_Snip/fr.md) <img src="images/Snip.png" width=24px><br/>[Macro Screen Wiki](Macro_Screen_Wiki/fr.md) <img src="images/Macro_Screen_Wiki.png" width=24px>
}}

## Description

Cette macro copie le contenu de la vue 3D redimensionnée en 640 x 480 pixels dans la mémoire en image bitmap (BMP). La copie dans Gimp n\'est pas possible Gimp utilise sa propre méthode pour la fonction copier.


{{Codeextralink|https://gist.githubusercontent.com/mario52a/f5c3738f858f7b058897c6c235232cbe/raw/a10bc3b8789badc1e405541d4697d7286d9f0fd3/Macro_Copy3DViewToClipboard.FCMacro}}

## Utilisation

-   Lancez la macro.
-   Pressez la touche **G** pour copier le contenu de la vue 3D.
-   Pressez la touche **Q** pour quitter la macro.

PS: Si vous voulez définir une autre résolution d\'image, modifiez les valeurs de la ligne numéro 33 ex:

line 33 : ***glw.resize(640, 480) \# reduce the SubWindow***

par

Line 33 : ***glw.resize(800, 600) \# reduce the SubWindow***

## Discussion

La discussion sur le forum [Copy contents of 3D view to clipboard](http://forum.freecadweb.org/viewtopic.php?f=3&t=16731).

## Script

L\'icône pour votre barre d\'outil ![](images/Macro_Copy3DViewToClipboard.png )

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



---
![](images/Right_arrow.png) [documentation index](../README.md) > Macro Copy3DViewToClipboard/fr
