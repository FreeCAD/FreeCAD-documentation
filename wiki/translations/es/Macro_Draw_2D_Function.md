# Macro Draw 2D Function/es
{{Macro/es
|Name=Draw 2D Function
|Translate=Draw 2D Function
|Icon=Macro_Draw_2D_Function.png
|Description= Utilízala para dibujar una función descrita por una "ecuación" [z=F(x)] (Z-X plano)
|Author=unknown
|Version=1.0
|Date=2011-08-01
|FCVersion=All
|Download=[https://www.freecadweb.org/wiki/images/3/36/Macro_Draw_2D_Function.png ToolBar Icon]
}}

## Descripción

Utilízala para dibujar una función descrita por una \"ecuación\" \[z=F(x)\] (Z-X plano) El ejemplo indicado aquí genera una parábola.

Necesita ser definida:

F=variable utilizada en la función,

X=Valor inicial de x,

Nb= Número de pasos,

Z=Función expresada express con x

ZZ=Función expresada express con xx

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
![](images/Right_arrow.png) [documentation index](../README.md) > Macro Draw 2D Function/es
