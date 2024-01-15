# Macro Texture Objects/fr
{{Macro/fr
|Name=Texture Objects
|Name/fr=Texture Objects
|Icon=Macro_Texture_Objects.png
|Description=Cette macro permet de mettre temporairement une image qui servira de texture sur les objets sélectionnés. Pour supprimer les textures, Fermez simplement le document et rouvrez le.
|Author=yorik
|Version=1.1
|Date=2023-12-08
|Download=[https://wiki.freecad.org/images/d/da/Macro_Texture_Objects.png Icône de la barre d'outils]
|FCVersion=0.18 et en dessous
}}

## Description

Cette macro permet de mettre temporairement une image qui servira de texture sur les objets sélectionnés. Pour supprimer les textures, Fermez simplement le document et rouvrez le.

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



## Liens

-   Fil du forum [Macro Texture Objects](https://forum.freecadweb.org/viewtopic.php?t=7216)

-   Fil du forum [Script to map texture with environement checked](https://forum.freecadweb.org/viewtopic.php?f=3&t=28795)



---
⏵ [documentation index](../README.md) > Macro Texture Objects/fr
