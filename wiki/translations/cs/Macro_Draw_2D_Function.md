# Macro Draw 2D Function/cs
{{Macro/cs
|Name=Draw 2D Function
|Translate=Vykresli 2D funkci
|Icon=Macro_Draw_2D_Function.png
|Description=Použijete k nakreslení funkce popsané "rovnicí" [z=F(x)] (Z-X rovina)
|Author=unknown
|Version=1.0
|Date=2011-08-01
|FCVersion=All
|Download=[https   *//www.freecadweb.org/wiki/images/3/36/Macro_Draw_2D_Function.png ToolBar Icon]
}}

## Description

Použijete k nakreslení funkce popsané \"rovnicí\" \[z=F(x)\] (Z-X rovina). Příklad ukázaný zde generuje parabolu.
Nemá žádné dialogové okno. Je potřeba definovat    *
F = proměnná použitá ve funkci,
X = iniciační hodnota x,
Nb = počet kroků,
Z = funkce vyjádřená x
ZZ = funkce vyjádřená xx

## Skript

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
for I in range(Nb)   *
    XX=X+Step 
    Z=X*X/(4*F)
    ZZ=XX*XX/(4*F)
    if I==0   *
        print( "Le test est vrai !")
        nomme=Part.makeLine((X,Y,Z),(XX,Y,ZZ))
        WWire=Part.Wire([nomme])
    else    *
        print( "Le test est 2 !")
        nomme=Part.makeLine((X,Y,Z),(XX,Y,ZZ))      
        WWire=Part.Wire([WWire,nomme])
    X=XX 
 
Part.show(WWire)

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Macro Draw 2D Function/cs
