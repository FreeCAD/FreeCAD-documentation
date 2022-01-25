# Macro Zoom1 1/fr
{{Macro/fr
|Name=Zoom 1:1
|Icon=Zoom1_1.svg
|Description=Zoom 1:1 pour que les objets apparaissent à leur taille réelle sur l'écran.
|Author=TheMarkster
|Version=1.0
|Date=2021-11-9
|FCVersion=Python3+
|Download=[https://wiki.freecadweb.org/File:Zoom1_1.svg Icône de la barre d'outils]
}}

## Description

Effectue un zoom pour que les objets apparaissent à leur taille réelle sur votre écran. Par exemple, vous devriez être en mesure de mesurer un cube de 100 mm à l\'aide d\'une règle tenue devant votre écran.

## Utilisation

Exécutez la macro pour zoomer à la taille réelle de vos objets. Parfois, en raison des limitations de Qt, les informations matérielles fournies à la macro peuvent être incorrectes, par exemple la largeur de l\'écran, en millimètres, peut être incorrecte. Dans ce cas, il existe une boîte de dialogue de calibrage. Pour faire apparaître cette boîte de dialogue, appuyez sur la touche Ctrl pendant l\'exécution de la macro. Un cube temporaire de 100 mm est créé. Mesurez le cube qui apparaît à l\'écran avec une règle ou un pied à coulisse et saisissez vos mesures (en MM) dans la boîte de dialogue. Celle-ci calculera le paramètre d\'ajustement approprié à utiliser pour votre matériel.

Ce paramètre d\'ajustement est stocké dans les paramètres utilisateur à Plugins/Zoom1\_1\_Macro/Tweak.

## Fonctionnement

La taille de l\'écran (de la vue MDI, c\'est-à-dire la vue 3D) est récupérée de Qt en MM. La hauteur de la caméra est alors fixée au plus petit de la largeur ou de la hauteur de l\'écran. Par exemple, si la largeur/hauteur de l\'écran est de 800, 600, la hauteur de la caméra est fixée à 600 au-dessus de la scène.

## Limitations

1.  Parfois, pour diverses raisons, les informations fournies à la macro par Qt concernant les dimensions du matériel peuvent être incorrectes, auquel cas le paramètre Tweak est nécessaire via la boîte de dialogue de calibrage intégrée.
2.  Ne fonctionne qu\'avec les modes de caméra orthographique.
3.  Évidemment, il y a une gamme limitée de tailles où cela peut être utilisé.

## Précautions

Il faut faire attention lorsque l\'on tient des objets ou que l\'on tente de mesurer des choses sur l\'écran, afin d\'éviter de rayer l\'écran.

## Script

L\'icône de la macro <img alt="" src=images/Zoom1_1.svg  style="width:48px;">

**Zoom1\_1.FCMacro**


{{MacroCode|code=
# -*- coding: utf-8 -*-
#Zoom 1:1 macro
#2021, by <TheMarkster>, based on work of kisolre
#Attempts to zoom 3D view such that objects on the screen
#appear to be their actual size
#For example, a 100mm cube should measure 100mm on your screen
#This relies on information provided by Qt about the underlying
#hardware, which Qt admits is not always reliable
#Thus we have a Tweak parameter to workaround such cases.
#Press Ctrl key while executing the macro to bring up the
#calibration dialog and set the tweak for your hardware.


import FreeCAD, FreeCADGui
from PySide import QtGui, QtCore

__version__ = "1.0"

def zoomActual(tweak=1.0):
    gv = av.graphicsView()
    height = gv.heightMM()
    width = gv.widthMM()
    node = av.getCameraNode()
    node.height.setValue(tweak*min(width,height))

doc = FreeCAD.ActiveDocument
if not doc:
    doc = FreeCAD.newDocument()
    FreeCAD.Console.PrintMessage("No document, creating one.\n")
av = FreeCADGui.activeView()
pg = FreeCAD.ParamGet("User parameter:Plugins/Zoom1_1_Macro")
tweak = pg.GetFloat("Tweak",1.0)
if hasattr(av,"graphicsView") and hasattr(av.getCameraNode(),"height"):
    zoomActual(tweak)
    modifiers = QtGui.QApplication.keyboardModifiers()
    if modifiers == QtCore.Qt.ControlModifier:
        visible = [obj for obj in doc.Objects if hasattr(obj,"ViewObject") and obj.ViewObject.Visibility == True]
        for obj in doc.Objects:
            if hasattr(obj,"ViewObject"):
                obj.ViewObject.Visibility = False
        cube = doc.addObject("Part::Box","TemporaryCalibrationCube")
        cube.Length = cube.Height = cube.Width = 100
        cube.ViewObject.DisplayMode = "Shaded"
        av.viewFront()
        doc.recompute()
        zoomActual(1.0)
        text = "\
Calibration dialog\n\
\n\
A temporary 100x100x100 mm cube has been created for this\n\
calibration. Measure this cube and enter your measurements.\n\
A tweak value will be calculated based on what you enter and \n\
will be stored in user parameters / Plugins / Zoom1_1_Macro\n\
\n\
You can move this dialog if necessary, but be sure not to zoom\n\
in or out before measuring the cube. If the cube does not fit\n\
cancel this dialog, resize the 3D view, and try again.\n\
\n\
Enter measured Cube Width or Height (in MM):\n"
        win = FreeCADGui.getMainWindow()
        title = "Zoom1_1 macro v"+__version__
        dlg = QtGui.QInputDialog()
        usertweak,ok = dlg.getDouble(win,title,text,100.0)
        doc.removeObject(cube.Name)
        for obj in visible:
            obj.ViewObject.Visibility = True
        if not ok:
            FreeCAD.Console.PrintMessage("Canceled, keeping current tweak value\n")
        else:
            tweak = usertweak/100.0
            pg.SetFloat("Tweak", tweak)
            zoomActual(tweak)
    FreeCAD.Console.PrintMessage("Zoom 1:1 macro -- Ctrl + execute to calibrate, if necessary\n")
    FreeCAD.Console.PrintMessage("Tweak = "+str(tweak)+"\n")
elif not hasattr(av.getCameraNode(),"height"):
    FreeCAD.Console.PrintError("Error: Only orthographic camera types are supported.\n")
else:
    FreeCAD.Console.PrintError("Error acquiring QGraphicsView. You might need to update your version of FreeCAD.\n")
}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Macro Zoom1 1/fr
