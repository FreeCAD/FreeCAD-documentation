# Macro Cut Circle
{{Macro
|Name=Macro Cut Circle
|Icon=Macro_Cut_Circle.png
|Description=Cut a circle(s) or arc(s) in multiple arcs, the arcs created can be coloured alternately to distinguish. The new circle is created in the real coordinate of object, not in the coordinate of the Body.<br/>{{ColoredText|(Command line, paste this complete macro in the Python console)}}.
|Author=mario52
|Version=00.03
|Date=2019-07-02
|FCVersion=All
|Download=[https://www.freecadweb.org/wiki/images/9/93/Macro_Cut_Circle.png Icon]
}}

## Description

This macro cut a circle(s) or arc(s) in multiple arcs, the arcs can be coloured alternately to distinguish.

 <img alt="" src=images/Macro_CutCircle_00.png  style="width:400px;">  
*CutCircle*

## Usage

Copy the macro **cutCirle** complete in the Python console FreeCAD select the circle(s) and (or) arc(s) type in the console: 

 to see the circles and arcs cut here in the example 5 contiguous arcs.

The original object is not deleted.

## Script



ToolBar Icon ![](images/Macro_Cut_Circle.png )

**Macro_Cut_Circle.FCMacro**


{{MacroCode|code=

# selection circle(s) (circles and arcs)
# give number of cut, biColor 0/1
# cut the circle to x arcs
# if biColor is <> 0 the arcs are coloured alternately Red White Red White ....
# 
 
__title__   = "cutCircle"
__author__  = "Mario52"
__date__    = "02/07/2019"
__version__ = "00.03"

import Draft
global biscolor ; biscolor = 0
def cutCircle(number = 2, biColor = 0):
    global biscolor
    def defbiColor(objet):
        global biscolor
        if biscolor == 0:
            FreeCADGui.ActiveDocument.getObject(objet.Name).LineColor = (1.0,0.0,0.0) # 255 = 1 (10 = (1/255 * 10 ))
            biscolor = 1
        else:
            FreeCADGui.ActiveDocument.getObject(objet.Name).LineColor = (1.0,1.0,1.0) # 255 = 1 (10 = (1/255 * 10 ))
            biscolor = 0
    selection = FreeCADGui.Selection.getSelection()
    for piece in selection:
        nom = piece.Name
        if (nom[:6] == "Circle") or (nom[:8] == "Cylinder"):
            circonference = piece.Shape.Length
            rayon = piece.Radius
            placem = piece.Placement
 
            if (nom[:8] == "Cylinder"):
                pivot0 = float(piece.Angle/number)
                FreeCAD.Console.PrintMessage("Cylinder"+"\n")
            else:
                pivot0 = float(360/number)
                FreeCAD.Console.PrintMessage("Circle"+"\n")
            pivot1 = 0.0
            for i in range(number):
                cercle = Draft.makeCircle(radius=rayon,placement=placem,face=False,startangle=(pivot1),endangle=(pivot0+pivot1),support=None)
                if biColor != 0:
                    defbiColor(cercle)
                pivot1 += pivot0
        elif nom[:3] == "Arc":
            FreeCAD.Console.PrintMessage("Arc"+"\n")
            circonference = piece.Shape.Length
            rayon = piece.Radius
            placem = piece.Placement
            First = float(piece.FirstAngle)
            Last  = float(piece.LastAngle)
            pivot0 = abs((First - Last) / number)
            pivot1 = 0.0
            for i in range(number):
                cercle = Draft.makeCircle(radius=rayon,placement=placem,face=False,startangle=(pivot1+First),endangle=(pivot0+pivot1+First),support=None)
                if biColor != 0:
                    defbiColor(cercle)
                pivot1 += pivot0
    App.ActiveDocument.recompute()

#cutCircle(5, 1)  # here with 5 arcs and coloured
#cutCircle(4)     #

}}



## Example




```python
cutCircle(5, 1)  # here with 5 arcs and coloured
cutCircle(4)     #
```



## Project

Cut circle to cylinder

## Version

ver 00.03 02/07/2019 : add \"App.ActiveDocument.recompute()\"

ver 00.02 09/03/2015 : adding create arcs coloured altenat alternately Red White Red White \.... or not

ver 00.01 24/02/2015 :



---
![](images/Button_right.svg) [documentation index](../README.md) > Macro Cut Circle
