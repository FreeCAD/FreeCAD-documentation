# Macro Draw Parametric 2D Function/de

 {{Macro/de
|Name=Macro Draw Parametric 2D Function
|Icon=Macro_Draw_Parametric_2D_Function.png
|Translate=Macro Draw Parametric 2D Function
|Description=Zeichnet 2-dimensionale, parametrische und optional polare Gleichungen.
|Author=T4b
|Version=1.0
|Date=2012-08-30
|FCVersion=All
|Download=[https://www.freecadweb.org/wiki/images/0/03/Macro_Draw_Parametric_2D_Function.png ToolBar Icon]
}}

## Beschreibung

Zeichnet 2-dimensionale, parametrische und optional polare Gleichungen.

<img alt="" src=images/Macro_drawParametric2Dfunction.png  style="width:480px;"> 
*DrawParametric2DFunction*

## Einschränkungen

Hat noch ein paar Fehler und vermisst einige Funktionen. Die Dokumentation befindet sich in den Dokumentenketten.

## Anwendung

Art :

Beispielverwendung:

draw2Dfunction(xFunction=\"0.5\*n\", yFunction=\"-0.75\*n\", n=0, nd=-math.pi, step=50, pol=1)

## Skript

ToolBar Icon ![](images/Macro_Draw_Parametric_2D_Function.png )

**Macro\_drawParametric2DFunction.FCMacro**


{{MacroCode|code=

import FreeCAD, FreeCADGui, Part
import math

def evalFunction(suppliedFunction, n):
    """This function uses eval to evaluate suppliedFunction.It does in no way check whether suppliedFunction is evil, thus it is itself evil!
    """
    return eval(suppliedFunction)

def draw2Dfunction(xFunction="n", yFunction="n", n=-5, nd=10, step=10, z=0, pol=0):
    """Draws 2-dimensional mathemathical functionsThe function is drawn for n's between n and n+nd, in steps of 1/step, on the z-coordinate z.
    Equations for x and y can be given (xFunction and yFunction arguments), they default to n.If pol=1 then x is interpreted as r and y is interpreted as t.
    """
    nStart=n
    while math.fabs(n-nd)-1.0/step>0:
        print( "n: " + str(n))
        x=evalFunction(xFunction, n)
        y=evalFunction(yFunction, n)
        nNext=n+math.copysign(1,nd-n)/step 
        print( "nNext: " + str(nNext))
        xNext=evalFunction(xFunction, nNext)
        yNext=evalFunction(yFunction, nNext)
        if pol==0:
            nextSeg=(x,y,z),(xNext,yNext,z)
        else:
            nextSeg=(x*math.cos(y),x*math.sin(y),z),(xNext*math.cos(yNext),xNext*math.sin(yNext),z)
        print( "nextSeg: " + str(nextSeg))
        nomme=Part.makeLine(*nextSeg)
        if n==nStart:
            WWire=Part.Wire([nomme])
        else:
            WWire=Part.Wire([WWire,nomme])
        n=nNext
    Part.show(WWire)
#Example usage:
draw2Dfunction(xFunction="0.5*n", yFunction="-0.75*n", n=0, nd=-math.pi, step=50, pol=1)

}}

