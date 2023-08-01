# Macro Draw 2D Function
{{Macro
|Name=Draw 2D Function
|Icon=Macro_Draw_2D_Function.png
|Description=Use it to draw a function described by a "equation" [z=F(x)] (Z-X plane)
|Author=unknown
|Version=1.0
|Date=2011-08-01
|FCVersion=All
|Download=[https://www.freecadweb.org/wiki/images/3/36/Macro_Draw_2D_Function.png ToolBar Icon]
}}

## Description

Use it to draw a function described by a \"equation\" \[z=F(x)\] (Z-X plane) The example done here generate a parabol. Has no dialog. Needs to be defined:

:   F = variable used in the function,
:   X = initial value of x,
:   Nb = Number of step,
:   Z = function express with x
:   ZZ = function express with xx

## Script



ToolBar Icon ![](images/Macro_Draw_2D_Function.png )

**Macro_Draw_2D_Function.FCMacro**


{{MacroCode|code=

# F = variable used in the function,
# X = initial value of x,
# Nb = Number of step,
# Z = function express with x
# ZZ = function express with xx

import FreeCAD, FreeCADGui, Part
import math
F=800
X=-500
Nb=10
Step=1000/Nb
Y=0
for I in range(Nb):
    XX=X+Step 
    Z=X*X/(4*F)
    ZZ=XX*XX/(4*F)
    if I==0:
        print( "Le test est vrai !")
        nomme=Part.makeLine((X,Y,Z),(XX,Y,ZZ))
        WWire=Part.Wire([nomme])
    else :
        print( "Le test est 2 !")
        nomme=Part.makeLine((X,Y,Z),(XX,Y,ZZ))      
        WWire=Part.Wire([WWire,nomme])
    X=XX 
 
Part.show(WWire)

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > Macro Draw 2D Function
