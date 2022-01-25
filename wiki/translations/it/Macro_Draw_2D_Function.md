# Macro Draw 2D Function/it
{{Macro/it
|Name=Draw 2D Function
|Icon=Macro_Draw_2D_Function.png
|Translate=Funzione 2D
|Description= Si usa per disegnare una funzione descritta da una equazione z=F(x) (piano Z-X)
|Author=ignoto
|Version=1.0
|Date=2011-08-01
|FCVersion=Tutte versione
|Download=[https://www.freecadweb.org/wiki/images/3/36/Macro_Draw_2D_Function.png Icona per la ToolBar]
}}

## Description

Si usa per disegnare una funzione descritta da una equazione \[z=F(x)\] (piano ZX). Questo esempio genera una parabola.

Elementi da definire:

:   F=variable utilizzata nella funzione,





:   X=Valore iniziale di x,





:   Nb= Numero di passi,





:   Z=Funzione espressa con x





:   ZZ=Funzione espressa con xx

## Script

ToolBar Icon ![](images/Macro_Draw_2D_Function.png )

**Macro\_Draw\_2D\_Function.FCMacro**


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
![](images/Right_arrow.png) [documentation index](../README.md) > Macro Draw 2D Function/it
