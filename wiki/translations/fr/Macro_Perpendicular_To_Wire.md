# Macro Perpendicular To Wire/fr
{{Macro/fr
|Name=Macro Perpendicular To Wire
|Icon=Macro_Perpendicular_To_Wire.png
|Description=Cette macro positionne un objet perpendiculairement au fil sélectionné.
|Author=Mario52
|Version=00.03
|Date=2020-03-31
|FCVersion=Tous
|Download=[https   *//www.freecadweb.org/wiki/images/0/0c/Macro_Perpendicular_To_Wire.png ToolBar Icon]
}}

## Description

Cette macro place l\'objet sélectionné perpendiculairement au fil sélectionné.

## Utilisation

1.  Installez la macro via le <img alt="" src=images/Std_AddonMgr.svg  style="width   *24px;"> [Gestionnaire des extensions](Std_AddonMgr/fr.md)
2.  Sélectionnez le chemin (peut être un élément ou un sous-élément)
3.  Sélectionnez l\'objet à aligner
4.  Exécuter la macro

## Script

L\'icône de la macro dans la barre d\'outils   * <img alt="" src=images/Macro_Perpendicular_To_Wire.png  style="width   *32px;">

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

## Options

Essentiellement, la ligne est coupée en x points avec `discretize()` (pour nos besoins, nous utilisons par défaut `Number&#61;500` mais les coupes peuvent être modulées entre 0 et 499)


```python
    pointsDirection = lineSelected.Shape.discretize(Number=500)             # discretize the path line first selection
```

1\. La perpendicularité est calculée entre 2 points   * 
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




Les autres paramètres de `discretize()` sont les suivants   *


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

## Exemples

![](images/Macro_Perpendicular_To_Wire_05.gif ) 

![](images/Macro_Perpendicular_To_Wire.gif )

## Discussions

-   Discussion sur le forum [https   *//forum.freecadweb.org/viewtopic.php?f=13&t=19899&start=20 Spiralbohrer](https   *//forum.freecadweb.org/viewtopic.php?f=13&t=19899&start=20_Spiralbohrer.md)
-   <http   *//forum.freecadweb.org/viewtopic.php?f=12&t=16336#p129468>

## Version

Ver 00.03 2020-03-21   * Corrections de fautes dans le code source et de commentaires Ver 00.02 2019-04-06    * Python 3



---
![](images/Right_arrow.png) [documentation index](../README.md) > Macro Perpendicular To Wire/fr
