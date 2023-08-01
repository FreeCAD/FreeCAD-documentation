---
- GuiCommand:/pl
   Name:Surface BlendCurve
   Name/pl:Powierzchnia 3D: Krzywa łącząca
   MenuLocation:Powierzchnia → Krzywa łącząca
   Workbenches:[Powierzchnia 3D](Surface_Workbench/pl.md)
   Version:0.21
---

# Surface BlendCurve/pl



## Opis

Narzędzie **Krzywa łącząca** tworzy krzywą Bezier\'a między dwiema krawędziami, z zachowaniem pożądanej ciągłości.

Geometria bazowa może należeć do krzywych utworzonych za pomocą środowiska [Rysunek Roboczy](Draft_Workbench/pl.md) lub [Szkicownik](Sketcher_Workbench/pl.md), ale może również należeć do obiektów bryłowych, takich jak te utworzone za pomocą środowiska [Część](Part_Workbench/pl.md).

<img alt="" src=images/Surface_BlendCurve_G3_example.png  style="width:400px;"> <img alt="" src=images/Surface_BlendCurve_Comb.png  style="width:400px;">


<div lang="en" dir="ltr" class="mw-content-ltr">



*Surface Blend Curve joining 2 edges with G3 continuity. Orange polygon represent the control points. Curvature comb (from [Curves addon](Curves_Workbench.md)) is smooth at contact points.*


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

## Usage


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

1.  Select two edges in the [3D view](3D_view.md)
2.  There are several ways to invoke the command:
    -   Press the **<img src="images/Surface_BlendCurve.svg" width=16px> [Surface Blend Curve](Surface_BlendCurve.md)** button.
    -   Select the **Surface → <img src="images/Surface_BlendCurve.svg" width=16px> Blend Curve** option from the menu.
3.  Adjust the curve shape in the object Data properties


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

## Properties


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

A [Surface Blend Curve](Surface_BlendCurve.md) is derived from the basic [Part Feature](Part_Feature.md) (`Part::Feature` class, through the `Part::Spline` subclass), therefore it shares all the latter\'s properties.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

In addition to the properties described in [Part Feature](Part_Feature.md), the Surface Blend Curve has the following properties in the [property editor](Property_editor.md).


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

### Data


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">


{{TitleProperty|Blend Curve}}


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-    **Start Edge|LinkSub**: First input edge.

-    **Start Continuity|Integer**: Geometric continuity value

-    **Start Parameter|Float**: Normalized parameter along edge; from {{Value|0.0}}(edge start) to {{Value|1.0}}(edge end).

-    **Start Size|Float**: Size of the tangent.

-    **End Edge|LinkSub**: Second input edge.

-    **End Continuity|Integer**: Geometric continuity value

-    **End Parameter|Float**: Normalized parameter along edge; from {{Value|0.0}}(edge start) to {{Value|1.0}}(edge end).

-    **End Size|Float**: Size of the tangent.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

### View


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">


{{TitleProperty|Base}}


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-    **Control Points|Bool**: it defaults to `False`; if set to `True`, it will show an overlay with the control points of the curve.


</div>



## Tworzenie skryptów 


**Zobacz również:**

[FreeCAD podstawy tworzenia skryptów](FreeCAD_Scripting_Basics/pl.md).


<div lang="en" dir="ltr" class="mw-content-ltr">

The Blend Curve tool can be used in [macros](Macros.md) and from the [Python](Python.md) console by adding the `Surface::FeatureBlendCurve` object.

-   The edges to be used to define the curve must be assigned as [LinkSub](LinkSub.md) to the `StartEdge` and `EndEdge` properties of the object.
-   All objects with edges need to be computed before they can be used as input for the properties of the Blend Curve object.


</div>


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

points1 = [App.Vector(-20, -20, 0), App.Vector(-20, -8, 0), App.Vector(-17, 7, 0), App.Vector(-18, 25, 0)]
obj1 = Draft.make_bspline(points1)

points2 = [App.Vector(60, 26, 0), App.Vector(37, 4, 0), App.Vector(33, -20, 0)]
obj2 = Draft.make_bspline(points2)

doc.recompute()

bcurve = doc.addObject("Surface::FeatureBlendCurve","BlendCurve")
bcurve.StartEdge = (obj1, 'Edge1')
bcurve.EndEdge = (obj2, 'Edge1')
bcurve.EndParameter = 1.00
bcurve.StartSize = -5.00
bcurve.EndSize = -5.00

doc.recompute()
```





{{Surface Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [Surface](Surface_Workbench.md) > Surface BlendCurve/pl
