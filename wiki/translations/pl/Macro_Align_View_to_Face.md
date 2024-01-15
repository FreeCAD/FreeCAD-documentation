# Macro Align View to Face/pl
{{Macro/pl
|Name=Macro Align View to Face
|Name/pl=Makrodefinicja: Wyrównaj widok do ściany
|Icone=Macro_Align_View_to_Face.png
|Description=Makro to ustawia bieżący widok na wybraną ścianę
|Author=Rockn
|Version=3.1
|Date=2023-11-12
|FCVersion=wszystkie
|Download=[https://www.freecadweb.org/wiki/images/d/d7/Macro_Align_View_to_Face.png Ikona paska narzędzi]
}}



## Opis

Makrodefinicja ta obraca bieżący widok tak, aby skierować go prostopadle do wybranej powierzchni istniejącego obiektu.



## Użycie

1.  Zaznacz ścianę na obiekcie.
2.  Uruchom makrodefinicję.



## Skrypt

Ikonka paska narzędzi ![](images/Macro_Align_View_to_Face.png )

**Macro_Align_View_to_Face.FCMacro** {{MacroCode|code=

# -*- coding: utf-8 -*-
# Set the current view perpendicular to the selected line
# Place la vue perpendiculairement a la line selectionnee
# 2013 Jonathan Wiedemann,
# 2016 Werner Mayer, 
# 2022 tchernomax, https://forum.freecadweb.org/viewtopic.php?p=630019#p630019
# 2023 FreeCutter, modifications towards linked objects like in workbench Assembly 4 , https://forum.freecad.org/viewtopic.php?p=718516#p718516
#
__title__   = "Align_View_to_Face"
__author__  = "Jonathan Wiedemann (Rockn)"
__url__     = "https://www.freecadweb.org/"
__Wiki__    = "https://wiki.freecadweb.org/Macro_Align_View_to_Face"
__version__ = "3.1"
__date__    = "2023/11/12"  #YYYY/MM/DD

from pivy import coin

import FreeCAD as app
import FreeCADGui as gui

def pointAt(normal, up):
    z = normal
    y = up
    x = y.cross(z)
    y = z.cross(x)
   
    rot = App.Matrix()
    rot.A11 = x.x
    rot.A21 = x.y
    rot.A31 = x.z
   
    rot.A12 = y.x
    rot.A22 = y.y
    rot.A32 = y.z
   
    rot.A13 = z.x
    rot.A23 = z.y
    rot.A33 = z.z

    return App.Placement(rot).Rotation

def get_selection_and_turn_view():
    doc = app.activeDocument()
    if doc is None:
        app.Console.PrintWarning('Align_view_to_face: No file open, nothing to do\n')
        returnselection = gui.Selection.getSelectionEx('', 0) # Returns a vector of selection objectsif not selection:
        app.Console.PrintWarning('Align_view_to_face: Nothing selected, nothing to do\n')
        returncam = FreeCADGui.ActiveDocument.ActiveView.getCameraNode()''' used to understand the 'getSelection' results
    for selection_object in selection:
        object_ = selection_object.Object
        sub_fullpaths = selection_object.SubElementNames
        if not sub_fullpaths:
            # An object is selected, not a face, edge, vertex.
            print(object_.Name)
        for sub_fullpath in sub_fullpaths:
            # One or more subelements are selected.
            print(object_.Name, sub_fullpath)
    '''sel = selection[0]
    face = sel.SubObjects[0]
    if face.Area == 0:          # trying to avoid errors due to wrong selected objects
        app.Console.PrintWarning('Align_view_to_face: Please select a face - not an edge or vertex\n')
        return
    dir = face.normalAt(0,0)if dir.z == 1 :
        rot = pointAt(dir, App.Vector(0.0,1.0,0.0))
    elif dir.z == -1 :
        rot = pointAt(dir, App.Vector(0.0,1.0,0.0))
    else :
        rot = pointAt(dir, App.Vector(0.0,0.0,1.0))cam.orientation.setValue(rot.Q)
    gui.SendMsgToActiveView("ViewSelection")
    app.Console.PrintWarning('Align_view_to_face: Done\n')

if __name__ == '__main__':
    get_selection_and_turn_view()

}}



---
⏵ [documentation index](../README.md) > Macro Align View to Face/pl
