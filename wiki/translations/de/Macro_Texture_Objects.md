# Macro Texture Objects/de
<div class="mw-translate-fuzzy">


{{Macro/de
|Name=Texture Objects
|Translate=Texture Objects
|Icon=Macro_Texture_Objects.png
|Description=This macro allows you to temporarily put a texture image on selected objects. To remove the textures, simply close and reopen the document.
|Author=yorik
|Version=1.0
|Date=2011-10-13
|Download=[https://www.freecadweb.org/wiki/images/d/da/Macro_Texture_Objects.png Icon Toolbar]
|FCVersion= 0.18 und darunter
}}


</div>

## Description


<div class="mw-translate-fuzzy">

## Beschreibung

Mit diesem Makro können Sie ein Texturbild vorübergehend auf ausgewählten Objekten platzieren. Um die Texturen zu entfernen, schließen Sie das Dokument einfach und öffnen Sie es erneut.


</div>

<img alt="" src=images/Textured_objects.jpg  style="width:680px;">



## Skript

**Macro_Texture_Objects.FCMacro**


{{MacroCode|code=

import FreeCADGui
from PySide import QtGui
from pivy import coin

# get a jpg filename
jpgfilename = QtGui.QFileDialog.getOpenFileName(QtGui.QApplication.activeWindow(),'Open image file','*.jpg')

# apply textures
for obj in FreeCADGui.Selection.getSelection():
    rootnode = obj.ViewObject.RootNode
    tex =  coin.SoTexture2()
    tex.filename = str(jpgfilename[0])
    rootnode.insertChild(tex,1)

}}

## Links


<div class="mw-translate-fuzzy">

[Macro Texture Objects](https://forum.freecadweb.org/viewtopic.php?t=7216)


</div>


<div class="mw-translate-fuzzy">

[Script to map texture with environement checked](https://forum.freecadweb.org/viewtopic.php?f=3&t=28795)


</div>



---
⏵ [documentation index](../README.md) > Macro Texture Objects/de
