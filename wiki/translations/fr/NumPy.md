# NumPy/fr
{{TOCright}}

## Introduction

Cette page vise à documenter comment utiliser [NumPy](https   *//numpy.org/) avec FreeCAD.

numpy est installé en tant que dépendance de FreeCAD, vous pouvez donc importer numpy en tant que np sans avoir à l\'installer au préalable comme dans les environnements de projet Python normaux.

## Convertir une liste de vecteurs entre FreeCAD Python et NumPy 

### De Python à NumPy 


```python
import FreeCAD as App
import numpy as np

vector_list = [App.Vector(1, 0, 0), App.Vector(1, 2, 3), App.Vector(0, 3, 0)]
numpy_array = np.asarray(vector_list)
print(numpy_array)
```

Le résultat est    *


{{Code|lang=text|code=
[[ 1.  0.  0.]
 [ 1.  2.  3.]
 [ 0.  3.  0.]]
}}

### De NumPy à Python 


```python
import FreeCAD as App
import numpy as np

cad_list = [App.Vector(itm) for itm in numpy_array]
print(cad_list)
```

Le résultat est    *


{{Code|lang=text|code=
[Vector (1.0, 0.0, 0.0), Vector (1.0, 2.0, 3.0), Vector (0.0, 3.0, 0.0)]
}}

## Projets FreeCAD utilisant NumPy 

-   <https   *//github.com/looooo/freecad.gears/blob/master/setup.py#L13>
-   <https   *//github.com/booya-at/OpenGlider/blob/develop/setup.py#L77>

## Discussion sur le forum FreeCAD 

-   [Any numpy experts?](https   *//forum.freecadweb.org/viewtopic.php?f=22&t=47529)



[Category   *3rd Party](Category_3rd_Party.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [3rd Party](Category_3rd Party.md) > NumPy/fr
