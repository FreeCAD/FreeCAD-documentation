# Macro Zoom1 1/en
{{Macro
|Name=Zoom 1   *1
|Icon=Zoom1_1.svg
|Description=1   *1 Zooming so objects appear their actual size on the screen.
|Author=TheMarkster
|Version=1.0
|Date=2021-11-9
|FCVersion=Python3+
|Download=[https   *//wiki.freecadweb.org/File   *Zoom1_1.svg ToolBar Icon]
}}

## Description

Zooms the camera so objects appear their actual size on your screen. For example, you should be able to measure a 100 mm cube to be 100 mm with a ruler held up to your screen.

## How To Use 

Execute the macro to zoom to the actual size of your objects. Sometimes, due to limitations with Qt the hardware information given to the macro might be incorrect, for example the screen width, in millimeters might be incorrect. For such cases there is a calibration dialog. To bring up the dialog, press Ctrl key while executing the macro. A 100 mm temporary cube is created. Measure the cube that appears on your screen with a ruler or caliper and enter your measurements (in MM) into the dialog. It will compute the appropriate tweak parameter to use for your hardware.

This tweak parameter is stored in user parameters at Plugins/Zoom1_1\_Macro/Tweak.

## How it works 

The screen size (of the MDI view, aka the 3D view) is fetched from Qt in MM. The camera height is then set to the lesser of the width or height of the screen. For example, if the screen width/height is 800, 600, then the camera height is set to 600 above the scene.

## Limitations

1.  Sometimes for various reasons the information provided to the macro by Qt regarding hardware dimensions might be incorrect, in which case the Tweak parameter is needed via the integrated calibration dialog.
2.  Only works with orthographic camera modes.
3.  Obviously, there is a limited range of sizes where this can be used.

## Precautions

Care must be taken when holding up objects or attempting to measure things on the screen lest the screen be physically scratched.

## Script

The macro icon <img alt="" src=images/Zoom1_1.svg  style="width   *48px;">

**Zoom1_1.FCMacro**


{{MacroCode|code=
# -*- coding   * utf-8 -*-
#Zoom 1   *1 macro
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

def zoomActual(tweak=1.0)   *
    gv = av.graphicsView()
    height = gv.heightMM()
    width = gv.widthMM()
    node = av.getCameraNode()
    node.height.setValue(tweak*min(width,height))

doc = FreeCAD.ActiveDocument
if not doc   *
    doc = FreeCAD.newDocument()
    FreeCAD.Console.PrintMessage("No document, creating one.\n")
av = FreeCADGui.activeView()
pg = FreeCAD.ParamGet("User parameter   *Plugins/Zoom1_1_Macro")
tweak = pg.GetFloat("Tweak",1.0)
if hasattr(av,"graphicsView") and hasattr(av.getCameraNode(),"height")   *
    zoomActual(tweak)
    modifiers = QtGui.QApplication.keyboardModifiers()
    if modifiers == QtCore.Qt.ControlModifier   *
        visible = [obj for obj in doc.Objects if hasattr(obj,"ViewObject") and obj.ViewObject.Visibility == True]
        for obj in doc.Objects   *
            if hasattr(obj,"ViewObject")   *
                obj.ViewObject.Visibility = False
        cube = doc.addObject("Part   *   *Box","TemporaryCalibrationCube")
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
Enter measured Cube Width or Height (in MM)   *n"
        win = FreeCADGui.getMainWindow()
        title = "Zoom1_1 macro v"+__version__
        dlg = QtGui.QInputDialog()
        usertweak,ok = dlg.getDouble(win,title,text,100.0)
        doc.removeObject(cube.Name)
        for obj in visible   *
            obj.ViewObject.Visibility = True
        if not ok   *
            FreeCAD.Console.PrintMessage("Canceled, keeping current tweak value\n")
        else   *
            tweak = usertweak/100.0
            pg.SetFloat("Tweak", tweak)
            zoomActual(tweak)
    FreeCAD.Console.PrintMessage("Zoom 1   *1 macro -- Ctrl + execute to calibrate, if necessary\n")
    FreeCAD.Console.PrintMessage("Tweak = "+str(tweak)+"\n")
elif not hasattr(av.getCameraNode(),"height")   *
    FreeCAD.Console.PrintError("Error   * Only orthographic camera types are supported.\n")
else   *
    FreeCAD.Console.PrintError("Error acquiring QGraphicsView. You might need to update your version of FreeCAD.\n")
}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Macro Zoom1 1/en
