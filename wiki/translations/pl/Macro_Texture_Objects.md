# Macro Texture Objects/pl
{{Macro
|Name=Texture Objects
|Icon=Macro_Texture_Objects.png
|Description=This macro allows you to temporarily put a texture image on selected objects. To remove the textures, simply close and reopen the document.
|Author=yorik
|Version=1.0
|Date=2011-10-13
|Download=[https://www.freecadweb.org/wiki/images/d/da/Macro_Texture_Objects.png Icon Toolbar]
|FCVersion= 0.18 and below
}}

## Description

This macro allows you to temporarily put a texture image on selected objects. To remove the textures, simply close and reopen the document.

<img alt="" src=images/Textured_objects.jpg  style="width:680px;">

## Script

**Macro_Texture_Objects.FCMacro**


{{MacroCode|code=

import FreeCADGui
from PySide import QtGui
from pivy import coin

# get a jpg filename
jpgfilename = QtGui.QFileDialog.getOpenFileName(QtGui.qApp.activeWindow(),'Open image file','*.jpg')

# apply textures
for obj in FreeCADGui.Selection.getSelection():
    rootnode = obj.ViewObject.RootNode
    tex =  coin.SoTexture2()
    tex.filename = str(jpgfilename[0])
    rootnode.insertChild(tex,1)

}}

## Links

-   Forum thread [Macro Texture Objects](https://forum.freecadweb.org/viewtopic.php?t=7216)

-   Forum thread [Script to map texture with environement checked](https://forum.freecadweb.org/viewtopic.php?f=3&t=28795)



---
![](images/Button_right.svg) [documentation index](../README.md) > Macro Texture Objects/pl
