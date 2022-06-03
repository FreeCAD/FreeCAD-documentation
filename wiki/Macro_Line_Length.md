# Macro Line Length
{{Macro
|Name=Macro Line Length
|Icon=Macro_Line_Length.png
|Description=Create a line giving as an argument the XYZ coordinates, length, and angle. The new line is created in the real coordinate of object, not in the coordinate of the Body.<br/>{{ColoredText|(Command line, paste this complete macro in the Python console)}}.
|Author=mario52
|Version=02.00
|Date=2014-08-08
|FCVersion=All
|Download=[https   *//www.freecadweb.org/wiki/images/b/bd/Macro_Line_Length.png ToolBar Icon]
}}

## Description

This small macro create a line giving as an argument the XYZ coordinates, length, and angle

## Usage

Can be used from the Freecad macro editor.

the default values are    * x1 = 0, y1 = 0, z1 = 0, length = 10, angle = 0

## Script



ToolBar Icon ![](images/Macro_Line_Length.png )

**Macro Line\_Length.py**


{{MacroCode|code=
# -*- coding   * utf-8 -*-
# créer une ligne avec une coordonnée une longueur et un angle sur le plan X Y
# create line with coordinate length and angle to plane X Y
import FreeCAD, FreeCADGui, Draft
from math import cos, sin, radians
#from FreeCAD import Base
 
def line_length(x1 = 0.0, y1 = 0.0, z1 = 0.0, length = 10.0, angle = 0.0)   *
    x2 = x1 + (length * cos(radians(angle)))
    y2 = y1 + (length * sin(radians(angle)))
    z2 = z1 #+ ()
    Draft.makeWire([FreeCAD.Vector(x1,y1,z1),FreeCAD.Vector(x2,y2,z2)])

#Example   *
#x1 = 0.0          # Edit coordinate x1 origin
#y1 = 0.0          # Edit coordinate y1 origin
#z1 = 0.0          # Edit coordinate z1 origin
#length = 50.0       # Edit length
#angle  = 45.0       # Edit angle plane XY
 
#line_length(x1, y1, z1, length, angle)

}}






## Example

If the macro is copied in the Python console, you can use it by   * 


```python
>>> line_length(x1 = 0, y1 = 0, z1 = 0, length = 10, angle = 45)
```



or choice 


```python
>>> line_length(x1 = 10, y1 = 10, z1 = 0, length = 50)

>>> line_length(length = 50, angle = 45)
```



---
![](images/Right_arrow.png) [documentation index](../README.md) > Macro Line Length
