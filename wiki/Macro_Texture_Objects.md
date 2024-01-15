# Macro Texture Objects
{{Macro
|Name=Texture Objects
|Icon=Macro_Texture_Objects.png
|Description=This macro allows you to temporarily put a texture image on selected objects. To remove the textures, simply close and reopen the document.
|Author=yorik
|Version=1.1
|Date=2023-12-08
|Download=[https://wiki.freecad.org/images/d/da/Macro_Texture_Objects.png ToolBar Icon]
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
jpgfilename = QtGui.QFileDialog.getOpenFileName(QtGui.QApplication.activeWindow(),'Open image file','*.jpg')

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
⏵ [documentation index](../README.md) > Macro Texture Objects
