# Macro Texture Objects/pl
{{Macro/pl
|Name=Tekstura na obiektach
|Icon=Macro_Texture_Objects.png
|Description=Makrodefinicja umożliwia tymczasowe umieszczenie obrazu tekstury na wybranych obiektach. Aby usunąć tekstury, wystarczy zamknąć i ponownie otworzyć dokument.
|Author=yorik
|Version=1.1
|Date=2023-12-08
|Download=[https://wiki.freecad.org/images/d/da/Macro_Texture_Objects.png ikonka paska narzędziowego]
|Download=[https://www.freecadweb.org/wiki/images/d/da/Macro_Texture_Objects.png Ikona paska narzędzi]
|FCVersion= 0.18 i nowszy
}}



## Opis

Makrodefinicja umożliwia tymczasowe umieszczenie obrazu tekstury na wybranych obiektach. Aby usunąć tekstury, wystarczy zamknąć i ponownie otworzyć dokument.

<img alt="" src=images/Textured_objects.jpg  style="width:680px;">



## Skrypt

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



## Odnośniki internetowe 

-   Wątek na forum [Obiekty tekstury](https://forum.freecadweb.org/viewtopic.php?t=7216)

-   Wątek na forum [Skrypt do mapowania tekstur przy zaznaczonym środowisku](https://forum.freecadweb.org/viewtopic.php?f=3&t=28795)



---
⏵ [documentation index](../README.md) > Macro Texture Objects/pl
