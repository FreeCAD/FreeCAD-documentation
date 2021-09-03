 {{Macro
|Name=Constraint Draft
|Icon=Macro_Constraint_Draft.png
|Description=Create simulation using the [expressions](Expressions.md) for link all objects (This macro run with FreeCAD version 16 ).
|Author=Mario52
|Version=1.0
|Date=2017-04-19
|FCVersion=0.16
|Download=The file example [http://forum.freecadweb.org/download/file.php?id=36559 Constraint_Draft00.FCStd]<br />[https://www.freecadweb.org/wiki/images/d/d8/Macro_Constraint_Draft.png ToolBar Icon]
}}

## Description

Simple example animation Draft wires by use the [expressions](Expressions.md) for associate many wires and simulate or verify the movement. Here the circle rotation create the movement for all objects connected

![](images/Constraint_Draft00.gif ) *Animation use the constraint expression*

## Uses

Download the file example [Constraint\_Draft00.FCStd](http://forum.freecadweb.org/download/file.php?id=36559), open it in FreeCAD

## Script

Select the **Line005\_with\_Code** object in the Combo View Select Data tab → Memo code → Code for rotation → ** ... ** (**This macro run with FreeCAD version 16** )

Select the complete code and paste in the Python Console

(If do not have the Python console: Menu → View → Panels → select Python console)

How copy the code snippet

![How copy the animation code](images/Constraint_Draft_Code01.gif )

ToolBar Icon ![](images/Macro_Constraint_Draft.png )

**Macro\_Constraint\_Draft.FCMacro**


{{MacroCode|code=

# Copy and pate this snippet in the FreeCAD console Python 
# mario52 19/04/2017

import FreeCADGui
import FreeCAD

#FreeCAD.Console.PrintMessage(str(FreeCAD.Version()) + "\n")
if int(FreeCAD.Version()[1]) == 16:    # Version de FreeCAD
    try:
        for i in range(0,360,5):
            App.getDocument("Constraint_Draft00").Circle.Placement=App.Placement(App.Vector(0,0,0), App.Rotation(i,0,0), App.Vector(0,0,0))
            FreeCADGui.updateGui()
            FreeCAD.ActiveDocument.recompute()
    except Exception:
        FreeCAD.Console.PrintMessage("You must download the Constraint_Draft00.FCStd file for run this macro" + "\n")
        import webbrowser 
        webbrowser.open("http://forum.freecadweb.org/download/file.php?id=36559")

else:
    FreeCAD.Console.PrintError("This macro run with the FreeCAD.Version 16 " + "\n")

}}

## Rotation with FreeCAD tools {#rotation_with_freecad_tools}

![Rotation with FreeCAD tools](images/Constraint_Draft01.gif )

## Link

The forum discussion [Sketch Feature to create linkage mechanism simulator](https://www.forum.freecadweb.org/viewtopic.php?f=22&t=21778&sid=28247565010ecdef0aa4f5c69e58f672)
