# NumPy/de
## Einführung

Diese Seite zielt darauf, die Nutzung von [NumPy](https://numpy.org/) mit FreeCAD zu dokumentieren.

numpy wird als Abhängigkeit von FreeCAD installiert, daher kannst du import numpy as np benutzen, ohne es zuerst installieren zu müssen wie in normalen Python-Projektumgebungen.



## Vektorliste zwischen FreeCAD-Python und NumPy konvertieren 



### Von Python zu NumPy 


```python
import FreeCAD as App
import numpy as np

vector_list = [App.Vector(1, 0, 0), App.Vector(1, 2, 3), App.Vector(0, 3, 0)]
numpy_array = np.asarray(vector_list)
print(numpy_array)
```

Output is:


{{Code|lang=text|code=
[[ 1.  0.  0.]
 [ 1.  2.  3.]
 [ 0.  3.  0.]]
}}



### Von NumPy zu Python 


```python
import FreeCAD as App
import numpy as np

cad_list = [App.Vector(itm) for itm in numpy_array]
print(cad_list)
```

Output is:


{{Code|lang=text|code=
[Vector (1.0, 0.0, 0.0), Vector (1.0, 2.0, 3.0), Vector (0.0, 3.0, 0.0)]
}}



## NumPy nutzende FreeCAD-Projekte 

-   <https://github.com/looooo/freecad.gears/blob/master/setup.py#L13>
-   <https://github.com/booya-at/OpenGlider/blob/develop/setup.py#L77>



## Diskussion im FreeCAD-Forum 

-   [Any numpy experts?](https://forum.freecadweb.org/viewtopic.php?f=22&t=47529) (engl.)



---
⏵ [documentation index](../README.md) > [3rd Party](Category_3rd%20Party.md) > NumPy/de
