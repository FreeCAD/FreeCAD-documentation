# Macro Line Length/fr
{{Macro/fr
|Name=Macro Line_Length
|Icon=Macro_Line_Length.png
|Description=Crée une ligne (en ligne de commande) en donnant les coordonnées XYZ, la longueur, et un angle.La nouvelle ligne est créée dans les coordonnées réelles de l'objet et non dans celles du corps.<br/>{{ColoredText|(Ligne de commande, collez cette macro complète dans la console Python)}}.
|Author=mario52
|Version=02.00
|Date=2014-08-08
|Download=[https://www.freecadweb.org/wiki/images/b/bd/Macro_Line_Length.png ToolBar Icon]
}}

## Description

Cette petite macro crée une ligne en donnant comme argument, ces coordonnées de départ XYZ, sa longueur et un angle

## Utilisation

Peut être utilisée dans l\'éditeur de macro de FreeCAD.

the default values are : x1 = 0, y1 = 0, z1 = 0, length = 10, angle = 0

## Script

ToolBar Icon ![](images/Macro_Line_Length.png )

**Macro Line_Length.py**


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




## Exemple

Si vous copiez la macro dans la console Python, vous pouvez l\'utiliser de cette façon:


```python
>>> line_length(x1 = 0, y1 = 0, z1 = 0, length = 10, angle = 45)
```

ou au choix


```python
>>> line_length(x1 = 10, y1 = 10, z1 = 0, length = 50)

>>> line_length(length = 50, angle = 45)
```



---
⏵ [documentation index](../README.md) > Macro Line Length/fr
