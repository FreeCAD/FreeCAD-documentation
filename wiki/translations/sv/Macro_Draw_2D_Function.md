# Macro Draw 2D Function/sv
{{Macro/sv
|Name=Draw 2D Function
|Translate=Rita 2D-funktionen
|Icon=Macro_Draw_2D_Function.png
|Description=Använd den för att rita en funktion som beskrivs av en "ekvation" [z=F(x)] (Z-X plane)
|Author=unknown
|Version=1.0
|Date=2011-08-01
|FCVersion=All
|Download=[https://www.freecadweb.org/wiki/images/3/36/Macro_Draw_2D_Function.png ToolBar Icon]
}}

## Beskrivning

Använd den för att rita en funktion som beskrivs av en \"ekvation\" \[z=F(x)\] (Z-X plan) Exemplet här genererar en parabol. Behöver definieras :

F=variabel som används i funktionen,

X=startvärde på x,

Nb= antal steg,

Z=funktionsuttryck med x

ZZ=funktionsuttryck med xx

## Manus

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
⏵ [documentation index](../README.md) > Macro Draw 2D Function/sv
