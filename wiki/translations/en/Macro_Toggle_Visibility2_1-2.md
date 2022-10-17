# Macro Toggle Visibility2 1-2/en
{{Macro
|Name=Macro Toggle Visibility2 1-2
|Icon=Macro SelectVisible2.png
|Description={{ColoredParagraph|DarkRed|Yellow|This macro must be used with '''Macro Toggle Visibility2 2-2'''}}<br/>This is a set of four related macros for managing the visibility of objects in the Object Model (return on original visibility)   *<br/># objects that are selected in a document are made visible while objects that are not selected are made invisible<br/>#*if no objects are selected then all objects are hidden;<br/>#*if all objects are selected then all objects are made visible<br/># make all objects visible
|Author=openfablab
|Version=00.02b
|Date=2017-07-27
|FCVersion=All
|Download=[https   *//www.freecadweb.org/wiki/images/d/d7/Macro_SelectVisible2.png ToolBar Icon]
|SeeAlso=[Macro Toggle Visibility2 2-2](Macro_Toggle_Visibility2_2-2.md)<br/>[Macro_Toggle_Visibility](Macro_Toggle_Visibility.md)
}}

## Description


{{ColoredText|This macro work with [Macro Toggle Visibility2 2-2](Macro_Toggle_Visibility2_2-2.md)}}

This is a set of four related macros for managing the visibility of objects in the Object Model   *

1.  objects that are selected in a document are made visible while objects that are not selected are made invisible
    -   if no objects are selected then all objects are hidden;
    -   if all objects are selected then all objects are made visible
2.  make all objects visible

## How To Use 

Copy the macros and the icons in your folder macros and run (see [How to install macros](How_to_install_macros.md))

## ToggleVisibility

Using the selection of objects in the one of the FreeCAD views, this macro makes all selected objects visible and hides all objects which are not selected.

If no object(s) are selected then all objects are hidden

If all objects are hidden and there is no selection in ComboView then all object are made visible

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

Second macro [Macro Toggle Visibility2 2-2](Macro_Toggle_Visibility2_2-2.md)

## Link

The discussion on the forum [Re   * Proposal   * select one or more pieces, hide the others.](https   *//forum.freecadweb.org/viewtopic.php?f=8&t=13152&start=10#p184056)

Original idea [Macro_Toggle_Visibility](https   *//www.freecadweb.org/wiki/index.php?title=Macro_Toggle_Visibility)



---
![](images/Right_arrow.png) [documentation index](../README.md) > Macro Toggle Visibility2 1-2/en
