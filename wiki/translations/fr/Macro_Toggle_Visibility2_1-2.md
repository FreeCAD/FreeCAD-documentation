# Macro Toggle Visibility2 1-2/fr
{{Macro/fr
|Name=Macro Toggle Visibility2 1-2
|Icon=Macro_SelectVisible2.png
|Description={{ColoredParagraph|DarkRed|Yellow|Cette macro doit être utilisée avec '''Macro Toggle Visibility2 2-2'''}}<br/>Cache tous les objets qui ne sont pas sélectionnés, le rappel permet de retourner à l'état original.
|Author=openfablab
|Version=00.02b
|Date=2017-07-27
|FCVersion=All
|Download=[https   *//www.freecadweb.org/wiki/images/d/d7/Macro_SelectVisible2.png ToolBar Icon]
|SeeAlso=[Macro Toggle Visibility2 2-2](Macro_Toggle_Visibility2_2-2/fr.md)<br/>[Macro_Toggle_Visibility](Macro_Toggle_Visibility/fr.md)
}}

## Description


{{ColoredText|Cette macro doit être utilisée avec [Macro Toggle Visibility2 2-2](Macro_Toggle_Visibility2_2-2.md)}}

Ceci est un ensemble de quatre macros liées à la gestion de la visibilité des objets dans la vue 3D    *

1.  Cache les objets qui ne sont pas sélectionnés
    -   s\'il n\'y a pas d\'objet sélectionné tous les objets seront cachés
    -   si les objets sont cachés et qu\'aucun objet n\'est sélectionné dans la Vue combinée tous les objets seront visibles.
2.  Affiche tous les objets.

## Utilisation

Copiez les macros et les icônes dans votre répertoire de macros (voir [Comment installer une macro](How_to_install_macros/fr.md)).

## ToggleVisibility

Cette macro rend tous les objets sélectionnés visibles et cache tous les objets qui ne sont pas sélectionnés.

Si aucun objet est sélectionné, tous les objets sont cachés

Si tous les objets sont cachés et non sélectionné(s) tous les objets deviennent visibles

## Script 1 

ToolBar Icon <img alt="" src=images/Macro_SelectVisible2.png  style="width   *64px;">

**Macro_Toggle_Visibility2_1-2.FCMacro**


{{MacroCode|code=

import FreeCAD
# "Macro_Toggle_Visibility2_1-2" associate with "Macro_Toggle_Visibility2_2-2"
__title__="Macro_Toggle_Visibility2_1-2"
__author__ = "openfablab"
__url__     = "http   *//www.freecadweb.org/index-fr.html"
__version__ = "00.02b"
__date__    = "27/07/2017"
FreeCAD.actual=[]
try   * 
    compt = 0
    for ShapeNameObj in FreeCAD.ActiveDocument.Objects   *                                   # list alls objet for test if alls hidden
        if (FreeCADGui.ActiveDocument.getObject(ShapeNameObj.Name).Visibility == False) and (Gui.Selection.isSelected(ShapeNameObj) == False)   *
            compt += 1                                                                    # if hidden    * compt += 1
            #print "False    * ",ShapeNameObj.Name
        elif Gui.Selection.isSelected(ShapeNameObj) == False   *
            FreeCAD.actual.append(ShapeNameObj.Name)
            #print "Actual    * ",ShapeNameObj.Name
    if compt == len(FreeCAD.ActiveDocument.Objects)   *                                      # if (compt = Alls objects hidden) then Visibility = True
        for ShapeNameObj in FreeCAD.ActiveDocument.Objects   *
            FreeCADGui.ActiveDocument.getObject(ShapeNameObj.Name).Visibility = True      # Visibility = True
            #print "True     * ",ShapeNameObj.Name
        compt = 0
    else    *
        for ShapeNameObj in FreeCAD.ActiveDocument.Objects   *                               # hidde objects not selecteds
            if Gui.Selection.isSelected(ShapeNameObj) == False   *
                FreeCADGui.ActiveDocument.getObject(ShapeNameObj.Name).Visibility = False # if objects is not selected then Visibility = False (Hidden)
                #print "False    * ",ShapeNameObj.Name
            else   *
                FreeCADGui.ActiveDocument.getObject(ShapeNameObj.Name).Visibility = True  # if objects are hidden and selected then Visibility = True and hidden alls objects visibles
                #print "True     * ",ShapeNameObj.Name
except Exception   *
    None }}

## Script 2 

ToolBar <img alt="" src=images/Macro_VisibleAlls2.png  style="width   *64px;">

Seconde macro [Macro Toggle Visibility2 2-2](Macro_Toggle_Visibility2_2-2/fr.md)

## Link

La discussion sure forum [Re   * Proposal   * select one or more pieces, hide the others.](https   *//forum.freecadweb.org/viewtopic.php?f=8&t=13152&start=10#p184056)

Idée Originale [Macro_Toggle_Visibility](https   *//www.freecadweb.org/wiki/index.php?title=Macro_Toggle_Visibility)



---
![](images/Right_arrow.png) [documentation index](../README.md) > Macro Toggle Visibility2 1-2/fr
