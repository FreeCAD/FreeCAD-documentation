# Macro Cut Line/fr
{{Macro/fr
|Name=Macro Cut Line
|Icon=Macro_Cut_Line.png
|Description=Coupe une ligne en donnant comme argument le nombre de coupures, création de lignes ou non, biscolor, points. La nouvelle ligne est créée dans les coordonnées réelles de l'objet et non dans celles du corps.<br/>{{ColoredText|(Ligne de commande, collez cette macro complète dans la console Python)}}.
|Author=mario52
|Version=2.0
|Date=2019/06/17
|FCVersion=All
|Download=[https://www.freecadweb.org/wiki/images/3/35/Macro_Cut_Line.png ToolBar Icon]
}}

## Description

Cette petite macro coupe une ligne en plusieurs lignes en donnant comme arguments le nombre de coupures, avec création de lignes ou non, colorer les lignes coupées par alternativement rouge puis blanche, création de points à l\'endroit de la coupure ou non.

<img alt="" src=images/Macro_cutLine_00.png  style="width:400px;"> 
*cutLine*

## Utilisation

Vous pouvez l\'utiliser dans une macro.

-   **4 :** nombre de coupures
-   **createPoint** : crée un point si (\>0) ou non (0) (Défaut 1)
-   **createLine** : crée les coupures de lignes (\>0) ou non (0) (Défaut 0)
-   **biColor** : crée les lignes biColor (alternativement rouge puis blanche) (\>0) ou non (0) (Défaut 0)

Vous pouvez changer la valeur de la couleur des lignes par défaut dans la macro.

Avec l\'option bisColor les lignes sont créées de couleurs rouge et blanche, la couleur par défaut est modifiable dans le code aux lignes 20 et 23.

## Script

ToolBar Icon ![](images/Macro_Cut_Line.png )

**Macro\_cutLine.FCMacro**


{{MacroCode|code=
#################################################################
# http://forum.freecadweb.org/viewtopic.php?f=3&t=4217&hilit=discretize
# 08/03/2015 2019/06/17

__title__   = "cutLine"
__author__  = "Mario52"
__version__ = "00.02"
__date__    = "2019/06/17"

import Draft, Part
def cutLine(numberOfPoints = 2, createPoint = 1, createLine = 0, biColor = 0):           # create a points of forme

    def createLines(numberOfPoints, points, biColor):                                        # create line
        biscolor = 0
        for lin in range(numberOfPoints-1):
            creaLine = [FreeCAD.Vector(points[lin]),FreeCAD.Vector(points[lin+1])]
            wire = Draft.makeWire(creaLine,closed=False,face=False,support=None)
            if biColor != 0:                                                                 # biColor 
                if biscolor == 0:
                    FreeCADGui.ActiveDocument.getObject(wire.Name).LineColor = (1.0,0.0,0.0) # 255 = 1 (10 = (1/255 * 10 ))
                    biscolor = 1
                else:
                    FreeCADGui.ActiveDocument.getObject(wire.Name).LineColor = (1.0,1.0,1.0) # 255 = 1 (10 = (1/255 * 10 ))
                    biscolor = 0
    try:
        points = []
        points[:] = []
        selectionObjects = FreeCADGui.Selection.getSelectionEx()         # getSelectionEx
        numberOfPoints += 1
        for selection in selectionObjects:
            compteur = pas = 0
            for selectedEdge in selection.SubObjects:
                    FreeCAD.Console.PrintMessage(selectionObjects[0].SubElementNames[compteur] + "\n")                   
#                    print( selectionObjects[0].SubElementNames[compteur])# getSelectionEx
                    compteur += 1                                              
                    points = selectedEdge.discretize(numberOfPoints)   
                    if createLine != 0:
                        createLines(numberOfPoints, points, biColor)
                    for p in points:
                        if createPoint != 0:
                            Draft.makePoint( p.x, p.y, p.z)
                        FreeCAD.Console.PrintMessage(str(compteur)+" X"+ str(p.x)+" Y"+ str(p.y)+ " Z"+ str(p.z) + "\n")
#                        print( compteur," X", p.x, " Y", p.y, " Z", p.z)
                    pas = 1                                              #

            if pas == 0:                                                 # the not SubObjects
                selectionObjects = FreeCADGui.Selection.getSelection()   # select all elements
                FreeCAD.Console.PrintMessage(selectionObjects[0].Name + "\n")
#                print( selectionObjects[0].Name)                         # getSelection()
                compteur = 0
                for ii in enumerate(selectionObjects[0].Shape.Edges): 
                    compteur += 1
                    points = ii[1].discretize(numberOfPoints)            # discretize the element
                    for p in points:
                        if createPoint != 0:
                            Draft.makePoint( p.x, p.y, p.z)              # create points
                        FreeCAD.Console.PrintMessage(str(compteur)+" X"+ str(p.x)+" Y"+ str(p.y)+ " Z"+ str(p.z) + "\n")
#                         print( compteur, " X", p.x, " Y", p.y, " Z", p.z)  # list and display the coordinates
                    if createLine != 0:
                        createLines(numberOfPoints, points, biColor)
    except:
        FreeCAD.Console.PrintError("Error" + "\n" + "Give : cutLine(numberOfPoints = 2, createPoint = 1, createLine = 0, biColor = 0)"+"\n")
        FreeCAD.Console.PrintError("Select the complete shape or separate wire(s) line, circle ..."+"\n")

#        print( "Error : Give cutLine(numberOfPoints = 2, createPoint = 1, createLine = 0, biColor = 0)")

# Example in command line (paste the macro in FC Python console) and write:
#cutLine(2, createLine = 1, biColor = 1, createPoint = 0)

}}

## Exemple

Peut être utilisée dans l\'éditeur de macro de FreeCAD.

Si la macro complète est collée dans l\'éditeur Python de FreeCAD utilisez la commande suivante :


```python
cutLine(4, createLine = 1, biColor = 1, createPoint = 0)
```

## Liens

Cette macro utilise la fonction discretize [voir le code original](http://forum.freecadweb.org/viewtopic.php?f=3&t=4217&hilit=discretize)



---
![](images/Right_arrow.png) [documentation index](../README.md) > Macro Cut Line/fr
