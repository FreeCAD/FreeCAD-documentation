 {{Macro/es
|Name=Texture Objects
|Icon=Macro_Texture_Objects.png
|Translate=Objetos de textura
|Description=Esta macro permite poner temporalmente una imagen de textura en los objetos seleccionados. Para eliminar las texturas, simplemente cierra y vuelve a abrir el documento.
|Author=yorik
|Version=1.0
|Date=2011-10-13
|Download=[https://www.freecadweb.org/wiki/images/d/da/Macro_Texture_Objects.png Icon Toolbar]
|FCVersion= 0.18 y por debajo
}}

## Descripción

Esta macro permite poner temporalmente una imagen de textura en los objetos seleccionados. Para eliminar las texturas, simplemente cierra y vuelve a abrir el documento.

<img alt="" src=images/Textured_objects.jpg  style="width:680px;">

## Guión

**Macro\_Texture\_Objects.FCMacro**


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

[Macro Texture Objects](https://forum.freecadweb.org/viewtopic.php?t=7216)

[Script to map texture with environement checked](https://forum.freecadweb.org/viewtopic.php?f=3&t=28795)




