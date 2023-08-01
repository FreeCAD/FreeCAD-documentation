# Macro Toggle Visibility2 2-2/fr
{{Macro/fr
|Name=Macro Toggle Visibility2 2-2
|translate=Macro Toggle Visibility2 2-2
|Icon=Macro_VisibleAlls2.png
|Description={{ColoredParagraph|DarkRed|Yellow|Cette macro travaille avec '''Macro_Toggle_Visibility2_1-2'''}}<br/>Cette macro rend tous les objets visibles en respectant les objets originaux visibles et cachés après utilisation du[Macro Toggle Visibility2 1-2](Macro_Toggle_Visibility2_1-2/fr.md)
|Author=openfablab
|Version=00.02b
|Date=2017-07-27
|FCVersion=All
|Download=[https://www.freecadweb.org/wiki/images/e/ec/Macro_VisibleAlls2.png ToolBar Icon]
|SeeAlso=[Macro Toggle Visibility2 1-2](Macro_Toggle_Visibility2_1-2/fr.md)<br/>[Macro Toggle Visibility](Macro_Toggle_Visibility/fr.md)
}}

## Description


{{ColoredText|Cette macro travaille avec '''[Macro Toggle Visibility2 1-2](Macro_Toggle_Visibility2_1-2/fr.md)'''}}

Cette macro rend tous les objets visibles en respectant les objets originaux visibles et cachés après utilisation du [Macro Toggle Visibility2 1-2](Macro_Toggle_Visibility2_1-2/fr.md)

## Utilisation

Copiez les macros et les icônes dans vos macros de dossiers et exécutez-les (voir [How to install macros](How_to_install_macros/fr.md))

## Script

Cette macro rend tous les objets visibles en respectant les objets originaux visibles et cachés après l\'utilisation de la macro [Macro_Toggle_Visibility2_1-2](Macro_Toggle_Visibility2_1-2/fr.md).

ToolBar Icon <img alt="" src=images/Macro_VisibleAlls2.png  style="width:64px;">

**Macro_DisplayAllObjects2_2-2.FCMacro**


{{MacroCode|code=

import FreeCAD
#original name "Macro_VisibleAlls" pratical name "Macro_Toggle_Visibility2_2-2" "Macro_Toggle_Visibility2_1-2" associate with "Macro_Toggle_Visibility2_2-2"
__title__="Macro_DisplayAllObjects2_2-2"
__author__ = "openfablab"
__url__     = "http://www.freecadweb.org/index-fr.html"
__version__ = "00.00b"
__date__    = "27/07/2017"

try:
    for ShapeNameObj in FreeCAD.actual:   # displyed alls objects
        #print ShapeNameObj
        FreeCADGui.ActiveDocument.getObject(ShapeNameObj).Visibility = True
except Exception:
    None }}



---
⏵ [documentation index](../README.md) > Macro Toggle Visibility2 2-2/fr
