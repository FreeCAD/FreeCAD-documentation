# Macro Line Length/it
 {{Macro/it
|Name=Macro Line_Length
|Translate=Linea e opzioni
|Icon=Macro_Line_Length.png
|Description=Crea una linea usando come argomento le coordinate XYZ, la lunghezza e l'angolo.La nuova linea viene creata nella coordinata reale dell'oggetto, non nelle coordinate del corpo.<br/>{{ColoredText|(Riga di comando, incolla questa macro completa nella console Python)}}.
|Author=mario52
|Version=02.00
|Date=2014-08-08
|FCVersion=Tutte
|Download=[https://www.freecadweb.org/wiki/images/b/bd/Macro_Line_Length.png ToolBar Icon]
}}

## Descrizione

Questa macro permette di creare una linea usando come argomento le coordinate XYZ, la lunghezza e l\'angolo.


<div class="mw-translate-fuzzy">

## Uso

Può essere usata nell\'editor delle macro di FreeCAD.


</div>

i valori di default sono : x1=0, y1=0, z1=0, length=10, angle=0

## Script

ToolBar Icon ![](images/Macro_Line_Length.png )

**Macro Line\_Length.py**


{{MacroCode|code=
# -*- coding: utf-8 -*-
# créer une ligne avec une coordonnée une longueur et un angle sur le plan X Y
# create line with coordinate length and angle to plane X Y
import FreeCAD, FreeCADGui, Draft
from math import cos, sin, radians
#from FreeCAD import Base
 
def line_length(x1 = 0.0, y1 = 0.0, z1 = 0.0, length = 10.0, angle = 0.0):
    x2 = x1 + (length * cos(radians(angle)))
    y2 = y1 + (length * sin(radians(angle)))
    z2 = z1 #+ ()
    Draft.makeWire([FreeCAD.Vector(x1,y1,z1),FreeCAD.Vector(x2,y2,z2)])

#Example:
#x1 = 0.0          # Edit coordinate x1 origin
#y1 = 0.0          # Edit coordinate y1 origin
#z1 = 0.0          # Edit coordinate z1 origin
#length = 50.0       # Edit length
#angle  = 45.0       # Edit angle plane XY
 
#line_length(x1, y1, z1, length, angle)

}}




## Esempio

Se la macro viene copiata nella console Python può essere utilizzata con:


```python
>>> line_length(x1 = 0, y1 = 0, z1 = 0, length = 10, angle = 45)
```

oppure, a scelta:


```python
>>> line_length(x1 = 10, y1 = 10, z1 = 0, length = 50)

>>> line_length(length = 50, angle = 45)
```

