 {{Macro/fr
|Name=Draw 2D Function
|Icon=Macro_Draw_2D_Function.png
|Description=Trace une fonction décrite par une équation [z=F(x)] (Z-X plan)
|Author=unknown
|Version=1.0
|Date=2011-08-01
|FCVersion=Toutes versions
|Download=[https://www.freecadweb.org/wiki/images/3/36/Macro_Draw_2D_Function.png Icône pour votre barre d'outils]
}}

## Description

Utilisez ce script pour tracer une fonction décrite par une équation \[z=F(x)\] (Z-X plane) L\'exemple donné ici génère une parabole.

Éléments à définir :

:   F = variable utilisée dans la fonction,





:   X = valeur initiale de x,





:   Nb = Nombre d\'étapes,





:   Z = fonction express avec x





:   ZZ = fonction express avec xx

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

