 {{Macro/pl
|Name=Draw 2D Function
|Icon=Macro_Draw_2D_Function.png
|Description=Użyj go do narysowania funkcji opisanej ''równaniem [z=F(x)] (płaszczyzna Z-X)''
|Author=nieznany
|Version=1.0
|Date=2011-08-01
|FCVersion=Wszystkie
|Download=[https://www.freecadweb.org/wiki/images/3/36/Macro_Draw_2D_Function.png ikonka paska narzędzi]
}}

## Opis

Użyj jej do narysowania funkcji opisanej *równaniem \[z=F(x)\]* (płaszczyzna Z-X). Przykład wykonany tutaj generuje parabolę. Nie ma okna dialogowego. Wymaga zdefiniowania:

:   F = zmienna używana w funkcji,

X = wartość początkowa x,

:   Nb = liczba kroków,
:   Z = funkcja wyrażona przez x
:   ZZ = funkcja wyrażona przez xx

## Tworzenie skryptów {#tworzenie_skryptów}

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

