# Macro Texture Objects/ru

 {{Macro/ru
|Name=Texture Objects
|Translate=Текстурные объекты
|Icon=Macro_Texture_Objects.png
|Description=Этот макрос позволяет временно поместить текстуру на выбранный объект. Для удаления текстуры, просто закройте и вновь откройте документ.
|Author=yorik
|Version=1.0
|Date=2011-10-13
|Download=[https://www.freecadweb.org/wiki/images/d/da/Macro_Texture_Objects.png Icon Toolbar]
|FCVersion= 0.18 и ниже
}}

## Описание

Этот макрос позволяет временно наложить текстуру изображения на выделенные объекты. Чтобы удалить текстуры, просто закройте и снова откройте документ.

<img alt="" src=images/Textured_objects.jpg  style="width:680px;">

## скрипт

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

## связи

[Macro Texture Objects](https://forum.freecadweb.org/viewtopic.php?t=7216)

[Script to map texture with environement checked](https://forum.freecadweb.org/viewtopic.php?f=3&t=28795)




