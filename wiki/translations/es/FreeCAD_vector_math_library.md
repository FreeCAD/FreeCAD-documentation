# FreeCAD vector math library/es
## Introduction


<div class="mw-translate-fuzzy">

Este es un archivo de Python que contiene un par de funciones útiles para manejar los vectores de FreeCAD. Simplemente pega el siguiente código en un archivo de Python, e importa ese archivo en tu archivo de guión de Python para utilizarlo. Esta biblioteca está incluida en el [Módulo de croquizado](Draft_Workbench/es.md) y se puede acceder a ella desde el interprete de Python:


</div>


```python
import DraftVecUtils
```

Please note that this module was created a long time ago, when the `Vector` class didn\'t have many of its methods. Now these operations can be done by the Vector class itself.

Although the `DraftVecUtils` module still exists, and it is still used inside the [Draft Workbench](Draft_Workbench.md), it is probably better to use the `Vector` methods directly for new developments.

## Functions

Los vectores son los bloques sobre los que se construyen casi todas las operaciones geométricas 3D, así que es útil conocer algo sobre ellos para comprender como esas funciones pueden ser útiles para ti. Un par de buenas páginas para aprender los conceptos matemáticos básicos sobre vectores:

-   <http://en.wikipedia.org/wiki/Vector_space>
-   <http://es.wikipedia.org/wiki/Espacio_vectorial>
-   <http://maths-wiki.wikispaces.com/Vectors>
-   <http://darksleep.com/player/opengl_coordinate_system_and_matrix_math.html>


```python
"""Vector math library for FreeCAD"""

import math
import FreeCAD
 
def add(first, other):
    """add(Vector,Vector) - adds two vectors"""
    if isinstance(first,FreeCAD.Vector) and isinstance(other,FreeCAD.Vector):
        return FreeCAD.Vector(first.x+other.x, first.y+other.y, first.z+other.z)
 
def sub(first, other): 
    """sub(Vector,Vector) - subtracts second vector from first one"""
    if isinstance(first,FreeCAD.Vector) and isinstance(other,FreeCAD.Vector):
        return FreeCAD.Vector(first.x-other.x, first.y-other.y, first.z-other.z)
 
def scale(first,scalar):
    """scale(Vector,Float) - scales (multiplies) a vector by a factor"""
    if isinstance(first,FreeCAD.Vector):
        return FreeCAD.Vector(first.x*scalar, first.y*scalar, first.z*scalar)
 
def length(first):
    """lengh(Vector) - gives vector length"""
    if isinstance(first,FreeCAD.Vector):
        return math.sqrt(first.x*first.x + first.y*first.y + first.z*first.z)
 
def dist(first, other):
    """dist(Vector,Vector) - returns the distance between both points/vectors"""
    if isinstance(first,FreeCAD.Vector) and isinstance(other,FreeCAD.Vector):
        return length(sub(first,other))
 
def normalized(first):
    """normalized(Vector) - returns a unit vector"""
    if isinstance(first,FreeCAD.Vector):
        l=length(first)
        return FreeCAD.Vector(first.x/l, first.y/l, first.z/l)
 
def dotproduct(first, other):
    """dotproduct(Vector,Vector) - returns the dot product of both vectors"""
    if isinstance(first,FreeCAD.Vector) and isinstance(other,FreeCAD.Vector):
        return (first.x*other.x + first.y*other.y + first.z*other.z)
 
def crossproduct(first, other=FreeCAD.Vector(0,0,1)):
    """crossproduct(Vector,Vector) - returns the cross product of both vectors. 
    If only one is specified, cross product is made with vertical axis, thus returning its perpendicular in XY plane"""
    if isinstance(first,FreeCAD.Vector) and isinstance(other,FreeCAD.Vector):
        return FreeCAD.Vector(first.y*other.z - first.z*other.y, first.z*other.x - first.x*other.z, first.x*other.y - first.y*other.x)
 
def angle(first, other=FreeCAD.Vector(1,0,0)):
    """angle(Vector,Vector) - returns the angle in radians between the two vectors. 
    If only one is given, angle is between the vector and the horizontal East direction"""
    if isinstance(first,FreeCAD.Vector) and isinstance(other,FreeCAD.Vector):
        return math.acos(dotproduct(normalized(first),normalized(other)))
 
def project(first, other):
    """project(Vector,Vector): projects the first vector onto the second one"""
    if isinstance(first,FreeCAD.Vector) and isinstance(other,FreeCAD.Vector):
        return scale(other, dotproduct(first,other)/dotproduct(other,other))
```


{{Powerdocnavi

}} 

_ _

---
[documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > FreeCAD vector math library/es
