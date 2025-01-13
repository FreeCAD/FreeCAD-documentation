# Macro HiddenAlls/pl
{{Macro/pl
|Name=Macro HiddenAlls
|Translate=Makrodefinicja: Ukryj wszystko
|Icon=Macro_HiddenAlls.png
|Description=Ukrywa wszystkie obiekty w dokumencie ''(Widoczność = "False")''.
|Author=Mario52
|Version=00.01
|Date=2015-11-12
|FCVersion=wszystkie
|Download=[https://www.freecadweb.org/wiki/images/d/d6/Macro_HiddenAlls.png ToolBar Icon]
|SeeAlso=[Makro Przełącz widoczność 2 1-2](Macro_Toggle_Visibility2_1-2/pl.md)<br>[Makro Przełącz widoczność 2 2-2](Macro_Toggle_Visibility2_2-2/pl.md)<br>[Makro Przełącz widoczność](Macro_Toggle_Visibility/pl.md)<br>[Makro Widoczne wszystko](Macro_VisibleAlls/pl.md)<br>[Makro Jeżeli zaznaczone pozostaw Jeżeli nie to usuń](Macro_If_Selected_Stay_If_Not_Then_Delete/pl.md)
}}



## Opis

Makrodefinicja ta umożliwia ukrycie wszystkich obiektów w dokumencie *(widoczność = \"False\")*.



## Tworzenie skryptów 

Ikonka paska narzędzi <img alt="" src=images/Macro_HiddenAlls.png  style="width:64px;">

**Macro_HidenAlls.FCMacro**


{{MacroCode|code=
import FreeCAD
#Macro_HideAllObjects
__title__="Macro_HideAlls"
__author__ = "Mario52"
__url__     = "http://www.freecadweb.org/index-fr.html"
__version__ = "00.00"
__date__    = "11/11/2015"

try:
    for ShapeNameObj in FreeCAD.ActiveDocument.Objects:   # hidden alls objects
        #print ShapeNameObj.Name
        FreeCADGui.ActiveDocument.getObject(ShapeNameObj.Name).Visibility = False
except Exception:
    None
}}



---
⏵ [documentation index](../README.md) > Macro HiddenAlls/pl
