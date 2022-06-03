# Macro Toggle Visibility/fr
{{Macro/fr
|Name=Toggle Visibility
|Icon=Macro SelectVisible.png
|Description=Bascule caché/affiché tous les objets non sélectionnés.<br />Les objets qui sont sélectionnés dans un document sont rendus visibles tandis que les objets qui ne sont pas sélectionnés sont rendus invisibles.<br />Si aucun objet n'est sélectionné alors tous les objets sont cachés.<br />Si tous les objets sont sélectionnés alors tous les objets sont rendus visibles.
|Author=Mario52
|Version=00.02
|Date=2015-11-12
|FCVersion=Toutes
|Download=[https   *//www.freecadweb.org/wiki/images/4/42/Macro_SelectVisible.png Icône de la barre d'outils]
|SeeAlso=[Macro Toggle Visibility2 1-2](Macro_Toggle_Visibility2_1-2/fr.md)<br>[Macro Toggle Visibility2 2-2](Macro_Toggle_Visibility2_2-2/fr.md)<br>[Macro VisibleAlls](Macro_VisibleAlls/fr.md)<br>[Macro HiddenAlls](Macro_HiddenAlls/fr.md)<br>[Macro If Selected Stay If Not Then Delete](Macro_If_Selected_Stay_If_Not_Then_Delete/fr.md)
}}

## Description

Les objets qui sont sélectionnés dans un document sont rendus visibles tandis que les objets qui ne sont pas sélectionnés sont rendus invisibles.

-   si aucun objet n\'est sélectionné, tous les objets sont cachés.
-   si tous les objets sont sélectionnés, tous les objets deviennent visibles.

## Utilisation

Copiez la macro et l\'icône dans votre répertoire de macros (voir [Comment installer une macro](How_to_install_macros/fr.md)).

## Basculer la visibilité 

En utilisant la sélection d\'objets dans l\'une des vues FreeCAD, cette macro rend tous les objets sélectionnés visibles et masque tous les objets non sélectionnés.

Si aucun objet n\'est sélectionné tous les objets seront cachés.

Si les objets sont cachés et qu\'aucun objet n\'est sélectionné dans la Vue combinée tous les objets seront visibles.

(Cette nouvelle version 00.02) inclus les trois macros en une seule.

## Script

L\'icône pour votre barre d\'outils <img alt="" src=images/Macro_SelectVisible.png  style="width   *48px;">

**Macro\_ToggleSelectedObjectVisibility.FCMacro**


{{MacroCode|code=

import FreeCAD
# Macro_ToggleSelectedObjectVisibility
__title__="Macro_ToggleSelectedObjectVisibility"
__author__ = "Mario52"
__url__     = "http   *//www.freecadweb.org/index-fr.html"
__version__ = "00.02"
__date__    = "12/11/2015"

try   *
    compt = 0
    for ShapeNameObj in FreeCAD.ActiveDocument.Objects   *                                   # list alls objet for test if alls hidden
        if (FreeCADGui.ActiveDocument.getObject(ShapeNameObj.Name).Visibility == False) and (Gui.Selection.isSelected(ShapeNameObj) == False)   *
            compt += 1                                                                    # if hidden    * compt += 1
            #print "False    * ",ShapeNameObj.Name
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
    None
}}

## Lien

La discussion sur le forum [Proposal   * select one or more pieces, hide the others.](http   *//forum.freecadweb.org/viewtopic.php?f=8&t=13152)

## Version

ver 00.02 12/11/2015 **macro Macro\_SelectVisible**    * Si aucun objet n\'est sélectionné tous les objets seront cachés, si les objets sont cachés et qu\'aucun objet n\'est sélectionné dans la Vue combinée tous les objets seront visibles. Cette nouvelle version inclus les trois macros en une seule.



---
![](images/Right_arrow.png) [documentation index](../README.md) > Macro Toggle Visibility/fr
