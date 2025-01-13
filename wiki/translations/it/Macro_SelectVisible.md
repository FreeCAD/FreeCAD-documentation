# Macro SelectVisible/it
{{Macro/it
|Name=Macro SelectVisible
|Translate=Seleziona oggetti visibili
|Icon=SelectVisible.png
|Description=Verranno selezionati tutti e soli gli oggetti visibili nell'albero.
|Author=galou_breizh
|Version=1.0
|Date=2016-04-08
|FCVersion=All
|Download=[https://wiki.freecad.org/images/5/51/SelectVisible.png Icona della barra degli strumenti]
}}



## Descrizione

Seleziona tutti gli oggetti visibili nella struttura e solo questi.


{{Codeextralink|https://raw.githubusercontent.com/FreeCAD/FreeCAD-macros/master/Utility/SelectVisible.FCMacro}}



## Utilizzo

Copiare la macro nella cartella delle macro ed eseguirla (vedi [Come installare le macro](How_to_install_macros/it.md) per ulteriori dettagli).

## Script

L\'ultima versione della macro si trova in <https://github.com/FreeCAD/FreeCAD-macros/blob/master/Utility/SelectVisible.FCMacro>

Icona della barra degli strumenti ![](images/SelectVisible.png )

**Macro_Select.FCMacro** {{MacroCode|code=
# FreeCAD Macro SelectVisible

__Name__ = 'Select Visible'
__Comment__ = 'All visible objects in the tree will be selected'
__Web__ = 'http://www.freecadweb.org/wiki/Macro_SelectVisible'
__Wiki__ = 'http://www.freecadweb.org/wiki/Macro_SelectVisible'
__Icon__ = 'https://wiki.freecad.org/images/5/51/SelectVisible.png'
__Help__ = 'All visible objects in the tree and only these will be selected'
__Author__ = 'galou_breizh'
__Version__ = '1.0'
__Status__ = 'Production'
__Requires__ = ''

import FreeCAD as App
import FreeCADGui as Gui

doc = App.activeDocument()

if not doc:
    App.Console.PrintWarning('SelectVisible: no active document')
else:
    Gui.Selection.clearSelection()
    for o in doc.Objects:
        if o.ViewObject.Visibility:
            Gui.Selection.addSelection(o)
}}



---
⏵ [documentation index](../README.md) > Macro SelectVisible/it
