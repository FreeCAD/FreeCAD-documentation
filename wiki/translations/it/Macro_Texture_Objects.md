# Macro Texture Objects/it
{{Macro/it
|Name=Texture Objects
|Icon=Macro_Texture_Objects.png
|Translate=Campitura di oggetti
|Description=Questa macro permette di mettere temporaneamente una immagine di texture sugli oggetti selezionati. Per rimuovere le campiture, è sufficiente chiudere e riaprire il documento.
|Author=yorik
|Version=1.0
|Date=2011-10-13
|Download=[https://www.freecadweb.org/wiki/images/d/da/Macro_Texture_Objects.png Icon Toolbar]
|FCVersion= 0.18 e precedenti
}}



## Descrizione

Questa macro permette di mettere temporaneamente una immagine di texture sugli oggetti selezionati. Per rimuovere le campiture, è sufficiente chiudere e riaprire il documento.

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



## Link

-   La discussione nel forum [Macro Texture Objects](https://forum.freecadweb.org/viewtopic.php?t=7216)

-   La discussione nel forum [Script to map texture with environement checked](https://forum.freecadweb.org/viewtopic.php?f=3&t=28795)



---
⏵ [documentation index](../README.md) > Macro Texture Objects/it
