# NumPy/it
## Introduzione

Questa pagina ha lo scopo di documentare come utilizzare [numpy](https://numpy.org/NumPy) con FreeCAD.

numpy viene installato come dipendenza di FreeCAD, quindi è possibile fare import numpy as np senza doverlo prima installare come nei normali ambienti di sviluppo di Python.



## Convertire una lista di vettori tra FreeCAD Python e NumPy 



### Da Python a NumPy 


```python
import FreeCAD as App
import numpy as np

vector_list = [App.Vector(1, 0, 0), App.Vector(1, 2, 3), App.Vector(0, 3, 0)]
numpy_array = np.asarray(vector_list)
print(numpy_array)
```

L\'output è:


{{Code|lang=text|code=
[[ 1.  0.  0.]
 [ 1.  2.  3.]
 [ 0.  3.  0.]]
}}



### Da NumPy a Python 


```python
import FreeCAD as App
import numpy as np

cad_list = [App.Vector(itm) for itm in numpy_array]
print(cad_list)
```

L\'output è:


{{Code|lang=text|code=
[Vector (1.0, 0.0, 0.0), Vector (1.0, 2.0, 3.0), Vector (0.0, 3.0, 0.0)]
}}



## Progetti FreeCAD che utilizzano NumPy 

-   <https://github.com/looooo/freecad.gears/blob/master/setup.py#L13>
-   <https://github.com/booya-at/OpenGlider/blob/develop/setup.py#L77>



## Discussione nel forum di FreeCAD 

-   [Qualche esperto in numpy?](https://forum.freecadweb.org/viewtopic.php?f=22&t=47529)



---
⏵ [documentation index](../README.md) > [3rd Party](Category_3rd Party.md) > NumPy/it
