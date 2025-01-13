# Macro If Selected Stay If Not Then Delete/pl
{{Macro/pl
|Name=Macro If Selected Stay If Not Then Delete
|Translate=Makrodefinicja: Jeśli wybrane pozostaw, jeśli nie to usuń
|Icon=Macro_If_Selected_Stay_If_Not_Then_Delete.png
|Description=Makrodefinicja umożliwia usunięcie wszystkich niezaznaczonych obiektów.
|Author=Mario52
|Version=00.03b
|Date=2023-09-24
|FCVersion=wszystkie
|Download=[https://www.freecadweb.org/wiki/images/6/62/Macro_If_Selected_Stay_If_Not_Then_Delete.png ToolBar Icon]
|SeeAlso=[Makro przełącz widoczność 2 1-2](Macro_Toggle_Visibility2_1-2/pl.md)<br>[Makro przełącz widoczność 2 2-2](Macro_Toggle_Visibility2_2-2/pl.md)<br>[Makro przełącz widoczność](Macro_Toggle_Visibility/pl.md)<br>[Makro ukryj wszystko](Macro_HiddenAlls/pl.md)<br>[Makro wyświetl wszystko](Macro_VisibleAlls/pl.md)
}}



## Opis

Makrodefinicja umożliwia usunięcie wszystkich niezaznaczonych obiektów.



## Tworzenie skryptów 

Ikonka paska narzędzi <img alt="" src=images/Macro_If_Selected_Stay_If_Not_Then_Delete.png  style="width:64px;">

**Macro_If_Selected_Stay_If_Not_Then_Delete.FCMacro**


{{MacroCode|code=
import FreeCAD
import Draft
# 16/06/2016, 21/02/2018, 22/09/2023, 24/09/2023
# Macro_SelectVisible series
__title__   = "Macro_If_Selected_Stay_If_Not_Then_Delete"
__author__  = "Mario52"
__url__     = "http://www.freecadweb.org/index-fr.html"
__version__ = "00.03b"
__date__    = "24/09/2023"

App = FreeCAD
try:
    for ShapeNameObj in FreeCAD.ActiveDocument.Objects:
        if str(ShapeNameObj) == "<group object>":
            if len(Draft.get_group_contents(ShapeNameObj)) == 0:
                App.ActiveDocument.removeObject(ShapeNameObj.Name)        # remove group not selecteds
        else:
            if Gui.Selection.isSelected(ShapeNameObj):
                None
            else:
                App.ActiveDocument.removeObject(ShapeNameObj.Name)        # remove objects not selectedsfor ShapeNameGroup in FreeCAD.ActiveDocument.Objects:
        if (str(ShapeNameGroup) == "<group object>"):
            if len(Draft.get_group_contents(ShapeNameGroup)) == 0:
                App.ActiveDocument.removeObject(ShapeNameGroup.Name)      # remove group emptied
except Exception:
    None
}}



---
⏵ [documentation index](../README.md) > Macro If Selected Stay If Not Then Delete/pl
