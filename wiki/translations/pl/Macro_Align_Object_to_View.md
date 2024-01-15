# Macro Align Object to View/pl
{{Macro/pl
|Name=Macro Align Object to View
|Icon=Macro_Align_Object_to_View.png
|Description=Makrodefinicja ta ustawia wybrany obiekt względem bieżącego widoku.
|Author=Mario52
|Version=0.1
|Date=2015-01-16
|FCVersion=Wszystkie
|Download=[https://www.freecadweb.org/wiki/images/f/f4/Macro_Align_Object_to_View.png ToolBar Icon]
|SeeAlso=[32px|FCCamera](File:FCCamera_00.png.md) [Makro FCCamera](Macro_FCCamera/pl.md)
}}

## Opis

Makrodefinicja ta wyrównuje i pozycjonuje wybrany obiekt względem bieżącego widoku.

## Użycie

-   Skieruj widok, wybierz obiekt i uruchom makrodefinicję.
-   Twój obiekt zostanie umieszczony we wskazanym miejscu przez współrzędne ujęcia widoku *(kamery)*.



## Tworzenie skryptów 

ToolBar Icon ![](images/Macro_Align_Object_to_View.png )

**Macro_Align_Object_to_View.FCMacro**


{{MacroCode|code=
# This macro place your object selected to the position ActiveView (camera)
# extact FCCamera
# 16/01/2015

__title__  ="Align Object to View"
__author__ = "Mario52"
__date__   = "16/01/2015"
__version__= "0.1"

import pivy
from pivy import coin

sel = FreeCADGui.Selection.getSelection()
Nameelement = sel[0].Name
App.Console.PrintMessage(str(Nameelement)+"\n")

pl = FreeCAD.Placement()
pl.Rotation = FreeCADGui.ActiveDocument.ActiveView.getCameraOrientation()
pl.Base = FreeCAD.Vector(0.0,0.0,0.0)

App.ActiveDocument.getObject(Nameelement).Placement=pl

}}



## Przykład


<center>

Image:Macro Align Object to View 01.png\|Obiekt w pierwotnym położeniu XY. Image:Macro Align Object to View 02.png\|Obrócić ekran X? Y? Z? lub użyj tej makrodefinicji [Makro Rotate View](Macro_Rotate_View/pl.md) do precyzyjnego obracania.


</center>


<center>

Image:Macro Align Object to View 03.png\|Wybierz obiekt i uruchom makro *(obiekt zwrócony w stronę ekranu)*. Image:Macro Align Object to View 04.png\|Twój obiekt powróci na płaszczyźnie XY i w nowej pozycji współrzędnych *(Umiejscowienie, Kąt)*.


</center>

## Uznania

Zbiorniki Uproszczony kod do rentlau_64



---
⏵ [documentation index](../README.md) > Macro Align Object to View/pl
