# Macro SelectVisible/fr
{{Macro/fr
|Name=Macro SelectVisible
|Name/fr=Macro SelectVisible
|Icon=SelectVisible.png
|Description=Tous les objets visibles dans l'arborescence et seulement ceux-ci seront sélectionnés.
|Author=galou_breizh
|Version=1.0
|Date=2016-04-08
|FCVersion=Toutes
|Download=[https://wiki.freecad.org/images/5/51/SelectVisible.png Icône de la barre d'outils]
}}

## Description

Sélectionne tous les objets visibles dans la vue 3D


{{Codeextralink|https://raw.githubusercontent.com/FreeCAD/FreeCAD-macros/master/Utility/SelectVisible.FCMacro}}



## Utilisation

Copiez la macro dans votre répertoire de macros (voir [Comment installer une macro](How_to_install_macros/fr.md) pour plus d\'informations)

## Script

La dernière version est téléchargeable sur <https://github.com/FreeCAD/FreeCAD-macros/blob/master/Utility/SelectVisible.FCMacro>

Icône de la barre d\'outils ![](images/SelectVisible.png )

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
⏵ [documentation index](../README.md) > Macro SelectVisible/fr
