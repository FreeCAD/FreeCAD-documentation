# Macro WireXYZ/fr
{{Macro/fr
|Name=WireXYZ
|Icon=Macro_WireXYZ.png
|Description=Crée un wire avec les coordonnées x y z séparées par un espace. Les données sont extraites d'un fichier.<br/>{{ColoredText|(Ligne de commande, collez cette macro complète dans la console Python)}}.
|Author=Mario52
|Version=0.3
|Date=2020-10-16
|FCVersion=All
|SeeAlso=[Macro_Dxf_To_Shape](Macro_Dxf_To_Shape.md) <img src="images/Macro_Dxf_To_Shape.png" width=24px>
|Download=[https://www.freecadweb.org/wiki/images/0/0a/Macro_WireXYZ.png ToolBar Icon]
}}

## Description

Cette macro crée un wire (ou points) avec les coordonnées XYZ extraites d\'un fichier. Les coordonnées X Y Z sont séparées par un espace.

## Utilisation

Le fichier doit avoir les coordonnées X Y Z au ASCII sans entête.

## Script

ToolBar Icon ![](images/Macro_WireXYZ.png )

**Macro\_WireXYZ.FCMacro**


{{MacroCode|code=
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# created a wire with coordinate x y z separated (in the file without coma)
__title__= "Macro_WireXYZ"
__author__= "Mario52"
__date__= "2020/10/16"
__version__= "00.03"
##
#EX:
#0 0 0
#10 10 10
#15 20 25
#. . . .

from FreeCAD import Base
import Draft, Part

## path for Windows    : C:\yourPath\cloud.asc (create one error in Python (cause, the "\" is a command syntax in Python)
## replace "\" by "/"  result : C:/yourPath/cloud.asc 
## or replace the "\" by "\\" result : C:\\yourPath\\cloud.asc 

fichier = "C:\\yourPath\\cloud.asc"                          # path and name of file.txt

file = open(fichier, "r")                                  # open the file read
wire = []
X=Y=Z = 0.0

for ligne in file:
    coordinates = ligne.split()
    try:                                                        # for format PCD ignore the header
        X,Y,Z = coordinates                                     # separate the coordinates
#        Draft.makePoint(float(X),float(Y),float(Z))            # create points (uncomment for use)
        print(X," ",Y," ",Z)
        wire.append(FreeCAD.Vector(float(X),float(Y),float(Z))) # append the coordinates
    except Exception:
        None
file.close()
Draft.makeWire(wire,closed=False,face=False,support=None)   # create the wire open
#Draft.makeWire(wire,closed=True,face=False,support=None)   # create the wire closed (uncomment for use)

#Draft.makeBSpline(wire,closed=False,face=False,support=None)# create the BSpline open (uncomment for use)
#Draft.makeBSpline(wire,closed=True,face=False,support=None)# create the BSpline open (uncomment for use)

App.ActiveDocument.recompute()

}}

## Exemples


```python
0 240.42686 0

20 243.83054 0

40 247.33677 0

60 250.94702 0

80 254.66283 0

100 258.48575 0

...
```

Modifiez le chemin et nom du fichier, sauvez la macro, rechargez la macro et lancez la.


```python
fichier = "C:\yourPath\cloud.asc"                          # path and name of file.txt

## path for Windows    : C:\yourPath\cloud.asc (create one error in Python (cause, the "\" is a command syntax in Python)
## replace "\" by "/"  result : C:/yourPath/cloud.asc 
## or replace the "\" by "\\" result : C:\\yourPath\\cloud.asc 

```

Si vous voulez un wire fermé, modifiez le code (closed=False):


```python
Draft.makeWire(wire,closed=False,face=False,support=None)   # create the wire open
```

et remplacez le par (closed=True)


```python
Draft.makeWire(wire,closed=True,face=False,support=None)   # create the wire closed
```

même procédure pour la face, False ou True (face=True).

## Liens

La discussion sur le forum [How do I transform a point cloud to a line?](http://forum.freecadweb.org/viewtopic.php?f=3&t=7828)

## Version

00.03 16/10/2020 : conversion pour Python 3, ajout d\'info pour le chemin du fichier dans \"Windows\" remplacer le slatch \"\\\" par \"\\\\\" ou \"/\" voir [How do I transform a point cloud to a line?](https://forum.freecadweb.org/viewtopic.php?f=3&t=7828)

00.02 02/07/2019 :

00.01 21/02/2015



---
![](images/Right_arrow.png) [documentation index](../README.md) > Macro WireXYZ/fr
