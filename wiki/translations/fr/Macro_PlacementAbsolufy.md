# Macro PlacementAbsolufy/fr
{{Macro
|Name=PlacementAbsolufy
|Name/fr=PlacementAbsolufy
|Icon=Macro_PlacementAbsolufy.png
|Description=Cette macro réinitialise la position de tous les conteneurs de pièces pour documenter l'origine tout en conservant les positions absolues des objets.<br/>Cette macro a été écrite principalement pour contourner l'implémentation inachevée du conteneur de pièces qui peut entraîner un changement de position absolue, principalement lors de l'exportation de pièces. Cela est dû au fait que les conteneurs de pièces créent un système de coordonnées local qui peut être déplacé du système global. Ce référentiel local est ensuite utilisé par les objets suivants mais n'est pas correctement géré par plusieurs fonctions (par exemple, l'exportation).
|Author=OpenBrain
|Date=2019-06-10
|Version=0.2
|FCVersion= 0.17+
|SeeAlso=[Macro StraightenObject](Macro_StraightenObject/fr.md) <img src="images/Macro_StraightenObject.png" width=24px>
|Download=[https://www.freecadweb.org/wiki/images/9/92/Macro_PlacementAbsolufy.png ToolBar Icon]
}}

## Description

### Contexte

Cette macro a été écrite principalement pour contourner l\'implémentation de conteneur de pièces inachevée qui peut entraîner un changement de position absolu, principalement lors de l\'exportation de pièces. Cela est dû au fait que les conteneurs de pièces créent un système de coordonnées local qui peut être déplacé du système global. Ce référentiel local est ensuite utilisé par les objets suivants mais n\'est pas correctement géré par plusieurs fonctions (par exemple, l\'exportation).

## Utilisation

Fonctionnellement, la macro réinitialisera le placement des conteneurs de pièces à l\'origine globale tout en préservant la position absolue des objets. Notez que la macro PlacementAbsolufy s\'applique à l\'ensemble du document actif.

Pour utiliser la macro, il suffit de l\'exécuter lorsque le document sur lequel elle doit être appliquée est ouvert.

## Installation

La macro est disponible via le [gestionnaire des extensions](Std_AddonMgr/fr.md). Le code est fourni sur cette page pour plus de commodité au cas où le système utilisateur n\'aurait pas git-python. Bien qu\'elle soit à jour, la dernière version est toujours disponible sur [FreeCAD-macro repository](https://github.com/FreeCAD/FreeCAD-macros/blob/master/Utility/PlacementAbsolufy.FCMacro)

Pour des explications plus détaillées, consultez la page [Comment installer des macros](How_to_install_macros/fr.md).

## Script

ToolBar Icon ![](images/Macro_PlacementAbsolufy.png )

**Macro_PlacementAbsolufy.FCMacro**


{{MacroCode|code=
#!/usr/bin/python
#####################################
# Copyright (c) openBrain 2019
# Licensed under LGPL v2
#
# This macro will reset position of all part containers to document origin while keeping the absolute object positions
#
# Version history :
# *0.2 : some typo improvement + commenting for official PR
# *0.1 : alpha release, almost no test performed
#
#####################################

__Name__ = 'PlacementAbsolufy'
__Comment__ = 'Reset part containers to global origin while keeping object positions'
__Author__ = 'openBrain'
__Version__ = '0.2'
__Date__ = '2019-06-10'
__License__ = 'LGPL v2'
__Web__ = 'https://www.freecadweb.org/wiki/Macro_PlacementAbsolufy'
__Wiki__ = 'https://www.freecadweb.org/wiki/Macro_PlacementAbsolufy'
__Icon__ = ''
__Help__ = 'Run the macro with model active in the GUI'
__Status__ = 'Alpha'
__Requires__ = 'FreeCAD >= 0.17'
__Communication__ = 'https://forum.freecadweb.org/viewtopic.php?f=3&t=36869'
__Files__ = ''

currState = {} #initialize a dictionary to store current object placements

for obj in App.ActiveDocument.Objects: #going through active document objects
    if "Placement" in obj.PropertiesList: #if object has a Placement property
        currState[obj] = obj.getGlobalPlacement() #store the object pointer with its global placement

App.ActiveDocument.openTransaction("Absolufy") #open a transaction for undo management

for obj, plac in currState.items(): #going through all moveable objects
    if obj.isDerivedFrom("App::Part"): #if object is a part container
        obj.Placement = App.Placement(App.Vector(0,0,0),App.Rotation(0,0,0)) #reset its placement to global document origin
    elif obj.TypeId[:5] == "App::": #if object is another App type (typically an origin axis or plane)
        None #do nothing
    else: #for all other objects
        obj.Placement = plac #replace them at their global (absolute) placement

App.ActiveDocument.commitTransaction() #commit transaction
}}

## Limitations

-   Traite le document ouvert

## Forum discussion 

Pour tout commentaire (bogue, demande de fonctionnalité, commentaires, \...), veuillez utiliser ce fil de discussion: [Preserving global position of Parts during export](https://forum.freecadweb.org/viewtopic.php?f=3&t=36869)



---
![](images/Right_arrow.png) [documentation index](../README.md) > Macro PlacementAbsolufy/fr
