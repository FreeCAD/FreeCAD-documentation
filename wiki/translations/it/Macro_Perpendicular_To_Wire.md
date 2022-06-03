# Macro Perpendicular To Wire/it
<div class="mw-translate-fuzzy">


{{Macro/it
|Name=Macro Perpendicular To Wire
|Icon=Macro_Perpendicular_To_Wire.png
|Translate=Perpendicolare a linea
|Description=Posiziona l'oggetto perpendicolarmente alla linea selezionata.<br />Versione 00.02    * 2019-04-06. Icona per la ToolBar   * [https   *//www.freecadweb.org/wiki/images/0/0c/Macro_Perpendicular_To_Wire.png Icon].<br />
|Author=Mario52
|Version=00.02
|Date=2019-04-06
|FCVersion=All
|Download=[https   *//www.freecadweb.org/wiki/images/0/0c/Macro_Perpendicular_To_Wire.png ToolBar Icon]
}}


</div>


<div class="mw-translate-fuzzy">

## Descrizione

Posiziona l\'oggetto perpendicolarmente alla linea selezionata.


</div>


<div class="mw-translate-fuzzy">

## Uso


</div>


<div class="mw-translate-fuzzy">

1.     * selezionare il percorso (può essere un elemento o un sotto-elemento)
2.     * selezionare l\'oggetto da posizionare
3.     * eseguire la macro


</div>

## Script


<div class="mw-translate-fuzzy">

L\'icona per la barra degli strumenti ![](images/Macro_Perpendicular_To_Wire.png )


</div>

**Macro Perpendicular To Wire.FCMacro**


{{MacroCode|code=
# -*- coding   * utf-8 -*-
__title__   = "Macro Perpendicular To Wire"
__author__  = "Mario52"
__url__     = "https   *//wiki.freecadweb.org/Macro_Perpendicular_To_Wire"
__version__ = "00.03"
__date__    = "31/03/2020"

import Draft, Part

try   *
    sel = FreeCADGui.Selection.getSelection()                               # Select an objectlineSelected = FreeCADGui.Selection.getSelectionEx()[0].SubObjects[0]   # first object the Path object or SubObjects
    myCircle     = sel[1]                                                   # second objectpointsDirection  = []pointsDirection = lineSelected.discretize(Number=500)                   # discretize the path line first selectionv=pointsDirection[0].sub(pointsDirection[1])                            # avec vecteurs 1 et 2 (direction debut ligne)
    r=App.Rotation(App.Vector(0,0,1),v)pl=FreeCAD.Placement()                                                  # placement object
    pl.Rotation.Q = r.Q
    pl.Base = pointsDirection[0]
    myCircle.Placement = pldel pointsDirection[   *]
    FreeCAD.ActiveDocument.recompute()
except Exception   *
    print( "Select two objects. 1   *The path 2   *The object to align" )

}}

## Opzioni


<div class="mw-translate-fuzzy">

Principio di funzionamento    *


</div>


```python
    pointsDirection = lineSelected.Shape.discretize(Number=500)             # discretize the path line first selection
```


<div class="mw-translate-fuzzy">

la perpendicolarità è calcolata tra 2 punti modificando    *


</div>


```python
v=pointsDirection[0].sub(pointsDirection[1])          # perpendicular of first > second point
```


   *   ![](images/Macro_Perpendicular_To_Wire_01.png )




2   *


```python
v=pointsDirection[-1].sub(pointsDirection[-2])       # perpendicular of last > before last point
pl.Base = pointsDirection[-1]                        # position base last point```


   *   ![](images/Macro_Perpendicular_To_Wire_02.png )




3   *


```python
v=pointsDirection[100].sub(pointsDirection[101])   # perpendicular of point 100 > point 101
pl.Base = pointsDirection[100]                     # position base point 100```


   *   ![](images/Macro_Perpendicular_To_Wire_03.png )




4   *


```python
v=pointsDirection[0].sub(pointsDirection[-1])         # perpendicular of first point > last point
pl.Base = pointsDirection[0]                          # position base first point```


   *   ![](images/Macro_Perpendicular_To_Wire_04.png )





<div class="mw-translate-fuzzy">

per discretizzare gli altri parametri


</div>


```python
# Discretizes the edge and returns a list of points.
# Forum thread   * http   *//forum.freecadweb.org/viewtopic.php?f=12&t=16336#p129468
# The function accepts keywords as argument   *
# discretize(Number=n) => gives a list of 'n' equidistant points
# discretize(QuasiNumber=n) => gives a list of 'n' quasi equidistant points (is faster than the method above)
# discretize(Distance=d) => gives a list of equidistant points with distance 'd'
# discretize(Deflection=d) => gives a list of points with a maximum deflection 'd' to the edge
# discretize(QuasiDeflection=d) => gives a list of points with a maximum deflection 'd' to the edge (faster)
# discretize(Angular=a,Curvature=c,[Minimum=m]) => gives a list of points with an angular deflection of 'a'
# and a curvature deflection of 'c'. Optionally a minimum number of points
# can be set which by default is set to 2.
```

## Esempio

![](images/Macro_Perpendicular_To_Wire_05.gif ) 

![](images/Macro_Perpendicular_To_Wire.gif )

## Discussions


<div class="mw-translate-fuzzy">

La discussione nel forum [https   *//forum.freecadweb.org/viewtopic.php?f=13&t=19899&start=20 Spiralbohrer](https   *//forum.freecadweb.org/viewtopic.php?f=13&t=19899&start=20_Spiralbohrer.md)


</div>


<div class="mw-translate-fuzzy">

## Version

Ver 00.02 2019-04-06    * Python 3


</div>

Ver 00.03 2020-03-21   * Source and comment typo fixes Ver 00.02 2019-04-06   * Python 3



---
![](images/Right_arrow.png) [documentation index](../README.md) > Macro Perpendicular To Wire/it
