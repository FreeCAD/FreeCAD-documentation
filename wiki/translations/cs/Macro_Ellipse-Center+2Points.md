# Macro Ellipse-Center+2Points/cs
{{Macro/cs
|Name=Macro_Ellipse-Center+2Points
|Translate=Ellipse Center+2Points
|Icon=Macro_Ellipse-Center%2B2Points.png
|Description=Vytvoří elipsu výběrem 3 bodů (v tomto pořadí): střed, velký poloměr, malý poloměr
|Author=Eriossoltero
|Version=02.00
|Date=2019-07-29
|FCVersion=All
|Download=[https://www.freecadweb.org/wiki/images/6/66/Macro_Ellipse-Center%2B2Points.png ToolBar Icon]
}}

## Popis

Vytvoří elipsu výběrem 3 bodů (v tomto pořadí): střed, velký poloměr, malý poloměr

![](images/EllipseCenter2Point.png )

## Најновији


<div class="mw-translate-fuzzy">

Најновија верзија макроа налази се на адреси [EllipseCenter2Points.FCMacro](https://github.com/FreeCAD/FreeCAD-macros/blob/master/ObjectCreation/EllipseCenter2Points.FCMacro) али најлакши начин да инсталирате овај макро је преко[Аддон Манагер](Std_AddonMgr/cs.md).


</div>

## Сцрипт

ToolBar Icon ![](images/Macro_Ellipse-Center%2B2Points.png )

**Macro\_EllipseCenter2Points.FCMacro**


{{MacroCode|code=


# Macro Begin: Ellipse-Center+2Points.FCMacro +++++++++++++++++++++++++++++++++++++++++++++++++
# http://freecad-tutorial.blogspot.com/2011/12/engine-9-poly-v-belt.html
# https://www.freecadweb.org/wiki/User:Eriossoltero
# 13/03/2012, 29/07/2019
import Part, FreeCAD, math, PartGui, FreeCADGui
from FreeCAD import Base

# get the selected objects, with first selection for the trajectory and second for the section
# Adapted from:
# Macro Begin: Ellipse-Center+2Points.FCMacro +++++++++++++++++++++++++++++++++++++++++++++++++
# http://freecad-tutorial.blogspot.com/2011/12/engine-9-poly-v-belt.html
import Part, FreeCAD, math, PartGui, FreeCADGui
from FreeCAD import Base

# get the selected objects, with first selection for the trajectory and second for the section
# Adapted from:
# http://freecad-tutorial.blogspot.com/2011/12/engine-9-poly-v-belt.html
s = FreeCADGui.Selection.getSelection()
try:
    sel1=s[0].Shape
    sel2=s[1].Shape
    sel3=s[2].Shape
    pt_center = sel1.Point
    pt_radmay = sel2.Point
    pt_radmen = sel3.Point# create Part object in the current document
    myObject=App.ActiveDocument.addObject("Part::Feature","Ellipse")# create a shape and assign it to the current document
    ellipse = Part.Ellipse(pt_radmay, pt_radmen, pt_center)
    myObject.Shape = ellipse.toShape()
    # Macro End: Ellipse-Center+2Points.FCMacro +++++++++++++++++++++++++++++++++++++++++++++++++

except:
    print( "Wrong selection")
    print( "First:centre, Second:major radius and Third:minor radius")

}}

---
[documentation index](../README.md) > Macro Ellipse-Center+2Points/cs
