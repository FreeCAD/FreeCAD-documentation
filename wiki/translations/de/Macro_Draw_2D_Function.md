 {{Macro/de
|Name=Draw 2D Function
|Translate=Draw 2D Function
|Icon=Macro_Draw_2D_Function.png
|Description=Zeichnen Sie eine durch eine "Gleichung" beschriebene Funktion [z = F (x)] (Z-X-Ebene).
|Author=unknown
|Version=1.0
|Date=2011-08-01
|FCVersion=All
|Download=[https://www.freecadweb.org/wiki/images/3/36/Macro_Draw_2D_Function.png ToolBar Icon]
}}

## Beschreibung

Verwenden Sie es, um eine Funktion zu zeichnen, die durch eine \"Gleichung\" beschrieben wird \[z = F (x)\] (Z-X-Ebene). Das hier ausgeführte Beispiel erzeugt einen Parabol. Hat keinen Dialog Muss definiert werden:

:   F = in der Funktion verwendete Variable,
:   X = Anfangswert von x,
:   Nb = Nummer der Stufe,
:   Z = Funktion mit x ausdrücken
:   ZZ = Funktion Express mit xx

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

