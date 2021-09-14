# Macro PlacementAbsolufy/en




{{Macro
|Name=PlacementAbsolufy
|Icon=Macro_PlacementAbsolufy.png
|Description=This macro resets position of all part containers to document origin while keeping the absolute object positions.<br/>This macro has been written mainly to circumvent unfinished Part container implementation that can lead to absolute position shift, mainly when exporting parts. This is due to fact that Part containers creates a local coordinate system that can be shifted from global one. This local referential is then used by subsequent objects but isn't correctly handled by several functions (eg. export).
|Author=OpenBrain
|Date=2019-06-10
|Version=0.2
|FCVersion= 0.17+
|SeeAlso=[Macro StraightenObject](Macro_StraightenObject.md) <img src="images/Macro_StraightenObject.png" width=24px>
|Download=[https://www.freecadweb.org/wiki/images/9/92/Macro_PlacementAbsolufy.png ToolBar Icon]
}}

## Description

### Context

This macro has been written mainly to circumvent unfinished Part container implementation that can lead to absolute position shift, mainly when exporting parts. This is due to fact that Part containers creates a local coordinate system that can be shifted from global one. This local referential is then used by subsequent objects but isn\'t correctly handled by several functions (eg. export).

## Usage

Functionally, the macro will reset the Part containers placement to global origin while preserving the objects absolute position. Notice that PlacementAbsolufy macro applies to the whole active document.

To use the macro, just run it when the document on which it shall be applied is open.

## Installation

The macro is available through [Addon Manager](Std_AddonMgr.md). Code is provided on this page for convenience in case user system doesn\'t have git-python. Though it should be up-to-date, latest release is always available at [FreeCAD-macro repository](https://github.com/FreeCAD/FreeCAD-macros/blob/master/Utility/PlacementAbsolufy.FCMacro)

For more detailed explanations, see the [How to install macros](How_to_install_macros.md) page.

## Script

ToolBar Icon ![](images/Macro_PlacementAbsolufy.png )

**Macro\_PlacementAbsolufy.FCMacro**


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

-   Process the whole open document

## Forum discussion 

For any feedback (bug, feature request, comments, \...), please use this forum thread : [Preserving global position of Parts during export](https://forum.freecadweb.org/viewtopic.php?f=3&t=36869)
