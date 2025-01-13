# Macro Texture Objects/de
{{Macro/de
|Name=Texture Objects
|Translate=Texture Objects
|Icon=Macro_Texture_Objects.png
|Description=Dieses Makro ermöglicht eine Texturabbildung auf ausgewählte Objekte zu legen. Zum Entfernen der Texturen einfach das Dokument schließen und erneut öffnen.
|Author=yorik
|Version=1.1
|Date=2023-12-08
|Download=[https://wiki.freecad.org/wiki/images/d/da/Macro_Texture_Objects.png ToolBar Icon]
|FCVersion= 0.18 und darunter
}}



## Beschreibung

Dieses Makro ermöglicht eine Texturabbildung auf ausgewählte Objekte zu legen. Zum Entfernen der Texturen einfach das Dokument schließen und erneut öffnen.

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

-   Forum-Thread [Macro Texture Objects](https://forum.freecadweb.org/viewtopic.php?t=7216)

-   Forum-Thread [https://forum.freecadweb.org/viewtopic.php?f=3&t=28795 Script to map texture with environement checked](https://forum.freecadweb.org/viewtopic.php?f=3&t=28795_Script_to_map_texture_with_environement_checked.md)



---
⏵ [documentation index](../README.md) > Macro Texture Objects/de
