# Macro Copy3DViewToClipboard/fr
{{Macro/fr
|Name=Macro Copy3DViewToClipboard
|Icon=Macro_Copy3DViewToClipboard.png
|Description=La macro copiera le contenu de la vue 3D dans le presse-papiers en image bitmap (BMP).<br/>Copier dans Gimp n'est pas possible. Gimp utilise sa propre méthode pour la fonction de copie. 
|Author=Mario52
|Version=00.01
|Date=2016-09-14
|FCVersion= <=0.17
|Download=[https://www.freecadweb.org/wiki/images/8/84/Macro_Copy3DViewToClipboard.png Icône de la barre d'outils]
|Shortcut=G, Q
|SeeAlso=[Macro Snip](Macro_Snip/fr.md) <img src="images/Snip.png" width=24px><br/>[Macro Screen Wiki](Macro_Screen_Wiki/fr.md) <img src="images/Macro_Screen_Wiki.png" width=24px>
}}

## Description

La macro copiera le contenu de la vue 3D dans le presse-papiers en image bitmap (BMP). Il n\'est pas possible de copier dans Gimp. Gimp utilise sa propre méthode pour la fonction de copie.


{{Codeextralink|https://gist.githubusercontent.com/mario52a/f5c3738f858f7b058897c6c235232cbe/raw/a10bc3b8789badc1e405541d4697d7286d9f0fd3/Macro_Copy3DViewToClipboard.FCMacro}}

## Utilisation

-   Lancer une fois pour activer la macro (la macro est chargée de manière résidente dans la mémoire du PC).
-   Appuyez sur **G** pour saisir le contenu de la vue 3D et le copier dans le presse-papiers.
-   Appuyez sur **Q** pour quitter.

PS : si vous voulez d\'autres formats, modifiez les valeurs du numéro de ligne 33 ex :

line 33 : ***glw.resize(640, 480) \# reduce the SubWindow***

par

line 33 : ***glw.resize(800, 600) \# reduce the SubWindow***

## Discussion

La discussion sur le forum [Copy contents of 3D view to clipboard](http://forum.freecadweb.org/viewtopic.php?f=3&t=16731).

## Script

L\'icône pour votre barre d\'outil ![](images/Macro_Copy3DViewToClipboard.png )

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
![](images/Button_right.svg) [documentation index](../README.md) > Macro Copy3DViewToClipboard/fr
