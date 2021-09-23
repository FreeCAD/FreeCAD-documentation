# Macro Cut Circle/fr
{{Macro/fr
|Name=Macro Cut Circle
|Name/fr=Macro Cut Circle
|Icon=Macro_Cut_Circle.png
|Description=Coupe un cercle(s) ou un arc(s) sélectionné(s) en plusieurs arcs contigus, les arcs créés sont colorés alternativement en rouge et blanc pour distinguer les différents arcs. Le nouveau cercle est créé dans la coordonnée réelle de l'objet, et non dans celle du corps. <br/>{{ColoredText|(Ligne de commande, collez cette macro complète dans la console Python)}}.
|Author=mario52
|Version=00.03
|Date=2019-07-02
|Download=[https://www.freecadweb.org/wiki/images/9/93/Macro_Cut_Circle.png Icon]
}}

## Description

Cette macro coupe un cercle(s) ou un arc(s) sélectionné(s) en plusieurs arcs contigus, les arcs sont colorés alternativement en rouge et blanc pour distinguer les différents arcs.

<img alt="" src=images/Macro_CutCircle_00.png  style="width:400px;"> 
*CutCircle*

## Utilisation

Copiez la macro **cutCirle** dans la console Python FreeCAD, sélectionnez le type de cercle(s) et (ou) arc(s) dans la console:

pour voir les cercles et arcs découpés dans cet exemple cinq arcs contigus.

l\'objet(s) original(aux) n\'est pas éffacé.

## Script

ToolBar Icon ![](images/Macro_Cut_Circle.png )

**Macro\_Cut\_Circle.FCMacro**


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

## Exemple


```python
cutCircle(5, 1)  # here with 5 arcs and coloured
cutCircle(4)     #
```

## Projet

Couper les cercles d\'un cylindre.

## Version

ver 00.03 02/07/2019 : ajout \"App.ActiveDocument.recompute()\"

ver 00.02 09/03/2015 : ajout de création des arcs colorés alternativement rouge et blanc ou non.

ver 00.01 24/02/2015 :

---
[documentation index](../README.md) > Macro Cut Circle/fr
