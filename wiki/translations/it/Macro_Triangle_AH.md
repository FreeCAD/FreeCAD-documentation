# Macro Triangle AH/it
{{Macro/it
|Name=Macro Triangle AH
|Translate=Triangolo AH
|Icon=Macro_Triangle_AH.png
|Description=Questa macro crea un triangolo isoscele dati l'angolo e l'altezza. Il nuovo triangolo viene creato nella coordinata reale.<br/>{{ColoredText|(Riga di comando, incolla questa macro completa nella console Python)}}.
|Author=mario52
|Version=00.03
|Date=2019/07/02
|FCVersion=Tutte
|Download=[https   *//www.freecadweb.org/wiki/images/4/41/Macro_Triangle_AH.png ToolBar icon]
}}

## Descrizione

Questa macro crea un triangolo isoscele dati l\'angolo e l\'altezza (il vertice è posizionato nel punto 0,0,0)

## Uso

Copiare la macro **Triangolo AH** nella console Python di FreeCAD

## Script

ToolBar Icon ![](images/Macro_Triangle_AH.png )

**Macro\_triangleAH.FCMacro**


{{MacroCode|code=
__title__   = "triangleAH"
__author__  = "Mario52"
__version__ = "00.03"
__date__    = "2019/07/02"
# Give angle and on choice    * height or base or hypo
from math import cos, sin, tan, degrees, radians, sqrt
import Draft, Part
def triangleAH(angle, height=0.0, base=0.0, hypo=0.0)   *
    def line_length(x1 = 0.0, y1 = 0.0, z1 = 0.0, length = 10.0, angle2 = 0.0)   *  # search coordinates
        x2 = x1 + (length * cos(radians(angle2)))
        y2 = y1 + (length * sin(radians(angle2)))
        z2 = z1 #+ ()
        return x2,y2,z2                                                          # return coordinates (xyz) to point
 
    x0 = y0 = z0 = 0.0
    angle = float(angle)
    height = float(height)
    base = float(base)
    if base != 0   *
        height = ( (base/2) / (tan(radians(angle/2))) )                          # imposing base and calculate height
    if hypo != 0   *
        height = hypo * (cos(radians(angle/2)))                                  # imposing hypo and calculate height 
    else   *
        hypo = height / cos(radians(angle/2))                                    # calculate hypotenuse
    if base==0   *                                                                  # base of triangle
        base = (tan(radians(angle/2) ) * height) * 2                             # calculate base
    a0 = line_length(x1=x0,y1=y0,z1=z0,length=height,angle2=0 )                  # coord height of triangle
    a0 = line_length(x1=x0,y1=y0,z1=z0,length=0, angle2 = angle )                # point 0 (begin vertex)
    a  = line_length(x1=a0[0],y1=a0[1],z1=a0[2],length= hypo, angle2=-(angle/2)) #
    b  = line_length(a[0],a[1],a[2],length= (abs(a[1])*2), angle2=90.0)          # base of triangle = (abs(a[1])*2)
    ##
    print()
    print("angle theet    * ", angle)
    print("angles base    * (", (180.0-angle)/2.0,"),(",(180-angle)/2.0,")")
    print("height         * ", height)
    print("base           * ", base)
    print("hypotenuse     * ", hypo)
    print("surface        * ", (base * height) / 2.0)
    print("_________________________")
    Draft.makeWire([FreeCAD.Vector(a0),FreeCAD.Vector(a),FreeCAD.Vector(b)],closed=True,face=True,support=None) # create triangle
    App.ActiveDocument.recompute()

#Example
#triangleAH(angle=90, height=10)
#triangleAH(90, 10)
#triangleAH(45, hypo=10)


}}

## Esempi


```python
triangleAH(angle=90, height=10)
# or
triangleAH(90, 10)
# or
triangleAH(45, hypo=10)
# or
triangleAH(90, base=10)
```

## Versioni

ver 00.03 2019/07/02 aggiunto \"App.ActiveDocument.recompute()\" e conversione verso Py3

ver 00.02 03/05/2015    * aggiunto \"base=0.0\", \"hypo=0.0\" dati del triangolo

ver 00.01 20/03/2015    *



---
![](images/Right_arrow.png) [documentation index](../README.md) > Macro Triangle AH/it
