# Macro SelectVisible/fr
 {{Macro/fr
|Icon=SelectVisible.png
|Name=Macro SelectVisible
|Description=Sélectionne tous les objets visibles.
|Author=galou_breizh
|Version=1.0
|Date=2016-04-08
|FCVersion=All
|Download=[https://www.freecadweb.org/wiki/images/5/51/SelectVisible.png ToolBar Icon]
}}

## Description

Sélectionne tous les objets visibles dans la vue 3D


{{Codeextralink|https://raw.githubusercontent.com/FreeCAD/FreeCAD-macros/master/Utility/SelectVisible.FCMacro}}

## Utilisation

Copiez la macro dans votre répertoire de macros (voir [Comment installer une macro](How_to_install_macros/fr.md) pour plus d\'informations)

## Script

La dernière version est téléchargeable sur <https://github.com/FreeCAD/FreeCAD-macros/blob/master/Utility/SelectVisible.FCMacro>

ToolBar Icon ![](images/SelectVisible.png )

**Macro\_Select.FCMacro** {{MacroCode|code=
# FreeCAD Macro SelectVisible

__Name__ = 'Select Visible'
__Comment__ = 'All visible objects in the tree will be selected'
__Web__ = 'http://www.freecadweb.org/wiki/Macro_SelectVisible'
__Wiki__ = 'http://www.freecadweb.org/wiki/Macro_SelectVisible'
__Icon__ = 'SelectVisible.svg'
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
