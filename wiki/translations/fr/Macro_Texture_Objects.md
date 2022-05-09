# Macro Texture Objects/fr
{{Macro/fr
|Name=Texture Objects
|Icon=Macro_Texture_Objects.png
|Description=Cette macro permet de mettre temporairement une image qui servira de texture sur les objets sélectionnés. Pour supprimer les textures, Fermez simplement le document et rouvrez le.
|Author=yorik
|Version=1.0
|Date=2011-10-13
|Download=[https   *//www.freecadweb.org/wiki/images/d/da/Macro_Texture_Objects.png Icône de la barre d'outils]
|FCVersion=0.18 et en dessous
}}

## Description

Cette macro permet de mettre temporairement une image qui servira de texture sur les objets sélectionnés. Pour supprimer les textures, Fermez simplement le document et rouvrez le.

<img alt="" src=images/Textured_objects.jpg  style="width   *680px;">

## Script

**Macro\_Texture\_Objects.FCMacro**


{{MacroCode|code=

import FreeCADGui
from PySide import QtGui
from pivy import coin

# get a jpg filename
jpgfilename = QtGui.QFileDialog.getOpenFileName(QtGui.qApp.activeWindow(),'Open image file','*.jpg')

# apply textures
for obj in FreeCADGui.Selection.getSelection()   *
    rootnode = obj.ViewObject.RootNode
    tex =  coin.SoTexture2()
    tex.filename = str(jpgfilename[0])
    rootnode.insertChild(tex,1)

}}

## Liens

[Macro Texture Objects](https   *//forum.freecadweb.org/viewtopic.php?t=7216)

[Script to map texture with environement checked](https   *//forum.freecadweb.org/viewtopic.php?f=3&t=28795)



---
![](images/Right_arrow.png) [documentation index](../README.md) > Macro Texture Objects/fr
