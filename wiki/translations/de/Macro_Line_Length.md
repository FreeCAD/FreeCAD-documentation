# Macro Line Length/de
{{Macro/de
|Name=Macro Line Length
|Translate=Macro Line Length
|Icon=Macro_Line_Length.png
|Description=Erzeugt eine Linie, in der die XYZ-Koordinaten, die Länge und der Winkel als Argument angegeben werden.Die neue Zeile wird in der realen Koordinate des Objekts erstellt, nicht in der Koordinate des Körpers.<br/>{{ColoredText|(Befehlszeile, fügen Sie dieses vollständige Makro in die Python-Konsole ein)}}.
|Author=mario52
|Version=02.00
|Date=2014-08-08
|FCVersion=All
|Download=[https://www.freecadweb.org/wiki/images/b/bd/Macro_Line_Length.png ToolBar Icon]
}}

## Beschreibung

Dieses kleine Makro erstellt eine Linie, in der die XYZ-Koordinaten, die Länge und der Winkel als Argument angegeben werden

## Anwendung

Kann vom Freecad-Makro-Editor verwendet werden.

Die Standardwerte sind: x1 = 0, y1 = 0, z1 = 0, Länge = 10, Winkel = 0

## Skript

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




## Beispiel

Wenn das Makro in die Python-Konsole kopiert wird, können Sie es folgendermaßen verwenden:


```python
>>> line_length(x1 = 0, y1 = 0, z1 = 0, length = 10, angle = 45)
```

oder Wahl


```python
>>> line_length(x1 = 10, y1 = 10, z1 = 0, length = 50)

>>> line_length(length = 50, angle = 45)
```



---
![](images/Right_arrow.png) [documentation index](../README.md) > Macro Line Length/de
