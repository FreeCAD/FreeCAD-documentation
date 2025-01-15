# NumPy/pl
## Wprowadzenie

Ta strona ma na celu udokumentowanie sposobu korzystania z [NumPy](https://numpy.org/) i FreeCAD.

numpy jest instalowany jako zależność FreeCAD, dzięki czemu można import numpy as np bez konieczności wcześniejszej instalacji, jak w normalnych środowiskach projektowych Python.



## Konwersja listy wektorów między FreeCAD Python i NumPy 



### Z Python do NumPy 


```python
import FreeCAD as App
import numpy as np

vector_list = [App.Vector(1, 0, 0), App.Vector(1, 2, 3), App.Vector(0, 3, 0)]
numpy_array = np.asarray(vector_list)
print(numpy_array)
```

Otrzymamy:


{{Code|lang=text|code=
[[ 1.  0.  0.]
 [ 1.  2.  3.]
 [ 0.  3.  0.]]
}}



### Z NumPy do Python 


```python
import FreeCAD as App
import numpy as np

cad_list = [App.Vector(itm) for itm in numpy_array]
print(cad_list)
```

Otrzymamy:


{{Code|lang=text|code=
[Vector (1.0, 0.0, 0.0), Vector (1.0, 2.0, 3.0), Vector (0.0, 3.0, 0.0)]
}}



## Projekty FreeCAD wykorzystujące NumPy 

-   <https://github.com/looooo/freecad.gears/blob/master/setup.py#L13>
-   <https://github.com/booya-at/OpenGlider/blob/develop/setup.py#L77>



## Forum FreeCAD 

-   [Czy są jacyś eksperci od NumPy?](https://forum.freecadweb.org/viewtopic.php?f=22&t=47529)



---
⏵ [documentation index](../README.md) > [3rd Party](Category_3rd%20Party.md) > NumPy/pl
