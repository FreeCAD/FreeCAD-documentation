# Macro Repro Wire/it
 {{Macro/it
|Name= Macro Repro Wire
|Translate=Replica un componente
|Icon= Macro_ReproWire.png
|Description=Questa macro crea un duplicato di un sottoelemento subObject ... selezionato.<br \>(Incluso con la versione FreeCAD 0.19 : Menu → Part → Creare una copia)
|Author=Mario52
|Version=00.04
|Date=2020-03-14
|Download=[https://www.freecadweb.org/wiki/images/a/a3/Macro_ReproWire.png ToolBar Icon]
|FCVersion=Tutte
}}

## Descrizione

Questa macro crea un duplicato di un oggetto, subObject, faccia, contorno o linea, selezionato.\<br \\\>(Incluso con la versione FreeCAD 0.19 : Menu → Part → Creare una copia)

<img alt="" src=images/Macro_ReproWire_00.png  style="width:480px;"> 
*ReproWire*

## Uso

Selezionare l\'oggetto e poi eseguire la macro per creare la sua copia. È possibile usare la copia per produrre delle estrusioni o altre ordinarie operazioni.

Le copie sono di colore rosso e denominate \"Shapexxx + il nome dell\'originale\".

## Script

L\'icona per la barra degli strumenti ![icon for the button](images/Macro_ReproWire.png )

*\' Macro\_ReproWire.FCMacro*\'


{{MacroCode|code=

# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import codecs   #https://docs.python.org/2/howto/unicode.html
import Part,Draft

#24/10/2015, 22/09/2018, 03/07/2019, 14/03/2020

__title__   = "Macro_ReproWire"
__author__  = "Mario52"
__url__     = "http://www.freecadweb.org/index-fr.html"
__Wiki__    = "https://www.freecadweb.org/wiki/Macro_Repro_Wire"
__version__ = "00.04"
__date__    = "2020/03/14"    #YYYY/MM/DD
__Comment__ = "Compatible with FreeCAD 0.17 0.18 and more"

global objectPlacementAngle ; objectPlacementAngle = ""
def objectRealPlacement3D(obj):
    global objectPlacementAngle
    try:
        objectPlacement      = obj.Shape.Placement
        #### 
        objectPlacementBase  = FreeCAD.Vector(objectPlacement.Base)
        ####
        objectWorkCenter     = objectPlacementBase
        ####
        objectPlacementAngle = objectPlacement.Rotation.toEuler()

        if hasattr(obj, "getGlobalPlacement"):
            globalPlacement       = obj.getGlobalPlacement()
            globalPlacementBase   = FreeCAD.Vector(globalPlacement.Base)
            objectRealPlacement3D = globalPlacementBase.add(objectWorkCenter).sub(objectPlacementBase)
            objectPlacementAngle  = globalPlacement.Rotation.toEuler()
        else:
            objectRealPlacement3D = objectWorkCenter

        return objectRealPlacement3D
    except Exception:
        return FreeCAD.Vector(0.0, 0.0, 0.0)

sel = Gui.Selection.getSelection()
s   = Gui.Selection.getSelectionEx()

try:
    if len(sel) != 0:
            print( "Object(s) : ", len(sel), " , SubObject(s) : ", len(s))
            i2 = ii2 = -1 
            for i in s:
                i2 += 1
                ii2 = -1
                try:
                    FreeCADGui.Selection.getSelectionEx()[i2].SubObjects[ii2]
                    for ii in i.SubElementNames:
                        placementOrigine = objectRealPlacement3D(FreeCAD.ActiveDocument.getObject(i.ObjectName))# search the original Placement
                        ii2 += 1
                        Part.show(FreeCADGui.Selection.getSelectionEx()[i2].SubObjects[ii2].copy())   # create repro shape subObject
                        print( i2+1 ,"/", ii2+1 ,"/", len(s) ," ", i.ObjectName ," ", ii)             # display the info SubObject
                        a = App.ActiveDocument.ActiveObject
                        a.Placement.Base = placementOrigine
                        a.Placement.Rotation = App.Rotation(objectPlacementAngle[0], objectPlacementAngle[1], objectPlacementAngle[2])
                        #    object Name  / original object Name / SubObject Name
                        a.Label = a.Name + " " + i.ObjectName + " " + ii                              # Label for the repro shape
                        try:
                            FreeCADGui.activeDocument().activeObject().LineColor  = (1.0,0.0,0.0)     # give LineColor
                            FreeCADGui.activeDocument().activeObject().PointColor = (1.0,0.0,0.0)     # give PointColor
                            FreeCADGui.activeDocument().activeObject().ShapeColor = (1.0,0.0,0.0)     # give ShapeColor
                        except Exception:
                            None
                except Exception:
#                    print( "Not SubObject")
                    placementOrigine = objectRealPlacement3D(FreeCAD.ActiveDocument.getObject(sel[i2].Name))# search the original Placement
                    Part.show(sel[i2].Shape)                                                          # create repro shape object
                    print( i2+1 ,"/", ii2+1 ,"/", len(s) ," ", sel[i2].Name)                          # display the info SubObject
                    a = App.ActiveDocument.ActiveObject
                    a.Placement.Base = placementOrigine
                    a.Placement.Rotation = App.Rotation(objectPlacementAngle[0], objectPlacementAngle[1], objectPlacementAngle[2])
                    #        object Name  /  original object Name
                    a.Label =a.Name + " " +  sel[i2].Name                                             # Label for the repro shape
                    try:
                        FreeCADGui.activeDocument().activeObject().LineColor  = (1.0,0.0,0.0)         # give LineColor
                        FreeCADGui.activeDocument().activeObject().PointColor = (1.0,0.0,0.0)         # give PointColor
                        FreeCADGui.activeDocument().activeObject().ShapeColor = (1.0,0.0,0.0)         # give ShapeColor
                    except Exception:
                        None
                try:
                    SubElement = FreeCADGui.Selection.getSelectionEx()[0].SubObjects[0]
                    print( FreeCADGui.Selection.getSelectionEx()[0].SubElementNames[0], " : ", SubElement.normalAt(0,0)) # ok Vector pour face
                except Exception:
                    None
                    
            FreeCAD.ActiveDocument.recompute()
    else :
        FreeCAD.Console.PrintError("Select one object" + "\n")
except Exception:
    FreeCAD.Console.PrintError("Unexpected error" + "\n")

}}

## Versione

00.04 2020-03-14 : correzione per rotazione obbietto

00.03 03/07/2019 : compatibilità con Python 3 \"print\" verso \"print()\"

00.02 22/09/2018 : Compatible with FreeCAD 0.17 (getGlobalPlacement())

00.01 24/10/2015 : extension to all objects

00.00 22/10/2015 :

## Link

Nel forum [are there any tools to extrude only selected surface from a sketch?](http://forum.freecadweb.org/viewtopic.php?f=3&t=12922)




