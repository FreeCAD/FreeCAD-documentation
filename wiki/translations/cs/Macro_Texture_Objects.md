# Macro Texture Objects/cs
{{Macro/cs
|Name=Texture Objects
|Translate=Texture Objects
|Icon=Macro_Texture_Objects.png
|Description=Toto makro umožňuje dočasně vložit obrázek s texturou na vybraný objekt. Pro odstranění textury stačí jednoduše zavřít a znovu otevřít dokument.
|Author=yorik
|Version=1.0
|Date=2011-10-13
|Download=[https://www.freecadweb.org/wiki/images/d/da/Macro_Texture_Objects.png Icon Toolbar]
|FCVersion= 0.18 и испод
}}

## Description


<div class="mw-translate-fuzzy">

## Description 

Toto makro umožňuje dočasně vložit obrázek s texturou na vybraný objekt. Pro odstranění textury stačí jednoduše zavřít a znovu otevřít dokument.


</div>

<img alt="" src=images/Textured_objects.jpg  style="width:680px;">

## Скрипта

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

## Линкови


<div class="mw-translate-fuzzy">

[Macro Texture Objects](https://forum.freecadweb.org/viewtopic.php?t=7216)


</div>


<div class="mw-translate-fuzzy">

[Script to map texture with environement checked](https://forum.freecadweb.org/viewtopic.php?f=3&t=28795)


</div>



---
![](images/Right_arrow.png) [documentation index](../README.md) > Macro Texture Objects/cs
